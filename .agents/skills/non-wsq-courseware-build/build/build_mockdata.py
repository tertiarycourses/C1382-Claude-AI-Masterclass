#!/usr/bin/env python3
"""Generate the Lumo Kopi Co. mock data and image assets used across the labs.

One synthetic dataset for one fictitious brand, written deterministically (fixed
seed) so every learner's research brief, dashboard and calendar shows the same
figures and the lab check steps can state exact numbers.

For every lab in data_domain1..3, each entry in the lab's `data` list is written
to labs/lab-NN-<slug>/data/<entry>. A file used by several labs (the survey and
competitor CSVs in Labs 2 and 3) is written to each. A `data` entry with no
generator below fails the build, so the lab text can never name a missing file.

The data is generated FROM course_data.FACTS and then re-measured and asserted,
so the courseware and the files can never drift. Guaranteed figures:

    Survey (lumo-consumer-survey-2026.csv)
        400 respondents: 240 Singapore, 160 Kuala Lumpur
        age bands 18-24 88 · 25-34 152 · 35-44 96 · 45+ 64
        248 likely to buy (intent 4-5) = 62%; 112 of 152 aged 25-34 = 74%
        228 willing to pay S$3.50 or more = 57%
        channels  Instagram 136 (34%) · TikTok 104 (26%) · Friends & family 72
                  · Shopee / Lazada 48 · Other 40
        drivers   Taste 124 (31%) · Less sugar 108 · Price 72 · Convenience 60
                  · Sustainability 36
    Competitors (lumo-competitors.csv)
        six fictional brands, S$3.20 to S$5.60, median S$4.30 (Lumo S$3.90 below)
    Social trends (lumo-social-trends.csv)
        twelve themes; top by engagement "Taste tests and first-sip reactions"
    Budget: Drive sheet and launch brief both total S$60,000 and disagree on
        exactly two lines — Instagram S$18,000 vs S$20,000 and
        Influencers S$12,000 vs S$10,000
    Lab 6 captions: five, each breaking at least one brand rule (checked by the
        same rule checker that passes the guidelines' "Do" examples)
    Lab 8 template: header only — date,platform,format,hook,copy,hashtags,
        visual_idea,call_to_action; ten weekdays 1-14 December 2026
    Lab 9 assets: five PNGs drawn with Pillow (no external images)

Besides asserting the data against FACTS, the script asserts the lab text in
data_domainN quotes the same figures, so an edit on either side fails loudly.
"""
import csv, math, os, random, re, sys
from datetime import date, datetime, timedelta
from statistics import median

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3

F = C.FACTS
LABS = {lab["num"]: lab for lab in DOMAIN1 + DOMAIN2 + DOMAIN3}
SEED = 20261201          # launch day; fixed so every build writes identical data


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


def lab_data_dir(num):
    """labs/lab-NN-<slug>/data, resolved from the single source so a lab
    renumbering never leaves data written to a folder nothing reads."""
    return os.path.join(REPO, "labs", f"lab-{num:02d}-{C.LAB_SLUGS[num]}", "data")


# ------------------------------------------------------------------ helpers
def money(s):
    """'S$3.90' -> 3.9 ;  'S$60,000' -> 60000.0"""
    return float(s.replace("S$", "").replace(",", ""))


def sgd(x):
    """Price format the brand guidelines mandate: S$3.90 (always two decimals)."""
    return f"S${x:,.2f}"


def sgd0(x):
    """Budget format: S$18,000."""
    return f"S${x:,.0f}"


def pct(n, d):
    return round(100 * n / d)


def parse_day(s):
    return datetime.strptime(s, "%d %B %Y").date()


def long_day(d):
    return f"{d.day} {d:%B %Y}"


