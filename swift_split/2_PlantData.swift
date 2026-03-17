// ============================================================
// FILE 2 of 5: PlantData.swift
// All 45 genera of Labiatae in Turkey
// Source: Flora of Turkey, Vol. 7, P.H. Davis
// ============================================================

import SwiftUI

let allPlants: [Plant] = [
    Plant(id: 1,  name: "Ajuga",         common: "Bugle",                 turkish: "Mayasıl otu",
          description: "Low-growing herbs. Upper lip of corolla absent or very tiny. Lower lip has 5 lobes.",
          habitat: "Meadows, roadsides, forest edges",
          funFact: "Used in traditional medicine to treat wounds and fevers."),

    Plant(id: 2,  name: "Teucrium",      common: "Germander",             turkish: "Kıbrıscık / Mahmut otu",
          description: "Herbs or shrubs. Corolla 1-lipped with 5-lobed lower lip. Tube smooth inside.",
          habitat: "Rocky hillsides, dry grasslands, scrub",
          funFact: "Wall Germander has been used as a medicine since ancient Greek times."),

    Plant(id: 3,  name: "Rosmarinus",    common: "Rosemary",              turkish: "Biberiye",
          description: "Evergreen shrub with narrow needle-like leaves. Pale blue flowers. Very aromatic.",
          habitat: "Dry rocky hillsides near the coast",
          funFact: "Used in cooking worldwide and is a symbol of remembrance."),

    Plant(id: 4,  name: "Lavandula",     common: "Lavender",              turkish: "Lavanta",
          description: "Aromatic shrubs with star-shaped or branched hairs. Purple flowers in long spikes.",
          habitat: "Dry rocky places, cultivated widely",
          funFact: "Turkey is one of the world's top producers of lavender oil."),

    Plant(id: 5,  name: "Prasium",       common: "Prasium",               turkish: "Prasiyum",
          description: "Small evergreen shrub. Shiny fleshy black fruits. White or pale purple flowers.",
          habitat: "Maquis scrubland near the coast",
          funFact: "One of the few Labiatae with fleshy berries instead of dry nutlets."),

    Plant(id: 6,  name: "Scutellaria",   common: "Skullcap",              turkish: "Mıknatısotu",
          description: "Herbs with a unique calyx: the upper lip has a small shield-like flap on top.",
          habitat: "Moist meadows, stream banks, rocky slopes",
          funFact: "Being studied by scientists for potential use in cancer treatment."),

    Plant(id: 7,  name: "Melittis",      common: "Bastard Balm",          turkish: "Arınanesi",
          description: "Large showy flowers (up to 35 mm!) in upper leaf axils. Strongly honey-scented.",
          habitat: "Shaded woodland, forest edges",
          funFact: "Its name comes from the Greek word for bee — bees absolutely love its flowers."),

    Plant(id: 8,  name: "Eremostachys",  common: "Desert Candle",         turkish: "Çöl şamdanı",
          description: "Tall woolly herbs. Yellow upper lip, orange lower lip. Very distinctive!",
          habitat: "Dry steppe and semi-desert areas of eastern Turkey",
          funFact: "Can grow over 1 metre tall and is hard to miss on the dry steppes."),

    Plant(id: 9,  name: "Phlomis",       common: "Jerusalem Sage",        turkish: "Şalba / Fener otu",
          description: "Woolly herbs or shrubs. Upper lip of corolla strongly curved like a hood (falcate).",
          habitat: "Rocky slopes, scrub, dry hills",
          funFact: "In Turkey, leaves are dried and made into herbal tea called 'çay dağı'."),

    Plant(id: 10, name: "Lamium",        common: "Dead Nettle",           turkish: "Ballıbaba",
          description: "Herbs that look like nettles but DO NOT sting! White, pink, or purple flowers.",
          habitat: "Roadsides, disturbed ground, gardens",
          funFact: "White Dead Nettle flowers are edible and can be added to salads."),

    Plant(id: 11, name: "Wiedemannia",   common: "Wiedemannia",           turkish: "Wiedemannya",
          description: "Similar to Prunella. Pinkish flowers with a very hairy (villous) upper lip.",
          habitat: "Moist mountain slopes, stream sides",
          funFact: "Named after German botanist E.J. von Wiedemann who worked in Istanbul."),

    Plant(id: 12, name: "Galeobdolon",   common: "Yellow Archangel",      turkish: "Sarı ölü ısırgan",
          description: "Spreads by runners (stoloniferous). Yellow flowers. Smooth (glabrous) thecae.",
          habitat: "Shaded woodland, hedgerows",
          funFact: "Its runners can spread metres from the parent plant, carpeting the woodland floor."),

    Plant(id: 13, name: "Galeopsis",     common: "Hemp Nettle",           turkish: "Kenevir ısırganı",
          description: "Annual herbs with spiny bracteoles. Lower lip has 2 bump-like appendages at base.",
          habitat: "Arable fields, disturbed ground",
          funFact: "One of the first plants used to demonstrate polyploidy — a key genetics concept!"),

    Plant(id: 14, name: "Leonurus",      common: "Motherwort",            turkish: "Oğulotu / Aslan kuyruğu",
          description: "Tall herbs with deeply divided hand-shaped leaves. Small pinkish-white flowers.",
          habitat: "Roadsides, waste places, near villages",
          funFact: "Used for centuries to calm the heart. Modern research confirms it has heart benefits."),

    Plant(id: 15, name: "Moluccella",    common: "Bells of Ireland",      turkish: "Zil çiçeği",
          description: "The calyx is HUGE and bell-shaped. Small white flowers inside. Very unusual!",
          habitat: "Disturbed ground, field margins",
          funFact: "Despite being called 'Bells of Ireland', it is actually native to Turkey and Syria!"),

    Plant(id: 16, name: "Ballota",       common: "Black Horehound",       turkish: "Ballota / Andız otu",
          description: "Woolly herbs. Calyx tube widens into a toothed flat star-like limb after flowering.",
          habitat: "Roadsides, rocky slopes, waste ground",
          funFact: "Its strong smell stops animals from eating it - a built-in pest repellent!"),

    Plant(id: 17, name: "Marrubium",     common: "Horehound",             turkish: "Topalak / Acı nane",
          description: "White-woolly herbs. Calyx has 5-10 hook-like teeth. Stamens hidden inside tube.",
          habitat: "Dry roadsides, overgrazed areas, waste ground",
          funFact: "Horehound candy and tea are traditional cough remedies — still sold in shops today!"),

    Plant(id: 18, name: "Sideritis",     common: "Ironwort / Mountain Tea", turkish: "Dağ çayı / Demir otu",
          description: "Herbs or small shrubs, often silvery-woolly. Bracts often leaf-like and spiny.",
          habitat: "Rocky mountain slopes, limestone cliffs",
          funFact: "Sideritis tea (dağ çayı) is extremely popular in Turkey for health and enjoyment."),

    Plant(id: 19, name: "Stachys",       common: "Woundwort / Betony",    turkish: "Karabaş / Moruk otu",
          description: "Herbs or shrubs. Calyx with 5 teeth. One of the LARGEST genera in Turkish Labiatae.",
          habitat: "Very varied: meadows, forests, rocky slopes, roadsides",
          funFact: "Turkey has more species of Stachys than almost any other country in the world."),

    Plant(id: 20, name: "Melissa",       common: "Lemon Balm",            turkish: "Melisa / Oğul otu",
          description: "Lemon-scented herb. White or pale pink small flowers. Leaves smell strongly of lemon.",
          habitat: "Woodland edges, hedgerows, stream banks",
          funFact: "Lemon Balm tea is popular in Turkey for calming nerves and helping with sleep."),

    Plant(id: 21, name: "Nepeta",        common: "Catmint",               turkish: "Kedi nanesi",
          description: "Blue or white flowers. Many-flowered clusters not in leaf axils.",
          habitat: "Dry rocky slopes, roadsides",
          funFact: "Cats go wild for catnip (Nepeta cataria) because it mimics cat pheromones!"),

    Plant(id: 22, name: "Glechoma",      common: "Ground Ivy",            turkish: "Yer sarmaşığı",
          description: "Creeping herb with round scalloped leaves. Spreads by stolons (ground runners).",
          habitat: "Shaded moist places, hedgerows, lawns",
          funFact: "Before hops were used, Ground Ivy was the main flavouring in European beer!"),

    Plant(id: 23, name: "Dracocephalum", common: "Dragonhead",            turkish: "Ejderha başı",
          description: "Blue-purple flowers. Bracteoles have pointed (acuminate) tips. Perennial herbs.",
          habitat: "Mountain steppes, rocky slopes",
          funFact: "The name means dragon head in Greek - the flowers look like a dragon mouth!"),

    Plant(id: 24, name: "Lallemantia",   common: "Lallemantia",           turkish: "Lallemantia",
          description: "Unique: upper lip of corolla has 2 internal folds. Bracteoles prominently veined.",
          habitat: "Arable fields, dry disturbed ground",
          funFact: "Seeds contain an oil used in traditional medicine and as food in Central Asia."),

    Plant(id: 25, name: "Hymenocrater",  common: "Hymenocrater",          turkish: "Hymenocrater",
          description: "Shrub with striking violet upside-down (resupinate) corollas. Leaf-like bracteoles.",
          habitat: "Rocky slopes and cliffs in eastern Turkey",
          funFact: "Resupinate means the flower is twisted 180 degrees — the top is actually the bottom!"),

    Plant(id: 26, name: "Hyssopus",      common: "Hyssop",                turkish: "Çördük / Hisop",
          description: "Small aromatic shrub. Tubular calyx with thickened folds. Violet-blue corolla.",
          habitat: "Dry rocky slopes, scrub",
          funFact: "Hyssop is mentioned in the Bible as a purifying herb used in ancient rituals."),

    Plant(id: 27, name: "Prunella",      common: "Selfheal",              turkish: "Ölmez otu / Yaraotu",
          description: "Dense terminal flower heads. Violet flowers. Calyx clearly 2-lipped (bilabiate).",
          habitat: "Meadows, roadsides, lawns, open woodland",
          funFact: "Selfheal was used to heal wounds — modern science confirms it has antimicrobial compounds."),

    Plant(id: 28, name: "Origanum",      common: "Oregano / Marjoram",    turkish: "Kekik / Mercanköşk",
          description: "Aromatic herb. Flowers in panicles or corymbs. Prominent bracts hide the flowers.",
          habitat: "Dry rocky hillsides, scrub",
          funFact: "Turkey exports huge amounts of oregano (kekik). Essential in Turkish cuisine!"),

    Plant(id: 29, name: "Pentapleura",   common: "Pentapleura",           turkish: "Pentapleura",
          description: "A rare genus found only in a small area of Turkey. Related to Hyssopus.",
          habitat: "Rocky limestone areas in southern Turkey",
          funFact: "Pentapleura subulifera is endemic to Turkey — it grows NOWHERE else in the world!"),

    Plant(id: 30, name: "Satureja",      common: "Savory",                turkish: "Sater / Bağ kekiği",
          description: "Small aromatic herbs or shrubs. Leaves often cuneate (wedge-shaped) at the base.",
          habitat: "Rocky limestone slopes, dry hillsides",
          funFact: "Summer Savory is used as a spice, especially to flavour bean dishes."),

    Plant(id: 31, name: "Calamintha",    common: "Calamint",              turkish: "Yaban nanesi",
          description: "Mint-like herbs. Lower calyx lip teeth clearly fringed with hairs (ciliate).",
          habitat: "Rocky slopes, forest edges, scrub",
          funFact: "Smells like a mix of mint and thyme and is sometimes used to make herbal tea."),

    Plant(id: 32, name: "Clinopodium",   common: "Wild Basil",            turkish: "Yaban fesleğeni",
          description: "Hairy herbs. Calyx tube strongly curved. Teeth long and hair-fringed (ciliate).",
          habitat: "Hedgerows, woodland edges, scrub",
          funFact: "Called Wild Basil but is not culinary basil — though it does smell similar!"),

    Plant(id: 33, name: "Acinos",        common: "Basil Thyme",           turkish: "Akinos",
          description: "Small herbs. Calyx tube gibbous (swollen and humped) at the base.",
          habitat: "Dry grassland, arable fields, rocky slopes",
          funFact: "Despite the name Basil Thyme, it is neither a basil nor a thyme!"),

    Plant(id: 34, name: "Micromeria",    common: "Micromeria",            turkish: "Küçük nane",
          description: "Small aromatic herbs. Calyx 1.5-6 mm, 13-15 veined. Corolla tube stays inside calyx.",
          habitat: "Rocky limestone cliffs, walls, scrub",
          funFact: "Some species are used to make herbal tea, collected from wild plants in Turkey."),

    Plant(id: 35, name: "Cyclotrichium", common: "Cyclotrichium",         turkish: "Silindir tüylü",
          description: "Shrubby herbs with star-shaped hairs. Stamens stick out beyond the upper lip.",
          habitat: "Rocky slopes in eastern Anatolia",
          funFact: "A genus found mainly in Turkey and Iran — quite rare globally."),

    Plant(id: 36, name: "Thymus",        common: "Thyme",                 turkish: "Kekik",
          description: "Small aromatic shrubs. Woody base, tiny leaves. Pink or purple flowers. Very fragrant!",
          habitat: "Dry rocky hillsides, grasslands, mountain slopes",
          funFact: "Turkey has over 50 species of wild thyme — more than any other country!"),

    Plant(id: 37, name: "Coridothymus",  common: "Cretan Thyme",          turkish: "Kekik (Girit)",
          description: "Thyme-like shrub. Inflorescence is a HEAD (not a spike). Calyx has 20-22 veins.",
          habitat: "Rocky coastal areas",
          funFact: "Produces a high-quality essential oil used in perfumes and medicines."),

    Plant(id: 38, name: "Thymbra",       common: "Za'atar",               turkish: "Zahter / Kaya kekiği",
          description: "Thyme-like shrub. Inflorescence is a SPIKE. Calyx 13-veined. Leaves folded (conduplicate).",
          habitat: "Rocky limestone hillsides in southern Turkey",
          funFact: "Thymbra spicata is the famous za'atar of the Middle East, used in the popular spice blend."),

    Plant(id: 39, name: "Mentha",        common: "Mint",                  turkish: "Nane",
          description: "Creeping herbs in moist places. Corolla has 4 EQUAL lobes — unusual for Labiatae!",
          habitat: "Stream banks, ditches, wet meadows",
          funFact: "Mint tea (nane çayı) is one of Turkey's most beloved drinks!"),

    Plant(id: 40, name: "Lycopus",       common: "Gipsywort / Bugleweed", turkish: "Kurt ayağı / Çingene otu",
          description: "Herb of wet places. Deeply toothed leaves. Non-aromatic (no smell). Tiny white flowers.",
          habitat: "Riverbanks, marshes, wet meadows",
          funFact: "Historically used to dye fabric black, and gypsies were said to use it to dye their skin."),

    Plant(id: 41, name: "Ziziphora",     common: "Ziziphora",             turkish: "Zizifora",
          description: "Small aromatic herbs. Cuneate-based leaves. Dense head or spike inflorescence.",
          habitat: "Dry steppe, rocky slopes",
          funFact: "Used in traditional medicine across Turkey and Central Asia for digestive problems."),

    Plant(id: 42, name: "Salvia",        common: "Sage",                  turkish: "Adaçayı",
          description: "LARGEST genus in Turkish Labiatae! Unique lever-like stamens. Incredibly diverse.",
          habitat: "Extremely varied: rocky slopes, scrub, meadows, forests",
          funFact: "Turkey has about 100 species of wild sage! Adaçayı is Turkey's most famous herbal tea."),

    Plant(id: 43, name: "Dorystoechas",  common: "Dorystoechas",          turkish: "Dorystoechas",
          description: "Woody shrub with arrow-shaped (hastate) leaves and slender cylindrical spikes.",
          habitat: "Rocky hillsides in southwestern Turkey",
          funFact: "Dorystoechas hastata is ENDEMIC to Turkey — it exists nowhere else on Earth!"),

    Plant(id: 44, name: "Elsholtzia",    common: "Elsholtzia",            turkish: "Elşoltsiya",
          description: "Annual or short-lived herb. Inflorescence a one-sided spike. Stamens droop downward.",
          habitat: "Disturbed ground, roadsides, cultivated areas",
          funFact: "In China, Elsholtzia ciliata is used as a spice and a cold remedy."),

    Plant(id: 45, name: "Ocimum",        common: "Basil",                 turkish: "Fesleğen",
          description: "Annual herb. Calyx bends back (deflexed) in fruit. Upper calyx lip broadly circular.",
          habitat: "Cultivated, occasionally naturalised",
          funFact: "Sweet Basil is one of the world's most important culinary herbs, from tropical Asia."),
]
