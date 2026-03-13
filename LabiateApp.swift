// ============================================================
// LABIATAE (Mint Family) of Turkey
// Based on: Flora of Turkey by P.H. Davis (Volume 7)
//
// HOW TO USE IN SWIFT PLAYGROUNDS (iPad):
//   1. Open Swift Playgrounds app
//   2. Tap "+" → "App Playground" → Create
//   3. Tap the file in the sidebar (usually "MyApp.swift")
//   4. Select ALL the code and DELETE it
//   5. Paste THIS code in
//   6. Tap the Run button (▶)
// ============================================================

import SwiftUI

// ============================================================
// MARK: - DATA MODELS
// A 'struct' is like a blueprint for an object.
// ============================================================

// Every plant genus has these properties:
struct Plant: Identifiable {
    let id: Int             // Number from the Flora of Turkey book
    let name: String        // Latin genus name
    let common: String      // Common English name
    let turkish: String     // Turkish name
    let description: String // Key features to identify it
    let habitat: String     // Where it grows in Turkey
    let funFact: String     // An interesting fact
}

// The identification key uses steps.
// Each step asks a question and gives 2 options (A or B).
// Each option leads to either another question or a plant.

// 'enum' is a type that can be one of a fixed set of values:
enum KeyResult {
    case step(String)   // Go to another question (by its ID)
    case plant(Int)     // You found it! Show this plant number
}

// Each step in the dichotomous key:
struct KeyStep: Identifiable {
    let id: String         // Label for this step (e.g. "s1", "s2")
    let question: String   // The question to ask
    let optionA: String    // First choice
    let optionB: String    // Second choice
    let nextA: KeyResult   // Where option A leads
    let nextB: KeyResult   // Where option B leads
}

// ============================================================
// MARK: - PLANT DATABASE
// All 45 genera of Labiatae in Turkey
// Source: Flora of Turkey, Vol. 7, P.H. Davis
// ============================================================

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
          funFact: "Its strong unpleasant smell keeps animals from eating it — nature's own pest repellent!"),

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
          funFact: "The name means dragon head in Greek — the flowers look like a dragon's open mouth!"),

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

// ============================================================
// MARK: - IDENTIFICATION KEY DATABASE
// Based on Davis, Flora of Turkey Vol. 7, pp. 37-42
// ============================================================