def write_bytes(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    print("  wrote", os.path.relpath(path, REPO))


def csv_text(header, rows):
    import io
    buf = io.StringIO()
    # csv defaults to \r\n, which git reports as trailing whitespace.
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()


PRICE_CAN = money(F["price_can"])          # 3.90
PRICE_PACK = money(F["price_pack"])        # 42.00
LAUNCH_SG = parse_day(F["launch_sg"])
LAUNCH_KL = parse_day(F["launch_kl"])
COLOURS = dict(C.BRAND_COLOURS)
BROWN, OAT, TEAL, ORANGE = (COLOURS[k] for k in
                            ("Kopi Brown", "Oat Cream", "Lumo Teal", "Sunrise Orange"))
TAGS = " ".join(F["hashtags"])             # "#LumoKopi #KopiChilledRight"

assert sgd(PRICE_CAN) == F["price_can"] and sgd(PRICE_PACK) == F["price_pack"]


# ================================================================== brand rules
# One checker for every brand rule a caption can break. The guidelines' "Do"
# examples must pass it; the Lab 6 sample captions must each fail it.
SINGLISH = ["lah", "leh", "lor", "sia", "meh", "shiok", "lepak", "wah", "lau",
            "alamak", "kiasu", "paiseh", "jialat", "chope", "makan", "dabao",
            "tapau", "steady", "pom pi pi", "confirm plus chop", "sibei"]
BANNED = ["healthy", "healthier", "healthiest", "good for your", "guilt-free",
          "burns fat", "lose weight", "boost", "immunity", "detox", "cure",
          "best", "no. 1", "number one", "#1"]
CTA_VERBS = ["grab", "order", "shop", "buy", "try", "pick up", "find", "stock",
             "follow", "tag", "share", "comment", "click", "get yours", "swipe"]


def brand_violations(text):
    """Return the brand rules a caption breaks, as {rule: detail}."""
    low = text.lower()
    out = {}
    bad_prices = [m.group(0) for m in re.finditer(r"(S\$|SGD\s?|RM|\$)\s?\d+(?:\.\d+)?", text)
                  if not re.fullmatch(r"S\$\d+\.\d{2}", m.group(0))]
    bad_prices += re.findall(r"\b\d+\s*dollars\b", low)
    if bad_prices:
        out["price format"] = bad_prices
    claims = [b for b in BANNED if re.search(r"(?<![\w#])" + re.escape(b) + r"(?!\w)", low)]
    if claims:
        out["unprovable claim"] = claims
    slang = [w for w in SINGLISH if re.search(r"\b" + re.escape(w) + r"\b", low)]
    if len(slang) > 1:
        out["too much Singlish"] = slang
    tags = re.findall(r"#\w+", text)
    if "#LumoKopi" not in tags:
        out["#LumoKopi missing"] = tags
    if len(tags) > 5:
        out["too many hashtags"] = len(tags)
    ctas = [v for v in CTA_VERBS if re.search(r"\b" + re.escape(v) + r"\b", low)]
    if len(ctas) != 1:
        out["not one clear call to action"] = ctas
    return out


DO_EXAMPLES = [
    (f"First sip of the day, sorted. Lumo Cold Kopi is oat-milk kopi cold brew with "
     f"5 g sugar, {F['price_can']} a can. Grab yours at the Lumo online store. {TAGS}"),
    (f"Weekend lepak, fridge ready. Twelve cans of Lumo Cold Kopi for {F['price_pack']}, "
     f"on Shopee and Lazada from {LAUNCH_SG.day} December. Stock up today. {TAGS} #ColdBrew"),
    (f"Kopi the way you like it, just colder. Find Lumo Cold Kopi at selected cafés "
     f"from {F['launch_sg']}. {TAGS}"),
]
DONT_EXAMPLES = [
    "The healthiest kopi in Singapore!!! Only $3.9 lah, confirm shiok! #kopi #coffee",
    "Best cold brew ever. 12 for 42 dollars. #KopiChilledRight",
]


# ================================================================== Lab 1 brand kit
def colour_table():
    rows = ["| Colour | Hex | Use it for |", "|---|---|---|"]
    use = {"Kopi Brown": "Wordmark, headlines, body text on light backgrounds",
           "Oat Cream": "Backgrounds, can label, generous white space",
           "Lumo Teal": "Accents, links, buttons, the 'COLD KOPI' line",
           "Sunrise Orange": "The sun mark, highlights, one call-to-action per layout"}
    for name, hx in C.BRAND_COLOURS:
        rows.append(f"| {name} | `{hx}` | {use[name]} |")
    return "\n".join(rows)


def gen_brand_guidelines():
    do = "\n".join(f"> {t}\n" for t in DO_EXAMPLES)
    dont = "\n".join(f"> {t}\n" for t in DONT_EXAMPLES)
    return f"""# Lumo Kopi Co. — Brand Guidelines

*Version 1.2 · October 2026 · Owner: Lumo marketing team · Fictitious brand, for training only*

## 1. Our story

Lumo started with a simple morning ritual: a cup of kopi at the hawker centre
before the day begins. We loved the taste, but not the sugar rush, and we wanted
something we could take with us. So we cold-brewed our kopi, paired it with oat
milk and kept the sugar down to {F['sugar_g']} g a can. **{F['product']}** is that
morning kopi, chilled and ready wherever you are.

*Lumo* comes from "lumen" — light. We are the bright start to a long day.

Campaign line: **{F['campaign']}**

## 2. Voice

| We are | Which means | We are never |
|---|---|---|
| **Warm** | We talk like a friend at the next table, not a billboard. | Cold or corporate |
| **Local** | We know kopi culture and Singapore life, and it shows. | A caricature of it |
| **Playful** | A light touch, a little wit, short sentences. | Silly or try-hard |
| **Confident** | We say what the product is, plainly. | Preachy, boastful or pushy |

We never lecture people about what they should drink. We invite them to try.

## 3. Brand colours

{colour_table()}

Keep at least half of any layout in Oat Cream or white. Use Sunrise Orange
sparingly — it is our highlight, not our background.

## 4. Typography

- **Headlines:** a rounded geometric sans in a heavy weight (for example
  Avenir Next Heavy or Nunito ExtraBold), Kopi Brown.
- **Body:** the same family in Regular or Medium, 1.4 line spacing.
- **Wordmark:** always lowercase **lumo**; never redraw or recolour it outside
  the four brand colours.
- Video captions: heavy weight, high contrast, no more than six words a card.

## 5. Hard rules for all customer-facing content

These are checkable rules. Every post, caption, email, script and ad must pass
all of them.

1. **Prices in Singapore dollars, two decimals.** Write `{F['price_can']}` per can
   and `{F['price_pack']}` per 12-pack. Never `$3.9`, `SGD4`, `3.90 dollars` or `RM` for
   Singapore content.
2. **No unprovable claims.** Never call the product "healthy", "healthier" or
   "guilt-free"; make no medical, weight-loss, energy or immunity claims; never
   say "best in Singapore", "No. 1" or any other superlative we cannot prove.
   **"{F['sugar_g']} g sugar" is allowed** — it is a fact on the can.
3. **At most ONE Singlish word per post** (for example *shiok* or *lepak*). One
   word adds warmth; more turns into a caricature.
4. **`#LumoKopi` is always present.** Add `#KopiChilledRight` during the launch.
5. **No more than five hashtags** in total.
6. **End with one clear call to action** — one, not three.
7. **Paid partnerships must be labelled.** Creator posts we pay for or gift
   product to carry the platform's paid-partnership label or `#ad` in the first line.
8. **Use only approved assets.** Never use a real person's likeness without a
   signed release, or another brand's logo.

## 6. Do and don't

**Do**

{do}
**Don't**

{dont}
Why the don'ts fail: a health claim, a superlative, a price without `S$` and two
decimals, two Singlish words, `#LumoKopi` missing, and no clear call to action.

## 7. Platform notes

| Platform | Format | Hashtags | Notes |
|---|---|---|---|
| Instagram | Carousel or Reel | 3-5 | Hook in the first line of the caption |
| TikTok | 15-second video | 3-5 | Hook in the first 2 seconds, on-screen text |
| LinkedIn | Text + image | Up to 3 | Founder's voice, the story behind the product |
| Facebook | Image or short video | Up to 3 | Community, offers, the 12-pack |
"""


def gen_product_sheet():
    per_can_in_pack = PRICE_PACK / 12
    return f"""# {F['product']} — Product Sheet

*Lumo Kopi Co. · October 2026 · Fictitious product, for training only*

## At a glance

| Item | Detail |
|---|---|
| Product name | {F['product']} |
| What it is | Ready-to-drink oat-milk kopi cold brew |
| Format | {F['can_ml']} ml can, recyclable aluminium |
| Milk | Oat milk (dairy-free) |
| Sugar | {F['sugar_g']} g sugar per can |
| Price — single can | {F['price_can']} |
| Price — 12-pack | {F['price_pack']} (works out at {sgd(per_can_in_pack)} a can) |
| Launch — Singapore | {F['launch_sg']} |
| Launch — Kuala Lumpur | {F['launch_kl']} (Malaysian pricing to be confirmed) |
| Campaign | {F['campaign']} |
| Hashtags | {", ".join(F['hashtags'])} |

## Ingredients

Cold-brewed kopi (water, roasted coffee), oat drink (water, oats, rapeseed oil,
calcium carbonate, salt), cane sugar, natural flavour.

Contains oats. Contains caffeine — not recommended for children or anyone
sensitive to caffeine. Serve chilled; once opened, drink within 24 hours.

## Taste

Smooth, roasty kopi with a gentle caramel note and a creamy oat finish. Less
sweet than a traditional kopi peng.

## Where to buy

- Lumo online store (lumokopi.example) — single cans and 12-packs
- Shopee — official Lumo Kopi store
- Lazada — official Lumo Kopi store
- Selected cafés in Singapore (list published on launch day)

## What we can say

- "Oat-milk kopi cold brew", "{F['sugar_g']} g sugar per can", "{F['can_ml']} ml can",
  "dairy-free oat milk", "{F['price_can']} a can", "{F['price_pack']} for a 12-pack".

## What we must not say

- "Healthy", "healthier", "guilt-free", or any medical, weight-loss, energy or
  immunity claim.
- "Best", "No. 1" or any comparison with another brand we cannot prove.
"""


def gen_launch_brief():
    rows = "\n".join(f"| {line} | {sgd0(amt)} | {pct(amt, money(F['budget_total']))}% |"
                     for line, amt in F["budget_brief"])
    total = sum(a for _, a in F["budget_brief"])
    return f"""# {F['product']} — Launch Brief

*Lumo Kopi Co. marketing · Approved 9 October 2026 · Fictitious, for training only*

## Objective

Launch {F['product']} in Singapore on **{F['launch_sg']}** so that 25-34
year-olds on Instagram and TikTok know the product exists by launch day, and
follow with Kuala Lumpur on **{F['launch_kl']}** — within a total budget of
**{F['budget_total']}**.

## Audience

- **Primary:** 25-34 year-olds in Singapore — office workers and young
  professionals who buy kopi most days and want something less sweet they can
  take with them.
- **Secondary:** 25-34 year-olds in Kuala Lumpur, from January 2027.

## Key message

**{F['campaign']}.** Your morning kopi, cold-brewed with oat milk and just
{F['sugar_g']} g sugar, ready wherever your day goes.

## Proof points

- Oat-milk kopi cold brew in a {F['can_ml']} ml can
- {F['sugar_g']} g sugar per can
- {F['price_can']} a can, {F['price_pack']} for a 12-pack

## Channels

Instagram and TikTok lead; creator partnerships amplify; Google Search and
Shopee / Lazada ads catch people ready to buy.

## Budget

| Line | Amount | Share |
|---|---|---|
{rows}
| **Total** | **{sgd0(total)}** | **100%** |

## Timeline

| Date | Milestone |
|---|---|
| 6 November 2026 | Launch deck and campaign brief approved |
| 20 November 2026 | Creator content approved (paid partnerships labelled) |
| 24 November 2026 | Launch video final |
| {F['launch_sg']} | Singapore launch — Instagram and TikTok posts go live |
| 14 December 2026 | Launch fortnight review |
| {F['launch_kl']} | Kuala Lumpur launch |

## KPIs (Singapore, launch fortnight)

- Reach: 1.5 million across Instagram and TikTok
- Engagement rate: 4% or higher on launch posts
- Followers: +5,000 on @lumokopi Instagram
- Sales: 8,000 cans (single and 12-pack combined) by 31 December 2026

## Mandatories

- Follow lumo-brand-guidelines.md for every customer-facing word.
- Never call the product healthy. "{F['sugar_g']} g sugar" is allowed.
- No email is sent and no post is published without approval.
"""


# ================================================================== survey
AGE_ORDER = [a for a, _ in F["age_bands"]]
# Respondents per (city, age band). Each city sums to its FACTS total and each
# band to its FACTS total — asserted below.
CITY_AGE = {
    ("Singapore", "18-24"): 52, ("Singapore", "25-34"): 96,
    ("Singapore", "35-44"): 56, ("Singapore", "45+"): 36,
    ("Kuala Lumpur", "18-24"): 36, ("Kuala Lumpur", "25-34"): 56,
    ("Kuala Lumpur", "35-44"): 40, ("Kuala Lumpur", "45+"): 28,
}
# Likely to buy (intent 4 or 5) per band: 25-34 comes from FACTS; the other three
# share the rest of FACTS["likely_to_buy"].
LIKELY_BY_AGE = {"18-24": 60, "25-34": F["likely_25_34"], "35-44": 50,
                 "45+": F["likely_to_buy"] - F["likely_25_34"] - 60 - 50}

# Relative preferences by age band, so the data has believable correlations
# (younger -> TikTok, older -> friends & family and less sugar). The exact
# totals come from FACTS via quota sampling, never from these weights.
CHANNEL_W = {
    "18-24": {"Instagram": 3.0, "TikTok": 5.5, "Friends & family": 1.2, "Shopee / Lazada": 1.0, "Other": 0.5},
    "25-34": {"Instagram": 4.5, "TikTok": 3.0, "Friends & family": 1.3, "Shopee / Lazada": 1.3, "Other": 0.7},
    "35-44": {"Instagram": 3.0, "TikTok": 1.3, "Friends & family": 2.2, "Shopee / Lazada": 1.6, "Other": 1.4},
    "45+":   {"Instagram": 1.5, "TikTok": 0.6, "Friends & family": 3.5, "Shopee / Lazada": 1.0, "Other": 2.6},
}
DRIVER_W = {
    "18-24": {"Taste": 3.0, "Less sugar": 1.4, "Price": 3.2, "Convenience": 1.4, "Sustainability": 1.4},
    "25-34": {"Taste": 3.5, "Less sugar": 2.6, "Price": 1.4, "Convenience": 1.8, "Sustainability": 0.9},
    "35-44": {"Taste": 3.0, "Less sugar": 3.2, "Price": 1.4, "Convenience": 1.4, "Sustainability": 0.7},
    "45+":   {"Taste": 2.4, "Less sugar": 4.2, "Price": 1.6, "Convenience": 0.8, "Sustainability": 0.6},
}
FREQUENCY_W = {
    "18-24": {"Daily": 2, "3-6 times a week": 4, "1-2 times a week": 3, "Less than weekly": 1.5},
    "25-34": {"Daily": 5, "3-6 times a week": 4, "1-2 times a week": 2, "Less than weekly": 0.8},
    "35-44": {"Daily": 5, "3-6 times a week": 3, "1-2 times a week": 2, "Less than weekly": 1},
    "45+":   {"Daily": 6, "3-6 times a week": 2, "1-2 times a week": 1.5, "Less than weekly": 1},
}
FORMAT_W = {"Single can": 5, "12-pack": 3, "No preference": 2}
PRICE_HIGH = [(3.50, 30), (3.80, 26), (4.00, 24), (4.50, 13), (5.00, 7)]   # >= S$3.50
PRICE_LOW = [(2.50, 18), (2.80, 24), (3.00, 34), (3.20, 24)]                # <  S$3.50
PAY_THRESHOLD = 3.50


def weighted(rng, pairs):
    vals, wts = zip(*pairs)
    return rng.choices(vals, weights=wts, k=1)[0]


def quota_assign(rng, rows, field, quotas, weights_by_age):
    """Give every row a value so the column hits `quotas` EXACTLY, while each
    row's pick still leans on its age band's weights. Sampling is proportional
    to weight x remaining quota, so an exhausted value is never chosen and the
    totals land exactly (sum of quotas == number of rows)."""
    left = dict(quotas)
    assert sum(left.values()) == len(rows), f"{field}: quotas do not sum to rows"
    for r in rng.sample(rows, len(rows)):
        w = weights_by_age[r["age_band"]]
        opts = [(k, w[k] * n) for k, n in left.items() if n > 0]
        pick = weighted(rng, opts)
        r[field] = pick
        left[pick] -= 1


def build_survey():
    rng = random.Random(SEED)
    rows = []
    for (city, age), n in CITY_AGE.items():
        rows += [dict(city=city, age_band=age) for _ in range(n)]

    # purchase intent: exactly LIKELY_BY_AGE[band] rows score 4-5 in each band
    for age in AGE_ORDER:
        band = [r for r in rows if r["age_band"] == age]
        rng.shuffle(band)
        k = LIKELY_BY_AGE[age]
        for i, r in enumerate(band):
            if i < k:
                r["purchase_intent"] = weighted(rng, [(4, 55), (5, 45)])
            else:
                r["purchase_intent"] = weighted(rng, [(1, 12), (2, 33), (3, 55)])

    # max price: the F["pay_350_plus"] rows with the highest latent willingness
    # (intent + noise) get a price >= S$3.50, everyone else below it.
    for r in rows:
        r["_wtp"] = r["purchase_intent"] + rng.gauss(0, 1.1) + (0.3 if r["age_band"] == "25-34" else 0)
    ranked = sorted(rows, key=lambda r: r["_wtp"], reverse=True)
    for i, r in enumerate(ranked):
        r["max_price_sgd"] = weighted(rng, PRICE_HIGH if i < F["pay_350_plus"] else PRICE_LOW)
        del r["_wtp"]

    quota_assign(rng, rows, "discovery_channel", dict(F["channels"]), CHANNEL_W)
    quota_assign(rng, rows, "top_driver", dict(F["drivers"]), DRIVER_W)
    for r in rows:
        r["coffee_frequency"] = weighted(rng, list(FREQUENCY_W[r["age_band"]].items()))
        r["preferred_format"] = weighted(rng, list(FORMAT_W.items()))

    # interleave cities and bands the way responses really arrive, then number them
    rng.shuffle(rows)
    start = date(2026, 9, 1)
    for i, r in enumerate(rows):
        r["respondent_id"] = f"LK-{i + 1:04d}"
        r["response_date"] = (start + timedelta(days=i * 29 // len(rows))).isoformat()
    return rows


SURVEY_COLS = ["respondent_id", "response_date", "city", "age_band", "coffee_frequency",
               "purchase_intent", "max_price_sgd", "discovery_channel", "top_driver",
               "preferred_format"]


def gen_survey():
    rows = SURVEY
    return csv_text(SURVEY_COLS, [[r[c] if c != "max_price_sgd" else f"{r[c]:.2f}"
                                   for c in SURVEY_COLS] for r in rows])


def check_survey(rows):
    """Re-measure the survey and assert every figure the labs quote."""
    n = len(rows)
    count = lambda pred: sum(1 for r in rows if pred(r))
    assert n == F["survey_n"], f"survey rows {n}"
    assert count(lambda r: r["city"] == "Singapore") == F["survey_sg"]
    assert count(lambda r: r["city"] == "Kuala Lumpur") == F["survey_kl"]
    for band, k in F["age_bands"]:
        assert count(lambda r: r["age_band"] == band) == k, f"age band {band}"
    likely = count(lambda r: r["purchase_intent"] >= 4)
    a25 = count(lambda r: r["age_band"] == "25-34")
    l25 = count(lambda r: r["age_band"] == "25-34" and r["purchase_intent"] >= 4)
    pay = count(lambda r: r["max_price_sgd"] >= PAY_THRESHOLD)
    assert likely == F["likely_to_buy"], f"likely {likely}"
    assert (l25, a25) == (F["likely_25_34"], dict(F["age_bands"])["25-34"]), f"25-34 {l25}/{a25}"
    assert pay == F["pay_350_plus"], f"pay >= 3.50: {pay}"
    for field, quotas in (("discovery_channel", F["channels"]), ("top_driver", F["drivers"])):
        for k, v in quotas:
            got = count(lambda r: r[field] == k)
            assert got == v, f"{field} {k}: {got} != {v}"
    assert all(1 <= r["purchase_intent"] <= 5 for r in rows)
    ch = {k: count(lambda r: r["discovery_channel"] == k) for k, _ in F["channels"]}
    dr = {k: count(lambda r: r["top_driver"] == k) for k, _ in F["drivers"]}
    top_ch, top_dr = max(ch, key=ch.get), max(dr, key=dr.get)
    assert (top_ch, top_dr) == ("Instagram", "Taste")
    # Lab 3's city filter: Instagram stays the top channel in both cities
    for city in ("Singapore", "Kuala Lumpur"):
        c = {k: count(lambda r: r["city"] == city and r["discovery_channel"] == k)
             for k, _ in F["channels"]}
        assert max(c, key=c.get) == "Instagram" and sorted(c.values())[-1] > sorted(c.values())[-2], \
            f"Instagram is not the clear top channel in {city}: {c}"
    return dict(n=n, likely=likely, l25=l25, a25=a25, pay=pay, channels=ch, drivers=dr,
                top_ch=top_ch, top_dr=top_dr)


# ================================================================== competitors
COMPETITOR_DETAIL = {
    # brand: (can_ml, pack, pack_price, milk, sugar_g, positioning, main_channel, market)
    "Kopi Kaki Cold":       (250, "6-pack", 18.00, "Evaporated milk", 14, "Value kopi-o-style, sweet and strong", "Supermarkets and convenience stores", "Singapore"),
    "Daily Grind RTD":      (240, "12-pack", 43.80, "Dairy milk", 11, "Everyday office coffee", "Convenience stores", "Singapore and Malaysia"),
    "Frostbean":            (250, "12-pack", 46.80, "Dairy milk", 9, "Café-style latte in a can", "Shopee and Lazada", "Singapore"),
    "OatRush":              (240, "6-pack", 25.20, "Oat milk", 12, "Plant-based, fitness crowd", "Gyms and online store", "Singapore"),
    "ChillBrew Co.":        (200, "4-pack", 18.40, "None (black)", 0, "Craft black cold brew for coffee purists", "Specialty cafés", "Singapore and Malaysia"),
    "Northpoint Cold Brew": (300, "4-pack", 21.60, "Dairy milk", 8, "Premium imported cold brew", "Premium supermarkets", "Singapore"),
}
COMPETITOR_COLS = ["brand", "price_per_can_sgd", "can_ml", "pack", "pack_price_sgd", "milk",
                   "sugar_g_per_can", "positioning", "main_channel", "market"]


def gen_competitors():
    rows = []
    for brand, price in F["competitors"]:
        ml, pack, pp, milk, sugar, pos, chan, mkt = COMPETITOR_DETAIL[brand]
        rows.append([brand, f"{price:.2f}", ml, pack, f"{pp:.2f}", milk, sugar, pos, chan, mkt])
    return csv_text(COMPETITOR_COLS, rows)


def check_competitors():
    prices = [p for _, p in F["competitors"]]
    assert len(prices) == 6 and set(COMPETITOR_DETAIL) == {b for b, _ in F["competitors"]}
    med = median(prices)
    assert sgd(med) == F["competitor_median"], f"median {sgd(med)}"
    assert PRICE_CAN < med, "Lumo is no longer below the competitor median"
    ladder = sorted(F["competitors"] + [("Lumo Cold Kopi", PRICE_CAN)], key=lambda x: (x[1], x[0] != "Lumo Cold Kopi"))
    # no competitor may claim Lumo's oat-milk + 5 g sugar position
    assert not any(d[3] == "Oat milk" and d[4] <= F["sugar_g"] for d in COMPETITOR_DETAIL.values())
    return dict(median=med, cheapest=ladder[0], dearest=ladder[-1],
                lumo_rank=[b for b, _ in ladder].index("Lumo Cold Kopi") + 1,
                ties=[b for b, p in F["competitors"] if p == PRICE_CAN])


# ================================================================== social trends
TRENDS = [
    # theme, best_platform, typical_format, posts_analysed, avg_engagement_pct, avg_views, trend_3m
    ("Behind the brew: how it is made", "Instagram", "Reel", 212, 5.9, 41000, "Rising"),
    ("Hawker and kopitiam nostalgia", "Instagram", "Carousel", 248, 5.6, 38500, "Steady"),
    ("Iced coffee recipes and hacks", "TikTok", "Short video", 305, 4.8, 66000, "Steady"),
    ("Taste tests and first-sip reactions", "TikTok", "Short video", 286, 7.4, 92000, "Rising"),
    ("Morning routines and desk setups", "TikTok", "Short video", 331, 5.2, 58000, "Rising"),
    ("Less-sugar swaps", "Instagram", "Carousel", 174, 4.5, 29500, "Rising"),
    ("Commute and on-the-go moments", "TikTok", "Short video", 198, 4.1, 47000, "Steady"),
    ("Creator collabs and duets", "TikTok", "Duet / stitch", 156, 4.7, 71000, "Steady"),
    ("Weekend lepak and picnics", "Instagram", "Reel", 143, 3.9, 26000, "Steady"),
    ("Giveaways and contests", "Instagram", "Static post", 267, 3.6, 33000, "Falling"),
    ("Price and value comparisons", "Facebook", "Static post", 121, 3.2, 14500, "Falling"),
    ("Sustainability and packaging", "LinkedIn", "Text + image", 98, 2.7, 9800, "Steady"),
]
TREND_COLS = ["theme", "best_platform", "typical_format", "posts_analysed",
              "avg_engagement_rate_pct", "avg_views", "trend_3m"]


def gen_trends():
    return csv_text(TREND_COLS, [[t, p, f, n, f"{e:.1f}", v, d] for t, p, f, n, e, v, d in TRENDS])


def check_trends():
    assert len(TRENDS) == 12, "Lab 2 says twelve content themes"
    by = sorted(TRENDS, key=lambda t: t[4], reverse=True)
    assert by[0][0] == F["top_trend"], f"top trend {by[0][0]}"
    rates = [t[4] for t in by[:4]]
    assert len(set(rates)) == 4, "top-three themes must not tie"
    return [t[0] for t in by[:3]]


# ================================================================== Lab 4 Drive folder
BUDGET_DETAIL = {
    "Instagram": ("Paid social", "Social lead", "Reels and carousel ads, 25-34 SG"),
    "TikTok": ("Paid social", "Social lead", "Spark ads on launch videos"),
    "Influencers": ("Creators", "Partnerships lead", "6 micro-creators, paid partnerships labelled"),
    "Google Search": ("Search", "Performance lead", "Brand and 'cold brew kopi' keywords"),
    "Shopee / Lazada ads": ("Marketplace", "E-commerce lead", "Sponsored listings, launch fortnight"),
}


def gen_budget():
    rows = [[line, amt, *BUDGET_DETAIL[line]] for line, amt in F["budget_sheet"]]
    return csv_text(["line_item", "amount_sgd", "category", "owner", "notes"], rows)


def check_budget():
    sheet, brief = dict(F["budget_sheet"]), dict(F["budget_brief"])
    total = money(F["budget_total"])
    assert sum(sheet.values()) == total and sum(brief.values()) == total
    assert list(sheet) == list(brief)
    diff = {k: (sheet[k], brief[k]) for k in sheet if sheet[k] != brief[k]}
    assert list(diff) == ["Instagram", "Influencers"], f"budget lines that disagree: {list(diff)}"
    return diff


TIMELINE = [
    (date(2026, 10, 9), "Launch brief approved", "Marketing lead", "Done"),
    (date(2026, 10, 16), "Brand kit and product sheet signed off", "Brand lead", "Done"),
    (date(2026, 10, 30), "Market research brief and insights dashboard", "Insights lead", "In progress"),
    (date(2026, 11, 6), "Launch deck and campaign brief approved", "Marketing lead", "Not started"),
    (date(2026, 11, 13), "Brand-voice skill and social calendar drafted", "Social lead", "Not started"),
    (date(2026, 11, 20), "Creator content approved (paid partnerships labelled)", "Partnerships lead", "Not started"),
    (date(2026, 11, 24), "Launch video final", "Content lead", "Not started"),
    (date(2026, 11, 27), "Shopee and Lazada store pages live", "E-commerce lead", "Not started"),
    (LAUNCH_SG, "Singapore launch - first Instagram and TikTok posts live", "Marketing lead", "Not started"),
    (date(2026, 12, 14), "Launch fortnight review", "Marketing lead", "Not started"),
    (LAUNCH_KL, "Kuala Lumpur launch", "Marketing lead", "Not started"),
]


def gen_timeline():
    rows = [[d.isoformat(), f"{d:%a}", m, o, s] for d, m, o, s in TIMELINE]
    return csv_text(["date", "day", "milestone", "owner", "status"], rows)


def check_timeline():
    dates = [d for d, *_ in TIMELINE]
    assert dates == sorted(dates)
    assert any(d == LAUNCH_SG and "Singapore launch" in m for d, m, *_ in TIMELINE)
    assert dates[-1] == LAUNCH_KL


# ================================================================== Lab 6 captions
SAMPLE_CAPTIONS = [
    ("Lumo Cold Kopi is HERE!!! Only $3.9 per can, so cheap lah. Grab yours now "
     "#coffee #kopi #singapore #icedcoffee #oatmilk #drinks #yummy #LumoKopi"),
    ("Meet the healthiest cold coffee in Singapore. Oat milk is good for your heart "
     "and only 5 g sugar, so it's totally guilt-free. #LumoKopi #KopiChilledRight"),
    ("Wah this one damn shiok sia, confirm plus chop the best kopi, lepak also can, "
     "steady pom pi pi! Try leh #LumoKopi"),
    ("Lumo 12-pack now SGD42 on Shopee! Follow us, tag 3 friends, share this post and "
     "click the link in bio to win! #KopiChilledRight #ColdBrew"),
    ("Okay my new morning obsession: Lumo Cold Kopi. All-day energy boost and it burns "
     "fat?? Comment below if you want to try #LumoKopi #KopiChilledRight #fyp"),
]


def gen_captions():
    lines = ["Lumo Kopi Co. - draft captions from the agency (NOT approved)",
             "Rewrite each one in the Lumo brand voice before anything is posted.",
             "Caption 5 is a creator's post for a paid partnership.", ""]
    for i, c in enumerate(SAMPLE_CAPTIONS, 1):
        lines += [f"Caption {i}:", c, ""]
    return "\n".join(lines)


def check_captions():
    for t in DO_EXAMPLES:
        assert not brand_violations(t), f"'Do' example breaks a rule: {brand_violations(t)}\n{t}"
    for t in DONT_EXAMPLES:
        assert brand_violations(t), f"'Don't' example passes every rule: {t}"
    found = {}
    for i, c in enumerate(SAMPLE_CAPTIONS, 1):
        v = brand_violations(c)
        assert v, f"sample caption {i} breaks no rule"
        found[i] = sorted(v)
    seen = {k for v in found.values() for k in v}
    # Lab 6 step 1 names these four
    for need in ("price format", "unprovable claim", "too much Singlish", "too many hashtags"):
        assert need in seen, f"no sample caption shows '{need}'"
    return found


# ================================================================== Lab 8 template
CALENDAR_COLS = ["date", "platform", "format", "hook", "copy", "hashtags",
                 "visual_idea", "call_to_action"]


def gen_calendar_template():
    return csv_text(CALENDAR_COLS, [])


def launch_weekdays():
    end = LAUNCH_SG + timedelta(days=13)
    days = [LAUNCH_SG + timedelta(days=i) for i in range(14)]
    return [d for d in days if d.weekday() < 5 and d <= end]


# ================================================================== Lab 9 images
SS = 2   # supersampling factor: draw at 2x, downsample for clean anti-aliased edges

FONT_CANDIDATES = {
    "heavy": [("/System/Library/Fonts/Avenir Next.ttc", 8),
              ("/System/Library/Fonts/Supplemental/Arial Black.ttf", 0),
              ("DejaVuSans-Bold.ttf", 0)],
    "bold": [("/System/Library/Fonts/Avenir Next.ttc", 0),
             ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 0),
             ("DejaVuSans-Bold.ttf", 0)],
    "demi": [("/System/Library/Fonts/Avenir Next.ttc", 2),
             ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 0),
             ("DejaVuSans-Bold.ttf", 0)],
    "medium": [("/System/Library/Fonts/Avenir Next.ttc", 5),
               ("/System/Library/Fonts/Supplemental/Arial.ttf", 0),
               ("DejaVuSans.ttf", 0)],
}


def font(style, size):
    for path, idx in FONT_CANDIDATES[style]:
        try:
            return ImageFont.truetype(path, int(size), index=idx)
        except OSError:
            continue
    return ImageFont.load_default(int(size))


def rgb(hx, a=255):
    hx = hx.lstrip("#")
    return tuple(int(hx[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


def mix(c1, c2, t):
    a, b = rgb(c1) if isinstance(c1, str) else c1, rgb(c2) if isinstance(c2, str) else c2
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(4))


def text_c(d, cx, y, s, f, fill, track=0):
    """Draw `s` centred on cx with optional letter-spacing (in px)."""
    widths = [f.getlength(ch) for ch in s]
    total = sum(widths) + track * (len(s) - 1)
    x = cx - total / 2
    for ch, w in zip(s, widths):
        d.text((x, y), ch, font=f, fill=fill)
        x += w + track


def fit_font(style, size, s, max_w):
    """Largest font <= size whose rendering of `s` fits in max_w."""
    while size > 8 and font(style, size).getlength(s) > max_w:
        size *= 0.95
    return font(style, size)


def vgrad(w, h, top, bottom):
    """Vertical gradient image (RGBA)."""
    col = Image.new("RGBA", (1, h))
    for y in range(h):
        col.putpixel((0, y), mix(top, bottom, y / max(1, h - 1)))
    return col.resize((w, h))


def hshade(w, h, fn):
    """L-mode image whose value per column is fn(x/w) in 0..255."""
    row = Image.new("L", (w, 1))
    for x in range(w):
        row.putpixel((x, 0), max(0, min(255, int(fn(x / max(1, w - 1))))))
    return row.resize((w, h))


def finish(img, size):
    return img.resize(size, Image.LANCZOS)


def sun_mark(d, cx, cy, r, colour, rays=True, horizon=None):
    """The Lumo sun: a rising half-disc with five short rays."""
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=colour)
    if rays:
        for ang in (180 + 22, 180 + 56, 270, 360 - 56, 360 - 22):
            a = math.radians(ang)
            x1, y1 = cx + math.cos(a) * r * 1.28, cy + math.sin(a) * r * 1.28
            x2, y2 = cx + math.cos(a) * r * 1.62, cy + math.sin(a) * r * 1.62
            d.line([x1, y1, x2, y2], fill=colour, width=max(2, int(r * 0.16)))
            for x, y in ((x1, y1), (x2, y2)):
                rr = r * 0.08
                d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=colour)
    if horizon:
        d.rounded_rectangle([cx - r * 1.5, cy + r * 0.08, cx + r * 1.5, cy + r * 0.24],
                            radius=r * 0.08, fill=horizon)


def draw_can(cw, ch):
    """A stylised Lumo can, cw x ch final pixels, RGBA on transparent."""
    W, H = cw * SS, ch * SS
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lid_h = W * 0.16                         # ellipse height of top and bottom
    top_y, neck_y, body_y, bot_y = lid_h * 0.5, lid_h * 0.5 + H * 0.025, H * 0.075, H - lid_h * 0.5
    inset = W * 0.07

    # silhouette mask
    mask = Image.new("L", (W, H), 0)
    m = ImageDraw.Draw(mask)
    m.rectangle([0, body_y, W, bot_y], fill=255)
    m.ellipse([0, bot_y - lid_h / 2, W, bot_y + lid_h / 2], fill=255)
    m.polygon([(0, body_y), (inset, neck_y), (W - inset, neck_y), (W, body_y)], fill=255)
    m.rectangle([inset, top_y, W - inset, neck_y], fill=255)
    m.ellipse([inset, top_y - lid_h * 0.42, W - inset, top_y + lid_h * 0.42], fill=255)

    art = Image.new("RGBA", (W, H), rgb(BROWN))
    d = ImageDraw.Draw(art)
    # metallic shoulder and neck
    d.rectangle([0, 0, W, body_y + H * 0.004], fill=rgb("#B9BDC1"))
    # oat-cream label band, with teal pinstripes
    band_t, band_b = H * 0.17, H * 0.64
    d.rectangle([0, band_t, W, band_b], fill=rgb(OAT))
    for y in (band_t, band_b):
        d.rectangle([0, y - H * 0.006, W, y + H * 0.006], fill=rgb(TEAL))
    cx = W / 2
    sun_mark(d, cx, H * 0.285, W * 0.11, rgb(ORANGE), horizon=rgb(TEAL))
    text_c(d, cx, H * 0.315, "lumo", font("heavy", W * 0.36), rgb(BROWN), track=-W * 0.006)
    text_c(d, cx, H * 0.475, "COLD KOPI", font("bold", W * 0.135), rgb(TEAL), track=W * 0.012)
    text_c(d, cx, H * 0.56, "OAT-MILK KOPI COLD BREW", font("demi", W * 0.058), rgb(BROWN), track=W * 0.006)
    # lower panel
    text_c(d, cx, H * 0.71, "LUMO COLD KOPI", font("bold", W * 0.083), rgb(OAT), track=W * 0.01)
    pill_w, pill_h, py = W * 0.74, H * 0.068, H * 0.79
    d.rounded_rectangle([cx - pill_w / 2, py, cx + pill_w / 2, py + pill_h],
                        radius=pill_h / 2, fill=rgb(ORANGE))
    text_c(d, cx, py + pill_h * 0.16, f"{F['sugar_g']} g sugar · {F['can_ml']} ml",
           font("demi", W * 0.075), rgb(BROWN))
    # cylinder shading: dark edges + a soft highlight stripe
    dark = hshade(W, H, lambda t: 150 * abs(t - 0.5) ** 2.4 * 2 ** 2.4 + 0)
    light = hshade(W, H, lambda t: 120 * math.exp(-((t - 0.27) / 0.07) ** 2)
                   + 40 * math.exp(-((t - 0.78) / 0.04) ** 2))
    art = Image.composite(Image.new("RGBA", (W, H), (20, 12, 8, 255)), art, dark)
    art = Image.composite(Image.new("RGBA", (W, H), (255, 255, 255, 255)), art, light)
    img.paste(art, (0, 0), mask)

    # lid: rim, recessed top, pull tab
    d = ImageDraw.Draw(img)
    lx0, lx1 = inset, W - inset
    d.ellipse([lx0, top_y - lid_h * 0.42, lx1, top_y + lid_h * 0.42], fill=rgb("#D7DADD"))
    d.ellipse([lx0 + W * 0.035, top_y - lid_h * 0.32, lx1 - W * 0.035, top_y + lid_h * 0.32],
              fill=rgb("#A9AEB3"))
    d.ellipse([lx0 + W * 0.05, top_y - lid_h * 0.27, lx1 - W * 0.05, top_y + lid_h * 0.29],
              fill=rgb("#C4C8CC"))
    d.rounded_rectangle([cx - W * 0.12, top_y - lid_h * 0.14, cx + W * 0.06, top_y + lid_h * 0.1],
                        radius=lid_h * 0.12, fill=rgb("#9DA2A7"))
    d.ellipse([cx - W * 0.085, top_y - lid_h * 0.07, cx - W * 0.035, top_y + lid_h * 0.04],
              fill=rgb("#C4C8CC"))
    return img.resize((cw, ch), Image.LANCZOS)


def drop_shadow(canvas, box, blur, alpha=90):
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse(box, fill=(40, 25, 15, alpha))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))


