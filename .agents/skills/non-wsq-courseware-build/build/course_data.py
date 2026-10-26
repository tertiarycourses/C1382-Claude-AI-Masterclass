"""
SINGLE SOURCE OF TRUTH — Claude AI Masterclass (C1382), v5.0.

Everything (PPT, Lesson Plan, Learner Guide, labs, prompts page) is generated
from this file plus data_domain1..3.py, so the artifacts can never drift apart.

v5.0 replaces the finance scenario with one marketing launch that runs inside a
single Claude Project from Lab 1 onwards: the project's lead agent (the
coordinator) splits each job into parallel threads, one per subject, and every
lab adds to the same project — research, artefacts, connectors, skills, social
posts, video and scheduled work.

Design: the Claude Style house look shared with the Claude Code Masterclass
(C1417) — terracotta accent, Cambria headings, white cards.

NON-WSQ: no assessment, no funding content, no attendance rules. Learning is
reinforced through the labs and a recap per topic.
"""

import os, copy

# ------------------------------------------------------------------ edition
# Two editions build from this one source (see edition_classic.py):
#   classic  Projects as most accounts show them — Instructions, Context, Folder,
#            Scheduled. The default, and the edition published to Drive and the LMS.
#   threads  the redesigned Projects beta — a lead agent and parallel threads.
# Select with COURSE_EDITION=classic|threads.
EDITION = os.environ.get("COURSE_EDITION", "classic")
if EDITION not in ("classic", "threads"):
    raise SystemExit(f"COURSE_EDITION must be classic or threads, not {EDITION!r}")
THREADS = EDITION == "threads"
EDITION_LABEL = "Threads Edition"

# ------------------------------------------------------------------ metadata
TITLE        = "Claude AI Masterclass"
SHORT_TITLE  = "Claude AI Masterclass - Threads Edition" if THREADS else "Claude AI Masterclass"
COURSE_CODE  = "C1382"
VERSION      = "v5.1"
VERSION_DATE = "27 October 2026"
TAGLINE      = "Projects, threads, artefacts, connectors, skills and content — for marketing teams"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
TRAINER_ROLE = "AI Trainer & Engineer"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"
REGISTRATION = "https://www.tertiarycourses.com.sg/claude-ai-masterclass.html"
REPO_URL     = "https://github.com/tertiarycourses/C1382-Claude-AI-Masterclass"
PAGES_URL    = "https://tertiarycourses.github.io/C1382-Claude-AI-Masterclass/"
PROMPTS_URL_CLASSIC = PAGES_URL + "prompts/"
PROMPTS_URL_THREADS = PAGES_URL + "prompts/threads/"
PROMPTS_URL  = PROMPTS_URL_THREADS if THREADS else PROMPTS_URL_CLASSIC

# Where this edition's outputs go, relative to the repo root. The classic edition
# keeps the plain paths, which are the ones the Drive and LMS pushes read.
COURSEWARE_SUBDIR = "courseware/threads-edition" if THREADS else "courseware"
LABS_SUBDIR       = "labs-threads" if THREADS else "labs"
PROMPTS_SUBDIR    = "docs/prompts/threads" if THREADS else "docs/prompts"

# ------------------------------------------------------------------ scenario
# ONE fictitious brand runs through every lab, so each lab builds on the last.
COMPANY       = "Lumo Kopi Co."
COMPANY_SHORT = "Lumo Kopi"
PROJECT_NAME  = "Lumo Cold Kopi Launch"
COMPANY_BLURB = (
    "Lumo Kopi Co. is a fictitious Singapore coffee brand about to launch Lumo Cold "
    "Kopi — a ready-to-drink oat-milk kopi cold brew in a 240 ml can — in Singapore "
    "on 1 December 2026 and Kuala Lumpur in January 2027. You are its marketing team. "
    "All brands, figures, survey answers and documents in this course are synthetic "
    "and used for training only."
)

# The story every lab belongs to, shown at the top of the prompts page, the
# lab PDFs and the Learner Guide. Each lab adds one chapter to it.
COURSE_SCENARIO = dict(
    title="The Lumo Cold Kopi launch",
    situation=(
        "It is late October 2026. Lumo Kopi Co. launches Lumo Cold Kopi, its first "
        "ready-to-drink canned kopi, in Singapore on 1 December — six weeks away — and in "
        "Kuala Lumpur in January. The marketing team is small, the budget is S$60,000, and "
        "nothing has been produced yet: no research, no deck, no posts, no video."
    ),
    role=(
        "You are the Lumo marketing team. Instead of juggling a dozen separate chats, you "
        "run the whole launch from one Claude Project. Its lead agent plans each job, "
        "starts parallel threads for the pieces, and brings the results back for you to "
        "check and approve."
    ),
    mission=(
        "By the end of the day the project holds everything the launch needs — verified "
        "market research, a dashboard, a deck and brief, a brand-voice skill, two weeks "
        "of social posts, a launch video — and scheduled tasks that keep it moving while "
        "you are away."
    ),
)

# The figures the labs quote. build_mockdata.py generates the data FROM these and
# asserts them, so a check step can never disagree with the file it checks.
FACTS = dict(
    product="Lumo Cold Kopi",
    can_ml=240,
    sugar_g=5,
    price_can="S$3.90",
    price_pack="S$42.00",           # 12-pack
    launch_sg="1 December 2026",
    launch_kl="15 January 2027",
    campaign="Kopi, Chilled Right",
    hashtags=["#LumoKopi", "#KopiChilledRight"],
    # Consumer survey (lumo-consumer-survey-2026.csv)
    survey_n=400, survey_sg=240, survey_kl=160,
    age_bands=[("18-24", 88), ("25-34", 152), ("35-44", 96), ("45+", 64)],
    likely_to_buy=248,               # purchase_intent 4 or 5 -> 62%
    likely_25_34=112,                # of 152 -> 74%
    pay_350_plus=228,                # willing to pay >= S$3.50 -> 57%
    channels=[("Instagram", 136), ("TikTok", 104), ("Friends & family", 72),
              ("Shopee / Lazada", 48), ("Other", 40)],
    drivers=[("Taste", 124), ("Less sugar", 108), ("Price", 72),
             ("Convenience", 60), ("Sustainability", 36)],
    # Competitors (lumo-competitors.csv) — all fictional
    competitors=[("Kopi Kaki Cold", 3.20), ("Daily Grind RTD", 3.70), ("Frostbean", 4.20),
                 ("OatRush", 4.40), ("ChillBrew Co.", 4.80), ("Northpoint Cold Brew", 5.60)],
    competitor_median="S$4.30",
    # Launch budget — the Drive sheet and the brief deliberately disagree on two lines
    budget_total="S$60,000",
    budget_sheet=[("Instagram", 18000), ("TikTok", 15000), ("Influencers", 12000),
                  ("Google Search", 8000), ("Shopee / Lazada ads", 7000)],
    budget_brief=[("Instagram", 20000), ("TikTok", 15000), ("Influencers", 10000),
                  ("Google Search", 8000), ("Shopee / Lazada ads", 7000)],
    top_trend="Taste tests and first-sip reactions",
    social_posts=10,                 # weekdays 1-14 December 2026
)

BRAND_COLOURS = [("Kopi Brown", "#5B3A29"), ("Oat Cream", "#F3E9DC"),
                 ("Lumo Teal", "#1F8A8A"), ("Sunrise Orange", "#F28C38")]

