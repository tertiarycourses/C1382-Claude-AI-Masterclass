#!/usr/bin/env python3
"""Generate the copy-ready Lab Prompts web page (GitHub Pages) from the SAME
single source (course_data.py + data_domainN.py) that drives the lab PDFs:

  docs/prompts/index.html   the course scenario, then every lab grouped by
                            topic: scenario, objective, what you build, data
                            files, then ONE numbered list of steps with each
                            prompt (lead line, Copy button, after line) placed
                            under the step that sends it, and the check
  docs/index.html           a small landing page: prompts, repo, registration
  docs/.nojekyll

Self-contained HTML/CSS/JS (no external scripts or fonts), in the Claude Style
warm palette. Serve with GitHub Pages from the main branch /docs folder.
Modelled on the C34 Copilot for Excel prompts page.
"""
import datetime, html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from build_labs import ACTS, REPO, TOPIC, lab_folder, pdf_name, blocks, steps_with_prompts

DOCS = os.path.join(REPO, "docs")
GH = C.REPO_URL.rstrip("/")


# ------------------------------------------------------------------ text helpers
def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def md(s):
    """Escape, then render the source's **bold** and `code` spans."""
    s = esc(" ".join(s.split()))
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def marked(s):
    """Escape a prompt, then highlight <PLACEHOLDERS> the learner must replace."""
    return re.sub(r"&lt;([A-Z][^&\n]*?)&gt;", r"<mark>&lt;\1&gt;</mark>", esc(s))


def gh_path(*parts):
    """A GitHub URL path segment, with spaces (e.g. "Lumo Launch/") encoded."""
    return "/".join(p.replace(" ", "%20") for p in parts)


def copy_btn(text, what):
    # Hidden until the script runs: with no JavaScript the prompt text is still
    # there to select by hand, and no dead button is shown.
    return (f'<button class="copy" type="button" hidden data-copy="{attr(text)}" '
            f'aria-label="Copy {attr(what)}">Copy</button>')


# ------------------------------------------------------------------ one lab
def prompt_card(a, b, multi):
    """One prompt: label + Copy button, lead line, the exact text, after line."""
    n, text = a["num"], b["text"].strip("\n")
    name = b["label"] if multi else "Prompt"
    what = f"Lab {n} {name}"
    lead = f'<p class="lead">{md(b["lead"])}</p>' if b.get("lead") else ""
    after = f'<p class="after">{md(b["after"])}</p>' if b.get("after") else ""
    notes = "".join(f'<p class="note"><b>Note:</b> {md(x)}</p>' for x in b.get("notes", []))
    return (f'<article class="prompt" aria-label="{attr(what)}">'
            f'<header><span class="pname"><span class="badge">Lab {n}</span> {esc(name)}</span>'
            f'{copy_btn(text, what)}</header>{lead}'
            f'<pre tabindex="0">{marked(text)}</pre>{after}{notes}</article>')