def img_can():
    W, H = 1080, 1350
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cw, ch = 470, 1120
    x, y = (W - cw) // 2, 95
    drop_shadow(out, [x - 30, y + ch - 50, x + cw + 30, y + ch + 40], 22)
    out.alpha_composite(draw_can(cw, ch), (x, y))
    return out


def img_12pack():
    W, H = 1350, 1080
    big = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    s = SS
    # carton in a gentle three-quarter view: front, side, top
    fx0, fy0, fx1, fy1 = 170 * s, 300 * s, 1010 * s, 900 * s
    dx, dy = 190 * s, -120 * s
    d.polygon([(fx0, fy0), (fx0 + dx, fy0 + dy), (fx1 + dx, fy0 + dy), (fx1, fy0)], fill=rgb("#7A5240"))
    d.polygon([(fx1, fy0), (fx1 + dx, fy0 + dy), (fx1 + dx, fy1 + dy), (fx1, fy1)], fill=rgb("#432A1D"))
    d.rectangle([fx0, fy0, fx1, fy1], fill=rgb(BROWN))
    # handle cut-out on the top
    hx, hy = (fx0 + fx1) / 2 + dx / 2, fy0 + dy / 2
    d.rounded_rectangle([hx - 110 * s, hy - 18 * s, hx + 110 * s, hy + 18 * s], radius=18 * s, fill=rgb("#2E1C13"))
    # side panel: teal band and "12" badge
    d.polygon([(fx1, fy0 + 210 * s), (fx1 + dx, fy0 + dy + 210 * s),
               (fx1 + dx, fy0 + dy + 330 * s), (fx1, fy0 + 330 * s)], fill=rgb("#17696A"))
    # front panel
    d.rounded_rectangle([fx0 + 40 * s, fy0 + 40 * s, fx1 - 40 * s, fy1 - 40 * s], radius=36 * s, fill=rgb(OAT))
    d.rectangle([fx0, fy0 + 210 * s, fx0 + 40 * s, fy0 + 330 * s], fill=rgb(TEAL))
    cx = (fx0 + fx1) / 2 - 40 * s          # the standing cans cover the right edge
    # sun + wordmark as one centred group
    wf = font("heavy", 165 * s)
    sun_r, gap = 50 * s, 46 * s
    group = sun_r * 3.24 + gap + wf.getlength("lumo")
    gx = cx - group / 2
    sun_mark(d, gx + sun_r * 1.62, fy0 + 200 * s, sun_r, rgb(ORANGE), horizon=rgb(TEAL))
    d.text((gx + sun_r * 3.24 + gap, fy0 + 38 * s), "lumo", font=wf, fill=rgb(BROWN))
    text_c(d, cx, fy0 + 268 * s, "COLD KOPI", font("bold", 78 * s), rgb(TEAL), track=10 * s)
    text_c(d, cx, fy0 + 372 * s, "OAT-MILK KOPI COLD BREW", font("demi", 30 * s), rgb(BROWN), track=4 * s)
    bw, bh, by = 500 * s, 62 * s, fy0 + 430 * s
    d.rounded_rectangle([cx - bw / 2, by, cx + bw / 2, by + bh], radius=bh / 2, fill=rgb(ORANGE))
    text_c(d, cx, by + 9 * s, f"12 × {F['can_ml']} ml  ·  {F['sugar_g']} g sugar each",
           font("demi", 34 * s), rgb(BROWN))
    pack = finish(big, (W, H))
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    drop_shadow(out, [140, 850, 1240, 960], 26)
    out.alpha_composite(pack)
    # two cans standing in front of the carton
    for x, y in ((960, 560), (1110, 600)):
        cw, ch = 190, 452
        drop_shadow(out, [x - 12, y + ch - 24, x + cw + 12, y + ch + 22], 10, 110)
        out.alpha_composite(draw_can(cw, ch), (x, y))
    return out