let keySteps: [KeyStep] = [

    KeyStep(id: "s1",
            question: "How many FERTILE stamens does the flower have?\n(Count only the ones that have pollen)",
            optionA: "2 stamens — the other pair is tiny or missing",
            optionB: "4 stamens — or all reduced/sterile in female flowers",
            nextA: .step("s2"), nextB: .step("s6")),

    KeyStep(id: "s2",
            question: "Look closely at the 2 stamens. Are the CONNECTIVES (the part that joins the 2 pollen sacs) long and lever-like — like a see-saw?",
            optionA: "YES — connectives long and lever-like",
            optionB: "NO — connectives very short, not lever-like",
            nextA: .plant(42), nextB: .step("s3")),          // Salvia

    KeyStep(id: "s3",
            question: "Are the leaves EVERGREEN and NARROW like a needle?",
            optionA: "YES — evergreen, narrow leaves; pale blue corolla 8-12 mm; woody shrub",
            optionB: "NO — leaves deciduous or broader",
            nextA: .plant(3), nextB: .step("s4")),            // Rosmarinus

    KeyStep(id: "s4",
            question: "Where are the FLOWER CLUSTERS (verticillasters)?",
            optionA: "In upper LEAF AXILS, widely spaced; leaves coarsely toothed; non-aromatic",
            optionB: "In TERMINAL SPIKES or HEADS; leaf margins entire or slightly toothed; aromatic",
            nextA: .plant(40), nextB: .step("s5")),           // Lycopus

    KeyStep(id: "s5",
            question: "Is the plant a WOODY SHRUB with arrow-shaped (hastate) leaves?",
            optionA: "YES — woody shrub; hastate leaves; slender cylindrical spikes",
            optionB: "NO — annual or perennial herb; cuneate-based leaves; head or spike inflorescence",
            nextA: .plant(43), nextB: .plant(41)),             // Dorystoechas / Ziziphora

    KeyStep(id: "s6",
            question: "Look at the UPPER LIP of the corolla (top part of the flower). Is it present?",
            optionA: "NO — upper lip absent or very tiny (flower looks 1-lipped)",
            optionB: "YES — upper lip clearly present and well-developed",
            nextA: .step("s7"), nextB: .step("s8")),

    KeyStep(id: "s7",
            question: "Is the inside of the COROLLA TUBE smooth (glabrous)?",
            optionA: "YES — tube smooth inside; lower lip with 5 lobes",
            optionB: "NO — tube usually has a ring of hairs inside; upper lip reduced to 2 small lobes",
            nextA: .plant(2), nextB: .plant(1)),               // Teucrium / Ajuga

    KeyStep(id: "s8",
            question: "Examine the HAIRS on the plant carefully. What type are they?",
            optionA: "BRANCHED — dendroid (tree-like), forked, or stellate (star-shaped)",
            optionB: "SIMPLE (unbranched) only, or the plant has NO hairs at all",
            nextA: .step("s9"), nextB: .step("s14")),

    KeyStep(id: "s9",
            question: "How are the flower clusters arranged?",
            optionA: "In PEDUNCULATE SPIKES (on a long stalk); upper calyx lip has an appendage; stamens droop downward",
            optionB: "NOT in pedunculate spikes; calyx without appendage; stamens not drooping",
            nextA: .plant(4), nextB: .step("s10")),            // Lavandula

    KeyStep(id: "s10",
            question: "Do the STAMENS stick out clearly beyond the upper lip of the corolla?",
            optionA: "YES — stamens clearly exserted beyond upper lip; corolla resupinate (upside-down)",
            optionB: "NO — stamens do not stick out beyond the upper lip",
            nextA: .plant(35), nextB: .step("s11")),           // Cyclotrichium

    KeyStep(id: "s11",
            question: "Is the upper lip of the corolla FALCATE — curved like a sickle or hood?",
            optionA: "YES — upper lip clearly curved or hooded",
            optionB: "NO — upper lip straight or slightly concave",
            nextA: .plant(9), nextB: .step("s12")),            // Phlomis

    KeyStep(id: "s12",
            question: "How many CALYX TEETH are there? What are the hairs like INSIDE the calyx throat?",
            optionA: "5 teeth; calyx throat smooth (glabrous) or weakly hairy",
            optionB: "5-10(-30) teeth; calyx throat has stiff long white hairs",
            nextA: .plant(19), nextB: .step("s13")),           // Stachys

    KeyStep(id: "s13",
            question: "Are the STAMENS hidden (included) inside the corolla tube?",
            optionA: "YES — stamens hidden inside tube; calyx not widened above",
            optionB: "NO — stamens visible; calyx tube widens into a flat star-like toothed limb",
            nextA: .plant(17), nextB: .plant(16)),             // Marrubium / Ballota

    KeyStep(id: "s14",
            question: "Is the FRUITING CALYX greatly enlarged and papery/membranous with broad spreading lobes?",
            optionA: "YES — fruiting calyx greatly enlarged, papery, with broad spreading lobes",
            optionB: "NO — fruiting calyx may enlarge a little but is not papery with broad lobes",
            nextA: .step("s15"), nextB: .step("s17")),

    KeyStep(id: "s15",
            question: "What colour are the LEAVES and COROLLA?",
            optionA: "Leaves woolly; corolla upper lip YELLOW, lower lip orange",
            optionB: "Leaves smooth (glabrous); corolla white, pink, or violet",
            nextA: .plant(8), nextB: .step("s16")),            // Eremostachys

    KeyStep(id: "s16",
            question: "Is the plant a SHRUB with violet UPSIDE-DOWN (resupinate) corollas?",
            optionA: "YES — shrub; violet resupinate corollas; bracteoles herbaceous",
            optionB: "NO — annual with white/pinkish non-resupinate corollas; bracteoles spiny",
            nextA: .plant(25), nextB: .plant(15)),             // Hymenocrater / Moluccella

    KeyStep(id: "s17",
            question: "How many VEINS or RIBS does the CALYX TUBE have?",
            optionA: "15 or more veins; upper (posterior) stamens LONGER than lower (anterior)",
            optionB: "5-14 veins; lower (anterior) stamens LONGER than upper, or all stamens equal",
            nextA: .step("s18"), nextB: .step("s21")),

    KeyStep(id: "s18",
            question: "Do the CALYX SINUSES (gaps between calyx teeth) have a thickened fold at the base?",
            optionA: "YES — thickened fold present; middle lobe of upper calyx lip clearly broader than side lobes",
            optionB: "NO — calyx sinuses without a thickened fold; lobes similar in width",
            nextA: .step("s19"), nextB: .step("s20")),

    KeyStep(id: "s19",
            question: "Does the UPPER LIP of the corolla have 2 internal longitudinal folds inside?",
            optionA: "YES — 2 internal folds; bracteoles prominently veined and aristate-dentate; annuals or perennials",
            optionB: "NO — no internal folds; bracteoles aristate or acuminate; perennials",
            nextA: .plant(24), nextB: .plant(23)),             // Lallemantia / Dracocephalum

    KeyStep(id: "s20",
            question: "Are the flower clusters 2-6-flowered, one-sided (secund), in upper leaf axils? Does the plant spread by stolons (runners)?",
            optionA: "YES — 2-6 flowered, one-sided, plant spreads by stolons",
            optionB: "NO — 6+ flowered; NOT in leaf axils; plant not stoloniferous",
            nextA: .plant(22), nextB: .plant(21)),             // Glechoma / Nepeta

    KeyStep(id: "s21",
            question: "Is the COROLLA TUBE long, slender, and S-shaped (sigmoid)?",
            optionA: "YES — long slender S-shaped tube; calyx lips entire; upper calyx has a small flap",
            optionB: "NO — corolla tube not like that; calyx without a flap",
            nextA: .plant(6), nextB: .step("s22")),            // Scutellaria

    KeyStep(id: "s22",
            question: "Is the upper lip of the corolla FALCATE — curved like a sickle or hood?",
            optionA: "YES — upper lip clearly falcate (curved)",
            optionB: "NO — upper lip straight or slightly concave",
            nextA: .step("s23"), nextB: .step("s29")),

    KeyStep(id: "s23",
            question: "Is the calyx CLEARLY 2-LIPPED (bilabiate)?",
            optionA: "YES — calyx clearly 2-lipped",
            optionB: "NO — calyx not or indistinctly 2-lipped",
            nextA: .step("s24"), nextB: .step("s25")),

    KeyStep(id: "s24",
            question: "Are flower clusters in DENSE TERMINAL SPIKES with bracts hiding the calyces?",
            optionA: "YES — dense terminal spikes; bracts hide calyces; flowers violet or creamy-white; upper lip hairy",
            optionB: "NO — clusters distant; bracts do NOT hide calyces; flowers pinkish; upper lip very hairy/tomentose",
            nextA: .plant(27), nextB: .plant(11)),             // Prunella / Wiedemannia

    KeyStep(id: "s25",
            question: "Do the NUTLETS (small fruits) have TUFTS OF HAIR at the tip?",
            optionA: "YES — nutlets have hair tufts at the apex",
            optionB: "NO — nutlets are smooth (glabrous)",
            nextA: .step("s26"), nextB: .step("s27")),

    KeyStep(id: "s26",
            question: "How big is the corolla and what do the leaves look like?",
            optionA: "Corolla 5-12 mm, pinkish-white; leaves digitately divided or subentire",
            optionB: "Corolla 18-40 mm, yellow or whitish; leaves pinnate, lobed, or subentire",
            nextA: .plant(14), nextB: .plant(8)),              // Leonurus / Eremostachys

    KeyStep(id: "s27",
            question: "Are the THECAE (pollen sacs) smooth? Is the corolla yellow? Does the plant spread by runners?",
            optionA: "YES — smooth thecae; yellow corolla; plant stoloniferous (spreads by runners)",
            optionB: "NO — thecae hairy; corolla white, cream, pink, or purple; not stoloniferous",
            nextA: .plant(12), nextB: .step("s28")),           // Galeobdolon

    KeyStep(id: "s28",
            question: "Are the BRACTEOLES SPINY?",
            optionA: "YES — bracteoles spiny; lower lip of corolla with 2 blunt conical appendages; annuals",
            optionB: "NO — bracteoles not spiny; lower lip with very reduced lateral lobes; annuals or perennials",
            nextA: .plant(13), nextB: .plant(10)),             // Galeopsis / Lamium

    KeyStep(id: "s29",
            question: "Do the STAMENS stick out clearly beyond the upper lip of the corolla?",
            optionA: "YES — stamens clearly exserted beyond the upper lip",
            optionB: "NO — stamens do not stick out beyond the upper lip",
            nextA: .step("s30"), nextB: .step("s39")),

    KeyStep(id: "s30",
            question: "Is the calyx CLEARLY 2-LIPPED with lower teeth markedly different from the upper?",
            optionA: "YES — clearly 2-lipped; lower teeth very different from upper",
            optionB: "NO — calyx not or indistinctly 2-lipped; upper and lower teeth/lobes similar",
            nextA: .step("s31"), nextB: .step("s35")),

    KeyStep(id: "s31",
            question: "Is the plant an ANNUAL or short-lived perennial? Do the stamens droop (declinate)?",
            optionA: "YES — annual or short-lived perennial; stamens declinate (droop downward)",
            optionB: "NO — shrub or woody-based perennial; stamens not drooping",
            nextA: .step("s32"), nextB: .step("s33")),

    KeyStep(id: "s32",
            question: "Is the calyx BENT BACK (deflexed) in fruit? Is the upper calyx lip broadly circular?",
            optionA: "YES — calyx deflexed in fruit; upper lip broadly circular; inflorescence of racemes",
            optionB: "NO — calyx not deflexed; upper lip not broadly circular; inflorescence a spike",
            nextA: .plant(45), nextB: .plant(44)),             // Ocimum / Elsholtzia

    KeyStep(id: "s33",
            question: "Is the calyx tube FLATTENED from top to bottom (dorsally compressed) with 2 fringed flanges on the sides?",
            optionA: "YES — calyx tube dorsally compressed with 2 ciliolate flanges",
            optionB: "NO — calyx tube not dorsally flattened; no flanges",
            nextA: .step("s34"), nextB: .plant(36)),           // → Thymus

    KeyStep(id: "s34",
            question: "What is the INFLORESCENCE TYPE?",
            optionA: "SPICATE (a spike); calyx 13-veined; leaves conduplicate (folded lengthwise)",
            optionB: "CAPITATE (a head); calyx 20-22-veined; leaves subtriquetrious (3-sided)",
            nextA: .plant(38), nextB: .plant(37)),             // Thymbra / Coridothymus

    KeyStep(id: "s35",
            question: "Is the inflorescence in PANICLES or CORYMBS with prominent overlapping bracts hiding the calyces?",
            optionA: "YES — panicles or corymbs; prominent imbricate bracts usually hiding calyces",
            optionB: "NO — bracts inconspicuous; not hiding calyces",
            nextA: .plant(28), nextB: .step("s36")),           // Origanum

    KeyStep(id: "s36",
            question: "Does the corolla have 4 NEARLY EQUAL LOBES? Does the plant grow in DAMP places with creeping rhizomes?",
            optionA: "YES — 4 subequal lobes; damp habitat; rhizomes root at nodes",
            optionB: "NO — 5 unequal lobes; dry places; no creeping rhizomes",
            nextA: .plant(39), nextB: .step("s37")),           // Mentha

    KeyStep(id: "s37",
            question: "Are the leaves OVATE to SUBORBICULAR? Is the corolla resupinate (upside-down)? Are the thecae parallel?",
            optionA: "YES — leaves ovate to suborbicular; corolla resupinate; thecae parallel",
            optionB: "NO — leaves linear to linear-lanceolate; corolla not resupinate; thecae divergent",
            nextA: .plant(35), nextB: .step("s38")),           // Cyclotrichium

    KeyStep(id: "s38",
            question: "Is the calyx tubular (6-8 mm) with thickened folds at the base of the sinuses?",
            optionA: "YES — tubular, 6-8 mm; thickened folds at sinus bases; corolla violet-blue",
            optionB: "NO — ovate-campanulate, 3-4(-5) mm; no thickened folds; corolla white",
            nextA: .plant(26), nextB: .plant(30)),             // Hyssopus / Satureja

    KeyStep(id: "s39",
            question: "Does the CALYX THROAT have a BEARD — a ring of stiff, thick white hairs?",
            optionA: "YES — calyx throat has a beard of stiff thick white hairs",
            optionB: "NO — calyx throat smooth or with only a few weak hairs",
            nextA: .step("s40"), nextB: .step("s52")),

    KeyStep(id: "s40",
            question: "Does the corolla have 4 NEARLY EQUAL LOBES? Does the plant grow in DAMP places with rhizomes?",
            optionA: "YES — 4 subequal lobes; damp places; rhizomes rooting at nodes",
            optionB: "NO — 5 unequal lobes (2 upper, 3 lower); dry places; procumbent or erect",
            nextA: .plant(39), nextB: .step("s41")),           // Mentha

    KeyStep(id: "s41",
            question: "Is the calyx dorsally COMPRESSED with 2 lateral fringed (ciliolate) flanges?",
            optionA: "YES — calyx compressed; 2 ciliolate flanges",
            optionB: "NO — calyx not dorsally flattened; no flanges",
            nextA: .step("s42"), nextB: .step("s43")),

    KeyStep(id: "s42",
            question: "What is the INFLORESCENCE TYPE?",
            optionA: "SPICATE (spike); calyx 13-veined; leaves conduplicate",
            optionB: "CAPITATE (head); calyx 20-22-veined; leaves triquetrious",
            nextA: .plant(38), nextB: .plant(37)),             // Thymbra / Coridothymus

    KeyStep(id: "s43",
            question: "Is the inflorescence in PANICLES or CORYMBS with prominent overlapping bracts hiding the calyces?",
            optionA: "YES — panicles or corymbs; prominent overlapping bracts hiding calyces",
            optionB: "NO — bracts inconspicuous; not hiding calyces",
            nextA: .plant(28), nextB: .step("s44")),           // Origanum

    KeyStep(id: "s44",
            question: "Do ALL parts of the plant have LONG, STURDY HAIRS? Do the calyces have 10-20(-30) ribs?",
            optionA: "YES — long sturdy hairs throughout; calyces 10-20(-30)-ribbed",
            optionB: "NO — hairs short, crisp, or antrorse/retrorse; calyces 5-13(-15)-veined",
            nextA: .step("s45"), nextB: .step("s46")),

    KeyStep(id: "s45",
            question: "Are the stamens INSIDE (included in) the corolla tube? Is the calyx NOT widened above the tube?",
            optionA: "YES — stamens inside tube; calyx not widened above",
            optionB: "NO — stamens NOT inside tube; calyx tube widens into a flat toothed limb",
            nextA: .plant(17), nextB: .plant(16)),             // Marrubium / Ballota

    KeyStep(id: "s46",
            question: "Are the LOWER CALYX TEETH long and awl-shaped (subulate) AND prominently fringed with hairs? Are leaves basally ciliate?",
            optionA: "YES — lower teeth long-subulate, prominently ciliate; leaves usually basally ciliate",
            optionB: "NO — lower teeth shorter; leaves usually without basal cilia",
            nextA: .plant(36), nextB: .step("s47")),           // Thymus

    KeyStep(id: "s47",
            question: "Is the CALYX TUBE strongly CURVED or gibbous (humped/swollen) below?",
            optionA: "YES — calyx tube strongly curved or gibbous (humped) below",
            optionB: "NO — calyx tube roughly straight",
            nextA: .step("s48"), nextB: .step("s49")),

    KeyStep(id: "s48",
            question: "Is the calyx tube strongly CURVED (not just humped) with long hair-fringed teeth? Are they perennials?",
            optionA: "YES — tube strongly curved; teeth long-ciliate; perennials",
            optionB: "NO — tube gibbous (humped) below, constricted above; annuals or perennials",
            nextA: .plant(32), nextB: .plant(33)),             // Clinopodium / Acinos

    KeyStep(id: "s49",
            question: "Are the LOWER CALYX LIP TEETH clearly fringed with hairs (ciliate)? Are the leaves petiolate (on stalks)?",
            optionA: "YES — lower lip teeth clearly ciliate; leaves petiolate",
            optionB: "NO — lower lip teeth not or scarcely ciliate; leaves petiolate or subsessile",
            nextA: .plant(31), nextB: .step("s50")),           // Calamintha

    KeyStep(id: "s50",
            question: "Are leaves SUBSESSILE and CUNEATE (wedge-shaped), folded (conduplicate) when young? Calyx 10-13-veined?",
            optionA: "YES — subsessile, cuneate, conduplicate when young; calyx 10-13-veined; stamens divergent",
            optionB: "NO — leaves petiolate, flat or with revolute margins; calyx 5-13(-15)-veined; stamens parallel",
            nextA: .plant(30), nextB: .step("s51")),           // Satureja

    KeyStep(id: "s51",
            question: "Is the calyx 1.5-6 mm with 13-15 veins, with the corolla tube INSIDE (not sticking out of) the calyx?",
            optionA: "YES — calyx 1.5-6 mm, 13-15-veined; corolla tube inside calyx; inflorescence often cymose",
            optionB: "NO — calyx 6+ mm, 5-10-veined; corolla tube sticks out; not cymose",
            nextA: .plant(34), nextB: .plant(19)),             // Micromeria / Stachys

    KeyStep(id: "s52",
            question: "Are the BRACTEOLES awl-shaped, spiny, and bent back (deflexed)? Is the upper calyx lip rigid with a single 4-8 mm spine?",
            optionA: "YES — awl-shaped, spiny, deflexed bracteoles; upper calyx lip rigid with 1 large spine",
            optionB: "NO — bracteoles herbaceous (leaf-like), erect or spreading; upper calyx lip not like that",
            nextA: .plant(15), nextB: .step("s53")),           // Moluccella

    KeyStep(id: "s53",
            question: "Is the calyx CLEARLY 2-LIPPED (bilabiate)?",
            optionA: "YES — calyx clearly 2-lipped",
            optionB: "NO — calyx not or indistinctly 2-lipped",
            nextA: .step("s54"), nextB: .step("s58")),

    KeyStep(id: "s54",
            question: "Is the plant a SHRUB (nearly glabrous) with fleshy BLACK fruit and flowers in terminal leafy racemes?",
            optionA: "YES — shrub; nearly glabrous; terminal leafy racemes; fleshy black fruit",
            optionB: "NO — herbs or suffruticose (woody at base); prominent hairs; fruit dry",
            nextA: .plant(5), nextB: .step("s55")),            // Prasium

    KeyStep(id: "s55",
            question: "Are the flowers in UPPER LEAF AXILS (not in bracts that are different from leaves)?",
            optionA: "YES — flowers in upper leaf axils",
            optionB: "NO — flowers in axils of BRACTS that are different from the leaves",
            nextA: .step("s56"), nextB: .step("s57")),

    KeyStep(id: "s56",
            question: "How large is the COROLLA?",
            optionA: "About 35 mm (large!); pedicels 6-8 mm",
            optionB: "About 8-15 mm (smaller); pedicels about 3 mm",
            nextA: .plant(7), nextB: .plant(20)),              // Melittis / Melissa

    KeyStep(id: "s57",
            question: "Are the leaves SUBSESSILE and cuneate, conduplicate when young, glandular-punctate? Calyx 10-13-veined?",
            optionA: "YES — subsessile, cuneate, conduplicate, glandular; calyx 10-13-veined",
            optionB: "NO — leaves petiolate, ovate to oblong; calyx 5-10-veined",
            nextA: .plant(30), nextB: .plant(18)),             // Satureja / Sideritis

    KeyStep(id: "s58",
            question: "Is the inflorescence in PANICLES or CORYMBS with prominent overlapping bracts hiding the calyces?",
            optionA: "YES — panicles or corymbs; prominent imbricate bracts hiding calyces",
            optionB: "NO — bracts inconspicuous",
            nextA: .plant(28), nextB: .step("s59")),           // Origanum

    KeyStep(id: "s59",
            question: "Does the corolla have 4 NEARLY EQUAL LOBES? Does the plant grow in DAMP places with rhizomes rooting at nodes?",
            optionA: "YES — 4 subequal lobes; damp places; rhizomes rooting at nodes",
            optionB: "NO — 5 unequal lobes; dry places",
            nextA: .plant(39), nextB: .step("s60")),           // Mentha

    KeyStep(id: "s60",
            question: "Do ALL parts of the plant have LONG STURDY HAIRS? Do the calyces have 10-20 ribs?",
            optionA: "YES — long sturdy hairs throughout; calyces 10-20-ribbed",
            optionB: "NO — hairs shorter; calyces fewer-ribbed",
            nextA: .plant(17), nextB: .plant(19)),             // Marrubium / Stachys
]

