"""CLASSIC PROJECTS EDITION — overrides applied on top of course_data + data_domainN.

The course ships in two editions built from one source:

  threads  the redesigned Claude Projects (September 2026 beta): a lead agent that
           splits each job into parallel threads, Goal, editable Memory, Project
           settings, Usage and cloud environments.
  classic  the project as most accounts still see it: a Cowork project backed by a
           folder, with four panels — Instructions, Context, Folder and Scheduled —
           and no lead agent. Where the threads edition hands a job to the lead
           agent, the classic edition has the learner start the parallel tasks
           themselves, or does the job in one task.

course_data.py and the data_domainN files hold the threads wording. This module
holds only what differs for the classic edition: course-level names (OVERRIDES)
and per-lab field replacements (LAB_OVERRIDES) or phrase swaps (LAB_SWAPS). A
value of None tells a builder to leave that slide or section out.
"""

PROJECT_NAME = "Lumo Cold Kopi Launch"

OVERRIDES = dict(
    EDITION_LABEL="Classic Projects Edition",

    # What is coming to Projects — taught in the classic edition so learners
    # recognise the new screen when their account gets it. Shown as slides at the
    # end of the Topic 1 Projects block and as a section in the Learner Guide.
    UPCOMING_THREADS=dict(
        title="Coming Soon: Projects with a Lead Agent and Threads",
        intro=("Anthropic redesigned Claude Projects in September 2026. The new version is in "
               "beta, rolling out to Pro and Max accounts first — if your Projects page shows a "
               "Goal and talks about threads, you already have it."),
        features=[
            ("Lead agent", "You state a goal once; a coordinator plans the work, splits it and merges the results."),
            ("Parallel threads", "The lead agent starts one thread per subject itself — what you do by hand with tasks in Lab 2."),
            ("Goal", "One outcome statement that every decision in the project steers toward."),
            ("Project memory", "Memory the project writes and you edit in settings — replacing the memory file you keep in Lab 1."),
            ("Usage per thread", "Project settings show the tokens used by the lead agent and by each thread."),
            ("Cloud environment", "Threads keep working in the cloud with your laptop closed."),
        ],
        mapping_head=("In today's labs (classic)", "With the new Projects"),
        mapping_rows=[
            ("Lab 2: you start four tasks, then a merge task", "One message; the lead agent starts four threads and merges them"),
            ("Lab 8: one task drafts all four platforms", "One thread per platform, merged into one calendar"),
            ("lumo-project-memory.md in the folder", "Project settings → Memory, editable memory files"),
            ("Instructions panel", "Project instructions under settings, plus a Goal"),
            ("Settings → Usage for your whole plan", "Usage per thread for this project"),
        ],
        foot=("Everything you build today carries over: skills, connectors, artefacts and scheduled "
              "tasks work the same way. The Threads edition of this course runs the same ten labs "
              "on the new Projects — see the course repository."),
    ),
    TAGLINE="Projects, artefacts, connectors, skills and content — for marketing teams",

    COURSE_SCENARIO=dict(
        title="The Lumo Cold Kopi launch",
        situation=(
            "It is late October 2026. Lumo Kopi Co. launches Lumo Cold Kopi, its first "
            "ready-to-drink canned kopi, in Singapore on 1 December — six weeks away — and in "
            "Kuala Lumpur in January. The marketing team is small, the budget is S$60,000, and "
            "nothing has been produced yet: no research, no deck, no posts, no video."
        ),
        role=(
            "You are the Lumo marketing team. Instead of juggling a dozen separate chats, you "
            "run the whole launch from one Claude Project in Cowork: its instructions, brand "
            "kit and working folder are set up once, and every task you start inside it "
            "already knows the brand."
        ),
        mission=(
            "By the end of the day the project holds everything the launch needs — verified "
            "market research, a dashboard, a deck and brief, a brand-voice skill, two weeks "
            "of social posts, a launch video — and scheduled tasks that keep it moving while "
            "you are away."
        ),
    ),

    LEARNING_OUTCOMES=[
        "LO1: Set up a Claude Project in Cowork with instructions, context, a working folder and a project memory file.",
        "LO2: Run multi-subject market research as parallel tasks in one project and consolidate it into one verified research brief.",
        "LO3: Build, refine, save and download a Live Artefact dashboard from supplied research data.",
        "LO4: Connect Google Drive and Gmail so Claude reads campaign files and sends an approved summary.",
        "LO5: Produce a launch deck and a campaign brief with Claude's Slides and Docs, using built-in skills.",
        "LO6: Capture a brand voice as an Agent Skill with /skill-creator, and install and use a marketing plugin.",
        "LO7: Create a two-week, multi-platform set of social media posts using the brand-voice skill.",
        "LO8: Produce a short vertical launch video from a script, storyboard and supplied brand assets.",
        "LO9: Schedule recurring project tasks and keep the project's instructions, context and memory file current, with a human approval step.",
    ],
    LO_TITLES=[
        "Set up the Project", "Research in parallel tasks", "Build a Live Artefact",
        "Connect Drive and Gmail", "Slides and Docs", "Skills and plugins",
        "Social posts", "Make a launch video", "Schedule and review",
    ],

    # Topic 1 and Topic 3 change; Topic 2 is the same in both editions.
    TOPIC_OVERRIDES={
        1: dict(
            subtitle="The Claude family · Projects in Cowork · instructions, context and folder · market research · Live Artefacts",
            agenda=["The Claude family and setup", "Projects: instructions, context, folder, scheduled",
                    "Parallel tasks for parallel work", "Market research and Live Artefacts"],
            concepts=[
                ("Claude Project", "A home for a long-running body of work. Its rules, files and outputs build up instead of resetting each chat."),
                ("Backed by a folder", "In Cowork a project points at a real folder on your computer — Claude works there, and you can open it yourself."),
                ("Instructions", "Standing rules every task in the project follows: currency, brand voice, approval before sending."),
                ("Context vs Folder", "Context is what Claude reads and never edits. Folder is where it works — reading data and writing output."),
                ("Parallel tasks", "Several tasks can run in one project at once — one per subject — and a final task merges their files."),
                ("Live Artefacts", "Interactive tools — dashboards, trackers — that persist in your workspace instead of scrolling away in chat."),
            ]),
        3: dict(
            subtitle="Social posts for four platforms · a launch video · scheduled tasks · the memory file",
            agenda=["One prompt, four platforms", "Social post specs and brand checks",
                    "Script, storyboard, render: the video pipeline", "Scheduled tasks and the memory file"],
            concepts=[
                ("Specs per platform", "Instagram, TikTok, LinkedIn and Facebook each get their own spec in the prompt, so one task drafts all four well."),
                ("Skill in every task", "Every task loads the same brand-voice skill, so four channels still sound like one brand."),
                ("Video as code", "Claude writes and runs the code that turns a storyboard and your images into an MP4."),
                ("Scheduled tasks", "A prompt that runs on a timetable — daily, weekly or monthly — inside the project, while you are away."),
                ("Approval stays human", "A scheduled task drafts and emails the post to you. Publishing is still your click."),
                ("A memory file", "A Markdown file in the project folder that records decisions, so every later task reads the same facts."),
            ]),
    },

    PRICING_PLANS=[
        ("Pro", "$17/mo (annual) · $20 monthly. Cowork and Projects included."),
        ("Max", "From $100/mo — 5× or 20× more usage than Pro. Best for heavy parallel tasks."),
        ("Team", "$20/seat standard · $100/seat premium (5× usage)."),
        ("Enterprise", "$20/seat + usage at API rates. Contact sales."),
    ],
    COWORK_SETUP=[
        ("Install the desktop app", "Download Claude for Mac or Windows from claude.ai/download — Projects, Cowork and Live Artefacts all run there."),
        ("Sign in on a paid plan", "Use the account that has your Pro or Max subscription."),
        ("Find Projects", "Switch to Cowork and open Projects from the sidebar — each project is backed by a folder on your computer."),
        ("Download the lab files", "Get the course labs from the GitHub repository; each lab has a prompt PDF and a data folder."),
        ("Enable what it needs", "Turn on only the connectors a lab needs, from the + menu."),
        ("Keep the app open", "Tasks and local scheduled tasks stop when the app closes."),
    ],
    PROJECT_WHEN=[
        ("A long-running goal", "Work keeps arriving for weeks — a product launch, a channel, an app."),
        ("A job that splits", "One big job breaks into pieces that can run at once — assets, ads, competitors, email."),
        ("Lots of research", "Many subjects to look into — one task per competitor, market or segment."),
        ("Regular routines", "Work that repeats on a timetable — scheduled tasks that belong to the project."),
    ],
    CONTEXT_WINDOW_FOOT=(
        "At the start of a task only the fixed overhead is loaded — most of the "
        "window is still free."
    ),
    SKILL_VS_PROMPT=dict(
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
            "Every task in the project shares it.",
            "Instagram and LinkedIn still sound like one brand.",
            "Onboarding is: copy the skill folder.",
        ]),
    ),
    LG_GLOSSARY_REPLACE={
        "Claude Project": "A workspace for one long-running body of work, with its own instructions, context files, working folder and scheduled tasks.",
        "Memory": "What a project keeps between tasks. In a classic project, the memory file you ask Claude to maintain; in the new Projects, editable memory in settings.",
    },

    DAY_THEMES={1: "From a blank project to a researched, branded, scheduled product launch"},

    SCHEDULE_TEXT={
        "Topic 1 — Claude Projects and Market Research: the Claude family, setup, the new Projects, lead agent and threads, goal, instructions, context and memory":
        "Topic 1 — Claude Projects and Market Research: the Claude family, setup, Projects in Cowork, instructions, context, folder and scheduled",
        "Topic 3 — Content Production and Scheduled Work: threads per channel, the video pipeline, scheduled tasks":
        "Topic 3 — Content Production and Scheduled Work: platform specs, the video pipeline, scheduled tasks",
    },

    # ---- Projects theory, classic shape
    PROJECTS_BEFORE_AFTER=dict(
        left=("One-off chats", [
            "A chat for copy, one for visuals, one for competitors.",
            "Re-attach the brand kit every time.",
            "Restate the rules from memory each time.",
            "Outputs scattered across conversations.",
            "Nothing for a colleague to pick up.",
        ]),
        right=("A Claude Project in Cowork", [
            "Instructions written once, followed by every task.",
            "The brand kit added once as context.",
            "A real working folder Claude reads and writes.",
            "Scheduled tasks that belong to the project.",
            "Hand the folder to a colleague and they are ready.",
        ]),
    ),
    PROJECT_TEAM_SUBTITLE="A folder-backed project with four panels",
    PROJECT_TEAM_PARTS=[
        ("Instructions", "Rules every\ntask follows", "clay"),
        ("Context", "Files Claude\nreads", "violet"),
        ("Folder", "Where Claude\nworks", "violet"),
        ("Scheduled", "Tasks on a\ntimetable", "amber"),
        ("Your tasks", "Run one or\nseveral at once", "green"),
        ("Memory file", "Decisions kept\nin the folder", "amber"),
    ],
    PROJECT_TEAM_FOOT=(
        "Every task you start in the project reads its instructions, context and folder. "
        "Start several at once and they run in parallel — one task per subject."
    ),
    PROJECT_ANATOMY=[
        ("Instructions", "Standing rules you write: brand voice, currency, never publish without approval."),
        ("Context", "Documents Claude READS and never edits — the brand guidelines, product sheet and launch brief."),
        ("Folder", "A real folder on your computer where Claude WORKS: it reads the data there and writes output back."),
        ("Scheduled", "Recurring tasks that belong to this project — the daily post draft, the weekly report."),
        ("Tasks", "Each job you start in the project. Several can run at once, one per subject."),
        ("Memory file", "lumo-project-memory.md in the folder: decisions you ask Claude to record, read by every later task."),
    ],
    PROJECT_DIALOG=[
        ("What are you working on?", "The project's name — " + PROJECT_NAME + ". This is how you find it in the sidebar."),
        ("What are you trying to achieve?", "The goal in two or three sentences. Every task in the project inherits it."),
        ("Use a folder", "Point the project at a folder on your computer, so the files and outputs are yours to open."),
        ("Create project", "The project page opens with four panels: Instructions, Context, Folder and Scheduled."),
    ],
    PROJECT_DIALOG_FOOT=("Start a new project from Projects in Cowork. The instructions and context "
                         "are added afterwards, from the project page."),
    PROJECT_SETTINGS=None,
    PROJECT_SETTINGS_FOOT=None,
    PROJECT_MODELS_HEAD=None,
    PROJECT_MODELS_ROWS=None,
    PROJECT_MODELS_FOOT=None,
    MEMORY_CONTEXT_HEAD=("", "Instructions", "Context", "Memory file"),
    MEMORY_CONTEXT_ROWS=[
        ("Who writes it", "You", "You add it", "Claude, when you ask it to"),
        ("What it holds", "Rules and style", "Files to read", "Decisions and facts to keep"),
        ("Lumo example", "Prices in S$; no health claims", "Brand guidelines, launch brief", "Launch date moved to 8 December"),
        ("Edit it in", "The Instructions panel", "The Context panel", "lumo-project-memory.md in the folder"),
        ("When output is wrong", "Tighten the rule", "Add the missing file", "Correct the line in the file"),
    ],
    PROJECT_VS_CHAT=dict(
        left=("Working in one-off chats", [
            "You re-attach the brand kit every session.",
            "Rules are restated from memory each time.",
            "Research, posts and artefacts are scattered.",
            "A colleague has to be told how you set it up.",
            "Work stops when you stop typing.",
        ]),
        right=("Working in a Claude Project", [
            "Context is added once and read by every task.",
            "Instructions apply to every task in the project.",
            "Outputs land together in the project folder.",
            "A colleague opens the folder and is ready.",
            "Scheduled tasks run while you are away.",
        ]),
    ),
    RESEARCH_THREADS=[
        ("Task 1 — Competitors", "Six cold-brew brands: price, pack, positioning, and the gap Lumo can own."),
        ("Task 2 — Customers", "400 survey respondents: who is likely to buy, why, and where they discover drinks."),
        ("Task 3 — Pricing", "Where S$3.90 sits against the market, and what the survey says people will pay."),
        ("Task 4 — Social trends", "Which content themes earn the most engagement in the category right now."),
    ],
    RESEARCH_FOOT=("Start four tasks in the project at once, one subject each, each saving its own "
                   "file to the folder. A fifth task merges them into the research brief."),
    CONTENT_THREADS_FLOW=[
        ("Brief once", "One prompt: the dates, the four platforms, the spec for each and the skill to use."),
        ("Draft by platform", "Claude works through each platform's posts to its own spec."),
        ("Check the voice", "The brand-voice skill runs its checklist on every post."),
        ("Save the calendar", "The posts land in one dated calendar file in the project folder."),
        ("Check and approve", "You check claims, prices and dates before anything is scheduled."),
    ],
    SOCIAL_SPECS_FOOT="Every post loads lumo-brand-voice, so four formats still sound like one brand.",
    SCHEDULED_ANATOMY=[
        ("Name", "What the task is called in the Scheduled list — for example, Today's Lumo post."),
        ("Instructions", "Exactly what to do each run — written like a lab prompt, with the checks included."),
        ("Project", "Pick the Lumo Cold Kopi Launch project, so the task reads its instructions, context and folder."),
        ("Frequency", "Daily, weekdays, weekly or monthly. The default is Manual — change it."),
        ("Permissions", "Defaults to Automatically approve: the task acts unattended, so it must only draft."),
        ("Require this computer", "On: runs only while your computer is awake, with your folders. Off: runs without them."),
    ],
    SCHEDULED_FOOT=("Open Scheduled tasks from the sidebar (or the project's Scheduled panel), choose "
                    "New task and Set up manually. A task with Permissions on Automatically approve must only draft."),
    CLOUD_ENVIRONMENT=None,

    CONTEXT_WINDOW_FULL_FOOT=(
        "As the task runs, files, tool results and executed skills all accumulate. This is "
        "why a big job is better split into several focused tasks, each with a fresh window."
    ),
    CONTEXT_ROT_FOOT=(
        "The fix is housekeeping: one job per task, only the connectors you need, and "
        "only the files the job actually reads."
    ),
    CONTEXT_LEVERS=[
        ("Conversation", "Your prompt. The messages you send, including both text and attachments."),
        ("Project context", "The files the project reads, and the folder it works in."),
        ("Connectors", "The connected tools Claude can pull data from, and take actions in."),
        ("Skills", "A set of instructions Claude follows for a repeatable workflow."),
        ("Instructions & memory file", "Project rules you wrote, and decisions kept in the memory file."),
    ],
    CONTEXT_LEVERS_FOOT=(
        "Every lab today pulls one of these levers — context in Lab 1, connectors in Lab 4, "
        "skills in Labs 5–7, and the memory file in Lab 10."
    ),
    PRICING_BAND=("Parallel tasks multiply usage: four tasks cost roughly four times one chat. "
                  "Watch Settings → Usage."),
    CONTROL_RULES=[
        ("Work from mock data", "Use the supplied synthetic Lumo data — never real customer records in training."),
        ("Scope the connector", "Give Claude one Drive folder for the task, not your entire Drive."),
        ("Check every figure", "Read the artefact's and the brief's numbers back against the source file."),
        ("Approve before sending", "Read each drafted email and post in full; approve it only when the facts match."),
        ("Use a test recipient", "Send class exercises to yourself, never to a real customer."),
        ("Draft-only schedules", "A scheduled task runs unattended — let it draft and email you, never publish."),
    ],
    NEXT_STEPS=[
        ("Start one real Project", "Give your next campaign a project with instructions, context and a folder."),
        ("Split one job into tasks", "Next time you research competitors, give each one its own task."),
        ("Capture your brand voice", "Turn your real brand guide into a skill your whole team shares."),
        ("Schedule one routine", "Pick the post or report you produce every week and schedule the draft."),
        ("Watch for the new Projects", "When your account gets the lead agent and threads, the Threads edition of this course shows the same labs on it."),
    ],
    THANK_YOU=dict(
        kicker="THANK YOU FOR ATTENDING",
        headline="Your launch project is ready",
        body=("A Claude Project with instructions, context and a working folder, verified market "
              "research, a Live Artefact dashboard, a deck and brief, a brand-voice skill, two "
              "weeks of social posts, a launch video and the scheduled tasks that keep it all moving."),
    ),
    SCREENSHOTS=[
        ("projects", "classic-projects.png", "Projects in Cowork",
         "The Projects list in Cowork — start a new project from here.", "lab1"),
        ("new-project", "classic-create-project.png", "Create a Project",
         "What are you working on, what are you trying to achieve, and a folder.", "lab1"),
        ("project-page", "classic-project-page.png", "The Project Page",
         "Instructions, Context, Folder and Scheduled — the four panels.", "lab1"),
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
        ("scheduled", "classic-scheduled.png", "Create a Scheduled Task",
         "Name, instructions, project, frequency and permissions.", "lab10"),
    ],
    LG_INTRO=(
        "Claude is no longer only a chat window. In Cowork, a Claude Project gives one body of "
        "work its own instructions, reference files and working folder, so every task you start "
        "already knows the brand and the rules. This course teaches that way of working through "
        "one continuous marketing scenario: you are the marketing team at Lumo Kopi Co., "
        "launching a new canned cold-brew kopi. Over ten labs, all inside one project, you "
        "research the market in parallel tasks, build a Live Artefact dashboard, connect Google "
        "Drive and Gmail, produce a launch deck and campaign brief, capture the brand voice as a "
        "skill, add a marketing plugin, create two weeks of social posts and a launch video, and "
        "schedule the routine work so it runs on its own."
    ),
    LG_SETUP_VERIFY=(
        "Open the Claude desktop app, sign in, switch to Cowork and open Projects. If you can "
        "start a new project and see its Instructions, Context, Folder and Scheduled panels, "
        "your setup is ready. (If your Projects page instead offers a Goal and talks about a "
        "lead agent and threads, your account has the new Projects — use the Threads edition "
        "of the labs.)"
    ),
    LG_PROJECT_HOWTO=[
        dict(title="Creating the project",
             shot="new-project",
             paras=[
                 "In Cowork, a project is created from a short dialog with two questions and a "
                 "folder. The name is how you find it again; the answer to \"What are you trying "
                 "to achieve?\" is the standing goal every task in the project inherits.",
                 "Point the project at a folder you create for it. That folder is where Claude "
                 "works — it reads the data you put there and writes every output back — and it "
                 "stays a normal folder you can open, back up or share.",
             ],
             example=("Launch Lumo Cold Kopi in Singapore on 1 December 2026. Produce the research, "
                      "launch deck, campaign brief, two weeks of social posts and a 15-second launch "
                      "video, within a S$60,000 budget, so that 25-34 year-olds on Instagram and "
                      "TikTok know the product exists by launch day."),
             steps=[
                 "In Cowork, open Projects and start a new project.",
                 "Type the name, paste the goal into What are you trying to achieve?, and choose Use a folder.",
                 "Click Create project. The project page opens with its four panels.",
             ]),
        dict(title="Writing project instructions",
             shot="project-page",
             paras=[
                 "Instructions are standing rules that apply to every task in the project. Use them "
                 "for things that are always true: the currency, the brand voice in brief, what "
                 "must never happen without your approval.",
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
                 "On the project page, open the Instructions panel.",
                 "Paste the instructions and save.",
                 "Start a new task and check that the rules are followed without you repeating them.",
             ]),
        dict(title="Adding context and using the folder",
             shot="project-page",
             paras=[
                 "Context is what the project reads: the brand guidelines, the product sheet, the "
                 "launch brief. Claude reads context but does not edit it, so it is the right home "
                 "for reference material you want kept exactly as it is.",
                 "The Folder is different: it is where Claude works. Data it should analyse and "
                 "every file it produces live there. Mixing the two up is the most common setup "
                 "mistake — reference in Context, working files in the Folder.",
             ],
             example=None,
             steps=[
                 "On the project page, open Context and add the reference files.",
                 "Put the lab's data files in the project folder on your computer.",
                 "Ask: \"Which context files and folder files can you see, and what is each one for?\"",
             ]),
        dict(title="Keeping a memory file",
             shot="project-page",
             paras=[
                 "A classic project has no memory panel of its own, so keep one yourself: a Markdown "
                 "file in the project folder — lumo-project-memory.md — where Claude records "
                 "decisions you ask it to remember. Every later task can read it.",
                 "Because Claude writes it, check it. Open the file from time to time, correct "
                 "anything out of date and delete anything you do not want every future task to "
                 "believe. It is a shared notebook that you are responsible for.",
             ],
             example=("Add this to lumo-project-memory.md: the Singapore launch date has moved from "
                      "1 December to 8 December 2026. Update anything you have planned that depends on it."),
             steps=[
                 "Ask Claude to create lumo-project-memory.md in the project folder (Lab 1 does this).",
                 "Tell Claude what to record whenever a decision changes.",
                 "Open the file yourself and correct or delete lines as needed.",
             ]),
        dict(title="Scheduling tasks",
             shot="scheduled",
             paras=[
                 "A scheduled task is a prompt that runs on a timetable. Pick the project in the "
                 "task's settings and it runs with the project's instructions, context and folder — "
                 "you do not repeat them in the task.",
                 "Schedule drafts, not publishing. Permissions defaults to Automatically approve, so "
                 "the task acts unattended: it should prepare today's post and email it to you for "
                 "approval, and the click that publishes stays yours.",
             ],
             example=("Take today's row from social-calendar.csv, polish the post with "
                      "lumo-brand-voice, check every price and claim against the brand kit, and "
                      "email it to me as a draft with the subject \"Today's Lumo post\". Never "
                      "publish anything."),
             steps=[
                 "Open Scheduled tasks from the sidebar and choose New task → Set up manually.",
                 "Enter the Name and paste the Instructions; pick the Lumo Cold Kopi Launch project.",
                 "Change Frequency from Manual to the timetable you want, and check Permissions.",
                 "Save, then check the email that arrives at the first run.",
             ]),
    ],
    LABS_README_NOTE=(
        "All ten labs run inside **one Claude Project** in Cowork — the Lumo Cold Kopi Launch\n"
        "project you create in Lab 1. Lab 2 starts several tasks in the project at once, one per\n"
        "subject, then merges their results.\n"
        "\n"
        "Each lab folder holds only the **prompt PDF** and, where the lab needs it, a **data/**\n"
        "folder of mock data and assets. The full step-by-step instructions and check steps are\n"
        "in the Learner Guide, and every prompt is on the copy-ready prompts page."
    ),
    LG_GLOSSARY_DROP=("Effort", "Lead agent", "Thread"),
    LG_GLOSSARY_ADD=[
        ("Memory file", "A Markdown file in the project folder where Claude records decisions you ask it to keep, read by every later task."),
        ("Project folder", "The folder on your computer a Cowork project works in: Claude reads data there and writes its outputs back."),
        ("Task", "One job you start inside a project. Several tasks can run at once."),
    ],
    LG_WRAPUP=dict(
        title="Wrap-Up",
        intro=("Across ten labs you took one product launch from an empty project to a "
               "researched, branded and scheduled campaign."),
        sections=[
            dict(title="What you built", bullets=[
                "The Lumo Cold Kopi Launch project, with instructions, context, a folder and a memory file.",
                "A market research brief merged from four parallel tasks, with conflicts flagged.",
                "A Market Insights Live Artefact dashboard, saved and downloaded.",
                "Google Drive and Gmail connected, with an approved summary sent to yourself.",
                "A launch deck in Slides and a campaign brief in Docs.",
                "A lumo-brand-voice Agent Skill and the Marketing plugin.",
                "Two weeks of social posts across four platforms.",
                "A 15-second vertical launch video.",
                "Scheduled tasks that draft the daily post and the weekly report for your approval.",
            ]),
            dict(title="The habit to keep", bullets=[
                "Give long-running work a project with clear instructions, not a string of chats.",
                "Split big jobs into focused tasks, one subject each, and merge the results.",
                "Check every figure and claim against the source before anything goes out.",
                "Write a routine down once as a skill instead of retyping it every time.",
                "Schedule the drafting; keep the publishing click for yourself.",
            ]),
        ],
    ),
)

