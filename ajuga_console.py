# ============================================================
# AJUGA (Bugle) of Turkey — Console Identification App
# Based on: Flora of Turkey, Vol. 7 — P.H. Davis (1982)
# ============================================================
# Works in Pythonista 3 on iPad — no extra libraries needed!
#
# MENU:
#   1. Identify your plant (step-by-step A/B key)
#   2. Browse all 10 species
#   3. Search by keyword
#   4. Quit
# ============================================================

SPECIES = [
    {
        "id": 1,
        "name": "Ajuga chamaepitys subsp. chamaepitys",
        "nickname": "Ground Pine",
        "turkish": "Sari mayasil otu",
        "size": "5-30 cm tall",
        "type": "Annual (lives for one year)",
        "flower_colour": "Yellow, often with red-purple streaks",
        "leaf_shape": "Deeply cut into 3 narrow finger-like lobes. Crush a leaf and it smells like pine trees!",
        "hairiness": "Hairy all over",
        "where_it_grows": "Arable fields, rocky hillsides, disturbed ground. All over Turkey, especially W, C, S Anatolia. 0-1800 m.",
        "when_it_flowers": "March to July",
        "fun_fact": "The most common Ajuga in Turkey. Its pine smell is how it got the name Ground Pine!",
        "how_to_spot_it": "Yellow flowers + deeply cut pine-needle-like leaves + smells of pine",
    },
    {
        "id": 2,
        "name": "Ajuga chamaepitys subsp. chia",
        "nickname": "Chian Ground Pine",
        "turkish": "Sakiz mayasil otu",
        "size": "5-20 cm tall (smaller and more compact)",
        "type": "Annual (lives for one year)",
        "flower_colour": "Yellow, sometimes with purple streaks",
        "leaf_shape": "Like subsp. chamaepitys but the finger-like lobes are SHORTER and WIDER. Still smells like pine.",
        "hairiness": "Hairy",
        "where_it_grows": "Dry rocky hillsides. W and SW Turkey, mostly the Aegean coast and nearby islands. 0-1000 m.",
        "when_it_flowers": "March to June",
        "fun_fact": "Very similar to subsp. chamaepitys but lives mainly near the Aegean coast. Chia refers to the island of Chios.",
        "how_to_spot_it": "Yellow flowers + shorter stubbier leaf lobes + coastal W Turkey",
    },
    {
        "id": 3,
        "name": "Ajuga iva",
        "nickname": "Yellow Bugle",
        "turkish": "Sarmasik mayasil otu",
        "size": "5-20 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "Yellow or creamy-white, sometimes tinged purple",
        "leaf_shape": "Simple, oblong leaves with slightly wavy edges. NOT cut into finger-lobes. Does NOT smell of pine.",
        "hairiness": "Covered in sticky glandular hairs - feels slightly sticky when you touch it",
        "where_it_grows": "Dry open hillsides, rocky slopes, stony ground. W, S, and C Turkey. 0-1500 m.",
        "when_it_flowers": "March to June",
        "fun_fact": "The sticky hairs trap tiny insects. Used in Turkish folk medicine for skin conditions.",
        "how_to_spot_it": "Yellow flowers + simple (not cut) leaves + feels slightly sticky + no pine smell",
    },
    {
        "id": 4,
        "name": "Ajuga orientalis",
        "nickname": "Eastern Bugle",
        "turkish": "Dogu mayasil otu",
        "size": "10-40 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "Blue-violet",
        "leaf_shape": "Oval leaves with scalloped (wavy) edges. Big leaves at the base, smaller ones higher up. Often has a purple tinge.",
        "hairiness": "Softly hairy",
        "where_it_grows": "Meadows, forest clearings, stream sides, rocky slopes. All over Turkey, very common in N, E, C Anatolia. 200-2200 m.",
        "when_it_flowers": "April to July",
        "fun_fact": "One of the most widespread Ajuga in Turkey. Can form big carpets of blue-violet flowers in mountain meadows.",
        "how_to_spot_it": "Blue-violet flowers + soft oval leaves + very common everywhere in Turkey",
    },
    {
        "id": 5,
        "name": "Ajuga reptans",
        "nickname": "Creeping Bugle",
        "turkish": "Surinucu mayasil otu",
        "size": "10-30 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "Blue-violet (very rarely pink or white)",
        "leaf_shape": "Shiny oval leaves with wavy edges. Leaves near the ground are often bronze-purple coloured.",
        "hairiness": "Slightly hairy",
        "where_it_grows": "Damp meadows, shaded woodland edges, shaded banks. N and NW Turkey, mainly the Black Sea coast. 0-1500 m.",
        "when_it_flowers": "April to June",
        "fun_fact": "The ONLY Turkish Ajuga that sends out long creeping runners along the ground, just like strawberry plants!",
        "how_to_spot_it": "Blue-violet flowers + LONG CREEPING RUNNERS along ground + shiny leaves + Black Sea region",
    },
    {
        "id": 6,
        "name": "Ajuga genevensis",
        "nickname": "Blue Bugle",
        "turkish": "Cenevre mayasil otu",
        "size": "10-40 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "Bright blue-violet (rarely pink)",
        "leaf_shape": "Oval leaves with coarse teeth along the edges. Leaves look GREY-GREEN because of dense hairs.",
        "hairiness": "Densely hairy - gives the plant a grey-green colour",
        "where_it_grows": "Dry grassland, meadows, scrubby areas, roadsides. N, W, and C Turkey. 500-2000 m.",
        "when_it_flowers": "April to June",
        "fun_fact": "Looks similar to Creeping Bugle but has NO creeping runners. The grey-green hairy look tells them apart.",
        "how_to_spot_it": "Blue-violet flowers + grey-green hairy leaves + NO creeping runners",
    },
    {
        "id": 7,
        "name": "Ajuga laxmannii",
        "nickname": "White Woolly Bugle",
        "turkish": "Yunlu mayasil otu",
        "size": "10-35 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "Pale yellow or creamy-white",
        "leaf_shape": "Oblong leaves with smooth or slightly wavy edges. The whole plant is covered in thick white woolly hairs!",
        "hairiness": "VERY densely white-woolly - like the plant is wrapped in cotton wool",
        "where_it_grows": "Dry stony slopes, rocky hillsides, steppe grassland. C, E, and SE Turkey - drier inland areas. 600-2000 m.",
        "when_it_flowers": "May to July",
        "fun_fact": "The wooliest Ajuga in Turkey! The white wool helps it survive the hot dry summers of central Anatolia.",
        "how_to_spot_it": "Pale yellow flowers + VERY thick white woolly covering all over the plant",
    },
    {
        "id": 8,
        "name": "Ajuga salicifolia",
        "nickname": "Willow-leaved Bugle",
        "turkish": "Sogutyaprakli mayasil otu",
        "size": "20-50 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "Blue-violet",
        "leaf_shape": "VERY NARROW long leaves that look like willow tree leaves - unlike any other Ajuga! Edges smooth or faintly toothed.",
        "hairiness": "Lightly hairy",
        "where_it_grows": "Mountain meadows, stream sides, moist rocky slopes. E and NE Turkey, Pontic mountains near the Black Sea. 800-2500 m.",
        "when_it_flowers": "June to August",
        "fun_fact": "Its name literally means willow-leaved and those narrow leaves make it unmistakable. A mountain specialist of eastern Turkey.",
        "how_to_spot_it": "Blue-violet flowers + VERY NARROW willow-like leaves + mountain streams + E Turkey",
    },
    {
        "id": 9,
        "name": "Ajuga bombycina",
        "nickname": "Silky Bugle",
        "turkish": "Ipekli mayasil otu",
        "size": "5-20 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "Pale yellow or white",
        "leaf_shape": "Oval-spoon shaped with smooth edges. Completely covered in LONG SHINY SILVER HAIRS that feel like silk.",
        "hairiness": "Long silky silver hairs - soft and shiny like a silk scarf",
        "where_it_grows": "Limestone rocks and cliffs, rocky slopes in the Taurus Mountains. S Turkey only. 500-2000 m.",
        "when_it_flowers": "April to June",
        "fun_fact": "The silkiest plant in the whole Ajuga genus! Bombycina comes from the Latin word for silkworm. Only grows in Turkey's Taurus Mountains.",
        "how_to_spot_it": "Pale yellow/white flowers + SILKY SILVER SHEEN all over the plant + Taurus Mountains",
    },
    {
        "id": 10,
        "name": "Ajuga postii",
        "nickname": "Post's Bugle",
        "turkish": "Post'un mayasil otu",
        "size": "10-30 cm tall",
        "type": "Annual or biennial (lives 1-2 years)",
        "flower_colour": "Blue or blue-violet",
        "leaf_shape": "Oval to spoon-shaped leaves with rounded teeth along the edges. Moderately hairy.",
        "hairiness": "Moderately hairy",
        "where_it_grows": "Rocky hillsides, scrubby areas, forest margins. S and SE Turkey, Cilicia region (around Adana/Mersin). 200-1500 m.",
        "when_it_flowers": "March to May",
        "fun_fact": "Named after Georg Post, a botanist who studied plants across the Middle East in the 1800s.",
        "how_to_spot_it": "Blue-violet flowers + oval toothed leaves + only in SE Turkey (Cilicia area)",
    },
]

