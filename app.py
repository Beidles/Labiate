# ============================================================
# LABIATAE (Mint Family) of Turkey - Streamlit Web App
# Based on: Flora of Turkey, Vol. 7 by P.H. Davis
#
# HOW TO RUN:
#   1. Install: pip install streamlit
#   2. Run:     streamlit run app.py
#   3. Opens automatically in your browser!
#
# HOW TO ADD PHOTOS:
#   1. Create a folder called "photos" next to this file
#   2. Put your photo in it, e.g. "photos/ajuga.jpg"
#   3. In PLANTS below, change  "photo": None
#      to  "photo": "photos/ajuga.jpg"
# ============================================================

import streamlit as st   # The library that makes the web app
import random            # Used to shuffle quiz questions
import streamlit.components.v1 as components  # For clipboard JS

# ============================================================
# PAGE SETUP
# st.set_page_config() must be the VERY FIRST streamlit call
# ============================================================

st.set_page_config(
    page_title="Labiatae of Turkey",
    page_icon="🌿",
    layout="wide",
)

# ============================================================
# PLANT DATABASE
# A list of dictionaries. Each dictionary = one plant genus.
# A dictionary is like a labelled box: {"label": value}
# ============================================================

PLANTS = [
    {
        "id": 1, "name": "Ajuga", "common": "Bugle",
        "turkish": "Mayasıl otu",
        "description": "Low-growing herbs. Upper lip of corolla absent or very tiny. Lower lip has 5 lobes.",
        "habitat": "Meadows, roadsides, forest edges",
        "fun_fact": "Used in traditional medicine to treat wounds and fevers.",
        "photo": None,
    },
    {
        "id": 2, "name": "Teucrium", "common": "Germander",
        "turkish": "Kıbrıscık",
        "description": "Herbs or shrubs. Corolla 1-lipped with 5-lobed lower lip. Tube smooth inside.",
        "habitat": "Rocky hillsides, dry grasslands, scrub",
        "fun_fact": "Wall Germander has been used as a medicine since ancient Greek times.",
        "photo": None,
    },
    {
        "id": 3, "name": "Rosmarinus", "common": "Rosemary",
        "turkish": "Biberiye",
        "description": "Evergreen shrub with narrow needle-like leaves. Pale blue flowers. Very aromatic.",
        "habitat": "Dry rocky hillsides near the coast",
        "fun_fact": "Used in cooking worldwide and is a symbol of remembrance.",
        "photo": None,
    },
    {
        "id": 4, "name": "Lavandula", "common": "Lavender",
        "turkish": "Lavanta",
        "description": "Aromatic shrubs with star-shaped or branched hairs. Purple flowers in long spikes.",
        "habitat": "Dry rocky places, cultivated widely",
        "fun_fact": "Turkey is one of the top producers of lavender oil in the world.",
        "photo": None,
    },
    {
        "id": 5, "name": "Prasium", "common": "Prasium",
        "turkish": "Prasiyum",
        "description": "Small evergreen shrub. Shiny fleshy black fruits. White or pale purple flowers.",
        "habitat": "Maquis scrubland near the coast",
        "fun_fact": "One of the few Labiatae with fleshy berries instead of dry nutlets.",
        "photo": None,
    },
    {
        "id": 6, "name": "Scutellaria", "common": "Skullcap",
        "turkish": "Mıknatısotu",
        "description": "Herbs with a unique calyx: the upper lip has a small shield-like flap on top.",
        "habitat": "Moist meadows, stream banks, rocky slopes",
        "fun_fact": "Being studied by scientists for potential use in cancer treatment.",
        "photo": None,
    },
    {
        "id": 7, "name": "Melittis", "common": "Bastard Balm",
        "turkish": "Arınanesi",
        "description": "Large showy flowers up to 35 mm in upper leaf axils. Strongly honey-scented.",
        "habitat": "Shaded woodland, forest edges",
        "fun_fact": "Its name comes from the Greek word for bee — bees love its flowers.",
        "photo": None,
    },
    {
        "id": 8, "name": "Eremostachys", "common": "Desert Candle",
        "turkish": "Çöl şamdanı",
        "description": "Tall woolly herbs. Yellow upper lip, orange lower lip. Very distinctive!",
        "habitat": "Dry steppe and semi-desert areas of eastern Turkey",
        "fun_fact": "Can grow over 1 metre tall and is hard to miss on the dry steppes.",
        "photo": None,
    },
    {
        "id": 9, "name": "Phlomis", "common": "Jerusalem Sage",
        "turkish": "Şalba / Fener otu",
        "description": "Woolly herbs or shrubs. Upper lip of corolla strongly curved like a hood (falcate).",
        "habitat": "Rocky slopes, scrub, dry hills",
        "fun_fact": "In Turkey, leaves are dried and made into herbal tea called 'dağ çayı'.",
        "photo": None,
    },
    {
        "id": 10, "name": "Lamium", "common": "Dead Nettle",
        "turkish": "Ballıbaba",
        "description": "Herbs that look like nettles but DO NOT sting! White, pink, or purple flowers.",
        "habitat": "Roadsides, disturbed ground, gardens",
        "fun_fact": "White Dead Nettle flowers are edible and can be added to salads.",
        "photo": None,
    },
    {
        "id": 11, "name": "Wiedemannia", "common": "Wiedemannia",
        "turkish": "Wiedemannya",
        "description": "Similar to Prunella. Pinkish flowers with a very hairy upper lip.",
        "habitat": "Moist mountain slopes, stream sides",
        "fun_fact": "Named after German botanist E.J. von Wiedemann who worked in Istanbul.",
        "photo": None,
    },
    {
        "id": 12, "name": "Galeobdolon", "common": "Yellow Archangel",
        "turkish": "Sarı ölü ısırgan",
        "description": "Spreads by runners (stoloniferous). Yellow flowers. Smooth thecae.",
        "habitat": "Shaded woodland, hedgerows",
        "fun_fact": "Its runners can spread metres from the parent plant, carpeting the woodland floor.",
        "photo": None,
    },
    {
        "id": 13, "name": "Galeopsis", "common": "Hemp Nettle",
        "turkish": "Kenevir ısırganı",
        "description": "Annual herbs with spiny bracteoles. Lower lip has 2 bump-like appendages at base.",
        "habitat": "Arable fields, disturbed ground",
        "fun_fact": "One of the first plants used to demonstrate polyploidy in genetics.",
        "photo": None,
    },
    {
        "id": 14, "name": "Leonurus", "common": "Motherwort",
        "turkish": "Oğulotu",
        "description": "Tall herbs with deeply divided hand-shaped leaves. Small pinkish-white flowers.",
        "habitat": "Roadsides, waste places, near villages",
        "fun_fact": "Used for centuries to calm the heart. Modern research confirms it has heart benefits.",
        "photo": None,
    },
    {
        "id": 15, "name": "Moluccella", "common": "Bells of Ireland",
        "turkish": "Zil çiçeği",
        "description": "The calyx is HUGE and bell-shaped. Small white flowers inside. Very unusual!",
        "habitat": "Disturbed ground, field margins",
        "fun_fact": "Despite the name 'Bells of Ireland', it is actually native to Turkey and Syria!",
        "photo": None,
    },
    {
        "id": 16, "name": "Ballota", "common": "Black Horehound",
        "turkish": "Ballota",
        "description": "Woolly herbs. Calyx tube widens into a toothed flat star-like limb after flowering.",
        "habitat": "Roadsides, rocky slopes, waste ground",
        "fun_fact": "Its strong smell stops animals from eating it — a built-in pest repellent!",
        "photo": None,
    },
    {
        "id": 17, "name": "Marrubium", "common": "Horehound",
        "turkish": "Topalak",
        "description": "White-woolly herbs. Calyx has 5-10 hook-like teeth. Stamens hidden inside tube.",
        "habitat": "Dry roadsides, overgrazed areas, waste ground",
        "fun_fact": "Horehound candy and tea are traditional cough remedies still sold today!",
        "photo": None,
    },
    {
        "id": 18, "name": "Sideritis", "common": "Mountain Tea",
        "turkish": "Dağ çayı",
        "description": "Herbs or small shrubs, often silvery-woolly. Bracts often leaf-like and spiny.",
        "habitat": "Rocky mountain slopes, limestone cliffs",
        "fun_fact": "Sideritis tea (dağ çayı) is extremely popular in Turkey for health and enjoyment.",
        "photo": None,
    },
    {
        "id": 19, "name": "Stachys", "common": "Woundwort",
        "turkish": "Karabaş",
        "description": "Herbs or shrubs. Calyx with 5 teeth. One of the LARGEST genera in Turkish Labiatae.",
        "habitat": "Meadows, forests, rocky slopes, roadsides",
        "fun_fact": "Turkey has more species of Stachys than almost any other country in the world.",
        "photo": None,
    },
    {
        "id": 20, "name": "Melissa", "common": "Lemon Balm",
        "turkish": "Melisa / Oğul otu",
        "description": "Lemon-scented herb. White or pale pink small flowers. Leaves smell strongly of lemon.",
        "habitat": "Woodland edges, hedgerows, stream banks",
        "fun_fact": "Lemon Balm tea is popular in Turkey for calming nerves and helping with sleep.",
        "photo": None,
    },
    {
        "id": 21, "name": "Nepeta", "common": "Catmint",
        "turkish": "Kedi nanesi",
        "description": "Blue or white flowers. Many-flowered clusters not in leaf axils.",
        "habitat": "Dry rocky slopes, roadsides",
        "fun_fact": "Cats go wild for catnip (Nepeta cataria) because it mimics cat pheromones!",
        "photo": None,
    },
    {
        "id": 22, "name": "Glechoma", "common": "Ground Ivy",
        "turkish": "Yer sarmaşığı",
        "description": "Creeping herb with round scalloped leaves. Spreads by stolons (ground runners).",
        "habitat": "Shaded moist places, hedgerows, lawns",
        "fun_fact": "Before hops were used, Ground Ivy was the main flavouring in European beer!",
        "photo": None,
    },
    {
        "id": 23, "name": "Dracocephalum", "common": "Dragonhead",
        "turkish": "Ejderha başı",
        "description": "Blue-purple flowers. Bracteoles have pointed tips. Perennial herbs.",
        "habitat": "Mountain steppes, rocky slopes",
        "fun_fact": "The name means 'dragon head' in Greek — the flowers look like a dragon's mouth!",
        "photo": None,
    },
    {
        "id": 24, "name": "Lallemantia", "common": "Lallemantia",
        "turkish": "Lallemantia",
        "description": "Unique: upper lip of corolla has 2 internal folds. Bracteoles prominently veined.",
        "habitat": "Arable fields, dry disturbed ground",
        "fun_fact": "Seeds contain an oil used in traditional medicine and as food in Central Asia.",
        "photo": None,
    },
    {
        "id": 25, "name": "Hymenocrater", "common": "Hymenocrater",
        "turkish": "Hymenocrater",
        "description": "Shrub with striking violet upside-down (resupinate) corollas. Leaf-like bracteoles.",
        "habitat": "Rocky slopes and cliffs in eastern Turkey",
        "fun_fact": "Resupinate means the flower is twisted 180 degrees — the top is actually the bottom!",
        "photo": None,
    },
    {
        "id": 26, "name": "Hyssopus", "common": "Hyssop",
        "turkish": "Çördük / Hisop",
        "description": "Small aromatic shrub. Tubular calyx with thickened folds. Violet-blue corolla.",
        "habitat": "Dry rocky slopes, scrub",
        "fun_fact": "Hyssop is mentioned in the Bible as a purifying herb used in ancient rituals.",
        "photo": None,
    },
    {
        "id": 27, "name": "Prunella", "common": "Selfheal",
        "turkish": "Ölmez otu",
        "description": "Dense terminal flower heads. Violet flowers. Calyx clearly 2-lipped (bilabiate).",
        "habitat": "Meadows, roadsides, lawns, open woodland",
        "fun_fact": "Selfheal was used to heal wounds — modern science confirms it has antimicrobial compounds.",
        "photo": None,
    },
    {
        "id": 28, "name": "Origanum", "common": "Oregano",
        "turkish": "Kekik / Mercanköşk",
        "description": "Aromatic herb. Flowers in panicles or corymbs. Prominent bracts hide the flowers.",
        "habitat": "Dry rocky hillsides, scrub",
        "fun_fact": "Turkey exports huge amounts of oregano (kekik). Essential in Turkish cuisine!",
        "photo": None,
    },
    {
        "id": 29, "name": "Pentapleura", "common": "Pentapleura",
        "turkish": "Pentapleura",
        "description": "A rare genus found only in a small area of Turkey. Related to Hyssopus.",
        "habitat": "Rocky limestone areas in southern Turkey",
        "fun_fact": "Pentapleura subulifera is endemic to Turkey — it grows NOWHERE else in the world!",
        "photo": None,
    },
    {
        "id": 30, "name": "Satureja", "common": "Savory",
        "turkish": "Sater",
        "description": "Small aromatic herbs or shrubs. Leaves often cuneate (wedge-shaped) at the base.",
        "habitat": "Rocky limestone slopes, dry hillsides",
        "fun_fact": "Summer Savory is used as a spice, especially to flavour bean dishes.",
        "photo": None,
    },
    {
        "id": 31, "name": "Calamintha", "common": "Calamint",
        "turkish": "Yaban nanesi",
        "description": "Mint-like herbs. Lower calyx lip teeth clearly fringed with hairs (ciliate).",
        "habitat": "Rocky slopes, forest edges, scrub",
        "fun_fact": "Smells like a mix of mint and thyme and is sometimes used to make herbal tea.",
        "photo": None,
    },
    {
        "id": 32, "name": "Clinopodium", "common": "Wild Basil",
        "turkish": "Yaban fesleğeni",
        "description": "Hairy herbs. Calyx tube strongly curved. Teeth long and hair-fringed (ciliate).",
        "habitat": "Hedgerows, woodland edges, scrub",
        "fun_fact": "Called 'Wild Basil' but is not culinary basil — though it does smell similar!",
        "photo": None,
    },
    {
        "id": 33, "name": "Acinos", "common": "Basil Thyme",
        "turkish": "Akinos",
        "description": "Small herbs. Calyx tube gibbous (swollen and humped) at the base.",
        "habitat": "Dry grassland, arable fields, rocky slopes",
        "fun_fact": "Despite the name 'Basil Thyme', it is neither a basil nor a thyme!",
        "photo": None,
    },
    {
        "id": 34, "name": "Micromeria", "common": "Micromeria",
        "turkish": "Küçük nane",
        "description": "Small aromatic herbs. Calyx 1.5-6 mm, 13-15 veined. Corolla tube stays inside calyx.",
        "habitat": "Rocky limestone cliffs, walls, scrub",
        "fun_fact": "Some species are used to make herbal tea, collected from wild plants in Turkey.",
        "photo": None,
    },
    {
        "id": 35, "name": "Cyclotrichium", "common": "Cyclotrichium",
        "turkish": "Silindir tüylü",
        "description": "Shrubby herbs with star-shaped hairs. Stamens stick out beyond the upper lip.",
        "habitat": "Rocky slopes in eastern Anatolia",
        "fun_fact": "A genus found mainly in Turkey and Iran — quite rare globally.",
        "photo": None,
    },
    {
        "id": 36, "name": "Thymus", "common": "Thyme",
        "turkish": "Kekik",
        "description": "Small aromatic shrubs. Woody base, tiny leaves. Pink or purple flowers. Very fragrant!",
        "habitat": "Dry rocky hillsides, grasslands, mountain slopes",
        "fun_fact": "Turkey has over 50 species of wild thyme — more than any other country!",
        "photo": None,
    },
    {
        "id": 37, "name": "Coridothymus", "common": "Cretan Thyme",
        "turkish": "Kekik (Girit)",
        "description": "Thyme-like shrub. Inflorescence is a HEAD (not a spike). Calyx has 20-22 veins.",
        "habitat": "Rocky coastal areas",
        "fun_fact": "Produces a high-quality essential oil used in perfumes and medicines.",
        "photo": None,
    },
    {
        "id": 38, "name": "Thymbra", "common": "Za'atar",
        "turkish": "Zahter",
        "description": "Thyme-like shrub. Inflorescence is a SPIKE. Calyx 13-veined. Leaves folded (conduplicate).",
        "habitat": "Rocky limestone hillsides in southern Turkey",
        "fun_fact": "Thymbra spicata is the famous za'atar of the Middle East, used in the popular spice blend.",
        "photo": None,
    },
    {
        "id": 39, "name": "Mentha", "common": "Mint",
        "turkish": "Nane",
        "description": "Creeping herbs in moist places. Corolla has 4 EQUAL lobes — unusual for Labiatae!",
        "habitat": "Stream banks, ditches, wet meadows",
        "fun_fact": "Mint tea (nane çayı) is one of Turkey's most beloved drinks!",
        "photo": None,
    },
    {
        "id": 40, "name": "Lycopus", "common": "Gipsywort",
        "turkish": "Kurt ayağı",
        "description": "Herb of wet places. Deeply toothed leaves. Non-aromatic. Tiny white flowers.",
        "habitat": "Riverbanks, marshes, wet meadows",
        "fun_fact": "Historically used to dye fabric black.",
        "photo": None,
    },
    {
        "id": 41, "name": "Ziziphora", "common": "Ziziphora",
        "turkish": "Zizifora",
        "description": "Small aromatic herbs. Cuneate-based leaves. Dense head or spike inflorescence.",
        "habitat": "Dry steppe, rocky slopes",
        "fun_fact": "Used in traditional medicine across Turkey and Central Asia for digestive problems.",
        "photo": None,
    },
    {
        "id": 42, "name": "Salvia", "common": "Sage",
        "turkish": "Adaçayı",
        "description": "LARGEST genus in Turkish Labiatae! Unique lever-like stamens. Incredibly diverse.",
        "habitat": "Rocky slopes, scrub, meadows, forests",
        "fun_fact": "Turkey has about 100 species of wild sage! Adaçayı is Turkey's most famous herbal tea.",
        "photo": None,
    },
    {
        "id": 43, "name": "Dorystoechas", "common": "Dorystoechas",
        "turkish": "Dorystoechas",
        "description": "Woody shrub with arrow-shaped (hastate) leaves and slender cylindrical spikes.",
        "habitat": "Rocky hillsides in southwestern Turkey",
        "fun_fact": "Dorystoechas hastata is ENDEMIC to Turkey — it exists nowhere else on Earth!",
        "photo": None,
    },
    {
        "id": 44, "name": "Elsholtzia", "common": "Elsholtzia",
        "turkish": "Elşoltsiya",
        "description": "Annual or short-lived herb. Inflorescence a one-sided spike. Stamens droop downward.",
        "habitat": "Disturbed ground, roadsides, cultivated areas",
        "fun_fact": "In China, Elsholtzia ciliata is used as a spice and a cold remedy.",
        "photo": None,
    },
    {
        "id": 45, "name": "Ocimum", "common": "Basil",
        "turkish": "Fesleğen",
        "description": "Annual herb. Calyx bends back (deflexed) in fruit. Upper calyx lip broadly circular.",
        "habitat": "Cultivated, occasionally naturalised",
        "fun_fact": "Sweet Basil is one of the world's most important culinary herbs, originally from tropical Asia.",
        "photo": None,
    },
]