# Lab folder slugs, keyed by lab number: labs/lab-NN-<slug>/
LAB_SLUGS = {
    1: "set-up-the-launch-project",
    2: "market-research-threads",
    3: "market-insights-artefact",
    4: "connect-drive-and-gmail",
    5: "launch-deck-and-brief",
    6: "brand-voice-skill",
    7: "marketing-plugin",
    8: "social-posts-threads",
    9: "launch-video",
    10: "schedule-and-review",
}

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Set up a Claude Project with a goal, instructions, context and memory, and explain how its lead agent splits work into parallel threads.",
    "LO2: Run multi-subject market research as parallel threads and consolidate it into one verified research brief.",
    "LO3: Build, refine, save and download a Live Artefact dashboard from supplied research data.",
    "LO4: Connect Google Drive and Gmail so Claude reads campaign files and sends an approved summary.",
    "LO5: Produce a launch deck and a campaign brief with Claude's Slides and Docs, using built-in skills.",
    "LO6: Capture a brand voice as an Agent Skill with /skill-creator, and install and use a marketing plugin.",
    "LO7: Create a two-week, multi-platform set of social media posts in parallel threads using the brand-voice skill.",
    "LO8: Produce a short vertical launch video from a script, storyboard and supplied brand assets.",
    "LO9: Schedule recurring project tasks, maintain project memory and review thread usage, keeping a human approval step.",
]
LO_TITLES = [
    "Set up the Project", "Research in threads", "Build a Live Artefact",
    "Connect Drive and Gmail", "Slides and Docs", "Skills and plugins",
    "Social posts in threads", "Make a launch video", "Schedule and review",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="Claude Projects and Market Research",
         subtitle="The Claude family · the new Projects · lead agent and threads · market research · Live Artefacts",
         agenda=["The Claude family and setup", "Projects: goal, instructions, context, memory",
                 "Lead agent and parallel threads", "Market research and Live Artefacts"],
         concepts=[
            ("Claude Project", "A home for a long-running goal. Context, memory and work build up over time instead of resetting each chat."),
            ("Lead agent", "The project's coordinator. You tell it the goal; it plans, splits the work and reports back."),
            ("Threads", "Parallel workers the lead agent starts — one per subject — each with its own focused context."),
            ("Goal", "One clear statement of what the project must achieve. Every decision the lead agent makes points at it."),
            ("Instructions vs memory", "Instructions are the rules you write. Memory is what the project learns and keeps — and you can edit it."),
            ("Live Artefacts", "Interactive tools — dashboards, trackers — that persist in your workspace instead of scrolling away in chat."),
         ]),
    dict(num=2, code="02",
         title="Connectors, Skills and Plugins",
         subtitle="Google Drive and Gmail · the context window · Slides and Docs · Agent Skills · plugins and mods",
         agenda=["Connectors: Drive and Gmail", "Context window housekeeping",
                 "Slides, Docs and built-in skills", "Agent Skills, plugins and mods"],
         concepts=[
            ("Connectors", "Toggle Gmail, Drive and Calendar on from the + menu so Claude can reach data outside the chat."),
            ("Scope the folder", "Point Claude at one Drive folder for the task — not your whole Drive."),
            ("Approval to send", "Claude drafts, sends and replies in Gmail — sending asks for explicit approval by default."),
            ("Slides and Docs", "Claude's own deck and document formats: shareable, editable, and downloadable as PowerPoint, Word or PDF."),
            ("Agent Skills", "A folder of instructions Claude loads on demand, so a task runs the same way every time."),
            ("/skill-creator", "Do the task once, verify the output, then let skill-creator write the SKILL.md for you."),
            ("Plugins", "A bundle somebody else packaged — several skills plus the tools they need, installed in one click."),
            ("Mods", "Changes to Claude's own interface or behaviour — a side panel, a status line, a slash command or a hook."),
         ]),
    dict(num=3, code="03",
         title="Content Production and Scheduled Work",
         subtitle="Social posts in parallel threads · a launch video · scheduled tasks · memory and usage",
         agenda=["One thread per channel", "Social post specs and brand checks",
                 "Script, storyboard, render: the video pipeline", "Scheduled tasks, memory and usage"],
         concepts=[
            ("One thread per channel", "The lead agent gives Instagram, TikTok, LinkedIn and Facebook a thread each, then merges one calendar."),
            ("Skill inside a thread", "Every thread loads the same brand-voice skill, so four channels still sound like one brand."),
            ("Video as code", "Claude writes and runs the code that turns a storyboard and your images into an MP4."),
            ("Scheduled tasks", "A prompt that runs on a timetable inside the project — daily, weekly or monthly — while you are away."),
            ("Approval stays human", "A scheduled task drafts and emails the post to you. Publishing is still your click."),
            ("Usage per thread", "Project settings show the tokens the lead agent and each thread used — the cost of parallel work."),
         ]),
]

DAY_THEMES = {1: "From a blank project to a researched, branded, scheduled product launch"}

# ------------------------------------------------------------------ schedule
def _SCHEDULE_BASE(lab_titles):
    """The one-day timetable, 9:00–18:00.

    Lunch is fixed at 12:30–13:30 and both tea breaks are 15 minutes. 315 of the
    day's 540 minutes are lab minutes: theory is taught in short blocks placed
    immediately before the lab that uses it.

    Rows must stay contiguous — each start equals the previous end, and the
    duration must equal end minus start. Consumers split the day at lunch by
    comparing times NUMERICALLY (see _mins in build_slides.py); never compare
    "9:00" and "12:30" as strings.
    """
    return {
     1: (DAY_THEMES[1], [
        ("9:00", "9:20",  20, "admin", "Welcome, introductions and ground rules"),
        ("9:20", "9:55",  35, "topic", "Topic 1 — Claude Projects and Market Research: the Claude family, setup, the new Projects, lead agent and threads, goal, instructions, context and memory"),
        ("9:55", "10:20", 25, "lab",   "Hands-on: " + lab_titles([1])),
        ("10:20","10:35", 15, "break", "Tea break"),
        ("10:35","11:15", 40, "lab",   "Hands-on: " + lab_titles([2])),
        ("11:15","11:25", 10, "topic", "Topic 1 — Live Artefacts: what they are, the sandbox, saving and downloading"),
        ("11:25","12:05", 40, "lab",   "Hands-on: " + lab_titles([3])),
        ("12:05","12:30", 25, "topic", "Topic 2 — Connectors, Skills and Plugins: connectors, Drive scope, Gmail approval and the context window"),
        ("12:30","13:30", 60, "lunch", "Lunch break"),
        ("13:30","14:05", 35, "lab",   "Hands-on: " + lab_titles([4])),
        ("14:05","14:15", 10, "topic", "Topic 2 — Slides, Docs and Agent Skills: built-in skills, the three layers and /skill-creator"),
        ("14:15","14:45", 30, "lab",   "Hands-on: " + lab_titles([5])),
        ("14:45","15:15", 30, "lab",   "Hands-on: " + lab_titles([6])),
        ("15:15","15:30", 15, "break", "Tea break"),
        ("15:30","15:40", 10, "topic", "Topic 2 — Plugins and mods: skills versus plugins, Discover, namespaced commands"),
        ("15:40","16:00", 20, "lab",   "Hands-on: " + lab_titles([7])),
        ("16:00","16:10", 10, "topic", "Topic 3 — Content Production and Scheduled Work: threads per channel, the video pipeline, scheduled tasks"),
        ("16:10","16:45", 35, "lab",   "Hands-on: " + lab_titles([8])),
        ("16:45","17:15", 30, "lab",   "Hands-on: " + lab_titles([9])),
        ("17:15","17:45", 30, "lab",   "Hands-on: " + lab_titles([10])),
        ("17:45","18:00", 15, "recap", "Recap, your reusable launch project and Q&A"),
     ]),
    }

def SCHEDULE(lab_titles):
    """The one-day timetable for this edition (see _SCHEDULE_BASE)."""
    sched = _SCHEDULE_BASE(lab_titles)
    swaps = {} if THREADS else _CLASSIC_SCHEDULE_TEXT
    return {d: (theme, [r[:4] + (swaps.get(r[4], r[4]),) for r in rows])
            for d, (theme, rows) in sched.items()}