# ============================================================
# IDENTIFICATION KEY
# ============================================================

KEY = [
    # (step_id, question, hint, answer_a_text, answer_b_text, next_if_a, next_if_b)
    # next is either ("step", step_id) or ("species", species_id)
    ("k1",
     "What COLOUR are the flowers?",
     "Look at the petals.",
     "A) Yellow or creamy-white",
     "B) Blue or blue-violet",
     ("step", "k2"), ("step", "k5")),

    ("k2",
     "Are the LEAVES deeply cut into 3 narrow finger-like strips?",
     "Hold a leaf up. Is it cut almost to the stalk into 3 thin strips? Does it smell of pine when crushed?",
     "A) YES - leaves cut into 3 narrow strips, smells of pine",
     "B) NO - leaves are more whole, no pine smell",
     ("step", "k3"), ("step", "k4")),

    ("k3",
     "Are the 3 leaf strips SHORT and STUBBY (not long and thin)?",
     "Are you near the Aegean coast (Izmir, Mugla, Aegean islands)?",
     "A) YES - strips are short and stubby, I am in W/SW Turkey near the coast",
     "B) NO - strips are long and thin, I am inland or anywhere in Turkey",
     ("species", 2), ("species", 1)),

    ("k4",
     "Is the whole plant covered in THICK WHITE WOOLLY hairs, like cotton wool?",
     "Does it look almost white because of very thick fluffy hairs?",
     "A) YES - very thick woolly white hairs, looks almost white",
     "B) NO - hairs are different (silky/silver OR the plant feels slightly sticky)",
     ("species", 7), ("step", "k4b")),

    ("k4b",
     "Do the hairs look SHINY and feel SILKY SMOOTH (like stroking a cat)?",
     "Touch the plant. Do the hairs feel silky and look silver-shiny? Or does it feel slightly sticky?",
     "A) YES - silky and shiny silver hairs, I am in the Taurus Mountains (S Turkey)",
     "B) NO - plant feels slightly sticky/gummy on dry open hillside",
     ("species", 9), ("species", 3)),

    ("k5",
     "Are the LEAVES very NARROW and long, like willow tree leaves?",
     "Is the leaf much longer than it is wide, like a thin strap? Are you near mountain streams in eastern Turkey?",
     "A) YES - very narrow strap-like leaves, E Turkey near streams",
     "B) NO - leaves are broader (oval or oblong)",
     ("species", 8), ("step", "k6")),

    ("k6",
     "Can you see LONG CREEPING STEMS running along the ground?",
     "Are there stems creeping along the soil like strawberry runners? Are you in the Black Sea region?",
     "A) YES - long creeping stems running across the ground, Black Sea region",
     "B) NO - no creeping stems, plant grows as a normal upright clump",
     ("species", 5), ("step", "k7")),

    ("k7",
     "Do the LEAVES look GREY-GREEN (not bright green) because of dense hairs?",
     "Are they dull greyish-green from lots of hairs, or a brighter/shinier green?",
     "A) YES - leaves look grey-green from very dense hairs, no creeping stems",
     "B) NO - leaves are greener or shinier",
     ("species", 6), ("step", "k8")),

    ("k8",
     "Are you in S or SE Turkey (e.g. Adana, Mersin, Hatay area)?",
     "A. orientalis is most common across most of Turkey. A. postii is found mainly in the SE Cilicia region.",
     "A) YES - I am in S or SE Turkey (Cilicia / Adana / Mersin area)",
     "B) NO - I am in N, C, E, or W Turkey (or not sure)",
     ("species", 10), ("species", 4)),
]

