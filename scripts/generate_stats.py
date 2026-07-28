#!/usr/bin/env python3
"""
Generates assets/stats.svg — a terminal-style GitHub stats panel.

Runs inside GitHub Actions (see .github/workflows/stats.yml) with the
default GITHUB_TOKEN. No third-party services, no rate-limit roulette.

Local preview without a token:  python3 generate_stats.py --mock
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

USER = os.environ.get("GH_USER", "FryFr")
OUT = os.environ.get("STATS_OUT", "assets/stats.svg")

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(privacy: PUBLIC, first: 100, ownerAffiliations: OWNER, isFork: false) {
      totalCount
      nodes { stargazerCount }
    }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_stats():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set (or use --mock for a local preview)")
    body = json.dumps({"query": QUERY, "variables": {"login": USER}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": f"{USER}-profile-stats",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    if "errors" in data:
        sys.exit(f"GraphQL errors: {data['errors']}")
    user = data["data"]["user"]
    days = [
        d
        for w in user["contributionsCollection"]["contributionCalendar"]["weeks"]
        for d in w["contributionDays"]
    ]
    days.sort(key=lambda d: d["date"])
    counts = [d["contributionCount"] for d in days]
    return {
        "total": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "repos": user["repositories"]["totalCount"],
        "stars": sum(n["stargazerCount"] for n in user["repositories"]["nodes"]),
        "followers": user["followers"]["totalCount"],
        "counts": counts,
    }


def mock_stats():
    counts = [0] * 335 + [0, 1, 0, 2, 0, 0, 3, 1, 0, 0, 4, 2, 7, 13, 4, 1, 0, 2, 5, 6, 3, 0, 1, 2, 4, 6, 2, 1, 3, 5]
    return {"total": 305, "repos": 22, "stars": 2, "followers": 2, "counts": counts}


def streaks(counts):
    current = 0
    for c in reversed(counts if counts[-1] > 0 else counts[:-1]):
        if c > 0:
            current += 1
        else:
            break
    longest = run = 0
    for c in counts:
        run = run + 1 if c > 0 else 0
        longest = max(longest, run)
    return current, longest


def line(label, value, suffix=""):
    dots = "." * max(2, 27 - len(label))
    return label, dots, value, suffix


def render(s):
    current, longest = streaks(s["counts"])
    last30 = s["counts"][-30:]
    peak = max(max(last30), 1)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    rows = [
        line("contributions[365d]", f"{s['total']:,}"),
        line("current_streak", str(current), f" days   (longest: {longest})"),
        line("public_repos", str(s["repos"])),
        line("stars · followers", f"{s['stars']} · {s['followers']}"),
    ]

    text_rows = ""
    y = 112
    for label, dots, value, suffix in rows:
        text_rows += (
            f'  <text class="mono" x="36" y="{y}" font-size="14" fill="#8b949e">{label} '
            f'<tspan fill="#30363d">{dots}</tspan> '
            f'<tspan fill="#e6edf3" font-weight="bold">{value}</tspan>'
            f'<tspan fill="#8b949e">{suffix}</tspan></text>\n'
        )
        y += 27

    # sparkline: last 30 days, 8px bars, 4px gaps, baseline y=170, max height 60
    bars = ""
    x0, baseline, maxh = 470, 172, 60
    for i, c in enumerate(last30):
        x = x0 + i * 12
        if c == 0:
            h, fill = 2, "#21262d"
        else:
            h = max(4, round(c / peak * maxh))
            fill = "#3fb950"
        bars += f'  <rect x="{x}" y="{baseline - h}" width="8" height="{h}" rx="1.5" fill="{fill}"/>\n'

    return f"""<svg width="880" height="250" viewBox="0 0 880 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="GitHub stats: {s['total']} contributions in the last year, {current}-day current streak, {s['repos']} public repos.">
  <title>stats — refreshed daily</title>
  <style>
    .mono {{ font-family: 'Courier New', 'SFMono-Regular', Consolas, Menlo, monospace; }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
  </style>
  <rect x="16" y="16" width="848" height="218" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="1.5"/>
  <defs>
    <pattern id="sgrid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#21262d"/>
    </pattern>
  </defs>
  <rect x="17" y="53" width="846" height="180" fill="url(#sgrid)" opacity="0.5"/>
  <line x1="17" y1="52" x2="863" y2="52" stroke="#30363d" stroke-width="1"/>
  <circle cx="38" cy="34" r="6" fill="#f85149"/>
  <circle cx="58" cy="34" r="6" fill="#d29922"/>
  <circle cx="78" cy="34" r="6" fill="#3fb950"/>
  <text class="mono" x="440" y="39" font-size="13" fill="#8b949e" text-anchor="middle">juan@bogota:~/stats</text>

  <text class="mono" x="36" y="84" font-size="14" fill="#c9d1d9"><tspan fill="#3fb950">$</tspan> ./stats --refresh daily</text>
{text_rows}
  <rect class="cursor" x="36" y="216" width="9" height="16" fill="#3fb950"/>
  <text class="mono" x="52" y="228" font-size="11" fill="#8b949e">updated: {today}</text>

  <text class="mono" x="470" y="96" font-size="12" fill="#8b949e">last_30_days</text>
  <text class="mono" x="826" y="96" font-size="11" fill="#8b949e" text-anchor="end">peak: {peak}/day</text>
{bars}
  <line x1="470" y1="174" x2="826" y2="174" stroke="#30363d" stroke-width="1"/>
  <text class="mono" x="470" y="192" font-size="10" fill="#484f58">-30d</text>
  <text class="mono" x="826" y="192" font-size="10" fill="#484f58" text-anchor="end">today</text>
</svg>
"""


def main():
    s = mock_stats() if "--mock" in sys.argv else fetch_stats()
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w") as f:
        f.write(render(s))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