def render_lab(a):
    n, folder = a["num"], lab_folder(a)
    t = TOPIC[a["topic"]]
    links = [f'<a href="{GH}/blob/main/labs/{folder}/{pdf_name(a)}">Prompt PDF</a>']
    if a.get("data"):
        links.append(f'<a href="{GH}/tree/main/labs/{folder}/data">Data folder on GitHub</a>')
        data = ", ".join(f'<a href="{GH}/blob/main/labs/{gh_path(folder, "data", f)}"><code>{esc(f)}</code></a>'
                         for f in a["data"])
    else:
        data = "None — this lab works from what the project already holds."

    facts = [("Scenario", esc(a["desc"])),
             ("Objective", f"By the end of this lab you can {esc(a['objective'])}."),
             ("You will build", f'{esc(a["build"])} <span class="uses">Uses: {esc(a["services"])}</span>'),
             ("Data files", data)]
    facts_html = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in facts)

    # Prerequisites first: the prompt note and tool notes say what to attach,
    # install or replace before step 1, so they sit above the walk-through.
    notes = list(a.get("prompt_notes", [])) + ([a["prompt_note"]] if a.get("prompt_note") else [])
    before = "".join(f'<p class="note"><b>Note:</b> {md(x)}</p>' for x in notes)
    before += "".join(f'<p class="note"><b>{esc(h)}.</b> {md(body)}</p>'
                      for h, body in (a.get("tools_sections") or []))
    if before:
        before = f'<div class="before"><h4>Before you start</h4>{before}</div>'

    # The walk-through: one numbered list, each prompt directly under its step.
    multi = len(blocks(a)) > 1
    has_ph, items = False, []
    for i, step, why, bl in steps_with_prompts(a):
        has_ph |= any("<mark>" in marked(b["text"]) for b in bl)
        tag = (f' <span class="tag">Prompt{"s" if len(bl) > 1 else ""} below</span>' if bl else "")
        items.append(
            f'<li class="{"has-prompt" if bl else ""}" id="lab-{n}-step-{i}">'
            f'<p class="step">{md(step)}{tag}</p>'
            + (f'<p class="why">{md(why)}</p>' if why else "")
            + "".join(prompt_card(a, b, multi) for b in bl) + "</li>")
    intro = f'<p class="intro">{md(a["prompt_intro"])}</p>' if a.get("prompt_intro") else ""
    hint = ('<p class="hint">Replace the <mark>highlighted</mark> parts with your own details before you send.</p>'
            if has_ph else "")

    return (
        f'<section class="lab" id="lab-{n}" aria-labelledby="lab-{n}-title">'
        f'<p class="eyebrow">Lab {n:02d} · Topic {t["code"]}</p>'
        f'<h3 id="lab-{n}-title">{esc(a["title"])}</h3>'
        f'<dl class="facts-list">{facts_html}</dl>'
        f'<p class="links">{" · ".join(links)}</p>{before}'
        f'<h4>Steps and prompts — {esc(a["prompt_title"])}</h4>{intro}{hint}'
        f'<ol class="steps" role="list">{"".join(items)}</ol>'
        f'<div class="check" role="note" aria-label="Check"><h4>Check — done when</h4><p>{esc(a["test"])}</p></div>'
        f'<p class="top"><a href="#top">Back to top</a></p>'
        f"</section>")


def scenario_html():
    """The overarching course story, shown once at the top of the prompts page."""
    sc = C.COURSE_SCENARIO
    rows = "".join(f"<dt>{k}</dt><dd>{esc(sc[key])}</dd>"
                   for k, key in (("The situation", "situation"), ("Your role", "role"),
                                  ("The mission", "mission")))
    return (f'<section class="scenario" aria-labelledby="scenario-title">'
            f'<p class="eyebrow">The course scenario</p>'
            f'<h2 id="scenario-title">{esc(sc["title"])}</h2><dl>{rows}</dl></section>')


