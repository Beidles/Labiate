#!/usr/bin/env python3
"""
Dicotyledon Plant Family Key for Turkey
Based on Flora of Turkey, Vol. 1 (P.H. Davis, 1965)

Simplified for beginners - no botanical degree needed!
Works on Replit - just press Run!
"""

import os

# --- Colours for the terminal (works on Replit) ---
G  = '\033[92m'   # green
B  = '\033[94m'   # blue
Y  = '\033[93m'   # yellow
R  = '\033[91m'   # red
C  = '\033[96m'   # cyan
M  = '\033[95m'   # magenta
BO = '\033[1m'    # bold
X  = '\033[0m'    # reset

# --------------------------------------------------
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(G + BO + """
╔══════════════════════════════════════════════════════════════╗
║    DICOTYLEDON PLANT KEY  -  Turkey (Flora of Turkey Vol.1) ║
║    Answer YES or NO to find your plant family!              ║
╚══════════════════════════════════════════════════════════════╝
""" + X)

def tip(text):
    """Print a helpful tip box."""
    print(Y + "  TIP: " + text + X)

def ask(number, question, hint=None):
    """
    Ask a yes/no question.
    Returns True for yes, False for no.
    'b' lets the user go back (raises BackSignal).
    """
    print(B + BO + f"\n  Q{number}. {question}" + X)
    if hint:
        tip(hint)
    while True:
        ans = input(C + "       y = YES   |   n = NO   |   r = restart: " + X).strip().lower()
        if ans in ('y', 'yes'):
            return True
        elif ans in ('n', 'no'):
            return False
        elif ans in ('r', 'restart'):
            raise RestartSignal()
        else:
            print(R + "       Please type  y  or  n  (or r to restart)" + X)

def show_result(latin, common, what_it_is, examples, warning=None):
    """Display the identified family."""
    print(G + BO + """
  ┌─────────────────────────────────────────────────────┐
  │                    FOUND IT!                        │
  └─────────────────────────────────────────────────────┘""" + X)
    print(BO + f"\n  Family:       {latin}" + X)
    print(    f"  Common name:  {common}")
    print(    f"\n  About it:     {what_it_is}")
    print(Y + f"\n  Examples:     {examples}" + X)
    if warning:
        print(R + BO + f"\n  WARNING:      {warning}" + X)
    print()

class RestartSignal(Exception):
    pass

# ==============================================================
#  THE KEY
#  Based on the main family key in Flora of Turkey, Vol. 1
#  Questions use plain everyday language where possible.
# ==============================================================