// Helper functions to look up a step or plant by ID
func findStep(_ id: String) -> KeyStep? {
    keySteps.first { $0.id == id }
}
func findPlant(_ id: Int) -> Plant? {
    allPlants.first { $0.id == id }
}

// ============================================================
// MARK: - VIEWS
// SwiftUI views are the building blocks of the app's screen.
// ============================================================

// The root view — shows a tab bar with 4 sections
struct ContentView: View {
    var body: some View {
        TabView {
            BrowseView()
                .tabItem { Label("Browse", systemImage: "list.bullet") }

            IdentifyView()
                .tabItem { Label("Identify", systemImage: "magnifyingglass") }

            SearchView()
                .tabItem { Label("Search", systemImage: "text.magnifyingglass") }

            QuizView()
                .tabItem { Label("Quiz", systemImage: "questionmark.circle") }
        }
        .tint(.green)
    }
}

// ============================================================
// MARK: - BROWSE TAB
// A scrollable list of all 45 genera
// ============================================================

struct BrowseView: View {
    var body: some View {
        NavigationView {
            List(allPlants) { plant in
                NavigationLink(destination: PlantDetailView(plant: plant)) {
                    VStack(alignment: .leading, spacing: 4) {
                        HStack {
                            // Genus number
                            Text("\(plant.id).")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                            // Latin name in italics
                            Text(plant.name)
                                .font(.headline)
                                .italic()
                            Spacer()
                            // Common name
                            Text(plant.common)
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                        // Turkish name in green
                        Text(plant.turkish)
                            .font(.caption)
                            .foregroundStyle(.green)
                    }
                    .padding(.vertical, 2)
                }
            }
            .navigationTitle("45 Genera of Labiatae")
        }
    }
}

// ============================================================
// MARK: - PLANT DETAIL VIEW
// Shows all information about one plant
// ============================================================

struct PlantDetailView: View {
    let plant: Plant

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {

                // Header
                VStack(alignment: .leading, spacing: 8) {
                    Text("Genus \(plant.id)")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Text(plant.name)
                        .font(.largeTitle).bold().italic()
                    Text(plant.common)
                        .font(.title2).foregroundStyle(.secondary)
                    Label(plant.turkish, systemImage: "flag")
                        .font(.subheadline).foregroundStyle(.green)
                }
                .padding()
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Color.green.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))