# ------------------------------------------------------------------ deck content
# Chat and Cowork are now one app, "Claude" — matching the Agentic AI
# Applications with Claude Code deck (v19, October 2026).
CLAUDE_PRODUCTS = [
    ("Claude (Chat + Cowork)", "Chat + Cowork in one app — web, desktop & mobile."),
    ("Claude Code",            "The agentic tool for building — terminal, IDE & web."),
    ("Claude Design",          "Polished UI, prototypes & front-end designs."),
    ("Claude for Microsoft",   "Claude inside Excel, PowerPoint, Word & Outlook."),
    ("Claude for Chrome",      "Browser agent that clicks & fills forms in Chrome."),
    ("Claude for Science",     "Speeds up research workflows for scientists and labs."),
]
CLAUDE_PRODUCTS_TIP = ("All are powered by the same Claude models — they differ in "
                       "where they run and who they're for. Projects span Claude and Claude Code.")

# Two columns now that Chat and Cowork have merged (title set in build_slides.py).
CLAUDE_THREE = [
    ("Claude (Chat + Cowork)", "Thinking and work partner — this course",
     ["Chat: ask, draft, analyse and research with web search",
      "Cowork: plans and runs multi-step tasks on your files",
      "Projects, connectors and skills: Drive, Gmail, Calendar",
      "For everyone — web, desktop and mobile apps"]),
    ("Claude Code", "Build partner",
     ["Builds software, sites and automations",
      "Runs in the terminal, VS Code, desktop app and web",
      "Edits files, runs commands and calls MCP tools",
      "Extended with CLAUDE.md, skills, sub agents and hooks"]),
]
CLAUDE_THREE_FOOT = (
    "Chat and Cowork are now one app: Claude. A marketing team works there — and a "
    "Project ties the work together around one goal."
)

# What Cowork mode — the work half of the merged Claude app — adds to a chat.
COWORK_CAPABILITIES = [
    ("Access local files", "Read, write and reorganise the folders on your computer."),
    ("Write & run code", "It writes the code a task needs — a chart, a video — and runs it for you."),
    ("Connect to tools", "Reach Google Drive, Gmail and Calendar through connectors."),
    ("Skills & plugins", "Reusable instructions it loads on demand, shareable with your team."),
    ("Agent loop", "Plan, act, check, correct — it keeps working until the task is done."),
]
COWORK_CAPABILITIES_FOOT = (
    "Together these are why Claude finishes a task instead of describing how to do it."
)

# Plan pricing — verify at claude.com/pricing before each delivery.
PRICING_INTRO = ("Projects, Cowork and Live Artefacts are features of the paid Claude "
                 "plans — the same subscription that covers Chat and Claude Code.")
PRICING_PLANS = [
    ("Pro", "$17/mo (annual) · $20 monthly. Cowork and the new Projects (beta) included."),
    ("Max", "From $100/mo — 5× or 20× more usage than Pro. Best for heavy parallel threads."),
    ("Team", "$20/seat standard · $100/seat premium. New Projects rolling out later."),
    ("Enterprise", "$20/seat + usage at API rates. Contact sales."),
]
PRICING_BAND = ("Parallel threads multiply usage: four threads cost roughly four times one chat. "
                "Watch Project settings → Usage.")
PRICING_TIP = ("A free plan is also available, but it does not include Cowork or Projects. "
               "Prices as of October 2026 — verify at claude.com/pricing.")

# Matches "A Brief History of AI, 2023–2026" in the Agentic AI Applications with
# Claude Code deck (v19).
AI_EVOLUTION = [
    ("Prompt Engineering",  "2023", "ChatGPT goes mainstream; results depend on the prompt wording."),
    ("Context Engineering", "2024", "Models call tools and MCP launches; results depend on context."),
    ("Harness Engineering", "2025", "Claude Code & Codex: systems that plan, act and check their work."),
    ("AI Agents",           "2026", "Always-on agents work 24/7 — OpenClaw, Hermes Agent, agent teams."),
]
AI_EVOLUTION_TITLE = "A Brief History of AI, 2023–2026"
AI_EVOLUTION_FOOT = ("From wording one prompt → curating context → engineering the harness → "
                     "AI agents that work around the clock.")

# Two trainer profile slides: a blank template the delivering trainer fills in,
# then Alfred's — with the Claude Certified Associate badge, as on the Agentic AI
# Applications with Claude Code deck.
TRAINER_BLANK = dict(
    name="[ Trainer Name ]",
    role="[ Title / Role ]",
    rows=[
        "Qualifications:  ____________________________________________",
        "Expertise:  _________________________________________________",
        "Experience:  ________________________________________________",
        "Contact / Profile:  __________________________________________",
    ],
    links=[],
)

TRAINER_PROFILE = dict(
    name=TRAINER,
    role=TRAINER_ROLE,
    initials="AC",          # Ang Chew Hoe — matches the linkedin.com/in/angchewhoe handle
    rows=[
        "PhD-qualified trainer specialising in AI, software engineering and developer tooling.",
        "Hands-on experience building agentic AI applications and automations with Claude.",
        "Trains professionals across Singapore on practical, project-based AI skills.",
        "Certifications: Claude Certified Associate (Foundations), PMP, AWS, Microsoft, CompTIA, CKA, CKAD.",
    ],
    links=["linkedin.com/in/angchewhoe", "github.com/alfredang"],
    # Shown under the avatar; file lives in the skill's assets/ folder.
    badge="claude-certified-associate.png",
    badge_label="Claude Certified Associate",
)

ICE_BREAKER = [
    ("Your name and role", "Which team you sit in and what you are responsible for."),
    ("Your marketing work", "One piece of content or report you produce again and again."),
    ("Your channels", "Which social platforms and tools your team actually uses."),
    ("Your goal today", "What you would most like Claude to take off your plate."),
]

GROUND_RULES = [
    ("Phones on silent", "Step out quietly if you need to take a call."),
    ("Ask as you go", "No question is too small — others usually have the same one."),
    ("Learn by doing", "Every block of theory is followed by a lab you build yourself."),
    ("Use the mock data", "Never bring real customer or personal data into a training exercise."),
    ("Check before you publish", "Approve every post and email against the source facts."),
    ("Mutual respect", "One conversation at a time; agree to disagree."),
]

COWORK_SETUP = [
    ("Install the desktop app", "Download Claude for Mac or Windows from claude.ai/download — Projects, Cowork and Live Artefacts all run there."),
    ("Sign in on a paid plan", "Use the account that has your Pro or Max subscription — the new Projects are in beta on those plans."),
    ("Find Projects", "Open Projects from the sidebar. If you cannot see it yet, the beta has not reached your account — use Cowork mode instead."),
    ("Download the lab files", "Get the course labs from the GitHub repository; each lab has a prompt PDF and a data folder."),
    ("Enable what it needs", "Turn on only the connectors a lab needs, from the + menu."),
    ("Keep the app open", "Local work stops when the app closes. Cloud environments keep going — covered in Topic 3."),
]

# ---- The new Claude Projects (redesigned September 2026) ---------------------
PROJECTS_BEFORE_AFTER = dict(
    left=("Before — one chat per job", [
        "A chat for copy, one for visuals, one for competitors.",
        "Re-explain the brand in every new chat.",
        "Copy and paste results between chats yourself.",
        "Nothing happens while your laptop is closed.",
        "You are the project manager.",
    ]),
    right=("Now — a Project with a lead agent", [
        "You state the goal once, to the lead agent.",
        "It splits the work and starts parallel threads.",
        "Each thread reports back; the lead merges the results.",
        "Goal, memory and context persist across every thread.",
        "It only comes back to you when it needs a decision.",
    ]),
)