def img_logo():
    W, H = 1600, 640
    big = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    s = SS
    sun_mark(d, 290 * s, 330 * s, 130 * s, rgb(ORANGE), horizon=rgb(TEAL))
    f = font("heavy", 360 * s)
    d.text((520 * s, 40 * s), "lumo", font=f, fill=rgb(BROWN))
    word_w = f.getlength("lumo")
    sub = font("bold", 74 * s)
    text_c(d, 520 * s + word_w / 2, 450 * s, "KOPI CO.", sub, rgb(TEAL), track=26 * s)
    return _pad_logo(finish(big, (W, H)))


def _pad_logo(img):
    """Trim to the artwork and pad evenly, so the logo centres cleanly in video."""
    box = img.getbbox()
    art = img.crop(box)
    pad = 60
    out = Image.new("RGBA", (art.width + pad * 2, art.height + pad * 2), (0, 0, 0, 0))
    out.alpha_composite(art, (pad, pad))
    return out


def scene_hawker():
    W, H = 1080 * SS, 1920 * SS
    s = SS
    rng = random.Random(SEED + 1)
    img = vgrad(W, H, "#FBE3C4", OAT)
    d = ImageDraw.Draw(img)
    # ceiling and roof beams
    ceil = 330 * s
    d.rectangle([0, 0, W, ceil], fill=rgb("#17696A"))
    for i in range(-2, 9):
        x = i * 160 * s
        d.polygon([(x, 0), (x + 40 * s, 0), (x + 120 * s, ceil), (x + 80 * s, ceil)], fill=rgb("#1C7B7B"))
    d.rectangle([0, ceil - 18 * s, W, ceil], fill=rgb(BROWN))
    # ceiling fans
    for fx in (230 * s, 850 * s):
        d.line([fx, 0, fx, 170 * s], fill=rgb("#0F4F4F"), width=8 * s)
        d.ellipse([fx - 150 * s, 160 * s, fx + 150 * s, 200 * s], fill=rgb("#0F4F4F"))
        d.ellipse([fx - 26 * s, 158 * s, fx + 26 * s, 204 * s], fill=rgb("#C7CBCF"))
    # pendant lamps
    for lx in (540 * s,):
        d.line([lx, 0, lx, 250 * s], fill=rgb(BROWN), width=5 * s)
        d.pieslice([lx - 60 * s, 230 * s, lx + 60 * s, 350 * s], 180, 360, fill=rgb(ORANGE))
    # stall row on the back wall
    wall_t, counter_t, floor_t = 400 * s, 900 * s, 1080 * s
    stalls = [("KOPI · TEH", TEAL), ("NOODLES", ORANGE), ("RICE & CURRY", BROWN)]
    sw = W / 3
    inner = sw - 36 * s - 80 * s
    sign_font = min((fit_font("bold", 48 * s, n, inner - 4 * s * len(n)) for n, _ in stalls),
                    key=lambda f: f.size)          # one size for all three signs
    for i, (name, col) in enumerate(stalls):
        x0, x1 = i * sw + 18 * s, (i + 1) * sw - 18 * s
        d.rectangle([x0, wall_t, x1, floor_t], fill=rgb("#E9DAC6"))
        # signboard
        d.rounded_rectangle([x0 + 10 * s, wall_t + 20 * s, x1 - 10 * s, wall_t + 130 * s],
                            radius=14 * s, fill=rgb(col))
        tc = rgb(OAT) if col != ORANGE else rgb(BROWN)
        sf = sign_font
        text_c(d, (x0 + x1) / 2, wall_t + 75 * s - sf.size * 0.62, name, sf, tc, track=4 * s)
        # striped awning
        aw_t, aw_b = wall_t + 150 * s, wall_t + 215 * s
        n = 7
        stripe = (x1 - x0) / n
        for k in range(n):
            c = rgb(col) if k % 2 == 0 else rgb(OAT)
            d.rectangle([x0 + k * stripe, aw_t, x0 + (k + 1) * stripe, aw_b], fill=c)
            d.pieslice([x0 + k * stripe, aw_b - stripe / 2, x0 + (k + 1) * stripe, aw_b + stripe / 2],
                       0, 180, fill=c)
        # shelves with cups and bowls
        for row, y in enumerate((wall_t + 330 * s, wall_t + 430 * s)):
            d.rectangle([x0 + 30 * s, y, x1 - 30 * s, y + 10 * s], fill=rgb(BROWN))
            for k in range(5):
                cx = x0 + 70 * s + k * (x1 - x0 - 140 * s) / 4
                if (i + row + k) % 2:
                    d.rounded_rectangle([cx - 20 * s, y - 50 * s, cx + 20 * s, y], radius=6 * s, fill=rgb(OAT))
                    d.rectangle([cx - 20 * s, y - 34 * s, cx + 20 * s, y - 26 * s], fill=rgb(col))
                else:
                    d.chord([cx - 30 * s, y - 50 * s, cx + 30 * s, y + 10 * s], 0, 180, fill=rgb("#FFFFFF"))
        # counter
        d.rectangle([x0, counter_t, x1, floor_t], fill=rgb("#C9B49A"))
        d.rectangle([x0, counter_t, x1, counter_t + 22 * s], fill=rgb("#8E6E55"))
    # floor: warm terrazzo
    d.rectangle([0, floor_t, W, H], fill=rgb("#E6D8C4"))
    for _ in range(900):
        x, y = rng.uniform(0, W), rng.uniform(floor_t + 10 * s, H)
        r = rng.uniform(2, 6) * s
        c = rng.choice(["#CDBBA3", "#D9C3A8", "#BFA88F", "#F1E6D6"])
        d.ellipse([x - r, y - r * 0.6, x + r, y + r * 0.6], fill=rgb(c))
    # round tables with stools: two at the sides, one large in the foreground
    def table(cx, cy, r, top=OAT):
        d.ellipse([cx - r * 0.95, cy + r * 1.05, cx + r * 0.95, cy + r * 1.35], fill=rgb("#D3C1A8"))
        d.rectangle([cx - r * 0.08, cy, cx + r * 0.08, cy + r * 1.2], fill=rgb("#8E6E55"))
        d.ellipse([cx - r * 0.45, cy + r * 1.1, cx + r * 0.45, cy + r * 1.28], fill=rgb("#8E6E55"))
        d.ellipse([cx - r, cy - r * 0.3, cx + r, cy + r * 0.3], fill=rgb("#8E6E55"))
        d.ellipse([cx - r, cy - r * 0.34, cx + r, cy + r * 0.24], fill=rgb(top))

    def stool(cx, cy, r, col):
        d.rectangle([cx - r * 0.12, cy, cx + r * 0.12, cy + r * 1.6], fill=rgb("#8E6E55"))
        d.ellipse([cx - r, cy - r * 0.32, cx + r, cy + r * 0.32], fill=rgb(col))

    for cx, cy, r in ((150 * s, 1250 * s, 120 * s), (930 * s, 1250 * s, 120 * s)):
        stool(cx - 150 * s if cx < W / 2 else cx + 150 * s, cy + 70 * s, 50 * s, ORANGE)
        table(cx, cy, r)
    stool(140 * s, 1640 * s, 80 * s, TEAL)
    stool(940 * s, 1640 * s, 80 * s, TEAL)
    table(540 * s, 1600 * s, 330 * s)
    return finish(img, (1080, 1920)).convert("RGB")