                // Info cards
                infoCard(icon: "leaf",       title: "Key Features",      text: plant.description)
                infoCard(icon: "mountain.2", title: "Habitat in Turkey",  text: plant.habitat)
                infoCard(icon: "star",        title: "Fun Fact",           text: plant.funFact)

                Text("Source: Flora of Turkey, Vol. 7 — P.H. Davis")
                    .font(.caption).foregroundStyle(.secondary)
            }
            .padding()
        }
        .navigationTitle(plant.name)
        .navigationBarTitleDisplayMode(.inline)
    }

    // A reusable card widget — used 3 times above
    func infoCard(icon: String, title: String, text: String) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            Label(title, systemImage: icon)
                .font(.headline).foregroundStyle(.green)
            Text(text)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color(.secondarySystemBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}

// ============================================================
// MARK: - IDENTIFY TAB
// The dichotomous key — walks you through A/B questions
// ============================================================

struct IdentifyView: View {
    // '@State' means: when this variable changes, redraw the view
    @State private var currentStep: KeyStep? = findStep("s1")
    @State private var foundPlant: Plant?    = nil
    @State private var questionCount: Int    = 0
    @State private var history: [KeyStep]    = []  // For the Back button

    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {

                    if let plant = foundPlant {
                        ResultView(plant: plant, questionCount: questionCount)
                    } else if let step = currentStep {
                        questionCard(step: step)
                    }

                    // Navigation buttons
                    HStack(spacing: 12) {
                        if !history.isEmpty {
                            Button("← Back") { goBack() }
                                .buttonStyle(.bordered)
                        }
                        Button("Reset") { reset() }
                            .buttonStyle(.borderedProminent)
                            .tint(.green)
                    }
                }
                .padding()
            }
            .navigationTitle("Identify Your Plant")
        }
    }

    // The card showing a question with A and B buttons
    func questionCard(step: KeyStep) -> some View {
        VStack(spacing: 16) {
            Text("Question \(questionCount + 1)")
                .font(.caption).foregroundStyle(.secondary)

            Text(step.question)
                .font(.body)
                .multilineTextAlignment(.center)
                .padding()
                .background(Color.green.opacity(0.08))
                .clipShape(RoundedRectangle(cornerRadius: 12))

            Text("Look carefully at your plant before answering!")
                .font(.caption).foregroundStyle(.secondary).italic()

            // Option A button
            answerButton(label: "A", text: step.optionA, color: .blue) {
                choose(step.nextA)
            }

            // Option B button
            answerButton(label: "B", text: step.optionB, color: .orange) {
                choose(step.nextB)
            }
        }
    }

    // Reusable answer button (used for A and B)
    func answerButton(label: String, text: String, color: Color, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            HStack(alignment: .top, spacing: 12) {
                Text(label)
                    .font(.headline)
                    .frame(width: 28, height: 28)
                    .background(color.opacity(0.2))
                    .clipShape(Circle())
                Text(text)
                    .font(.body)
                    .multilineTextAlignment(.leading)
                Spacer()
            }
            .padding()
            .frame(maxWidth: .infinity)
            .background(color.opacity(0.06))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .overlay(
                RoundedRectangle(cornerRadius: 12)
                    .stroke(color.opacity(0.3), lineWidth: 1)
            )
        }
        .foregroundStyle(.primary)
    }

    // Called when the user taps A or B
    func choose(_ result: KeyResult) {
        if let step = currentStep { history.append(step) }
        questionCount += 1
        switch result {
        case .step(let id):
            currentStep = findStep(id)
            foundPlant  = nil
        case .plant(let id):
            foundPlant  = findPlant(id)
            currentStep = nil
        }
    }

    func goBack() {
        if let prev = history.popLast() {
            currentStep   = prev
            foundPlant    = nil
            questionCount = max(0, questionCount - 1)
        }
    }

    func reset() {
        currentStep   = findStep("s1")
        foundPlant    = nil
        questionCount = 0
        history       = []
    }
}

