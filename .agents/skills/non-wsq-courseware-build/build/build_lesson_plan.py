#!/usr/bin/env python3
"""Generate the non-WSQ Lesson Plan (LP) DOCX in the Tertiary house format.

Cover page + Document Version Control Record + auto TOC + Arial 11pt body +
colour-coded daily schedule tables (times, lunch and tea breaks read from
course_data.SCHEDULE; 8 scheduled hours per day excluding lunch, tea breaks
within). NO assessment, funding, SSG or TRAQOM content. Day themes,
topics, schedule and labs all come from course_data + the domain data files so
the LP stays aligned with the deck, guide and labs.
"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
# Dynamic domain import — supports ANY number of data_domainN.py files.
import importlib, glob as _glob
def _load_domains():
    acts=[]
    for f in sorted(_glob.glob(os.path.join(HERE,"data_domain[0-9]*.py")),
                    key=lambda q:int("".join(c for c in os.path.basename(q) if c.isdigit()) or 0)):
        n="".join(c for c in os.path.basename(f) if c.isdigit())
        acts+=getattr(importlib.import_module(os.path.basename(f)[:-3]),f"DOMAIN{n}",[])
    return acts
ACT=_load_domains()
import prodoc
def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE); ASSETS=os.path.join(os.path.dirname(HERE),"assets")

BRAND=RGBColor(0x1F,0x6F,0xEB); DARK=RGBColor(0x11,0x18,0x27); GREY=RGBColor(0x55,0x5B,0x66)
HEADER_FILL="1F6FEB"; TOPIC_FILL="E8F0FE"; BREAK_FILL="FFF4E5"; LUNCH_FILL="FDE9D9"; ASSESS_FILL="E8F7EE"

def lab_titles(nums):
    return "; ".join(f"Lab {a['num']}: {a['title']}" for a in ACT if a['num'] in nums)

# ------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The schedule is supplied by course_data.SCHEDULE
# as {day: (theme, [(start, end, mins, kind, text), ...])} where kind is one of
# admin/topic/lab/break/lunch/recap. `lab_titles([...])` is available to course
# authors for building the activity text from the lab data.
SCHEDULE=C.SCHEDULE(lab_titles) if callable(getattr(C,"SCHEDULE",None)) else getattr(C,"SCHEDULE",{})
if not SCHEDULE:
    raise SystemExit("course_data.py must define SCHEDULE (dict or callable taking lab_titles)")

# ------------------------------------------------ build document
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)

prodoc.add_cover_page(doc,"LESSON PLAN",C.TITLE,f"{C.VERSION.lstrip('v')} · {C.VERSION_DATE}",
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,getattr(C,"VERSION_HISTORY",[(C.VERSION.lstrip("v"),C.VERSION_DATE,"Initial release.",C.TRAINER)]))
prodoc.add_toc(doc)

def H(text,level=1):
    h=doc.add_heading(text,level=level); return h

H("Course Information",1)

# Daily timing is READ FROM the schedule rather than hard-coded, so this row can
# never contradict the timetable below it. Times in SCHEDULE are 24h "H:MM".
def _fmt12(hhmm):
    h,m=(int(x) for x in hhmm.split(":"))
    ap="am" if h<12 else "pm"
    hh=h if 1<=h<=12 else (h-12 if h>12 else 12)
    return f"{hh}:{m:02d} {ap}"

_day_rows=next(iter(SCHEDULE.values()))[1]
_first,_last=_day_rows[0][0],_day_rows[-1][1]
_lunch=sum(d for _s,_e,d,k,_t in _day_rows if k=="lunch")
_daily_timing=(f"{_fmt12(_first)} – {_fmt12(_last)}"
               + (f" ({_lunch//60}-hour lunch; tea breaks within training time)" if _lunch else ""))
# Instructional hours = scheduled time excluding lunch and tea breaks.
_inst_min=sum(d for _s,_e,d,k,_t in _day_rows if k not in ("lunch","break"))

# Hands-on time is summed from the lab rows, so it always matches the timetable.
_lab_min=sum(d for _t,rows_ in SCHEDULE.values() for _s,_e,d,k,_x in rows_ if k=="lab")
_day_min=sum(d for _t,rows_ in SCHEDULE.values() for _s,_e,d,k,_x in rows_)

info=[("Course Title",C.TITLE),("Course Code",C.COURSE_CODE),
      ("Training Provider",C.ORG+"  ("+C.UEN.replace('UEN: ','UEN ')+")"),
      ("Duration",f"{C.DAYS} day{'s' if C.DAYS>1 else ''} · {_inst_min/60:g} instructional hours per day "
                  f"({C.DAYS*_inst_min/60:g} hours)"),
      ("Daily Timing",_daily_timing),
      ("Hands-on Labs",f"{len(ACT)} labs · {_lab_min} of the {_day_min} scheduled minutes "
                       f"({_lab_min*100//_day_min}%) are hands-on lab time"),
      ("Mode",getattr(C,"MODE","Instructor-led, hands-on practical labs")),
      ("Trainer",C.TRAINER)]
t=doc.add_table(rows=0,cols=2); t.style="Table Grid"
for k,v in info:
    c=t.add_row().cells; c[0].text=""; r=c[0].paragraphs[0].add_run(k); r.bold=True; r.font.size=Pt(10)
    prodoc._shade_cell(c[0],TOPIC_FILL)
    c[1].text=""; c[1].paragraphs[0].add_run(v).font.size=Pt(10)
prodoc.set_col_widths(t,(1.6,4.4))

H("Learning Outcomes",1)
doc.add_paragraph("On completion of this course, learners will be able to:")
for lo in C.LEARNING_OUTCOMES:
    p=doc.add_paragraph(style="List Bullet"); p.add_run(lo).font.size=Pt(10.5)

# NON-WSQ: there is NO assessment for this course. Learning is reinforced through
# the hands-on labs and their verification steps instead.
H("Learning Reinforcement",1)
for a_ in ["Each short theory block is followed immediately by the hands-on lab that applies it.",
           "All labs build on one continuous project, so each lab reuses and extends the work of the labs before it.",
           "Each lab ends with a check step in the Learner Guide so learners can confirm their own output against the source data.",
           "The trainer circulates during lab time to give individual feedback and unblock learners.",
           "The day closes with a recap mapped back to the course learning outcomes."]:
    p_=doc.add_paragraph(style="List Bullet"); p_.add_run(a_).font.size=Pt(10.5)

def set_cell(cell,text,bold=False,size=9.5,color=None,fill=None,align=None):
    cell.text=""; p=cell.paragraphs[0]
    if align: p.alignment=align
    r=p.add_run(text); r.bold=bold; r.font.size=Pt(size); r.font.name="Arial"
    if color: r.font.color.rgb=color
    if fill: prodoc._shade_cell(cell,fill)

KIND_FILL={"topic":TOPIC_FILL,"break":BREAK_FILL,"lunch":LUNCH_FILL,
           "admin":"F3F5F8","recap":"F3F5F8","lab":None}

H("Course Schedule",1)
for day,(theme,rows) in SCHEDULE.items():
    H(f"Day {day} — {theme}",2)
    tbl=doc.add_table(rows=0,cols=3); tbl.style="Table Grid"; tbl.alignment=WD_TABLE_ALIGNMENT.CENTER
    hdr=tbl.add_row().cells
    for i,htext in enumerate(["Time","Duration","Topic / Activity"]):
        set_cell(hdr[i],htext,bold=True,size=10,color=RGBColor(0xFF,0xFF,0xFF),fill=HEADER_FILL)
    training=0
    for start,end,mins,kind,text in rows:
        cells=tbl.add_row().cells; fill=KIND_FILL.get(kind)
        set_cell(cells[0],f"{start}–{end}",bold=(kind=="topic"),size=9.5,fill=fill)
        set_cell(cells[1],f"{mins} min",size=9.5,fill=fill)
        set_cell(cells[2],text,bold=(kind=="topic"),size=9.5,fill=fill)
        if kind!="lunch": training+=mins
    # widths (grid + cells, so Word and LibreOffice agree)
    prodoc.set_col_widths(tbl,(1.1,0.8,4.1))
    # `training` excludes lunch but still counts tea breaks, so report both it and
    # the instructional total (tea breaks removed) — the latter is the figure the
    # advertised course duration is based on.
    tea=sum(m for _s,_e,m,k,_t in rows if k=="break")
    inst=training-tea
    r=doc.add_paragraph().add_run(
        f"Total scheduled time: {training} minutes ({training//60} hours) excluding lunch — "
        f"of which {inst} minutes ({inst/60:g} hours) are instructional, plus {tea} minutes of tea breaks.")
    r.italic=True; r.font.size=Pt(9.5); r.font.color.rgb=GREY
    assert training==480, f"Day {day} scheduled minutes = {training}, expected 480"

H("Lab Reference (aligned to course topics)",1)
_lr=doc.add_paragraph("Scheduled time per topic is summed from the timetable above: each topic's "
                      "theory blocks plus the hands-on time for its labs.")
_lr.paragraph_format.keep_with_next=True
# A non-WSQ course has no exam weighting, so the middle column reports the time
# actually scheduled for each topic — summed from the SCHEDULE rows that name it,
# so it can never disagree with the daily timetable above.
def _topic_minutes(tp):
    """Minutes the timetable actually devotes to this topic: its teaching rows
    plus the hands-on rows for its labs. Each row is attributed to at most one
    topic, so the column sums back to the instructional total."""
    mins=0
    # Lab rows carry lab TITLES (built by lab_titles()), not "Lab N:" labels.
    titles={a["title"] for a in ACT if a["topic"]==tp["num"]}
    for _theme,rows in SCHEDULE.values():
        for _start,_end,dur,kind,text in rows:
            if kind=="topic" and (f"Topic {tp['num']} " in text or f"Topic {tp['code']}:" in text):
                mins+=dur
            elif kind=="lab" and any(t in text for t in titles):
                mins+=dur
    return mins


def _hrs(mins):
    """'175 min (2 h 55 min)' — never a raw float like 2.16667 h."""
    h,m=divmod(mins,60)
    span=f"{h} h" + (f" {m} min" if m else "")
    return f"{mins} min ({span})" if h else f"{mins} min"

tt=doc.add_table(rows=0,cols=3); tt.style="Table Grid"
hdr=tt.add_row().cells
for i,htext in enumerate(["Topic","Scheduled time","Labs"]):
    set_cell(hdr[i],htext,bold=True,size=10,color=RGBColor(0xFF,0xFF,0xFF),fill=HEADER_FILL)
for tp in C.TOPICS:
    acts=[a for a in ACT if a["topic"]==tp["num"]]
    mins=_topic_minutes(tp)
    cells=tt.add_row().cells
    set_cell(cells[0],f"Topic {tp['code']}: {tp['title']}",bold=True,size=9.5,fill=TOPIC_FILL)
    set_cell(cells[1],(_hrs(mins) if mins else "—"),size=9.5,fill=TOPIC_FILL)
    set_cell(cells[2],"\n".join(f"Lab {a['num']}: {a['title']}" for a in acts),size=9.5)
prodoc.set_col_widths(tt,(1.8,1.1,3.1))
# Keep the short reference table on one page: rows never split, and every row
# but the last stays with the next one.
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
for _i,_row in enumerate(tt.rows):
    _e=OxmlElement("w:cantSplit"); _e.set(qn("w:val"),"true"); _row._tr.get_or_add_trPr().append(_e)
    if _i<len(tt.rows)-1:
        for _c in _row.cells:
            for _p in _c.paragraphs: _p.paragraph_format.keep_with_next=True

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
OUT=os.path.join(REPO,"courseware",f"LP-{C.SHORT_TITLE}.docx")
prodoc.set_properties(doc, f"Lesson Plan — {C.TITLE}", C.COURSE_CODE)
doc.save(OUT)
print("Saved",OUT)
