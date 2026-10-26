#!/usr/bin/env python3
"""Generate labs/README.md, the labs index, from the same single source as the
deck and guide.

From v5.0 a lab folder holds only two things: the lab's prompt PDF
(build_lab_pdfs.py) and, where the lab needs it, a data/ folder of mock data
and assets (build_mockdata.py). The full instructions and check steps live in
the Learner Guide, so no per-lab Markdown is written here.

The shared helpers below (ACTS, REPO, lab_dir, ...) are imported by
build_lab_pdfs.py, build_prompts_page.py and build_readme.py, so every lab
artifact names its folders and files the same way.
"""
import os, sys, glob, re, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def load_domains():
    acts = []
    for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py")),
                    key=lambda p: int("".join(c for c in os.path.basename(p) if c.isdigit()) or 0)):
        if not re.fullmatch(r"data_domain\d+\.py", os.path.basename(f)):
            continue
        mod = importlib.import_module(os.path.basename(f)[:-3])
        n = "".join(c for c in os.path.basename(f) if c.isdigit())
        acts += getattr(mod, f"DOMAIN{n}", [])
    return sorted(acts, key=lambda a: a["num"])


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return start


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")
ACTS = load_domains()
TOPIC = {t["num"]: t for t in C.TOPICS}
_NUMWORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
             7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}


# ------------------------------------------------------------------ naming
def lab_folder(a):
    """labs/<this>/ — e.g. lab-01-set-up-the-launch-project."""
    return f"lab-{a['num']:02d}-{C.LAB_SLUGS[a['num']]}"


def lab_dir(a):
    return os.path.join(LABS, lab_folder(a))


def pdf_name(a):
    """The prompt PDF is named after its folder: lab-01-<slug>/lab-01-<slug>.pdf."""
    return f"{lab_folder(a)}.pdf"


def blocks(a):
    """A lab's prompts as a list of blocks, whatever shape the source uses.

    Most labs carry one `prompt`; multi-message labs carry `prompt_blocks`
    (label, lead, text, after). Normalising here means the PDF and the web page
    render one shape and cannot disagree about what a lab asks learners to send.
    """
    if a.get("prompt_blocks"):
        return a["prompt_blocks"]
    return [dict(label="Prompt", lead="", text=a["prompt"], after="",
                 step=a.get("prompt_step"))]


def steps_with_prompts(a):
    """The lab as one ordered walk-through: [(n, step, why, [blocks])].

    Every prompt names the step it belongs to (`prompt_step` on a one-prompt
    lab, `step` on each block), so the PDF and the web page can place each
    prompt box directly under its step — step, prompt, step, prompt. A prompt
    whose step is missing or out of range fails the build rather than being
    silently dropped from what learners see.
    """
    by_step = {}
    for b in blocks(a):
        s = b.get("step")
        assert isinstance(s, int) and 1 <= s <= len(a["steps"]), (
            f"Lab {a['num']}: prompt {b['label']!r} has step={s!r}; "
            f"expected 1..{len(a['steps'])}")
        by_step.setdefault(s, []).append(b)
    return [(i, step, why, by_step.get(i, []))
            for i, (step, why) in enumerate(a["steps"], 1)]


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def scenario_md(level="##"):
    """The overarching course story (COURSE_SCENARIO) as a short Markdown section,
    shared by labs/README.md and the repository README."""
    sc = C.COURSE_SCENARIO
    return [f"{level} The scenario — {sc['title']}", "",
            f"**The situation.** {sc['situation']}", "",
            f"**Your role.** {sc['role']}", "",
            f"**The mission.** {sc['mission']}", ""]


# ------------------------------------------------------------------ README
def readme():
    out = [
        f"# {C.TITLE} — Labs",
        "",
        C.COMPANY_BLURB,
        "",
        f"{_NUMWORDS.get(len(ACTS), len(ACTS))} labs, one continuous build, "
        f"opening with {ACTS[0]['title']}.",
        "Every lab after it extends the same project, so work through them in order.",
        "",
    ]
    out += scenario_md("##")
    if getattr(C, "LABS_README_NOTE", ""):
        out += [C.LABS_README_NOTE.strip(), ""]
    out += [
        f"**Copy-ready prompts:** every prompt below is also on the [Lab Prompts page]({C.PROMPTS_URL}),",
        "with a one-click **Copy** button for each block.",
        "",
        "| Lab | Topic | Title | Prompt PDF | Data |",
        "|---:|---|---|---|---|",
    ]
    for a in ACTS:
        t = TOPIC[a["topic"]]
        folder = lab_folder(a)
        pdf = f"[PDF]({folder}/{pdf_name(a)})"
        n = len(a.get("data", []))
        data = f"[{n} file{'s' if n != 1 else ''}]({folder}/data/)" if n else "—"
        out.append(f"| {a['num']:02d} | {t['code']} {t['title']} | {a['title']} | {pdf} | {data} |")
    out += ["", "## Lab objectives", ""]
    out += [f"- **Lab {a['num']:02d}.** By the end of this lab you can {a['objective']}." for a in ACTS]
    out += [
        "",
        "## What each lab folder holds",
        "",
        "- `lab-NN-<name>.pdf` — the course scenario, the lab's scenario and objective, then the",
        "  steps with each prompt in a copy-friendly box under the step that sends it, and the check.",
        "- `data/` — the synthetic Lumo Kopi files and assets the lab uses (where it needs any).",
        "",
        "Labs with no `data/` folder work from what the project already holds.",
        "",
        "## Ground rules",
        "",
        C.LAB_NOTE,
        "",
    ]
    return "\n".join(out)


def main():
    write(os.path.join(LABS, "README.md"), readme())
    print(f"  index  labs/README.md  ({len(ACTS)} labs)")


if __name__ == "__main__":
    print("Generating labs index")
    main()