def scene_office():
    W, H = 1080 * SS, 1920 * SS
    s = SS
    img = Image.new("RGBA", (W, H), rgb(OAT))
    d = ImageDraw.Draw(img)
    # window with a dusk skyline
    wx0, wy0, wx1, wy1 = 110 * s, 230 * s, 970 * s, 1180 * s
    sky = vgrad(wx1 - wx0, wy1 - wy0, "#1F8A8A", "#F7B77A")
    img.paste(sky, (wx0, wy0))
    rng = random.Random(SEED + 2)
    x = wx0
    while x < wx1:
        bw = rng.randint(70, 150) * s
        bh = rng.randint(250, 720) * s
        col = rng.choice(["#155F60", "#1A6E6E", "#3F2A1F", "#4E3426"])
        top = wy1 - bh
        d.rectangle([x, top, min(x + bw, wx1), wy1], fill=rgb(col))
        for wy in range(int(top + 30 * s), int(wy1 - 20 * s), int(46 * s)):
            for wxp in range(int(x + 16 * s), int(min(x + bw, wx1) - 24 * s), int(36 * s)):
                if rng.random() < 0.45:
                    d.rectangle([wxp, wy, wxp + 14 * s, wy + 20 * s], fill=rgb("#FFD08A"))
        x += bw + rng.randint(4, 18) * s
    # frame and mullions
    fr = 26 * s
    d.rectangle([wx0 - fr, wy0 - fr, wx1 + fr, wy0], fill=rgb(BROWN))
    d.rectangle([wx0 - fr, wy1, wx1 + fr, wy1 + fr], fill=rgb(BROWN))
    d.rectangle([wx0 - fr, wy0, wx0, wy1], fill=rgb(BROWN))
    d.rectangle([wx1, wy0, wx1 + fr, wy1], fill=rgb(BROWN))
    d.rectangle([(wx0 + wx1) / 2 - 9 * s, wy0, (wx0 + wx1) / 2 + 9 * s, wy1], fill=rgb(BROWN))
    d.rectangle([wx0, wy0 + 360 * s, wx1, wy0 + 376 * s], fill=rgb(BROWN))
    # pendant lamp
    d.line([540 * s, 0, 540 * s, 120 * s], fill=rgb(BROWN), width=5 * s)
    d.pieslice([440 * s, 90 * s, 640 * s, 290 * s], 180, 360, fill=rgb(TEAL))
    d.ellipse([515 * s, 175 * s, 565 * s, 205 * s], fill=rgb("#FFE2B0"))
    # desk
    desk_t = 1360 * s
    d.rectangle([0, desk_t, W, H], fill=rgb("#A9774F"))
    d.rectangle([0, desk_t, W, desk_t + 26 * s], fill=rgb("#C38E62"))
    d.rectangle([0, desk_t + 26 * s, W, desk_t + 44 * s], fill=rgb("#8A5F3F"))
    for i in range(6):   # wood grain
        y = desk_t + (110 + i * 90) * s
        d.line([0, y, W, y + 14 * s], fill=rgb("#9C6C47"), width=3 * s)
    # laptop (left)
    lx0, lx1 = 40 * s, 400 * s
    d.polygon([(lx0 + 30 * s, desk_t - 250 * s), (lx1 - 20 * s, desk_t - 250 * s),
               (lx1, desk_t + 5 * s), (lx0 + 10 * s, desk_t + 5 * s)], fill=rgb("#5E6469"))
    d.polygon([(lx0 + 50 * s, desk_t - 232 * s), (lx1 - 38 * s, desk_t - 232 * s),
               (lx1 - 20 * s, desk_t - 18 * s), (lx0 + 30 * s, desk_t - 18 * s)], fill=rgb("#2F4A4F"))
    for k in range(4):
        y = desk_t - (200 - k * 40) * s
        d.rounded_rectangle([lx0 + 80 * s, y, lx0 + (230 - k * 25) * s, y + 16 * s], radius=8 * s,
                            fill=rgb(ORANGE if k == 0 else "#7FB8B8"))
    d.rounded_rectangle([lx0 - 20 * s, desk_t + 5 * s, lx1 + 30 * s, desk_t + 40 * s], radius=10 * s,
                        fill=rgb("#C7CBCF"))
    # notebook and pen (front left)
    d.polygon([(110 * s, 1640 * s), (420 * s, 1600 * s), (470 * s, 1820 * s), (150 * s, 1870 * s)],
              fill=rgb("#FFFFFF"))
    for k in range(5):
        y0 = 1660 + k * 36
        d.line([(150 * s, (y0 + 4) * s), (420 * s, (y0 - 34) * s)], fill=rgb("#D9CDBE"), width=3 * s)
    d.line([(390 * s, 1650 * s), (520 * s, 1830 * s)], fill=rgb(TEAL), width=12 * s)
    # plant (right)
    px = 850 * s
    for ang, ln, col in ((-70, 320, "#2E8B57"), (-100, 350, "#3C9D63"), (-125, 290, "#2E8B57"),
                         (-50, 230, "#3C9D63"), (-85, 240, "#4BAE73"), (-140, 230, "#4BAE73")):
        a = math.radians(ang)
        ex, ey = px + math.cos(a) * ln * s, desk_t - 120 * s + math.sin(a) * ln * s
        mx, my = (px + ex) / 2, (desk_t - 120 * s + ey) / 2
        d.line([px, desk_t - 120 * s, ex, ey], fill=rgb("#2A6F47"), width=5 * s)
        d.ellipse([mx - 46 * s, my - 22 * s, mx + 46 * s, my + 22 * s], fill=rgb(col))
        d.ellipse([ex - 40 * s, ey - 26 * s, ex + 40 * s, ey + 26 * s], fill=rgb(col))
    d.polygon([(px - 110 * s, desk_t - 150 * s), (px + 110 * s, desk_t - 150 * s),
               (px + 85 * s, desk_t + 30 * s), (px - 85 * s, desk_t + 30 * s)], fill=rgb(ORANGE))
    d.rectangle([px - 116 * s, desk_t - 160 * s, px + 116 * s, desk_t - 128 * s], fill=rgb("#D9762A"))
    return finish(img, (1080, 1920)).convert("RGB")


