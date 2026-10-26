#!/usr/bin/env python3
"""Generate the repository README.md — the course landing page on GitHub —
from the same single source as the deck, guide, lab PDFs and prompts page.

Layout follows the C34 Microsoft 365 Copilot for Excel README: title and
pitch, course table, about, learning outcomes, topics, labs, before you start,
courseware package, distribution boundary, data notice and provider. Every
value that course_data.py holds is read from it; paths with spaces use the
<...> link form so GitHub renders them.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from build_labs import ACTS, REPO, TOPIC, lab_folder, pdf_name, scenario_md
from build_prompts_page import _day_bounds

PITCH = (
    "Run a whole product launch from one Claude Project: a lead agent splits the work into "
    "parallel threads for market research, a Live Artefact dashboard, Google Drive and Gmail, "
    "a launch deck and campaign brief, a brand-voice skill, social posts, a launch video and "
    "scheduled tasks."
)


def _hours():
    """Length of the timetabled day in hours, lunch included (9:00–18:00 → 9)."""
    rows = [r for _, (_, rs) in sorted(C.SCHEDULE(lambda nums: "").items()) for r in rs]
    to_min = lambda hhmm: int(hhmm.split(":")[0]) * 60 + int(hhmm.split(":")[1])
    mins = to_min(rows[-1][1]) - to_min(rows[0][0])
    return f"{mins // 60}" if mins % 60 == 0 else f"{mins / 60:.1f}"


def _unwrap(text):
    """Join the hard-wrapped lines of a course_data paragraph block, keeping
    blank-line paragraph breaks."""
    return "\n\n".join(" ".join(p.split()) for p in text.strip().split("\n\n"))


def _labs_in(topic_num):
    nums = [a["num"] for a in ACTS if a["topic"] == topic_num]
    if not nums:
        return "—"
    return f"Lab {nums[0]}" if len(nums) == 1 else f"Labs {nums[0]}–{nums[-1]}"


def readme():
    first, last = _day_bounds()
    deck = f"courseware/{C.SHORT_TITLE}-{C.VERSION}"
    lg, lp = f"LG-{C.SHORT_TITLE}", f"LP-{C.SHORT_TITLE}"
    out = [
        f"# {C.TITLE}",
        "",
        PITCH,
        "",
        "| Course detail | Information |",
        "|---|---|",
        f"| Course code | `{C.COURSE_CODE}` |",
        "| Programme | Non-WSQ |",
        f"| Duration | {C.DAYS} day · {_hours()} hours with lunch ({first}–{last}) |",
        f"| Format | {C.MODE.split(',')[0]}, with {len(ACTS)} hands-on labs in one Claude Project |",
        f"| Registration | [View course details and register]({C.REGISTRATION}) |",
        f"| Lab prompts | [Copy-ready prompts page]({C.PROMPTS_URL}) |",
        f"| Courseware version | {C.VERSION} · {C.VERSION_DATE} |",
        "",
        "---",
        "",
        "## About the course",
        "",
        C.LG_INTRO,
        "",
        C.COMPANY_BLURB,
        "",
        "The course is built for marketing teams — no coding required. Every lab ends with a "
        "check step that lists the exact figures you should see, so you can verify Claude's "
        "output against the source data before anything goes out.",
        "",
        *scenario_md("##"),
        "## Learning outcomes",
        "",
        "By the end of the course, you will be able to:",
        "",
    ]
    for i, (lo, title) in enumerate(zip(C.LEARNING_OUTCOMES, C.LO_TITLES), 1):
        text = lo.split(":", 1)[1].strip() if lo.startswith("LO") else lo
        out.append(f"{i}. **{title}.** {text}")
    out += [
        "",
        "## Topics covered",
        "",
        "| Topic | Content | Labs |",
        "|---|---|---|",
    ]
    for t in C.TOPICS:
        content = "; ".join(s.strip() for s in t["subtitle"].split("·"))
        out.append(f"| **{t['num']}. {t['title']}** | {content} | {_labs_in(t['num'])} |")

    out += [
        "",
        "## Labs",
        "",
        _unwrap(C.LABS_README_NOTE),
        "",
        f"All lab prompts are also on one web page with one-click **Copy** buttons: "
        f"[Lab Prompts]({C.PROMPTS_URL}).",
        "",
        "See the [labs index](labs/README.md).",
        "",
        "| # | Lab | Topic | Prompt PDF | Data |",
        "|---:|---|---|---|---|",
    ]
    for a in ACTS:
        folder = f"labs/{lab_folder(a)}"
        pdf = f"{folder}/{pdf_name(a)}"
        n = len(a.get("data", []))
        data = f"[{n} file{'s' if n != 1 else ''}]({folder}/data/)" if n else "—"
        # The objective sits under the title in the same cell — a sixth column
        # would make the table unreadable on GitHub's narrow layout.
        out.append(f"| {a['num']} | [{a['title']}]({pdf})<br>*Objective: {a['objective']}.* | "
                   f"{TOPIC[a['topic']]['title']} | "
                   f"[PDF]({pdf}) | {data} |")

    # Before you start: the setup needs, minus the two that point at this repo
    # and the prompts page (the reader is already here), plus the Projects beta
    # note and the lab ground rule.
    needs = [s for s in C.LG_SETUP["needs"] if C.REPO_URL not in s and C.PROMPTS_URL not in s]
    out += ["", "### Before you start", ""]
    out += [f"- {s}" for s in needs]
    out += [f"- {C.LG_SETUP['verify_text']}", f"- {C.LAB_NOTE}"]

    out += [
        "",
        "## Courseware package",
        "",
        "| Item | Files |",
        "|---|---|",
        f"| Slide deck | [PowerPoint](<{deck}.pptx>) · [PDF](<{deck}.pdf>) |",
        f"| Learner Guide | [Word](<courseware/{lg}.docx>) · [PDF](<courseware/{lg}.pdf>) · [Markdown](<{lg}.md>) |",
        f"| Lesson Plan | [Word](<courseware/{lp}.docx>) · [PDF](<courseware/{lp}.pdf>) |",
        f"| Labs | [labs/](labs/README.md): {len(ACTS)} lab folders, each with a prompt PDF and, where needed, a `data/` folder of mock data |",
        f"| Lab prompts | [Copy-ready prompts page]({C.PROMPTS_URL}) (source in `docs/`) |",
        "",
        "The deck, Learner Guide, Lesson Plan, lab PDFs and prompts page are all generated from one "
        "content source (`course_data.py` and `data_domain1..3.py` in the course build engine), so "
        "they stay aligned.",
        "",
        "## Distribution boundary",
        "",
        "This repository publishes the current learner-facing courseware, lab PDFs, mock data and "
        "the prompts page. It does not publish superseded versions (`courseware/archive/`), source "
        "reference material or credentials. This is a non-WSQ commercial course, so it has no "
        "assessment.",
        "",
        "## Data notice",
        "",
        f"{C.COMPANY}, Lumo Cold Kopi, the competitor brands, the survey responses, budgets and every "
        "other figure or document in this course are **fictional training data**, generated for this "
        "course. Any resemblance to a real company or person is coincidental. Do not paste real "
        "customer or personal data into Claude during practice.",
        "",
        "## Provider",
        "",
        f"Developed and delivered by **{C.ORG}** (Tertiary Courses), Singapore · "
        f"{C.UEN.replace('UEN: ', 'UEN ')}  ",
        f"Course page: <{C.REGISTRATION}>",
        "",
    ]
    return "\n".join(out)


def main():
    path = os.path.join(REPO, "README.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(readme())
    print(f"  README.md  ({len(ACTS)} labs, {C.VERSION})")


if __name__ == "__main__":
    print("Generating repository README")
    main()