// The result screen shown after the key reaches a plant
struct ResultView: View {
    let plant: Plant
    let questionCount: Int

    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "checkmark.circle.fill")
                .font(.system(size: 64))
                .foregroundStyle(.green)

            Text("Identified in \(questionCount) questions!")
                .font(.subheadline).foregroundStyle(.secondary)

            Text(plant.name)
                .font(.largeTitle).bold().italic()
            Text(plant.common)
                .font(.title2).foregroundStyle(.secondary)
            Label(plant.turkish, systemImage: "flag")
                .foregroundStyle(.green)

            VStack(alignment: .leading, spacing: 12) {
                factRow(icon: "leaf",       text: plant.description)
                Divider()
                factRow(icon: "mountain.2", text: plant.habitat)
                Divider()
                factRow(icon: "star",        text: plant.funFact)
            }
            .padding()
            .background(Color(.secondarySystemBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))
        }
    }

    func factRow(icon: String, text: String) -> some View {
        HStack(alignment: .top, spacing: 10) {
            Image(systemName: icon).foregroundStyle(.green).frame(width: 20)
            Text(text)
        }
    }
}

// ============================================================
// MARK: - SEARCH TAB
// Live search by Latin, English, or Turkish name
// ============================================================

struct SearchView: View {
    @State private var query = ""

