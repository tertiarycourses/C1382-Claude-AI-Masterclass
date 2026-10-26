#!/usr/bin/env python3
"""Generate the repository README.md — the course landing page on GitHub —
from the same single source as the deck, guide, lab PDFs and prompts page.

Layout follows the C34 Microsoft 365 Copilot for Excel README: title and
pitch, course table, about, learning outcomes, topics, labs, before you start,
courseware package, distribution boundary, data notice and provider. Every
value that course_data.py holds is read from it; paths with spaces use the
<...> link form so GitHub renders them.

The course ships in two editions from one source. README.md is ONE file for
both: it is always written from the Classic Projects Edition (the default),
names the Threads Edition's prompts page, labs index and courseware files, and
explains which edition to use.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# One README for both editions, always written from the default (classic).
if os.environ.get("COURSE_EDITION", "classic") != "classic":
    os.execvpe(sys.executable, [sys.executable, os.path.abspath(__file__)] + sys.argv[1:],
               {**os.environ, "COURSE_EDITION": "classic"})
sys.path.insert(0, HERE)
import course_data as C
from build_labs import ACTS, REPO, TOPIC, lab_folder, lab_rel, pdf_name, scenario_md, edition_info, EDITION_HINT
from build_prompts_page import _day_bounds

PITCH = (
    "Run a whole product launch from one Claude Project: market research in parallel, a Live "
    "Artefact dashboard, Google Drive and Gmail, a launch deck and campaign brief, a brand-voice "
    "skill, social posts, a launch video and scheduled tasks — in two editions, for the Claude "
    "Projects most accounts have today and for the new Projects beta with a lead agent and threads."
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


def _package_rows(info):
    """Courseware package rows for one edition: deck, LG, LP, labs, prompts."""
    cw, short, ver = info["COURSEWARE_SUBDIR"], info["SHORT_TITLE"], info["VERSION"]
    deck, lg, lp = f"{cw}/{short}-{ver}", f"LG-{short}", f"LP-{short}"
    tag = f"**{info['EDITION_LABEL']}**"
    return [
        f"| {tag} slide deck | [PowerPoint](<{deck}.pptx>) · [PDF](<{deck}.pdf>) |",
        f"| {tag} Learner Guide | [Word](<{cw}/{lg}.docx>) · [PDF](<{cw}/{lg}.pdf>) · [Markdown](<{lg}.md>) |",
        f"| {tag} Lesson Plan | [Word](<{cw}/{lp}.docx>) · [PDF](<{cw}/{lp}.pdf>) |",
        f"| {tag} labs | [{info['LABS_SUBDIR']}/]({info['LABS_SUBDIR']}/README.md): {len(ACTS)} lab folders, "
        f"each with a prompt PDF and, where needed, a `data/` folder of mock data |",
        f"| {tag} lab prompts | [Copy-ready prompts page]({info['PROMPTS_URL']}) "
        f"(source in `{info['PROMPTS_SUBDIR']}/`) |",
    ]


def readme():
    first, last = _day_bounds()
    classic, threads = edition_info("classic"), edition_info("threads")
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
        f"| Lab prompts | [{classic['EDITION_LABEL']}]({classic['PROMPTS_URL']}) · "
        f"[{threads['EDITION_LABEL']}]({threads['PROMPTS_URL']}) |",
        f"| Courseware version | {C.VERSION} · {C.VERSION_DATE} · two editions |",
        "",
        "---",
        "",
        "## Two editions",
        "",
        "Claude Projects are changing, and accounts do not all see the same screen yet, so the "
        "course ships in two editions built from one source. Both run the same ten labs on the "
        "same Lumo Kopi launch, with the same data and the same check figures.",
        "",
        "| Edition | Use it when | Prompts | Labs |",
        "|---|---|---|---|",
        f"| **{classic['EDITION_LABEL']}** (default) | Your Projects page creates a Cowork project "
        f"with Instructions, Context, Folder and Scheduled panels — most accounts today. You start "
        f"parallel tasks yourself. | [Prompts]({classic['PROMPTS_URL']}) | "
        f"[{classic['LABS_SUBDIR']}/]({classic['LABS_SUBDIR']}/README.md) |",
        f"| **{threads['EDITION_LABEL']}** | Your Projects page shows a **Goal** and talks about a "
        f"lead agent and threads — the redesigned Projects beta. The lead agent starts the parallel "
        f"threads for you. | [Prompts]({threads['PROMPTS_URL']}) | "
        f"[{threads['LABS_SUBDIR']}/]({threads['LABS_SUBDIR']}/README.md) |",
        "",
        f"{EDITION_HINT} Everything you build carries over between them: skills, connectors, "
        "artefacts and scheduled tasks work the same way.",
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
        f"The table below is the **{classic['EDITION_LABEL']}** (`{classic['LABS_SUBDIR']}/`). "
        f"The **{threads['EDITION_LABEL']}** labs have their own index: "
        f"[{threads['LABS_SUBDIR']}/README.md]({threads['LABS_SUBDIR']}/README.md).",
        "",
        _unwrap(C.LABS_README_NOTE),
        "",
        f"All lab prompts are also on one web page with one-click **Copy** buttons: "
        f"[Lab Prompts — {classic['EDITION_LABEL']}]({classic['PROMPTS_URL']}) · "
        f"[Lab Prompts — {threads['EDITION_LABEL']}]({threads['PROMPTS_URL']}).",
        "",
        f"See the [labs index]({C.LABS_SUBDIR}/README.md).",
        "",
        "| # | Lab | Topic | Prompt PDF | Data |",
        "|---:|---|---|---|---|",
    ]
    for a in ACTS:
        folder = lab_rel(a)
        pdf = lab_rel(a, pdf_name(a))
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
        *_package_rows(classic),
        *_package_rows(threads),
        "",
        "The deck, Learner Guide, Lesson Plan, lab PDFs and prompts page of both editions are all "
        "generated from one content source (`course_data.py`, `edition_classic.py` and "
        "`data_domain1..3.py` in the course build engine), so they stay aligned.",
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
    print(f"  README.md  ({len(ACTS)} labs, {C.VERSION}, both editions)")


if __name__ == "__main__":
    print("Generating repository README")
    main()