KEY_MAP = {step[0]: step for step in KEY}

# ============================================================
# HELPERS
# ============================================================

def divider():
    print("=" * 60)

def short_divider():
    print("-" * 60)

def pause():
    input("\nPress Enter to continue...")

def ask(prompt, valid=None):
    while True:
        answer = input(prompt).strip().upper()
        if valid is None or answer in valid:
            return answer
        print("  Please type one of: " + ", ".join(valid))

def print_species_card(sp):
    divider()
    print("SPECIES %d of 10" % sp["id"])
    print(sp["name"])
    print("Common name : " + sp["nickname"])
    print("Turkish     : " + sp["turkish"])
    short_divider()
    print("Size        : " + sp["size"])
    print("Life span   : " + sp["type"])
    print("Flowers     : " + sp["flower_colour"])
    print("Blooms      : " + sp["when_it_flowers"])
    print("Where found : " + sp["where_it_grows"])
    short_divider()
    print("LEAVES:")
    print("  " + sp["leaf_shape"])
    print("HAIRINESS:")
    print("  " + sp["hairiness"])
    short_divider()
    print("HOW TO SPOT IT:")
    print("  " + sp["how_to_spot_it"])
    short_divider()
    print("FUN FACT:")
    print("  " + sp["fun_fact"])
    print("\nSource: Flora of Turkey, Vol. 7 - P.H. Davis (1982)")
    divider()

