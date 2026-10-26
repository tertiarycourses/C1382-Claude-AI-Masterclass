#!/usr/bin/env bash
# One-command aligned build of the whole course from the single source
# (course_data.py + data_domain1..3.py): mock data and assets, lab prompt PDFs,
# the copy-ready prompts page, the README, the slide deck, Lesson Plan and
# Learner Guide, each rendered to PDF with a page-numbered TOC.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SOFFICE="${SOFFICE:-soffice}"

IFS=$'\t' read -r REPO SHORT <<< "$(python3 - "$HERE" <<'PY'
import os, sys
here = sys.argv[1]; sys.path.insert(0, here)
import course_data as C
def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))
print(find_repo(here) + "\t" + C.SHORT_TITLE)
PY
)"
CW="$REPO/courseware"

echo "==> Mock data and assets (asserts the figures the courseware quotes)"
python3 "$HERE/build_mockdata.py"

echo "==> Labs index and prompt PDFs"
python3 "$HERE/build_labs.py"
python3 "$HERE/build_lab_pdfs.py"

echo "==> Prompts page (docs/) and README"
python3 "$HERE/build_prompts_page.py"
python3 "$HERE/build_readme.py"

echo "==> Slides / Lesson Plan / Learner Guide"
python3 "$HERE/build_slides.py"
python3 "$HERE/build_lesson_plan.py"
python3 "$HERE/build_learner_guide.py"

PPT="$(ls -t "$CW"/*.pptx | head -1)"
LP="$CW/LP-$SHORT.docx"
LG="$CW/LG-$SHORT.docx"

echo "==> Render PDFs (pass 1)"
for f in "$PPT" "$LP" "$LG"; do
  "$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$f" >/dev/null 2>&1
done

echo "==> Inject page-numbered Tables of Contents"
python3 "$HERE/inject_toc.py" "$LP" "${LP%.docx}.pdf" 2
python3 "$HERE/inject_toc.py" "$LG" "${LG%.docx}.pdf" 2

echo "==> Render PDFs (pass 2 — with built TOC)"
for f in "$LP" "$LG"; do
  "$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$f" >/dev/null 2>&1
done

echo "==> Done. Artifacts in courseware/:"
ls -1 "$CW"/*.pptx "$CW"/*.docx "$CW"/*.pdf
