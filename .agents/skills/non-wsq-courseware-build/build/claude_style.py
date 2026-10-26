#!/usr/bin/env python3
"""Claude Style slide component library.

The house look of the Claude family masterclasses, lifted from the Claude Code
Masterclass (C1417) deck so every Claude course shares one design: terracotta
accent, Cambria headings, Calibri body, white cards on a warm off-white ground (FAF9F5), matching the Agentic AI
Applications with Claude Code deck.

Every component here is a LAYOUT. All wording comes from course_data.py /
data_domainN.py so the PPT, LP, LG and labs stay aligned from one source.
"""
import os, re
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------------------------------------------------------------- palette
CLAY   = RGBColor(0xD9, 0x77, 0x57)   # Claude terracotta — the signature accent
TEAL   = RGBColor(0x3A, 0x7D, 0x7B)   # secondary accent (cover blob, success)
INK    = RGBColor(0x21, 0x20, 0x1C)   # headings and body
MUTED  = RGBColor(0x6B, 0x68, 0x62)   # captions, footers, card body
CREAM  = RGBColor(0xFA, 0xF9, 0xF5)   # slide ground
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)   # card fill
DARK   = RGBColor(0x2E, 0x2C, 0x26)   # dark agenda panel on topic sections
DIM    = RGBColor(0xB9, 0xB4, 0xA9)   # cover subtext on dark
FAINT  = RGBColor(0x8A, 0x86, 0x7D)   # cover copyright
RULE   = RGBColor(0xE4, 0xE1, 0xD9)   # hairline rules
GREEN  = RGBColor(0x4A, 0x8F, 0x5F)   # verify / test-it
AMBER  = RGBColor(0xC8, 0x8A, 0x2E)   # caution

HEAD_FONT = "Cambria"
BODY_FONT = "Calibri"

# Images the components draw themselves (the trainer's certification badge)
# live in the skill's assets/ folder, beside build/.
ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")