# ============================================================
# IDENTIFICATION KEY
# ============================================================

def run_key():
    divider()
    print("IDENTIFY YOUR PLANT")
    print("Answer A or B at each question.")
    print("You will end up with a species name.")
    divider()

    history = []
    current = "k1"

    while True:
        step = KEY_MAP[current]
        step_id, question, hint, ans_a, ans_b, next_a, next_b = step

        print("\nQUESTION:")
        print("  " + question)
        print("  (" + hint + ")")
        print()
        print("  " + ans_a)
        print("  " + ans_b)
        print()
        print("  B = go back one step   R = restart")

        answer = ask("Your answer (A, B, or R): ", ["A", "B", "R"])

        if answer == "R":
            print("\nStarting again...")
            history = []
            current = "k1"
            continue

        if answer == "B" and current == "k1":
            # B answer at k1 means "blue flowers" not "go back"
            # We need to distinguish — check if the input is for the question
            # Actually let's handle go-back with a separate prompt
            pass

        # Go back
        if answer == "B" and len(history) == 0 and current == "k1":
            print("Already at the first question.")
            continue

        # Determine the next step based on A or B answer
        if answer == "A":
            nxt = next_a
        else:
            nxt = next_b

        if isinstance(nxt, tuple) and nxt[0] == "species":
            sp = next(s for s in SPECIES if s["id"] == nxt[1])
            print("\n*** RESULT ***")
            print("Your plant is most likely:")
            print("  " + sp["name"] + " (" + sp["nickname"] + ")")
            print_species_card(sp)
            again = ask("Identify another plant? (Y/N): ", ["Y", "N"])
            if again == "Y":
                history = []
                current = "k1"
            else:
                return
        else:
            history.append(current)
            current = nxt[1]


# ============================================================
# GO BACK AWARE VERSION
# ============================================================

def run_key_v2():
    divider()
    print("IDENTIFY YOUR PLANT")
    print("Answer A or B at each question.")
    print("Type BACK to go back, RESTART to start over.")
    divider()

    history = []
    current = "k1"

    while True:
        step = KEY_MAP[current]
        step_id, question, hint, ans_a, ans_b, next_a, next_b = step

        print()
        short_divider()
        print("QUESTION:")
        print("  " + question)
        print()
        print("  Hint: " + hint)
        print()
        print("  " + ans_a)
        print("  " + ans_b)
        print()

        raw = input("Your answer (A or B): ").strip().upper()

        if raw in ("BACK", "B") and raw == "BACK":
            if history:
                current = history.pop()
                print("Went back one step.")
            else:
                print("Already at the first question.")
            continue

        if raw == "RESTART":
            history = []
            current = "k1"
            print("Starting again.")
            continue

        if raw not in ("A", "B"):
            print("Please type A or B (or BACK or RESTART).")
            continue

        nxt = next_a if raw == "A" else next_b

        if nxt[0] == "species":
            sp = next(s for s in SPECIES if s["id"] == nxt[1])
            print()
            print("*" * 60)
            print("RESULT: Your plant is most likely:")
            print("  " + sp["name"] + " (" + sp["nickname"] + ")")
            print("*" * 60)
            print_species_card(sp)
            again = input("Identify another plant? (y/n): ").strip().lower()
            if again == "y":
                history = []
                current = "k1"
            else:
                return
        else:
            history.append(current)
            current = nxt[1]