def run_key():
    q = 0   # question counter (so numbering is always sequential)

    def nq():
        nonlocal q
        q += 1
        return q

    # ── Q1 ────────────────────────────────────────────────────
    if ask(nq(),
           "Does the plant ooze MILKY or strangely coloured sap when you "
           "snap a stem or scratch a leaf?",
           "Milky sap = white liquid like watered-down milk. "
           "Normal sap is clear or just slightly wet."):

        # ── Q2 (milky sap branch) ─────────────────────────────
        if ask(nq(),
               "Are the flowers LARGE and showy, with petals that fall off "
               "very easily (even a light touch knocks them off)?",
               "Think of a poppy flower - big, bright, papery petals."):
            show_result(
                "Papaveraceae",
                "Poppy Family",
                "Milky or coloured sap + large showy flowers whose petals drop quickly. "
                "Seed pods are often rounded capsules with tiny holes at the top.",
                "Poppy (Papaver), Greater celandine (Chelidonium), Horned poppy (Glaucium)",
                warning=None
            )
        else:
            show_result(
                "Euphorbiaceae",
                "Spurge Family",
                "Milky WHITE sap (very distinctive). The 'flowers' are tiny and surrounded "
                "by leaf-like green or yellow bracts that look like petals. Very common in Turkey.",
                "Spurges (Euphorbia) - huge genus with 100+ Turkish species, Sun spurge, Cypress spurge",
                warning="The milky sap of most spurges can irritate skin and eyes. Wash hands after touching."
            )
        return

    # ── Q2 ────────────────────────────────────────────────────
    if not ask(nq(),
               "Can you see PROPER PETALS on the flowers? "
               "(Even tiny, greenish, or petal-like ones count.)",
               "Some plants have only tiny green or brown flowers with no real petals at all."):

        # No petals sub-key ────────────────────────────────────
        if ask(nq(),
               "Do the tiny flowers hang in long, dangly, caterpillar-like clusters "
               "called CATKINS (common on trees and shrubs)?",
               "Catkins look like a woolly worm hanging from a twig - "
               "common on birch, alder, willow."):
            show_result(
                "Betulaceae / Fagaceae / Salicaceae",
                "Birch / Oak / Willow Family",
                "Trees or shrubs with tiny petalless flowers in hanging catkins or "
                "short clusters. Wind-pollinated. Often produce nuts, acorns, or fluffy seeds.",
                "Birch (Betula), Alder (Alnus), Hazel (Corylus), Oak (Quercus), "
                "Willow (Salix), Poplar (Populus)"
            )
            return

        if ask(nq(),
               "Does the stem have a papery or membranous SHEATH (like a little skirt "
               "or sleeve) wrapped around it at each point where a leaf joins?",
               "Polygonaceae are famous for this papery sheath (called an ochrea). "
               "Look where leaf meets stem."):
            show_result(
                "Polygonaceae",
                "Dock / Knotweed Family",
                "Papery sheath around stem at each leaf-joint is the key feature. "
                "Small petalless flowers. Often in damp or disturbed places.",
                "Dock (Rumex), Knotweed (Polygonum), Bistort (Bistorta), "
                "Buckwheat (Fagopyrum), Russian vine (Fallopia)"
            )
            return

        if ask(nq(),
               "Are the leaves or stem covered with a white MEALY or powdery coating "
               "(like flour dusted on them)?",
               "Rub the leaf gently - the white powder comes off on your finger. "
               "Very common on fat hen and orache."):
            show_result(
                "Chenopodiaceae",
                "Goosefoot / Saltbush Family",
                "Small greenish petalless flowers. Leaves often with mealy white coating. "
                "Very common in salty ground, roadsides, and waste places.",
                "Fat hen (Chenopodium), Orache (Atriplex), "
                "Sea beet (Beta vulgaris), Glasswort (Salicornia)"
            )
            return

        show_result(
            "Urticaceae / Amaranthaceae",
            "Nettle / Amaranth Family",
            "Tiny petalless flowers in clusters or spikes. Leaves opposite, often with "
            "stinging hairs (nettle) or in an amaranth spike.",
            "Stinging nettle (Urtica), Pellitory-of-the-wall (Parietaria), "
            "Amaranth (Amaranthus)"
        )
        return

    # ── Has petals ─────────────────────────────────────────────
    # Q5: fused vs free
    if ask(nq(),
           "Are the petals JOINED together - forming a tube, bell, funnel, "
           "or cup shape - rather than being completely separate?",
           "Test: try to pull off just ONE petal gently. "
           "If ALL petals come away as one piece they are joined (fused). "
           "If a single petal comes away by itself they are free."):

        # ══════════════════════════════════════════════════════
        #  FUSED-PETAL FAMILIES
        # ══════════════════════════════════════════════════════

        # Q6: composite / daisy head
        if ask(nq(),
               "Is what looks like a single flower actually a TIGHT CLUSTER of "
               "many tiny flowers packed together, like a daisy or dandelion?",
               "Look very closely at the centre of the flower. "
               "A daisy 'flower' is actually hundreds of minute flowers. "
               "Each yellow 'eye' disc is dozens of tiny tubular flowers; "
               "each white 'petal' is actually one tiny ray-flower."):
            show_result(
                "Compositae (Asteraceae)",
                "Daisy / Sunflower Family",
                "The BIGGEST flowering-plant family! What looks like one flower is a "
                "'head' of tens to hundreds of tiny flowers. Outer ray-flowers look like petals; "
                "inner disc-flowers are tiny tubes. Seed usually has a feathery parachute.",
                "Daisy (Bellis), Dandelion (Taraxacum), Chamomile (Anthemis), "
                "Thistle (Cirsium), Knapweed (Centaurea), "
                "Ox-eye daisy (Leucanthemum), Groundsel (Senecio)"
            )
            return

        # Q7: square stem = mint family
        if ask(nq(),
               "Is the stem clearly SQUARE (4 flat sides) when you look down at it "
               "from above, or roll it between your fingers?",
               "Most stems are round. A square stem feels like a 4-sided pencil. "
               "This is one of the best clues in the plant world!"):
            show_result(
                "Labiatae (Lamiaceae)",
                "Mint / Dead-nettle Family",
                "Square stems + leaves in opposite pairs = almost certain Labiatae. "
                "Flowers have two 'lips' (upper and lower), like a tiny mouth. "
                "Many species are strongly aromatic (minty, herby, or sage-like).",
                "Mint (Mentha), Thyme (Thymus), Sage (Salvia), Lavender (Lavandula), "
                "Rosemary (Rosmarinus), Dead-nettle (Lamium), Self-heal (Prunella), "
                "Woundwort (Stachys), Marjoram (Origanum)"
            )
            return

        # Q8: scorpioid cyme = borage family
        if ask(nq(),
               "Do the flowers grow on a stem that CURLS over like a scorpion's tail "
               "or a watch spring, slowly uncurling as more flowers open?",
               "This coiled cluster is called a 'scorpioid cyme'. "
               "Forget-me-nots are the classic example. "
               "The stem starts curled and straightens out from the tip."):
            show_result(
                "Boraginaceae",
                "Borage / Forget-me-not Family",
                "Flowers in a coiled cluster that uncurls as it blooms (scorpioid cyme). "
                "Usually 5 petals fused into a short tube, often blue, pink, or white. "
                "Plant often covered in rough, bristly hairs. Leaves alternate.",
                "Forget-me-not (Myosotis), Borage (Borago), Bugloss (Anchusa), "
                "Viper's bugloss (Echium), Hound's-tongue (Cynoglossum), "
                "Lungwort (Pulmonaria)"
            )
            return

        # Q9: irregular fused = scrophulariaceae / convolvulaceae
        if ask(nq(),
               "Is the flower IRREGULAR - meaning if you hold it facing you, "
               "the LEFT half looks different from the RIGHT half?",
               "Regular flowers look the same from any direction (like a star). "
               "Irregular flowers have a 'top' and 'bottom' - like a snapdragon "
               "or foxglove which has an obvious upper and lower lip."):

            if ask(nq(),
                   "Does the flower look like a FOXGLOVE or SNAPDRAGON - tubular "
                   "with an upper lip and a lower lip (2-lipped)?",
                   "Scrophulariaceae flowers often look like a small mouth or tunnel "
                   "with two lips. Hold one up and look straight into it."):
                show_result(
                    "Scrophulariaceae",
                    "Figwort / Foxglove Family",
                    "Irregular 2-lipped tubular flowers. Usually 4 stamens inside "
                    "(sometimes 2 or 5). Many species are semi-parasitic on grass roots. "
                    "Very diverse family in Turkey.",
                    "Foxglove (Digitalis), Mullein (Verbascum), Snapdragon (Antirrhinum), "
                    "Eyebright (Euphrasia), Speedwell (Veronica), "
                    "Lousewort (Pedicularis), Cow-wheat (Melampyrum)",
                    warning=None
                )
            else:
                show_result(
                    "Convolvulaceae",
                    "Bindweed / Morning-glory Family",
                    "Usually climbing or twining plants. Flowers are a wide funnel or "
                    "trumpet shape, often with 5 faint stripes. Open in morning, close by afternoon.",
                    "Bindweed (Convolvulus) - the common garden pest, "
                    "Field bindweed (C. arvensis), Morning-glory (Ipomoea)"
                )
            return

        # Q10: nightshade
        if ask(nq(),
               "Are the petals folded BACK like a star (reflexed), with a "
               "noticeable yellow or orange CONE of stamens sticking forward "
               "from the centre of the flower?",
               "Tomato and potato flowers look like this - a star of petals "
               "swept backwards, with a pointy yellow column in the middle."):
            show_result(
                "Solanaceae",
                "Nightshade / Potato Family",
                "5 petals fused at base, usually reflexed to form a star. "
                "Stamens fused into a yellow cone. Often produces berries. "
                "Leaves can smell unpleasant when crushed.",
                "Tomato (Lycopersicon), Potato (Solanum tuberosum), "
                "Deadly nightshade (Atropa belladonna), "
                "Henbane (Hyoscyamus niger), Tobacco (Nicotiana)",
                warning="Many members are HIGHLY POISONOUS. Never eat berries you cannot identify!"
            )
            return

        # Q11: plantain / bellflower
        if ask(nq(),
               "Does the plant grow as a ROSETTE of leaves flat on the ground, "
               "with a leafless flowering spike growing up from the centre?",
               "A rosette looks like a flat circle of leaves spreading out "
               "from one central point, like a star on the ground. "
               "Plantains are the classic lawn weed with this shape."):
            show_result(
                "Plantaginaceae",
                "Plantain Family",
                "Basal rosette of leaves with strong parallel veins. "
                "Tiny 4-petalled flowers in a spike or oval head. "
                "Very common in lawns, paths, and trampled ground.",
                "Ribwort plantain (Plantago lanceolata), "
                "Greater plantain (P. major - the broad flat lawn weed), "
                "Hoary plantain (P. media)"
            )
        else:
            show_result(
                "Campanulaceae",
                "Bellflower Family",
                "Usually clear blue or violet bell-shaped or star-shaped flowers "
                "with 5 joined petals. Milky sap sometimes present. "
                "Leaves alternate. Very well-represented in Turkey.",
                "Bellflower (Campanula) - dozens of Turkish species, "
                "Sheep's bit (Jasione), Rampion (Phyteuma)"
            )
        return

    # ══════════════════════════════════════════════════════════
    #  FREE-PETAL FAMILIES
    # ══════════════════════════════════════════════════════════

    # Q12: 4 petals in a cross
    if ask(nq(),
           "Are there EXACTLY 4 petals arranged in a cross shape (like a + or x)?",
           "Count the petals carefully! Cabbage family always has exactly 4. "
           "They are often arranged in a neat cross. "
           "Also look for the long thin seed pods (siliques)."):
        show_result(
            "Cruciferae (Brassicaceae)",
            "Cabbage / Mustard Family",
            "Always exactly 4 petals in a cross shape. Usually 6 stamens "
            "(4 tall + 2 short). Seeds in a long thin pod (silique) or short round pod. "
            "Often smells of cabbage or mustard when crushed.",
            "Cabbage, Mustard (Sinapis), Wallflower (Erysimum), "
            "Shepherd's purse (Capsella bursa-pastoris - tiny heart-shaped pods), "
            "Sweet alyssum (Lobularia), Honesty (Lunaria), Watercress (Nasturtium)"
        )
        return

    # Q13: pea-shaped flower
    if ask(nq(),
           "Does the flower look like a BUTTERFLY or a little boat - with one large "
           "upper petal, two side petals, and two bottom petals forming a 'keel'?",
           "Pea flowers are very distinctive. The big upper petal is the 'standard' "
           "(like a flag), the two side petals are 'wings', and the bottom two form "
           "a 'keel' (the boat hull). Clover and bean flowers look like this."):
        show_result(
            "Leguminosae (Fabaceae)",
            "Pea / Bean Family",
            "Butterfly-shaped flowers (standard, wings, keel). Seeds grow in PODS. "
            "Root nodules fix nitrogen from the air, making soil more fertile. "
            "Leaves often compound (made of many small leaflets).",
            "Peas and beans (Pisum, Vicia, Phaseolus), Clover (Trifolium), "
            "Vetch (Vicia), Broom (Genista), Gorse (Ulex), "
            "Locust tree (Robinia), Liquorice (Glycyrrhiza)"
        )
        return

    # Q14: umbel (flat-topped cluster)
    if ask(nq(),
           "Do MANY tiny flowers grow on stalks that all radiate from the SAME "
           "point, forming a flat-topped or domed UMBRELLA shape?",
           "The stalks spread out like umbrella spines from one point, "
           "and each stalk may then branch again the same way (a compound umbel). "
           "Think of fennel, cow parsley, or carrot flowers."):
        show_result(
            "Umbelliferae (Apiaceae)",
            "Carrot / Parsley Family",
            "Flowers in flat umbrella-like clusters (umbels). Stems often hollow. "
            "Leaves usually feathery and divided. Aromatic when crushed. "
            "Very important in Turkey's flora with 400+ species.",
            "Carrot (Daucus carota), Fennel (Foeniculum), Cow parsley (Anthriscus), "
            "Angelica, Hogweed (Heracleum), Cumin (Cuminum), "
            "Coriander (Coriandrum), Anise (Pimpinella)",
            warning="This family contains some of the DEADLIEST plants known "
                    "(Hemlock - Conium maculatum, Hemlock water-dropwort - Oenanthe). "
                    "Never eat anything from this family unless you are 100% certain of the ID."
        )
        return

    # Q15: rose family
    if ask(nq(),
           "Does the flower have EXACTLY 5 petals (often round and spreading), "
           "with MANY stamens in a ring around the centre?",
           "Rose family flowers look like a classic 5-petalled flower. "
           "Count the stamens - if there are more than 10, that is a strong clue. "
           "The petals are usually not notched or fringed."):
        show_result(
            "Rosaceae",
            "Rose Family",
            "5 petals (sometimes 4), usually MANY stamens. One of the most important "
            "plant families for food! Leaves usually have toothed or serrated edges. "
            "May have thorns or prickles.",
            "Rose (Rosa), Bramble / Blackberry (Rubus), Hawthorn (Crataegus), "
            "Strawberry (Fragaria), Apple / Pear / Cherry / Plum (Malus, Pyrus, "
            "Prunus), Cinquefoil (Potentilla), Lady's mantle (Alchemilla)"
        )
        return

    # Q16: pink family (notched petals / swollen calyx)
    if ask(nq(),
           "Are the petals NOTCHED or forked at the tip (as if someone cut a "
           "V-shape into each petal), OR does the base of the flower have "
           "a striped or inflated tube (calyx tube)?",
           "Carnation and campion flowers have this look. "
           "Hold a flower up and look at each petal tip - is it split into two points? "
           "Also look for the swollen striped calyx (the green tube below the petals)."):
        show_result(
            "Caryophyllaceae",
            "Pink / Campion / Carnation Family",
            "Petals often notched or fringed at the tip. Leaves in OPPOSITE PAIRS, "
            "often narrow. Stem joints (nodes) often swollen. "
            "Calyx (sepal tube) often striped or inflated.",
            "Carnation / Pink (Dianthus) - many Turkish species, "
            "Campion (Silene) - the largest genus in Turkey with 100+ species, "
            "Chickweed (Stellaria), Stitchwort (Cerastium), Soapwort (Saponaria)"
        )
        return

    # Q17: buttercup family
    if ask(nq(),
           "Are the petals SHINY (especially if yellow), and does the plant "
           "have MANY separate stamens and pistils crowded in the centre?",
           "Buttercup petals have a lacquered, waxy shine in sunlight. "
           "In the centre there are usually lots of small separate parts "
           "(many stamens AND many pistils all separate from each other)."):
        show_result(
            "Ranunculaceae",
            "Buttercup / Crowfoot Family",
            "Often many free petals AND many free stamens and pistils in the centre. "
            "Great variety of flower shapes in this family (from buttercups to delphiniums). "
            "Sepals sometimes coloured and petal-like.",
            "Buttercup (Ranunculus), Anemone, Clematis (climber), "
            "Delphinium / Larkspur, Columbine (Aquilegia), "
            "Hellebore (Helleborus), Pheasant's-eye (Adonis)",
            warning="Most members are poisonous if eaten."
        )
        return

    # Q18: mallow family
    if ask(nq(),
           "Are the stamens (the pollen-making parts in the flower centre) "
           "all FUSED TOGETHER into a central column or tube?",
           "In the mallow family, all the stamens are joined together into "
           "one structure that looks like a column sticking up from the flower centre. "
           "The petals are free but the stamens are joined."):
        show_result(
            "Malvaceae",
            "Mallow Family",
            "5 free petals, but all stamens fused into a central column (very distinctive). "
            "Leaves often large, lobed or rounded with palmate veins. "
            "Flowers often large and showy.",
            "Mallow (Malva), Hollyhock (Alcea rosea), Tree mallow (Lavatera), "
            "Hibiscus, Cotton (Gossypium)"
        )
        return

    # Q19: stonecrop / saxifrage
    if ask(nq(),
           "Are the leaves very THICK and FLESHY (plump, almost rubbery, "
           "full of water) - like a succulent houseplant?",
           "Succulent leaves feel like they are full of gel or water. "
           "They are much thicker and firmer than a normal leaf. "
           "Common on rocks, walls, and dry stony places."):
        show_result(
            "Crassulaceae",
            "Stonecrop / Houseleek Family",
            "Fleshy, succulent leaves full of water (an adaptation to dry rocky habitats). "
            "Flowers star-shaped, usually 5 petals. Often grow in tight rosettes. "
            "Very common on rock ledges and old walls in Turkey.",
            "Stonecrop (Sedum) - dozens of Turkish species, "
            "Houseleek (Sempervivum), Rosularia"
        )
        return

    # Catch-all
    print(M + BO + """
  ┌─────────────────────────────────────────────────────┐
  │          Hmm, needs a closer look...                │
  └─────────────────────────────────────────────────────┘""" + X)
    print("""
  Your plant did not fit neatly into the families covered here.
  Turkey has over 3,000 dicotyledon species across 100+ families,
  so this beginner key only covers the most common ones.

  Suggestions:
    1. Try again - sometimes a closer look at the flower changes the answer.
    2. Take a clear photo of the flower, leaf, and stem, then use
       the free iNaturalist app or website - it identifies plants from photos.
    3. Other common Turkish families not in this key include:
         Geraniaceae (crane's-bills), Hypericaceae (St John's-wort),
         Cistaceae (rock-roses), Violaceae (violets),
         Primulaceae (primroses), Linaceae (flaxes).
""")


# ──────────────────────────────────────────────────────────────
def main():
    while True:
        clear()
        banner()
        print("  Look carefully at your plant, then answer each question.")
        print("  Type  y  for YES  or  n  for NO  after each question.")
        print("  Type  r  at any point to restart from the beginning.\n")
        input(C + "  Press ENTER to start..." + X)

        try:
            run_key()
        except RestartSignal:
            continue

        print(C + "  " + "─" * 55 + X)
        again = input(Y + "  Identify another plant? (y / n): " + X).strip().lower()
        if again not in ('y', 'yes'):
            print(G + BO + "\n  Good luck with your plant hunting!\n" + X)
            break


if __name__ == "__main__":
    main()
