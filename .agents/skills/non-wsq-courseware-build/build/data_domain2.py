"""Topic 2 — Connectors, Skills and Plugins. Labs 4-7.

Lab 4 connects Google Drive and Gmail: the launch budget lives in Drive, and the
Drive sheet deliberately disagrees with the launch brief on two lines, so the
project's "flag disagreements" instruction gets a real test. Lab 5 produces the
launch deck and campaign brief with Claude's Slides and Docs. Lab 6 captures the
brand voice as a skill with /skill-creator; Lab 7 installs a plugin somebody
else packaged.

Lab 6 carries `prompt_blocks`: its blocks are sent as separate messages with a
verify step between, and block 2 begins with the learner typing /skill-creator.
"""

DOMAIN2 = [
    dict(
        num=4, topic=2,
        title="Connect Google Drive and Gmail",
        objective="connect Google Drive and Gmail, read campaign files from Drive and send an approved summary",
        desc=(
            "The launch budget and timeline live in a shared Google Drive folder, not on your "
            "laptop. You upload the Lab 04 data folder to Drive, connect the Google Drive and "
            "Gmail connectors, and have the project read the budget from Drive, reconcile it "
            "against the launch brief, save the research brief back to Drive, and email you an "
            "approved summary. The budget sheet and the brief disagree on two lines — the "
            "project should catch it."
        ),
        build="Drive and Gmail connected, the research brief saved to Drive, and an approved launch summary emailed to yourself.",
        services="Claude Projects, Google Drive connector, Gmail connector",
        data=["Lumo Launch/lumo-launch-budget.csv", "Lumo Launch/lumo-launch-timeline.csv"],
        tools_sections=[
            ("Turning connectors on",
             "Click the **+** in the chat composer, hover **Connectors**, and toggle on only\n"
             "Google Drive and Gmail. You can manage them later under **Customize → Connectors**."),
            ("If Claude says \"insufficient scope\"",
             "The connector is linked but was authorised without permission to read files.\n"
             "Fix it in **Settings → Connectors → Google Drive → Reconnect**, and accept the\n"
             "read access Google asks for. Then tell Claude to try again."),
        ],
        prompt_step=3,
        prompt_title="Reconcile the budget and send the summary",
        prompt=(
            "Using Google Drive, open the \"Lumo Launch\" folder.\n"
            "\n"
            "1. Read lumo-launch-budget.csv and lumo-launch-timeline.csv.\n"
            "2. Compare the budget sheet, line by line, with the budget in\n"
            "   lumo-launch-brief.md from our project context. Show both in one\n"
            "   table and flag every line where they disagree. Do not decide\n"
            "   which is right.\n"
            "3. Upload lumo-research-brief.docx from Lab 2 into the same Drive\n"
            "   folder.\n"
            "4. Draft an email to <YOUR EMAIL> with the subject\n"
            "   \"Lumo launch - research and budget check\": three bullet points\n"
            "   from the research brief, the budget table with the disagreements\n"
            "   flagged, the next milestone from the timeline, and a link to the\n"
            "   brief in Drive.\n"
            "\n"
            "Show me the draft. Do not send it until I approve."
        ),
        prompt_note="Replace <YOUR EMAIL> with your own address. Send lab emails only to yourself.",
        steps=[
            ("Upload the Lab 04 data/Lumo Launch folder to your Google Drive.",
             "In real work the files are already there; the upload stands in for the shared team drive."),
            ("In the project, click + → Connectors and switch on Google Drive and Gmail, signing in to Google.",
             "Accept the read access Google asks for. A connector that shows Connected without read access fails with \"insufficient scope\"."),
            ("Send the lab prompt with your own email address in place of <YOUR EMAIL>.",
             "No files are attached this time — the project reaches Drive itself."),
            ("Read the budget table Claude produces.",
             "Both total S$60,000, but Instagram is S$18,000 in the Drive sheet and S$20,000 in the brief, and Influencers is S$12,000 against S$10,000."),
            ("Confirm Claude flagged both lines instead of choosing one.",
             "That is your Lab 1 instruction at work. Two sources disagreeing is a decision for a human, not a guess for Claude."),
            ("Check that lumo-research-brief.docx now sits in the Lumo Launch folder in Drive.",
             "Saving outputs back to the team's folder is what makes the work findable by colleagues."),
            ("Read the draft email in full, then approve it.",
             "Gmail sends only after your explicit approval. Check the figures against the table before you click."),
            ("Open your inbox and confirm the email arrived with the Drive link working.",
             "Close the loop: an email you did not check arrived is an email you hope arrived."),
        ],
        test=(
            "Google Drive and Gmail are connected. Claude read both CSV files from the Lumo "
            "Launch folder, showed a budget table totalling S$60,000 on both sides, and flagged "
            "Instagram (S$18,000 vs S$20,000) and Influencers (S$12,000 vs S$10,000) without "
            "choosing between them. lumo-research-brief.docx is in the Drive folder, and the "
            "approved summary email arrived in your own inbox with a working link."
        ),
    ),
    dict(
        num=5, topic=2,
        title="Create the Launch Deck and Campaign Brief",
        objective="produce a launch deck in Slides and a campaign brief in Docs from the project's research",
        desc=(
            "The launch team meets on Friday and needs two things: a short deck for the room "
            "and a campaign brief everyone can work from. You ask the project for both. Claude "
            "builds the deck in Slides and the brief in Docs, choosing its built-in skills on "
            "its own, using the numbers from your research and dashboard. You check every "
            "figure, then download the deck as PowerPoint."
        ),
        build="An eight-slide launch deck in Slides (downloaded as .pptx) and a campaign brief in Docs.",
        services="Claude Projects, Slides, Docs, built-in skills",
        data=[],
        prompt_step=1,
        prompt_title="Build the launch deck and campaign brief",
        prompt=(
            "Using our research brief, the Market Insights dashboard and the\n"
            "brand kit, create two things for Friday's launch meeting.\n"
            "\n"
            "1. A launch deck in Slides, eight slides:\n"
            "   1 Title - Lumo Cold Kopi: Kopi, Chilled Right\n"
            "   2 The opportunity - the three survey numbers that matter most\n"
            "   3 Who we are for - 25-34s in Singapore, with the evidence\n"
            "   4 Competitors - a price ladder chart with Lumo highlighted\n"
            "   5 Where they find us - a discovery channel chart\n"
            "   6 The campaign - message, channels and dates\n"
            "   7 Budget - the S$60,000 split, noting the two open questions\n"
            "   8 Next steps and owners\n"
            "\n"
            "   Use the Lumo brand colours. Real charts, not pictures of charts.\n"
            "\n"
            "2. A campaign brief in Docs: objective, audience, key message,\n"
            "   proof points, channels, budget, timeline, KPIs, and a \"claims\n"
            "   we must not make\" section.\n"
            "\n"
            "Every number must come from the research brief or the dashboard.\n"
            "List the source of each number at the end of the brief."
        ),
        prompt_note="You do not name a skill. Ask for a deck and a document; Claude picks the format and the built-in skill.",
        steps=[
            ("In the project, send the lab prompt.",
             "No attachments: the research brief, the dashboard data and the brand kit are all already in the project."),
            ("Open the deck when it appears and page through all eight slides.",
             "Check the charts are real charts — click one; a real chart has editable data behind it."),
            ("Check slide 2 and slide 4 against your research.",
             "62% likely to buy, 74% among 25-34s, Instagram 34%; a price ladder from S$3.20 to S$5.60 with Lumo at S$3.90."),
            ("Check slide 7.",
             "The S$60,000 split should carry the two open questions from Lab 4 — Instagram and Influencers — not quietly pick one figure."),
            ("Open the campaign brief in Docs and read the \"claims we must not make\" section.",
             "It should rule out \"healthy\" and any claim the product sheet does not support. This section protects every post you write later."),
            ("Ask for one change to each, for example: Shorten slide 6 to three bullets.",
             "Slides and Docs are edited in place by conversation, the same way as an artefact."),
            ("Download the deck as PowerPoint and open it.",
             "The download is the file you take into the meeting — check the charts survived."),
        ],
        test=(
            "The deck has eight slides in the Lumo colours, with real charts for the price "
            "ladder and the discovery channels, the survey figures 62%, 74% and 34%, and a "
            "budget slide that shows S$60,000 with the Instagram and Influencers lines marked "
            "as open questions. The campaign brief in Docs has all nine sections, including "
            "\"claims we must not make\", and lists a source for every number. The deck opens "
            "in PowerPoint with its charts intact."
        ),
    ),
    dict(
        num=6, topic=2,
        title="Capture the Brand Voice as an Agent Skill",
        objective="rewrite content in the brand voice, verify it, and save the routine as a skill with /skill-creator",
        desc=(
            "Four channels and two weeks of posts are coming, and they all have to sound like "
            "Lumo. You rewrite five off-brand captions with Claude until they are right, then "
            "use /skill-creator to turn that verified routine into a lumo-brand-voice skill. "
            "From then on, every thread in the project — and every colleague — loads the same "
            "voice by name."
        ),
        build="A lumo-brand-voice Agent Skill, tested on a new caption.",
        services="Claude Projects, Agent Skills, /skill-creator",
        data=["lumo-sample-captions.txt"],
        prompt_intro=("This lab has **three blocks**, sent at different times. Block 1 does the "
                      "work once. Block 2 saves it as a skill — type /skill-creator first. "
                      "Block 3 tests the skill on something new."),
        prompt_intro_md=("This lab has **three blocks**, sent at different times.\n"
                         "Block 1 does the work, Block 2 saves it with /skill-creator, Block 3 tests it."),
        prompt_intro_lg=("This lab has three blocks, sent at different times. Block 1 does the work "
                         "once so you can verify it. Block 2 saves it as a skill: type /skill-creator "
                         "in the composer, then paste the block. Block 3 tests the saved skill."),
        prompt_title="Rewrite, verify, then save the brand voice",
        prompt_blocks=[
            dict(
                label="Block 1 — DO", step=2,
                lead="Attach lumo-sample-captions.txt and send this first, on its own:",
                text=(
                    "Rewrite the five captions in the attached file in the Lumo\n"
                    "brand voice, following lumo-brand-guidelines.md.\n"
                    "\n"
                    "For each caption, show:\n"
                    "- the original\n"
                    "- your rewrite\n"
                    "- every rule you applied, by name\n"
                    "- any claim you removed, and why\n"
                    "\n"
                    "Then run these checks on each rewrite and show the result:\n"
                    "price written as S$3.90; no \"healthy\" or medical claims; at\n"
                    "most one Singlish word; #LumoKopi present; no more than five\n"
                    "hashtags; ends with one clear call to action."
                ),
                after=("**Now stop and read the output.** Ask for changes until every rewrite "
                       "sounds right. Whatever you settle on here is exactly what the skill "
                       "will reproduce."),
                after_md=("**Stop here.** Read the rewrites and refine them until they are right.\n"
                          "Whatever you settle on is what the skill will reproduce."),
                slide_note="Stop here. Refine the rewrites until they are right before you save anything.",
            ),
            dict(
                label="Block 2 — SAVE", step=4,
                lead="Type /skill-creator in the composer, then paste this:",
                text=(
                    "Create a skill called lumo-brand-voice from what we just did.\n"
                    "\n"
                    "Description: Use when writing or reviewing any customer-facing\n"
                    "Lumo Kopi content - social posts, captions, emails, video\n"
                    "scripts or ads.\n"
                    "\n"
                    "It should rewrite or draft content in the Lumo voice, apply the\n"
                    "brand rules, remove claims we cannot prove, and finish with the\n"
                    "same checklist of checks we used. Include two of today's\n"
                    "before-and-after examples as a resource."
                ),
                after="Approve the skill when Claude shows it to you, then open **Customize → Skills** and find it.",
                after_md="Approve the skill, then find it under **Customize → Skills**.",
                slide_note="Type /skill-creator first, then paste the block.",
            ),
            dict(
                label="Block 3 — TEST", step=7,
                lead="Start a new thread in the project and send:",
                text=(
                    "Use lumo-brand-voice to write an Instagram caption announcing\n"
                    "that Lumo Cold Kopi 12-packs are available on Shopee from\n"
                    "1 December. It's super healthy and the best kopi in Singapore!"
                ),
                after="The skill should load by itself, remove both unprovable claims and run its checklist.",
                after_md="The skill should load by itself and remove both unprovable claims.",
                slide_note="Both claims in this prompt are traps — the skill must remove them.",
            ),
        ],
        prompt_note="Block 2 begins with you typing /skill-creator in the composer — it is not part of the pasted text.",
        steps=[
            ("Open lumo-sample-captions.txt and read the five captions.",
             "Each breaks at least one brand rule — a wrong price format, a health claim, too much slang, too many hashtags."),
            ("In the project, attach the file and send Block 1.",
             "This is the Do step of Do · Verify · Save. You never write a skill from a blank page."),
            ("Check each rewrite against the brand guidelines and refine until all five are right.",
             "This is the Verify step. Ask for changes in plain English; you are teaching the routine by correcting it."),
            ("Type /skill-creator in the composer, then paste Block 2 and send.",
             "skill-creator writes the SKILL.md from the run you just verified — name, description, instructions and examples."),
            ("Read the skill Claude proposes, especially its description, and approve it.",
             "The description is the one part always in context. It decides when the skill loads, so it must say WHEN to use it."),
            ("Open Customize → Skills and find lumo-brand-voice.",
             "Your own skills are listed here. Built-in skills such as pptx are not — they show in the context panel when they load."),
            ("Start a new thread and send Block 3.",
             "A fresh thread proves the skill works without the earlier conversation — which is exactly how other threads will use it."),
            ("Check the caption: no \"healthy\", no \"best kopi in Singapore\", S$ prices, #LumoKopi present.",
             "Both claims were traps. A skill that removes them has learned the rule, not just the examples."),
        ],
        test=(
            "lumo-brand-voice appears under Customize → Skills with a description that says "
            "when to use it. In a fresh thread, Block 3 loaded the skill without being asked to "
            "find it, and the caption it returned drops \"healthy\" and \"best kopi in "
            "Singapore\", includes #LumoKopi, uses at most five hashtags and ends with one call "
            "to action, followed by the checklist results."
        ),
    ),
    dict(
        num=7, topic=2,
        title="Add the Marketing Plugin",
        objective="install a plugin and use its namespaced commands alongside your own skill",
        desc=(
            "You wrote one skill yourself; now you install a toolkit somebody else packaged. "
            "Anthropic's Marketing plugin bundles several marketing skills behind namespaced "
            "commands. You install it, use /marketing:campaign-plan to stress-test the launch "
            "plan, and run /marketing:brand-review on the deck copy — then compare a plugin "
            "with the skill you wrote, and see where mods fit."
        ),
        build="The Marketing plugin installed, a campaign plan review and a brand review of the launch copy.",
        services="Claude Projects, plugins, Customize",
        data=[],
        prompt_title="Stress-test the launch with the Marketing plugin",
        prompt_intro=("This lab has **two blocks**, each a command from the plugin. Install the "
                      "plugin first, then send Block 1 and, after you have read its answer, Block 2."),
        prompt_intro_md=("This lab has **two blocks**, each a plugin command. Install the plugin\n"
                         "first, then send them one at a time."),
        prompt_intro_lg=("This lab has two blocks, each a command from the Marketing plugin. Install "
                         "the plugin first, then send Block 1 and, after reading its answer, Block 2."),
        prompt_blocks=[
            dict(
                label="Block 1 — PLAN", step=4,
                lead="Send this in the project:",
                text=(
                    "/marketing:campaign-plan Review the Lumo Cold Kopi launch using\n"
                    "our campaign brief and research brief. Keep our objective,\n"
                    "audience, budget and dates. Tell me:\n"
                    "- what is missing from the plan,\n"
                    "- the three biggest risks to the 1 December launch,\n"
                    "- the KPIs you would track in the first two weeks, with targets.\n"
                    "Do not change the S$60,000 budget."
                ),
                after="Read its answer in full before you send Block 2.",
                after_md="Check the risks, KPIs and the unchanged S$60,000 budget.",
                slide_note="Install the plugin first: Customize → Plugins → Browse → Marketing → Install.",
            ),
            dict(
                label="Block 2 — REVIEW", step=6,
                lead="Then send:",
                text=(
                    "/marketing:brand-review Review the copy on slides 1, 2 and 6 of\n"
                    "our launch deck against lumo-brand-guidelines.md. List each\n"
                    "change you would make and the rule behind it."
                ),
                after="Compare its findings with what your lumo-brand-voice skill would flag.",
                after_md="Compare with what lumo-brand-voice would flag.",
                slide_note="The plugin reviews; your own skill holds the house rules.",
            ),
        ],
        prompt_note=("Install the plugin first: Customize → Plugins → Browse, find Marketing, "
                     "click Install. Then type /marketing in the composer to see its commands."),
        steps=[
            ("Open Customize → Plugins and browse the available plugins.",
             "Discover before you build: check whether someone has already packaged what you need."),
            ("Find the Marketing plugin, read what it contains, and click Install.",
             "One install brings several skills and commands at once — the difference between a plugin and a skill."),
            ("In the project composer, type /marketing and look at the commands it offers.",
             "Plugin commands carry the plugin's name as a prefix. That is how you tell them from a skill you wrote yourself."),
            ("Send Block 1 to stress-test the plan with /marketing:campaign-plan.",
             "The plugin's skill works with your project context: the campaign brief and research brief are already there."),
            ("Read the risks and KPIs it proposes, and check the budget is unchanged at S$60,000.",
             "A plugin is someone else's judgement. Keep what fits your goal; question what does not."),
            ("Send Block 2 to review the deck copy with /marketing:brand-review.",
             "Two tools on one job: the plugin reviews, and your lumo-brand-voice skill holds the house rules it checks against."),
            ("Open Customize and look at the Mods section.",
             "Mods change Claude's interface itself — a panel, a status line, a slash command or a hook. You will not build one today; know where they live."),
        ],
        test=(
            "The Marketing plugin is installed and its /marketing: commands appear in the "
            "composer. /marketing:campaign-plan returned the gaps, three launch risks and "
            "two-week KPIs with targets while keeping the S$60,000 budget and the 1 December "
            "date. /marketing:brand-review reviewed the deck copy. You can explain the "
            "difference between lumo-brand-voice (a skill you wrote), the Marketing plugin "
            "(a packaged bundle) and a mod (a change to Claude's interface)."
        ),
    ),
]