# The project as a team: one lead agent and its threads, drawn as a container.
PROJECT_TEAM_SUBTITLE = "One goal, one lead agent, many threads"
PROJECT_TEAM_PARTS = [
    ("Lead agent", "Plans, splits\nand merges", "clay"),
    ("Thread 1", "Competitors", "violet"),
    ("Thread 2", "Customer\nsurvey", "violet"),
    ("Thread 3", "Pricing", "violet"),
    ("Thread 4", "Social\ntrends", "violet"),
    ("Memory", "Shared by\nevery thread", "amber"),
]
PROJECT_TEAM_FOOT = (
    "You talk to the lead agent. It decides how many threads a job needs, gives each a "
    "focused brief, and brings one merged answer back to you."
)

PROJECT_WHEN = [
    ("A long-running goal", "Work keeps arriving for weeks — a product launch, a channel, an app."),
    ("A job that splits", "One big job breaks into pieces that can run at once — assets, ads, competitors, email."),
    ("Lots of research", "Many subjects to look into — one thread per competitor, market or segment."),
    ("Regular check-ins", "You want to review each workstream's progress, not one long chat."),
]
PROJECT_WHEN_FOOT = "A one-off question that is done in one reply? Use an ordinary chat."

PROJECT_ANATOMY = [
    ("Goal", "What the project must achieve. The lead agent steers every decision toward it."),
    ("Instructions", "Standing rules you write: brand voice, currency, never publish without approval."),
    ("Context", "What Claude reads: files, folders, a Google Drive folder or a GitHub repository."),
    ("Memory", "What the project learns and keeps between threads. Open the memory files to edit them."),
    ("Threads", "The parallel workers the lead agent starts for each piece of a job."),
    ("Scheduled", "Tasks that run on a timetable inside the project — the daily post, the weekly report."),
]

PROJECT_DIALOG = [
    ("Name", "What you are working on — " + PROJECT_NAME + ". This is how you find it in the sidebar."),
    ("Goal", "What the project must achieve, in two or three sentences. You can type it or dictate it."),
    ("Context", "Add the brand kit files now, or a folder or Drive folder. You can skip and add them later."),
    ("Create project", "The lead agent opens, reads the goal and context, and is ready for its first job."),
]
PROJECT_DIALOG_FOOT = ("New project is at the top right of the Projects page. Instructions "
                       "and memory are edited afterwards, in Project settings.")

PROJECT_SETTINGS = [
    ("General", "The project name, the goal, and the models and effort for the lead agent and the threads."),
    ("Memory", "The project instructions and the memory files the project has written — open one to edit it."),
    ("Environment", "Local, or a cloud environment so threads keep working with your laptop closed."),
    ("Usage", "Input and output tokens, for the lead agent and for each thread separately."),
    ("Debug access", "Let another project read this one's conversations, read-only, to help diagnose a problem."),
]
PROJECT_SETTINGS_FOOT = "Open Project settings from the gear icon at the top right of the project."

PROJECT_MODELS_HEAD = ("Role", "Typical default", "Effort", "Change it when")
PROJECT_MODELS_ROWS = [
    ("Lead agent", "Opus 5.5", "Low", "It misreads your requests — raise to Medium."),
    ("Threads", "Opus 5.5", "Medium", "Research is shallow — raise; drafts are simple — lower."),
    ("Effort", "—", "Low · Medium · High", "Higher effort thinks harder and uses more of your limit."),
]
PROJECT_MODELS_FOOT = ("Defaults vary by account and change over time — read yours in "
                       "Project settings → General → Models.")

# Only the classic edition teaches what is coming (edition_classic.UPCOMING_THREADS);
# the threads edition already teaches it.
UPCOMING_THREADS = None

# Instructions, context and memory are easy to confuse — the difference matters
# for what you edit when the output is wrong.
MEMORY_CONTEXT_HEAD = ("", "Instructions", "Context", "Memory")
MEMORY_CONTEXT_ROWS = [
    ("Who writes it", "You", "You add it", "The project, as it works"),
    ("What it holds", "Rules and style", "Files and folders to read", "Facts and decisions learned"),
    ("Lumo example", "Prices in S$; no health claims", "Brand guidelines, launch brief", "Launch date moved; IG performs best"),
    ("Edit it in", "Settings → Memory", "Context panel", "Settings → Memory → memory files"),
    ("When output is wrong", "Tighten the rule", "Add the missing file", "Correct or delete the fact"),
]

PROJECT_VS_CHAT = dict(
    left=("Working in one-off chats", [
        "You re-attach the brand kit every session.",
        "Rules are restated from memory each time.",
        "Research, posts and artefacts are scattered.",
        "A colleague has to be told how you set it up.",
        "Work stops when you stop typing.",
    ]),
    right=("Working in a Claude Project", [
        "Context is added once and read by every thread.",
        "Instructions apply to every job in the project.",
        "Artefacts, skills and outputs live together.",
        "A colleague opens the project and is ready.",
        "Scheduled tasks run while you are away.",
    ]),
)

# Market research by thread — the subjects Lab 2 hands to the lead agent.
RESEARCH_THREADS = [
    ("Competitors", "Six cold-brew brands: price, pack, positioning, and the gap Lumo can own."),
    ("Customer survey", "400 respondents: who is likely to buy, why, and where they discover drinks."),
    ("Pricing", "Where S$3.90 sits against the market, and what the survey says people will pay."),
    ("Social trends", "Which content themes earn the most engagement in the category right now."),
]
RESEARCH_FOOT = ("Each thread gets one subject and its own data file. The lead agent merges "
                 "the four findings into one research brief — and flags where they disagree.")

# ---- Live Artefacts ----------------------------------------------------------
ARTEFACT_LIMITS = dict(
    left=("An artefact CAN", [
        "Run interactive code — inputs, filters, charts.",
        "Use data you gave it, or that Claude looked up while building.",
        "Keep what you type into it between sessions.",
        "Be saved, reopened and shared.",
        "Be downloaded as a file you own.",
    ]),
    right=("An artefact CANNOT", [
        "Call an external API or website — the sandbox blocks it.",
        "Load a script, font or image from another site.",
        "Reach your local files or network.",
        "Refresh third-party data on its own.",
        "So: bake the data in, or download the HTML and run it yourself.",
    ]),
)

LIVE_ARTEFACT_FLOW = [
    ("Describe", "Tell Claude the tool you want — a dashboard, tracker or planner — and what data it shows."),
    ("Generate", "Claude writes the code and renders it in the preview pane beside the chat."),
    ("Refine", "Ask for changes in plain English until the layout and figures are right."),
    ("Save", "Save it so it persists as a reusable tool, not a lost chat message."),
    ("Download", "Export a copy to file, attach or hand on to someone without Claude."),
]

ARTEFACT_VS_CHAT = dict(
    left=("A normal chat answer", [
        "A static snapshot in the conversation.",
        "Scrolls away as the chat grows.",
        "Figures are frozen at the moment they were written.",
        "You copy and paste to reuse anything.",
        "Nothing to click, filter or explore.",
    ]),
    right=("A Live Artefact", [
        "An interactive tool with its own place in the workspace.",
        "Reopenable — it stays available after the chat ends.",
        "Can refresh from connected data when reopened.",
        "Keeps what you typed into it between sessions.",
        "Clickable: filter, sort and drill into the numbers.",
    ]),
)

# ---- Connectors and context -------------------------------------------------
CONNECTOR_STEPS = [
    ("Open the + menu", "In the chat composer, click the plus sign."),
    ("Hover Connectors", "The list of available connectors appears."),
    ("Toggle Drive and Gmail", "Switch each on and sign in to your Google account."),
    ("Grant access", "Approve the permissions Google asks for — including file read access."),
    ("Name the folder", "Tell Claude which Drive folder to use for this task."),
]

