"""Topic 1 — Claude Projects and Market Research. Labs 1-3.

Lab 1 creates the one project every later lab works inside. Lab 2 hands the
project's lead agent a four-subject research job, which it splits into parallel
threads. Lab 3 turns the research data into the Live Artefact dashboard the
launch deck and social posts later quote.

Every figure in a check step comes from course_data.FACTS, which
build_mockdata.py asserts against the generated files.
"""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Set Up the Lumo Launch Project",
        objective="create a Claude Project with a goal, instructions, context and memory",
        desc=(
            "Lumo Kopi Co. launches Lumo Cold Kopi in six weeks, and the marketing work will "
            "keep coming until launch day — exactly what a Claude Project is for. You create "
            "the Lumo Cold Kopi Launch project, give it a goal, add the brand kit as context, "
            "write its standing instructions, and check that its lead agent understood all "
            "three. Every later lab runs inside this project."
        ),
        build="The Lumo Cold Kopi Launch project, with a goal, instructions, three context files and a first memory entry.",
        services="Claude desktop app, Claude Projects",
        data=["brand-kit/lumo-brand-guidelines.md", "brand-kit/lumo-product-sheet.md",
              "brand-kit/lumo-launch-brief.md"],
        prompt_intro=("This lab has **three blocks**. Block 1 is the project goal, pasted into "
                      "the New project dialog. Block 2 is the project instructions, pasted into "
                      "Project settings. Block 3 is your first message to the lead agent."),
        prompt_intro_md=("This lab has **three blocks**: the goal (New project dialog), the\n"
                         "instructions (Project settings → Memory) and a first message to the\n"
                         "lead agent."),
        prompt_intro_lg=("This lab has three blocks. Block 1 is the project goal, typed into the "
                         "New project dialog. Block 2 is the standing instructions, pasted into "
                         "Project settings → Memory. Block 3 is your first message to the lead agent."),
        prompt_title="Create the launch project",
        prompt_blocks=[
            dict(
                label="Block 1 — GOAL", step=3,
                lead="Paste this into the Goal field of the New project dialog:",
                text=(
                    "Launch Lumo Cold Kopi in Singapore on 1 December 2026.\n"
                    "Produce the market research, a launch deck, a campaign brief,\n"
                    "two weeks of social media posts and a 15-second launch video,\n"
                    "within a S$60,000 budget, so that 25-34 year-olds on Instagram\n"
                    "and TikTok know the product exists by launch day."
                ),
                after="Name the project **Lumo Cold Kopi Launch**, add the three brand-kit files as Context, and click **Create project**.",
                after_md="Name it **Lumo Cold Kopi Launch**, add the three brand-kit files as Context, then **Create project**.",
                slide_note="Name: Lumo Cold Kopi Launch. Add the three brand-kit files as Context.",
            ),
            dict(
                label="Block 2 — INSTRUCTIONS", step=5,
                lead="Paste this into Project settings → Memory → Project instructions:",
                text=(
                    "You are the marketing team for Lumo Kopi Co.\n"
                    "- Prices are in Singapore dollars: S$3.90 per can, S$42.00 per\n"
                    "  12-pack. Always two decimals.\n"
                    "- Follow lumo-brand-guidelines.md for anything customer-facing.\n"
                    "- Never describe the product as healthy. You may say 5 g sugar.\n"
                    "- Never send an email or publish a post without my approval.\n"
                    "- When a job has several independent subjects, give each one\n"
                    "  its own thread and merge the results for me.\n"
                    "- Flag any figure that two sources disagree on. Do not pick one."
                ),
                after="Save the instructions, then go back to the project and send Block 3.",
                after_md="Save, then send Block 3 to the lead agent.",
                slide_note="Save the instructions before you send Block 3.",
            ),
            dict(
                label="Block 3 — FIRST MESSAGE", step=7,
                lead="Send this to the lead agent:",
                text=(
                    "Before we start work, check your setup:\n"
                    "1. Restate the project goal in one line.\n"
                    "2. List the context files you can read and what each is for.\n"
                    "3. List the three instructions you think matter most.\n"
                    "4. From the product sheet, give me the price per can, the sugar\n"
                    "   per can and the launch date.\n"
                    "Then remember this for the project: our primary audience is\n"
                    "25-34 year-olds in Singapore, and our secondary market is\n"
                    "Kuala Lumpur, launching 15 January 2027."
                ),
                after="Compare the answer with the brand kit, then open Project settings → Memory and find the new memory entry.",
                after_md="Check the answers against the brand kit, then find the new memory entry.",
                slide_note="Check the four answers, then find the new entry in the memory files.",
            ),
        ],
        prompt_note=("No Projects in your sidebar yet? The beta has not reached your account. "
                     "Switch to Cowork mode, attach the three brand-kit files, paste Block 2 "
                     "as your first message, then send Block 3."),
        steps=[
            ("Download the course labs and open the Lab 01 data/brand-kit folder.",
             "Skim the three files — guidelines, product sheet, launch brief. You will check Claude's answers against them."),
            ("In the Claude desktop app, open Projects from the sidebar and click New project.",
             "Projects are shared across the Claude app (Chat and Cowork) and Claude Code, so the same project is reachable from all three."),
            ("Name the project Lumo Cold Kopi Launch and paste Block 1 into the Goal field.",
             "The goal is what the lead agent steers every decision toward, so it is worth writing as an outcome with a date and a measure."),
            ("Under Context, add the three brand-kit files, then click Create project.",
             "Context is read, never edited — the right home for reference files you want kept exactly as they are."),
            ("Click the gear icon to open Project settings, choose Memory, and paste Block 2 into Project instructions. Save.",
             "Instructions are standing rules for every thread. Short, checkable rules work better than general wishes."),
            ("While you are in settings, open General and look at Models.",
             "Note the model and effort for the lead agent and for threads. You will see their cost in Lab 10."),
            ("Back in the project, send Block 3 to the lead agent.",
             "This is a setup check: if it cannot restate the goal or find the files, fix that now, before any real work."),
            ("Check the answers: S$3.90 per can, 5 g sugar, launch 1 December 2026.",
             "Every figure must match the product sheet. A wrong figure here means a wrong context file."),
            ("Open Project settings → Memory and find the memory entry about the audience and Kuala Lumpur.",
             "The project wrote it, so you are responsible for it. Memory you never read is memory you cannot trust."),
        ],
        test=(
            "The Lumo Cold Kopi Launch project exists with the goal from Block 1, the three "
            "brand-kit files under Context and the Block 2 instructions saved. The lead agent "
            "restated the goal, listed all three context files, and quoted S$3.90 per can, "
            "5 g sugar and a 1 December 2026 launch. A memory file now records the 25-34 "
            "audience and the 15 January 2027 Kuala Lumpur launch."
        ),
    ),
    dict(
        num=2, topic=1,
        title="Run Market Research in Parallel Threads",
        objective="hand a multi-subject research job to the lead agent and verify the merged brief",
        desc=(
            "Before anyone writes a post, the team needs to know the market. Four subjects "
            "need research — competitors, the customer survey, pricing and social trends — and "
            "none depends on another. You give the whole job to the lead agent in one message. "
            "It starts one thread per subject, each with its own data file, then merges the "
            "four findings into one research brief, which you check against the data."
        ),
        build="A research brief (lumo-research-brief.docx) merged from four parallel threads, saved in the project.",
        services="Claude Projects, lead agent and threads, web search",
        data=["lumo-consumer-survey-2026.csv", "lumo-competitors.csv", "lumo-social-trends.csv"],
        prompt_step=2,
        prompt_title="Research the market in four threads",
        prompt=(
            "Research the market for the Lumo Cold Kopi launch. The data is in\n"
            "the three files I have attached. Split this into four threads,\n"
            "one per subject, and run them in parallel:\n"
            "\n"
            "Thread 1 - COMPETITORS (lumo-competitors.csv): price per can, pack,\n"
            "  positioning and channel for each brand. Where is the gap Lumo\n"
            "  can own?\n"
            "Thread 2 - CUSTOMERS (lumo-consumer-survey-2026.csv): share likely\n"
            "  to buy (intent 4 or 5), split by age band and city; top purchase\n"
            "  drivers; top discovery channels.\n"
            "Thread 3 - PRICING: where S$3.90 sits against the competitor\n"
            "  median, and the share of respondents willing to pay S$3.50 or\n"
            "  more.\n"
            "Thread 4 - SOCIAL TRENDS (lumo-social-trends.csv): the three content\n"
            "  themes with the highest engagement, with one post idea each.\n"
            "\n"
            "When all four threads are done, merge them into one research brief,\n"
            "lumo-research-brief.docx: a one-paragraph summary, one section per\n"
            "thread with the key numbers, and three recommendations for the\n"
            "launch. Show your working for every percentage. Tell me which\n"
            "thread produced each section, and flag anything the threads\n"
            "disagree on."
        ),
        prompt_note="Attach the three CSV files from the Lab 02 data folder, or add them to the project's Context first.",
        steps=[
            ("Open the Lab 02 data folder and glance at the three CSV files.",
             "Know your source: 400 survey rows, six competitors, twelve content themes."),
            ("In the Lumo Cold Kopi Launch project, attach the three files and send the lab prompt.",
             "One message, four subjects. You are briefing the lead agent, not doing the splitting yourself."),
            ("Watch the lead agent announce the threads it starts.",
             "Each thread has one subject and one file — a focused brief with a fresh context window. That is why parallel research stays sharp."),
            ("Open one thread while it works and read its brief.",
             "You can see exactly what the lead agent asked each thread to do. A poor result usually traces back to a poor thread brief."),
            ("When the merged brief arrives, check the survey numbers.",
             "Expect 400 respondents, 248 likely to buy (62%), and 112 of 152 in the 25-34 band (74%)."),
            ("Check the channel and driver findings.",
             "Instagram is the top discovery channel at 136 (34%), then TikTok at 104 (26%). Taste is the top driver at 124 (31%)."),
            ("Check the pricing section.",
             "The competitor median is S$4.30, so S$3.90 sits below it; 228 respondents (57%) would pay S$3.50 or more."),
            ("Check the trends section and the recommendations.",
             "The top theme should be Taste tests and first-sip reactions. Do the three recommendations follow from the numbers above them?"),
            ("Open lumo-research-brief.docx and confirm each section names its thread.",
             "Traceability: every number in the brief can be traced to one thread and one file."),
        ],
        test=(
            "lumo-research-brief.docx has a summary, four thread sections and three "
            "recommendations. It reports 400 respondents, 248 likely to buy (62%), 112 of 152 "
            "aged 25-34 (74%), Instagram as the top discovery channel at 34%, Taste as the top "
            "driver at 31%, a competitor median of S$4.30 with Lumo's S$3.90 below it, 228 "
            "respondents (57%) willing to pay S$3.50 or more, and Taste tests and first-sip "
            "reactions as the top content theme."
        ),
    ),
    dict(
        num=3, topic=1,
        title="Build the Market Insights Live Artefact",
        objective="turn research data into an interactive Live Artefact dashboard and save it",
        desc=(
            "The research brief is a document; the launch team wants something they can "
            "explore. You turn the survey and competitor data into a Live Artefact — KPI "
            "tiles, a channel chart, a price ladder and a city filter — refine it in plain "
            "English, save it and download a copy. The launch deck in Lab 5 quotes this "
            "dashboard's numbers."
        ),
        build="A saved Market Insights Live Artefact, plus a downloaded HTML copy.",
        services="Claude Projects, Live Artefacts",
        data=["lumo-consumer-survey-2026.csv", "lumo-competitors.csv"],
        prompt_step=1,
        prompt_title="Build the Market Insights dashboard",
        prompt=(
            "Using lumo-consumer-survey-2026.csv and lumo-competitors.csv, build\n"
            "a Live Artefact: an interactive Market Insights dashboard for the\n"
            "Lumo Cold Kopi launch.\n"
            "\n"
            "Include:\n"
            "- KPI tiles: respondents, % likely to buy (intent 4 or 5), top\n"
            "  discovery channel, competitor median price.\n"
            "- A bar chart of discovery channels.\n"
            "- A bar chart of purchase drivers.\n"
            "- A price ladder: the six competitors and Lumo at S$3.90, cheapest\n"
            "  to dearest, with Lumo highlighted.\n"
            "- A filter for city: All, Singapore, Kuala Lumpur. The KPI tiles and\n"
            "  both survey charts must follow the filter.\n"
            "\n"
            "Bake the data into the artefact - do not fetch anything. Use the\n"
            "Lumo brand colours from the brand guidelines. Title it\n"
            "\"Lumo Cold Kopi - Market Insights\"."
        ),
        prompt_note=("Artefacts run in a sandbox and cannot call the internet, which is why "
                     "the prompt says to bake the data in."),
        steps=[
            ("In the project, send the lab prompt with the two CSV files attached or in Context.",
             "The project already knows the brand colours from the guidelines in Context — you do not attach them again."),
            ("Check the KPI tiles with the filter on All.",
             "400 respondents, 62% likely to buy, Instagram top channel, competitor median S$4.30 — the same numbers as the Lab 2 brief."),
            ("Switch the filter to Singapore, then Kuala Lumpur.",
             "The respondents tile should read 240, then 160. If a chart does not change, ask Claude to wire it to the filter."),
            ("Check the price ladder.",
             "Kopi Kaki Cold at S$3.20 is cheapest, Northpoint Cold Brew at S$5.60 is dearest, and Lumo sits third at S$3.90, between Daily Grind RTD at S$3.70 and Frostbean at S$4.20."),
            ("Ask for one refinement, for example: Put the price ladder beside the channel chart.",
             "Refining by conversation is the normal way to work — you never edit the code yourself."),
            ("Save the artefact, then download a copy as HTML.",
             "A saved artefact persists and can be reopened; the download is a file you can share with someone who does not use Claude."),
        ],
        test=(
            "The Market Insights artefact shows 400 respondents, 62% likely to buy, Instagram "
            "as the top channel and a S$4.30 competitor median. The city filter changes the "
            "respondent count to 240 (Singapore) and 160 (Kuala Lumpur) and both survey charts "
            "follow it. The price ladder runs from S$3.20 to S$5.60 with Lumo highlighted at "
            "S$3.90. The artefact is saved and an HTML copy is downloaded."
        ),
    ),
]