# Lab folder slugs that named the threads feature.
SLUG_OVERRIDES = {2: "market-research", 8: "social-posts"}

# ---- per-lab replacements -----------------------------------------------------
LAB_OVERRIDES = {
    1: dict(
        objective="create a Claude Project in Cowork with instructions, context, a working folder and a memory file",
        desc=(
            "Lumo Kopi Co. launches Lumo Cold Kopi in six weeks, and the marketing work will "
            "keep coming until launch day — exactly what a Claude Project is for. You create "
            "the Lumo Cold Kopi Launch project in Cowork, point it at a working folder, write "
            "its standing instructions, add the brand kit as context, and check that Claude "
            "understood all of it. Every later lab runs inside this project."
        ),
        build="The Lumo Cold Kopi Launch project, with instructions, three context files, a working folder and a project memory file.",
        services="Claude desktop app (Cowork), Claude Projects",
        prompt_intro=("This lab has **three blocks**. Block 1 is the project goal, pasted into the "
                      "Create a project dialog. Block 2 is the standing instructions, pasted into "
                      "the Instructions panel. Block 3 is your first task in the project."),
        prompt_intro_md=("This lab has **three blocks**: the goal (Create a project dialog), the\n"
                         "instructions (Instructions panel) and your first task."),
        prompt_intro_lg=("This lab has three blocks. Block 1 is the project goal, pasted into the "
                         "Create a project dialog. Block 2 is the standing instructions, pasted into "
                         "the Instructions panel. Block 3 is your first task in the project."),
        prompt_blocks=[
            dict(
                label="Block 1 — GOAL", step=3,
                lead="Paste this into \"What are you trying to achieve?\" in the Create a project dialog:",
                text=(
                    "Launch Lumo Cold Kopi in Singapore on 1 December 2026.\n"
                    "Produce the market research, a launch deck, a campaign brief,\n"
                    "two weeks of social media posts and a 15-second launch video,\n"
                    "within a S$60,000 budget, so that 25-34 year-olds on Instagram\n"
                    "and TikTok know the product exists by launch day."
                ),
                after="Name it **Lumo Cold Kopi Launch**, choose **Use a folder** and pick your Lumo Launch folder, then **Create project**.",
                after_md="Name it **Lumo Cold Kopi Launch**, use your Lumo Launch folder, then **Create project**.",
                slide_note="Name: Lumo Cold Kopi Launch. Use a folder: your empty Lumo Launch folder.",
            ),
            dict(
                label="Block 2 — INSTRUCTIONS", step=5,
                lead="Paste this into the project's Instructions panel:",
                text=(
                    "You are the marketing team for Lumo Kopi Co.\n"
                    "- Prices are in Singapore dollars: S$3.90 per can, S$42.00 per\n"
                    "  12-pack. Always two decimals.\n"
                    "- Follow lumo-brand-guidelines.md for anything customer-facing.\n"
                    "- Never describe the product as healthy. You may say 5 g sugar.\n"
                    "- Never send an email or publish a post without my approval.\n"
                    "- Save every output to the project folder.\n"
                    "- Read lumo-project-memory.md before you start any task.\n"
                    "- Flag any figure that two sources disagree on. Do not pick one."
                ),
                after="Save the instructions, then add the three brand-kit files in the **Context** panel.",
                after_md="Save, then add the three brand-kit files under **Context**.",
                slide_note="Save the instructions, then add the brand kit under Context.",
            ),
            dict(
                label="Block 3 — FIRST TASK", step=7,
                lead="Start a new task in the project and send:",
                text=(
                    "Before we start work, check your setup:\n"
                    "1. Restate the project goal in one line.\n"
                    "2. List the context files you can read and what each is for.\n"
                    "3. List the three instructions you think matter most.\n"
                    "4. From the product sheet, give me the price per can, the sugar\n"
                    "   per can and the launch date.\n"
                    "Then create lumo-project-memory.md in the project folder with\n"
                    "the heading \"Project memory\" and record: our primary audience\n"
                    "is 25-34 year-olds in Singapore, and our secondary market is\n"
                    "Kuala Lumpur, launching 15 January 2027."
                ),
                after="Compare the answer with the brand kit, then open your Lumo Launch folder and read lumo-project-memory.md.",
                after_md="Check the answers, then open lumo-project-memory.md in the folder.",
                slide_note="Check the four answers, then open the new memory file in the folder.",
            ),
        ],
        prompt_note=("Projects live in Cowork mode in the desktop app. Create an empty folder called "
                     "Lumo Launch on your computer first — the project works inside it."),
        steps=[
            ("Download the course labs and open the Lab 01 data/brand-kit folder. Create an empty folder called Lumo Launch on your computer.",
             "Skim the three brand-kit files — you will check Claude's answers against them. The empty folder becomes the project's working folder."),
            ("In the Claude desktop app, switch to Cowork, open Projects and start a new project.",
             "In Cowork a project is backed by a real folder on your computer, so its files stay yours to open."),
            ("Under \"What are you working on?\" type Lumo Cold Kopi Launch, and paste Block 1 into \"What are you trying to achieve?\".",
             "The goal is the standing context every task inherits, so write it as an outcome with a date and a measure."),
            ("Choose Use a folder, pick your Lumo Launch folder, and click Create project.",
             "The project page opens with four panels: Instructions, Context, Folder and Scheduled."),
            ("Open the Instructions panel and paste Block 2. Save.",
             "Instructions are standing rules for every task. Short, checkable rules work better than general wishes."),
            ("Open the Context panel and add the three brand-kit files.",
             "Context is read, never edited — the right home for reference files you want kept exactly as they are."),
            ("Start a new task in the project and send Block 3.",
             "This is a setup check: if Claude cannot restate the goal or find the files, fix that now, before any real work."),
            ("Check the answers: S$3.90 per can, 5 g sugar, launch 1 December 2026.",
             "Every figure must match the product sheet. A wrong figure here means a wrong context file."),
            ("Open the Lumo Launch folder on your computer and read lumo-project-memory.md.",
             "A classic project has no memory panel, so this file plays that role: every task reads it (Block 2 says so), and you can edit it."),
        ],
        test=(
            "The Lumo Cold Kopi Launch project exists in Cowork, using your Lumo Launch folder, "
            "with the Block 2 instructions saved and the three brand-kit files under Context. "
            "Claude restated the goal, listed all three context files, and quoted S$3.90 per can, "
            "5 g sugar and a 1 December 2026 launch. lumo-project-memory.md in the folder "
            "records the 25-34 audience and the 15 January 2027 Kuala Lumpur launch."
        ),
    ),
    2: dict(
        title="Run Market Research in Parallel Tasks",
        objective="split a multi-subject research job into parallel tasks and verify the merged brief",
        desc=(
            "Before anyone writes a post, the team needs to know the market. Four subjects need "
            "research — competitors, the customer survey, pricing and social trends — and none "
            "depends on another. So you start four tasks in the project at once, one per "
            "subject, each saving its findings to the folder. A fifth task merges the four files "
            "into one research brief, which you check against the data."
        ),
        build="Four research files and lumo-research-brief.docx merged from them, in the project folder.",
        services="Claude Projects in Cowork, parallel tasks, web search",
        prompt_intro=("This lab has **five blocks**. Blocks 1-4 each start their own task — send "
                      "them one after another without waiting. Block 5 goes in a fifth task once "
                      "the four research files exist."),
        prompt_intro_md=("This lab has **five blocks**: four research tasks started together, then\n"
                         "one merge task."),
        prompt_intro_lg=("This lab has five blocks. Blocks 1 to 4 each go into their own new task, "
                         "started one after another without waiting for the previous one to finish. "
                         "Block 5 goes into a fifth task once the four research files are in the folder."),
        prompt_blocks=[
            dict(label="Block 1 — COMPETITORS", step=3,
                 lead="Start a new task in the project and send:",
                 text=(
                     "Research COMPETITORS for the Lumo Cold Kopi launch using\n"
                     "lumo-competitors.csv: price per can, pack, positioning and\n"
                     "channel for each brand, and the gap Lumo can own.\n"
                     "Save your findings as research-1-competitors.md in the project\n"
                     "folder."
                 ),
                 after="Do not wait for it — start the next task straight away.",
                 after_md="Do not wait — start the next task.",
                 slide_note="Start the next task straight away — these four run in parallel."),
            dict(label="Block 2 — CUSTOMERS", step=4,
                 lead="Start a second task and send:",
                 text=(
                     "Research CUSTOMERS using lumo-consumer-survey-2026.csv: the share\n"
                     "likely to buy (intent 4 or 5), split by age band and city; the\n"
                     "top purchase drivers; the top discovery channels. Show your\n"
                     "working for every percentage. Save your findings as\n"
                     "research-2-customers.md in the project folder."
                 ),
                 after="Start the third task.",
                 after_md="Start the third task.",
                 slide_note="Show your working is what lets you check every percentage."),
            dict(label="Block 3 — PRICING", step=5,
                 lead="Start a third task and send:",
                 text=(
                     "Research PRICING using lumo-competitors.csv and\n"
                     "lumo-consumer-survey-2026.csv: where S$3.90 sits against the\n"
                     "competitor median, and the share of respondents willing to pay\n"
                     "S$3.50 or more. Show your working. Save your findings as\n"
                     "research-3-pricing.md in the project folder."
                 ),
                 after="Start the fourth task.",
                 after_md="Start the fourth task.",
                 slide_note="\"S$3.50 or more\" includes S$3.50 exactly."),
            dict(label="Block 4 — TRENDS", step=6,
                 lead="Start a fourth task and send:",
                 text=(
                     "Research SOCIAL TRENDS using lumo-social-trends.csv: the three\n"
                     "content themes with the highest engagement, with one post idea\n"
                     "each. Save your findings as research-4-trends.md in the project\n"
                     "folder."
                 ),
                 after="Four tasks are now running at once. Watch them finish in the project's task list.",
                 after_md="Four tasks now run at once.",
                 slide_note="Four tasks, four subjects, four fresh context windows."),
            dict(label="Block 5 — MERGE", step=7,
                 lead="When all four files are in the folder, start a fifth task and send:",
                 text=(
                     "Merge research-1-competitors.md, research-2-customers.md,\n"
                     "research-3-pricing.md and research-4-trends.md from the project\n"
                     "folder into one research brief, lumo-research-brief.docx:\n"
                     "a one-paragraph summary, one section per subject with the key\n"
                     "numbers, and three recommendations for the launch. Name the\n"
                     "source file under each section, and flag anything the four\n"
                     "files disagree on."
                 ),
                 after="Open the brief and check it against the data in the next steps.",
                 after_md="Then check the brief against the data.",
                 slide_note="You are doing by hand what the new Projects' lead agent does automatically."),
        ],
        prompt_note="Copy the three CSV files from the Lab 02 data folder into your Lumo Launch project folder first.",
        steps=[
            ("Open the Lab 02 data folder and glance at the three CSV files.",
             "Know your source: 400 survey rows, six competitors, twelve content themes."),
            ("Copy the three CSV files into your Lumo Launch project folder.",
             "Data Claude analyses belongs in the Folder; the brand kit stays in Context."),
            ("Start a new task in the project and send Block 1. Do not wait for it.",
             "Each task has one subject and one file — a focused brief with a fresh context window. That is why parallel research stays sharp."),
            ("Start a second task and send Block 2.",
             "Several tasks can run in one project at the same time."),
            ("Start a third task and send Block 3.",
             "Pricing reads both files; it does not need the other tasks' results."),
            ("Start a fourth task and send Block 4.",
             "You are now the lead agent: four workers, four subjects, one goal."),
            ("When the four research files are in the folder, start a fifth task and send Block 5.",
             "The merge task reads the files, not the other conversations — so the folder is how the tasks share their work."),
            ("When the merged brief arrives, check the survey numbers.",
             "Expect 400 respondents, 248 likely to buy (62%), and 112 of 152 in the 25-34 band (74%)."),
            ("Check the channel, driver and pricing findings.",
             "Instagram 136 (34%), TikTok 104 (26%); Taste 124 (31%); competitor median S$4.30 with S$3.90 below it; 228 (57%) would pay S$3.50 or more."),
            ("Check the trends section and the recommendations.",
             "The top theme should be Taste tests and first-sip reactions. Do the three recommendations follow from the numbers above them?"),
        ],
        test=(
            "The project folder holds the four research files and lumo-research-brief.docx, "
            "whose summary, four sections and three recommendations name their source files. "
            "The brief reports 400 respondents, 248 likely to buy (62%), 112 of 152 aged 25-34 "
            "(74%), Instagram as the top discovery channel at 34%, Taste as the top driver at "
            "31%, a competitor median of S$4.30 with Lumo's S$3.90 below it, 228 respondents "
            "(57%) willing to pay S$3.50 or more, and Taste tests and first-sip reactions as the "
            "top content theme."
        ),
    ),
    10: dict(
        objective="schedule recurring project tasks, keep the project memory file current and review the project",
        desc=(
            "The launch needs a post drafted every weekday morning and a report every Monday, "
            "and nobody should have to remember either. You create both as scheduled tasks on "
            "the project, then do the housekeeping a real project needs: record a changed plan "
            "in the memory file, and review what the project now holds."
        ),
        build="Two scheduled tasks on the project, an updated memory file and a project review.",
        services="Claude Projects in Cowork, scheduled tasks, Gmail connector",
        prompt_intro=("This lab has **four blocks**. Blocks 1 and 2 are pasted into the **Create "
                      "scheduled task** dialog, not the chat. Block 3 updates the memory file, and "
                      "Block 4 is a review you send at the end."),
        prompt_intro_md=("This lab has **four blocks**: two scheduled-task instructions (pasted into\n"
                         "the dialog), a memory update and a review."),
        prompt_intro_lg=("This lab has four blocks. Blocks 1 and 2 are pasted into the Instructions "
                         "field of the Create scheduled task dialog, not typed into the chat. Block 3 "
                         "updates the project's memory file. Block 4 asks the project to review itself."),
        prompt_blocks=[
            dict(
                label="Block 1 — DAILY POST TASK", step=2,
                lead="Paste into the Instructions field of a new scheduled task named \"Today's Lumo post\":",
                text=(
                    "Take today's row from social-calendar.csv in the project folder,\n"
                    "polish the post with lumo-brand-voice, and check every price and\n"
                    "claim against the brand kit. Email it to <YOUR EMAIL> as a draft\n"
                    "with the subject \"Today's Lumo post - <date>\".\n"
                    "\n"
                    "Never publish anything and never post to social media. If there\n"
                    "is no row for today, email \"No Lumo post scheduled today\"."
                ),
                after=("Pick the **Lumo Cold Kopi Launch** project, set **Frequency** to weekdays at "
                       "9:00am, and save. Permissions defaults to *Automatically approve* — which is "
                       "why the task only drafts."),
                after_md="Pick the project, set weekdays at 9:00am, save.",
                slide_label="INSTRUCTIONS — paste into the scheduled task dialog",
                slide_note="Not the chat — this is the scheduled task's own Instructions field.",
            ),
            dict(
                label="Block 2 — WEEKLY REPORT TASK", step=4,
                lead="Paste into a second scheduled task named \"Weekly launch report\":",
                text=(
                    "Summarise last week's posts from social-calendar.csv and anything\n"
                    "new in the Lumo Launch Drive folder in five bullet points, and\n"
                    "email the summary to <YOUR EMAIL>. Draft only - do not send\n"
                    "anything else."
                ),
                after="Pick the project, set **Frequency** to weekly, Mondays at 8:00am, and save.",
                after_md="Pick the project, set Mondays at 8:00am, save.",
                slide_label="INSTRUCTIONS — paste into the scheduled task dialog",
                slide_note="Mondays at 8:00am. Replace <YOUR EMAIL>.",
            ),
            dict(
                label="Block 3 — MEMORY", step=6,
                lead="Start a new task in the project and send:",
                text=(
                    "Add this to lumo-project-memory.md: the Singapore launch has\n"
                    "moved from 1 December to 8 December 2026. Kuala Lumpur is\n"
                    "unchanged. Then tell me everything in the project folder and\n"
                    "scheduled tasks that depends on the launch date - posts, tasks,\n"
                    "the deck, the brief - and propose the changes. Do not make them yet."
                ),
                after="Open **lumo-project-memory.md** in the folder and check the new line.",
                after_md="Check the new line in lumo-project-memory.md.",
                slide_note="Then open the memory file yourself and check what it wrote.",
            ),
            dict(
                label="Block 4 — REVIEW", step=8,
                lead="Send this at the end of the lab:",
                text=(
                    "Review this project for me: list every file in the project\n"
                    "folder, which lab produced it, and what it is for. Then tell me\n"
                    "which instructions, context files or memory-file lines are now\n"
                    "out of date."
                ),
                after="Compare its list with the folder on your computer.",
                after_md="Compare its answer with the folder.",
                slide_note="A project that can describe itself is one a colleague can pick up tomorrow.",
            ),
        ],
        prompt_note=("Replace <YOUR EMAIL> in Blocks 1 and 2. Copy social-calendar.csv from Lab 8 into "
                     "the project folder if Claude saved it elsewhere."),
        steps=[
            ("Open Scheduled tasks from the sidebar (or the project's Scheduled panel), choose New task, then Set up manually.",
             "Create with Claude asks you questions instead; setting it up manually shows you every field."),
            ("Name it Today's Lumo post and paste Block 1 into Instructions, with your own email.",
             "The task runs in the project, so it inherits the instructions, context, folder and the brand-voice skill — the prompt stays short."),
            ("Pick the Lumo Cold Kopi Launch project, set Frequency to weekdays at 9:00am, check Permissions, and save.",
             "Frequency defaults to Manual — a task left on Manual never runs. Permissions defaults to Automatically approve, so the task must only draft."),
            ("Create a second task, Weekly launch report, with Block 2, Mondays at 8:00am.",
             "Two tasks, two timetables, one project. This is where you would add a monthly competitor scan next."),
            ("Confirm both tasks appear under Scheduled, with the right days and times. Use Run now if it is offered.",
             "A task scheduled at the wrong time is a silent failure. A test run's email shows exactly what arrives each morning."),
            ("Start a new task in the project and send Block 3.",
             "Expect the calendar, Task 1, the deck's title slide and timeline, and the brief. The memory file is how one fact reaches every later task."),
            ("Open lumo-project-memory.md and check the new launch-date line. Edit it if the wording is wrong.",
             "Claude writes the file, but you own it. Delete anything you would not want every future task to believe."),
            ("Send Block 4 at the end of the lab.",
             "A project that can list its own files and what each is for is one a colleague can pick up tomorrow."),
            ("Open Settings → Usage and see how much of your plan today's labs used.",
             "Parallel tasks finish faster but use more in total — worth knowing before you schedule work every day."),
        ],
        test=(
            "Two scheduled tasks are listed on the project — Today's Lumo post on weekdays at "
            "9:00am and Weekly launch report on Mondays at 8:00am — both drafting and emailing "
            "only, with nothing published. lumo-project-memory.md records the 8 December "
            "Singapore launch, Claude listed what depends on it, and the project review matches "
            "the files in your Lumo Launch folder."
        ),
    ),
}