CONNECTOR_CAPABILITIES = [
    ("Google Drive", "Search and read Sheets, Docs, Slides and PDFs; upload files; create folders; save Claude's output back to Drive."),
    ("Gmail", "Search and read mail, draft messages, send / reply / forward with approval, and manage labels."),
    ("Google Calendar", "View events, find availability, and create or update meetings."),
    ("Social and ads tools", "Where your workspace has them, connectors for scheduling and ad platforms reach the same way — always with approval."),
    ("Approval by default", "Claude asks for explicit approval before it sends, replies to or forwards an email."),
    ("Where to manage them", "Individually from the + menu; account-wide under Customize → Connectors."),
]

CONTEXT_WINDOW_QUOTE = (
    "The context window is all the information the model can “see” "
    "when producing a response."
)
CONTEXT_WINDOW_SEGMENTS = [
    ("System", 9.0, "ink"),
    ("Project instructions", 2.0, "amber"),
    ("Tool definitions", 2.5, "blue"),
    ("Skill definitions", 4.0, "clay"),
    ("Conversation", 6.5, "green"),
]
CONTEXT_WINDOW_FOOT = (
    "At the start of a thread only the fixed overhead is loaded — most of the "
    "window is still free."
)
CONTEXT_WINDOW_SEGMENTS_FULL = [
    ("System", 6.0, "ink"),
    ("Project instructions", 1.4, "amber"),
    ("Tool definitions", 1.6, "blue"),
    ("Skill definitions", 3.0, "clay"),
    ("Conversation", 34.0, "green"),
    ("Files read", 14.0, "violet"),
    ("Tool call results", 11.0, "sky"),
    ("Skills executed", 9.0, "blush"),
]
CONTEXT_WINDOW_FULL_FOOT = (
    "As the task runs, files, tool results and executed skills all accumulate. This is "
    "why a project splits big jobs into threads: each thread gets a fresh window."
)
CONTEXT_COMMAND_ROWS = [
    ("System prompt", "35.3k", "3.5%"),
    ("System tools", "768", "0.1%"),
    ("MCP tools", "2.6k", "0.3%"),
    ("MCP tools (deferred)", "301.7k", "30.2%"),
    ("Memory files", "81", "0.0%"),
    ("Skills", "9k", "0.9%"),
    ("Messages", "13", "0.0%"),
    ("Free space", "650.5k", "65.0%"),
]
CONTEXT_COMMAND_HEAD = ("Category", "Tokens", "Percentage")
CONTEXT_COMMAND_NOTE = (
    "In Claude Code, run /context to see this for your own session. Note how much a large set of "
    "connectors costs before you have typed anything — turn off the ones you do not need."
)
CONTEXT_ROT = [
    ("Context rot",
     "Performance degrades. Recall of specific facts gets worse, the model starts "
     "confusing similar entities, and reasoning quality drops."),
    ("Tool confusion",
     "Claude sees every tool definition. The more options competing for its attention, "
     "the more likely it picks the wrong one or fills in the wrong parameters."),
    ("Slower responses",
     "The model processes every token on every turn. A bigger context means more work "
     "per message, which means longer waits before you see a reply."),
    ("Eats up your usage faster",
     "Your entire context gets resent with each new message — so more tokens are burned "
     "per turn, and your limits are reached sooner."),
]
CONTEXT_ROT_FOOT = (
    "The fix is housekeeping: one job per thread, only the connectors you need, and "
    "only the files the job actually reads."
)
CONTEXT_LEVERS = [
    ("Conversation", "Your prompt. The messages you send, including both text and attachments."),
    ("Project context", "The files, folders and Drive folder the project reads from."),
    ("Connectors", "The connected tools Claude can pull data from, and take actions in."),
    ("Skills", "A set of instructions Claude follows for a repeatable workflow."),
    ("Instructions & memory", "Project rules you wrote, and facts the project has learned."),
]
CONTEXT_LEVERS_FOOT = (
    "Every lab today pulls one of these levers — context in Lab 1, connectors in Lab 4, "
    "skills in Labs 5–7, and memory in Lab 10."
)

# ---- Slides and Docs ---------------------------------------------------------
SLIDES_DOCS = [
    ("Slides", "A deck Claude builds and you edit in place — download as PowerPoint or PDF for the meeting."),
    ("Docs", "A living document — a campaign brief, a plan — that you and Claude edit and comment on together."),
    ("Dashboards", "A page of live numbers — the Live Artefact you build in Lab 3 is one."),
    ("Built-in skills", "Claude's pptx, docx and xlsx skills load on their own when your request needs a file."),
]
SLIDES_DOCS_FOOT = ("You never name the skill. Ask for a deck or a document; Claude picks "
                    "the format and the skill that builds it.")

# ---- Skills ------------------------------------------------------------------
SKILL_LAYERS = [
    ("Metadata", "Skill name and description.",
     "Always in context — this is all Claude sees until the skill is triggered."),
    ("Instructions", "The step-by-step workflow, written in a SKILL.md.",
     "Loaded when the skill is triggered."),
    ("Resources", "Supporting documents, templates and examples.",
     "Loaded only when the skill needs them."),
]
SKILL_ANATOMY = [
    ("Metadata — name", "A short identifier such as lumo-brand-voice. This is what you type to run it."),
    ("Metadata — description", "What the skill does and WHEN to use it. Always in context, so this is what Claude matches against your request."),
    ("Instructions (SKILL.md)", "The routine itself: tone rules, words to avoid, hashtag rules, the checks to run."),
    ("Resources", "Optional examples of on-brand and off-brand posts the instructions call on."),
]
SKILL_PROCESS = [
    ("Do", "Do the task together with Claude once, step by step."),
    ("Verify", "Review and refine until the output is right."),
    ("Save", "Turn it into a skill using the /skill-creator skill."),
    ("Update", "Refine it later and save over it — Claude confirms before replacing."),
]
SKILL_VS_PROMPT = dict(
    left=("Pasting the brand guide each time", [
        "You describe the voice again in every chat.",
        "Easy to forget a rule when you are in a hurry.",
        "Each colleague words it slightly differently.",
        "Four channels drift into four voices.",
        "Nothing to hand to a new joiner or agency.",
    ]),
    right=("A brand-voice Agent Skill", [
        "Written once in SKILL.md and loaded by name.",
        "Claude applies every rule, every time.",
        "Every thread in the project shares it.",
        "Instagram and LinkedIn still sound like one brand.",
        "Onboarding is: copy the skill folder.",
    ]),
)
SKILL_AUTOMATION = [
    ("One command", "Run the whole routine by name instead of describing it again each time."),
    ("Across your tools", "The skill decides which connectors to use — Drive, Gmail — and in what order."),
    ("A fixed structure", "It returns the same sections every run, so you can scan it in seconds."),
    ("With checks built in", "It checks claims, prices and hashtags before it hands the post back."),
    ("Still under approval", "The skill drafts and reports; publishing anything still needs you."),
    ("Shared with the team", "Everyone runs the same routine and gets the same format."),
]

