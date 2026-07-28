<!-- ============================================================
  Profile README — lives in the repo FryFr/FryFr as README.md
  Companion files:
    · header.svg  → commit to  assets/header.svg  (same repo)
    · snake.yml   → commit to  .github/workflows/snake.yml
  Only pending TODO: the Platica live-site link (search "TODO").
  TikTok badge is commented out — enable it when the account exists.
  If you ever rename your GitHub handle, find & replace "FryFr"
  in the stats/snake URLs below.
============================================================ -->

<div align="center">

<img src="assets/header.svg" width="880" alt="Terminal boot sequence — robotics, software, infra, AI automation. Mission: automate everything." />

<a href="https://www.linkedin.com/in/jsilva-medina/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="https://www.youtube.com/@zicamtech"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"/></a>
<a href="https://portfolio-juan-silva-eight.vercel.app/en"><img src="https://img.shields.io/badge/Portfolio-238636?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"/></a>
<!-- TikTok badge pending: add it when the account exists -->
<!-- <a href="#"><img src="https://img.shields.io/badge/TikTok-010101?style=for-the-badge&logo=tiktok&logoColor=white" alt="TikTok"/></a> -->

</div>

## $ whoami

```console
juan@bogota:~$ whoami
Mechatronics engineer · Bogotá, Colombia
Business Systems & AI Specialist @ industrial manufacturing (remote)

juan@bogota:~$ cat mission.txt
Automate everything — from a company's processes to my own life.
Robotics, AI and software. Built in public.
```

By day I design AI automations, self-hosted infrastructure and AI adoption programs for an industrial manufacturer. By night I build robots, physical AI assistants and products of my own. Next stop: a robotics & automation master's in Spain.

## $ cat architecture.txt

Four stacked layers that rarely live in the same engineer — the intersection is the whole point:

```text
                 ┌───────────────────────────────┐
                 │        MISSION CONTROL        │
                 │      automate everything      │
                 └───────────────┬───────────────┘
                                 │
        ┌────────────────┬───────┴────────┬────────────────┐
        │                │                │                │
  ┌─────┴─────┐    ┌─────┴─────┐    ┌─────┴─────┐    ┌─────┴─────┐
  │ ROBOTICS  │    │    AI     │    │ SOFTWARE  │    │   INFRA   │
  ├───────────┤    ├───────────┤    ├───────────┤    ├───────────┤
  │ ESP32     │    │ n8n       │    │ Python    │    │ Docker    │
  │ STM32     │    │ agents    │    │ TypeScript│    │ VPS · VPN │
  │ ROS       │    │ LLM + OCR │    │ FastAPI   │    │ self-host │
  └─────┬─────┘    └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
        │                │                │                │
        └────────────────┴────────┬───────┴────────────────┘
                                  ▼
                    ┌──────────────────────────┐
                    │  systems that run alone  │
                    └──────────────────────────┘
```

## $ systemctl status projects

|     | Project | What it is | Stack | Signal |
|-----|---------|------------|-------|--------|
| 🟢 | **Platica** <!-- TODO: link to live site --> | WhatsApp bot comparing grocery prices **per unit** across Colombian chains | Python · TypeScript · PostgreSQL · OCR | 241,000+ price points · 8 chains · 4 cities |
| 🟢 | **[Milu](https://miluprana.com)** | Premium e-commerce for a physical product, built end-to-end | React 19 · Supabase · MercadoPago | live & selling · 84 unit + 24 E2E tests |
| 🟡 | **[Michibot](https://portfolio-juan-silva-eight.vercel.app/en/projects/michibot)** <!-- swap to repo link when public --> | Desktop robot with a conversational voice assistant, Spanish-first | FastAPI · ESP32-S3 · STT/LLM/TTS | first word in **< 900 ms** |
| 🔒 | [Logistics control tower](https://portfolio-juan-silva-eight.vercel.app/en/projects/dynapro-tracking) | AI reads dispatch emails, validates against the ERP, tracks every shipment | n8n · React · Firebase | replaced a 26-column manual spreadsheet |
| 🔒 | Commissions engine | Deterministic rules engine for sales commissions | Next.js · Supabase · n8n | replaced a manual Excel process |
| 🎓 | [6-DoF robotic arm](https://portfolio-juan-silva-eight.vercel.app/en/projects/robotic-arm) | SolidWorks → URDF → ROS → physical build | ROS · control theory | university flagship |

<div align="center">

`🟢 in production` · `🟡 building now` · `🔒 private (work)` · `🎓 university archive`

</div>

> The systems I build at work run behind closed doors — the engineering lessons don't. Incidents, postmortems and architecture decisions get shared in public.

## $ htop

<!-- No top-languages card on purpose: it would read the old university
     repos and say "Dart & C++", which misrepresents the current stack. -->

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=FryFr&show_icons=true&hide_border=true&bg_color=0d1117&title_color=3fb950&icon_color=58a6ff&text_color=c9d1d9&include_all_commits=true&count_private=true" alt="GitHub stats"/>
<img height="170" src="https://streak-stats.demolab.com?user=FryFr&hide_border=true&background=0d1117&ring=3fb950&fire=d29922&currStreakLabel=3fb950&currStreakNum=e6edf3&sideNums=e6edf3&sideLabels=8b949e&dates=8b949e&stroke=30363d" alt="Contribution streak"/>

<img width="92%" src="https://github-readme-activity-graph.vercel.app/graph?username=FryFr&hide_border=true&bg_color=0d1117&color=8b949e&line=3fb950&point=58a6ff&area=true&area_color=238636" alt="Contribution activity graph"/>

<!-- Generated by .github/workflows/snake.yml — run the workflow once (Actions tab) before this renders -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/FryFr/FryFr/output/snake-dark.svg">
  <img alt="Snake eating the contribution graph" src="https://raw.githubusercontent.com/FryFr/FryFr/output/snake.svg" width="92%">
</picture>

</div>

## $ ping juan

Open to interesting problems in AI automation and robotics. If you want your company's processes to run themselves — or just want to talk robots — reach out:

<div align="center">

<a href="https://www.linkedin.com/in/jsilva-medina/"><img src="https://img.shields.io/badge/Let%27s_talk-LinkedIn-0A66C2?style=for-the-badge" alt="LinkedIn"/></a>
<a href="https://wa.me/573161309551?text=Hola%20Juan%2C%20vi%20tu%20GitHub%20y%20quiero%20hablar%20de%20automatizaci%C3%B3n."><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>

</div>

---

<div align="center">

`[ STATUS: BUILDING IN PUBLIC — incidents and postmortems included ]`

</div>