    // 'var' with a computed value — filters automatically as query changes
    var results: [Plant] {
        guard !query.isEmpty else { return allPlants }
        return allPlants.filter {
            $0.name.localizedCaseInsensitiveContains(query)    ||
            $0.common.localizedCaseInsensitiveContains(query)  ||
            $0.turkish.localizedCaseInsensitiveContains(query) ||
            $0.description.localizedCaseInsensitiveContains(query)
        }
    }

    var body: some View {
        NavigationView {
            List(results) { plant in
                NavigationLink(destination: PlantDetailView(plant: plant)) {
                    VStack(alignment: .leading, spacing: 4) {
                        Text(plant.name).font(.headline).italic()
                        Text("\(plant.common) • \(plant.turkish)")
                            .font(.caption).foregroundStyle(.secondary)
                    }
                }
            }
            .searchable(text: $query, prompt: "Try: sage, nane, thyme, lavanta...")
            .navigationTitle("Search Plants")
        }
    }
}

// ============================================================
// MARK: - QUIZ TAB
// Guess the genus from clues
// ============================================================

struct QuizView: View {
    @State private var quizPlants:   [Plant] = []
    @State private var index:        Int     = 0
    @State private var score:        Int     = 0
    @State private var guess:        String  = ""
    @State private var showAnswer:   Bool    = false
    @State private var isCorrect:    Bool    = false
    @State private var finished:     Bool    = false