class Deck:
    """Wraps a python-pptx Presentation with the Claude Style components."""

    def __init__(self, prs, course):
        self.prs = prs
        self.C = course
        self.blank = prs.slide_layouts[6]
        self.SW = prs.slide_width
        self.SH = prs.slide_height
        self.page = 0

    # ------------------------------------------------------------ primitives
    def slide(self, ground=CREAM):
        s = self.prs.slides.add_slide(self.blank)
        self.rect(s, 0, 0, self.SW, self.SH, ground)
        return s

    def rect(self, s, x, y, w, h, color, line=None):
        sp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, int(x), int(y), int(w), int(h))
        sp.fill.solid()
        sp.fill.fore_color.rgb = color
        if line is None:
            sp.line.fill.background()
        else:
            sp.line.color.rgb = line
            sp.line.width = Pt(0.75)
        sp.shadow.inherit = False
        return sp

    def oval(self, s, x, y, w, h, color):
        sp = s.shapes.add_shape(MSO_SHAPE.OVAL, int(x), int(y), int(w), int(h))
        sp.fill.solid()
        sp.fill.fore_color.rgb = color
        sp.line.fill.background()
        sp.shadow.inherit = False
        return sp

    def txt(self, s, x, y, w, h, lines, align=PP_ALIGN.LEFT,
            anchor=MSO_ANCHOR.TOP, space=4, wrap=True):
        """lines: list of paragraphs; each paragraph is a list of
        (text, size, colour, bold[, font]) run tuples."""
        tb = s.shapes.add_textbox(int(x), int(y), int(w), int(h))
        tf = tb.text_frame
        tf.word_wrap = wrap
        tf.vertical_anchor = anchor
        tf.margin_left = tf.margin_right = 0
        tf.margin_top = tf.margin_bottom = 0
        for i, para in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            p.space_after = Pt(space)
            for run in para:
                text, size, colour, bold = run[:4]
                font = run[4] if len(run) > 4 else BODY_FONT
                r = p.add_run()
                # Lab text is authored as Markdown for the lab files, where
                # `code` and **bold** render. A slide shows the raw characters,
                # so strip the markers here — the one place all slide text
                # passes through — rather than at each call site.
                r.text = re.sub(r"[`*]", "", text) if isinstance(text, str) else text
                r.font.size = Pt(size)
                r.font.bold = bold
                r.font.color.rgb = colour
                r.font.name = font
        return tb

    def footer(self, s, dark=False):
        self.page += 1
        col = DIM if dark else MUTED
        self.txt(s, Inches(0.5), Inches(7.08), Inches(7.0), Inches(0.3),
                 [[("© Tertiary Infotech Academy Pte Ltd", 9, col, False)]])
        self.txt(s, Inches(7.0), Inches(7.08), Inches(5.3), Inches(0.3),
                 [[(self.C.SHORT_TITLE, 9, col, False)]], align=PP_ALIGN.RIGHT)
        self.txt(s, Inches(12.43), Inches(7.08), Inches(0.5), Inches(0.3),
                 [[(str(self.page), 9, col, False)]], align=PP_ALIGN.RIGHT)

    def head(self, title, kicker=None, intro=None):
        """Standard content slide header: kicker, Cambria title, optional intro."""
        s = self.slide()
        if kicker:
            self.txt(s, Inches(0.6), Inches(0.42), Inches(11.0), Inches(0.3),
                     [[(kicker.upper(), 12, CLAY, True)]])
        size = 30 if len(title) <= 46 else (26 if len(title) <= 62 else 22)
        self.txt(s, Inches(0.6), Inches(0.72), Inches(12.1), Inches(0.8),
                 [[(title, size, INK, True, HEAD_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
        if intro:
            self.txt(s, Inches(0.6), Inches(1.85), Inches(12.1),
                     Inches(0.5) + self.intro_extra(intro),
                     [[(intro, 16, INK, False)]])
        return s

    @staticmethod
    def intro_extra(intro):
        """Extra height a wrapped intro needs: about 115 characters of 16pt
        Calibri fit on one 12.1in line, and each extra line takes 0.3in."""
        if not intro:
            return 0
        lines = -(-len(intro) // 115)
        return Inches(0.3) * max(0, lines - 1)

    # ------------------------------------------------------------ templates
    def cover(self):
        C = self.C
        s = self.slide(ground=INK)
        # brand blobs bleeding off the right edge
        self.oval(s, Inches(10.4), Inches(-1.6), Inches(4.6), Inches(4.6), CLAY)
        self.oval(s, Inches(11.6), Inches(4.4), Inches(3.4), Inches(3.4), TEAL)
        self.txt(s, Inches(0.9), Inches(1.5), Inches(8.5), Inches(0.4),
                 [[(f"NON-WSQ COURSE  •  {C.COURSE_CODE}", 14, CLAY, True)]])
        # Under the terracotta circle's arc, left-aligned with the title block,
        # so it never reads on top of the blob.
        self.txt(s, Inches(0.9), Inches(1.92), Inches(8.5), Inches(0.35),
                 [[(f"Version {C.VERSION}  ·  {C.VERSION_DATE}", 12, DIM, False)]])
        self.txt(s, Inches(0.85), Inches(2.45), Inches(9.6), Inches(1.9),
                 [[(C.TITLE, 52, WHITE, True, HEAD_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
        # The edition (two editions build from one source) as the subtitle line,
        # then the tagline under it.
        _ed = getattr(C, "EDITION_LABEL", None)
        if _ed:
            self.txt(s, Inches(0.9), Inches(4.30), Inches(9.0), Inches(0.5),
                     [[(_ed, 22, CLAY, True, HEAD_FONT)]])
        self.txt(s, Inches(0.9), Inches(4.85) if _ed else Inches(4.45), Inches(9.0), Inches(0.5),
                 [[(C.TAGLINE, 16, DIM, False)]])
        self.txt(s, Inches(0.9), Inches(5.7), Inches(11.0), Inches(0.7),
                 [[(C.ORG, 15, WHITE, True)], [(C.UEN, 13, DIM, False)]], space=3)
        self.txt(s, Inches(0.9), Inches(6.75), Inches(8.5), Inches(0.35),
                 [[("www.tertiarycourses.com.sg   |   enquiry@tertiaryinfotech.com   |   +65 6100 0613",
                    12, DIM, False)]])
        # Bottom-left, clear of the teal circle bleeding off the right edge.
        self.txt(s, Inches(0.9), Inches(7.10), Inches(6.0), Inches(0.3),
                 [[("© Tertiary Infotech Academy Pte Ltd", 9, FAINT, False)]])
        self.page += 1
        return s

    def section(self, kicker, title, agenda):
        """Topic divider: terracotta blob bottom-left, dark agenda panel right."""
        s = self.slide(ground=INK)
        self.oval(s, Inches(-1.4), Inches(4.0), Inches(5.0), Inches(5.0), CLAY)
        # A title too long for one line at 40pt wraps to two, and the second
        # line then ran into the blob (whose top is at 4.0in). Set a long title
        # smaller and higher so both lines finish clear of it.
        long_title = len(title) > 30
        ky, ty, th = ((Inches(1.95), Inches(2.45), Inches(1.35)) if long_title
                      else (Inches(2.2), Inches(2.75), Inches(1.8)))
        self.txt(s, Inches(0.9), ky, Inches(8.0), Inches(0.5),
                 [[(kicker.upper(), 16, CLAY, True)]])
        self.txt(s, Inches(0.85), ty, Inches(8.0), th,
                 [[(title, 34 if long_title else 40, WHITE, True, HEAD_FONT)]],
                 anchor=MSO_ANCHOR.MIDDLE)
        ph = Inches(0.62) * len(agenda) + Inches(0.5)
        self.rect(s, Inches(9.1), Inches(1.6), Inches(3.5), ph, DARK)
        for i, item in enumerate(agenda):
            y = Inches(1.92) + Inches(0.62) * i
            self.txt(s, Inches(9.35), y, Inches(0.5), Inches(0.4),
                     [[(str(i + 1), 13, CLAY, True)]])
            self.txt(s, Inches(9.9), y - Inches(0.02), Inches(2.5), Inches(0.5),
                     [[(item, 12, WHITE, False)]], anchor=MSO_ANCHOR.MIDDLE)
        self.footer(s, dark=True)
        return s

    @staticmethod
    def _chips(names):
        """Short, unique badge letters for a family of names. A prefix every
        name shares ("Claude") is skipped; each name takes the initial of its
        first distinguishing word, or two or three letters where that is
        already taken — Claude (Chat + Cowork) -> C, Claude Code -> Co."""
        # Split on anything that is not a letter or digit, so "Claude.ai" and
        # "Claude (Chat + Cowork)" yield words, not "(" or "+" as a chip.
        def _words(n):
            return [w for w in re.split(r"[^A-Za-z0-9]+", n)
                    if w and w.lower() not in ("for", "the")]
        first = _words(names[0])[0].lower() if names else ""
        shared = len(names) > 1 and all(_words(n)[0].lower() == first for n in names)
        chips, used = [], set()
        for n in names:
            ws = _words(n)
            ws = (ws[1:] if shared and len(ws) > 1 else ws) or ws
            cands = [w[:k].title() for k in (1, 2, 3) for w in ws]
            chip = next((c for c in cands if c not in used), cands[0])
            used.add(chip)
            chips.append(chip)
        return chips

    def cards(self, title, items, kicker=None, intro=None, cols=4, tip=None):
        """Grid of white cards, each a terracotta chip + name + caption.
        items: (name, caption) tuples. Used by the Claude Product Family slide.

        The chip letter is the initial of the DISTINGUISHING word, so a family
        of same-prefixed names ("Claude Code", "Claude Cowork") gets C, D, M …
        rather than seven identical C chips. Where two would still collide
        ("Code", "Chrome"), the later one takes two letters (Co, Ch)."""
        s = self.head(title, kicker, intro)
        chips = self._chips([n for n, _cap in items])
        x0, y0 = Inches(0.6), Inches(2.50)
        gut = Inches(0.20)
        cw = int((Inches(12.1) - gut * (cols - 1)) / cols)
        chh = Inches(1.65)
        for i, (name, cap) in enumerate(items):
            r, c = divmod(i, cols)
            x = x0 + c * (cw + gut)
            y = y0 + r * (chh + gut)
            self.rect(s, x, y, cw, chh, WHITE)
            self.rect(s, x + Inches(0.30), y + Inches(0.21), Inches(0.53), Inches(0.53), CLAY)
            self.txt(s, x + Inches(0.30), y + Inches(0.21), Inches(0.53), Inches(0.53),
                     [[(chips[i], 20 if len(chips[i]) == 1 else 16, WHITE, True, HEAD_FONT)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x + Inches(0.30), y + Inches(0.79), cw - Inches(0.5), Inches(0.38),
                     [[(name, 13, INK, True, HEAD_FONT)]])
            self.txt(s, x + Inches(0.30), y + Inches(1.16), cw - Inches(0.5), Inches(0.53),
                     [[(cap, 10.5, MUTED, False)]])
        if tip:
            self.txt(s, Inches(0.6), Inches(6.17), Inches(12.1), Inches(0.35),
                     [[("TIP  ", 13, CLAY, True), (tip, 13, MUTED, False)]])
        self.footer(s)
        return s

    def timeline(self, title, steps, kicker=None, foot=None):
        """Horizontal era timeline: label above, terracotta year chip, body below.
        steps: (label, year, body). Used by The Evolution of AI Engineering."""
        s = self.head(title, kicker)
        n = len(steps)
        x0 = Inches(0.80)
        step = Inches(3.10)
        self.rect(s, Inches(1.50), Inches(4.00), Inches(10.30), Inches(0.02), RULE)
        for i, (label, year, body) in enumerate(steps):
            x = x0 + step * i
            self.txt(s, x, Inches(2.35), Inches(3.00), Inches(0.70),
                     [[(label, 17, INK, True, HEAD_FONT)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            cx = x + Inches(1.05)
            self.oval(s, cx, Inches(3.55), Inches(0.90), Inches(0.90), CLAY)
            self.txt(s, cx, Inches(3.55), Inches(0.90), Inches(0.90),
                     [[(year, 15, WHITE, True)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x - Inches(0.05), Inches(4.65), Inches(3.10), Inches(1.30),
                     [[(body, 12, MUTED, False)]], align=PP_ALIGN.CENTER)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.45), Inches(12.1), Inches(0.40),
                     [[(foot, 13, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def outline(self, title, topics, kicker="ROADMAP"):
        """Three big numbered columns — the Course Outline slide."""
        s = self.head(title, kicker)
        cw = Inches(3.93)
        gut = Inches(0.20)
        for i, (name, bullets) in enumerate(topics):
            x = Inches(0.6) + (cw + gut) * i
            self.rect(s, x, Inches(1.90), cw, Inches(4.60), WHITE)
            self.rect(s, x + Inches(0.30), Inches(2.20), Inches(0.80), Inches(0.80), CLAY)
            self.txt(s, x + Inches(0.30), Inches(2.20), Inches(0.80), Inches(0.80),
                     [[(str(i + 1), 30, WHITE, True, HEAD_FONT)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x + Inches(0.30), Inches(3.15), cw - Inches(0.6), Inches(0.80),
                     [[(name, 17, INK, True, HEAD_FONT)]])
            self.txt(s, x + Inches(0.35), Inches(4.00), cw - Inches(0.65), Inches(2.30),
                     [[(f"•  {b}", 12, MUTED, False)] for b in bullets], space=8)
        self.footer(s)
        return s

    def tiles(self, title, items, kicker=None, intro=None, cols=2, numbered=True,
              foot=None):
        """Numbered white tiles: (heading, body) — the workhorse content slide.
        An optional `foot` line sits under the grid, which shortens it to make room."""
        s = self.head(title, kicker, intro)
        y0 = (Inches(2.35) + self.intro_extra(intro)) if intro else Inches(1.95)
        avail = (Inches(6.05) if foot else Inches(6.45)) - y0
        rows = (len(items) + cols - 1) // cols
        gut = Inches(0.18)
        cw = int((Inches(12.1) - gut * (cols - 1)) / cols)
        ch = int((avail - gut * (rows - 1)) / rows)
        # Size the type to the tile that was actually produced. With five or six
        # rows on a slide the tile is short enough that a two-line body at the
        # default size spills past the box, so step both sizes down rather than
        # letting the text escape its tile.
        _ch_in = ch / 914400.0
        if _ch_in >= 0.95:
            head_pt, body_pt = 14, 11.5
        elif _ch_in >= 0.80:
            head_pt, body_pt = 13, 10.5
        else:
            head_pt, body_pt = 12, 9.5
        for i, item in enumerate(items):
            headline, body = item if isinstance(item, (tuple, list)) else (item, "")
            r, c = divmod(i, cols)
            x = Inches(0.6) + c * (cw + gut)
            y = y0 + r * (ch + gut)
            self.rect(s, x, y, cw, ch, WHITE)
            self.rect(s, x, y, Inches(0.06), ch, CLAY)
            tx = x + Inches(0.30)
            tw = cw - Inches(0.55)
            if numbered:
                self.oval(s, tx, y + ch / 2 - Inches(0.19), Inches(0.38), Inches(0.38), CLAY)
                self.txt(s, tx, y + ch / 2 - Inches(0.19), Inches(0.38), Inches(0.38),
                         [[(str(i + 1), 12, WHITE, True)]],
                         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
                tx += Inches(0.56)
                tw -= Inches(0.56)
            para = [[(headline, head_pt, INK, True, HEAD_FONT)]]
            if body:
                para.append([(body, body_pt, MUTED, False)])
            self.txt(s, tx, y + Inches(0.12), tw, ch - Inches(0.24), para,
                     anchor=MSO_ANCHOR.MIDDLE, space=3)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.22), Inches(12.1), Inches(0.45),
                     [[(foot, 12.5, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def quote(self, title, text, kicker=None, foot=None):
        """A single definition set in large monospace between quote marks —
        for the one sentence that anchors a concept."""
        s = self.head(title, kicker)
        self.txt(s, Inches(0.75), Inches(2.55), Inches(0.9), Inches(0.9),
                 [[("“", 62, CLAY, True, HEAD_FONT)]])
        self.txt(s, Inches(1.65), Inches(2.85), Inches(10.4), Inches(2.0),
                 [[(text, 21, INK, False, "Courier New")]], anchor=MSO_ANCHOR.MIDDLE)
        self.txt(s, Inches(11.7), Inches(4.55), Inches(0.9), Inches(0.9),
                 [[("”", 62, CLAY, True, HEAD_FONT)]], align=PP_ALIGN.RIGHT)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.20), Inches(12.1), Inches(0.5),
                     [[(foot, 13, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def trainer(self, profile, kicker="INTRODUCTION", title="About the Trainer"):
        """Trainer profile: dark portrait panel with initials on the left, teal-
        badged fact rows on the right, optional terracotta social badges.

        An optional `badge` (a certification image in the skill's assets/
        folder, or an absolute path) sits in the portrait panel under the role,
        and the panel grows downward to hold it."""
        s = self.head(title, kicker)
        badge = profile.get("badge")
        if badge and not os.path.isabs(badge):
            badge = os.path.join(ASSETS, badge)
        if badge and not os.path.exists(badge):
            badge = None
        # left portrait panel — taller when it has to carry a badge
        px, py, pw = Inches(0.6), Inches(1.90), Inches(3.6)
        ph = Inches(3.95) if badge else Inches(3.6)
        self.rect(s, px, py, pw, ph, INK)
        bd = Inches(0.70)
        self.oval(s, px + (pw - bd) / 2, Inches(2.30), bd, bd, CLAY)
        name = profile["name"]
        # An explicit `initials` wins; otherwise derive from the name, dropping
        # titles. A bracketed placeholder name gets a neutral glyph, not letters.
        parts = [w for w in name.replace(".", "").split()
                 if w.lower() not in ("dr", "mr", "ms", "mrs", "prof")
                 and not w.startswith("[")]
        initials = profile.get("initials") or (
            "".join(w[0] for w in parts[:2]).upper() if parts else "—")
        self.txt(s, px + (pw - bd) / 2, Inches(2.30), bd, bd,
                 [[(initials, 24, WHITE, True, HEAD_FONT)]],
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        self.txt(s, px, Inches(3.20), pw, Inches(0.6),
                 [[(name, 21, WHITE, True, HEAD_FONT)]],
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        self.txt(s, px, Inches(3.80), pw, Inches(0.4),
                 [[(profile["role"], 13, DIM, False)]], align=PP_ALIGN.CENTER)
        if badge:
            # ~1.1 in square, centred in the panel under the role line; the
            # badge already carries its own wording, so its label goes in the
            # picture's alt text rather than repeating it as a caption.
            bs = Inches(1.1)
            pic = s.shapes.add_picture(badge, int(px + (pw - bs) / 2), Inches(4.38),
                                       width=bs, height=bs)
            pic._element.nvPicPr.cNvPr.set("descr", profile.get("badge_label", ""))

        # right fact rows, each with a teal badge
        rows = profile.get("rows", [])
        n = max(1, len(rows))
        step = Inches(0.92) if n <= 4 else Inches(0.74)
        for i, text in enumerate(rows):
            y = Inches(2.00) + step * i
            self.rect(s, Inches(4.60), y, Inches(0.55), Inches(0.55), TEAL)
            self.txt(s, Inches(4.60), y, Inches(0.55), Inches(0.55),
                     [[("✓", 16, WHITE, True)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, Inches(5.35), y - Inches(0.05), Inches(7.40), Inches(0.70),
                     [[(text, 14, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)

        # optional social links along the foot of the right column
        for i, link in enumerate(profile.get("links", [])[:2]):
            lx = Inches(4.60) + Inches(4.40) * i
            self.rect(s, lx, Inches(5.57), Inches(0.55), Inches(0.55), CLAY)
            self.txt(s, lx, Inches(5.57), Inches(0.55), Inches(0.55),
                     [[("●", 14, WHITE, True)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, lx + Inches(0.75), Inches(5.57), Inches(3.6), Inches(0.55),
                     [[(link, 13, MUTED, False)]], anchor=MSO_ANCHOR.MIDDLE)
        self.footer(s)
        return s

    def compare(self, title, items, kicker=None, foot=None, tab="Best for"):
        """Product columns: a terracotta badge, name, quoted role, a dashed
        connector, then a tabbed 'Best for' card of bullets."""
        s = self.head(title, kicker)
        n = len(items)
        gap = Inches(0.45)
        cw = int((Inches(12.1) - gap * (n - 1)) / n)
        # Badge letters must differ — "Claude (Chat + Cowork)" and "Claude Code"
        # both start "C" — so use the same unique-chip rule as the cards slide.
        badges = self._chips([nm for nm, _r, _b in items])
        for i, (name, role, bullets) in enumerate(items):
            x = Inches(0.6) + (cw + gap) * i
            # badge
            bd = Inches(0.78)
            self.oval(s, x + cw / 2 - bd / 2, Inches(1.95), bd, bd, CLAY)
            self.txt(s, x + cw / 2 - bd / 2, Inches(1.95), bd, bd,
                     [[(badges[i], 20, WHITE, True, HEAD_FONT)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x, Inches(2.88), cw, Inches(0.40),
                     [[(name, 19, INK, True, HEAD_FONT)]], align=PP_ALIGN.CENTER)
            self.txt(s, x, Inches(3.30), cw, Inches(0.34),
                     [[(f"“{role}”", 14, MUTED, False)]], align=PP_ALIGN.CENTER)
            # dashed connector
            for d in range(3):
                self.rect(s, x + cw / 2 - Inches(0.01), Inches(3.78) + Inches(0.14) * d,
                          Inches(0.02), Inches(0.07), MUTED)
            # card with its tab
            cy, ch = Inches(4.45), Inches(1.85)
            self.rect(s, x, cy, cw, ch, WHITE, line=INK)
            tw, th = Inches(1.65), Inches(0.42)
            tx = x + (cw - tw) / 2
            self.rect(s, tx, cy - th / 2, tw, th, INK)
            self.txt(s, tx, cy - th / 2, tw, th,
                     [[(tab, 12, WHITE, True, "Courier New")]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x + Inches(0.30), cy + Inches(0.34), cw - Inches(0.5), ch - Inches(0.5),
                     [[(f"•  {b}", 12.5, INK, False)] for b in bullets], space=7)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.55), Inches(12.1), Inches(0.5),
                     [[(foot, 12.5, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def pricing(self, title, intro, plans, band, tip, kicker=None):
        """Plan cards in a row, a dark API-rate band, and a TIP line — the
        pricing layout from the Agentic AI Applications with Claude Code deck."""
        s = self.head(title, kicker, intro)
        n = len(plans)
        gap = Inches(0.2)
        cw = int((Inches(12.1) - gap * (n - 1)) / n)
        cy, ch = Inches(2.40), Inches(2.75)
        for i, (name, detail) in enumerate(plans):
            x = Inches(0.6) + (cw + gap) * i
            self.rect(s, x, cy, cw, ch, WHITE)
            self.rect(s, x + Inches(0.30), cy + Inches(0.30), Inches(0.62), Inches(0.62), CLAY)
            self.txt(s, x + Inches(0.30), cy + Inches(0.30), Inches(0.62), Inches(0.62),
                     [[(name[0], 22, WHITE, True, HEAD_FONT)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x + Inches(0.30), cy + Inches(1.05), cw - Inches(0.55), Inches(0.5),
                     [[(name, 19, INK, True, HEAD_FONT)]])
            self.txt(s, x + Inches(0.30), cy + Inches(1.58), cw - Inches(0.55), Inches(1.07),
                     [[(detail, 12.5, MUTED, False)]])
        if band:
            by, bh = Inches(5.35), Inches(0.85)
            self.rect(s, Inches(0.6), by, Inches(12.1), bh, INK)
            self.txt(s, Inches(0.9), by, Inches(11.5), bh,
                     [[(band, 13, DIM, False)]], anchor=MSO_ANCHOR.MIDDLE)
        if tip:
            self.txt(s, Inches(0.6), Inches(6.35), Inches(12.1), Inches(0.35),
                     [[("TIP  ", 13, CLAY, True), (tip, 13, MUTED, False)]])
        self.footer(s)
        return s

    def container(self, title, outer_label, outer_sub, parts, kicker=None,
                  foot=None, cols=3):
        """One labelled outer box holding a grid of labelled inner boxes — for
        showing that a plugin CONTAINS skills, tools, agents and hooks. Each
        part is (label, body, colour key); labels sit on dark tabs."""
        tints = {"violet": RGBColor(0xE5, 0xE2, 0xF7), "amber": RGBColor(0xFA, 0xE6, 0xB0),
                 "green": RGBColor(0xD6, 0xEF, 0xDF), "blush": RGBColor(0xF5, 0xC8, 0xB8),
                 "sky": RGBColor(0xD6, 0xE6, 0xF7),
                 # terracotta tint — marks the one box in charge (the lead agent)
                 "clay": RGBColor(0xF7, 0xDA, 0xCF)}
        s = self.head(title, kicker)
        # outer container
        ox, oy = Inches(1.05), Inches(2.25)
        ow, oh = Inches(11.2), Inches(3.95)
        self.rect(s, ox, oy, ow, oh, WHITE, line=INK)
        # its tab, straddling the top edge
        tw, th = Inches(3.2), Inches(0.46)
        tx = ox + (ow - tw) / 2
        self.rect(s, tx, oy - th / 2, tw, th, INK)
        self.txt(s, tx, oy - th / 2, tw, th,
                 [[(outer_label, 15, WHITE, True, "Courier New")]],
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if outer_sub:
            self.txt(s, ox, oy + Inches(0.38), ow, Inches(0.34),
                     [[(outer_sub, 14, INK, False, "Courier New")]], align=PP_ALIGN.CENTER)

        # inner grid
        rows = -(-len(parts) // cols)
        gx, gy = Inches(0.30), Inches(0.52)
        iw = int((ow - Inches(1.0) - gx * (cols - 1)) / cols)
        ih = int((oh - Inches(1.25) - gy * (rows - 1)) / rows)
        x0 = ox + Inches(0.5)
        y0 = oy + Inches(0.95)
        for i, (label, body, key) in enumerate(parts):
            r, c = divmod(i, cols)
            x = x0 + c * (iw + gx)
            y = y0 + r * (ih + gy)
            self.rect(s, x, y, iw, ih, tints.get(key, tints["violet"]), line=INK)
            # dark tab on the box's top-left
            ltw = min(iw - Inches(0.4), Inches(0.28) + Inches(0.115) * len(label))
            self.rect(s, x + Inches(0.18), y - Inches(0.19), ltw, Inches(0.38), INK)
            self.txt(s, x + Inches(0.18), y - Inches(0.19), ltw, Inches(0.38),
                     [[(label, 12, WHITE, True, "Courier New")]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x + Inches(0.12), y + Inches(0.16), iw - Inches(0.24), ih - Inches(0.28),
                     [[(ln, 12, INK, False, "Courier New")] for ln in body.split("\n")],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, space=2)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.42), Inches(12.1), Inches(0.5),
                     [[(foot, 12.5, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def numbered_rows(self, title, items, kicker=None, intro=None, foot=None):
        """Full-width outlined rows, each with a boxed number, a monospace label
        and a description — for a short ordered list of named things."""
        s = self.head(title, kicker, intro)
        y = Inches(2.35) if intro else Inches(2.00)
        n = max(1, len(items))
        gap = Inches(0.14)
        avail = (Inches(6.15) if foot else Inches(6.55)) - y
        h = int((avail - gap * (n - 1)) / n)
        for i, (label, body) in enumerate(items):
            yy = y + (h + gap) * i
            self.rect(s, Inches(0.6), yy, Inches(12.1), h, WHITE, line=INK)
            # boxed number
            bx, bs = Inches(0.95), Inches(0.42)
            self.rect(s, bx, yy + (h - bs) / 2, bs, bs, WHITE, line=INK)
            self.txt(s, bx, yy + (h - bs) / 2, bs, bs,
                     [[(str(i + 1), 14, INK, False)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            # Label and description as one vertically-centred block, so the text
            # sits in the middle of the row rather than crowding its lower edge.
            self.txt(s, Inches(1.65), yy, Inches(10.6), h,
                     [[(label, 15, INK, True, "Courier New")],
                      [(body, 12.5, MUTED, False)]],
                     anchor=MSO_ANCHOR.MIDDLE, space=5)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.42), Inches(12.1), Inches(0.5),
                     [[(foot, 12, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def dark_list(self, title, items, kicker=None, foot=None):
        """Numbered heading + body rows on the dark ground — for the one slide in
        a section that carries a warning rather than a mechanism."""
        s = self.slide(ground=INK)
        if kicker:
            self.txt(s, Inches(0.7), Inches(0.42), Inches(11.0), Inches(0.3),
                     [[(kicker.upper(), 12, CLAY, True)]])
        self.txt(s, Inches(0.7), Inches(0.78), Inches(12.0), Inches(0.8),
                 [[(title, 30, WHITE, True, HEAD_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
        y = Inches(1.85)
        n = max(1, len(items))
        block = int((Inches(6.15) - y) / n)
        for i, (headline, body) in enumerate(items):
            self.txt(s, Inches(0.7), y, Inches(11.9), Inches(0.34),
                     [[(f"{i + 1}. ", 15, CLAY, True), (headline, 15, WHITE, True)]])
            self.txt(s, Inches(0.7), y + Inches(0.36), Inches(11.9), block - Inches(0.44),
                     [[(body, 13, DIM, False)]])
            y += block
        if foot:
            self.txt(s, Inches(0.7), Inches(6.30), Inches(11.9), Inches(0.5),
                     [[(foot, 12.5, CLAY, False)]])
        self.footer(s, dark=True)
        return s

    def table(self, title, head, rows, kicker=None, intro=None, foot=None,
              highlight_last=True, first=None):
        """A rule-separated table. Three columns is the numeric layout — for
        command output such as /context, where the numbers are the point. Any
        other width is a text comparison grid (see _text_table); `first` sets
        that grid's label-column share of the width (0-1), for a two-column
        mapping whose left cells are sentences rather than labels."""
        if len(head) != 3:
            return self._text_table(title, head, rows, kicker, intro, foot,
                                    highlight_last, first)
        s = self.head(title, kicker, intro)
        y = Inches(2.40) if intro else Inches(2.05)
        x0, w = Inches(0.9), Inches(11.5)
        cols = (Inches(0.9), Inches(7.6), Inches(10.2))
        widths = (Inches(6.5), Inches(2.4), Inches(2.2))
        # header
        for i, h in enumerate(head):
            self.txt(s, cols[i], y, widths[i], Inches(0.34),
                     [[(h, 12.5, MUTED, True)]],
                     align=PP_ALIGN.LEFT if i == 0 else PP_ALIGN.RIGHT)
        y += Inches(0.36)
        self.rect(s, x0, y, w, Inches(0.015), MUTED)
        y += Inches(0.12)
        rh = min(Inches(0.44), int((Inches(6.25) - y) / max(1, len(rows))))
        for r, row in enumerate(rows):
            last = highlight_last and r == len(rows) - 1
            for i, cell in enumerate(row):
                self.txt(s, cols[i], y, widths[i], rh,
                         [[(cell, 13, INK if not last else CLAY, last)]],
                         align=PP_ALIGN.LEFT if i == 0 else PP_ALIGN.RIGHT,
                         anchor=MSO_ANCHOR.MIDDLE)
            y += rh
            self.rect(s, x0, y, w, Inches(0.01), RULE)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.42), Inches(12.1), Inches(0.5),
                     [[(foot, 12, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def _text_table(self, title, head, rows, kicker, intro, foot, highlight_last, first_share=None):
        """Text comparison grid: a bold label column, then equal-width columns
        of short wrapped phrases, all left-aligned. Each row is as tall as its
        longest cell needs, and leftover height is shared out so a three-row
        table does not huddle at the top of the slide."""
        s = self.head(title, kicker, intro)
        y = Inches(2.40) if intro else Inches(2.05)
        x0, w = Inches(0.9), Inches(11.5)
        n = len(head)
        gut = Inches(0.25)
        first = Inches(2.3) if not first_share else int((w - gut * (n - 1)) * first_share)
        # Share the remaining width by each column's longest entry, with a
        # floor, so a column of one-word values does not take as much room as
        # a column of sentences.
        free = w - first - gut * (n - 1)
        longest = [max(len(str(r[i])) for r in list(rows) + [head]) for i in range(1, n)]
        share = [max(14, L) for L in longest]
        ws = [first] + [int(free * k / sum(share)) for k in share]
        xs = [x0]
        for i in range(1, n):
            xs.append(xs[-1] + ws[i - 1] + gut)
        # header
        for i, h in enumerate(head):
            self.txt(s, xs[i], y, ws[i], Inches(0.34),
                     [[(h, 13, CLAY if i else MUTED, True, HEAD_FONT if i else BODY_FONT)]])
        y += Inches(0.40)
        self.rect(s, x0, y, w, Inches(0.015), MUTED)
        y += Inches(0.10)
        # Estimate wrapped lines per cell (about 12 characters per inch of
        # 13pt Calibri) and size each row to its tallest cell.
        pad = Inches(0.22)
        avail = (Inches(6.15) if foot else Inches(6.55)) - y
        def _need(pt):
            def _lines(text, width):
                per = max(8, int(width / 914400.0 * 12.0 * 13.0 / pt))
                return max(1, -(-len(text) // per))
            line_h = int(Inches(0.235) * pt / 13.0)
            return [max(_lines(c, ws[i]) for i, c in enumerate(row)) * line_h + pad
                    for row in rows]
        size = 13
        need = _need(size)
        if sum(need) > avail:
            # Too tall: step the type down rather than run past the foot.
            size = 11.5
            need = _need(size)
        spare = max(0, avail - sum(need))
        extra = min(Inches(0.35), int(spare / max(1, len(rows))))
        for r, row in enumerate(rows):
            rh = int(need[r] + extra)
            last = highlight_last and r == len(rows) - 1
            for i, cell in enumerate(row):
                colour = CLAY if last else INK
                self.txt(s, xs[i], y, ws[i], rh,
                         [[(cell, size, colour, i == 0 or last)]],
                         anchor=MSO_ANCHOR.MIDDLE)
            y += rh
            self.rect(s, x0, y, w, Inches(0.01), RULE)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.42), Inches(12.1), Inches(0.5),
                     [[(foot, 12, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def meter(self, title, segments, kicker=None, intro=None, foot=None,
              scale_left="0", scale_right="1M", notes=None):
        """A horizontal capacity bar split into coloured segments with a legend —
        used for the context window. segments: (label, share, colour key)."""
        palette = {"ink": INK, "amber": AMBER, "blue": RGBColor(0x4A, 0x82, 0xC4),
                   "clay": CLAY, "green": RGBColor(0x4A, 0x7C, 0x3F),
                   "violet": RGBColor(0x7C, 0x6B, 0xE0), "sky": RGBColor(0xAE, 0xD2, 0xF0),
                   "blush": RGBColor(0xE8, 0xC2, 0xB4)}
        s = self.head(title, kicker, intro)
        x0, w = Inches(0.6), Inches(12.1)
        y, h = Inches(2.75), Inches(1.5)
        # scale marks
        self.txt(s, x0, y - Inches(0.38), Inches(2.0), Inches(0.3),
                 [[(scale_left, 12, MUTED, False)]])
        self.txt(s, x0 + w - Inches(2.0), y - Inches(0.38), Inches(2.0), Inches(0.3),
                 [[(scale_right, 12, MUTED, False)]], align=PP_ALIGN.RIGHT)
        self.rect(s, x0, y, w, h, WHITE, line=MUTED)
        cx = x0
        for label, share, key in segments:
            seg_w = int(w * share / 100.0)
            self.rect(s, cx, y, seg_w, h, palette.get(key, CLAY))
            cx += seg_w
        # Legend: two columns up to six entries, three beyond that, so a long
        # legend stays short enough to clear the footnote beneath it.
        ncols = 2 if len(segments) <= 6 else 3
        per_col = -(-len(segments) // ncols)
        col_w = Inches(11.9) / ncols
        ly = y + h + Inches(0.50)
        row_h = Inches(0.40)
        for i, (label, _share, key) in enumerate(segments):
            col, row = divmod(i, per_col)
            lx = x0 + Inches(0.1) + col * col_w
            yy = ly + row * row_h
            self.oval(s, lx, yy + Inches(0.05), Inches(0.20), Inches(0.20),
                      palette.get(key, CLAY))
            self.txt(s, lx + Inches(0.36), yy, col_w - Inches(0.5), Inches(0.30),
                     [[(label, 12, INK, False, "Courier New")]], anchor=MSO_ANCHOR.MIDDLE)
        if foot:
            fy = ly + row_h * per_col + Inches(0.18)
            self.txt(s, Inches(0.6), fy, Inches(12.1), Inches(0.5),
                     [[(foot, 12.5, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def layers(self, title, rows, kicker=None, intro=None,
               left_head="Layers", right_head="When Claude sees them"):
        """Stacked layer panels on the left, each with a dashed arrow to when it
        applies on the right. rows: (name, detail, when)."""
        s = self.head(title, kicker, intro)
        # Column headers sit below the intro line, never beside it.
        head_y = Inches(2.50) if intro else Inches(2.10)
        y0 = head_y + Inches(0.42)
        n = len(rows)
        gap = Inches(0.22)
        h = int((Inches(6.40) - y0 - gap * (n - 1)) / n)
        self.txt(s, Inches(0.6), head_y, Inches(6.6), Inches(0.35),
                 [[(left_head, 13, MUTED, True)]], align=PP_ALIGN.CENTER)
        self.txt(s, Inches(8.0), head_y, Inches(4.7), Inches(0.35),
                 [[(right_head, 13, MUTED, True)]], align=PP_ALIGN.CENTER)
        # Widest layer at the top, narrowing down — the shape of the diagram.
        for i, (name, detail, when) in enumerate(rows):
            y = y0 + (h + gap) * i
            w = Inches(6.6) - Inches(0.35) * (n - 1 - i)
            x = Inches(0.6) + Inches(0.35) * (n - 1 - i)
            self.rect(s, x, y, w, h, WHITE, line=CLAY)
            self.txt(s, x + Inches(0.3), y + Inches(0.16), w - Inches(0.6), Inches(0.36),
                     [[(name, 15, INK, True, HEAD_FONT)]])
            self.txt(s, x + Inches(0.3), y + Inches(0.56), w - Inches(0.6), h - Inches(0.7),
                     [[(detail, 11.5, MUTED, False)]])
            # dashed connector
            mid = y + h / 2
            for d in range(6):
                self.rect(s, Inches(7.05) + Inches(0.14) * d, mid - Inches(0.01),
                          Inches(0.07), Inches(0.02), RULE)
            self.txt(s, Inches(8.0), mid - Inches(0.16), Inches(4.7), Inches(0.34),
                     [[("✓  ", 12, TEAL, True), (when, 12.5, INK, False)]],
                     anchor=MSO_ANCHOR.MIDDLE)
        self.footer(s)
        return s

    def flow(self, title, steps, kicker=None, intro=None, foot=None):
        """Numbered chips joined by chevrons — process/agentic-loop slides."""
        s = self.head(title, kicker, intro)
        n = len(steps)
        gap = Inches(0.30)
        cw = int((Inches(12.1) - gap * (n - 1)) / n)
        y, ch = Inches(2.80), Inches(2.90)
        for i, step in enumerate(steps):
            headline, body = step if isinstance(step, (tuple, list)) else (step, "")
            x = Inches(0.6) + (cw + gap) * i
            self.rect(s, x, y, cw, ch, WHITE)
            self.rect(s, x, y, cw, Inches(0.08), CLAY)
            bd = Inches(0.70)
            self.oval(s, x + cw / 2 - bd / 2, y + Inches(0.40), bd, bd, CLAY)
            self.txt(s, x + cw / 2 - bd / 2, y + Inches(0.40), bd, bd,
                     [[(str(i + 1), 22, WHITE, True, HEAD_FONT)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x + Inches(0.15), y + Inches(1.28), cw - Inches(0.30), Inches(0.50),
                     [[(headline, 13, INK, True, HEAD_FONT)]], align=PP_ALIGN.CENTER)
            if body:
                self.txt(s, x + Inches(0.15), y + Inches(1.80), cw - Inches(0.30), Inches(0.95),
                         [[(body, 11, MUTED, False)]], align=PP_ALIGN.CENTER)
            if i < n - 1:
                self.txt(s, x + cw, y + ch / 2 - Inches(0.18), gap, Inches(0.36),
                         [[("▶", 13, CLAY, True)]],
                         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if foot:
            self.txt(s, Inches(0.6), Inches(6.20), Inches(12.1), Inches(0.40),
                     [[(foot, 13, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def split(self, title, left, right, kicker=None, intro=None):
        """Two labelled panels: (heading, [bullets]) each."""
        s = self.head(title, kicker, intro)
        y0 = Inches(2.35) if intro else Inches(1.95)
        h = Inches(6.45) - y0
        # Size the bullets to the taller of the two columns so a long list stays
        # inside its card instead of running past the footer and off the slide.
        rows = max(len(left[1]), len(right[1]), 1)
        body_h = h - Inches(1.15)
        avail_pt = (body_h / 914400.0) * 72.0
        size = max(9.0, min(12.5, round((avail_pt / rows / 1.75) * 2) / 2))
        gap = 9 if size >= 12 else (6 if size >= 10.5 else 3)
        for i, (headline, bullets) in enumerate((left, right)):
            x = Inches(0.6) + i * Inches(6.25)
            w = Inches(5.85)
            self.rect(s, x, y0, w, h, WHITE)
            self.rect(s, x, y0, w, Inches(0.08), CLAY if i == 0 else TEAL)
            self.txt(s, x + Inches(0.32), y0 + Inches(0.28), w - Inches(0.6), Inches(0.45),
                     [[(headline, 16, CLAY if i == 0 else TEAL, True, HEAD_FONT)]])
            self.txt(s, x + Inches(0.32), y0 + Inches(0.90), w - Inches(0.6), body_h,
                     [[(f"•  {b}", size, INK, False)] for b in bullets], space=gap)
        self.footer(s)
        return s

    # Prompt type limits. Below PROMPT_MIN_PT even in two columns, a prompt is
    # split across a "(cont.)" slide rather than shrunk further; above
    # PROMPT_MAX_PT a short prompt stops growing.
    PROMPT_MIN_PT = 10.0
    PROMPT_MAX_PT = 15.0
    # Measured in LibreOffice and PowerPoint: Calibri paragraph pitch is about
    # 1.2 x the point size plus the 2 pt space_after. Measured against the real
    # Calibri metrics, the widest-per-character prompt line runs 0.468 em per
    # character, so 0.47 em is a safe width estimate.
    _PITCH, _SPACE, _EM = 1.2, 2.0, 0.47

    def _prompt_fit(self, weight, avail_pt, width_pt, longest):
        """Largest point size at which `weight` lines fit `avail_pt` of height
        and the longest line fits `width_pt` without wrapping."""
        by_h = (avail_pt / max(weight, 1) - self._SPACE) / self._PITCH
        by_w = width_pt / (max(longest, 1) * self._EM)
        return min(by_h, by_w, self.PROMPT_MAX_PT)

    @staticmethod
    def _prompt_split(lines):
        """Index at which to break a prompt into two balanced columns. Only a
        blank line or the start of a new item (an unindented line) is a legal
        break, so a wrapped continuation never starts a column."""
        best, best_score = None, None
        for i in range(1, len(lines)):
            blank = not lines[i - 1].strip() or not lines[i].strip()
            if not blank and lines[i].startswith(" "):
                continue
            score = max(i, len(lines) - i) + (0 if blank else 0.75)
            if best_score is None or score < best_score:
                best, best_score = i, score
        return best

    def prompt(self, title, prompt_text, kicker=None, intro=None, note=None,
               label="PROMPT — copy into Claude"):
        """A ready-to-paste prompt in a bordered panel — learners copy this
        verbatim into Claude. Every lab has one.

        The type is solved to the largest size that fits. A long prompt flows
        into two balanced columns on the same slide rather than shrinking to an
        unreadable size; only if two columns would still be too small does it
        paginate onto a "(cont.)" slide."""
        lines = prompt_text.strip().split("\n")
        y0 = Inches(2.35) if intro else Inches(2.00)
        # Leave a clear band under the panel for the NOTE line so the two can
        # never collide, whatever the prompt length.
        h = (Inches(6.20) if note else Inches(6.60)) - y0
        body_h = h - Inches(0.75)
        avail_pt = body_h / 914400.0 * 72.0
        full_w, gap = Inches(11.4), Inches(0.45)
        col_w = int((full_w - gap) / 2)
        # Every paragraph — blank ones included — costs one pitch. Lines are
        # hard-wrapped in the source, so one source line is one drawn line.
        longest = max(len(ln) for ln in lines)
        one = self._prompt_fit(len(lines), avail_pt, full_w / 12700.0, longest)
        cut = self._prompt_split(lines) if len(lines) > 6 else None
        two = 0
        if cut:
            left, right = list(lines[:cut]), lines[cut:]
            while left and not left[-1].strip():
                left.pop()
            while right and not right[0].strip():
                right = right[1:]
            two = self._prompt_fit(max(len(left), len(right)), avail_pt,
                                   col_w / 12700.0, longest)
        if max(one, two) < self.PROMPT_MIN_PT and cut:
            # Even two columns are too small: paginate at the same clean break.
            self.prompt(title, "\n".join(lines[:cut]).rstrip(),
                        kicker=kicker, intro=intro, note="Continues on the next slide.",
                        label=label)
            return self.prompt(f"{title} (cont.)", "\n".join(lines[cut:]).lstrip("\n"),
                               kicker=kicker, note=note, label=label)
        # Two columns only when they buy a clearly larger size.
        cols = [lines] if one >= min(two, 12.0) or not cut else [left, right]
        size = max(8.0, int((one if len(cols) == 1 else two) * 2) / 2.0)

        s = self.head(title, kicker, intro)
        # A short prompt — a bare slash command, say — should not sit in a
        # four-inch empty box. Shrink the panel to the text plus the label band,
        # keeping the NOTE where it is so the slide foot stays consistent.
        tallest = max(len(c) for c in cols)
        _needed = Inches(0.95) + int(Inches(1) * tallest * (size * self._PITCH + self._SPACE) / 72.0)
        if _needed < h:
            h = int(_needed)
        self.rect(s, Inches(0.6), y0, Inches(12.1), h, WHITE, line=CLAY)
        self.rect(s, Inches(0.6), y0, Inches(0.07), h, CLAY)
        self.txt(s, Inches(0.95), y0 + Inches(0.18), Inches(11.5), Inches(0.30),
                 [[(label, 11, CLAY, True)]])
        body_h = h - Inches(0.75)
        if len(cols) == 1:
            self.txt(s, Inches(0.95), y0 + Inches(0.58), full_w, body_h,
                     [[(ln, size, INK, False)] for ln in lines], space=2)
        else:
            for i, col in enumerate(cols):
                x = Inches(0.95) + (col_w + gap) * i
                self.txt(s, x, y0 + Inches(0.58), col_w, body_h,
                         [[(ln, size, INK, False)] for ln in col], space=2)
            # hairline between the columns, so the reading order is obvious
            self.rect(s, Inches(0.95) + col_w + gap / 2, y0 + Inches(0.62),
                      Inches(0.01), body_h - Inches(0.10), RULE)
        if note:
            # The NOTE sits in a fixed band near the slide foot. When the panel
            # has shrunk to its text, that leaves a dead gap between the two,
            # so tuck the note under the panel instead.
            note_y = min(Inches(6.34), int(y0 + h + Inches(0.30)))
            self.txt(s, Inches(0.6), note_y, Inches(12.1), Inches(0.40),
                     [[("NOTE  ", 12, CLAY, True), (note, 12, MUTED, False)]])
        self.footer(s)
        return s

    def statement(self, headline, body, kicker=None, ground=INK):
        """Full-bleed statement slide for topic openers and the close."""
        dark = ground in (INK, DARK)
        s = self.slide(ground=ground)
        # Kept clear of the footer band (y=7.08in) so it never sits under the
        # footer text and kill its contrast.
        self.oval(s, Inches(11.3), Inches(4.05), Inches(2.9), Inches(2.9),
                  CLAY if dark else TEAL)
        if kicker:
            self.txt(s, Inches(1.0), Inches(2.20), Inches(11.0), Inches(0.45),
                     [[(kicker.upper(), 15, CLAY, True)]])
        self.txt(s, Inches(1.0), Inches(2.75), Inches(10.4), Inches(1.7),
                 [[(headline, 40, WHITE if dark else INK, True, HEAD_FONT)]],
                 anchor=MSO_ANCHOR.MIDDLE)
        if body:
            self.txt(s, Inches(1.02), Inches(4.60), Inches(10.2), Inches(1.0),
                     [[(body, 17, DIM if dark else MUTED, False)]])
        self.footer(s, dark=dark)
        return s

    def lab_cover(self, num, title, goal, build, tools, objective=None):
        """Lab opener: big terracotta lab number, goal, what you build, tools.

        An optional `objective` sits on the same row as the LAB chip, in space
        that is otherwise empty, so it adds nothing to the slide's height."""
        s = self.head(title, f"LAB {num:02d} · HANDS-ON")
        self.rect(s, Inches(0.6), Inches(1.95), Inches(1.5), Inches(0.5), CLAY)
        self.txt(s, Inches(0.6), Inches(2.0), Inches(1.5), Inches(0.4),
                 [[(f"LAB {num:02d}", 15, WHITE, True)]], align=PP_ALIGN.CENTER)
        if objective:
            objective = objective[0].upper() + objective[1:]
            # One line in 10.3 in: about 105 characters at 15pt, 113 at 14pt.
            pt = 15 if len(objective) <= 92 else 14
            self.txt(s, Inches(2.35), Inches(1.95), Inches(10.35), Inches(0.5),
                     [[("Objective:  ", pt, CLAY, True), (objective, pt, INK, True)]],
                     anchor=MSO_ANCHOR.MIDDLE)
        self.txt(s, Inches(0.6), Inches(2.70), Inches(12.1), Inches(1.5),
                 [[(goal, 19, INK, False)]])
        self.rect(s, Inches(0.6), Inches(4.35), Inches(12.1), Inches(1.95), WHITE)
        self.rect(s, Inches(0.6), Inches(4.35), Inches(0.07), Inches(1.95), CLAY)
        self.txt(s, Inches(0.95), Inches(4.58), Inches(11.4), Inches(0.35),
                 [[("YOU'LL BUILD", 12, CLAY, True)]])
        self.txt(s, Inches(0.95), Inches(4.95), Inches(11.4), Inches(0.60),
                 [[(build, 17, INK, True, HEAD_FONT)]])
        self.txt(s, Inches(0.95), Inches(5.70), Inches(11.4), Inches(0.40),
                 [[("Tools:  ", 12, MUTED, True), (tools, 12, MUTED, False)]])
        self.footer(s)
        return s

    def step(self, lab, title, n, total, text, detail=""):
        """One numbered lab step: big step chip, the instruction, and a teal
        'why' panel. A progress rail along the foot shows where the learner is
        in the lab, which also stops the lower half of the slide reading empty."""
        s = self.head(title, f"LAB {lab:02d} · STEP {n} OF {total}")
        self.oval(s, Inches(0.6), Inches(2.35), Inches(1.30), Inches(1.30), CLAY)
        self.txt(s, Inches(0.6), Inches(2.35), Inches(1.30), Inches(1.30),
                 [[(str(n), 34, WHITE, True, HEAD_FONT)]],
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        self.txt(s, Inches(2.25), Inches(2.20), Inches(10.4), Inches(1.60),
                 [[(text, 21, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
        if detail:
            self.rect(s, Inches(2.25), Inches(4.05), Inches(10.4), Inches(1.45), WHITE)
            self.rect(s, Inches(2.25), Inches(4.05), Inches(0.06), Inches(1.45), TEAL)
            self.txt(s, Inches(2.60), Inches(4.25), Inches(9.9), Inches(1.05),
                     [[("WHY THIS STEP", 10.5, TEAL, True)], [(detail, 13, MUTED, False)]],
                     anchor=MSO_ANCHOR.MIDDLE, space=5)
        # progress rail
        rail_w = Inches(12.1)
        seg = int((rail_w - Inches(0.08) * (total - 1)) / total)
        for i in range(total):
            x = Inches(0.6) + (seg + Inches(0.08)) * i
            self.rect(s, x, Inches(6.25), seg, Inches(0.10),
                      CLAY if i < n else RULE)
        self.txt(s, Inches(0.6), Inches(6.45), Inches(12.1), Inches(0.30),
                 [[(f"Step {n} of {total}", 10.5, MUTED, False)]], align=PP_ALIGN.RIGHT)
        self.footer(s)
        return s

    def steps_summary(self, lab, title, steps):
        """All of a lab's steps on ONE slide as a numbered list, in two columns
        once there are more than six. The full detail lives in the Learner Guide;
        this is the at-a-glance version the trainer talks to."""
        s = self.head(title, f"LAB {lab:02d} · STEPS",
                      intro="Full step-by-step, with the reasoning for each step, is in your Learner Guide.")
        n = max(1, len(steps))
        cols = 1 if n <= 6 else 2
        per = -(-n // cols)
        gut = Inches(0.35)
        cw = int((Inches(12.1) - gut * (cols - 1)) / cols)
        y0 = Inches(2.45)
        avail = Inches(6.45) - y0
        rh = min(Inches(0.62), int(avail / per))
        size = 13 if per <= 6 else (12 if per <= 8 else 11)
        for i, text in enumerate(steps):
            c, r = divmod(i, per)
            x = Inches(0.6) + c * (cw + gut)
            y = y0 + rh * r
            bd = Inches(0.30)
            self.oval(s, x, y + (rh - bd) / 2, bd, bd, CLAY)
            self.txt(s, x, y + (rh - bd) / 2, bd, bd,
                     [[(str(i + 1), 10.5, WHITE, True)]],
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.txt(s, x + Inches(0.46), y, cw - Inches(0.56), rh,
                     [[(text, size, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
        self.footer(s)
        return s

    def verify(self, lab, title, text, shot=None, caption=None):
        """Green 'check it' slide that closes every lab.

        With `shot`, the expected output is shown beside the checklist: the
        image is scaled to fit its column at its own aspect ratio (never
        stretched) and the text panel narrows to make room, so the two sit
        side by side instead of overlapping."""
        s = self.head(title, f"LAB {lab:02d} · VERIFY")
        # Same as steps_summary: the check text is Markdown for the lab files,
        # so strip the markers before it is drawn on a slide.
        text = re.sub(r"[`*]", "", text)

        img_w = img_h = img_x = img_y = None
        panel_w = Inches(12.1)
        if shot and os.path.exists(shot):
            from PIL import Image
            with Image.open(shot) as im:
                iw, ih = im.size
            # Give the shot the right-hand third; fit it inside that box.
            box_x, box_y = Inches(8.95), Inches(1.95)
            box_w, box_h = Inches(3.75), Inches(4.55)
            scale = min(box_w / iw, box_h / ih)
            img_w, img_h = int(iw * scale), int(ih * scale)
            img_x = int(box_x + (box_w - img_w) / 2)
            img_y = int(box_y + (box_h - img_h) / 2)
            panel_w = Inches(7.95)          # text stops clear of the image

        # Grow the panel to fit the text rather than fixing its height: a long
        # check step beside a screenshot used to run out of the bottom of the
        # box. Estimate the wrapped line count from the usable width.
        body_pt = 15 if img_w else 16
        text_w_in = (panel_w - Inches(0.8)) / 914400.0
        chars_per_line = max(20, int(text_w_in * 96 / body_pt))
        n_lines = max(1, -(-len(text) // chars_per_line))
        panel_h = Inches(1.15) + Inches(0.030 * body_pt) * n_lines
        panel_h = int(max(Inches(2.70), min(panel_h, Inches(4.15))))

        self.rect(s, Inches(0.6), Inches(2.30), panel_w, panel_h, WHITE)
        self.rect(s, Inches(0.6), Inches(2.30), Inches(0.07), panel_h, GREEN)
        self.txt(s, Inches(1.0), Inches(2.62), panel_w - Inches(0.7), Inches(0.5),
                 [[("✓  Check your work", 20, GREEN, True, HEAD_FONT)]])
        self.txt(s, Inches(1.0), Inches(3.30), panel_w - Inches(0.8),
                 panel_h - Inches(1.10),
                 [[(text, body_pt, INK, False)]])

        if img_w:
            # Hairline frame, then the picture — a screenshot reads as an
            # artefact rather than as floating page furniture.
            self.rect(s, img_x - Inches(0.05), img_y - Inches(0.05),
                      img_w + Inches(0.10), img_h + Inches(0.10), RULE)
            s.shapes.add_picture(shot, img_x, img_y, width=img_w, height=img_h)
            self.txt(s, Inches(8.95), img_y + img_h + Inches(0.12), Inches(3.75), Inches(0.3),
                     [[(caption or "Expected output", 10.5, MUTED, False)]],
                     align=PP_ALIGN.CENTER)
        self.footer(s)
        return s

    def screenshot(self, title, image, caption=None, kicker=None):
        """A real screenshot of the app, fitted inside the content area at its
        own aspect ratio (never stretched or cropped), on a white mat with a
        hairline frame and a terracotta top rule, and one caption line beneath.

        The caller decides whether to emit it (only when the file exists); this
        component assumes the image is there."""
        from PIL import Image
        s = self.head(title, kicker)
        with Image.open(image) as im:
            iw, ih = im.size
        # The box the framed picture must fit in: below the title, above the
        # caption band. The mat adds a fixed margin around the picture.
        mat = Inches(0.14)
        box_x, box_y = Inches(0.6), Inches(1.85)
        box_w, box_h = Inches(12.1), Inches(4.45)
        scale = min((box_w - 2 * mat) / iw, (box_h - 2 * mat) / ih)
        img_w, img_h = int(iw * scale), int(ih * scale)
        fw, fh = img_w + 2 * mat, img_h + 2 * mat
        fx = int(box_x + (box_w - fw) / 2)
        fy = int(box_y + (box_h - fh) / 2)
        self.rect(s, fx, fy, fw, fh, WHITE, line=RULE)
        self.rect(s, fx, fy, fw, Inches(0.06), CLAY)
        s.shapes.add_picture(image, int(fx + mat), int(fy + mat), width=img_w, height=img_h)
        if caption:
            self.txt(s, Inches(0.6), Inches(6.45), Inches(12.1), Inches(0.4),
                     [[(caption, 13, MUTED, False)]], align=PP_ALIGN.CENTER)
        self.footer(s)
        return s