def png_bytes(img):
    import io
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def check_images(imgs):
    expect = {"lumo-can.png": ((1080, 1350), True), "scene-hawker.png": ((1080, 1920), False),
              "scene-office.png": ((1080, 1920), False)}
    for name, ((w, h), alpha) in expect.items():
        im = imgs[name]
        assert im.size == (w, h), f"{name} is {im.size}"
        if alpha:
            assert im.mode == "RGBA" and im.getpixel((0, 0))[3] == 0, f"{name} needs a transparent background"
    for name in ("lumo-12pack.png", "lumo-logo.png"):
        assert imgs[name].mode == "RGBA" and imgs[name].getpixel((0, 0))[3] == 0


# ================================================================== registry
# basename of a lab `data` entry -> generator returning str (text) or Image.
GENERATORS = {
    "lumo-brand-guidelines.md": gen_brand_guidelines,
    "lumo-product-sheet.md": gen_product_sheet,
    "lumo-launch-brief.md": gen_launch_brief,
    "lumo-consumer-survey-2026.csv": gen_survey,
    "lumo-competitors.csv": gen_competitors,
    "lumo-social-trends.csv": gen_trends,
    "lumo-launch-budget.csv": gen_budget,
    "lumo-launch-timeline.csv": gen_timeline,
    "lumo-sample-captions.txt": gen_captions,
    "social-calendar-template.csv": gen_calendar_template,
    "lumo-can.png": img_can,
    "lumo-12pack.png": img_12pack,
    "lumo-logo.png": img_logo,
    "scene-hawker.png": scene_hawker,
    "scene-office.png": scene_office,
}