# ---- Plugins and mods ---------------------------------------------------------
PLUGIN_SUBTITLE = "A shareable setup for Claude"
PLUGIN_PARTS = [
    ("Skill", "How Claude\nshould work", "violet"),
    ("Skill #2", "How Claude\nshould work", "violet"),
    ("Skill #3", "How Claude\nshould work", "violet"),
    ("Tools", "What Claude\ncan access", "amber"),
    ("Agents", "Specialist\nhelpers", "green"),
    ("Hooks", "Automated\nactions", "blush"),
]
PLUGIN_FOOT = (
    "A skill is one routine. A plugin is the whole setup — install the Marketing "
    "plugin and you get every skill, command and tool it contains."
)
MODS = [
    ("What a mod is", "A change to Claude's own interface or behaviour, rather than to the work it does."),
    ("A panel or pane", "Something that stays beside the chat and updates — a running checklist, a campaign tracker."),
    ("A status line or toast", "A small always-visible signal, such as the active project or remaining usage."),
    ("A slash command", "Your own /command that starts a routine you use often."),
    ("A hook", "An action that runs automatically on an event — for example, before Claude sends anything."),
    ("Where to find them", "Under Customize, alongside Skills, Connectors and Plugins. Ask Claude to make one for you."),
]
SKILLS_PLUGINS_MODS_HEAD = ("", "Skill", "Plugin", "Mod")
SKILLS_PLUGINS_MODS_ROWS = [
    ("Changes", "How a task is done", "A whole toolkit", "Claude's own interface"),
    ("Contains", "One SKILL.md + resources", "Skills, tools, agents, hooks", "A panel, command, hook or status line"),
    ("You get it by", "Writing it with /skill-creator", "Installing from Discover", "Asking Claude to make one"),
    ("Lumo example", "lumo-brand-voice", "Marketing plugin", "A launch-countdown panel"),
]

# ---- Content production -------------------------------------------------------
SOCIAL_SPECS = [
    ("Instagram", "Carousel or Reel. Hook in the first line; caption up to 2,200 characters; 3–5 hashtags."),
    ("TikTok", "9:16 video, 15–30 s. A hook in the first 2 seconds; on-screen text; one call to action."),
    ("LinkedIn", "Founder or team voice; the story behind the product; no more than 3 hashtags."),
    ("Facebook", "Community and offers; a clear link to buy; questions that invite comments."),
]
SOCIAL_SPECS_FOOT = "Every thread loads lumo-brand-voice, so four formats still sound like one brand."

CONTENT_THREADS_FLOW = [
    ("Brief the lead", "One message: the goal, the dates, the channels and the skill to use."),
    ("Split by channel", "The lead agent starts one thread per platform with its own spec."),
    ("Draft in parallel", "Each thread drafts its posts using the brand-voice skill."),
    ("Merge the calendar", "The lead agent merges the drafts into one dated calendar."),
    ("Check and approve", "You check claims, prices and dates before anything is scheduled."),
]

VIDEO_PIPELINE = [
    ("Script", "Five lines, three seconds each — hook, problem, product, proof, call to action."),
    ("Storyboard", "One frame per line: which image, which on-screen text, which motion."),
    ("Render", "Claude writes and runs code that animates your images and text into an MP4."),
    ("Check", "Length, size 1080 × 1920, brand colours, every claim true, end card with the price."),
    ("Refine", "Ask for timing or text changes in plain English and render again."),
]
VIDEO_SPECS = [
    ("Format", "Vertical 9:16, 1080 × 1920 pixels, MP4 — fits Reels, TikTok and Shorts."),
    ("Length", "15 seconds: five scenes of three seconds each."),
    ("Text", "Large, high-contrast captions — most people watch with the sound off."),
    ("Brand", "Lumo colours and logo; the end card shows the price and the campaign hashtag."),
    ("Assets", "Only the supplied product images — never a real person's likeness or a stock logo."),
    ("Fallback", "No video tools in the session? Claude builds an animated HTML version to screen-record."),
]

SCHEDULED_ANATOMY = [
    ("Prompt", "Exactly what to do each run — written like a lab prompt, with the checks included."),
    ("Frequency", "Daily, weekdays, weekly or monthly."),
    ("Time", "When it runs, in your time zone — for example, weekdays at 9:00am."),
    ("Where it runs", "Inside the project, so it reads the same goal, context, memory and skills."),
    ("Output", "Where the result goes — an email draft, a file in Drive, a note in the project."),
    ("Approval", "The step a human still takes — the task drafts, you publish."),
]
SCHEDULED_EXAMPLES = [
    ("Daily post, weekdays 9:00am", "Take today's row from the social calendar, polish it with lumo-brand-voice and email it to me for approval."),
    ("Weekly report, Mondays 8:00am", "Summarise last week's posts from the social calendar and anything new in the Lumo Launch Drive folder in five bullet points."),
    ("Monthly scan, 1st at 10:00am", "Check the six competitors for new products or price changes and update the research brief."),
]
SCHEDULED_FOOT = ("A local task needs the app open. To keep tasks running with the laptop "
                  "closed, give the project a cloud environment in Project settings → Environment.")

CLOUD_ENVIRONMENT = [
    ("Network access", "Which websites the threads may reach — add only the ones the work needs."),
    ("Secrets", "API keys the threads can use. Once saved, nobody can read them back — not even you."),
    ("Setup script", "What each thread installs before it starts work, such as one package-install line."),
]

RESPONSIBLE_MARKETING = [
    ("Claims you can prove", "“5 g sugar” is on the label. “Healthy” is a claim Lumo cannot substantiate — never use it."),
    ("Consent for email", "Email only people who opted in. Lab emails go to yourself, never to real customers."),
    ("No real likenesses", "Do not generate a real person, influencer or competitor logo into an ad."),
    ("Disclose partnerships", "Influencer posts are labelled as paid partnerships."),
    ("A human publishes", "Claude drafts and schedules drafts; a person approves every public post."),
    ("Keep the source", "Keep the research files, so every number in a post can be traced back."),
]

CONTROL_RULES = [
    ("Work from mock data", "Use the supplied synthetic Lumo data — never real customer records in training."),
    ("Scope the connector", "Give Claude one Drive folder for the task, not your entire Drive."),
    ("Check every figure", "Read the artefact's and the brief's numbers back against the source file."),
    ("Approve before sending", "Read each drafted email and post in full; approve it only when the facts match."),
    ("Use a test recipient", "Send class exercises to yourself, never to a real customer."),
    ("Watch thread usage", "Parallel threads multiply usage — check Project settings → Usage."),
]

NEXT_STEPS = [
    ("Start one real Project", "Give your next campaign a project with a goal, instructions and context."),
    ("Split one job into threads", "Next time you research competitors, give each one its own thread."),
    ("Capture your brand voice", "Turn your real brand guide into a skill your whole team shares."),
    ("Schedule one routine", "Pick the post or report you produce every week and schedule the draft."),
    ("Browse Discover", "See which plugins already exist before you write a skill someone has packaged."),
]

THANK_YOU = dict(
    kicker="THANK YOU FOR ATTENDING",
    headline="Your launch project is ready",
    body=("A Claude Project with a lead agent and threads, verified market research, a Live "
          "Artefact dashboard, a deck and brief, a brand-voice skill, two weeks of social posts, "
          "a launch video and the scheduled tasks that keep it all moving."),
)