# ============================================================
# IDENTIFICATION KEY
# Each step has:
#   "q"    = the question to ask
#   "a"    = option A text
#   "b"    = option B text
#   "next_a" = where A leads: ("step", "s2") or ("plant", 42)
#   "next_b" = where B leads: ("step", "s6") or ("plant", 1)
# ============================================================

KEY = {
    "s1":  {"q": "How many FERTILE stamens does the flower have?",
            "a": "2 stamens — the other pair is tiny or missing",
            "b": "4 stamens — or all reduced/sterile",
            "next_a": ("step", "s2"), "next_b": ("step", "s6")},

    "s2":  {"q": "Are the 2 stamens LEVER-LIKE — connectives long like a see-saw?",
            "a": "YES — connectives long and lever-like",
            "b": "NO — connectives very short, not lever-like",
            "next_a": ("plant", 42), "next_b": ("step", "s3")},

    "s3":  {"q": "Are the leaves EVERGREEN and NARROW like a needle?",
            "a": "YES — evergreen, narrow leaves; pale blue corolla; woody shrub",
            "b": "NO — leaves deciduous or broader",
            "next_a": ("plant", 3), "next_b": ("step", "s4")},

    "s4":  {"q": "Where are the FLOWER CLUSTERS?",
            "a": "In upper LEAF AXILS, widely spaced; leaves coarsely toothed; non-aromatic",
            "b": "In TERMINAL SPIKES or HEADS; entire margins; aromatic",
            "next_a": ("plant", 40), "next_b": ("step", "s5")},

    "s5":  {"q": "Is the plant a WOODY SHRUB with arrow-shaped (hastate) leaves?",
            "a": "YES — woody shrub; hastate leaves; slender cylindrical spikes",
            "b": "NO — herb; cuneate-based leaves; head or spike inflorescence",
            "next_a": ("plant", 43), "next_b": ("plant", 41)},

    "s6":  {"q": "Is the UPPER LIP of the corolla present?",
            "a": "NO — upper lip absent or very tiny (flower looks 1-lipped)",
            "b": "YES — upper lip clearly present",
            "next_a": ("step", "s7"), "next_b": ("step", "s8")},

    "s7":  {"q": "Is the inside of the COROLLA TUBE smooth (glabrous)?",
            "a": "YES — tube smooth; lower lip with 5 lobes",
            "b": "NO — tube has a ring of hairs inside",
            "next_a": ("plant", 2), "next_b": ("plant", 1)},

    "s8":  {"q": "What type of HAIRS does the plant have?",
            "a": "BRANCHED — tree-like, forked, or star-shaped (stellate)",
            "b": "SIMPLE (unbranched) only, or NO hairs at all",
            "next_a": ("step", "s9"), "next_b": ("step", "s14")},

    "s9":  {"q": "How are the flower clusters arranged?",
            "a": "In PEDUNCULATE SPIKES; upper calyx has an appendage; stamens droop downward",
            "b": "NOT in pedunculate spikes; no calyx appendage; stamens not drooping",
            "next_a": ("plant", 4), "next_b": ("step", "s10")},

    "s10": {"q": "Do STAMENS stick out clearly beyond the upper lip?",
            "a": "YES — stamens clearly exserted; corolla resupinate (upside-down)",
            "b": "NO — stamens do not stick out beyond the upper lip",
            "next_a": ("plant", 35), "next_b": ("step", "s11")},

    "s11": {"q": "Is the upper lip FALCATE — curved like a sickle or hood?",
            "a": "YES — upper lip clearly curved or hooded",
            "b": "NO — upper lip straight or slightly concave",
            "next_a": ("plant", 9), "next_b": ("step", "s12")},

    "s12": {"q": "How many CALYX TEETH? What are the HAIRS inside the calyx throat?",
            "a": "5 teeth; calyx throat smooth or weakly hairy",
            "b": "5-10 teeth; stiff long white hairs in the calyx throat",
            "next_a": ("plant", 19), "next_b": ("step", "s13")},

    "s13": {"q": "Are STAMENS hidden (included) inside the corolla tube?",
            "a": "YES — stamens hidden inside tube; calyx not widened above",
            "b": "NO — calyx tube widens into a flat star-like toothed limb",
            "next_a": ("plant", 17), "next_b": ("plant", 16)},

    "s14": {"q": "Is the FRUITING CALYX greatly enlarged and papery with broad spreading lobes?",
            "a": "YES — fruiting calyx greatly enlarged and papery",
            "b": "NO — calyx not papery with broad lobes",
            "next_a": ("step", "s15"), "next_b": ("step", "s17")},

    "s15": {"q": "What colour are the COROLLA LIPS?",
            "a": "Upper lip YELLOW, lower lip orange; leaves woolly",
            "b": "Corolla white, pink, or violet; leaves smooth",
            "next_a": ("plant", 8), "next_b": ("step", "s16")},

    "s16": {"q": "Is the plant a SHRUB with violet UPSIDE-DOWN (resupinate) corollas?",
            "a": "YES — shrub; violet resupinate corollas; bracteoles herbaceous",
            "b": "NO — annual; white/pinkish corollas; bracteoles spiny",
            "next_a": ("plant", 25), "next_b": ("plant", 15)},

    "s17": {"q": "How many VEINS does the CALYX TUBE have?",
            "a": "15 or more veins; upper stamens LONGER than lower",
            "b": "5-14 veins; lower stamens LONGER than upper, or equal",
            "next_a": ("step", "s18"), "next_b": ("step", "s21")},

    "s18": {"q": "Do the CALYX SINUSES have a thickened fold at the base?",
            "a": "YES — thickened fold present; middle lobe of upper lip broader",
            "b": "NO — no thickened fold; lobes similar in width",
            "next_a": ("step", "s19"), "next_b": ("step", "s20")},

    "s19": {"q": "Does the UPPER LIP of the corolla have 2 internal longitudinal folds?",
            "a": "YES — 2 internal folds; bracteoles prominently veined",
            "b": "NO — no internal folds; bracteoles aristate or acuminate",
            "next_a": ("plant", 24), "next_b": ("plant", 23)},

    "s20": {"q": "Are flower clusters 2-6-flowered and one-sided? Does the plant spread by stolons (runners)?",
            "a": "YES — 2-6 flowered, one-sided, spreads by stolons",
            "b": "NO — 6+ flowered; NOT in leaf axils; not stoloniferous",
            "next_a": ("plant", 22), "next_b": ("plant", 21)},

    "s21": {"q": "Is the COROLLA TUBE long, slender, and S-shaped (sigmoid)?",
            "a": "YES — long slender S-shaped tube; upper calyx has a small flap",
            "b": "NO — corolla tube not like that; calyx without a flap",
            "next_a": ("plant", 6), "next_b": ("step", "s22")},

    "s22": {"q": "Is the upper lip FALCATE — curved like a sickle or hood?",
            "a": "YES — upper lip clearly falcate (curved)",
            "b": "NO — upper lip straight or slightly concave",
            "next_a": ("step", "s23"), "next_b": ("step", "s29")},

    "s23": {"q": "Is the calyx CLEARLY 2-LIPPED (bilabiate)?",
            "a": "YES — calyx clearly 2-lipped",
            "b": "NO — calyx not or indistinctly 2-lipped",
            "next_a": ("step", "s24"), "next_b": ("step", "s25")},

    "s24": {"q": "Are flower clusters in DENSE TERMINAL SPIKES with bracts hiding the calyces?",
            "a": "YES — dense terminal spikes; bracts hide calyces; flowers violet",
            "b": "NO — clusters distant; bracts do NOT hide calyces; flowers pinkish",
            "next_a": ("plant", 27), "next_b": ("plant", 11)},

    "s25": {"q": "Do the NUTLETS (small fruits) have TUFTS OF HAIR at the tip?",
            "a": "YES — nutlets have hair tufts at the apex",
            "b": "NO — nutlets are smooth (glabrous)",
            "next_a": ("step", "s26"), "next_b": ("step", "s27")},

    "s26": {"q": "How big is the corolla?",
            "a": "Corolla 5-12 mm, pinkish-white; leaves digitately divided",
            "b": "Corolla 18-40 mm, yellow or whitish; leaves pinnate or lobed",
            "next_a": ("plant", 14), "next_b": ("plant", 8)},

    "s27": {"q": "Are the THECAE (pollen sacs) smooth? Is the corolla yellow? Does the plant spread by runners?",
            "a": "YES — smooth thecae; yellow corolla; plant stoloniferous",
            "b": "NO — thecae hairy; corolla white, cream, pink, or purple",
            "next_a": ("plant", 12), "next_b": ("step", "s28")},

    "s28": {"q": "Are the BRACTEOLES SPINY?",
            "a": "YES — bracteoles spiny; lower lip with 2 blunt conical appendages",
            "b": "NO — bracteoles not spiny; lower lip with reduced lateral lobes",
            "next_a": ("plant", 13), "next_b": ("plant", 10)},

    "s29": {"q": "Do STAMENS stick out clearly beyond the upper lip?",
            "a": "YES — stamens clearly exserted beyond the upper lip",
            "b": "NO — stamens do not stick out beyond the upper lip",
            "next_a": ("step", "s30"), "next_b": ("step", "s39")},

    "s30": {"q": "Is the calyx CLEARLY 2-LIPPED?",
            "a": "YES — clearly 2-lipped; lower teeth very different from upper",
            "b": "NO — calyx not or indistinctly 2-lipped",
            "next_a": ("step", "s31"), "next_b": ("step", "s35")},

    "s31": {"q": "Is the plant an ANNUAL? Do the stamens droop (declinate)?",
            "a": "YES — annual or short-lived perennial; stamens droop downward",
            "b": "NO — shrub or woody-based perennial; stamens not drooping",
            "next_a": ("step", "s32"), "next_b": ("step", "s33")},

    "s32": {"q": "Is the calyx BENT BACK (deflexed) in fruit? Is the upper calyx lip broadly circular?",
            "a": "YES — calyx deflexed in fruit; upper lip broadly circular",
            "b": "NO — calyx not deflexed; inflorescence a spike",
            "next_a": ("plant", 45), "next_b": ("plant", 44)},

    "s33": {"q": "Is the calyx tube DORSALLY COMPRESSED with 2 fringed flanges on the sides?",
            "a": "YES — calyx tube dorsally compressed with 2 ciliolate flanges",
            "b": "NO — calyx tube not dorsally flattened; no flanges",
            "next_a": ("step", "s34"), "next_b": ("plant", 36)},

    "s34": {"q": "What is the INFLORESCENCE TYPE?",
            "a": "SPICATE (a spike); calyx 13-veined; leaves folded (conduplicate)",
            "b": "CAPITATE (a head); calyx 20-22-veined; leaves subtriquetrious",
            "next_a": ("plant", 38), "next_b": ("plant", 37)},

    "s35": {"q": "Is the inflorescence in PANICLES or CORYMBS with prominent bracts hiding the calyces?",
            "a": "YES — panicles or corymbs; prominent bracts hiding calyces",
            "b": "NO — bracts inconspicuous; not hiding calyces",
            "next_a": ("plant", 28), "next_b": ("step", "s36")},

    "s36": {"q": "Does the corolla have 4 NEARLY EQUAL LOBES? Does the plant grow in DAMP places?",
            "a": "YES — 4 subequal lobes; damp habitat; rhizomes root at nodes",
            "b": "NO — 5 unequal lobes; dry places; no creeping rhizomes",
            "next_a": ("plant", 39), "next_b": ("step", "s37")},

    "s37": {"q": "Are the leaves OVATE to SUBORBICULAR? Is the corolla resupinate (upside-down)?",
            "a": "YES — leaves ovate to suborbicular; corolla resupinate; thecae parallel",
            "b": "NO — leaves linear to linear-lanceolate; thecae divergent",
            "next_a": ("plant", 35), "next_b": ("step", "s38")},

    "s38": {"q": "Is the calyx tubular (6-8 mm) with thickened folds at the base of the sinuses?",
            "a": "YES — tubular, 6-8 mm; thickened folds; corolla violet-blue",
            "b": "NO — ovate-campanulate, 3-4 mm; no thickened folds; corolla white",
            "next_a": ("plant", 26), "next_b": ("plant", 30)},

    "s39": {"q": "Does the CALYX THROAT have a BEARD of stiff, thick white hairs?",
            "a": "YES — calyx throat has a beard of stiff thick white hairs",
            "b": "NO — calyx throat smooth or with only a few weak hairs",
            "next_a": ("step", "s40"), "next_b": ("step", "s52")},

    "s40": {"q": "Does the corolla have 4 NEARLY EQUAL LOBES? Does the plant grow in DAMP places?",
            "a": "YES — 4 subequal lobes; damp places; rhizomes rooting at nodes",
            "b": "NO — 5 unequal lobes; dry places; procumbent or erect",
            "next_a": ("plant", 39), "next_b": ("step", "s41")},

    "s41": {"q": "Is the calyx dorsally COMPRESSED with 2 lateral fringed (ciliolate) flanges?",
            "a": "YES — calyx compressed; 2 ciliolate flanges",
            "b": "NO — calyx not dorsally flattened; no flanges",
            "next_a": ("step", "s42"), "next_b": ("step", "s43")},

    "s42": {"q": "What is the INFLORESCENCE TYPE?",
            "a": "SPICATE (spike); calyx 13-veined; leaves conduplicate",
            "b": "CAPITATE (head); calyx 20-22-veined; leaves triquetrious",
            "next_a": ("plant", 38), "next_b": ("plant", 37)},

    "s43": {"q": "Is the inflorescence in PANICLES or CORYMBS with prominent bracts hiding the calyces?",
            "a": "YES — panicles or corymbs; prominent bracts hiding calyces",
            "b": "NO — bracts inconspicuous; not hiding calyces",
            "next_a": ("plant", 28), "next_b": ("step", "s44")},

    "s44": {"q": "Do ALL parts of the plant have LONG, STURDY HAIRS? Do the calyces have 10-20 ribs?",
            "a": "YES — long sturdy hairs throughout; calyces 10-20-ribbed",
            "b": "NO — hairs short or crisp; calyces 5-13-veined",
            "next_a": ("step", "s45"), "next_b": ("step", "s46")},

    "s45": {"q": "Are STAMENS INSIDE (included in) the corolla tube?",
            "a": "YES — stamens inside tube; calyx not widened above",
            "b": "NO — calyx tube widens into a flat toothed limb",
            "next_a": ("plant", 17), "next_b": ("plant", 16)},

    "s46": {"q": "Are the LOWER CALYX TEETH long, awl-shaped, AND prominently fringed with hairs?",
            "a": "YES — lower teeth long-subulate, prominently ciliate",
            "b": "NO — lower teeth shorter; leaves without basal cilia",
            "next_a": ("plant", 36), "next_b": ("step", "s47")},

    "s47": {"q": "Is the CALYX TUBE strongly CURVED or gibbous (humped) below?",
            "a": "YES — calyx tube strongly curved or gibbous below",
            "b": "NO — calyx tube roughly straight",
            "next_a": ("step", "s48"), "next_b": ("step", "s49")},

    "s48": {"q": "Is the calyx tube strongly CURVED with long hair-fringed teeth? Are they perennials?",
            "a": "YES — tube strongly curved; teeth long-ciliate; perennials",
            "b": "NO — tube gibbous (humped) below, constricted above",
            "next_a": ("plant", 32), "next_b": ("plant", 33)},

    "s49": {"q": "Are the LOWER CALYX LIP TEETH clearly fringed with hairs (ciliate)?",
            "a": "YES — lower lip teeth clearly ciliate; leaves petiolate",
            "b": "NO — lower lip teeth not or scarcely ciliate; leaves petiolate or subsessile",
            "next_a": ("plant", 31), "next_b": ("step", "s50")},

    "s50": {"q": "Are leaves SUBSESSILE and CUNEATE (wedge-shaped), folded when young? Calyx 10-13-veined?",
            "a": "YES — subsessile, cuneate, conduplicate when young; calyx 10-13-veined",
            "b": "NO — leaves petiolate, flat; calyx 5-13-veined; stamens parallel",
            "next_a": ("plant", 30), "next_b": ("step", "s51")},

    "s51": {"q": "Is the calyx 1.5-6 mm with 13-15 veins, with the corolla tube INSIDE the calyx?",
            "a": "YES — calyx 1.5-6 mm, 13-15-veined; corolla tube inside calyx",
            "b": "NO — calyx 6+ mm, 5-10-veined; corolla tube sticks out",
            "next_a": ("plant", 34), "next_b": ("plant", 19)},

    "s52": {"q": "Are the BRACTEOLES awl-shaped, spiny, and bent back (deflexed)?",
            "a": "YES — awl-shaped, spiny, deflexed bracteoles; upper calyx rigid with 1 large spine",
            "b": "NO — bracteoles herbaceous (leaf-like), erect or spreading",
            "next_a": ("plant", 15), "next_b": ("step", "s53")},

    "s53": {"q": "Is the calyx CLEARLY 2-LIPPED (bilabiate)?",
            "a": "YES — calyx clearly 2-lipped",
            "b": "NO — calyx not or indistinctly 2-lipped",
            "next_a": ("step", "s54"), "next_b": ("step", "s58")},

    "s54": {"q": "Is the plant a SHRUB with fleshy BLACK fruit in terminal leafy racemes?",
            "a": "YES — shrub; nearly glabrous; terminal leafy racemes; fleshy black fruit",
            "b": "NO — herbs; prominent hairs; fruit dry",
            "next_a": ("plant", 5), "next_b": ("step", "s55")},

    "s55": {"q": "Are the flowers in UPPER LEAF AXILS?",
            "a": "YES — flowers in upper leaf axils",
            "b": "NO — flowers in axils of BRACTS that are different from the leaves",
            "next_a": ("step", "s56"), "next_b": ("step", "s57")},

    "s56": {"q": "How large is the COROLLA?",
            "a": "About 35 mm (large!); pedicels 6-8 mm",
            "b": "About 8-15 mm (smaller); pedicels about 3 mm",
            "next_a": ("plant", 7), "next_b": ("plant", 20)},

    "s57": {"q": "Are the leaves SUBSESSILE and cuneate, conduplicate when young, glandular-punctate?",
            "a": "YES — subsessile, cuneate, conduplicate, glandular; calyx 10-13-veined",
            "b": "NO — leaves petiolate, ovate to oblong; calyx 5-10-veined",
            "next_a": ("plant", 30), "next_b": ("plant", 18)},

    "s58": {"q": "Is the inflorescence in PANICLES or CORYMBS with prominent bracts hiding the calyces?",
            "a": "YES — panicles or corymbs; prominent bracts hiding calyces",
            "b": "NO — bracts inconspicuous",
            "next_a": ("plant", 28), "next_b": ("step", "s59")},

    "s59": {"q": "Does the corolla have 4 NEARLY EQUAL LOBES? Does the plant grow in DAMP places?",
            "a": "YES — 4 subequal lobes; damp places; rhizomes rooting at nodes",
            "b": "NO — 5 unequal lobes; dry places",
            "next_a": ("plant", 39), "next_b": ("step", "s60")},

    "s60": {"q": "Do ALL parts of the plant have LONG STURDY HAIRS? Do the calyces have 10-20 ribs?",
            "a": "YES — long sturdy hairs throughout; calyces 10-20-ribbed",
            "b": "NO — hairs shorter; calyces fewer-ribbed",
            "next_a": ("plant", 17), "next_b": ("plant", 19)},
}