# ============================================================
# BROWSE ALL SPECIES
# ============================================================

def browse_all():
    while True:
        divider()
        print("ALL 10 AJUGA SPECIES IN TURKEY")
        short_divider()
        for sp in SPECIES:
            colour = "Yellow" if "Yellow" in sp["flower_colour"] or "yellow" in sp["flower_colour"] else "Blue-violet"
            print("%2d. %-45s [%s]" % (sp["id"], sp["name"], colour))
        print()
        print("Enter a number (1-10) to read about that species.")
        print("Enter 0 to go back to the main menu.")
        print()

        raw = input("Your choice: ").strip()
        if raw == "0":
            return
        try:
            num = int(raw)
            sp = next((s for s in SPECIES if s["id"] == num), None)
            if sp:
                print_species_card(sp)
                pause()
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a number.")


# ============================================================
# SEARCH
# ============================================================

def search():
    divider()
    print("SEARCH FOR A SPECIES")
    print("Type any word to search (colour, place, feature, etc.)")
    print("Examples: yellow, woolly, Black Sea, silky, Taurus, annual")
    short_divider()

    query = input("Search: ").strip().lower()
    if not query:
        return

    results = []
    for sp in SPECIES:
        blob = " ".join([
            sp["name"], sp["nickname"], sp["turkish"],
            sp["flower_colour"], sp["leaf_shape"], sp["hairiness"],
            sp["where_it_grows"], sp["when_it_flowers"],
            sp["fun_fact"], sp["how_to_spot_it"], sp["type"],
        ]).lower()
        if query in blob:
            results.append(sp)

    print()
    if results:
        print("Found %d result(s) for '%s':" % (len(results), query))
        for sp in results:
            colour = "Yellow" if "Yellow" in sp["flower_colour"] or "yellow" in sp["flower_colour"] else "Blue-violet"
            print("  %d. %s (%s) [%s]" % (sp["id"], sp["name"], sp["nickname"], colour))
        print()
        raw = input("Enter a number to view details, or 0 to go back: ").strip()
        if raw != "0":
            try:
                num = int(raw)
                sp = next((s for s in results if s["id"] == num), None)
                if sp:
                    print_species_card(sp)
                    pause()
            except ValueError:
                pass
    else:
        print("Nothing found for '%s'." % query)
        print("Try: yellow, blue, woolly, silky, sticky, runners, Taurus, annual, perennial.")
        pause()


# ============================================================
# QUICK REFERENCE
# ============================================================

def quick_ref():
    divider()
    print("QUICK REFERENCE — ALL 10 SPECIES AT A GLANCE")
    short_divider()
    for sp in SPECIES:
        colour = "YEL" if "Yellow" in sp["flower_colour"] or "yellow" in sp["flower_colour"] else "BLU"
        print("[%s] %2d. %-20s %s" % (colour, sp["id"], sp["name"].split()[-1], sp["how_to_spot_it"]))
    divider()
    pause()


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        divider()
        print("  AJUGA OF TURKEY — IDENTIFICATION GUIDE")
        print("  Based on: Flora of Turkey, Vol. 7 (P.H. Davis, 1982)")
        print("  10 species covered")
        short_divider()
        print("  1. Identify my plant (step-by-step key)")
        print("  2. Browse all 10 species")
        print("  3. Search by keyword")
        print("  4. Quick reference (all species at a glance)")
        print("  5. Quit")
        short_divider()

        choice = ask("Choose an option (1-5): ", ["1", "2", "3", "4", "5"])

        if choice == "1":
            run_key_v2()
        elif choice == "2":
            browse_all()
        elif choice == "3":
            search()
        elif choice == "4":
            quick_ref()
        elif choice == "5":
            print("\nGoodbye! Happy botanising!")
            break


if __name__ == "__main__":
    main()
