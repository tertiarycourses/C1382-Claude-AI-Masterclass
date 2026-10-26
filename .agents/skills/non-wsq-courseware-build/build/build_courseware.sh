#!/usr/bin/env bash
# One-command aligned build of the whole course from the single source
# (course_data.py + edition_classic.py + data_domain1..3.py), in BOTH editions:
#
#   classic  Classic Projects Edition  -> courseware/, labs/, docs/prompts/
#   threads  Threads Edition           -> courseware/threads-edition/, labs-threads/,
#                                         docs/prompts/threads/
#
# For each edition: mock data and assets, the labs index, lab prompt PDFs, the
# copy-ready prompts page, the slide deck, Lesson Plan and Learner Guide, each
# rendered to PDF with a page-numbered TOC. Then, once: README.md and the
# docs/ landing page, both of which present the two editions.
#
# Build one edition only with:  EDITIONS=threads bash build_courseware.sh
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SOFFICE="${SOFFICE:-soffice}"
EDITIONS="${EDITIONS:-classic threads}"

# Paths for one edition, read from course_data: repo, short title, version and
# the edition's courseware folder.
edition_paths() {
  COURSE_EDITION="$1" python3 - "$HERE" <<'PY'
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
print("\t".join([find_repo(here), C.SHORT_TITLE, C.VERSION, C.COURSEWARE_SUBDIR, C.EDITION_LABEL]))
PY
}

mtime() { stat -f %m "$1" 2>/dev/null || stat -c %Y "$1" 2>/dev/null || echo 0; }

# DOCX/PPTX -> PDF in its own folder. LibreOffice sometimes leaves the old PDF
# in place on the first conversion, so check the PDF is newer than its source
# and retry once before failing the build.
render_pdf() {
  local src="$1" out pdf
  out="$(dirname "$src")"
  pdf="${src%.*}.pdf"
  "$SOFFICE" --headless --convert-to pdf --outdir "$out" "$src" >/dev/null 2>&1 || true
  if [ ! -f "$pdf" ] || [ "$(mtime "$pdf")" -lt "$(mtime "$src")" ]; then
    echo "    retrying: $(basename "$pdf") was not refreshed"
    sleep 2
    "$SOFFICE" --headless --convert-to pdf --outdir "$out" "$src" >/dev/null 2>&1 || true
  fi
  if [ ! -f "$pdf" ] || [ "$(mtime "$pdf")" -lt "$(mtime "$src")" ]; then
    echo "ERROR: $pdf is missing or older than $(basename "$src")" >&2
    exit 1
  fi
}

for ED in $EDITIONS; do
  export COURSE_EDITION="$ED"
  IFS=$'\t' read -r REPO SHORT VERSION CW_SUB LABEL <<< "$(edition_paths "$ED")"
  CW="$REPO/$CW_SUB"
  mkdir -p "$CW"
  echo ""
  echo "################ $LABEL  (COURSE_EDITION=$ED -> $CW_SUB/) ################"

  echo "==> Mock data and assets (asserts the figures the courseware quotes)"
  python3 "$HERE/build_mockdata.py"

  echo "==> Labs index and prompt PDFs"
  python3 "$HERE/build_labs.py"
  python3 "$HERE/build_lab_pdfs.py"

  echo "==> Prompts page"
  python3 "$HERE/build_prompts_page.py"

  echo "==> Slides / Lesson Plan / Learner Guide"
  python3 "$HERE/build_slides.py"
  python3 "$HERE/build_lesson_plan.py"
  python3 "$HERE/build_learner_guide.py"

  # This edition's files only: the deck is named after the edition's short
  # title and version, so a glob over the folder can never pick the other
  # edition's deck or an older version.
  PPT="$CW/$SHORT-$VERSION.pptx"
  LP="$CW/LP-$SHORT.docx"
  LG="$CW/LG-$SHORT.docx"
  for f in "$PPT" "$LP" "$LG"; do
    [ -f "$f" ] || { echo "ERROR: expected $f" >&2; exit 1; }
  done

  echo "==> Render PDFs (pass 1)"
  for f in "$PPT" "$LP" "$LG"; do render_pdf "$f"; done

  echo "==> Inject page-numbered Tables of Contents"
  python3 "$HERE/inject_toc.py" "$LP" "${LP%.docx}.pdf" 2
  python3 "$HERE/inject_toc.py" "$LG" "${LG%.docx}.pdf" 2

  echo "==> Render PDFs (pass 2 — with built TOC)"
  for f in "$LP" "$LG"; do render_pdf "$f"; done

  echo "==> $LABEL artifacts in $CW_SUB/:"
  ls -1 "$PPT" "${PPT%.pptx}.pdf" "$LP" "${LP%.docx}.pdf" "$LG" "${LG%.docx}.pdf"
done

echo ""
echo "==> README and docs/ landing page (both editions, written once)"
COURSE_EDITION=classic python3 "$HERE/build_readme.py"
COURSE_EDITION=classic python3 "$HERE/build_prompts_page.py" --landing

echo "==> Done."
