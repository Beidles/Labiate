#!/usr/bin/env python3
"""
Lamium (Dead-nettle) Species Key for Turkey
Based on Flora of Turkey, Vol. 7 (P.H. Davis, 1982)

For beginners - just answer Y or N to each question!
Copy and paste the whole file into Python 3 and run it.
No extra libraries needed.
"""

# ── helpers ───────────────────────────────────────────────────

def ask(question, hint=None):
    """Ask a yes/no question. Returns True for yes, False for no."""
    print()
    print("  " + question)
    if hint:
        print("  Hint: " + hint)
    while True:
        ans = input("  --> Y = YES   N = NO   R = restart: ").strip().upper()
        if ans in ("Y", "YES"):
            return True
        if ans in ("N", "NO"):
            return False
        if ans in ("R", "RESTART"):
            raise RestartError()
        print("  Please type Y or N")

class RestartError(Exception):
    pass

def show_result(species, common_name, description, where_found, fun_fact=None):
    """Print the identified species."""
    print()
    print("=" * 58)
    print("  FOUND IT!")
    print("=" * 58)
    print()
    print("  Species:      " + species)
    print("  Common name:  " + common_name)
    print()
    # Word-wrap the long text at ~52 chars
    for label, text in [
        ("Description:  ", description),
        ("Where found:  ", where_found),
    ]:
        words = text.split()
        line = "  " + label
        for word in words:
            if len(line) + len(word) + 1 > 58:
                print(line)
                line = "  " + " " * len(label) + word
            else:
                line += " " + word if line.strip() else word
        print(line)
        print()
    if fun_fact:
        words = fun_fact.split()
        line = "  Fun fact:    "
        for word in words:
            if len(line) + len(word) + 1 > 58:
                print(line)
                line = "  " + " " * 14 + word
            else:
                line += " " + word if line.strip() else word
        print(line)
        print()
    print("=" * 58)
    print()


# ══════════════════════════════════════════════════════════════
#  THE KEY
# ══════════════════════════════════════════════════════════════