# ---- Real screenshots of the Claude desktop app -------------------------------
# Captured into courseware/assets/screenshots/. A slide or LG figure is emitted
# only when its file exists, so a missing capture never ships a blank frame.
# (key, filename, title, caption, where — a lab number it precedes, or a topic tag)
SCREENSHOTS = [
    ("projects", "claude-projects.png", "The Projects Page",
     "Projects in the Claude desktop app — New project is at the top right.", "lab1"),
    ("new-project", "claude-new-project.png", "Creating a Project",
     "Name, goal and context — the three things a new project asks for.", "lab1"),
    ("project-threads", "claude-project-threads.png", "The Lead Agent and Its Threads",
     "The lead agent reports which threads it started and what each returned.", "lab2"),
    ("memory", "claude-project-memory.png", "Project Memory and Instructions",
     "Project settings → Memory: the instructions and the editable memory files.", "lab10"),
    ("connectors", "claude-connectors.png", "Customize → Connectors",
     "Google Drive and Gmail connected, with the other available connectors.", "lab4"),
    ("slides", "claude-slides.png", "Claude Slides",
     "A deck built by Claude — edit it in place or download as PowerPoint or PDF.", "lab5"),
    ("docs", "claude-docs.png", "Claude Docs",
     "A living document you and Claude edit together.", "lab5"),
    ("skills", "claude-skills.png", "Customize → Skills",
     "Your own skills, with the ones you installed from plugins.", "lab6"),
    ("plugins", "claude-plugins.png", "Customize → Plugins",
     "Browse and install plugins — the Marketing plugin is used in Lab 7.", "lab7"),
    ("mods", "claude-mods.png", "Customize → Mods",
     "Mods change Claude's own interface — panels, status lines, commands and hooks.", "lab7"),
    ("scheduled", "claude-scheduled.png", "Scheduled Tasks",
     "A recurring task: the prompt, how often it runs and when.", "lab10"),
    ("usage", "claude-project-usage.png", "Project Usage",
     "Project settings → Usage: tokens for the lead agent and each thread.", "lab10"),
]

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "Claude is no longer only a chat window. With the redesigned Claude Projects, you "
    "give a project one goal and a lead agent plans the work, splits it into parallel "
    "threads and brings the results back to you. This course teaches that way of working "
    "through one continuous marketing scenario: you are the marketing team at " + COMPANY +
    ", launching a new canned cold-brew kopi. Over ten labs, all inside one project, you "
    "research the market in parallel threads, build a Live Artefact dashboard, connect "
    "Google Drive and Gmail, produce a launch deck and campaign brief, capture the brand "
    "voice as a skill, add a marketing plugin, create two weeks of social posts and a launch "
    "video, and schedule the routine work so it runs on its own."
)
LG_INTRO2 = COMPANY_BLURB

LG_SETUP = dict(
    needs=[
        "A laptop (Mac or Windows) with the Claude desktop app installed from claude.ai/download.",
        "A Claude account on a paid plan (Pro or Max) — Projects, Cowork and Live Artefacts are paid-plan features.",
        "A Google account with Google Drive and Gmail, used for the connector labs.",
        "The course labs downloaded from " + REPO_URL + " — each lab folder holds a prompt PDF and, where needed, a data folder.",
        "The prompts page open in a browser, so you can copy each prompt with one click: " + PROMPTS_URL,
    ],
    verify_text=(
        "Open the Claude desktop app, sign in, and open Projects from the sidebar. If you "
        "can see the New project button, your account has the new Projects. If you cannot, "
        "the beta has not reached your account yet: run each lab in Cowork mode "
        "instead, and attach the lab's data files yourself — every prompt still works."
    ),
    conventions=[
        "Prompts shown in a bordered box are copied into Claude exactly as they are — or copy them from the prompts page.",
        "Placeholders such as <YOUR EMAIL> are replaced with your own values.",
        "All Lumo Kopi data is synthetic; use only the supplied mock data.",
        "Every lab ends with a check step — confirm the output before moving on.",
    ],
)

# How-to sections for the four project levers the brief asks learners to master.
# Rendered as a dedicated LG chapter, with the matching screenshot where captured.
LG_PROJECT_HOWTO = [
    dict(title="Writing the goal",
         shot="new-project",
         paras=[
             "The goal is the one statement every decision in the project points at. The lead "
             "agent reads it before it plans any job, so a vague goal produces vague plans.",
             "Write it as an outcome with a date and a measure: what will exist, for whom, and "
             "how you will know it worked. Two or three sentences is enough.",
         ],
         example=("Launch Lumo Cold Kopi in Singapore on 1 December 2026. Produce the research, "
                  "launch deck, campaign brief, two weeks of social posts and a 15-second launch "
                  "video, within a S$60,000 budget, so that 25-34 year-olds on Instagram and "
                  "TikTok know the product exists by launch day."),
         steps=[
             "Open the project and click the gear icon to open Project settings.",
             "Under General, edit the goal and save.",
             "Ask the lead agent: \"Restate the project goal in one line.\" If it gets it wrong, the goal is unclear.",
         ]),
    dict(title="Writing project instructions",
         shot="memory",
         paras=[
             "Instructions are standing rules that apply to every thread and every job in the "
             "project. Use them for things that are always true: the currency, the brand voice "
             "in brief, what must never happen without your approval.",
             "Keep them short and testable. A rule Claude can check — \"prices always in S$ with "
             "two decimals\" — works far better than a wish such as \"be professional\".",
         ],
         example=("You are the marketing team for Lumo Kopi Co.\n"
                  "- Prices are in Singapore dollars: S$3.90 per can, S$42.00 per 12-pack.\n"
                  "- Follow lumo-brand-guidelines.md for anything customer-facing.\n"
                  "- Never describe the product as healthy; you may say 5 g sugar.\n"
                  "- Never send an email or publish a post without my approval.\n"
                  "- Save outputs to the project folder with the date in the filename."),
         steps=[
             "Open Project settings and choose Memory.",
             "Paste the instructions into Project instructions and save.",
             "Start a new job and check that the rules are followed without you repeating them.",
         ]),
    dict(title="Adding context",
         shot="new-project",
         paras=[
             "Context is what the project reads: the brand guidelines, the product sheet, the "
             "launch brief. Claude reads context but does not edit it, so it is the right home "
             "for reference material you want kept exactly as it is.",
             "Add only what the work needs. Every file in context competes for space in each "
             "thread's context window, so a lean set of reference files gives sharper answers "
             "than a whole shared drive.",
         ],
         example=None,
         steps=[
             "In the project, open the Context panel and choose Add.",
             "Add files, a folder from your computer, or a Google Drive folder.",
             "Ask: \"Which context files do you have, and what is each one for?\"",
         ]),
    dict(title="Working with memory",
         shot="memory",
         paras=[
             "Memory is what the project writes down for itself as it works: decisions you made, "
             "facts it discovered, what performed well. Every thread can read it, which is how "
             "something learned in one thread reaches the next.",
             "Because the project writes it, memory can be wrong. Open the memory files from "
             "time to time, correct anything out of date and delete anything you do not want "
             "kept. Treat it like a shared notebook that you are responsible for.",
         ],
         example=("Remember this for the project: the Singapore launch date has moved from "
                  "1 December to 8 December 2026. Update anything you have planned that depends on it."),
         steps=[
             "Open Project settings → Memory and open a memory file.",
             "Edit or delete a line, then save.",
             "Or tell the lead agent what to remember, and check the memory file afterwards.",
         ]),
    dict(title="Scheduling tasks",
         shot="scheduled",
         paras=[
             "A scheduled task is a prompt the project runs on a timetable. Because it runs "
             "inside the project, it has the goal, instructions, context, memory and skills — "
             "you do not repeat any of them in the task.",
             "Schedule drafts, not publishing. A good marketing task prepares today's post and "
             "emails it to you for approval; the click that publishes stays yours. If your "
             "workspace has a social-scheduling connector, the task can queue the approved "
             "post — still behind your approval.",
         ],
         example=("Every weekday at 9:00am: take today's row from social-calendar.csv, polish the "
                  "post with lumo-brand-voice, check every price and claim against the brand kit, "
                  "and email it to me as a draft with the subject \"Today's Lumo post\". Never "
                  "publish anything."),
         steps=[
             "In the project, ask the lead agent to schedule the task, or open Scheduled and choose New task.",
             "Set the prompt, the frequency and the time, and save.",
             "Use Run now once to test it, then check the email that arrives.",
             "For tasks that must run with your laptop closed, add a cloud environment in Project settings → Environment.",
         ]),
]

LABS_README_NOTE = (
    "All ten labs run inside **one Claude Project** — the Lumo Cold Kopi Launch project you\n"
    "create in Lab 1. Labs 2 and 8 hand a job to the project's lead agent, which splits it\n"
    "into parallel threads, one per subject.\n"
    "\n"
    "Each lab folder holds only the **prompt PDF** and, where the lab needs it, a **data/**\n"
    "folder of mock data and assets. The full step-by-step instructions and check steps are\n"
    "in the Learner Guide, and every prompt is on the copy-ready prompts page."
)