# ================================================================== lab-text checks
def lab_text(num):
    lab = LABS[num]
    parts = [lab.get("desc", ""), lab.get("build", ""), lab.get("prompt", ""), lab.get("test", "")]
    parts += [b["text"] for b in lab.get("prompt_blocks", [])]
    parts += [x for st in lab.get("steps", []) for x in st]
    return " ".join(" ".join(parts).split())      # prompts wrap lines; compare words


def quoted(num, *phrases):
    txt = lab_text(num)
    for p in phrases:
        assert p in txt, f"Lab {num} text no longer quotes: {p!r}"


def check_lab_text(sv, comp, top3, diff):
    n = sv["n"]
    # Lab 1 — product sheet figures
    quoted(1, F["price_can"], f"{F['sugar_g']} g sugar", F["launch_sg"], F["launch_kl"], "25-34")
    # Lab 2 — research brief figures
    quoted(2, f"{n} survey rows", "six competitors", "twelve content themes",
           f"{sv['likely']} likely to buy ({pct(sv['likely'], n)}%)",
           f"{sv['l25']} of {sv['a25']} in the 25-34 band ({pct(sv['l25'], sv['a25'])}%)",
           f"Instagram is the top discovery channel at {sv['channels']['Instagram']} "
           f"({pct(sv['channels']['Instagram'], n)}%)",
           f"TikTok at {sv['channels']['TikTok']} ({pct(sv['channels']['TikTok'], n)}%)",
           f"Taste is the top driver at {sv['drivers']['Taste']} ({pct(sv['drivers']['Taste'], n)}%)",
           f"competitor median is {sgd(comp['median'])}",
           f"{sv['pay']} respondents ({pct(sv['pay'], n)}%) would pay S$3.50 or more",
           F["top_trend"])
    # Lab 3 — dashboard
    cheap, dear = comp["cheapest"], comp["dearest"]
    quoted(3, f"{n} respondents", f"{pct(sv['likely'], n)}% likely to buy", f"{sgd(comp['median'])}",
           f"{F['survey_sg']}, then {F['survey_kl']}",
           f"{cheap[0]} at {sgd(cheap[1])} is cheapest", f"{dear[0]} at {sgd(dear[1])} is dearest")
    # Lab 4 — budget disagreement
    ig, inf = diff["Instagram"], diff["Influencers"]
    quoted(4, f"Both total {F['budget_total']}",
           f"Instagram is {sgd0(ig[0])} in the Drive sheet and {sgd0(ig[1])} in the brief",
           f"Influencers is {sgd0(inf[0])} against {sgd0(inf[1])}",
           f"Instagram ({sgd0(ig[0])} vs {sgd0(ig[1])})", f"Influencers ({sgd0(inf[0])} vs {sgd0(inf[1])})")
    # Lab 5 — deck
    quoted(5, f"{pct(sv['likely'], n)}% likely to buy", f"{pct(sv['l25'], sv['a25'])}% among 25-34s",
           f"Instagram {pct(sv['channels']['Instagram'], n)}%",
           f"from {sgd(cheap[1])} to {sgd(dear[1])}", F["budget_total"])
    # Lab 8 — calendar
    days = launch_weekdays()
    assert len(days) == F["social_posts"]
    day_list = ", ".join(str(d.day) for d in days[:-1]) + f" and {days[-1].day} December"
    quoted(8, ", ".join(c.replace("_", " ") for c in CALENDAR_COLS),
           f"{days[0]:%A} {days[0].day} December", f"{days[-1]:%A} {days[-1].day} December", day_list)
    # Lab 9 — five supplied images
    assert len(LABS[9]["data"]) == 5
    quoted(9, "five images", "1080 × 1920")