# ------------------------------------------------------------------ shared look
# Claude Style: terracotta accent, ink text, warm cream ground; a warm dark
# variant follows the system setting. Filled buttons and badges use the darker
# --btn terracotta: white on #D97757 is only 3.1:1, on #B85A3A it is 4.6:1 (AA).
CSS = """
:root{--bg:#FAF9F5;--panel:#fff;--ink:#21201C;--muted:#5F5B54;--rule:#E4E1D9;
--accent:#D97757;--btn:#B85A3A;--accent-ink:#A8502F;--on-accent:#fff;--accent-bg:#FBF3EF;--ok:#3E7A52;
--mark:#F8E3C4;--code:#F5F3EE;--note:#F5F3EE}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
--bg:#1F1E1B;--panel:#2A2925;--ink:#F1EEE6;--muted:#BDB7AB;--rule:#3D3B36;
--accent:#E08A6D;--btn:#E08A6D;--accent-ink:#F0A68C;--on-accent:#1F1E1B;--accent-bg:#352A25;--ok:#7CC096;
--mark:#5C4630;--code:#23221F;--note:#2F2D29}}
:root[data-theme="dark"]{--bg:#1F1E1B;--panel:#2A2925;--ink:#F1EEE6;--muted:#BDB7AB;--rule:#3D3B36;
--accent:#E08A6D;--btn:#E08A6D;--accent-ink:#F0A68C;--on-accent:#1F1E1B;--accent-bg:#352A25;--ok:#7CC096;
--mark:#5C4630;--code:#23221F;--note:#2F2D29}
*{box-sizing:border-box}
html{scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--ink);
font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Calibri,Roboto,sans-serif}
.wrap{max-width:880px;margin:0 auto;padding:28px 16px 80px}
a{color:var(--accent-ink);text-underline-offset:2px}
a:focus-visible,button:focus-visible,summary:focus-visible,pre:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
h1,h2,h3{font-family:Cambria,Georgia,"Times New Roman",serif;font-weight:600;line-height:1.2}
h1{font-size:34px;margin:6px 0 8px}
h2{font-size:24px;margin:44px 0 4px;padding-top:6px;border-top:3px solid var(--accent)}
h3{font-size:25px;margin:4px 0 10px}
h4{font-size:14px;letter-spacing:.07em;text-transform:uppercase;color:var(--accent-ink);margin:26px 0 10px}
.eyebrow{margin:0;color:var(--accent-ink);font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.sub{color:var(--muted);margin:0 0 14px}
.topic-sub{color:var(--muted);margin:0 0 6px;font-size:15px}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:8px;z-index:9;background:var(--panel);padding:8px 12px}
nav{position:sticky;top:0;z-index:2;background:var(--bg);padding:10px 0;margin-top:8px;
border-bottom:1px solid var(--rule);display:flex;flex-wrap:wrap;gap:6px;align-items:center}
nav span{font-size:13px;font-weight:700;color:var(--muted);margin-right:4px}
nav a{display:inline-block;min-width:44px;text-align:center;padding:7px 10px;border:1.5px solid var(--rule);
border-radius:999px;color:var(--ink);text-decoration:none;font-weight:600;font-size:15px;background:var(--panel)}
nav a:hover{border-color:var(--accent)}
nav a[aria-current="true"]{background:var(--btn);border-color:var(--btn);color:var(--on-accent)}
@media (max-width:600px){nav{flex-wrap:nowrap;overflow-x:auto}nav a{flex:none}h1{font-size:28px}h3{font-size:22px}}
.lab{padding:26px 0 8px;border-bottom:1px solid var(--rule)}
.meta{color:var(--muted);font-size:15px}
.links{font-size:15px;font-weight:600}
details{background:var(--panel);border:1px solid var(--rule);border-radius:10px;padding:8px 14px;margin:0 0 8px}
summary{cursor:pointer;font-weight:600}
details ol,details ul{margin:8px 0 4px;padding-left:22px}details li{margin:6px 0}
details.files{font-size:15px}
details.check{border-left:4px solid var(--ok)}
.intro,.hint{font-size:16px}.hint{color:var(--muted)}
mark{background:var(--mark);color:inherit;border-radius:3px;padding:0 2px}
code{font:0.9em ui-monospace,Menlo,Consolas,monospace}
.prompt{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--accent);
border-radius:10px;margin:0 0 16px;overflow:hidden}
.prompt header{display:flex;justify-content:space-between;align-items:center;gap:12px;
padding:9px 14px;background:var(--accent-bg)}
.pname{font-weight:700}
.badge{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
background:var(--btn);color:var(--on-accent);border-radius:999px;padding:2px 9px;margin-right:6px;vertical-align:1px}
.lead,.after{margin:0;padding:12px 14px 0;font-size:16px}
.after{padding:0 14px 12px;color:var(--muted)}
.prompt pre{margin:10px 14px 12px;padding:14px;background:var(--code);border-radius:8px;
white-space:pre-wrap;word-wrap:break-word;font:14.5px/1.55 ui-monospace,Menlo,Consolas,monospace}
.prompt .note{margin:0 14px 12px}
.note{background:var(--note);border-radius:8px;padding:10px 14px;font-size:15px}
.copy{flex:none;font:inherit;font-weight:700;font-size:15px;color:var(--on-accent);background:var(--btn);
border:0;border-radius:8px;padding:8px 18px;cursor:pointer;min-height:40px;min-width:92px}
.copy:hover{filter:brightness(1.07)}
.copy.done{background:var(--ok)}
.top{font-size:14px;margin:6px 0 0}
.card{background:var(--panel);border:1px solid var(--rule);border-radius:12px;padding:18px 20px;margin:18px 0}
.facts{width:100%;border-collapse:collapse;font-size:16px}
.facts th,.facts td{text-align:left;padding:8px 6px;border-bottom:1px solid var(--rule);vertical-align:top}
.facts th{color:var(--muted);font-weight:600;width:38%}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}
.btn{display:inline-block;padding:11px 18px;border-radius:10px;font-weight:700;text-decoration:none;
border:1.5px solid var(--accent);color:var(--accent-ink)}
.btn.primary{background:var(--btn);border-color:var(--btn);color:var(--on-accent)}
footer{margin-top:40px;color:var(--muted);font-size:14px}
.scenario{background:var(--panel);border:1px solid var(--rule);border-top:4px solid var(--accent);
border-radius:12px;padding:16px 20px 8px;margin:18px 0 6px}
.scenario h2{border:0;margin:2px 0 10px;padding:0;font-size:24px}
.scenario dl,.facts-list{margin:0}
.scenario dt,.facts-list dt{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-ink)}
.scenario dd{margin:2px 0 12px}
.facts-list{background:var(--panel);border:1px solid var(--rule);border-radius:10px;padding:12px 16px 2px;margin:4px 0 12px}
.facts-list dd{margin:2px 0 12px}
.facts-list .uses{display:block;color:var(--muted);font-size:15px}
.before .note{margin:0 0 8px}
ol.steps{list-style:none;counter-reset:step;margin:0;padding:0}
ol.steps>li{counter-increment:step;position:relative;padding:0 0 6px 46px;margin:0}
ol.steps>li::before{content:counter(step);position:absolute;left:0;top:0;width:32px;height:32px;
border-radius:50%;border:1.5px solid var(--rule);background:var(--panel);color:var(--ink);
font-weight:700;font-size:15px;line-height:29px;text-align:center}
ol.steps>li::after{content:"";position:absolute;left:15px;top:36px;bottom:4px;width:2px;background:var(--rule)}
ol.steps>li:last-child::after{display:none}
ol.steps>li.has-prompt::before{background:var(--btn);border-color:var(--btn);color:var(--on-accent)}
.step{margin:4px 0 2px}
li.has-prompt>.step{font-weight:600}
.why{margin:0 0 10px;color:var(--muted);font-size:15px}
.tag{display:inline-block;margin-left:6px;font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
color:var(--accent-ink);white-space:nowrap}
ol.steps .prompt{margin:4px 0 14px;position:relative;z-index:1}  /* paint over the step rail */
.check{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--ok);border-radius:10px;
padding:4px 16px 10px;margin:10px 0}
.check h4{color:var(--ok);margin:10px 0 4px}.check p{margin:0}
@media (max-width:600px){ol.steps>li{padding-left:38px}ol.steps>li::before{width:28px;height:28px;line-height:25px;font-size:14px}
ol.steps>li::after{left:13px;top:32px}ol.steps .prompt{margin-left:-38px}.prompt pre{font-size:13.5px}}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
"""