LAB_NOTE = (
    "Use only the supplied mock data and your own test accounts. Never put real "
    "customer, personal or confidential data into a training exercise, and send lab "
    "emails to yourself rather than to a real recipient."
)

LG_GLOSSARY = [
    ("Agent Skill", "A folder containing a SKILL.md of instructions that Claude loads on demand when the task matches its description."),
    ("Artefact", "A self-contained output Claude builds — a document, dashboard or tool — shown beside the chat rather than inside it."),
    ("Claude Project", "A workspace for one long-running goal, with its own instructions, context, memory, threads and scheduled tasks."),
    ("Connector", "An integration that lets Claude reach an outside service such as Google Drive, Gmail or Calendar."),
    ("Effort", "How hard a model thinks before it answers. Higher effort is more thorough and uses more of your limit."),
    ("Lead agent", "The project's coordinator: it plans each job, starts threads and merges their results. Also called the coordinator."),
    ("Live Artefact", "An artefact that persists in your workspace, keeps its state, and can refresh its data when reopened."),
    ("MCP", "Model Context Protocol — the open standard connectors use to expose tools and data to Claude."),
    ("Memory", "Facts and decisions a project writes down as it works, readable by every thread and editable by you."),
    ("Mod", "A change to Claude's own interface or behaviour, such as a side panel, status line, slash command or hook."),
    ("Plugin", "A packaged bundle of skills, tools, agents and hooks, installed in one step."),
    ("Scheduled task", "A prompt a project runs automatically on a timetable."),
    ("SKILL.md", "The Markdown file at the heart of an Agent Skill: name, description and instructions."),
    ("Thread", "One parallel worker inside a project, started by the lead agent with a focused brief and its own context window."),
]

LG_WRAPUP = dict(
    title="Wrap-Up",
    intro=("Across ten labs you took one product launch from an empty project to a "
           "researched, branded and scheduled campaign."),
    sections=[
        dict(title="What you built", bullets=[
            "The Lumo Cold Kopi Launch project, with a goal, instructions, context and memory.",
            "A market research brief built from four parallel threads, with conflicts flagged.",
            "A Market Insights Live Artefact dashboard, saved and downloaded.",
            "Google Drive and Gmail connected, with an approved summary sent to yourself.",
            "A launch deck in Slides and a campaign brief in Docs.",
            "A lumo-brand-voice Agent Skill and the Marketing plugin.",
            "Two weeks of social posts across four platforms, drafted in parallel threads.",
            "A 15-second vertical launch video.",
            "Scheduled tasks that draft the daily post and the weekly report for your approval.",
        ]),
        dict(title="The habit to keep", bullets=[
            "Give long-running work a project with a clear goal, not a string of chats.",
            "Split big jobs into threads, one subject each, and let the lead agent merge them.",
            "Check every figure and claim against the source before anything goes out.",
            "Write a routine down once as a skill instead of retyping it every time.",
            "Schedule the drafting; keep the publishing click for yourself.",
        ]),
    ],
)

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", "15 September 2026", "Initial release.", TRAINER),
    ("2.0", "15 September 2026", "Finance task automation scenarios.", TRAINER),
    ("2.1", "16 September 2026", "Eight finance labs with mock data and skills.", TRAINER),
    ("3.0", "17 September 2026",
     "Rebuilt on the Claude Style design with three topics and six labs on one "
     "fictitious finance firm; prompts added to the slides, Learner Guide and labs.", TRAINER),
    ("3.1", "17 September 2026",
     "Added an invoice-processing first lab, the context window section, the skill "
     "lifecycle and the two About the Trainer slides.", TRAINER),
    ("3.2", "18 September 2026",
     "Restructured to ten labs: connectors, a built-in skill board deck, two "
     "learner-written skills, a Claude Project and a plugin.", TRAINER),
    ("4.0", "18 September 2026", "First stable release of the ten-lab finance course.", TRAINER),
    ("4.1", "18 September 2026",
     "Lab 4: recovery step for the Google Drive connector's \"insufficient scope\" error.", TRAINER),
    ("4.2", "18 September 2026",
     "Moved the Skills vs. Plugins diagram to sit immediately before the plugin lab.", TRAINER),
    ("5.0", "27 October 2026",
     "Renamed Claude AI Masterclass and rebuilt for marketing teams on the redesigned "
     "Claude Projects: one fictitious brand launch (Lumo Kopi Co.) run in a single "
     "project across ten labs, with a lead agent and parallel threads, Live Artefacts, "
     "Drive and Gmail, Slides and Docs, skills, plugins and mods, social posts, a launch "
     "video and scheduled tasks. Lab folders now hold only the prompt PDF and data; full "
     "instructions are in the Learner Guide and every prompt is on a copy-ready prompts "
     "page. Trainer profile adds the Claude Certified Associate certification.", TRAINER),
]
VERSION_HISTORY.append(
    ("5.1", VERSION_DATE,
     "Issued in two editions from one source. The Classic Projects Edition teaches "
     "Projects as most accounts show them today — Instructions, Context, Folder and "
     "Scheduled panels, with parallel tasks started by the learner and a project memory "
     "file — and is the edition distributed to learners. The Threads Edition keeps the "
     "redesigned Projects with a lead agent and parallel threads. The prompts page adds "
     "a lab index and links the two editions; the AI history slide follows the Agentic "
     "AI Applications with Claude Code deck.", TRAINER))

# ------------------------------------------------------------------ apply edition
_CLASSIC_SCHEDULE_TEXT = {}


def apply_edition(labs):
    """Return a domain's lab list adjusted for this edition. Threads is the base
    wording, so it is returned unchanged; classic gets edition_classic's
    per-lab replacements and phrase swaps."""
    if THREADS:
        return labs
    import edition_classic as E
    out = []
    for a in labs:
        a = copy.deepcopy(a)
        over = E.LAB_OVERRIDES.get(a["num"], {})
        if "prompt_blocks" in over:
            a.pop("prompt", None); a.pop("prompt_step", None)
        a.update(copy.deepcopy(over))
        swaps = sorted(E.LAB_SWAPS.get(a["num"], []), key=lambda x: -len(x[0]))

        def _swap(v):
            if isinstance(v, str):
                for old, new in swaps:
                    v = v.replace(old, new)
                return v
            if isinstance(v, list):
                return [_swap(x) for x in v]
            if isinstance(v, tuple):
                return tuple(_swap(x) for x in v)
            if isinstance(v, dict):
                return {k: _swap(x) for k, x in v.items()}
            return v
        out.append(_swap(a) if swaps else a)
    return out


if not THREADS:
    import edition_classic as _E
    _o = copy.deepcopy(_E.OVERRIDES)
    for _num, _t in _o.pop("TOPIC_OVERRIDES").items():
        next(t for t in TOPICS if t["num"] == _num).update(_t)
    _CLASSIC_SCHEDULE_TEXT = _o.pop("SCHEDULE_TEXT")
    LG_SETUP["verify_text"] = _o.pop("LG_SETUP_VERIFY")
    _repl = _o.pop("LG_GLOSSARY_REPLACE")
    LG_GLOSSARY = [(g[0], _repl.get(g[0], g[1])) for g in LG_GLOSSARY]
    _drop = _o.pop("LG_GLOSSARY_DROP")
    LG_GLOSSARY = sorted([g for g in LG_GLOSSARY if g[0] not in _drop] + _o.pop("LG_GLOSSARY_ADD"))
    globals().update(_o)
    LAB_SLUGS.update(_E.SLUG_OVERRIDES)