def run_key():

    print()
    print("=" * 58)
    print("  LAMIUM (DEAD-NETTLE) KEY  --  TURKEY")
    print("  Flora of Turkey, Vol. 7  (P.H. Davis, 1982)")
    print("=" * 58)
    print()
    print("  Dead-nettles are in the MINT FAMILY (Labiatae).")
    print("  Key features to check before you start:")
    print()
    print("  * SQUARE stem  (roll it between your fingers)")
    print("  * Leaves in OPPOSITE PAIRS")
    print("  * 2-LIPPED flowers (upper lip like a hood,")
    print("    lower lip 3-lobed like a landing platform)")
    print("  * NO STING  (they look like nettles but are safe!)")
    print()
    input("  Press ENTER to begin...")

    # ── Q1: flower colour ─────────────────────────────────────
    if ask(
        "Q1.  Are the flowers YELLOW?",
        "Pure yellow, sometimes with orange or brown streaks."
    ):
        show_result(
            "Lamiastrum galeobdolon (L.) Ehrend. & Polatschek",
            "Yellow Archangel",
            "Strictly this is not a true Lamium - it is placed in "
            "its own genus Lamiastrum. Yellow flowers with orange-"
            "brown markings on the lower lip. Perennial. Leaves "
            "often have silver or pale blotches. Hairy plant.",
            "Shaded woodland edges, scrub, hedgerows. Found in "
            "northern Turkey (Black Sea region).",
            "Botanists argued for years whether to put this in "
            "Lamium or its own genus. Today most use Lamiastrum."
        )
        return

    # ── Q2: white flowers? ────────────────────────────────────
    if ask(
        "Q2.  Are the flowers WHITE (pure white or very pale cream)?",
        "NOT pink, NOT purple. If there are any purple spots on "
        "an otherwise white flower, still answer YES."
    ):
        # White flower branch ──────────────────────────────────

        if ask(
            "Q3.  Does the plant smell strongly of MUSK when you "
            "crush a leaf between your fingers?",
            "Musk is a musky, slightly heavy or cat-like smell. "
            "Crush a leaf and sniff it. If in doubt, answer NO."
        ):
            show_result(
                "Lamium moschatum Mill.",
                "Musk Dead-nettle",
                "Annual (lives one year). White flowers with purple "
                "or brownish spots and streaks on the lower lip. "
                "Triangular to heart-shaped leaves with rounded "
                "teeth. Softly hairy. The musk smell when crushed "
                "is unique among Turkish dead-nettles.",
                "Fields, rocky disturbed ground, olive groves, "
                "roadsides. Found mainly in western and southern "
                "Turkey, often near the coast.",
                "The musky smell probably puts off animals that "
                "might eat it - a clever chemical defence system!"
            )
            return

        if ask(
            "Q4.  Is the plant LARGE AND ROBUST - clearly perennial "
            "(comes back every year from the same root, with a "
            "tough woody base)?",
            "Perennial plants are bigger and tougher. Annual plants "
            "are softer, smaller, and die after one season."
        ):
            show_result(
                "Lamium album L.",
                "White Dead-nettle",
                "Perennial. Large white flowers, up to 2.5 cm long. "
                "Leaves heart-shaped with strongly toothed edges - "
                "they look EXACTLY like stinging nettle leaves but "
                "DO NOT STING. Stems and leaves covered in soft "
                "white hairs. Very common and easy to recognise.",
                "Hedgerows, roadsides, waste ground, stream banks. "
                "Very common across all of Turkey from sea level "
                "up to around 2000 m altitude.",
                "The long flower tube is perfectly sized for "
                "bumblebee tongues. Look inside a flower - you can "
                "see nectar droplets at the base. Flowers are edible "
                "and taste faintly sweet!"
            )
            return

        # Small white-flowered annual
        show_result(
            "Lamium moschatum Mill. (young) or check again",
            "Musk Dead-nettle",
            "A small annual with white flowers. Check the musk "
            "smell again - crush a fresh leaf between your fingers "
            "and sniff carefully. L. moschatum is the only common "
            "small white-flowered annual Lamium in Turkey.",
            "Disturbed ground, fields, roadsides, rocky places.",
            "If you are still unsure, try the iNaturalist app - "
            "take a photo and it can help identify the species!"
        )
        return

    # ── Pink / purple flower branch ───────────────────────────
    print()
    print("  OK - the flowers are pink, purple, or mauve.")
    print("  Look carefully at the plant size and leaves...")

    # ── Q5: annual or perennial? ─────────────────────────────
    if ask(
        "Q5.  Is this a SMALL ANNUAL WEED - soft, low-growing, "
        "with thin soft stems (will die completely after flowering)?",
        "Annual = lives less than a year, grows from seed each "
        "year. Perennial = comes back each year from the same "
        "root, usually bigger and tougher."
    ):
        # Annual pink branch ───────────────────────────────────

        if ask(
            "Q6.  Do the UPPER LEAVES (the ones closest to the "
            "flowers, right near the top of the stem) have NO "
            "stalk at all - do they clasp or wrap around the stem?",
            "Look at the leaves nearest the flowers. "
            "If they sit directly against the stem with no stalk, "
            "like a collar around the stem = YES (sessile/clasping). "
            "If they have even a short stalk = NO."
        ):
            show_result(
                "Lamium amplexicaule L.",
                "Henbit Dead-nettle",
                "Small annual. Pink-purple flowers with a long narrow "
                "tube and a spotted lower lip. The KEY feature is the "
                "upper leaves which have NO stalk and clasp the stem "
                "like a collar. Lower leaves do have stalks. "
                "Leaves round to kidney-shaped with blunt teeth. "
                "Very common weed.",
                "Gardens, fields, roadsides, arable land, disturbed "
                "ground. One of the most common weeds across ALL of "
                "Turkey, from the coast to 2000 m altitude.",
                "Some bees cannot reach the nectar because the "
                "flower tube is too long for them. Watch carefully - "
                "you might see bees biting a hole in the side of the "
                "tube to steal nectar without pollinating the flower!"
            )
            return

        show_result(
            "Lamium purpureum L.",
            "Red Dead-nettle / Purple Dead-nettle",
            "Small annual. Pink-purple flowers. ALL leaves have "
            "stalks (this is different from L. amplexicaule). "
            "Upper leaves often tinged reddish-purple. Leaves "
            "heart-shaped, deeply toothed and crinkled, softly "
            "hairy. Smells slightly unpleasant when crushed.",
            "Gardens, fields, roadsides, waste ground. Extremely "
            "common across all of Turkey. One of the first plants "
            "to flower in late winter and early spring.",
            "Red dead-nettle is one of the most important early "
            "spring plants for bumblebees just out of hibernation "
            "- it flowers when very little else does!"
        )
        return

    # ── Perennial pink branch ─────────────────────────────────
    print()
    print("  OK - it is a perennial pink/purple dead-nettle.")
    print("  Now look at the hairs and leaves carefully...")

    if ask(
        "Q7.  Is the WHOLE PLANT covered in VERY THICK DENSE "
        "WHITE WOOLLY HAIR, making it look grey-white or felted?",
        "This is much more hair than normal. L. tomentosum looks "
        "like it has been dusted with thick white cotton wool or "
        "felt. Normal dead-nettles are hairy but not this extreme."
    ):
        show_result(
            "Lamium tomentosum Mill.",
            "Woolly Dead-nettle",
            "Perennial. Densely covered in thick white woolly "
            "hair all over - this makes it unmistakable. Pink to "
            "purple flowers. Leaves heart-shaped to triangular "
            "with toothed edges, almost hidden under the wool. "
            "The extreme hairiness is the key feature.",
            "Rocky slopes, stony hillsides, dry mountain places. "
            "Central and eastern Turkey, often at higher altitudes "
            "of 1000-2500 m.",
            "The thick woolly coat is an adaptation to survive "
            "on hot dry rocky hillsides - it reflects strong "
            "sunlight and traps moisture around the leaves!"
        )
        return

    if ask(
        "Q8.  Do the leaves have a clearly visible WHITE or PALE "
        "BLOTCH or STRIPE in the middle of the leaf - like a "
        "paint splash or a pale stripe along the centre?",
        "Not always present - some plants have it, some do not. "
        "The blotch is usually whitish, silvery, or just paler "
        "than the rest of the leaf. Look at several leaves."
    ):
        show_result(
            "Lamium maculatum (L.) L.",
            "Spotted Dead-nettle",
            "Perennial. Pink to purple flowers with a spotted or "
            "streaked lower lip. Leaves heart-shaped with toothed "
            "edges, OFTEN with a white or silvery blotch or stripe "
            "in the middle (maculatum means spotted). Stems hairy. "
            "Not all plants have the white blotch though!",
            "Shaded places, woodland edges, hedgerows, stream "
            "banks, damp roadsides. Found across Turkey, especially "
            "in shadier and damper habitats than other species.",
            "This is one of the most popular garden ground-cover "
            "plants in the world - nurseries sell many varieties "
            "with extra-large white blotches on the leaves!"
        )
        return

    if ask(
        "Q9.  Are the flowers LARGE - as long as your thumbnail "
        "(over 2 cm), with a long tube - and is the plant "
        "quite tall and robust?",
        "Compare the flower size to your thumbnail. "
        "L. garganicum has noticeably bigger flowers than most "
        "other dead-nettles. The tube is long and the whole "
        "flower looks bigger overall."
    ):
        show_result(
            "Lamium garganicum L.",
            "Large-flowered Dead-nettle",
            "Perennial with large pink to deep magenta flowers, "
            "usually over 2 cm long - noticeably bigger than other "
            "species. Robust plant. Leaves heart-shaped to "
            "triangular with toothed edges. Several quite different-"
            "looking subspecies occur in Turkey - some very hairy, "
            "some less so, some with pale flowers, some dark.",
            "Rocky places, scrub, forest edges, mountain slopes, "
            "old walls. Very widespread across Turkey from sea level "
            "to over 2500 m. One of the most common Turkish Lamium.",
            "Turkey has more subspecies of L. garganicum than "
            "almost any other country in the world - botanists are "
            "still arguing about exactly how many there are!"
        )
        return

    if ask(
        "Q10. Does the plant have UNDERGROUND TUBERS - small "
        "potato-shaped swellings attached to the roots "
        "(you would need to carefully dig it up to check)?",
        "Tubers look like tiny potatoes or beads on the roots. "
        "You need to dig up the plant carefully to see them. "
        "If you cannot check the roots, answer NO."
    ):
        show_result(
            "Lamium tuberosum Hoffmanns. & Link",
            "Tuberous Dead-nettle",
            "Perennial. Has small underground tubers (swellings "
            "like tiny potatoes) on the roots - the key feature. "
            "Pink-purple flowers of medium size. Leaves heart-"
            "shaped with toothed edges.",
            "Fields, disturbed ground, scrub, olive groves. "
            "Found in parts of Turkey, mainly in the west and "
            "south-west.",
            "The underground tubers act as a food store - the "
            "plant uses the energy stored in them to regrow "
            "quickly in spring, even if the top is damaged!"
        )
        return

    if ask(
        "Q11. Are the leaves NARROW AND ELONGATED - clearly longer "
        "than they are wide, more like an oval than a heart?",
        "Most dead-nettles have broad heart-shaped leaves "
        "(wider than long). If the leaves are noticeably "
        "narrow and more oval or lance-shaped = YES."
    ):
        show_result(
            "Lamium orientale Bieberst.",
            "Oriental Dead-nettle",
            "Perennial with pink-purple flowers. The leaves are "
            "more elongated and narrower than in most dead-nettles "
            "- more oval than heart-shaped. Calyx teeth (the "
            "pointed tips of the green cup below the flower) are "
            "relatively long, about as long as the tube.",
            "Rocky slopes, scrub, disturbed ground. Found mainly "
            "in eastern Turkey and extending into the Caucasus "
            "region.",
            "The name orientale means eastern in Latin - "
            "reflecting that this is one of the dead-nettles "
            "found towards the eastern part of Turkey."
        )
        return

    if ask(
        "Q12. Are you in EASTERN TURKEY (provinces like Erzurum, "
        "Van, Kars, Agri, or nearby areas)?",
        "L. armenum is found mainly in eastern Anatolia and "
        "the Caucasus region."
    ):
        show_result(
            "Lamium armenum Boiss.",
            "Armenian Dead-nettle",
            "Perennial with pink-purple flowers. Similar to "
            "L. garganicum but with smaller flowers. Found mainly "
            "in eastern Turkey. Leaves heart-shaped with toothed "
            "edges. Hairy plant.",
            "Mountain slopes, rocky places, scrub. Mainly eastern "
            "Turkey, into the Caucasus region (Armenia, Georgia).",
            "The name armenum means Armenian - named after "
            "Armenia, the region where it was first discovered "
            "by botanists."
        )
        return

    # ── Default / catch-all ───────────────────────────────────
    show_result(
        "Lamium longiflorum Ten. or another Turkish species",
        "Long-flowered Dead-nettle or similar",
        "A pink-purple perennial dead-nettle that did not quite "
        "fit the other options. Could be L. longiflorum (found "
        "in western Turkey, similar to L. garganicum), or "
        "possibly a local variety. Turkey has over 15 Lamium "
        "species and some are very similar to each other!",
        "Rocky places, scrub, fields. Various habitats "
        "depending on the exact species.",
        "Even expert botanists sometimes need a microscope "
        "and the full Flora of Turkey book to identify some "
        "Lamium species. Try taking a photo and using the "
        "free iNaturalist app for help!"
    )


# ── main ──────────────────────────────────────────────────────

def main():
    while True:
        try:
            run_key()
        except RestartError:
            print()
            print("  Starting again from the beginning...")
            continue

        print()
        again = input("  Identify another plant? (Y/N): ").strip().upper()
        if again not in ("Y", "YES"):
            print()
            print("  Happy botanising in Turkey!")
            print()
            break

if __name__ == "__main__":
    main()
