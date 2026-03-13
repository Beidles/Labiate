# ============================================================
# LABIATAE (Mint Family) of Turkey
# Based on: Flora of Turkey by P.H. Davis (Volume 7)
# ============================================================
# This program helps you identify plants from the Labiatae family
# found in Turkey using a step-by-step identification key.
#
# The Labiatae family (also called Lamiaceae) includes plants like
# mint, lavender, thyme, and rosemary. They usually have:
#   - Square stems
#   - Opposite leaves (leaves grow in pairs)
#   - Two-lipped (bilabiate) flowers
#   - Strong smell (aromatic)
# ============================================================

# -----------------------------------------------------------
# PLANT DATA
# Each plant genus (group) has: name, Turkish name, description,
# habitat, and a fun fact.
# -----------------------------------------------------------

GENERA = {
    1:  {
        "name": "Ajuga",
        "common": "Bugle",
        "turkish": "Mayasıl otu",
        "description": "Low-growing herbs with 1-lipped corolla (the upper lip is tiny or missing). Lower lip has 5 lobes.",
        "habitat": "Meadows, roadsides, forest edges",
        "fun_fact": "Used in traditional medicine to treat wounds and fevers.",
        "stamens": 4,
        "corolla_upper_lip": "absent or tiny",
    },
    2:  {
        "name": "Teucrium",
        "common": "Germander",
        "turkish": "Kıbrıscık / Mahmut otu",
        "description": "Herbs or shrubs. Corolla appears 1-lipped with a 5-lobed lower lip. Tube is smooth inside.",
        "habitat": "Rocky hillsides, dry grasslands, scrub",
        "fun_fact": "Wall Germander (Teucrium chamaedrys) has been used since ancient Greek times.",
        "stamens": 4,
        "corolla_upper_lip": "absent or tiny",
    },
    3:  {
        "name": "Rosmarinus",
        "common": "Rosemary",
        "turkish": "Biberiye",
        "description": "Evergreen shrub with narrow, needle-like leaves. Pale blue flowers. Very aromatic.",
        "habitat": "Dry rocky hillsides near the coast",
        "fun_fact": "Rosemary is used in cooking all around the world and is a symbol of remembrance.",
        "stamens": 2,
        "corolla_upper_lip": "present",
    },
    4:  {
        "name": "Lavandula",
        "common": "Lavender",
        "turkish": "Lavanta",
        "description": "Aromatic shrubs with star-shaped or branched hairs. Purple flowers in long spikes.",
        "habitat": "Dry rocky places, cultivated widely",
        "fun_fact": "Turkey is one of the world's top producers of lavender oil.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    5:  {
        "name": "Prasium",
        "common": "Prasium",
        "turkish": "Prasiyum",
        "description": "A small evergreen shrub. Shiny, fleshy black fruits. White or pale purple flowers.",
        "habitat": "Maquis scrubland near the coast",
        "fun_fact": "One of the few Labiatae with fleshy berries instead of dry nutlets.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    6:  {
        "name": "Scutellaria",
        "common": "Skullcap",
        "turkish": "Mıknatısotu",
        "description": "Herbs with a unique calyx: the upper lip has a small shield-like flap on top.",
        "habitat": "Moist meadows, stream banks, rocky slopes",
        "fun_fact": "Scutellaria baicalensis is used in Chinese medicine and is being studied for cancer treatment.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    7:  {
        "name": "Melittis",
        "common": "Bastard Balm",
        "turkish": "Arınanesi",
        "description": "Large, showy flowers (up to 35 mm!) in upper leaf axils. Strongly honey-scented.",
        "habitat": "Shaded woodland, forest edges",
        "fun_fact": "Its name comes from the Greek word for 'bee' — bees love its flowers.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    8:  {
        "name": "Eremostachys",
        "common": "Desert Candle",
        "turkish": "Çöl şamdanı",
        "description": "Tall herbs with large, woolly leaves. Yellow upper lip, orange lower lip. Very distinctive.",
        "habitat": "Dry steppe and semi-desert areas of eastern Turkey",
        "fun_fact": "Can grow over 1 metre tall and is hard to miss on the dry steppes.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    9:  {
        "name": "Phlomis",
        "common": "Jerusalem Sage",
        "turkish": "Şalba / Fener otu",
        "description": "Woolly herbs or shrubs. The upper lip of the corolla is strongly curved like a hood (falcate).",
        "habitat": "Rocky slopes, scrub, dry hills",
        "fun_fact": "In Turkey, Phlomis leaves are dried and made into a herbal tea called 'çay dağı'.",
        "stamens": 4,
        "corolla_upper_lip": "falcate (hooded)",
    },
    10: {
        "name": "Lamium",
        "common": "Dead Nettle",
        "turkish": "Ballıbaba",
        "description": "Herbs that look like nettles but DON'T sting! White, pink, or purple flowers.",
        "habitat": "Roadsides, disturbed ground, gardens",
        "fun_fact": "White Dead Nettle (Lamium album) flowers are edible and can be added to salads.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    11: {
        "name": "Wiedemannia",
        "common": "Wiedemannia",
        "turkish": "Wiedemannya",
        "description": "Herbs similar to Prunella. Pinkish flowers with a very hairy (villous) upper lip.",
        "habitat": "Moist mountain slopes, stream sides",
        "fun_fact": "Named after the German botanist E.J. von Wiedemann who worked in Istanbul.",
        "stamens": 4,
        "corolla_upper_lip": "present, villous",
    },
    12: {
        "name": "Galeobdolon",
        "common": "Yellow Archangel",
        "turkish": "Sarı ölü ısırgan",
        "description": "Stoloniferous herb (spreads by runners). Yellow flowers. Glabrous (smooth) thecae.",
        "habitat": "Shaded woodland, hedgerows",
        "fun_fact": "Its runners can spread metres from the parent plant, carpeting the woodland floor.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    13: {
        "name": "Galeopsis",
        "common": "Hemp Nettle",
        "turkish": "Kenevir ısırganı",
        "description": "Annual herbs with spiny bracteoles. Lower lip of corolla has 2 bump-like appendages at the base.",
        "habitat": "Arable fields, disturbed ground",
        "fun_fact": "Galeopsis tetrahit was one of the first plants used to demonstrate polyploidy — a key concept in genetics!",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    14: {
        "name": "Leonurus",
        "common": "Motherwort",
        "turkish": "Oğulotu / Aslan kuyruğu",
        "description": "Tall herbs with deeply divided, hand-shaped leaves. Small pinkish-white flowers (5-12 mm).",
        "habitat": "Roadsides, waste places, near villages",
        "fun_fact": "Motherwort has been used for centuries to calm the heart. Modern research is investigating its use for heart conditions.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    15: {
        "name": "Moluccella",
        "common": "Bells of Ireland",
        "turkish": "Zil çiçeği",
        "description": "The calyx (cup around the flower) is HUGE and bell-shaped. Small white flowers inside.",
        "habitat": "Disturbed ground, field margins",
        "fun_fact": "Despite its common name 'Bells of Ireland', it is actually native to Turkey and Syria!",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    16: {
        "name": "Ballota",
        "common": "Black Horehound",
        "turkish": "Ballota / Andız otu",
        "description": "Woolly herbs. Calyx tube widens into a toothed, flat, star-like limb after flowering.",
        "habitat": "Roadsides, rocky slopes, waste ground",
        "fun_fact": "The strong, unpleasant smell keeps most animals from eating it — nature's own pest repellent.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    17: {
        "name": "Marrubium",
        "common": "Horehound",
        "turkish": "Topalak / Acı nane",
        "description": "White-woolly herbs. Calyx has 5-10 hook-like teeth. Stamens hidden inside the corolla tube.",
        "habitat": "Dry roadsides, overgrazed areas, waste ground",
        "fun_fact": "Horehound candy and horehound tea are traditional remedies for coughs — still sold today.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    18: {
        "name": "Sideritis",
        "common": "Ironwort / Mountain Tea",
        "turkish": "Dağ çayı / Demir otu",
        "description": "Herbs or small shrubs, often silvery-woolly. Bracts often leaf-like and spiny.",
        "habitat": "Rocky mountain slopes, limestone cliffs",
        "fun_fact": "Sideritis tea ('dağ çayı') is extremely popular in Turkey, drunk for health and enjoyment.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    19: {
        "name": "Stachys",
        "common": "Woundwort / Betony",
        "turkish": "Karabaş / Moruk otu",
        "description": "Herbs or shrubs. Calyx with 5 teeth. One of the LARGEST genera in the Turkish Labiatae.",
        "habitat": "Very varied — meadows, forests, rocky slopes, roadsides",
        "fun_fact": "Turkey has more species of Stachys than almost any other country in the world.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    20: {
        "name": "Melissa",
        "common": "Lemon Balm",
        "turkish": "Melisa / Oğul otu",
        "description": "Lemon-scented herb. White or pale pink small flowers. Leaves smell strongly of lemon.",
        "habitat": "Woodland edges, hedgerows, stream banks",
        "fun_fact": "Lemon Balm tea is one of the most popular herbal teas in Turkey for calming nerves and helping sleep.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    21: {
        "name": "Nepeta",
        "common": "Catmint",
        "turkish": "Kedi nanesi",
        "description": "Blue or white flowers in branching cymes. Many-flowered verticillasters not in leaf axils.",
        "habitat": "Dry rocky slopes, roadsides",
        "fun_fact": "Cats go wild for Nepeta cataria (catnip) because it contains a chemical that mimics cat pheromones.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    22: {
        "name": "Glechoma",
        "common": "Ground Ivy",
        "turkish": "Yer sarmaşığı",
        "description": "Creeping herb with round, scalloped leaves. Spreads by stolons (runners along the ground).",
        "habitat": "Shaded moist places, hedgerows, lawns",
        "fun_fact": "Before hops were used, Ground Ivy was the main flavouring added to beer in medieval Europe.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    23: {
        "name": "Dracocephalum",
        "common": "Dragonhead",
        "turkish": "Ejderha başı",
        "description": "Blue-purple flowers. Bracteoles have pointed (acuminate) tips. Perennial herbs.",
        "habitat": "Mountain steppes, rocky slopes",
        "fun_fact": "The name means 'dragon head' in Greek — the flowers are said to look like a dragon's mouth.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    24: {
        "name": "Lallemantia",
        "common": "Lallemantia",
        "turkish": "Lallemantia",
        "description": "Upper lip of corolla has 2 internal folds (unique feature!). Bracteoles prominently veined.",
        "habitat": "Arable fields, dry disturbed ground",
        "fun_fact": "Lallemantia seeds contain an oil used in traditional medicine and as a food source in Central Asia.",
        "stamens": 4,
        "corolla_upper_lip": "present with 2 internal folds",
    },
    25: {
        "name": "Hymenocrater",
        "common": "Hymenocrater",
        "turkish": "Hymenocrater",
        "description": "A shrub with striking violet resupinate (upside-down) corollas. Bracteoles are leaf-like.",
        "habitat": "Rocky slopes and cliffs in eastern Turkey",
        "fun_fact": "Resupinate means the flower is twisted 180 degrees — the 'top' is actually the bottom!",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    26: {
        "name": "Hyssopus",
        "common": "Hyssop",
        "turkish": "Çördük / Hisop",
        "description": "Small aromatic shrub. Tubular calyx with thickened folds. Violet-blue corolla.",
        "habitat": "Dry rocky slopes, scrub",
        "fun_fact": "Hyssop is mentioned in the Bible as a purifying herb and was used in ancient religious rituals.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    27: {
        "name": "Prunella",
        "common": "Selfheal",
        "turkish": "Ölmez otu / Yaraotu",
        "description": "Dense terminal flower heads. Violet flowers. Calyx is clearly 2-lipped (bilabiate).",
        "habitat": "Meadows, roadsides, lawns, open woodland",
        "fun_fact": "Selfheal (Prunella vulgaris) was historically used to heal wounds — and modern science confirms it has antimicrobial compounds.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    28: {
        "name": "Origanum",
        "common": "Oregano / Marjoram",
        "turkish": "Kekik / Mercanköşk",
        "description": "Aromatic herb. Flowers in panicles or corymbs with prominent, imbricate bracts hiding the flowers.",
        "habitat": "Dry rocky hillsides, scrub",
        "fun_fact": "Turkey exports large amounts of oregano (kekik). It is essential in Turkish and Mediterranean cooking.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    29: {
        "name": "Pentapleura",
        "common": "Pentapleura",
        "turkish": "Pentapleura",
        "description": "A rare genus found only in a small part of Turkey. Related to Hyssopus.",
        "habitat": "Rocky limestone areas in south Turkey",
        "fun_fact": "Pentapleura subulifera is endemic to Turkey — it grows NOWHERE else in the world.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    30: {
        "name": "Satureja",
        "common": "Savory",
        "turkish": "Sater / Bağ kekiği",
        "description": "Small aromatic herbs or shrubs. Leaves often cuneate (wedge-shaped) at the base.",
        "habitat": "Rocky limestone slopes, dry hillsides",
        "fun_fact": "Summer Savory (Satureja hortensis) is used as a spice in cooking, especially with beans.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    31: {
        "name": "Calamintha",
        "common": "Calamint",
        "turkish": "Yaban nanesi",
        "description": "Mint-like herbs. Teeth of the calyx lower lip are clearly fringed with hairs (ciliate).",
        "habitat": "Rocky slopes, forest edges, scrub",
        "fun_fact": "Calamint smells like a mix of mint and thyme and is sometimes used to make herbal tea.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    32: {
        "name": "Clinopodium",
        "common": "Wild Basil",
        "turkish": "Yaban fesleğeni",
        "description": "Hairy herbs. Calyx tube strongly curved. Teeth are long and ciliate (fringed with hairs).",
        "habitat": "Hedgerows, woodland edges, scrub",
        "fun_fact": "Though called 'Wild Basil', it is not the same as culinary basil — but it does smell similar.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    33: {
        "name": "Acinos",
        "common": "Basil Thyme",
        "turkish": "Akinos",
        "description": "Small annual or perennial herbs. Calyx tube gibbous (swollen/hump-shaped) at base.",
        "habitat": "Dry grassland, arable fields, rocky slopes",
        "fun_fact": "Despite the name 'Basil Thyme', it is neither a basil nor a thyme — taxonomy can be confusing!",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    34: {
        "name": "Micromeria",
        "common": "Micromeria",
        "turkish": "Küçük nane",
        "description": "Small aromatic herbs. Calyx 1.5-6 mm and 13-15 veined. Corolla tube stays inside the calyx.",
        "habitat": "Rocky limestone cliffs, walls, scrub",
        "fun_fact": "Some species are used to make herbal tea in Turkey and are collected from wild plants.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    35: {
        "name": "Cyclotrichium",
        "common": "Cyclotrichium",
        "turkish": "Silindir tüylü",
        "description": "Shrubby herbs with stellate (star-shaped) hairs. Stamens stick out beyond the upper lip.",
        "habitat": "Rocky slopes in eastern Anatolia",
        "fun_fact": "A genus found mainly in Turkey and Iran — quite rare in global terms.",
        "stamens": 4,
        "corolla_upper_lip": "present, resupinate",
    },
    36: {
        "name": "Thymus",
        "common": "Thyme",
        "turkish": "Kekik",
        "description": "Small aromatic shrubs. Woody base, tiny leaves. Pink or purple flowers. Very fragrant.",
        "habitat": "Dry rocky hillsides, grasslands, mountain slopes",
        "fun_fact": "Turkey has over 50 species of wild thyme — more than any other country. Thyme ('kekik') is essential in Turkish cuisine.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    37: {
        "name": "Coridothymus",
        "common": "Cretan Thyme",
        "turkish": "Kekik (Girit)",
        "description": "A thyme-like shrub. Inflorescence is a HEAD (not a spike). Calyx has 20-22 veins.",
        "habitat": "Rocky coastal areas",
        "fun_fact": "Produces a high-quality essential oil used in perfumes and medicines.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    38: {
        "name": "Thymbra",
        "common": "Za'atar",
        "turkish": "Zahter / Kaya kekiği",
        "description": "Thyme-like shrub. Inflorescence is a SPIKE. Calyx has 13 veins. Leaves conduplicate (folded).",
        "habitat": "Rocky limestone hillsides in southern Turkey",
        "fun_fact": "Thymbra spicata is the famous 'za'atar' herb of the Middle East, used in the spice blend of the same name.",
        "stamens": 4,
        "corolla_upper_lip": "present",
    },
    39: {
        "name": "Mentha",
        "common": "Mint",
        "turkish": "Nane",
        "description": "Creeping herbs in moist places. Corolla has 4 nearly equal lobes (unusual for Labiatae).",
        "habitat": "Stream banks, ditches, wet meadows",
        "fun_fact": "Mint tea ('nane çayı') is one of Turkey's most beloved drinks. Mint also grows in the wild near almost every stream.",
        "stamens": 4,
        "corolla_upper_lip": "4 equal lobes (unusual)",
    },
    40: {
        "name": "Lycopus",
        "common": "Gipsywort / Bugleweed",
        "turkish": "Kurt ayağı / Çingene otu",
        "description": "Herb of wet places. Deeply toothed leaves. Non-aromatic (no smell). Tiny white flowers.",
        "habitat": "Riverbanks, marshes, wet meadows",
        "fun_fact": "Historically used to dye fabric black, and gypsies were said to use it to dye their skin.",
        "stamens": 2,
        "corolla_upper_lip": "present",
    },
    41: {
        "name": "Ziziphora",
        "common": "Ziziphora",
        "turkish": "Zizifora",
        "description": "Small aromatic herbs with cuneate-based leaves. Dense head or spike inflorescence.",
        "habitat": "Dry steppe, rocky slopes",
        "fun_fact": "Used in traditional medicine across Central Asia and Turkey for digestive problems.",
        "stamens": 2,
        "corolla_upper_lip": "present",
    },
    42: {
        "name": "Salvia",
        "common": "Sage",
        "turkish": "Adaçayı",
        "description": "The LARGEST genus in Turkish Labiatae! Unique lever-like stamens. Very diverse.",
        "habitat": "Extremely varied — rocky slopes, scrub, meadows, forests",
        "fun_fact": "Turkey has around 100 species of wild sage! Sage tea ('adaçayı') is Turkey's most famous herbal tea and is sold everywhere.",
        "stamens": 2,
        "corolla_upper_lip": "present, with elongated staminal connectives",
    },
    43: {
        "name": "Dorystoechas",
        "common": "Dorystoechas",
        "turkish": "Dorystoechas",
        "description": "A woody shrub with arrow-shaped (hastate) leaves and slender cylindrical spikes.",
        "habitat": "Rocky hillsides in southwestern Turkey",
        "fun_fact": "Dorystoechas hastata is ENDEMIC to Turkey — it exists nowhere else on Earth and is endangered.",
        "stamens": 2,
        "corolla_upper_lip": "present",
    },
    44: {
        "name": "Elsholtzia",
        "common": "Elsholtzia",
        "turkish": "Elşoltsiya",
        "description": "Annual or short-lived herb. Inflorescence a one-sided spike. Stamens decline (droop downward).",
        "habitat": "Disturbed ground, roadsides, cultivated areas",
        "fun_fact": "In China, Elsholtzia ciliata is used as a spice and a medicine for colds.",
        "stamens": 4,
        "corolla_upper_lip": "present, small",
    },
    45: {
        "name": "Ocimum",
        "common": "Basil",
        "turkish": "Fesleğen",
        "description": "Annual herb. Calyx deflexed in fruit. Upper lip of calyx broadly circular with decurrent margins.",
        "habitat": "Cultivated, occasionally naturalised",
        "fun_fact": "Sweet Basil (Ocimum basilicum) is one of the most important culinary herbs in the world. It originates from tropical Asia.",
        "stamens": 4,
        "corolla_upper_lip": "small",
    },
}

# -----------------------------------------------------------
# IDENTIFICATION KEY
# This is a simplified version of the key from:
# Flora of Turkey, Volume 7, P.H. Davis (pp. 37-42)
#
# How a dichotomous key works:
#   - You are given TWO choices (a or b)
#   - You pick the one that matches your plant
#   - You keep going until you reach a genus name
# -----------------------------------------------------------

def ask_question(question, option_a, option_b):
    """
    Ask the user a yes/no style question.
    Returns 'a' or 'b' based on their choice.
    """
    print()
    print("=" * 60)
    print(f"QUESTION: {question}")
    print()
    print(f"  A) {option_a}")
    print(f"  B) {option_b}")
    print()

    while True:
        answer = input("Your answer (A or B): ").strip().upper()
        if answer in ("A", "B"):
            return answer.lower()
        else:
            print("  Please type A or B!")


def identify_plant():
    """
    Walk the user through a dichotomous key to identify
    which genus their plant belongs to.
    """
    print()
    print("*" * 60)
    print("  LABIATAE IDENTIFICATION KEY")
    print("  Flora of Turkey (P.H. Davis, Vol. 7)")
    print("*" * 60)
    print()
    print("Look carefully at your plant and answer each question.")
    print("TIP: Use a magnifying glass if you have one!")

    # ---- STEP 1: Count the fertile stamens ----
    answer = ask_question(
        "How many FERTILE (fully developed) stamens does the flower have?",
        "2 stamens (the other pair is tiny/missing)",
        "4 stamens (or all stamens reduced/sterile in female flowers)"
    )

    # Branch: 2 fertile stamens
    if answer == "a":
        answer2 = ask_question(
            "Look at the stamens closely. Are the CONNECTIVES (the part joining the two pollen sacs) elongated and lever-like?",
            "YES — connectives are long, articulating with the filament (like a see-saw)",
            "NO — connectives are very short, not lever-like"
        )
        if answer2 == "a":
            return 42  # Salvia

        # Short connectives — now check leaves
        answer3 = ask_question(
            "Are the leaves EVERGREEN and LINEAR (narrow, like a needle)?",
            "YES — evergreen, narrow leaves; pale blue corolla 8-12 mm; shrub",
            "NO — deciduous or broader leaves"
        )
        if answer3 == "a":
            return 3  # Rosmarinus

        # Deciduous leaves
        answer4 = ask_question(
            "Where are the flower clusters (verticillasters)?",
            "In the UPPER LEAF AXILS, widely spaced; leaves coarsely toothed to deeply divided; non-aromatic",
            "Grouped into TERMINAL SPIKES or HEADS; leaf margins entire or slightly toothed; aromatic"
        )
        if answer4 == "a":
            return 40  # Lycopus

        answer5 = ask_question(
            "Is the plant a WOODY SHRUB with arrow-shaped (hastate) leaves and slender cylindrical spikes?",
            "YES — woody shrub, hastate leaves, cylindrical spikes",
            "NO — annual or perennial herb with cuneate-based leaves; inflorescence a head or spike"
        )
        if answer5 == "a":
            return 43  # Dorystoechas
        else:
            return 41  # Ziziphora

    # Branch: 4 fertile stamens (or all sterile in female plants)
    # ---- STEP 2: Upper lip of corolla ----
    answer6 = ask_question(
        "Look at the UPPER LIP of the corolla (the top petal). Is it well-developed?",
        "NO — upper lip absent or very tiny (flower looks 1-lipped)",
        "YES — upper lip clearly present and well-developed"
    )

    if answer6 == "a":
        answer7 = ask_question(
            "Look at the lower lip. Does the corolla tube have a smooth (glabrous) inside?",
            "YES — corolla tube smooth inside; lower lip with 5 lobes",
            "NO — corolla tube usually has a ring of hairs inside; upper lip reduced to 2 lobes"
        )
        if answer7 == "a":
            return 2  # Teucrium
        else:
            return 1  # Ajuga

    # Upper lip present — check hairs on plant
    # ---- STEP 3: Type of hairs ----
    answer8 = ask_question(
        "Examine the HAIRS on the plant (leaves, stem, calyx). What type are they?",
        "BRANCHED hairs — dendroid (tree-like), forked, or stellate (star-shaped)",
        "SIMPLE hairs only (unbranched), or the plant has no hairs at all"
    )

    # Branched hairs
    if answer8 == "a":
        answer9 = ask_question(
            "How are the flower clusters arranged?",
            "In PEDUNCULATE SPIKES (on a long stalk); upper calyx lip has an appendage; stamens droop downward",
            "Flower clusters DISTANT or CLOSE but NOT in pedunculate spikes; calyx without appendage; stamens not drooping"
        )
        if answer9 == "a":
            return 4  # Lavandula

        answer10 = ask_question(
            "Are the stamens CLEARLY EXSERTED (sticking out) beyond the upper lip of the corolla?",
            "YES — stamens clearly stick out beyond the upper lip; corolla resupinate",
            "NO — stamens do not stick out beyond the upper lip"
        )
        if answer10 == "a":
            return 35  # Cyclotrichium

        answer11 = ask_question(
            "Is the upper lip of the corolla FALCATE (curved like a sickle or hood)?",
            "YES — upper lip clearly curved/hooded",
            "NO — upper lip straight or slightly concave"
        )
        if answer11 == "a":
            return 9  # Phlomis

        # Straight upper lip with branched hairs
        answer12 = ask_question(
            "How many TEETH does the calyx have, and what are the hairs inside the calyx throat like?",
            "5 teeth; calyx throat glabrous (smooth) or weakly hairy",
            "5-10(-30) teeth; calyx throat has stiff long white hairs"
        )
        if answer12 == "a":
            return 19  # Stachys

        answer13 = ask_question(
            "Are the STAMENS included (hidden) inside the corolla tube?",
            "YES — stamens hidden inside the tube; calyx tube not widened above",
            "NO — stamens NOT inside the tube; calyx tube widens into a flat toothed limb"
        )
        if answer13 == "a":
            return 17  # Marrubium
        else:
            return 16  # Ballota

    # Simple hairs or glabrous
    # ---- STEP 4: Fruiting calyx ----
    answer14 = ask_question(
        "Look at the FRUITING CALYX (the calyx when fruits are forming). Is it MUCH ENLARGED and membrane-like with broad spreading lobes?",
        "YES — fruiting calyx greatly enlarged, papery/membranous with broad spreading lobes",
        "NO — fruiting calyx not like that (may enlarge a little, but not membranous with broad lobes)"
    )

    if answer14 == "a":
        answer15 = ask_question(
            "What colour are the LEAVES and COROLLA?",
            "Leaves woolly; corolla upper lip YELLOW, lower lip orange",
            "Leaves glabrous (smooth); corolla white, pink, or violet"
        )
        if answer15 == "a":
            return 8  # Eremostachys
        answer16 = ask_question(
            "Is the plant a SHRUB with violet upside-down (resupinate) corollas?",
            "YES — shrub; violet resupinate corollas; bracteoles herbaceous",
            "NO — annual with white/pinkish non-resupinate corollas; bracteoles spinose"
        )
        if answer16 == "a":
            return 25  # Hymenocrater
        else:
            return 15  # Moluccella

    # Fruiting calyx not enlarged/membranous
    # ---- STEP 5: Calyx venation ----
    answer17 = ask_question(
        "How many veins/ribs does the CALYX TUBE have?",
        "15 or more (distinctly 15-veined or ribbed); UPPER stamens longer than lower",
        "5-14 veins or ribs; LOWER (anterior) stamens longer than upper, or stamens equal"
    )

    if answer17 == "a":
        # 15+ veined calyx
        answer18 = ask_question(
            "Do the CALYX SINUSES (gaps between calyx teeth) have a thickened fold at the base?",
            "YES — thickened fold present; middle lobe of upper calyx lip clearly broader than laterals",
            "NO — calyx sinuses without a thickened fold; lobes not much different in width"
        )
        if answer18 == "a":
            answer19 = ask_question(
                "Does the UPPER LIP of the corolla have 2 internal longitudinal folds?",
                "YES — 2 internal folds; bracteoles prominently veined and aristate-dentate; annuals or perennials",
                "NO — no internal folds; bracteoles aristate or acuminate; perennials"
            )
            if answer19 == "a":
                return 24  # Lallemantia
            else:
                return 23  # Dracocephalum

        answer20 = ask_question(
            "Are the verticillasters 2-6-flowered, in UPPER LEAF AXILS, and one-sided (secund)? Is the plant stoloniferous?",
            "YES — 2-6 flowered, secund, plant spreads by stolons",
            "NO — 6 or more flowered, NOT in leaf axils (or inflorescence of pedunculate cymes); plant not stoloniferous"
        )
        if answer20 == "a":
            return 22  # Glechoma
        else:
            return 21  # Nepeta

    # 5-14 veined calyx
    # ---- STEP 6: Corolla tube shape ----
    answer21 = ask_question(
        "Is the COROLLA TUBE long, slender, and sigmoid (S-shaped), with small lips?",
        "YES — corolla tube long, slender, sigmoid; calyx lips entire, upper with a small flap",
        "NO — corolla tube not like that; calyx without a flap"
    )
    if answer21 == "a":
        return 6  # Scutellaria

    # ---- STEP 7: Upper lip of corolla shape ----
    answer22 = ask_question(
        "Is the upper lip of the corolla FALCATE (curved like a sickle or hood)?",
        "YES — upper lip clearly falcate (curved)",
        "NO — upper lip straight or slightly concave"
    )

    if answer22 == "a":
        answer23 = ask_question(
            "Is the calyx CLEARLY BILABIATE (two-lipped)?",
            "YES — calyx clearly 2-lipped",
            "NO — calyx not or indistinctly 2-lipped"
        )
        if answer23 == "a":
            answer24 = ask_question(
                "Are the verticillasters CROWDED into dense terminal spikes with bracts hiding the calyces?",
                "YES — dense terminal spikes; bracts hide calyces; flowers violet or creamy-white; upper lip hairy",
                "NO — verticillasters distant; bracts do NOT hide calyces; flowers pinkish; upper lip very hairy/tomentose"
            )
            if answer24 == "a":
                return 27  # Prunella
            else:
                return 11  # Wiedemannia

        # Calyx not distinctly bilabiate
        answer25 = ask_question(
            "Do the nutlets (small fruits) have TUFTS OF HAIR at the tip?",
            "YES — nutlets have hair tufts at apex",
            "NO — nutlets are smooth (glabrous)"
        )
        if answer25 == "a":
            answer26 = ask_question(
                "How big is the corolla, and what do the leaves look like?",
                "Corolla 5-12 mm, pinkish-white; leaves digitately divided or subentire",
                "Corolla 18-40 mm, yellow or whitish; leaves pinnate, lobed, or subentire"
            )
            if answer26 == "a":
                return 14  # Leonurus
            else:
                return 8  # Eremostachys

        # Nutlets glabrous
        answer27 = ask_question(
            "Are the THECAE (pollen sacs) glabrous and is the corolla yellow? Is the plant stoloniferous?",
            "YES — thecae smooth; corolla yellow; plant stoloniferous (spreads by runners)",
            "NO — thecae hairy; corolla white, cream, pink, or purple; not stoloniferous"
        )
        if answer27 == "a":
            return 12  # Galeobdolon

        answer28 = ask_question(
            "Are the bracteoles SPINY?",
            "YES — bracteoles spiny; lower lip of corolla with 2 blunt conical appendages; annuals",
            "NO — bracteoles not spiny; lower lip with very reduced lateral lobes"
        )
        if answer28 == "a":
            return 13  # Galeopsis
        else:
            return 10  # Lamium

    # Upper lip straight or concave
    # ---- STEP 8: Are stamens exserted? ----
    answer29 = ask_question(
        "Are the stamens CLEARLY EXSERTED (sticking out beyond) the upper lip of the corolla?",
        "YES — stamens clearly stick out beyond the upper lip",
        "NO — stamens do not stick out beyond the upper lip"
    )

    if answer29 == "a":
        answer30 = ask_question(
            "Is the calyx CLEARLY BILABIATE with LOWER TEETH markedly different in shape from upper?",
            "YES — calyx clearly 2-lipped; lower teeth very different from upper",
            "NO — calyx not or indistinctly bilabiate; upper and lower lobes/teeth similar"
        )
        if answer30 == "a":
            answer31 = ask_question(
                "Is the plant an ANNUAL or short-lived perennial? Do the stamens droop (declinate)?",
                "YES — annual or short-lived perennial; stamens declinate",
                "NO — shrub or woody-based perennial; stamens not declinate"
            )
            if answer31 == "a":
                answer32 = ask_question(
                    "Is the calyx DEFLEXED (bent back) in fruit? Is the upper calyx lip broadly circular?",
                    "YES — calyx deflexed in fruit; upper lip broadly orbicular; inflorescence of racemes",
                    "NO — calyx not deflexed in fruit; upper lip not broadly circular; inflorescence of spikes"
                )
                if answer32 == "a":
                    return 45  # Ocimum
                else:
                    return 44  # Elsholtzia

            # Shrubs or woody perennials
            answer33 = ask_question(
                "Is the calyx tube dorsally COMPRESSED (flattened from top to bottom) with 2 lateral ciliolate flanges?",
                "YES — calyx tube dorsally compressed with 2 ciliolate flanges",
                "NO — calyx tube not dorsally flattened, without flanges"
            )
            if answer33 == "a":
                answer34 = ask_question(
                    "What is the INFLORESCENCE type?",
                    "SPICATE (a spike); calyx 13-veined; leaves conduplicate (folded lengthwise)",
                    "CAPITATE (a head); calyx 20-22-veined; leaves subtriquetrious (3-angled)"
                )
                if answer34 == "a":
                    return 38  # Thymbra
                else:
                    return 37  # Coridothymus
            else:
                return 36  # Thymus

        # Calyx not bilabiate, lobes similar
        answer35 = ask_question(
            "Is the inflorescence spicules arranged in PANICLES or CORYMBS with prominent, overlapping bracts hiding the calyces?",
            "YES — panicles or corymbs; bracts prominent, imbricate, usually hiding calyces",
            "NO — inflorescence not like that; bracts inconspicuous"
        )
        if answer35 == "a":
            return 28  # Origanum

        answer36 = ask_question(
            "Does the corolla have 4 SUBEQUAL (nearly equal) lobes? Does the plant grow in DAMP places with creeping rhizomes?",
            "YES — 4 subequal lobes; damp habitats; creeping rhizomes rooting at nodes",
            "NO — 5 unequal lobes; dry places; no creeping rhizomes"
        )
        if answer36 == "a":
            return 39  # Mentha

        answer37 = ask_question(
            "Are the leaves OVATE to SUBORBICULAR? Is the corolla resupinate (upside-down)?",
            "YES — leaves ovate to suborbicular; corolla resupinate; thecae parallel",
            "NO — leaves linear to linear-lanceolate; corolla not resupinate; thecae divergent"
        )
        if answer37 == "a":
            return 35  # Cyclotrichium

        answer38 = ask_question(
            "Is the calyx tubular (6-8 mm) with thickened folds at the base of the sinuses?",
            "YES — tubular, 6-8 mm; thickened folds at sinus bases; corolla violet-blue",
            "NO — ovate-campanulate, 3-4(-5) mm; WITHOUT thickened folds; corolla white"
        )
        if answer38 == "a":
            return 26  # Hyssopus
        else:
            return 30  # Satureja

    # Stamens NOT exserted beyond upper lip
    # ---- STEP 9: Calyx throat ----
    answer39 = ask_question(
        "Does the CALYX THROAT have a BEARD — a ring of stiff, thick white hairs?",
        "YES — calyx throat has a beard of stiff white hairs",
        "NO — calyx throat glabrous (smooth) or with only a few weak hairs"
    )

    if answer39 == "a":
        answer40 = ask_question(
            "Does the corolla have 4 SUBEQUAL lobes? Does the plant grow in DAMP places with rhizomes?",
            "YES — 4 subequal lobes; damp places; rhizomes root at nodes (usually male-sterile plants)",
            "NO — 5 unequal lobes (2 upper, 3 lower); dry places; procumbent or erect"
        )
        if answer40 == "a":
            return 39  # Mentha

        answer41 = ask_question(
            "Is the calyx dorsally COMPRESSED with two lateral ciliolate flanges?",
            "YES — calyx compressed; two ciliolate flanges present",
            "NO — calyx not dorsally flattened; no flanges"
        )
        if answer41 == "a":
            answer42 = ask_question(
                "What is the inflorescence type?",
                "SPICATE (spike); calyx 13-veined; leaves conduplicate",
                "CAPITATE (head); calyx 20-22-veined; leaves triquetrious"
            )
            if answer42 == "a":
                return 38  # Thymbra
            else:
                return 37  # Coridothymus

        # Calyx not flattened
        answer43 = ask_question(
            "Is the inflorescence in PANICLES or CORYMBS with prominent overlapping bracts hiding the calyces?",
            "YES — panicles or corymbs; prominent imbricate bracts",
            "NO — bracts inconspicuous; not hiding calyces"
        )
        if answer43 == "a":
            return 28  # Origanum

        answer44 = ask_question(
            "Do ALL parts of the plant have long, sturdy hairs? Do the calyces have 10-20(-30) ribs?",
            "YES — long sturdy hairs throughout; calyces 10-20(-30)-ribbed",
            "NO — hairs short, crisp, or pointing forward/backward; calyces 5-13(-15)-veined"
        )
        if answer44 == "a":
            answer45 = ask_question(
                "Are the stamens INCLUDED inside the corolla tube? Is the calyx NOT widened above the tube?",
                "YES — stamens inside tube; calyx not widened above",
                "NO — stamens NOT included in tube; calyx tube widens into a flat toothed limb"
            )
            if answer45 == "a":
                return 17  # Marrubium
            else:
                return 16  # Ballota

        # Short hairs
        answer46 = ask_question(
            "Are the LOWER calyx teeth long-subulate (awl-shaped), prominently ciliate, and are leaves usually ciliate at the base?",
            "YES — lower calyx teeth long-subulate; prominently and regularly ciliate; leaves basally ciliate",
            "NO — lower calyx teeth shortly lanceolate to subulate; leaves usually WITHOUT basal cilia"
        )
        if answer46 == "a":
            return 36  # Thymus

        # Not Thymus
        answer47 = ask_question(
            "Is the CALYX TUBE strongly CURVED or gibbous (swollen/humped) below?",
            "YES — calyx tube strongly curved or gibbous below",
            "NO — calyx tube roughly straight; teeth may be ciliate or not"
        )
        if answer47 == "a":
            answer48 = ask_question(
                "Is the calyx tube strongly CURVED with long-ciliate teeth? Are they perennials?",
                "YES — tube strongly curved; teeth long-ciliate; perennials",
                "NO — tube gibbous (humped) below, constricted above; annuals or perennials"
            )
            if answer48 == "a":
                return 32  # Clinopodium
            else:
                return 33  # Acinos

        # Calyx tube straight
        answer49 = ask_question(
            "Are the teeth of the CALYX LOWER LIP clearly CILIATE (fringed with hairs)? Are the leaves petiolate?",
            "YES — lower lip teeth clearly ciliate; leaves petiolate",
            "NO — lower lip teeth not or scarcely ciliate; leaves petiolate or subsessile"
        )
        if answer49 == "a":
            return 31  # Calamintha

        answer50 = ask_question(
            "Are the leaves SUBSESSILE and CUNEATE (wedge-shaped), conduplicate (folded) when young?",
            "YES — subsessile, cuneate, conduplicate when young; calyx 10-13-veined; stamens divergent",
            "NO — leaves petiolate, flat or with revolute margins; calyx 5-13(-15)-veined; stamens parallel or convergent"
        )
        if answer50 == "a":
            return 30  # Satureja

        answer51 = ask_question(
            "How big is the calyx and what is the inflorescence?",
            "Calyx 1.5-6 mm, 13-15-veined; corolla tube INSIDE calyx; inflorescence often cymose",
            "Calyx more than 6 mm, 5-10-veined; corolla tube EXSERTED from calyx; inflorescence of distant/close verticillasters, not cymose"
        )
        if answer51 == "a":
            return 34  # Micromeria
        else:
            return 19  # Stachys

    # Calyx throat glabrous or weakly hairy
    answer52 = ask_question(
        "Are the BRACTEOLES subulate (awl-shaped), spinose (spiny), and deflexed? Is the upper calyx lip rigid with a single 4-8 mm spine?",
        "YES — subulate spinose deflexed bracteoles; upper calyx lip rigid with 1 large spine",
        "NO — bracteoles herbaceous (leaf-like), erect or spreading; upper calyx lip not as above"
    )
    if answer52 == "a":
        return 15  # Moluccella

    answer53 = ask_question(
        "Is the calyx CLEARLY BILABIATE (two-lipped)?",
        "YES — calyx clearly 2-lipped",
        "NO — calyx not or indistinctly bilabiate"
    )

    if answer53 == "a":
        answer54 = ask_question(
            "Is the plant a SHRUB (± glabrous) with verticillasters in terminal leafy racemes and fleshy black fruit?",
            "YES — shrub; glabrous; terminal leafy racemes; fleshy black fruit",
            "NO — herbs or suffruticose (woody at base); prominent indumentum; fruit dry"
        )
        if answer54 == "a":
            return 5  # Prasium

        answer55 = ask_question(
            "Are the flowers borne in UPPER LEAF AXILS (not in bracts dissimilar to leaves)?",
            "YES — flowers in upper leaf axils",
            "NO — flowers in axils of BRACTS that are different from the leaves"
        )
        if answer55 == "a":
            answer56 = ask_question(
                "How large is the corolla?",
                "Corolla about 35 mm; pedicels 6-8 mm",
                "Corolla about 8-15 mm; pedicels about 3 mm"
            )
            if answer56 == "a":
                return 7   # Melittis
            else:
                return 20  # Melissa

        # Flowers in bracts
        answer57 = ask_question(
            "Are the leaves SUBSESSILE and cuneate, conduplicate when young, glandular-punctate? Is the calyx 10-13-veined?",
            "YES — subsessile, cuneate, conduplicate, glandular; calyx 10-13-veined",
            "NO — leaves petiolate, ovate to oblong; calyx 5-10-veined"
        )
        if answer57 == "a":
            return 30  # Satureja
        else:
            return 18  # Sideritis

    # Calyx not bilabiate
    # Final few genera
    answer58 = ask_question(
        "Is the inflorescence in PANICLES or CORYMBS with prominent overlapping bracts hiding calyces?",
        "YES — panicles or corymbs; prominent imbricate bracts hiding calyces",
        "NO — bracts inconspicuous; not hiding calyces"
    )
    if answer58 == "a":
        return 28  # Origanum

    answer59 = ask_question(
        "Does the corolla have 4 SUBEQUAL (nearly equal) lobes? Are the leaves ovate and aromatic? Damp habitat?",
        "YES — 4 subequal lobes; damp places; rhizomes rooting at nodes",
        "NO — 5 unequal lobes; dry places"
    )
    if answer59 == "a":
        return 39  # Mentha

    answer60 = ask_question(
        "Are ALL PARTS of the plant covered in long, sturdy hairs? Do the calyces have 10-20 ribs?",
        "YES — long sturdy hairs throughout; calyces 10-20 ribbed",
        "NO — hairs shorter; calyces fewer-ribbed"
    )
    if answer60 == "a":
        return 17  # Marrubium

    return 19  # Stachys (default for remaining)


# -----------------------------------------------------------
# DISPLAY FUNCTIONS
# -----------------------------------------------------------

def show_plant_info(genus_number):
    """
    Display all information about a plant genus.
    """
    if genus_number not in GENERA:
        print("Sorry, genus not found!")
        return

    plant = GENERA[genus_number]
    print()
    print("=" * 60)
    print(f"  RESULT: Genus {genus_number}. {plant['name']}")
    print("=" * 60)
    print(f"  Common name  : {plant['common']}")
    print(f"  Turkish name : {plant['turkish']}")
    print()
    print(f"  Description  : {plant['description']}")
    print()
    print(f"  Habitat      : {plant['habitat']}")
    print()
    print(f"  Fun fact     : {plant['fun_fact']}")
    print("=" * 60)


def show_all_genera():
    """
    List all 45 genera in the Labiatae of Turkey.
    """
    print()
    print("=" * 60)
    print("  ALL 45 GENERA OF LABIATAE IN TURKEY")
    print("  (Source: Flora of Turkey, P.H. Davis, Vol. 7)")
    print("=" * 60)

    # Print in two columns, like the book
    numbers = list(GENERA.keys())
    half = len(numbers) // 2 + len(numbers) % 2  # split list in half

    for i in range(half):
        left_num = numbers[i]
        left_name = GENERA[left_num]["name"]
        left_col = f"  {left_num:2}. {left_name}"

        # Check if there is a right column entry
        right_index = i + half
        if right_index < len(numbers):
            right_num = numbers[right_index]
            right_name = GENERA[right_num]["name"]
            right_col = f"{right_num:2}. {right_name}"
            print(f"{left_col:<30}  {right_col}")
        else:
            print(left_col)

    print()


def quiz_mode():
    """
    A fun quiz! The program shows a plant description
    and you try to guess the genus name.
    """
    import random

    print()
    print("*" * 60)
    print("  QUIZ MODE")
    print("  Can you identify the genus from the description?")
    print("*" * 60)

    # Pick 5 random genera for the quiz
    quiz_genera = random.sample(list(GENERA.keys()), 5)
    score = 0

    for i, genus_number in enumerate(quiz_genera):
        plant = GENERA[genus_number]
        print()
        print(f"Question {i + 1} of 5:")
        print(f"  Description : {plant['description']}")
        print(f"  Habitat     : {plant['habitat']}")
        print(f"  Fun fact    : {plant['fun_fact']}")
        print()

        guess = input("  What is the genus name? ").strip()

        # Check answer (case-insensitive)
        if guess.lower() == plant["name"].lower():
            print(f"  CORRECT! Well done!")
            score += 1
        else:
            print(f"  Not quite! The answer was: {plant['name']} ({plant['common']})")

    print()
    print(f"Your score: {score} out of 5")
    if score == 5:
        print("PERFECT SCORE! You are a Labiatae expert!")
    elif score >= 3:
        print("Good job! Keep studying and you'll be an expert soon.")
    else:
        print("Keep practising — these plants are tricky!")


def search_by_name():
    """
    Search for a plant genus by its name (Latin, common, or Turkish).
    """
    print()
    search_term = input("Enter a name to search (Latin, common, or Turkish): ").strip().lower()

    found = False
    for number, plant in GENERA.items():
        if (search_term in plant["name"].lower() or
                search_term in plant["common"].lower() or
                search_term in plant["turkish"].lower()):
            show_plant_info(number)
            found = True

    if not found:
        print(f"  No genus found matching '{search_term}'.")
        print("  Try searching for: sage, nane, thyme, or lavanta")


# -----------------------------------------------------------
# MAIN MENU
# -----------------------------------------------------------

def main():
    """
    The main program — shows a menu and runs the chosen option.
    """
    print()
    print("*" * 60)
    print("  LABIATAE (MINT FAMILY) OF TURKEY")
    print("  Based on: Flora of Turkey by P.H. Davis, Volume 7")
    print()
    print("  The Labiatae family has 45 genera in Turkey and")
    print("  includes some of the most useful and beautiful")
    print("  plants in the world: mint, sage, thyme, lavender,")
    print("  rosemary, and many more!")
    print("*" * 60)

    while True:
        print()
        print("MAIN MENU")
        print("-" * 30)
        print("  1. Identify a plant (use the dichotomous key)")
        print("  2. Browse all 45 genera")
        print("  3. Look up a plant by name")
        print("  4. Quiz mode (test your knowledge!)")
        print("  5. Quit")
        print()

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            genus_number = identify_plant()
            show_plant_info(genus_number)

        elif choice == "2":
            show_all_genera()
            print("Enter a genus NUMBER to see details, or press Enter to go back:")
            sub = input().strip()
            if sub.isdigit():
                show_plant_info(int(sub))

        elif choice == "3":
            search_by_name()

        elif choice == "4":
            quiz_mode()

        elif choice == "5":
            print()
            print("Goodbye! Happy botanising in Turkey!")
            print()
            break

        else:
            print("Please choose a number between 1 and 5.")


# -----------------------------------------------------------
# Run the program
# -----------------------------------------------------------
if __name__ == "__main__":
    main()
