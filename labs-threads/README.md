# Claude AI Masterclass — Labs

**Threads Edition** · v6.0 · 28 October 2026. For the redesigned Claude Projects beta — a project with a Goal, a lead agent and parallel threads.
Not sure? If your Projects page shows a Goal and threads, use Threads; otherwise Classic. The other edition: [Classic Projects Edition labs](../labs/README.md).

Lumo Kopi Co. is a fictitious Singapore coffee brand about to launch Lumo Cold Kopi — a ready-to-drink oat-milk kopi cold brew in a 240 ml can — in Singapore on 1 December 2026 and Kuala Lumpur in January 2027. You are its marketing team. All brands, figures, survey answers and documents in this course are synthetic and used for training only.

Ten labs, one continuous build, opening with Set Up the Lumo Launch Project.
Every lab after it extends the same project, so work through them in order.

## The scenario — The Lumo Cold Kopi launch

**The situation.** It is late October 2026. Lumo Kopi Co. launches Lumo Cold Kopi, its first ready-to-drink canned kopi, in Singapore on 1 December — six weeks away — and in Kuala Lumpur in January. The marketing team is small, the budget is S$60,000, and nothing has been produced yet: no research, no deck, no posts, no video.

**Your role.** You are the Lumo marketing team. Instead of juggling a dozen separate chats, you run the whole launch from one Claude Project. Its lead agent plans each job, starts parallel threads for the pieces, and brings the results back for you to check and approve.

**The mission.** By the end of the day the project holds everything the launch needs — verified market research, a dashboard, a deck and brief, a brand-voice skill, two weeks of social posts, a launch video — and scheduled tasks that keep it moving while you are away.

All ten labs run inside **one Claude Project** — the Lumo Cold Kopi Launch project you
create in Lab 1. Labs 2 and 8 hand a job to the project's lead agent, which splits it
into parallel threads, one per subject.

Each lab folder holds only the **prompt PDF** and, where the lab needs it, a **data/**
folder of mock data and assets. The full step-by-step instructions and check steps are
in the Learner Guide, and every prompt is on the copy-ready prompts page.

**Copy-ready prompts:** every prompt below is also on the [Lab Prompts page](https://tertiarycourses.github.io/C1382-Claude-AI-Masterclass/prompts/threads/),
with a one-click **Copy** button for each block.

| Lab | Topic | Title | Prompt PDF | Data |
|---:|---|---|---|---|
| 01 | 01 Claude Projects and Market Research | Set Up the Lumo Launch Project | [PDF](lab-01-set-up-the-launch-project/lab-01-set-up-the-launch-project.pdf) | [3 files](lab-01-set-up-the-launch-project/data/) |
| 02 | 01 Claude Projects and Market Research | Run Market Research in Parallel Threads | [PDF](lab-02-market-research-threads/lab-02-market-research-threads.pdf) | [3 files](lab-02-market-research-threads/data/) |
| 03 | 01 Claude Projects and Market Research | Build the Market Insights Live Artefact | [PDF](lab-03-market-insights-artefact/lab-03-market-insights-artefact.pdf) | [2 files](lab-03-market-insights-artefact/data/) |
| 04 | 02 Connectors, Skills and Plugins | Connect Google Drive and Gmail | [PDF](lab-04-connect-drive-and-gmail/lab-04-connect-drive-and-gmail.pdf) | [2 files](lab-04-connect-drive-and-gmail/data/) |
| 05 | 02 Connectors, Skills and Plugins | Analyse the Survey, Then Build the Deck and Brief | [PDF](lab-05-launch-deck-and-brief/lab-05-launch-deck-and-brief.pdf) | [1 file](lab-05-launch-deck-and-brief/data/) |
| 06 | 02 Connectors, Skills and Plugins | Capture the Brand Voice as an Agent Skill | [PDF](lab-06-brand-voice-skill/lab-06-brand-voice-skill.pdf) | [2 files](lab-06-brand-voice-skill/data/) |
| 07 | 02 Connectors, Skills and Plugins | Add the Marketing Plugin and a Mod | [PDF](lab-07-marketing-plugin/lab-07-marketing-plugin.pdf) | — |
| 08 | 03 Content Production and Scheduled Work | Create and Schedule Social Posts in Parallel Threads | [PDF](lab-08-social-posts-threads/lab-08-social-posts-threads.pdf) | [1 file](lab-08-social-posts-threads/data/) |
| 09 | 03 Content Production and Scheduled Work | Produce a 15-Second Launch Video | [PDF](lab-09-launch-video/lab-09-launch-video.pdf) | [5 files](lab-09-launch-video/data/) |
| 10 | 03 Content Production and Scheduled Work | Schedule the Weekly Report and Review the Project | [PDF](lab-10-schedule-and-review/lab-10-schedule-and-review.pdf) | — |

## Lab objectives

- **Lab 01.** By the end of this lab you can create a Claude Project with a goal, instructions, context and memory.
- **Lab 02.** By the end of this lab you can hand a multi-subject research job to the lead agent and verify the merged brief.
- **Lab 03.** By the end of this lab you can turn research data into an interactive Live Artefact dashboard and save it.
- **Lab 04.** By the end of this lab you can connect Google Drive and Gmail and use their tools to reconcile, search, save and draft, sending only what you approve.
- **Lab 05.** By the end of this lab you can analyse survey data with Claude's code tool and save it to Excel, then produce a launch deck in Slides and a campaign brief in Docs.
- **Lab 06.** By the end of this lab you can capture the brand voice as an Agent Skill with /skill-creator, read its SKILL.md, use it on workplace messages and update it.
- **Lab 07.** By the end of this lab you can install a plugin, use its namespaced commands alongside your own skill, and build a mod that suggests the next social post.
- **Lab 08.** By the end of this lab you can produce a two-week, four-platform social calendar with one thread per channel, and schedule the daily post.
- **Lab 09.** By the end of this lab you can script, storyboard and render a vertical launch video from supplied brand assets.
- **Lab 10.** By the end of this lab you can schedule a weekly report beside the daily post, edit project memory and review thread usage.

## What each lab folder holds

- `lab-NN-<name>.pdf` — the course scenario, the lab's scenario and objective, then the
  steps with each prompt in a copy-friendly box under the step that sends it, and the check.
- `data/` — the synthetic Lumo Kopi files and assets the lab uses (where it needs any).

Labs with no `data/` folder work from what the project already holds.

## Ground rules

Use only the supplied mock data and your own test accounts. Never put real customer, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
