# Claude AI Masterclass — Learner Guide

**Classic Projects Edition**  |  **Course Code:** C1382  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v5.1 · 27 October 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Working in a Claude Project](#working-in-a-claude-project)
  - [How a project is organised](#how-a-project-is-organised)
  - [The parts of a project](#the-parts-of-a-project)
  - [Creating the project](#creating-the-project)
  - [Writing project instructions](#writing-project-instructions)
  - [Adding context and using the folder](#adding-context-and-using-the-folder)
  - [Keeping a memory file](#keeping-a-memory-file)
  - [Scheduling tasks](#scheduling-tasks)
  - [Coming soon: the new Projects](#coming-soon-the-new-projects)
- [Topic 01 — Claude Projects and Market Research](#topic-01--claude-projects-and-market-research)
  - [The Claude family](#the-claude-family)
  - [Lab 1 — Set Up the Lumo Launch Project](#lab-1--set-up-the-lumo-launch-project)
  - [Market research in parallel tasks](#market-research-in-parallel-tasks)
  - [Lab 2 — Run Market Research in Parallel Tasks](#lab-2--run-market-research-in-parallel-tasks)
  - [Live Artefacts](#live-artefacts)
  - [Lab 3 — Build the Market Insights Live Artefact](#lab-3--build-the-market-insights-live-artefact)
- [Topic 02 — Connectors, Skills and Plugins](#topic-02--connectors-skills-and-plugins)
  - [Connectors and the context window](#connectors-and-the-context-window)
  - [Lab 4 — Connect Google Drive and Gmail](#lab-4--connect-google-drive-and-gmail)
  - [Slides, Docs and built-in skills](#slides-docs-and-built-in-skills)
  - [Lab 5 — Create the Launch Deck and Campaign Brief](#lab-5--create-the-launch-deck-and-campaign-brief)
  - [Agent Skills](#agent-skills)
  - [Lab 6 — Capture the Brand Voice as an Agent Skill](#lab-6--capture-the-brand-voice-as-an-agent-skill)
  - [Skills, plugins and mods](#skills-plugins-and-mods)
  - [Lab 7 — Add the Marketing Plugin](#lab-7--add-the-marketing-plugin)
- [Topic 03 — Content Production and Scheduled Work](#topic-03--content-production-and-scheduled-work)
  - [Social content for four platforms](#social-content-for-four-platforms)
  - [Lab 8 — Create Two Weeks of Social Media Posts](#lab-8--create-two-weeks-of-social-media-posts)
  - [The video pipeline](#the-video-pipeline)
  - [Lab 9 — Produce a 15-Second Launch Video](#lab-9--produce-a-15-second-launch-video)
  - [Scheduled tasks](#scheduled-tasks)
  - [Lab 10 — Schedule the Posts and Review the Project](#lab-10--schedule-the-posts-and-review-the-project)
- [Wrap-Up](#wrap-up)
- [Glossary](#glossary)


## Introduction

Claude is no longer only a chat window. In Cowork, a Claude Project gives one body of work its own instructions, reference files and working folder, so every task you start already knows the brand and the rules. This course teaches that way of working through one continuous marketing scenario: you are the marketing team at Lumo Kopi Co., launching a new canned cold-brew kopi. Over ten labs, all inside one project, you research the market in parallel tasks, build a Live Artefact dashboard, connect Google Drive and Gmail, produce a launch deck and campaign brief, capture the brand voice as a skill, add a marketing plugin, create two weeks of social posts and a launch video, and schedule the routine work so it runs on its own.

#### The scenario — The Lumo Cold Kopi launch

**The situation:** It is late October 2026. Lumo Kopi Co. launches Lumo Cold Kopi, its first ready-to-drink canned kopi, in Singapore on 1 December — six weeks away — and in Kuala Lumpur in January. The marketing team is small, the budget is S$60,000, and nothing has been produced yet: no research, no deck, no posts, no video.

**Your role:** You are the Lumo marketing team. Instead of juggling a dozen separate chats, you run the whole launch from one Claude Project in Cowork: its instructions, brand kit and working folder are set up once, and every task you start inside it already knows the brand.

**Your mission:** By the end of the day the project holds everything the launch needs — verified market research, a dashboard, a deck and brief, a brand-voice skill, two weeks of social posts, a launch video — and scheduled tasks that keep it moving while you are away.

Lumo Kopi Co. is a fictitious Singapore coffee brand about to launch Lumo Cold Kopi — a ready-to-drink oat-milk kopi cold brew in a 240 ml can — in Singapore on 1 December 2026 and Kuala Lumpur in January 2027. You are its marketing team. All brands, figures, survey answers and documents in this course are synthetic and used for training only.

This guide carries the full instructions for all 10 labs. Each lab folder in the course repository holds only the lab's prompt PDF and, where the lab needs it, a data folder; the goal, every prompt, the step-by-step instructions and the check step for each lab are here.


## Course Learning Outcomes

On completion of this course, you will be able to:

- LO1: Set up a Claude Project in Cowork with instructions, context, a working folder and a project memory file.
- LO2: Run multi-subject market research as parallel tasks in one project and consolidate it into one verified research brief.
- LO3: Build, refine, save and download a Live Artefact dashboard from supplied research data.
- LO4: Connect Google Drive and Gmail so Claude reads campaign files and sends an approved summary.
- LO5: Produce a launch deck and a campaign brief with Claude's Slides and Docs, using built-in skills.
- LO6: Capture a brand voice as an Agent Skill with /skill-creator, and install and use a marketing plugin.
- LO7: Create a two-week, multi-platform set of social media posts using the brand-voice skill.
- LO8: Produce a short vertical launch video from a script, storyboard and supplied brand assets.
- LO9: Schedule recurring project tasks and keep the project's instructions, context and memory file current, with a human approval step.


## Before You Start — Preparation

#### What you need

- A laptop (Mac or Windows) with the Claude desktop app installed from claude.ai/download.
- A Claude account on a paid plan (Pro or Max) — Projects, Cowork and Live Artefacts are paid-plan features.
- A Google account with Google Drive and Gmail, used for the connector labs.
- The course labs downloaded from https://github.com/tertiarycourses/C1382-Claude-AI-Masterclass — each lab folder holds a prompt PDF and, where needed, a data folder.
- The prompts page open in a browser, so you can copy each prompt with one click: https://tertiarycourses.github.io/C1382-Claude-AI-Masterclass/prompts/

#### Verify your setup

Open the Claude desktop app, sign in, switch to Cowork and open Projects. If you can start a new project and see its Instructions, Context, Folder and Scheduled panels, your setup is ready. (If your Projects page instead offers a Goal and talks about a lead agent and threads, your account has the new Projects — use the Threads edition of the labs.)

#### Course links

| Resource | Address |
|---|---|
| Course repository (lab files) | https://github.com/tertiarycourses/C1382-Claude-AI-Masterclass |
| Copy-ready prompts page | https://tertiarycourses.github.io/C1382-Claude-AI-Masterclass/prompts/ |

#### Conventions used in every lab

- Prompts shown in a bordered box are copied into Claude exactly as they are — or copy them from the prompts page.
- Placeholders such as `<YOUR EMAIL>` are replaced with your own values.
- All Lumo Kopi data is synthetic; use only the supplied mock data.
- Every lab ends with a check step — confirm the output before moving on.

#### Rules for every lab

- **Work from mock data** — Use the supplied synthetic Lumo data — never real customer records in training.
- **Scope the connector** — Give Claude one Drive folder for the task, not your entire Drive.
- **Check every figure** — Read the artefact's and the brief's numbers back against the source file.
- **Approve before sending** — Read each drafted email and post in full; approve it only when the facts match.
- **Use a test recipient** — Send class exercises to yourself, never to a real customer.
- **Draft-only schedules** — A scheduled task runs unattended — let it draft and email you, never publish.

> **Note:** Use only the supplied mock data and your own test accounts. Never put real customer, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.


## Working in a Claude Project

Every lab in this course runs inside one Claude Project — Lumo Cold Kopi Launch — which you create in Lab 1. This chapter explains how a project works and how to set up each of its parts. Come back to it whenever a lab asks you to change the goal, instructions, context, memory or a scheduled task.


### How a project is organised

A folder-backed project with four panels. Every task you start in the project reads its instructions, context and folder. Start several at once and they run in parallel — one task per subject.

- **Instructions** — Rules every task follows
- **Context** — Files Claude reads
- **Folder** — Where Claude works
- **Scheduled** — Tasks on a timetable
- **Your tasks** — Run one or several at once
- **Memory file** — Decisions kept in the folder

How this changes the way you work:

| One-off chats | A Claude Project in Cowork |
|---|---|
| A chat for copy, one for visuals, one for competitors. | Instructions written once, followed by every task. |
| Re-attach the brand kit every time. | The brand kit added once as context. |
| Restate the rules from memory each time. | A real working folder Claude reads and writes. |
| Outputs scattered across conversations. | Scheduled tasks that belong to the project. |
| Nothing for a colleague to pick up. | Hand the folder to a colleague and they are ready. |

#### When to use a project

| Use a project for | Why |
|---|---|
| A long-running goal | Work keeps arriving for weeks — a product launch, a channel, an app. |
| A job that splits | One big job breaks into pieces that can run at once — assets, ads, competitors, email. |
| Lots of research | Many subjects to look into — one task per competitor, market or segment. |
| Regular routines | Work that repeats on a timetable — scheduled tasks that belong to the project. |

A one-off question that is done in one reply? Use an ordinary chat.


### The parts of a project

| Part | What it is |
|---|---|
| Instructions | Standing rules you write: brand voice, currency, never publish without approval. |
| Context | Documents Claude READS and never edits — the brand guidelines, product sheet and launch brief. |
| Folder | A real folder on your computer where Claude WORKS: it reads the data there and writes output back. |
| Scheduled | Recurring tasks that belong to this project — the daily post draft, the weekly report. |
| Tasks | Each job you start in the project. Several can run at once, one per subject. |
| Memory file | lumo-project-memory.md in the folder: decisions you ask Claude to record, read by every later task. |

#### Creating a project

1. **What are you working on?** — The project's name — Lumo Cold Kopi Launch. This is how you find it in the sidebar.
2. **What are you trying to achieve?** — The goal in two or three sentences. Every task in the project inherits it.
3. **Use a folder** — Point the project at a folder on your computer, so the files and outputs are yours to open.
4. **Create project** — The project page opens with four panels: Instructions, Context, Folder and Scheduled.

Start a new project from Projects in Cowork. The instructions and context are added afterwards, from the project page.

#### Instructions, context and memory compared

These three are easy to confuse, and the difference matters: when an output is wrong, it tells you which one to fix.

|  | Instructions | Context | Memory file |
|---|---|---|---|
| Who writes it | You | You add it | Claude, when you ask it to |
| What it holds | Rules and style | Files to read | Decisions and facts to keep |
| Lumo example | Prices in S$; no health claims | Brand guidelines, launch brief | Launch date moved to 8 December |
| Edit it in | The Instructions panel | The Context panel | lumo-project-memory.md in the folder |
| When output is wrong | Tighten the rule | Add the missing file | Correct the line in the file |


### Creating the project

In Cowork, a project is created from a short dialog with two questions and a folder. The name is how you find it again; the answer to "What are you trying to achieve?" is the standing goal every task in the project inherits.

Point the project at a folder you create for it. That folder is where Claude works — it reads the data you put there and writes every output back — and it stays a normal folder you can open, back up or share.

**Example**

*EXAMPLE — Lumo Kopi*

```text
Launch Lumo Cold Kopi in Singapore on 1 December 2026. Produce the
research, launch deck, campaign brief, two weeks of social posts and a
15-second launch video, within a S$60,000 budget, so that 25-34
year-olds on Instagram and TikTok know the product exists by launch day.
```

**How to do it**

1. In Cowork, open Projects and start a new project.
2. Type the name, paste the goal into What are you trying to achieve?, and choose Use a folder.
3. Click Create project. The project page opens with its four panels.


### Writing project instructions

Instructions are standing rules that apply to every task in the project. Use them for things that are always true: the currency, the brand voice in brief, what must never happen without your approval.

Keep them short and testable. A rule Claude can check — "prices always in S$ with two decimals" — works far better than a wish such as "be professional".

**Example**

*EXAMPLE — Lumo Kopi*

```text
You are the marketing team for Lumo Kopi Co.
- Prices are in Singapore dollars: S$3.90 per can, S$42.00 per 12-pack.
- Follow lumo-brand-guidelines.md for anything customer-facing.
- Never describe the product as healthy; you may say 5 g sugar.
- Never send an email or publish a post without my approval.
- Save outputs to the project folder with the date in the filename.
```

**How to do it**

1. On the project page, open the Instructions panel.
2. Paste the instructions and save.
3. Start a new task and check that the rules are followed without you repeating them.


### Adding context and using the folder

Context is what the project reads: the brand guidelines, the product sheet, the launch brief. Claude reads context but does not edit it, so it is the right home for reference material you want kept exactly as it is.

The Folder is different: it is where Claude works. Data it should analyse and every file it produces live there. Mixing the two up is the most common setup mistake — reference in Context, working files in the Folder.

**How to do it**

1. On the project page, open Context and add the reference files.
2. Put the lab's data files in the project folder on your computer.
3. Ask: "Which context files and folder files can you see, and what is each one for?"


### Keeping a memory file

A classic project has no memory panel of its own, so keep one yourself: a Markdown file in the project folder — lumo-project-memory.md — where Claude records decisions you ask it to remember. Every later task can read it.

Because Claude writes it, check it. Open the file from time to time, correct anything out of date and delete anything you do not want every future task to believe. It is a shared notebook that you are responsible for.

**Example**

*EXAMPLE — Lumo Kopi*

```text
Add this to lumo-project-memory.md: the Singapore launch date has moved
from 1 December to 8 December 2026. Update anything you have planned
that depends on it.
```

**How to do it**

1. Ask Claude to create lumo-project-memory.md in the project folder (Lab 1 does this).
2. Tell Claude what to record whenever a decision changes.
3. Open the file yourself and correct or delete lines as needed.


### Scheduling tasks

A scheduled task is a prompt that runs on a timetable. Pick the project in the task's settings and it runs with the project's instructions, context and folder — you do not repeat them in the task.

Schedule drafts, not publishing. Permissions defaults to Automatically approve, so the task acts unattended: it should prepare today's post and email it to you for approval, and the click that publishes stays yours.

**Example**

*EXAMPLE — Lumo Kopi*

```text
Take today's row from social-calendar.csv, polish the post with
lumo-brand-voice, check every price and claim against the brand kit, and
email it to me as a draft with the subject "Today's Lumo post". Never
publish anything.
```

**How to do it**

1. Open Scheduled tasks from the sidebar and choose New task → Set up manually.
2. Enter the Name and paste the Instructions; pick the Lumo Cold Kopi Launch project.
3. Change Frequency from Manual to the timetable you want, and check Permissions.
4. Save, then check the email that arrives at the first run.


### Coming soon: the new Projects

Anthropic redesigned Claude Projects in September 2026. The new version is in beta, rolling out to Pro and Max accounts first — if your Projects page shows a Goal and talks about threads, you already have it.

| Feature | What it does |
|---|---|
| Lead agent | You state a goal once; a coordinator plans the work, splits it and merges the results. |
| Parallel threads | The lead agent starts one thread per subject itself — what you do by hand with tasks in Lab 2. |
| Goal | One outcome statement that every decision in the project steers toward. |
| Project memory | Memory the project writes and you edit in settings — replacing the memory file you keep in Lab 1. |
| Usage per thread | Project settings show the tokens used by the lead agent and by each thread. |
| Cloud environment | Threads keep working in the cloud with your laptop closed. |

#### What changes in the labs

| In today's labs (classic) | With the new Projects |
|---|---|
| Lab 2: you start four tasks, then a merge task | One message; the lead agent starts four threads and merges them |
| Lab 8: one task drafts all four platforms | One thread per platform, merged into one calendar |
| lumo-project-memory.md in the folder | Project settings → Memory, editable memory files |
| Instructions panel | Project instructions under settings, plus a Goal |
| Settings → Usage for your whole plan | Usage per thread for this project |

Everything you build today carries over: skills, connectors, artefacts and scheduled tasks work the same way. The Threads edition of this course runs the same ten labs on the new Projects — see the course repository.


## Topic 01 — Claude Projects and Market Research

The Claude family · Projects in Cowork · instructions, context and folder · market research · Live Artefacts

#### Key concepts

| Concept | What it means |
|---|---|
| Claude Project | A home for a long-running body of work. Its rules, files and outputs build up instead of resetting each chat. |
| Backed by a folder | In Cowork a project points at a real folder on your computer — Claude works there, and you can open it yourself. |
| Instructions | Standing rules every task in the project follows: currency, brand voice, approval before sending. |
| Context vs Folder | Context is what Claude reads and never edits. Folder is where it works — reading data and writing output. |
| Parallel tasks | Several tasks can run in one project at once — one per subject — and a final task merges their files. |
| Live Artefacts | Interactive tools — dashboards, trackers — that persist in your workspace instead of scrolling away in chat. |


### The Claude family

| Product | Role | What it does |
|---|---|---|
| Claude (Chat + Cowork) | Thinking and work partner — this course | • Chat: ask, draft, analyse and research with web search<br>• Cowork: plans and runs multi-step tasks on your files<br>• Projects, connectors and skills: Drive, Gmail, Calendar<br>• For everyone — web, desktop and mobile apps |
| Claude Code | Build partner | • Builds software, sites and automations<br>• Runs in the terminal, VS Code, desktop app and web<br>• Edits files, runs commands and calls MCP tools<br>• Extended with CLAUDE.md, skills, sub agents and hooks |

Chat and Cowork are now one app: Claude. A marketing team works there — and a Project ties the work together around one goal.


### Lab 1 — Set Up the Lumo Launch Project

**Objective:** By the end of this lab you can create a Claude Project in Cowork with instructions, context, a working folder and a memory file.

**Scenario:** Lumo Kopi Co. launches Lumo Cold Kopi in six weeks, and the marketing work will keep coming until launch day — exactly what a Claude Project is for. You create the Lumo Cold Kopi Launch project in Cowork, point it at a working folder, write its standing instructions, add the brand kit as context, and check that Claude understood all of it. Every later lab runs inside this project.

**You will build:** The Lumo Cold Kopi Launch project, with instructions, three context files, a working folder and a project memory file.

**Tools:** Claude desktop app (Cowork), Claude Projects.

#### Lab files

- Prompt PDF: labs/lab-01-set-up-the-launch-project/lab-01-set-up-the-launch-project.pdf
- labs/lab-01-set-up-the-launch-project/data/brand-kit/lumo-brand-guidelines.md
- labs/lab-01-set-up-the-launch-project/data/brand-kit/lumo-product-sheet.md
- labs/lab-01-set-up-the-launch-project/data/brand-kit/lumo-launch-brief.md

#### Step-by-step

This lab has three blocks. Block 1 is the project goal, pasted into the Create a project dialog. Block 2 is the standing instructions, pasted into the Instructions panel. Block 3 is your first task in the project.

> **Note:** Projects live in Cowork mode in the desktop app. Create an empty folder called Lumo Launch on your computer first — the project works inside it.

1. Download the course labs and open the Lab 01 data/brand-kit folder. Create an empty folder called Lumo Launch on your computer.  
   *Why:* Skim the three brand-kit files — you will check Claude's answers against them. The empty folder becomes the project's working folder.
2. In the Claude desktop app, switch to Cowork, open Projects and start a new project.  
   *Why:* In Cowork a project is backed by a real folder on your computer, so its files stay yours to open.
3. Under "What are you working on?" type Lumo Cold Kopi Launch, and paste Block 1 into "What are you trying to achieve?".  
   *Why:* The goal is the standing context every task inherits, so write it as an outcome with a date and a measure.

   **Block 1 — GOAL**

   Paste this into "What are you trying to achieve?" in the Create a project dialog:

   *PROMPT — copy into Claude*

   ```text
   Launch Lumo Cold Kopi in Singapore on 1 December 2026.
   Produce the market research, a launch deck, a campaign brief,
   two weeks of social media posts and a 15-second launch video,
   within a S$60,000 budget, so that 25-34 year-olds on Instagram
   and TikTok know the product exists by launch day.
   ```

   Name it **Lumo Cold Kopi Launch**, choose **Use a folder** and pick your Lumo Launch folder, then **Create project**.


4. Choose Use a folder, pick your Lumo Launch folder, and click Create project.  
   *Why:* The project page opens with four panels: Instructions, Context, Folder and Scheduled.
5. Open the Instructions panel and paste Block 2. Save.  
   *Why:* Instructions are standing rules for every task. Short, checkable rules work better than general wishes.

   **Block 2 — INSTRUCTIONS**

   Paste this into the project's Instructions panel:

   *PROMPT — copy into Claude*

   ```text
   You are the marketing team for Lumo Kopi Co.
   - Prices are in Singapore dollars: S$3.90 per can, S$42.00 per
     12-pack. Always two decimals.
   - Follow lumo-brand-guidelines.md for anything customer-facing.
   - Never describe the product as healthy. You may say 5 g sugar.
   - Never send an email or publish a post without my approval.
   - Save every output to the project folder.
   - Read lumo-project-memory.md before you start any task.
   - Flag any figure that two sources disagree on. Do not pick one.
   ```

   Save the instructions, then add the three brand-kit files in the **Context** panel.


6. Open the Context panel and add the three brand-kit files.  
   *Why:* Context is read, never edited — the right home for reference files you want kept exactly as they are.
7. Start a new task in the project and send Block 3.  
   *Why:* This is a setup check: if Claude cannot restate the goal or find the files, fix that now, before any real work.

   **Block 3 — FIRST TASK**

   Start a new task in the project and send:

   *PROMPT — copy into Claude*

   ```text
   Before we start work, check your setup:
   1. Restate the project goal in one line.
   2. List the context files you can read and what each is for.
   3. List the three instructions you think matter most.
   4. From the product sheet, give me the price per can, the sugar
      per can and the launch date.
   Then create lumo-project-memory.md in the project folder with
   the heading "Project memory" and record: our primary audience
   is 25-34 year-olds in Singapore, and our secondary market is
   Kuala Lumpur, launching 15 January 2027.
   ```

   Compare the answer with the brand kit, then open your Lumo Launch folder and read lumo-project-memory.md.


8. Check the answers: S$3.90 per can, 5 g sugar, launch 1 December 2026.  
   *Why:* Every figure must match the product sheet. A wrong figure here means a wrong context file.
9. Open the Lumo Launch folder on your computer and read lumo-project-memory.md.  
   *Why:* A classic project has no memory panel, so this file plays that role: every task reads it (Block 2 says so), and you can edit it.

#### Check

> **Check — you are done when:** The Lumo Cold Kopi Launch project exists in Cowork, using your Lumo Launch folder, with the Block 2 instructions saved and the three brand-kit files under Context. Claude restated the goal, listed all three context files, and quoted S$3.90 per can, 5 g sugar and a 1 December 2026 launch. lumo-project-memory.md in the folder records the 25-34 audience and the 15 January 2027 Kuala Lumpur launch.


### Market research in parallel tasks

In Lab 2 you start four research tasks in the project at once, one per independent subject, then a fifth task merges them:

| Task | What it researches |
|---|---|
| Task 1 — Competitors | Six cold-brew brands: price, pack, positioning, and the gap Lumo can own. |
| Task 2 — Customers | 400 survey respondents: who is likely to buy, why, and where they discover drinks. |
| Task 3 — Pricing | Where S$3.90 sits against the market, and what the survey says people will pay. |
| Task 4 — Social trends | Which content themes earn the most engagement in the category right now. |

Start four tasks in the project at once, one subject each, each saving its own file to the folder. A fifth task merges them into the research brief.


### Lab 2 — Run Market Research in Parallel Tasks

**Objective:** By the end of this lab you can split a multi-subject research job into parallel tasks and verify the merged brief.

**Scenario:** Before anyone writes a post, the team needs to know the market. Four subjects need research — competitors, the customer survey, pricing and social trends — and none depends on another. So you start four tasks in the project at once, one per subject, each saving its findings to the folder. A fifth task merges the four files into one research brief, which you check against the data.

**You will build:** Four research files and lumo-research-brief.docx merged from them, in the project folder.

**Tools:** Claude Projects in Cowork, parallel tasks, web search.

#### Lab files

- Prompt PDF: labs/lab-02-market-research/lab-02-market-research.pdf
- labs/lab-02-market-research/data/lumo-consumer-survey-2026.csv
- labs/lab-02-market-research/data/lumo-competitors.csv
- labs/lab-02-market-research/data/lumo-social-trends.csv

#### Step-by-step

This lab has five blocks. Blocks 1 to 4 each go into their own new task, started one after another without waiting for the previous one to finish. Block 5 goes into a fifth task once the four research files are in the folder.

> **Note:** Copy the three CSV files from the Lab 02 data folder into your Lumo Launch project folder first.

1. Open the Lab 02 data folder and glance at the three CSV files.  
   *Why:* Know your source: 400 survey rows, six competitors, twelve content themes.
2. Copy the three CSV files into your Lumo Launch project folder.  
   *Why:* Data Claude analyses belongs in the Folder; the brand kit stays in Context.
3. Start a new task in the project and send Block 1. Do not wait for it.  
   *Why:* Each task has one subject and one file — a focused brief with a fresh context window. That is why parallel research stays sharp.

   **Block 1 — COMPETITORS**

   Start a new task in the project and send:

   *PROMPT — copy into Claude*

   ```text
   Research COMPETITORS for the Lumo Cold Kopi launch using
   lumo-competitors.csv: price per can, pack, positioning and
   channel for each brand, and the gap Lumo can own.
   Save your findings as research-1-competitors.md in the project
   folder.
   ```

   Do not wait for it — start the next task straight away.


4. Start a second task and send Block 2.  
   *Why:* Several tasks can run in one project at the same time.

   **Block 2 — CUSTOMERS**

   Start a second task and send:

   *PROMPT — copy into Claude*

   ```text
   Research CUSTOMERS using lumo-consumer-survey-2026.csv: the share
   likely to buy (intent 4 or 5), split by age band and city; the
   top purchase drivers; the top discovery channels. Show your
   working for every percentage. Save your findings as
   research-2-customers.md in the project folder.
   ```

   Start the third task.


5. Start a third task and send Block 3.  
   *Why:* Pricing reads both files; it does not need the other tasks' results.

   **Block 3 — PRICING**

   Start a third task and send:

   *PROMPT — copy into Claude*

   ```text
   Research PRICING using lumo-competitors.csv and
   lumo-consumer-survey-2026.csv: where S$3.90 sits against the
   competitor median, and the share of respondents willing to pay
   S$3.50 or more. Show your working. Save your findings as
   research-3-pricing.md in the project folder.
   ```

   Start the fourth task.


6. Start a fourth task and send Block 4.  
   *Why:* You are now the lead agent: four workers, four subjects, one goal.

   **Block 4 — TRENDS**

   Start a fourth task and send:

   *PROMPT — copy into Claude*

   ```text
   Research SOCIAL TRENDS using lumo-social-trends.csv: the three
   content themes with the highest engagement, with one post idea
   each. Save your findings as research-4-trends.md in the project
   folder.
   ```

   Four tasks are now running at once. Watch them finish in the project's task list.


7. When the four research files are in the folder, start a fifth task and send Block 5.  
   *Why:* The merge task reads the files, not the other conversations — so the folder is how the tasks share their work.

   **Block 5 — MERGE**

   When all four files are in the folder, start a fifth task and send:

   *PROMPT — copy into Claude*

   ```text
   Merge research-1-competitors.md, research-2-customers.md,
   research-3-pricing.md and research-4-trends.md from the project
   folder into one research brief, lumo-research-brief.docx:
   a one-paragraph summary, one section per subject with the key
   numbers, and three recommendations for the launch. Name the
   source file under each section, and flag anything the four
   files disagree on.
   ```

   Open the brief and check it against the data in the next steps.


8. When the merged brief arrives, check the survey numbers.  
   *Why:* Expect 400 respondents, 248 likely to buy (62%), and 112 of 152 in the 25-34 band (74%).
9. Check the channel, driver and pricing findings.  
   *Why:* Instagram 136 (34%), TikTok 104 (26%); Taste 124 (31%); competitor median S$4.30 with S$3.90 below it; 228 (57%) would pay S$3.50 or more.
10. Check the trends section and the recommendations.  
   *Why:* The top theme should be Taste tests and first-sip reactions. Do the three recommendations follow from the numbers above them?

#### Check

> **Check — you are done when:** The project folder holds the four research files and lumo-research-brief.docx, whose summary, four sections and three recommendations name their source files. The brief reports 400 respondents, 248 likely to buy (62%), 112 of 152 aged 25-34 (74%), Instagram as the top discovery channel at 34%, Taste as the top driver at 31%, a competitor median of S$4.30 with Lumo's S$3.90 below it, 228 respondents (57%) willing to pay S$3.50 or more, and Taste tests and first-sip reactions as the top content theme.


### Live Artefacts

A Live Artefact is an interactive tool Claude builds and keeps in your workspace. You make one in five moves:

1. **Describe** — Tell Claude the tool you want — a dashboard, tracker or planner — and what data it shows.
2. **Generate** — Claude writes the code and renders it in the preview pane beside the chat.
3. **Refine** — Ask for changes in plain English until the layout and figures are right.
4. **Save** — Save it so it persists as a reusable tool, not a lost chat message.
5. **Download** — Export a copy to file, attach or hand on to someone without Claude.

#### What an artefact can and cannot do

| An artefact CAN | An artefact CANNOT |
|---|---|
| Run interactive code — inputs, filters, charts. | Call an external API or website — the sandbox blocks it. |
| Use data you gave it, or that Claude looked up while building. | Load a script, font or image from another site. |
| Keep what you type into it between sessions. | Reach your local files or network. |
| Be saved, reopened and shared. | Refresh third-party data on its own. |
| Be downloaded as a file you own. |  |

So: bake the data in, or download the HTML and run it yourself.


### Lab 3 — Build the Market Insights Live Artefact

**Objective:** By the end of this lab you can turn research data into an interactive Live Artefact dashboard and save it.

**Scenario:** The research brief is a document; the launch team wants something they can explore. You turn the survey and competitor data into a Live Artefact — KPI tiles, a channel chart, a price ladder and a city filter — refine it in plain English, save it and download a copy. The launch deck in Lab 5 quotes this dashboard's numbers.

**You will build:** A saved Market Insights Live Artefact, plus a downloaded HTML copy.

**Tools:** Claude Projects, Live Artefacts.

#### Lab files

- Prompt PDF: labs/lab-03-market-insights-artefact/lab-03-market-insights-artefact.pdf
- labs/lab-03-market-insights-artefact/data/lumo-consumer-survey-2026.csv
- labs/lab-03-market-insights-artefact/data/lumo-competitors.csv

#### Step-by-step

1. In the project, send the lab prompt with the two CSV files attached or in Context.  
   *Why:* The project already knows the brand colours from the guidelines in Context — you do not attach them again.

   *PROMPT — copy into Claude*

   ```text
   Using lumo-consumer-survey-2026.csv and lumo-competitors.csv, build
   a Live Artefact: an interactive Market Insights dashboard for the
   Lumo Cold Kopi launch.

   Include:
   - KPI tiles: respondents, % likely to buy (intent 4 or 5), top
     discovery channel, competitor median price.
   - A bar chart of discovery channels.
   - A bar chart of purchase drivers.
   - A price ladder: the six competitors and Lumo at S$3.90, cheapest
     to dearest, with Lumo highlighted.
   - A filter for city: All, Singapore, Kuala Lumpur. The KPI tiles and
     both survey charts must follow the filter.

   Bake the data into the artefact - do not fetch anything. Use the
   Lumo brand colours from the brand guidelines. Title it
   "Lumo Cold Kopi - Market Insights".
   ```

   > **Note:** Artefacts run in a sandbox and cannot call the internet, which is why the prompt says to bake the data in.


2. Check the KPI tiles with the filter on All.  
   *Why:* 400 respondents, 62% likely to buy, Instagram top channel, competitor median S$4.30 — the same numbers as the Lab 2 brief.
3. Switch the filter to Singapore, then Kuala Lumpur.  
   *Why:* The respondents tile should read 240, then 160. If a chart does not change, ask Claude to wire it to the filter.
4. Check the price ladder.  
   *Why:* Kopi Kaki Cold at S$3.20 is cheapest, Northpoint Cold Brew at S$5.60 is dearest, and Lumo sits third at S$3.90, between Daily Grind RTD at S$3.70 and Frostbean at S$4.20.
5. Ask for one refinement, for example: Put the price ladder beside the channel chart.  
   *Why:* Refining by conversation is the normal way to work — you never edit the code yourself.
6. Save the artefact, then download a copy as HTML.  
   *Why:* A saved artefact persists and can be reopened; the download is a file you can share with someone who does not use Claude.

#### Check

> **Check — you are done when:** The Market Insights artefact shows 400 respondents, 62% likely to buy, Instagram as the top channel and a S$4.30 competitor median. The city filter changes the respondent count to 240 (Singapore) and 160 (Kuala Lumpur) and both survey charts follow it. The price ladder runs from S$3.20 to S$5.60 with Lumo highlighted at S$3.90. The artefact is saved and an HTML copy is downloaded.


## Topic 02 — Connectors, Skills and Plugins

Google Drive and Gmail · the context window · Slides and Docs · Agent Skills · plugins and mods

#### Key concepts

| Concept | What it means |
|---|---|
| Connectors | Toggle Gmail, Drive and Calendar on from the + menu so Claude can reach data outside the chat. |
| Scope the folder | Point Claude at one Drive folder for the task — not your whole Drive. |
| Approval to send | Claude drafts, sends and replies in Gmail — sending asks for explicit approval by default. |
| Slides and Docs | Claude's own deck and document formats: shareable, editable, and downloadable as PowerPoint, Word or PDF. |
| Agent Skills | A folder of instructions Claude loads on demand, so a task runs the same way every time. |
| /skill-creator | Do the task once, verify the output, then let skill-creator write the SKILL.md for you. |
| Plugins | A bundle somebody else packaged — several skills plus the tools they need, installed in one click. |
| Mods | Changes to Claude's own interface or behaviour — a side panel, a status line, a slash command or a hook. |


### Connectors and the context window

A connector lets Claude reach a service outside the chat. These are the ones this course uses:

| Connector | What Claude can do |
|---|---|
| Google Drive | Search and read Sheets, Docs, Slides and PDFs; upload files; create folders; save Claude's output back to Drive. |
| Gmail | Search and read mail, draft messages, send / reply / forward with approval, and manage labels. |
| Google Calendar | View events, find availability, and create or update meetings. |
| Social and ads tools | Where your workspace has them, connectors for scheduling and ad platforms reach the same way — always with approval. |
| Approval by default | Claude asks for explicit approval before it sends, replies to or forwards an email. |
| Where to manage them | Individually from the + menu; account-wide under Customize → Connectors. |

#### Keeping the context window lean

The context window is all the information the model can “see” when producing a response. Five levers decide what goes into it:

| Lever | What it adds |
|---|---|
| Conversation | Your prompt. The messages you send, including both text and attachments. |
| Project context | The files the project reads, and the folder it works in. |
| Connectors | The connected tools Claude can pull data from, and take actions in. |
| Skills | A set of instructions Claude follows for a repeatable workflow. |
| Instructions & memory file | Project rules you wrote, and decisions kept in the memory file. |

Every lab today pulls one of these levers — context in Lab 1, connectors in Lab 4, skills in Labs 5–7, and the memory file in Lab 10.

A window that fills up costs you in four ways:

| Problem | What happens |
|---|---|
| Context rot | Performance degrades. Recall of specific facts gets worse, the model starts confusing similar entities, and reasoning quality drops. |
| Tool confusion | Claude sees every tool definition. The more options competing for its attention, the more likely it picks the wrong one or fills in the wrong parameters. |
| Slower responses | The model processes every token on every turn. A bigger context means more work per message, which means longer waits before you see a reply. |
| Eats up your usage faster | Your entire context gets resent with each new message — so more tokens are burned per turn, and your limits are reached sooner. |

The fix is housekeeping: one job per task, only the connectors you need, and only the files the job actually reads.


### Lab 4 — Connect Google Drive and Gmail

**Objective:** By the end of this lab you can connect Google Drive and Gmail, read campaign files from Drive and send an approved summary.

**Scenario:** The launch budget and timeline live in a shared Google Drive folder, not on your laptop. You upload the Lab 04 data folder to Drive, connect the Google Drive and Gmail connectors, and have the project read the budget from Drive, reconcile it against the launch brief, save the research brief back to Drive, and email you an approved summary. The budget sheet and the brief disagree on two lines — the project should catch it.

**You will build:** Drive and Gmail connected, the research brief saved to Drive, and an approved launch summary emailed to yourself.

**Tools:** Claude Projects, Google Drive connector, Gmail connector.

#### Lab files

- Prompt PDF: labs/lab-04-connect-drive-and-gmail/lab-04-connect-drive-and-gmail.pdf
- labs/lab-04-connect-drive-and-gmail/data/Lumo Launch/lumo-launch-budget.csv
- labs/lab-04-connect-drive-and-gmail/data/Lumo Launch/lumo-launch-timeline.csv

#### Tips

**Turning connectors on**

Click the **+** in the chat composer, hover **Connectors**, and toggle on only Google Drive and Gmail. You can manage them later under **Customize → Connectors**.

**If Claude says "insufficient scope"**

The connector is linked but was authorised without permission to read files. Fix it in **Settings → Connectors → Google Drive → Reconnect**, and accept the read access Google asks for. Then tell Claude to try again.

#### Step-by-step

1. Upload the Lab 04 data/Lumo Launch folder to your Google Drive.  
   *Why:* In real work the files are already there; the upload stands in for the shared team drive.
2. In the project, click + → Connectors and switch on Google Drive and Gmail, signing in to Google.  
   *Why:* Accept the read access Google asks for. A connector that shows Connected without read access fails with "insufficient scope".
3. Send the lab prompt with your own email address in place of `<YOUR EMAIL>`.  
   *Why:* No files are attached this time — the project reaches Drive itself.

   *PROMPT — copy into Claude*

   ```text
   Using Google Drive, open the "Lumo Launch" folder.

   1. Read lumo-launch-budget.csv and lumo-launch-timeline.csv.
   2. Compare the budget sheet, line by line, with the budget in
      lumo-launch-brief.md from our project context. Show both in one
      table and flag every line where they disagree. Do not decide
      which is right.
   3. Upload lumo-research-brief.docx from Lab 2 into the same Drive
      folder.
   4. Draft an email to <YOUR EMAIL> with the subject
      "Lumo launch - research and budget check": three bullet points
      from the research brief, the budget table with the disagreements
      flagged, the next milestone from the timeline, and a link to the
      brief in Drive.

   Show me the draft. Do not send it until I approve.
   ```

   > **Note:** Replace `<YOUR EMAIL>` with your own address. Send lab emails only to yourself.


4. Read the budget table Claude produces.  
   *Why:* Both total S$60,000, but Instagram is S$18,000 in the Drive sheet and S$20,000 in the brief, and Influencers is S$12,000 against S$10,000.
5. Confirm Claude flagged both lines instead of choosing one.  
   *Why:* That is your Lab 1 instruction at work. Two sources disagreeing is a decision for a human, not a guess for Claude.
6. Check that lumo-research-brief.docx now sits in the Lumo Launch folder in Drive.  
   *Why:* Saving outputs back to the team's folder is what makes the work findable by colleagues.
7. Read the draft email in full, then approve it.  
   *Why:* Gmail sends only after your explicit approval. Check the figures against the table before you click.
8. Open your inbox and confirm the email arrived with the Drive link working.  
   *Why:* Close the loop: an email you did not check arrived is an email you hope arrived.

#### Check

> **Check — you are done when:** Google Drive and Gmail are connected. Claude read both CSV files from the Lumo Launch folder, showed a budget table totalling S$60,000 on both sides, and flagged Instagram (S$18,000 vs S$20,000) and Influencers (S$12,000 vs S$10,000) without choosing between them. lumo-research-brief.docx is in the Drive folder, and the approved summary email arrived in your own inbox with a working link.


### Slides, Docs and built-in skills

| Format | What it is |
|---|---|
| Slides | A deck Claude builds and you edit in place — download as PowerPoint or PDF for the meeting. |
| Docs | A living document — a campaign brief, a plan — that you and Claude edit and comment on together. |
| Dashboards | A page of live numbers — the Live Artefact you build in Lab 3 is one. |
| Built-in skills | Claude's pptx, docx and xlsx skills load on their own when your request needs a file. |

You never name the skill. Ask for a deck or a document; Claude picks the format and the skill that builds it.


### Lab 5 — Create the Launch Deck and Campaign Brief

**Objective:** By the end of this lab you can produce a launch deck in Slides and a campaign brief in Docs from the project's research.

**Scenario:** The launch team meets on Friday and needs two things: a short deck for the room and a campaign brief everyone can work from. You ask the project for both. Claude builds the deck in Slides and the brief in Docs, choosing its built-in skills on its own, using the numbers from your research and dashboard. You check every figure, then download the deck as PowerPoint.

**You will build:** An eight-slide launch deck in Slides (downloaded as .pptx) and a campaign brief in Docs.

**Tools:** Claude Projects, Slides, Docs, built-in skills.

#### Lab files

- Prompt PDF: labs/lab-05-launch-deck-and-brief/lab-05-launch-deck-and-brief.pdf

This lab has no data folder — it works from what the project already holds.

#### Step-by-step

1. In the project, send the lab prompt.  
   *Why:* No attachments: the research brief, the dashboard data and the brand kit are all already in the project.

   *PROMPT — copy into Claude*

   ```text
   Using our research brief, the Market Insights dashboard and the
   brand kit, create two things for Friday's launch meeting.

   1. A launch deck in Slides, eight slides:
      1 Title - Lumo Cold Kopi: Kopi, Chilled Right
      2 The opportunity - the three survey numbers that matter most
      3 Who we are for - 25-34s in Singapore, with the evidence
      4 Competitors - a price ladder chart with Lumo highlighted
      5 Where they find us - a discovery channel chart
      6 The campaign - message, channels and dates
      7 Budget - the S$60,000 split, noting the two open questions
      8 Next steps and owners

      Use the Lumo brand colours. Real charts, not pictures of charts.

   2. A campaign brief in Docs: objective, audience, key message,
      proof points, channels, budget, timeline, KPIs, and a "claims
      we must not make" section.

   Every number must come from the research brief or the dashboard.
   List the source of each number at the end of the brief.
   ```

   > **Note:** You do not name a skill. Ask for a deck and a document; Claude picks the format and the built-in skill.


2. Open the deck when it appears and page through all eight slides.  
   *Why:* Check the charts are real charts — click one; a real chart has editable data behind it.
3. Check slide 2 and slide 4 against your research.  
   *Why:* 62% likely to buy, 74% among 25-34s, Instagram 34%; a price ladder from S$3.20 to S$5.60 with Lumo at S$3.90.
4. Check slide 7.  
   *Why:* The S$60,000 split should carry the two open questions from Lab 4 — Instagram and Influencers — not quietly pick one figure.
5. Open the campaign brief in Docs and read the "claims we must not make" section.  
   *Why:* It should rule out "healthy" and any claim the product sheet does not support. This section protects every post you write later.
6. Ask for one change to each, for example: Shorten slide 6 to three bullets.  
   *Why:* Slides and Docs are edited in place by conversation, the same way as an artefact.
7. Download the deck as PowerPoint and open it.  
   *Why:* The download is the file you take into the meeting — check the charts survived.

#### Check

> **Check — you are done when:** The deck has eight slides in the Lumo colours, with real charts for the price ladder and the discovery channels, the survey figures 62%, 74% and 34%, and a budget slide that shows S$60,000 with the Instagram and Influencers lines marked as open questions. The campaign brief in Docs has all nine sections, including "claims we must not make", and lists a source for every number. The deck opens in PowerPoint with its charts intact.


### Agent Skills

An Agent Skill is a folder of instructions Claude loads on demand, so a routine runs the same way every time. A skill has three layers, and only the first is always in context:

| Layer | What it holds | When Claude loads it |
|---|---|---|
| Metadata | Skill name and description. | Always in context — this is all Claude sees until the skill is triggered. |
| Instructions | The step-by-step workflow, written in a SKILL.md. | Loaded when the skill is triggered. |
| Resources | Supporting documents, templates and examples. | Loaded only when the skill needs them. |

#### Do, Verify, Save, Update

You never write a skill from a blank page. You do the task once, then save the verified routine:

1. **Do** — Do the task together with Claude once, step by step.
2. **Verify** — Review and refine until the output is right.
3. **Save** — Turn it into a skill using the /skill-creator skill.
4. **Update** — Refine it later and save over it — Claude confirms before replacing.


### Lab 6 — Capture the Brand Voice as an Agent Skill

**Objective:** By the end of this lab you can rewrite content in the brand voice, verify it, and save the routine as a skill with /skill-creator.

**Scenario:** Four channels and two weeks of posts are coming, and they all have to sound like Lumo. You rewrite five off-brand captions with Claude until they are right, then use /skill-creator to turn that verified routine into a lumo-brand-voice skill. From then on, every task in the project — and every colleague — loads the same voice by name.

**You will build:** A lumo-brand-voice Agent Skill, tested on a new caption.

**Tools:** Claude Projects, Agent Skills, /skill-creator.

#### Lab files

- Prompt PDF: labs/lab-06-brand-voice-skill/lab-06-brand-voice-skill.pdf
- labs/lab-06-brand-voice-skill/data/lumo-sample-captions.txt

#### Step-by-step

This lab has three blocks, sent at different times. Block 1 does the work once so you can verify it. Block 2 saves it as a skill: type /skill-creator in the composer, then paste the block. Block 3 tests the saved skill.

> **Note:** Block 2 begins with you typing /skill-creator in the composer — it is not part of the pasted text.

1. Open lumo-sample-captions.txt and read the five captions.  
   *Why:* Each breaks at least one brand rule — a wrong price format, a health claim, too much slang, too many hashtags.
2. In the project, attach the file and send Block 1.  
   *Why:* This is the Do step of Do · Verify · Save. You never write a skill from a blank page.

   **Block 1 — DO**

   Attach lumo-sample-captions.txt and send this first, on its own:

   *PROMPT — copy into Claude*

   ```text
   Rewrite the five captions in the attached file in the Lumo
   brand voice, following lumo-brand-guidelines.md.

   For each caption, show:
   - the original
   - your rewrite
   - every rule you applied, by name
   - any claim you removed, and why

   Then run these checks on each rewrite and show the result:
   price written as S$3.90; no "healthy" or medical claims; at
   most one Singlish word; #LumoKopi present; no more than five
   hashtags; ends with one clear call to action.
   ```

   **Now stop and read the output.** Ask for changes until every rewrite sounds right. Whatever you settle on here is exactly what the skill will reproduce.


3. Check each rewrite against the brand guidelines and refine until all five are right.  
   *Why:* This is the Verify step. Ask for changes in plain English; you are teaching the routine by correcting it.
4. Type /skill-creator in the composer, then paste Block 2 and send.  
   *Why:* skill-creator writes the SKILL.md from the run you just verified — name, description, instructions and examples.

   **Block 2 — SAVE**

   Type /skill-creator in the composer, then paste this:

   *PROMPT — copy into Claude*

   ```text
   Create a skill called lumo-brand-voice from what we just did.

   Description: Use when writing or reviewing any customer-facing
   Lumo Kopi content - social posts, captions, emails, video
   scripts or ads.

   It should rewrite or draft content in the Lumo voice, apply the
   brand rules, remove claims we cannot prove, and finish with the
   same checklist of checks we used. Include two of today's
   before-and-after examples as a resource.
   ```

   Approve the skill when Claude shows it to you, then open **Customize → Skills** and find it.


5. Read the skill Claude proposes, especially its description, and approve it.  
   *Why:* The description is the one part always in context. It decides when the skill loads, so it must say WHEN to use it.
6. Open Customize → Skills and find lumo-brand-voice.  
   *Why:* Your own skills are listed here. Built-in skills such as pptx are not — they show in the context panel when they load.
7. Start a new task and send Block 3.  
   *Why:* A fresh task proves the skill works without the earlier conversation — which is exactly how later tasks will use it.

   **Block 3 — TEST**

   Start a new task in the project and send:

   *PROMPT — copy into Claude*

   ```text
   Use lumo-brand-voice to write an Instagram caption announcing
   that Lumo Cold Kopi 12-packs are available on Shopee from
   1 December. It's super healthy and the best kopi in Singapore!
   ```

   The skill should load by itself, remove both unprovable claims and run its checklist.


8. Check the caption: no "healthy", no "best kopi in Singapore", S$ prices, #LumoKopi present.  
   *Why:* Both claims were traps. A skill that removes them has learned the rule, not just the examples.

#### Check

> **Check — you are done when:** lumo-brand-voice appears under Customize → Skills with a description that says when to use it. In a fresh task, Block 3 loaded the skill without being asked to find it, and the caption it returned drops "healthy" and "best kopi in Singapore", includes #LumoKopi, uses at most five hashtags and ends with one call to action, followed by the checklist results.


### Skills, plugins and mods

A skill is one routine. A plugin is the whole setup — install the Marketing plugin and you get every skill, command and tool it contains.

|  | Skill | Plugin | Mod |
|---|---|---|---|
| Changes | How a task is done | A whole toolkit | Claude's own interface |
| Contains | One SKILL.md + resources | Skills, tools, agents, hooks | A panel, command, hook or status line |
| You get it by | Writing it with /skill-creator | Installing from Discover | Asking Claude to make one |
| Lumo example | lumo-brand-voice | Marketing plugin | A launch-countdown panel |

#### Mods

- **What a mod is** — A change to Claude's own interface or behaviour, rather than to the work it does.
- **A panel or pane** — Something that stays beside the chat and updates — a running checklist, a campaign tracker.
- **A status line or toast** — A small always-visible signal, such as the active project or remaining usage.
- **A slash command** — Your own /command that starts a routine you use often.
- **A hook** — An action that runs automatically on an event — for example, before Claude sends anything.
- **Where to find them** — Under Customize, alongside Skills, Connectors and Plugins. Ask Claude to make one for you.


### Lab 7 — Add the Marketing Plugin

**Objective:** By the end of this lab you can install a plugin and use its namespaced commands alongside your own skill.

**Scenario:** You wrote one skill yourself; now you install a toolkit somebody else packaged. Anthropic's Marketing plugin bundles several marketing skills behind namespaced commands. You install it, use /marketing:campaign-plan to stress-test the launch plan, and run /marketing:brand-review on the deck copy — then compare a plugin with the skill you wrote, and see where mods fit.

**You will build:** The Marketing plugin installed, a campaign plan review and a brand review of the launch copy.

**Tools:** Claude Projects, plugins, Customize.

#### Lab files

- Prompt PDF: labs/lab-07-marketing-plugin/lab-07-marketing-plugin.pdf

This lab has no data folder — it works from what the project already holds.

#### Step-by-step

This lab has two blocks, each a command from the Marketing plugin. Install the plugin first, then send Block 1 and, after reading its answer, Block 2.

> **Note:** Install the plugin first: Customize → Plugins → Browse, find Marketing, click Install. Then type /marketing in the composer to see its commands.

1. Open Customize → Plugins and browse the available plugins.  
   *Why:* Discover before you build: check whether someone has already packaged what you need.
2. Find the Marketing plugin, read what it contains, and click Install.  
   *Why:* One install brings several skills and commands at once — the difference between a plugin and a skill.
3. In the project composer, type /marketing and look at the commands it offers.  
   *Why:* Plugin commands carry the plugin's name as a prefix. That is how you tell them from a skill you wrote yourself.
4. Send Block 1 to stress-test the plan with /marketing:campaign-plan.  
   *Why:* The plugin's skill works with your project context: the campaign brief and research brief are already there.

   **Block 1 — PLAN**

   Send this in the project:

   *PROMPT — copy into Claude*

   ```text
   /marketing:campaign-plan Review the Lumo Cold Kopi launch using
   our campaign brief and research brief. Keep our objective,
   audience, budget and dates. Tell me:
   - what is missing from the plan,
   - the three biggest risks to the 1 December launch,
   - the KPIs you would track in the first two weeks, with targets.
   Do not change the S$60,000 budget.
   ```

   Read its answer in full before you send Block 2.


5. Read the risks and KPIs it proposes, and check the budget is unchanged at S$60,000.  
   *Why:* A plugin is someone else's judgement. Keep what fits your goal; question what does not.
6. Send Block 2 to review the deck copy with /marketing:brand-review.  
   *Why:* Two tools on one job: the plugin reviews, and your lumo-brand-voice skill holds the house rules it checks against.

   **Block 2 — REVIEW**

   Then send:

   *PROMPT — copy into Claude*

   ```text
   /marketing:brand-review Review the copy on slides 1, 2 and 6 of
   our launch deck against lumo-brand-guidelines.md. List each
   change you would make and the rule behind it.
   ```

   Compare its findings with what your lumo-brand-voice skill would flag.


7. Open Customize and look at the Mods section.  
   *Why:* Mods change Claude's interface itself — a panel, a status line, a slash command or a hook. You will not build one today; know where they live.

#### Check

> **Check — you are done when:** The Marketing plugin is installed and its /marketing: commands appear in the composer. /marketing:campaign-plan returned the gaps, three launch risks and two-week KPIs with targets while keeping the S$60,000 budget and the 1 December date. /marketing:brand-review reviewed the deck copy. You can explain the difference between lumo-brand-voice (a skill you wrote), the Marketing plugin (a packaged bundle) and a mod (a change to Claude's interface).


## Topic 03 — Content Production and Scheduled Work

Social posts for four platforms · a launch video · scheduled tasks · the memory file

#### Key concepts

| Concept | What it means |
|---|---|
| Specs per platform | Instagram, TikTok, LinkedIn and Facebook each get their own spec in the prompt, so one task drafts all four well. |
| Skill in every task | Every task loads the same brand-voice skill, so four channels still sound like one brand. |
| Video as code | Claude writes and runs the code that turns a storyboard and your images into an MP4. |
| Scheduled tasks | A prompt that runs on a timetable — daily, weekly or monthly — inside the project, while you are away. |
| Approval stays human | A scheduled task drafts and emails the post to you. Publishing is still your click. |
| A memory file | A Markdown file in the project folder that records decisions, so every later task reads the same facts. |


### Social content for four platforms

Each platform has its own format, so the Lab 8 prompt gives every platform its own spec:

| Platform | Format and rules |
|---|---|
| Instagram | Carousel or Reel. Hook in the first line; caption up to 2,200 characters; 3–5 hashtags. |
| TikTok | 9:16 video, 15–30 s. A hook in the first 2 seconds; on-screen text; one call to action. |
| LinkedIn | Founder or team voice; the story behind the product; no more than 3 hashtags. |
| Facebook | Community and offers; a clear link to buy; questions that invite comments. |

Every post loads lumo-brand-voice, so four formats still sound like one brand.

#### From brief to calendar

1. **Brief once** — One prompt: the dates, the four platforms, the spec for each and the skill to use.
2. **Draft by platform** — Claude works through each platform's posts to its own spec.
3. **Check the voice** — The brand-voice skill runs its checklist on every post.
4. **Save the calendar** — The posts land in one dated calendar file in the project folder.
5. **Check and approve** — You check claims, prices and dates before anything is scheduled.


### Lab 8 — Create Two Weeks of Social Media Posts

**Objective:** By the end of this lab you can produce a two-week, four-platform social calendar using the brand-voice skill.

**Scenario:** Launch fortnight needs ten posts across Instagram, TikTok, LinkedIn and Facebook. Each platform has its own format, so the prompt gives Claude a spec for each. It loads lumo-brand-voice, drafts every platform's posts to its spec, and saves one dated calendar that you check before anything is scheduled.

**You will build:** social-calendar.csv with ten dated posts across four platforms, plus lumo-social-posts.docx with the full copy.

**Tools:** Claude Projects in Cowork, Agent Skills.

#### Lab files

- Prompt PDF: labs/lab-08-social-posts/lab-08-social-posts.pdf
- labs/lab-08-social-posts/data/social-calendar-template.csv

#### Step-by-step

1. In the project, attach social-calendar-template.csv and send the lab prompt.  
   *Why:* One task with four precise specs. In the Threads edition each platform gets its own thread; here the specs keep one task on track.

   *PROMPT — copy into Claude*

   ```text
   Create the launch social calendar for Lumo Cold Kopi: ten posts,
   one each weekday from Tuesday 1 December to Monday 14 December
   2026, using social-calendar-template.csv for the columns.

   Draft each platform's posts to its own spec:
   - Instagram: 3 posts (carousel or Reel), caption with a hook in
     the first line, 3-5 hashtags.
   - TikTok: 3 posts, each a 15-second video script with a hook in
     the first 2 seconds and on-screen text.
   - LinkedIn: 2 posts in the founder's voice, the story behind the
     product, no more than 3 hashtags.
   - Facebook: 2 posts for community and the 12-pack offer.

   Use the lumo-brand-voice skill for every post, and our top
   content theme from the research. The 1 December launch-day
   post is an Instagram Reel; TikTok follows on 2 December.

   Then save them into social-calendar.csv (date, platform,
   format, hook, copy, hashtags, visual idea, call to action) and
   lumo-social-posts.docx with the full copy. Report the brand-voice
   checklist result for every post, and list any post that failed.
   ```

   > **Note:** Attach social-calendar-template.csv from the Lab 08 data folder.


2. Watch Claude work through the four platforms.  
   *Why:* Each platform is drafted against its own spec, so the TikTok scripts and the LinkedIn story stay distinct.
3. Check in the task's activity that Claude loaded lumo-brand-voice.  
   *Why:* The skill you wrote in Lab 6 is now doing its real job: keeping four formats in one voice.
4. When the calendar arrives, count the rows and check the dates.  
   *Why:* Ten rows, weekdays only: 1, 2, 3, 4, 7, 8, 9, 10, 11 and 14 December. Instagram 3, TikTok 3, LinkedIn 2, Facebook 2.
5. Read the brand-voice checklist results.  
   *Why:* Every post should pass. If one fails, ask Claude to redraft it.
6. Spot-check three posts against the campaign brief's "claims we must not make".  
   *Why:* Parallel production is fast; a human check on the claims is what makes it safe to publish.
7. Open lumo-social-posts.docx and confirm the copy matches the calendar.  
   *Why:* The calendar is what Lab 10's scheduled task reads every morning.

#### Check

> **Check — you are done when:** social-calendar.csv has ten rows dated on the ten weekdays from 1 to 14 December 2026 — Instagram 3, TikTok 3, LinkedIn 2, Facebook 2 — with the 1 December launch post an Instagram Reel and TikTok on 2 December. Every post passed the lumo-brand-voice checklist, none uses "healthy", every price is written S$3.90 or S$42.00, and lumo-social-posts.docx carries the same copy.


### The video pipeline

Claude does not edit video by hand — it writes and runs the code that renders it. The work runs in five stages:

1. **Script** — Five lines, three seconds each — hook, problem, product, proof, call to action.
2. **Storyboard** — One frame per line: which image, which on-screen text, which motion.
3. **Render** — Claude writes and runs code that animates your images and text into an MP4.
4. **Check** — Length, size 1080 × 1920, brand colours, every claim true, end card with the price.
5. **Refine** — Ask for timing or text changes in plain English and render again.

#### Video specifications

| Spec | Requirement |
|---|---|
| Format | Vertical 9:16, 1080 × 1920 pixels, MP4 — fits Reels, TikTok and Shorts. |
| Length | 15 seconds: five scenes of three seconds each. |
| Text | Large, high-contrast captions — most people watch with the sound off. |
| Brand | Lumo colours and logo; the end card shows the price and the campaign hashtag. |
| Assets | Only the supplied product images — never a real person's likeness or a stock logo. |
| Fallback | No video tools in the session? Claude builds an animated HTML version to screen-record. |


### Lab 9 — Produce a 15-Second Launch Video

**Objective:** By the end of this lab you can script, storyboard and render a vertical launch video from supplied brand assets.

**Scenario:** The TikTok and Instagram posts need a launch video. You give the project the supplied product images and logo; Claude first writes a five-scene script and storyboard with lumo-brand-voice, then writes and runs the code that animates the images and captions into a 15-second, 1080 × 1920 MP4. You check it frame by frame and ask for changes in plain English.

**You will build:** lumo-launch-15s.mp4 (1080 × 1920, 15 seconds), with its script and storyboard.

**Tools:** Claude Projects in Cowork, code execution.

#### Lab files

- Prompt PDF: labs/lab-09-launch-video/lab-09-launch-video.pdf
- labs/lab-09-launch-video/data/video-assets/lumo-can.png
- labs/lab-09-launch-video/data/video-assets/lumo-12pack.png
- labs/lab-09-launch-video/data/video-assets/lumo-logo.png
- labs/lab-09-launch-video/data/video-assets/scene-hawker.png
- labs/lab-09-launch-video/data/video-assets/scene-office.png

#### Step-by-step

1. Open the Lab 09 data/video-assets folder and look at the five images.  
   *Why:* These are the only images the video may use. Supplying assets is how you keep likenesses and logos safe.
2. In the project, attach the folder and send the lab prompt.  
   *Why:* Two stages in one task: the render waits for the script, so you can read the storyboard first.

   *PROMPT — copy into Claude*

   ```text
   Make a 15-second vertical launch video for Lumo Cold Kopi, using
   only the five images in the attached video-assets folder.

   Work in two stages:
   Stage 1 - SCRIPT: with lumo-brand-voice, write five scenes of
     three seconds each: hook, problem, product, proof, call to action.
     For each scene give the image, the on-screen text (max 6 words)
     and the motion. Save it as lumo-video-storyboard.md.
   Stage 2 - RENDER: when the storyboard is ready, write and run
     code that renders it to lumo-launch-15s.mp4: 1080 x 1920, 30 fps,
     exactly 15 seconds, large high-contrast captions in the Lumo
     colours, a gentle zoom on each image, and an end card with the
     logo, "From S$3.90" and #KopiChilledRight.

   If you cannot render video in this session, build the same thing
   as an animated HTML page at 1080 x 1920 and tell me, so I can
   screen-record it. Report the file's duration and size when done.
   ```

   > **Note:** Attach the whole video-assets folder. Use only the supplied images — never a real person's likeness or another brand's logo.


3. Read the storyboard when Stage 1 finishes.  
   *Why:* Five scenes, three seconds each, captions of six words or fewer, and no health claims — the brand-voice skill applies to scripts too.
4. When the video arrives, check the reported duration and size.  
   *Why:* Exactly 15 seconds and 1080 × 1920. A wrong size is the most common reason a platform crops your captions.
5. Play it through, then scrub it frame by frame.  
   *Why:* Check every caption is readable with the sound off and the end card shows the logo, From S$3.90 and #KopiChilledRight.
6. Ask for one change, for example: Hold the end card for one second longer and shorten scene 2.  
   *Why:* The video is code, so a change is a re-render, not a re-edit. Check the length is still 15 seconds afterwards.
7. If Claude built the HTML fallback instead, open it full screen and screen-record 15 seconds.  
   *Why:* Same storyboard, different renderer. The checks stay the same.

#### Check

> **Check — you are done when:** lumo-launch-15s.mp4 is 1080 × 1920, 30 fps and 15 seconds long, uses only the supplied images, shows five scenes with captions of six words or fewer in the Lumo colours, and ends on a card with the logo, "From S$3.90" and #KopiChilledRight. lumo-video-storyboard.md sits beside it and matches what plays. No scene makes a health claim.


### Scheduled tasks

A scheduled task has six parts. Write each one down before you schedule anything:

| Part | What to decide |
|---|---|
| Name | What the task is called in the Scheduled list — for example, Today's Lumo post. |
| Instructions | Exactly what to do each run — written like a lab prompt, with the checks included. |
| Project | Pick the Lumo Cold Kopi Launch project, so the task reads its instructions, context and folder. |
| Frequency | Daily, weekdays, weekly or monthly. The default is Manual — change it. |
| Permissions | Defaults to Automatically approve: the task acts unattended, so it must only draft. |
| Require this computer | On: runs only while your computer is awake, with your folders. Off: runs without them. |

#### Examples for the launch

| Schedule | Task |
|---|---|
| Daily post, weekdays 9:00am | Take today's row from the social calendar, polish it with lumo-brand-voice and email it to me for approval. |
| Weekly report, Mondays 8:00am | Summarise last week's posts from the social calendar and anything new in the Lumo Launch Drive folder in five bullet points. |
| Monthly scan, 1st at 10:00am | Check the six competitors for new products or price changes and update the research brief. |

Open Scheduled tasks from the sidebar (or the project's Scheduled panel), choose New task and Set up manually. A task with Permissions on Automatically approve must only draft.

#### Responsible marketing with Claude

Speed is only useful if what goes out is true and fair. Keep these rules on every job:

| Rule | In practice |
|---|---|
| Claims you can prove | “5 g sugar” is on the label. “Healthy” is a claim Lumo cannot substantiate — never use it. |
| Consent for email | Email only people who opted in. Lab emails go to yourself, never to real customers. |
| No real likenesses | Do not generate a real person, influencer or competitor logo into an ad. |
| Disclose partnerships | Influencer posts are labelled as paid partnerships. |
| A human publishes | Claude drafts and schedules drafts; a person approves every public post. |
| Keep the source | Keep the research files, so every number in a post can be traced back. |


### Lab 10 — Schedule the Posts and Review the Project

**Objective:** By the end of this lab you can schedule recurring project tasks, keep the project memory file current and review the project.

**Scenario:** The launch needs a post drafted every weekday morning and a report every Monday, and nobody should have to remember either. You create both as scheduled tasks on the project, then do the housekeeping a real project needs: record a changed plan in the memory file, and review what the project now holds.

**You will build:** Two scheduled tasks on the project, an updated memory file and a project review.

**Tools:** Claude Projects in Cowork, scheduled tasks, Gmail connector.

#### Lab files

- Prompt PDF: labs/lab-10-schedule-and-review/lab-10-schedule-and-review.pdf

This lab has no data folder — it works from what the project already holds.

#### Step-by-step

This lab has four blocks. Blocks 1 and 2 are pasted into the Instructions field of the Create scheduled task dialog, not typed into the chat. Block 3 updates the project's memory file. Block 4 asks the project to review itself.

> **Note:** Replace `<YOUR EMAIL>` in Blocks 1 and 2. Copy social-calendar.csv from Lab 8 into the project folder if Claude saved it elsewhere.

1. Open Scheduled tasks from the sidebar (or the project's Scheduled panel), choose New task, then Set up manually.  
   *Why:* Create with Claude asks you questions instead; setting it up manually shows you every field.
2. Name it Today's Lumo post and paste Block 1 into Instructions, with your own email.  
   *Why:* The task runs in the project, so it inherits the instructions, context, folder and the brand-voice skill — the prompt stays short.

   **Block 1 — DAILY POST TASK**

   Paste into the Instructions field of a new scheduled task named "Today's Lumo post":

   *PROMPT — copy into Claude*

   ```text
   Take today's row from social-calendar.csv in the project folder,
   polish the post with lumo-brand-voice, and check every price and
   claim against the brand kit. Email it to <YOUR EMAIL> as a draft
   with the subject "Today's Lumo post - <date>".

   Never publish anything and never post to social media. If there
   is no row for today, email "No Lumo post scheduled today".
   ```

   Pick the **Lumo Cold Kopi Launch** project, set **Frequency** to weekdays at 9:00am, and save. Permissions defaults to *Automatically approve* — which is why the task only drafts.


3. Pick the Lumo Cold Kopi Launch project, set Frequency to weekdays at 9:00am, check Permissions, and save.  
   *Why:* Frequency defaults to Manual — a task left on Manual never runs. Permissions defaults to Automatically approve, so the task must only draft.
4. Create a second task, Weekly launch report, with Block 2, Mondays at 8:00am.  
   *Why:* Two tasks, two timetables, one project. This is where you would add a monthly competitor scan next.

   **Block 2 — WEEKLY REPORT TASK**

   Paste into a second scheduled task named "Weekly launch report":

   *PROMPT — copy into Claude*

   ```text
   Summarise last week's posts from social-calendar.csv and anything
   new in the Lumo Launch Drive folder in five bullet points, and
   email the summary to <YOUR EMAIL>. Draft only - do not send
   anything else.
   ```

   Pick the project, set **Frequency** to weekly, Mondays at 8:00am, and save.


5. Confirm both tasks appear under Scheduled, with the right days and times. Use Run now if it is offered.  
   *Why:* A task scheduled at the wrong time is a silent failure. A test run's email shows exactly what arrives each morning.
6. Start a new task in the project and send Block 3.  
   *Why:* Expect the calendar, Task 1, the deck's title slide and timeline, and the brief. The memory file is how one fact reaches every later task.

   **Block 3 — MEMORY**

   Start a new task in the project and send:

   *PROMPT — copy into Claude*

   ```text
   Add this to lumo-project-memory.md: the Singapore launch has
   moved from 1 December to 8 December 2026. Kuala Lumpur is
   unchanged. Then tell me everything in the project folder and
   scheduled tasks that depends on the launch date - posts, tasks,
   the deck, the brief - and propose the changes. Do not make them yet.
   ```

   Open **lumo-project-memory.md** in the folder and check the new line.


7. Open lumo-project-memory.md and check the new launch-date line. Edit it if the wording is wrong.  
   *Why:* Claude writes the file, but you own it. Delete anything you would not want every future task to believe.
8. Send Block 4 at the end of the lab.  
   *Why:* A project that can list its own files and what each is for is one a colleague can pick up tomorrow.

   **Block 4 — REVIEW**

   Send this at the end of the lab:

   *PROMPT — copy into Claude*

   ```text
   Review this project for me: list every file in the project
   folder, which lab produced it, and what it is for. Then tell me
   which instructions, context files or memory-file lines are now
   out of date.
   ```

   Compare its list with the folder on your computer.


9. Open Settings → Usage and see how much of your plan today's labs used.  
   *Why:* Parallel tasks finish faster but use more in total — worth knowing before you schedule work every day.

#### Check

> **Check — you are done when:** Two scheduled tasks are listed on the project — Today's Lumo post on weekdays at 9:00am and Weekly launch report on Mondays at 8:00am — both drafting and emailing only, with nothing published. lumo-project-memory.md records the 8 December Singapore launch, Claude listed what depends on it, and the project review matches the files in your Lumo Launch folder.


## Wrap-Up

Across ten labs you took one product launch from an empty project to a researched, branded and scheduled campaign.

#### What you built

- The Lumo Cold Kopi Launch project, with instructions, context, a folder and a memory file.
- A market research brief merged from four parallel tasks, with conflicts flagged.
- A Market Insights Live Artefact dashboard, saved and downloaded.
- Google Drive and Gmail connected, with an approved summary sent to yourself.
- A launch deck in Slides and a campaign brief in Docs.
- A lumo-brand-voice Agent Skill and the Marketing plugin.
- Two weeks of social posts across four platforms.
- A 15-second vertical launch video.
- Scheduled tasks that draft the daily post and the weekly report for your approval.

#### The habit to keep

- Give long-running work a project with clear instructions, not a string of chats.
- Split big jobs into focused tasks, one subject each, and merge the results.
- Check every figure and claim against the source before anything goes out.
- Write a routine down once as a skill instead of retyping it every time.
- Schedule the drafting; keep the publishing click for yourself.

#### Next steps

- **Start one real Project** — Give your next campaign a project with instructions, context and a folder.
- **Split one job into tasks** — Next time you research competitors, give each one its own task.
- **Capture your brand voice** — Turn your real brand guide into a skill your whole team shares.
- **Schedule one routine** — Pick the post or report you produce every week and schedule the draft.
- **Watch for the new Projects** — When your account gets the lead agent and threads, the Threads edition of this course shows the same labs on it.


## Glossary

| Term | Meaning |
|---|---|
| Agent Skill | A folder containing a SKILL.md of instructions that Claude loads on demand when the task matches its description. |
| Artefact | A self-contained output Claude builds — a document, dashboard or tool — shown beside the chat rather than inside it. |
| Claude Project | A workspace for one long-running body of work, with its own instructions, context files, working folder and scheduled tasks. |
| Connector | An integration that lets Claude reach an outside service such as Google Drive, Gmail or Calendar. |
| Live Artefact | An artefact that persists in your workspace, keeps its state, and can refresh its data when reopened. |
| MCP | Model Context Protocol — the open standard connectors use to expose tools and data to Claude. |
| Memory | What a project keeps between tasks. In a classic project, the memory file you ask Claude to maintain; in the new Projects, editable memory in settings. |
| Memory file | A Markdown file in the project folder where Claude records decisions you ask it to keep, read by every later task. |
| Mod | A change to Claude's own interface or behaviour, such as a side panel, status line, slash command or hook. |
| Plugin | A packaged bundle of skills, tools, agents and hooks, installed in one step. |
| Project folder | The folder on your computer a Cowork project works in: Claude reads data there and writes its outputs back. |
| SKILL.md | The Markdown file at the heart of an Agent Skill: name, description and instructions. |
| Scheduled task | A prompt a project runs automatically on a timetable. |
| Task | One job you start inside a project. Several tasks can run at once. |