# ============================================================
# HELPER — look up a plant by its ID number
# ============================================================

def copy_to_clipboard_button(text, key="copy"):
    """Render an HTML button that copies `text` to the clipboard."""
    # Escape for safe JS string embedding
    safe = text.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
    components.html(
        f"""
        <button
            onclick="navigator.clipboard.writeText('{safe}')
                     .then(()=>{{this.textContent='✅ Copied!';
                                setTimeout(()=>this.textContent='📋 Copy plant info',2000);}});"
            style="background:#4CAF50;color:white;border:none;padding:8px 18px;
                   border-radius:6px;cursor:pointer;font-size:14px;margin-top:6px;">
            📋 Copy plant info
        </button>
        """,
        height=50,
    )


def get_plant(plant_id):
    # Go through the list and return the one with the matching id
    for p in PLANTS:
        if p["id"] == plant_id:
            return p
    return None   # If not found (should never happen)

# ============================================================
# HELPER — show a plant card (used in Browse and Identify tabs)
# ============================================================

def show_plant_card(plant):
    """Display all the information about one plant genus."""

    # Photo — show it if a filename is set, otherwise show a placeholder
    if plant["photo"]:
        st.image(plant["photo"], use_container_width=True)
    else:
        # A friendly placeholder when no photo is available yet
        st.info("📷 No photo yet — add one by putting a .jpg in the photos/ folder "
                "and updating this plant's 'photo' field in app.py")

    # Green header box
    st.markdown(
        f"""
        <div style="background:#e8f5e9; padding:16px; border-radius:10px; margin-bottom:12px;">
            <small style="color:#555;">Genus {plant['id']}</small><br>
            <span style="font-size:1.8em; font-weight:bold; font-style:italic;">{plant['name']}</span><br>
            <span style="font-size:1.2em; color:#444;">{plant['common']}</span><br>
            <span style="color:green;">🇹🇷 {plant['turkish']}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Three info cards side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🌿 Key Features**")
        st.write(plant["description"])
    with col2:
        st.markdown("**⛰️ Habitat in Turkey**")
        st.write(plant["habitat"])
    with col3:
        st.markdown("**⭐ Fun Fact**")
        st.write(plant["fun_fact"])

    st.caption("Source: Flora of Turkey, Vol. 7 — P.H. Davis")

    # --- Copy to clipboard ---
    plant_text = (
        f"{plant['name']} ({plant['common']}) — {plant['turkish']}\n"
        f"Key Features: {plant['description']}\n"
        f"Habitat: {plant['habitat']}\n"
        f"Fun Fact: {plant['fun_fact']}\n"
        f"Source: Flora of Turkey, Vol. 7 — P.H. Davis"
    )
    copy_to_clipboard_button(plant_text, key=f"copy_{plant['id']}")

# ============================================================
# SESSION STATE SETUP
# Streamlit reruns the whole script every time you click a
# button. 'st.session_state' is like a memory that survives
# between reruns — it remembers values like your quiz score.
# ============================================================

# Set up Identify tab memory (only on first ever load)
if "key_step" not in st.session_state:
    st.session_state.key_step = "s1"        # Start at question 1
if "key_plant" not in st.session_state:
    st.session_state.key_plant = None       # No plant found yet
if "key_history" not in st.session_state:
    st.session_state.key_history = []       # History for Back button
if "key_count" not in st.session_state:
    st.session_state.key_count = 0          # How many questions answered

# Set up Quiz tab memory
if "quiz_plants" not in st.session_state:
    st.session_state.quiz_plants = []
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_guess" not in st.session_state:
    st.session_state.quiz_guess = ""
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

# ============================================================
# APP TITLE
# ============================================================

st.title("🌿 Labiatae of Turkey")
st.caption("45 genera of the Mint Family · Based on Flora of Turkey, Vol. 7 · P.H. Davis")

# ============================================================
# TABS — the four sections of the app
# ============================================================

tab_browse, tab_identify, tab_search, tab_quiz, tab_swift = st.tabs(
    ["📋 Browse", "🔍 Identify", "🔎 Search", "❓ Quiz", "📱 Swift Code"]
)

# ============================================================
# TAB 1: BROWSE
# Shows all 45 genera in a list. Click one to see details.
# ============================================================

with tab_browse:
    st.subheader("All 45 Genera of Labiatae in Turkey")

    # Two columns: left = list, right = detail
    left, right = st.columns([1, 2])

    with left:
        # Show a button for every plant
        for plant in PLANTS:
            label = f"{plant['id']}. *{plant['name']}* — {plant['common']}"
            if st.button(label, key=f"browse_{plant['id']}", use_container_width=True):
                # Save which plant was clicked
                st.session_state.browse_selected = plant["id"]

    with right:
        # Show the selected plant's details
        selected_id = st.session_state.get("browse_selected", 1)
        selected = get_plant(selected_id)
        if selected:
            show_plant_card(selected)

# ============================================================
# TAB 2: IDENTIFY
# The step-by-step dichotomous key.
# Click A or B at each question until you reach a genus.
# ============================================================

with tab_identify:
    st.subheader("Identify Your Plant")
    st.write("Answer A or B at each question. You will reach a genus name at the end!")

    # --- If we have already identified a plant ---
    if st.session_state.key_plant is not None:
        plant = get_plant(st.session_state.key_plant)
        st.success(f"✅ Identified in {st.session_state.key_count} questions!")
        show_plant_card(plant)

    # --- Otherwise show the current question ---
    else:
        step_id = st.session_state.key_step
        step = KEY[step_id]

        st.info(f"**Question {st.session_state.key_count + 1}:** {step['q']}")
        st.caption("Look carefully at your plant before answering!")

        col_a, col_b = st.columns(2)

        with col_a:
            if st.button(f"🔵 A — {step['a']}", use_container_width=True, key="btn_a"):
                # Save where we are before moving (for Back button)
                st.session_state.key_history.append(step_id)
                st.session_state.key_count += 1
                result_type, result_val = step["next_a"]
                if result_type == "step":
                    st.session_state.key_step = result_val
                    st.session_state.key_plant = None
                else:
                    st.session_state.key_plant = result_val
                st.rerun()   # Refresh the page to show the next question

        with col_b:
            if st.button(f"🟠 B — {step['b']}", use_container_width=True, key="btn_b"):
                st.session_state.key_history.append(step_id)
                st.session_state.key_count += 1
                result_type, result_val = step["next_b"]
                if result_type == "step":
                    st.session_state.key_step = result_val
                    st.session_state.key_plant = None
                else:
                    st.session_state.key_plant = result_val
                st.rerun()

    # --- Back and Reset buttons ---
    st.divider()
    col_back, col_reset = st.columns(2)

    with col_back:
        # Only show Back if there is history to go back to
        if st.session_state.key_history:
            if st.button("← Back", use_container_width=True):
                prev = st.session_state.key_history.pop()
                st.session_state.key_step = prev
                st.session_state.key_plant = None
                st.session_state.key_count = max(0, st.session_state.key_count - 1)
                st.rerun()

    with col_reset:
        if st.button("🔄 Reset from start", use_container_width=True):
            st.session_state.key_step = "s1"
            st.session_state.key_plant = None
            st.session_state.key_history = []
            st.session_state.key_count = 0
            st.rerun()

# ============================================================
# TAB 3: SEARCH
# Type any word to search across all plant data.
# ============================================================

with tab_search:
    st.subheader("Search Plants")

    query = st.text_input(
        "Search by Latin name, English name, Turkish name, or description:",
        placeholder="e.g. sage, nane, thyme, woolly..."
    )

    if query:
        # Search all fields of every plant
        q = query.lower()
        results = []
        for plant in PLANTS:
            # Check if the query appears in any of these fields
            if (q in plant["name"].lower()
                    or q in plant["common"].lower()
                    or q in plant["turkish"].lower()
                    or q in plant["description"].lower()
                    or q in plant["habitat"].lower()
                    or q in plant["fun_fact"].lower()):
                results.append(plant)

        if results:
            st.write(f"Found **{len(results)}** result(s) for '{query}':")
            for plant in results:
                # Each result in an expandable box
                with st.expander(
                    f"{plant['id']}. *{plant['name']}* — {plant['common']} | {plant['turkish']}"
                ):
                    show_plant_card(plant)
        else:
            st.warning(f"No plants found for '{query}'. Try a different word!")
    else:
        st.write("Start typing above to search all 45 genera.")

# ============================================================
# TAB 4: QUIZ
# You are shown clues about a plant. Type the genus name!
# ============================================================

with tab_quiz:
    st.subheader("Quiz Mode")

    # --- Start screen (no quiz running yet) ---
    if not st.session_state.quiz_plants:
        st.write("You will be shown **5 random plants**.")
        st.write("Read the clues and type the genus name (in Latin, e.g. *Salvia*).")

        if st.button("▶️ Start Quiz", use_container_width=True):
            # Pick 5 random plants and shuffle them
            st.session_state.quiz_plants = random.sample(PLANTS, 5)
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_submitted = False
            st.session_state.quiz_finished = False
            st.rerun()

    # --- Finished screen ---
    elif st.session_state.quiz_finished:
        score = st.session_state.quiz_score

        # Pick a message based on score
        if score == 5:
            msg = "PERFECT SCORE! You are a Labiatae expert! 🏆"
        elif score >= 4:
            msg = "Excellent! Almost perfect! 🌟"
        elif score >= 3:
            msg = "Good job! Keep studying! 👍"
        elif score >= 2:
            msg = "Not bad — try again to improve! 📚"
        else:
            msg = "Keep practising — these plants are tricky! 🌱"

        st.balloons()   # Fun Streamlit animation!
        st.markdown(f"## Quiz Complete!")
        st.markdown(f"### You scored **{score} out of 5**")
        st.info(msg)

        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.quiz_plants = []
            st.session_state.quiz_finished = False
            st.rerun()

    # --- Quiz question screen ---
    else:
        idx = st.session_state.quiz_index
        plant = st.session_state.quiz_plants[idx]

        # Progress bar (goes from 0 to 5)
        st.progress(idx / 5, text=f"Question {idx + 1} of 5")
        st.write(f"**Score so far: {st.session_state.quiz_score}**")

        # Photo (if available)
        if plant["photo"]:
            st.image(plant["photo"], use_container_width=True)

        # Clues card
        st.markdown("### 🔍 Clues")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**🌿 Description**")
            st.write(plant["description"])
        with col2:
            st.markdown("**⛰️ Habitat**")
            st.write(plant["habitat"])
        with col3:
            st.markdown("**⭐ Fun Fact**")
            st.write(plant["fun_fact"])

        st.divider()

        # If the answer has NOT been submitted yet
        if not st.session_state.quiz_submitted:
            guess = st.text_input(
                "Type the genus name (Latin):",
                key=f"quiz_input_{idx}",   # Unique key per question
                placeholder="e.g. Salvia"
            )

            if st.button("✅ Submit Answer", use_container_width=True):
                st.session_state.quiz_guess = guess
                st.session_state.quiz_submitted = True
                # Check if correct (case-insensitive)
                if guess.strip().lower() == plant["name"].lower():
                    st.session_state.quiz_score += 1
                st.rerun()

        # If the answer HAS been submitted — show feedback
        else:
            guess = st.session_state.quiz_guess
            correct = guess.strip().lower() == plant["name"].lower()

            if correct:
                st.success(f"✅ Correct! It is *{plant['name']}* ({plant['common']})!")
            else:
                st.error(
                    f"❌ Not quite! You wrote: *{guess}*\n\n"
                    f"The answer is: **{plant['name']}** ({plant['common']})"
                )

            if st.button("Next →", use_container_width=True):
                next_idx = idx + 1
                if next_idx >= 5:
                    st.session_state.quiz_finished = True
                else:
                    st.session_state.quiz_index = next_idx
                    st.session_state.quiz_submitted = False
                    st.session_state.quiz_guess = ""
                st.rerun()

# ============================================================
# TAB 5: SWIFT CODE
# Shows the full LabiateApp.swift with a one-click copy button
# ============================================================

with tab_swift:
    st.subheader("Swift Playgrounds Code (iPad)")
    st.write("Click the **copy icon** in the top-right corner of the code box to copy everything.")
    st.info(
        "**How to use:**\n"
        "1. Copy the code below\n"
        "2. Open Swift Playgrounds on iPad → tap **+** → App Playground → Create\n"
        "3. Tap the file in the sidebar (e.g. `MyApp.swift`)\n"
        "4. Select all existing code and delete it\n"
        "5. Paste this code in\n"
        "6. Delete any other `.swift` files in the project\n"
        "7. Tap the Run ▶ button"
    )

    import os
    swift_path = os.path.join(os.path.dirname(__file__), "LabiateApp.swift")
    try:
        with open(swift_path, "r", encoding="utf-8") as f:
            swift_code = f.read()
        st.code(swift_code, language="swift")
    except FileNotFoundError:
        st.error("LabiateApp.swift not found next to app.py")