# ================================================================== main
def generate(name, cache):
    if name not in cache:
        if name not in GENERATORS:
            raise SystemExit(f"No generator for lab data file '{name}' — add one to GENERATORS")
        cache[name] = GENERATORS[name]()
    return cache[name]


SURVEY = build_survey()


def main():
    sv = check_survey(SURVEY)
    comp = check_competitors()
    top3 = check_trends()
    diff = check_budget()
    check_timeline()
    caps = check_captions()
    check_lab_text(sv, comp, top3, diff)

    cache = {}
    for num in sorted(LABS):
        for entry in LABS[num]["data"]:
            content = generate(os.path.basename(entry), cache)
            data = png_bytes(content) if isinstance(content, Image.Image) else content.encode("utf-8")
            write_bytes(os.path.join(lab_data_dir(num), entry), data)
    check_images({k: v for k, v in cache.items() if isinstance(v, Image.Image)})

    # the brief and the sheet must still disagree after being written out
    brief = cache["lumo-launch-brief.md"]
    for line, (sheet_amt, brief_amt) in diff.items():
        assert f"| {line} | {sgd0(brief_amt)} |" in brief and f"| {line} | {sgd0(sheet_amt)} |" not in brief

    n = sv["n"]
    print(f"\n  Survey        {n} rows · SG {F['survey_sg']} / KL {F['survey_kl']}   [matches courseware]")
    print(f"  Likely to buy {sv['likely']} ({pct(sv['likely'], n)}%) · 25-34 {sv['l25']} of {sv['a25']} "
          f"({pct(sv['l25'], sv['a25'])}%) · pay >= S$3.50 {sv['pay']} ({pct(sv['pay'], n)}%)")
    print(f"  Top channel   {sv['top_ch']} {sv['channels'][sv['top_ch']]} · top driver "
          f"{sv['top_dr']} {sv['drivers'][sv['top_dr']]}")
    print(f"  Competitors   median {sgd(comp['median'])} · ladder {sgd(comp['cheapest'][1])}-"
          f"{sgd(comp['dearest'][1])} · Lumo #{comp['lumo_rank']}"
          + (f" (ties at {F['price_can']} with {', '.join(comp['ties'])})" if comp["ties"] else ""))
    print(f"  Top trends    {', '.join(top3)}")
    print("  Budget        " + " · ".join(f"{k}: sheet {sgd0(a)} vs brief {sgd0(b)}"
                                         for k, (a, b) in diff.items()) + "   [deliberate]")
    print("  Captions      " + " · ".join(f"{i}: {', '.join(v)}" for i, v in caps.items()))


if __name__ == "__main__":
    print("Generating Lumo Kopi Co. mock data")
    main()