JS = """
(function(){
  var live=document.getElementById('live');
  function fallback(t){var a=document.createElement('textarea');a.value=t;a.setAttribute('readonly','');
    a.style.position='fixed';a.style.top='0';a.style.opacity='0';document.body.appendChild(a);
    a.select();a.setSelectionRange(0,t.length);var ok=false;try{ok=document.execCommand('copy')}catch(e){}
    document.body.removeChild(a);return ok}
  function flash(b,ok){var old=b.getAttribute('data-label')||b.textContent;b.setAttribute('data-label',old);
    b.textContent=ok?'Copied \\u2713':'Press Ctrl+C';b.classList.toggle('done',ok);
    if(live)live.textContent=ok?'Prompt copied to clipboard':'Copy failed - select the text and copy it';
    setTimeout(function(){b.textContent=old;b.classList.remove('done')},1800)}
  var btns=document.querySelectorAll('.copy');
  for(var i=0;i<btns.length;i++){btns[i].hidden=false;btns[i].addEventListener('click',function(){
    var b=this,t=b.getAttribute('data-copy');
    if(navigator.clipboard&&window.isSecureContext){
      navigator.clipboard.writeText(t).then(function(){flash(b,true)},function(){flash(b,fallback(t))});
    }else{flash(b,fallback(t))}
  })}
  /* Highlight the lab currently on screen in the sticky nav. */
  var links=document.querySelectorAll('nav a[href^="#lab-"]');
  if('IntersectionObserver' in window&&links.length){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;
      for(var j=0;j<links.length;j++)links[j].setAttribute('aria-current',links[j].getAttribute('href')==='#'+e.target.id)})},
      {rootMargin:'-30% 0px -60% 0px'});
    document.querySelectorAll('.lab').forEach(function(s){io.observe(s)});
  }
})();
"""


def page(title, desc, body, script=True):
    return f"""<!doctype html>
<html lang="en-SG"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="data:,">
<title>{esc(title)}</title>
<meta name="description" content="{attr(desc)}">
<style>{CSS}</style></head><body>{body}{f'<script>{JS}</script>' if script else ''}</body></html>
"""


def footer():
    today = datetime.date.today().strftime("%-d %B %Y")
    return (f"<footer>{esc(C.TITLE)} ({C.COURSE_CODE}) · courseware {C.VERSION}, {esc(C.VERSION_DATE)}. "
            f"Built from the course source on {today}. {esc(C.COMPANY)} and all lab data are fictitious, "
            f"for training only. {esc(C.LAB_NOTE)} © {esc(C.ORG)} · {esc(C.UEN)}.</footer>")


