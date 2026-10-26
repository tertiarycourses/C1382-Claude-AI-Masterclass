"""Topic 3 — Content Production and Scheduled Work. Labs 8-10.

Lab 8 is the second multi-thread job: the lead agent gives each social platform
its own thread, every thread loads the Lab 6 brand-voice skill, and the drafts
merge into one dated calendar. Lab 9 turns a script and the supplied brand
assets into a 15-second vertical video. Lab 10 schedules the routine work
inside the project, edits its memory and reads the usage of every thread.
"""

DOMAIN3 = [
    dict(
        num=8, topic=3,
        title="Create Social Media Posts in Parallel Threads",
        objective="produce a two-week, four-platform social calendar with one thread per channel",
        desc=(
            "Launch fortnight needs ten posts across Instagram, TikTok, LinkedIn and Facebook. "
            "Each platform has its own format, so you hand the job to the lead agent and let it "
            "start one thread per platform. Every thread loads lumo-brand-voice, drafts its "
            "posts to its platform's spec, and the lead agent merges them into one dated "
            "calendar that you check before anything is scheduled."
        ),
        build="social-calendar.csv with ten dated posts across four platforms, plus lumo-social-posts.docx with the full copy.",
        services="Claude Projects, lead agent and threads, Agent Skills",
        data=["social-calendar-template.csv"],
        prompt_step=1,
        prompt_title="Draft two weeks of posts, one thread per platform",
        prompt=(
            "Create the launch social calendar for Lumo Cold Kopi: ten posts,\n"
            "one each weekday from Tuesday 1 December to Monday 14 December\n"
            "2026, using social-calendar-template.csv for the columns.\n"
            "\n"
            "Split the drafting into four threads, one per platform, and run\n"
            "them in parallel:\n"
            "- Instagram: 3 posts (carousel or Reel), caption with a hook in\n"
            "  the first line, 3-5 hashtags.\n"
            "- TikTok: 3 posts, each a 15-second video script with a hook in\n"
            "  the first 2 seconds and on-screen text.\n"
            "- LinkedIn: 2 posts in the founder's voice, the story behind the\n"
            "  product, no more than 3 hashtags.\n"
            "- Facebook: 2 posts for community and the 12-pack offer.\n"
            "\n"
            "Every thread must use the lumo-brand-voice skill and our top\n"
            "content theme from the research. The 1 December launch-day\n"
            "post is an Instagram Reel; TikTok follows on 2 December.\n"
            "\n"
            "Then merge the threads into social-calendar.csv (date, platform,\n"
            "format, hook, copy, hashtags, visual idea, call to action) and\n"
            "lumo-social-posts.docx with the full copy. Report the brand-voice\n"
            "checklist result for every post, and list any post that failed."
        ),
        prompt_note="Attach social-calendar-template.csv from the Lab 08 data folder.",
        steps=[
            ("In the project, attach social-calendar-template.csv and send the lab prompt.",
             "This is the same pattern as Lab 2 — one message, independent subjects — applied to production instead of research."),
            ("Watch the lead agent start the four platform threads.",
             "Each thread has its own spec and its own context window, so the TikTok scripts never crowd out the LinkedIn story."),
            ("Open the Instagram thread and check it loaded lumo-brand-voice.",
             "The skill you wrote in Lab 6 is now doing its real job: keeping four parallel writers on one voice."),
            ("When the merged calendar arrives, count the rows and check the dates.",
             "Ten rows, weekdays only: 1, 2, 3, 4, 7, 8, 9, 10, 11 and 14 December. Instagram 3, TikTok 3, LinkedIn 2, Facebook 2."),
            ("Read the brand-voice checklist results.",
             "Every post should pass. If one fails, ask the lead agent to send it back to its thread for a fix."),
            ("Spot-check three posts against the campaign brief's \"claims we must not make\".",
             "Parallel production is fast; a human check on the claims is what makes it safe to publish."),
            ("Open lumo-social-posts.docx and confirm the copy matches the calendar.",
             "The calendar is what Lab 10's scheduled task reads every morning."),
        ],
        test=(
            "social-calendar.csv has ten rows dated on the ten weekdays from 1 to 14 December "
            "2026 — Instagram 3, TikTok 3, LinkedIn 2, Facebook 2 — with the 1 December launch "
            "post an Instagram Reel and TikTok on 2 December. Every post passed the lumo-brand-voice checklist, none "
            "uses \"healthy\", every price is written S$3.90 or S$42.00, and "
            "lumo-social-posts.docx carries the same copy."
        ),
    ),
    dict(
        num=9, topic=3,
        title="Produce a 15-Second Launch Video",
        objective="script, storyboard and render a vertical launch video from supplied brand assets",
        desc=(
            "The TikTok and Instagram posts need a launch video. You give the project the "
            "supplied product images and logo; one thread writes a five-scene script and "
            "storyboard with lumo-brand-voice, another writes and runs the code that animates "
            "the images and captions into a 15-second, 1080 × 1920 MP4. You check it frame by "
            "frame and ask for changes in plain English."
        ),
        build="lumo-launch-15s.mp4 (1080 × 1920, 15 seconds), with its script and storyboard.",
        services="Claude Projects, threads, code execution",
        data=["video-assets/lumo-can.png", "video-assets/lumo-12pack.png",
              "video-assets/lumo-logo.png", "video-assets/scene-hawker.png",
              "video-assets/scene-office.png"],
        prompt_step=2,
        prompt_title="Script, storyboard and render the video",
        prompt=(
            "Make a 15-second vertical launch video for Lumo Cold Kopi, using\n"
            "only the five images in the attached video-assets folder.\n"
            "\n"
            "Use two threads:\n"
            "Thread 1 - SCRIPT: with lumo-brand-voice, write five scenes of\n"
            "  three seconds each: hook, problem, product, proof, call to action.\n"
            "  For each scene give the image, the on-screen text (max 6 words)\n"
            "  and the motion. Save it as lumo-video-storyboard.md.\n"
            "Thread 2 - RENDER: when the storyboard is ready, write and run\n"
            "  code that renders it to lumo-launch-15s.mp4: 1080 x 1920, 30 fps,\n"
            "  exactly 15 seconds, large high-contrast captions in the Lumo\n"
            "  colours, a gentle zoom on each image, and an end card with the\n"
            "  logo, \"From S$3.90\" and #KopiChilledRight.\n"
            "\n"
            "If you cannot render video in this session, build the same thing\n"
            "as an animated HTML page at 1080 x 1920 and tell me, so I can\n"
            "screen-record it. Report the file's duration and size when done."
        ),
        prompt_note=("Attach the whole video-assets folder. Use only the supplied images — "
                     "never a real person's likeness or another brand's logo."),
        steps=[
            ("Open the Lab 09 data/video-assets folder and look at the five images.",
             "These are the only images the video may use. Supplying assets is how you keep likenesses and logos safe."),
            ("In the project, attach the folder and send the lab prompt.",
             "Two threads, but not in parallel this time: the render thread waits for the script. The lead agent manages that order."),
            ("Read the storyboard when Thread 1 finishes.",
             "Five scenes, three seconds each, captions of six words or fewer, and no health claims — the brand-voice skill applies to scripts too."),
            ("When the video arrives, check the reported duration and size.",
             "Exactly 15 seconds and 1080 × 1920. A wrong size is the most common reason a platform crops your captions."),
            ("Play it through, then scrub it frame by frame.",
             "Check every caption is readable with the sound off and the end card shows the logo, From S$3.90 and #KopiChilledRight."),
            ("Ask for one change, for example: Hold the end card for one second longer and shorten scene 2.",
             "The video is code, so a change is a re-render, not a re-edit. Check the length is still 15 seconds afterwards."),
            ("If Claude built the HTML fallback instead, open it full screen and screen-record 15 seconds.",
             "Same storyboard, different renderer. The checks stay the same."),
        ],
        test=(
            "lumo-launch-15s.mp4 is 1080 × 1920, 30 fps and 15 seconds long, uses only the "
            "supplied images, shows five scenes with captions of six words or fewer in the Lumo "
            "colours, and ends on a card with the logo, \"From S$3.90\" and #KopiChilledRight. "
            "lumo-video-storyboard.md sits beside it and matches what plays. No scene makes a "
            "health claim."
        ),
    ),
    dict(
        num=10, topic=3,
        title="Schedule the Posts and Review the Project",
        objective="schedule recurring project tasks, edit project memory and review thread usage",
        desc=(
            "The launch needs a post drafted every weekday morning and a report every Monday, "
            "and nobody should have to remember either. You schedule both inside the project, "
            "test one with Run now, then do the housekeeping a real project needs: correct its "
            "memory when a plan changes, and read the usage of the lead agent and each thread "
            "to see what parallel work costs."
        ),
        build="Two scheduled tasks in the project, a tested daily-post email, an updated memory file and a usage review.",
        services="Claude Projects, scheduled tasks, memory, Gmail connector",
        data=[],
        prompt_intro=("This lab has **three blocks**. Block 1 schedules the two tasks. Block 2 "
                      "changes the plan through memory. Block 3 is a review you send at the end."),
        prompt_intro_md=("This lab has **three blocks**: schedule, change the plan through memory,\n"
                         "then review."),
        prompt_intro_lg=("This lab has three blocks. Block 1 schedules the two recurring tasks. "
                         "Block 2 changes the launch plan through project memory. Block 3 asks "
                         "the project to review itself."),
        prompt_title="Schedule, update memory, review",
        prompt_blocks=[
            dict(
                label="Block 1 — SCHEDULE", step=1,
                lead="Send this to the lead agent:",
                text=(
                    "Schedule two recurring tasks in this project.\n"
                    "\n"
                    "Task 1 - \"Today's Lumo post\", every weekday at 9:00am:\n"
                    "take today's row from social-calendar.csv, polish it with\n"
                    "lumo-brand-voice, check every price and claim against the brand\n"
                    "kit, and email it to <YOUR EMAIL> as a draft with the subject\n"
                    "\"Today's Lumo post - <date>\". Never publish anything.\n"
                    "\n"
                    "Task 2 - \"Weekly launch report\", Mondays at 8:00am:\n"
                    "summarise last week's posts from the calendar and anything new\n"
                    "in the Lumo Launch Drive folder in five bullet points, and\n"
                    "email it to <YOUR EMAIL>.\n"
                    "\n"
                    "Show me both tasks before you save them, then run Task 1 once\n"
                    "now as a test, using 1 December 2026 as today."
                ),
                after="Check the test email in your inbox, then open **Scheduled** and confirm both tasks are listed with the right times.",
                after_md="Check the test email, then confirm both tasks under **Scheduled**.",
                slide_note="Replace <YOUR EMAIL>. The task drafts and emails — it never publishes.",
            ),
            dict(
                label="Block 2 — MEMORY", step=5,
                lead="Send this to the lead agent:",
                text=(
                    "Remember this for the project: the Singapore launch has moved\n"
                    "from 1 December to 8 December 2026. Kuala Lumpur is unchanged.\n"
                    "Tell me everything in the project that depends on the launch\n"
                    "date - posts, tasks, the deck, the brief - and propose the\n"
                    "changes. Do not make them yet."
                ),
                after="Open **Project settings → Memory**, find the new entry, and correct the wording if needed.",
                after_md="Find the entry in **Project settings → Memory** and check it.",
                slide_note="Then open Project settings → Memory and check what it wrote.",
            ),
            dict(
                label="Block 3 — REVIEW", step=7,
                lead="Send this at the end of the lab:",
                text=(
                    "Review this project for me: list the threads you started today,\n"
                    "what each produced, and where each output is saved. Then tell\n"
                    "me which context files, instructions or memory entries are now\n"
                    "out of date."
                ),
                after="Compare its list with **Project settings → Usage**, which shows the tokens used by the lead agent and each thread.",
                after_md="Compare its answer with **Project settings → Usage**.",
                slide_note="Then open Project settings → Usage and compare.",
            ),
        ],
        prompt_note=("Scheduled tasks that run locally need the desktop app open. To run them "
                     "with your laptop closed, add a cloud environment in Project settings → Environment."),
        steps=[
            ("Send Block 1 with your own email address in place of <YOUR EMAIL>.",
             "The tasks run inside the project, so they inherit the goal, instructions, context, memory and the brand-voice skill — the prompt stays short."),
            ("Read both tasks before they are saved: name, prompt, frequency and time.",
             "Weekdays at 9:00am and Mondays at 8:00am. A task scheduled at the wrong time is a silent failure."),
            ("Open your inbox and read the test email for 1 December.",
             "It should be the Instagram launch Reel from your calendar, polished, with S$ prices and no \"healthy\" claim — a draft, not a published post."),
            ("Open Scheduled in the project and confirm both tasks are listed.",
             "From here you can pause, edit or run a task now. This is where you would schedule a monthly competitor scan next."),
            ("Send Block 2, then read the list of things that depend on the date.",
             "Expect the calendar, Task 1, the deck's title slide and timeline, and the brief. Memory is how one fact reaches every thread."),
            ("Open Project settings → Memory and find the new launch-date entry. Edit it if the wording is wrong.",
             "The project writes memory, but you own it. Delete anything you would not want every future thread to believe."),
            ("Send Block 3 at the end of the lab.",
             "A project that can list its own threads and outputs is one a colleague can pick up tomorrow."),
            ("Open Project settings → Usage and read the lead agent's and each thread's tokens.",
             "Parallel threads finish faster but use more in total. Compare the research threads from Lab 2 with the single-thread labs."),
        ],
        test=(
            "Two tasks are listed under Scheduled — Today's Lumo post on weekdays at 9:00am and "
            "Weekly launch report on Mondays at 8:00am. The test run emailed you a polished 1 "
            "December post as a draft, with S$ prices and no health claim, and nothing was "
            "published. Project memory records the 8 December Singapore launch, and the lead "
            "agent listed what depends on it. Project settings → Usage shows tokens for the lead "
            "agent and for each thread you started today."
        ),
    ),
]