# Phrase swaps for labs whose threads wording only needs re-pointing at tasks.
# Applied to every string in the lab, longest phrase first.
LAB_SWAPS = {
    2: [("Research the market in four threads", "Research the market in four parallel tasks")],
    6: [
        ("every thread in the project", "every task in the project"),
        ("Start a new thread in the project and send:", "Start a new task in the project and send:"),
        ("Start a new thread and send Block 3.", "Start a new task and send Block 3."),
        ("A fresh thread proves the skill works without the earlier conversation — which is exactly how other threads will use it.",
         "A fresh task proves the skill works without the earlier conversation — which is exactly how later tasks will use it."),
        ("In a fresh thread", "In a fresh task"),
    ],
    8: [
        ("Draft two weeks of posts, one thread per platform", "Draft two weeks of posts for four platforms"),
        ("Create Social Media Posts in Parallel Threads", "Create Two Weeks of Social Media Posts"),
        ("produce a two-week, four-platform social calendar with one thread per channel",
         "produce a two-week, four-platform social calendar using the brand-voice skill"),
        ("Each platform has its own format, so you hand the job to the lead agent and let it "
         "start one thread per platform. Every thread loads lumo-brand-voice, drafts its "
         "posts to its platform's spec, and the lead agent merges them into one dated "
         "calendar that you check before anything is scheduled.",
         "Each platform has its own format, so the prompt gives Claude a spec for each. It "
         "loads lumo-brand-voice, drafts every platform's posts to its spec, and saves one "
         "dated calendar that you check before anything is scheduled."),
        ("Claude Projects, lead agent and threads, Agent Skills", "Claude Projects in Cowork, Agent Skills"),
        ("Split the drafting into four threads, one per platform, and run\n"
         "them in parallel:\n", "Draft each platform's posts to its own spec:\n"),
        ("Every thread must use the lumo-brand-voice skill and our top\n"
         "content theme from the research.", "Use the lumo-brand-voice skill for every post, and our top\n"
         "content theme from the research."),
        ("Then merge the threads into social-calendar.csv", "Then save them into social-calendar.csv"),
        ("This is the same pattern as Lab 2 — one message, independent subjects — applied to production instead of research.",
         "One task with four precise specs. In the Threads edition each platform gets its own thread; here the specs keep one task on track."),
        ("Watch the lead agent start the four platform threads.", "Watch Claude work through the four platforms."),
        ("Each thread has its own spec and its own context window, so the TikTok scripts never crowd out the LinkedIn story.",
         "Each platform is drafted against its own spec, so the TikTok scripts and the LinkedIn story stay distinct."),
        ("Open the Instagram thread and check it loaded lumo-brand-voice.", "Check in the task's activity that Claude loaded lumo-brand-voice."),
        ("The skill you wrote in Lab 6 is now doing its real job: keeping four parallel writers on one voice.",
         "The skill you wrote in Lab 6 is now doing its real job: keeping four formats in one voice."),
        ("ask the lead agent to send it back to its thread for a fix", "ask Claude to redraft it"),
        ("When the merged calendar arrives", "When the calendar arrives"),
    ],
    9: [
        ("one thread writes a five-scene script and storyboard with lumo-brand-voice, another "
         "writes and runs the code", "Claude first writes a five-scene script and storyboard with "
         "lumo-brand-voice, then writes and runs the code"),
        ("Claude Projects, threads, code execution", "Claude Projects in Cowork, code execution"),
        ("Use two threads:\n", "Work in two stages:\n"),
        ("Thread 1 - SCRIPT", "Stage 1 - SCRIPT"),
        ("Thread 2 - RENDER", "Stage 2 - RENDER"),
        ("Two threads, but not in parallel this time: the render thread waits for the script. The lead agent manages that order.",
         "Two stages in one task: the render waits for the script, so you can read the storyboard first."),
        ("when Thread 1 finishes", "when Stage 1 finishes"),
    ],
}