# ------------------------------------------------------------------ pages
def prompts_page():
    nav = "".join(f'<a href="#lab-{a["num"]}" aria-label="Lab {a["num"]}">{a["num"]}</a>' for a in ACTS)
    sections = []
    for t in C.TOPICS:
        labs = [a for a in ACTS if a["topic"] == t["num"]]
        if not labs:
            continue
        sections.append(
            f'<section aria-labelledby="topic-{t["num"]}"><h2 id="topic-{t["num"]}">Topic {t["code"]} · {esc(t["title"])}</h2>'
            f'<p class="topic-sub">{esc(t["subtitle"])}</p>{"".join(render_lab(a) for a in labs)}</section>')
    body = f"""<a class="skip" href="#main">Skip to the prompts</a>
<div class="wrap" id="top">
<p class="eyebrow">{C.COURSE_CODE} · {esc(C.TITLE)} · {C.VERSION}</p>
<h1>Lab Prompts</h1>
<p class="sub">All {len(ACTS)} labs, step by step. Each lab reads top to bottom — step, prompt, step, prompt.
When a step has a prompt, click <b>Copy</b> and paste it into your <b>{esc(C.PROJECT_NAME)}</b> project in Claude.
Every prompt card is labelled with its lab — check it before you copy.</p>
<p class="links"><a href="{GH}">Course repository</a> · <a href="{GH}/tree/main/labs">Lab folders</a> ·
<a href="../">Course home</a></p>
{scenario_html()}
<nav aria-label="Jump to lab"><span>Lab</span>{nav}</nav>
<main id="main">{"".join(sections)}</main>
<p id="live" class="sr" aria-live="polite"></p>
{footer()}
</div>"""
    return page(f"Lab Prompts · {C.TITLE}",
                f"Copy-ready prompts for every lab of {C.TITLE} ({C.COURSE_CODE}).", body)


def landing_page():
    first, last = _day_bounds()
    rows = [
        ("Course code", C.COURSE_CODE),
        ("Programme", "Non-WSQ"),
        ("Duration", f"{C.DAYS} day · {first}–{last}"),
        ("Format", f"{C.MODE} · {len(ACTS)} labs"),
        ("Courseware", f"{C.VERSION} · {C.VERSION_DATE}"),
    ]
    facts = "".join(f"<tr><th scope='row'>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in rows)
    body = f"""<div class="wrap">
<p class="eyebrow">{C.COURSE_CODE} · {C.VERSION}</p>
<h1>{esc(C.TITLE)}</h1>
<p class="sub">{esc(C.TAGLINE)}</p>
<p>{esc(C.COMPANY_BLURB)}</p>
<div class="btns"><a class="btn primary" href="prompts/">Open the lab prompts</a>
<a class="btn" href="{GH}">Course repository</a>
<a class="btn" href="{attr(C.REGISTRATION)}">Course details and registration</a></div>
<div class="card"><table class="facts"><caption class="sr">Course details</caption>{facts}</table></div>
{footer()}
</div>"""
    return page(C.TITLE, f"{C.TITLE} ({C.COURSE_CODE}) — lab prompts and course materials.", body, script=False)


def _day_bounds():
    """First start and last end of the timetable, e.g. ('9am', '6pm')."""
    rows = [r for _, (_, rs) in sorted(C.SCHEDULE(lambda nums: "").items()) for r in rs]
    return _ampm(rows[0][0]), _ampm(rows[-1][1])


def _ampm(hhmm):
    h, m = (int(x) for x in hhmm.split(":"))
    suffix = "am" if h < 12 else "pm"
    h12 = h % 12 or 12
    return f"{h12}{suffix}" if m == 0 else f"{h12}:{m:02d}{suffix}"


def main():
    os.makedirs(os.path.join(DOCS, "prompts"), exist_ok=True)
    with open(os.path.join(DOCS, "prompts", "index.html"), "w", encoding="utf-8") as f:
        f.write(prompts_page())
    with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
        f.write(landing_page())
    open(os.path.join(DOCS, ".nojekyll"), "a").close()
    n = sum(len(blocks(a)) for a in ACTS)
    print(f"  docs/prompts/index.html  ({len(ACTS)} labs, {n} prompt blocks)")
    print("  docs/index.html, docs/.nojekyll")


if __name__ == "__main__":
    print("Generating prompts page")
    main()