    var current: Plant? { index < quizPlants.count ? quizPlants[index] : nil }

    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    if quizPlants.isEmpty      { startScreen }
                    else if finished            { resultsScreen }
                    else if let p = current     { questionScreen(p) }
                }
                .padding()
            }
            .navigationTitle("Quiz Mode")
        }
    }

    // ── Start screen ─────────────────────────────────────────
    var startScreen: some View {
        VStack(spacing: 24) {
            Image(systemName: "questionmark.circle.fill")
                .font(.system(size: 80)).foregroundStyle(.green)
            Text("Test Your Knowledge!")
                .font(.title).bold()
            Text("You will be shown 5 plants.\nRead the clues and type the genus name.")
                .multilineTextAlignment(.center).foregroundStyle(.secondary)
            Button("Start Quiz") { startQuiz() }
                .buttonStyle(.borderedProminent).tint(.green).controlSize(.large)
        }
    }

    // ── Question screen ───────────────────────────────────────
    func questionScreen(_ plant: Plant) -> some View {
        VStack(spacing: 16) {
            // Progress bar
            ProgressView(value: Double(index), total: 5)
                .tint(.green)
            HStack {
                Text("Question \(index + 1) of 5").font(.caption).foregroundStyle(.secondary)
                Spacer()
                Text("Score: \(score)").font(.caption.bold()).foregroundStyle(.green)
            }

            // Clues card
            VStack(alignment: .leading, spacing: 12) {
                clueRow(icon: "leaf",       label: "Description", text: plant.description)
                Divider()
                clueRow(icon: "mountain.2", label: "Habitat",     text: plant.habitat)
                Divider()
                clueRow(icon: "star",        label: "Fun Fact",    text: plant.funFact)
            }
            .padding()
            .background(Color(.secondarySystemBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))

            if !showAnswer {
                // Answer input
                TextField("Type the genus name...", text: $guess)
                    .textFieldStyle(.roundedBorder)
                    .autocorrectionDisabled()
                    .textInputAutocapitalization(.words)

                Button("Submit") { checkAnswer(plant) }
                    .buttonStyle(.borderedProminent).tint(.green)
                    .disabled(guess.trimmingCharacters(in: .whitespaces).isEmpty)
            } else {
                // Feedback
                VStack(spacing: 6) {
                    if isCorrect {
                        Label("Correct! Well done!", systemImage: "checkmark.circle.fill")
                            .foregroundStyle(.green).font(.headline)
                    } else {
                        Label("Not quite!", systemImage: "xmark.circle.fill")
                            .foregroundStyle(.red).font(.headline)
                        Text("Answer: \(plant.name) (\(plant.common))")
                            .foregroundStyle(.secondary)
                    }
                }
                .padding()
                .frame(maxWidth: .infinity)
                .background(isCorrect ? Color.green.opacity(0.1) : Color.red.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))

                Button("Next →") { nextQuestion() }
                    .buttonStyle(.borderedProminent).tint(.green)
            }
        }
    }

    // ── Results screen ────────────────────────────────────────
    var resultsScreen: some View {
        VStack(spacing: 20) {
            Image(systemName: score >= 4 ? "star.circle.fill" : "hand.thumbsup.fill")
                .font(.system(size: 80)).foregroundStyle(.green)
            Text("Quiz Complete!").font(.title).bold()
            Text("You scored \(score) out of 5").font(.title2)
            Text(message).multilineTextAlignment(.center).foregroundStyle(.secondary)
            Button("Play Again") { startQuiz() }
                .buttonStyle(.borderedProminent).tint(.green).controlSize(.large)
        }
    }

    var message: String {
        switch score {
        case 5: return "PERFECT SCORE! You are a Labiatae expert!"
        case 4: return "Excellent! Almost perfect!"
        case 3: return "Good job! Keep studying!"
        case 2: return "Not bad — try again to improve."
        default: return "Keep practising — these plants are tricky!"
        }
    }

    // ── Helper views ─────────────────────────────────────────
    func clueRow(icon: String, label: String, text: String) -> some View {
        VStack(alignment: .leading, spacing: 4) {
            Label(label, systemImage: icon)
                .font(.caption).foregroundStyle(.secondary)
            Text(text)
        }
    }

    // ── Logic functions ───────────────────────────────────────
    func startQuiz() {
        quizPlants = Array(allPlants.shuffled().prefix(5))
        index      = 0
        score      = 0
        guess      = ""
        showAnswer = false
        isCorrect  = false
        finished   = false
    }

    func checkAnswer(_ plant: Plant) {
        isCorrect = guess.trimmingCharacters(in: .whitespaces)
                         .lowercased() == plant.name.lowercased()
        if isCorrect { score += 1 }
        showAnswer = true
    }

    func nextQuestion() {
        index     += 1
        guess      = ""
        showAnswer = false
        isCorrect  = false
        if index >= quizPlants.count { finished = true }
    }
}

// ============================================================
// MARK: - APP ENTRY POINT
// '@main' tells Swift: start the app here.
// ============================================================

@main
struct LabiateApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
