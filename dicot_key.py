#!/usr/bin/env python3
"""
Complete Dicotyledon Plant Family Key - Turkey
Based on Flora of Turkey, Vol. 1 (P.H. Davis, 1965)

Covers ~45 families.  Designed for beginners on Replit.
Just press Run and answer y / n to each question.
"""

import os

# ── terminal colours ──────────────────────────────────────────
G  = '\033[92m'; B  = '\033[94m'; Y  = '\033[93m'
R  = '\033[91m'; C  = '\033[96m'; M  = '\033[95m'
BO = '\033[1m';  X  = '\033[0m'

class RestartSignal(Exception):
    pass

_q = [0]   # question counter shared across calls

# ── helpers ───────────────────────────────────────────────────

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(G + BO + """
╔══════════════════════════════════════════════════════════════════╗
║  COMPLETE DICOTYLEDON KEY  -  Turkey (Flora of Turkey Vol. 1)   ║
║  P.H. Davis  |  Answer y/n to identify your plant family        ║
╚══════════════════════════════════════════════════════════════════╝
""" + X)

def ask(question, hint=None):
    _q[0] += 1
    print(B + BO + f"\n  Q{_q[0]}. {question}" + X)
    if hint:
        print(Y + "      TIP: " + hint + X)
    while True:
        a = input(C + "      y=YES  n=NO  r=restart: " + X).strip().lower()
        if a in ('y', 'yes'):   return True
        if a in ('n', 'no'):    return False
        if a in ('r', 'restart'): raise RestartSignal()
        print(R + "      Please type  y  or  n  (or r to restart)" + X)

def result(latin, common, about, examples, warning=None):
    print(G + BO + """
  ╔════════════════════════════════════════════════╗
  ║                   FOUND IT!                   ║
  ╚════════════════════════════════════════════════╝""" + X)
    print(BO + f"\n  Family:      {latin}" + X)
    print(     f"  Common name: {common}")
    print(     f"\n  About:       {about}")
    print(Y +  f"\n  Examples:    {examples}" + X)
    if warning:
        print(R + BO + f"\n  WARNING:     {warning}" + X)
    print()

# ══════════════════════════════════════════════════════════════
#  THE KEY
# ══════════════════════════════════════════════════════════════

def run_key():
    _q[0] = 0   # reset counter for each run

    # ── GROUP 0: special / parasitic ─────────────────────────
    if ask(
        "Is the plant COMPLETELY lacking green colour "
        "(entirely yellow, brown, red, or purple — not a flower, the whole plant)?",
        "True root-parasites have no green at all — they cannot photosynthesise. "
        "They grow attached to other plant roots and often look like a thick spike or club."
    ):
        result(
            "Orobanchaceae",
            "Broomrape Family",
            "Entirely parasitic on the roots of other plants. No chlorophyll (no green). "
            "Usually a fleshy spike or club of tubular 2-lipped flowers. "
            "Leaves reduced to brown scales.",
            "Broomrape (Orobanche) — over 40 Turkish species, "
            "Toothwort (Lathraea), Cistanche"
        )
        return

    # ── GROUP 1: milky / coloured sap ────────────────────────
    if ask(
        "Does the plant ooze MILKY or strangely coloured sap "
        "when you snap a stem or scratch a leaf?",
        "Milky sap = white liquid like diluted milk. "
        "Orange or yellow sap = also yes here. "
        "Normal clear or slightly green watery juice = NO."
    ):
        if ask(
            "Is the sap YELLOW or ORANGE (not white)?",
            "Greater celandine has vivid orange-yellow sap — very distinctive."
        ):
            result(
                "Papaveraceae (Chelidonium / Glaucium)",
                "Poppy Family — Celandine group",
                "Bright orange or yellow sap. Flowers 4-petalled. "
                "Celandine has small yellow flowers; sea/horned poppy has large orange ones.",
                "Greater celandine (Chelidonium majus), "
                "Horned poppy (Glaucium flavum), Hypecoum"
            )
            return

        if ask(
            "Are the flowers LARGE and showy, with papery petals "
            "that fall off very easily?",
            "A gentle touch or breeze knocks poppy petals off. "
            "They are large, bright, and papery."
        ):
            result(
                "Papaveraceae",
                "Poppy Family",
                "White milky sap + large showy papery petals that drop quickly. "
                "4 petals (sometimes more). Seed capsule with small holes at top.",
                "Poppy (Papaver) — many Turkish species, "
                "Fumewort (Corydalis) — but see Fumariaceae below",
                warning="Opium poppy sap is a controlled substance."
            )
        else:
            result(
                "Euphorbiaceae",
                "Spurge Family",
                "White milky sap. Flowers are tiny, often surrounded by cup-shaped "
                "green or yellow bracts that look like petals (cyathium). "
                "Enormous genus Euphorbia has 100+ Turkish species.",
                "Spurge (Euphorbia): sun spurge, cypress spurge, caper spurge, "
                "Albanian spurge. Also Dog's mercury (Mercurialis).",
                warning="Milky sap irritates skin and eyes — wash hands after handling."
            )
        return

    # ── GROUP 2: aquatic / floating ──────────────────────────
    if ask(
        "Does the plant grow IN water or float ON the surface?",
        "Not just in wet mud — actually in or on the water."
    ):
        if ask(
            "Does it have large ROUND FLOATING LEAVES "
            "and big showy flowers (white or yellow)?",
            "Water-lily leaves are large, round, floating pads. "
            "Flowers sit on or just above the water."
        ):
            result(
                "Nymphaeaceae",
                "Water-lily Family",
                "Large round floating leaves (pads). Showy flowers with many petals "
                "and many stamens. Roots anchored in mud.",
                "White water-lily (Nymphaea alba), "
                "Yellow water-lily (Nuphar lutea)"
            )
        else:
            result(
                "Ranunculaceae (aquatic)",
                "Water Crowfoot — Buttercup Family",
                "Aquatic buttercups with white flowers and feathery underwater leaves. "
                "Often found in streams and ponds.",
                "Water crowfoot (Ranunculus aquatilis and relatives)"
            )
        return

    # ── GROUP 3: climbing vines ───────────────────────────────
    if ask(
        "Is the plant a CLIMBING VINE that grips with TENDRILS "
        "(small curly threads that coil around supports)?",
        "Tendrils are thin, coiling threads the plant uses to climb. "
        "Not the same as twining stems (bindweed) or scrambling thorns (bramble)."
    ):
        if ask(
            "Are the leaves PALMATELY LOBED "
            "(spreading from a central point like fingers on a hand)?",
            "Grape leaves look like a hand with 5 finger-shaped lobes."
        ):
            result(
                "Vitaceae",
                "Grape / Vine Family",
                "Climbing by tendrils opposite the leaves. Palmately-lobed leaves. "
                "Small flowers. Fruit a berry (grape). Tendrils are modified stems.",
                "Grape vine (Vitis vinifera), Virginia creeper (Parthenocissus)"
            )
        else:
            result(
                "Cucurbitaceae",
                "Cucumber / Gourd Family",
                "Climbing by tendrils. Leaves usually lobed. "
                "Flowers yellow, often large. Fruit can be very large (gourd, cucumber).",
                "Cucumber, Courgette, Pumpkin (Cucurbita), "
                "White bryony (Bryonia dioica) — wild species in Turkey",
                warning="White bryony berries are poisonous."
            )
        return

    # ── GROUP 4: no visible petals ───────────────────────────
    if not ask(
        "Can you see CLEAR PETALS on the flowers?",
        "Even tiny, greenish, or scale-like petals count as YES. "
        "If the flower is just a cluster of stamens/pistils with green or brown parts only = NO."
    ):

        if ask(
            "Does the stem have a PAPERY SLEEVE or SHEATH "
            "wrapped around it at each point where a leaf joins?",
            "Polygonaceae are famous for this papery tube (called an ochrea) — "
            "look at every leaf joint on the stem."
        ):
            result(
                "Polygonaceae",
                "Dock / Knotweed Family",
                "Papery sheath (ochrea) around stem at each leaf-joint — the key feature. "
                "Small petalless flowers. Very common in damp or disturbed ground.",
                "Dock (Rumex), Knotweed (Polygonum), Bistort, "
                "Buckwheat (Fagopyrum), Japanese knotweed (Fallopia)"
            )
            return

        if ask(
            "Does the plant have STINGING HAIRS that cause a painful sting?",
            "Stinging nettles have hollow hair-like needles that inject formic acid — "
            "you will know immediately if you have touched one!"
        ):
            result(
                "Urticaceae",
                "Nettle Family",
                "Stinging or non-stinging herbs. Tiny petalless flowers in clusters "
                "or dangly strings. Leaves often toothed.",
                "Stinging nettle (Urtica dioica), Small nettle (U. urens), "
                "Pellitory-of-the-wall (Parietaria) — no sting, grows on old walls"
            )
            return

        if ask(
            "Do the flowers hang in long, dangling, caterpillar-like clusters "
            "called CATKINS, on a tree or shrub?",
            "Catkins dangle like a woolly worm from twigs — "
            "common on birch, hazel, oak, willow in spring."
        ):
            if ask(
                "Does the tree produce ACORNS, hazelnuts, or beechnuts?",
                "Acorns sit in a scaly cup; hazelnuts have papery husks; "
                "beechnuts are in a prickly case."
            ):
                result(
                    "Fagaceae / Betulaceae / Juglandaceae",
                    "Oak / Beech / Birch / Hazel / Walnut Family",
                    "Wind-pollinated trees with catkins. Produce nuts or winged seeds. "
                    "Very important forest trees in Turkey.",
                    "Oak (Quercus), Beech (Fagus), Hornbeam (Carpinus), "
                    "Hazel (Corylus), Birch (Betula), Alder (Alnus), "
                    "Walnut (Juglans)"
                )
            else:
                result(
                    "Salicaceae",
                    "Willow / Poplar Family",
                    "Trees and shrubs with catkins. Seeds tiny with silky white hairs "
                    "(cotton-like fluff in spring). Leaves lance-shaped (willow) "
                    "or triangular (poplar).",
                    "Willow (Salix) — many Turkish species, "
                    "White poplar (Populus alba), Black poplar (P. nigra), "
                    "Aspen (P. tremula)"
                )
            return

        if ask(
            "Is it a tree or shrub whose 'fruit' is a FIG or a MULBERRY?",
            "Figs are pear-shaped with tiny flowers hidden inside. "
            "Mulberry fruits look like elongated raspberries."
        ):
            result(
                "Moraceae",
                "Mulberry / Fig Family",
                "Trees or shrubs. Flowers tiny and enclosed within the fruit (fig) "
                "or in dense heads (mulberry). Often have milky sap — but less "
                "prominent than Euphorbiaceae.",
                "Fig (Ficus carica), White mulberry (Morus alba), "
                "Black mulberry (Morus nigra)"
            )
            return

        if ask(
            "Are the leaves covered in a WHITE MEALY or powdery coating, "
            "as if dusted with flour?",
            "Rub the leaf — the white powder comes off on your finger. "
            "Very common on fat hen and orache."
        ):
            result(
                "Chenopodiaceae",
                "Goosefoot / Saltbush Family",
                "Small greenish petalless flowers. Leaves often with mealy-white coating. "
                "Very common in salty, disturbed, or nutrient-rich ground.",
                "Fat hen (Chenopodium album), Orache (Atriplex), "
                "Sea beet (Beta vulgaris subsp. maritima — ancestor of sugar beet), "
                "Glasswort (Salicornia), Spinach (Spinacia)"
            )
            return

        if ask(
            "Do the flowers have COLOURED SEPALS "
            "(a yellow, white, or pink tube) but NO real petals?",
            "In Thymelaeaceae the coloured part is actually the sepal-tube, not petals. "
            "Daphne flowers are very fragrant and the tube is pink or white."
        ):
            result(
                "Thymelaeaceae",
                "Daphne Family",
                "No petals — the petal-like tube is made of fused sepals. "
                "Often very fragrant. Bark very tough and fibrous (used historically to make paper). "
                "Berries usually brightly coloured.",
                "Daphne (Daphne) — several Turkish species, "
                "Spurge-laurel (Daphne laureola)",
                warning="All parts of Daphne are POISONOUS — especially the berries."
            )
            return

        if ask(
            "Are the leaves SILVERY-grey, covered in tiny star-shaped scales, "
            "and is the fruit like a small olive or hip?",
            "Oleaster and sea-buckthorn look silvery-grey all over "
            "due to tiny scale-like hairs."
        ):
            result(
                "Elaeagnaceae",
                "Oleaster / Sea-buckthorn Family",
                "Leaves and stems densely covered in silvery scales — "
                "gives the plant a distinctive grey appearance. "
                "Small, fragrant, petalless flowers. Fleshy fruit.",
                "Oleaster / Russian olive (Elaeagnus angustifolia), "
                "Sea-buckthorn (Hippophae rhamnoides)"
            )
            return

        if ask(
            "Is it a tree with WINGED SEEDS (helicopter 'keys') "
            "and OPPOSITE, pinnate (divided) leaves?",
            "Ash trees produce paired, paddle-shaped winged seeds in large hanging clusters. "
            "Leaves divided into 5-11 pairs of opposite leaflets — opposite each other."
        ):
            result(
                "Oleaceae (Fraxinus)",
                "Ash Tree — Olive Family",
                "Ash flowers have no petals. Opposite compound leaves. "
                "Winged fruits (samaras) in drooping bunches. "
                "Other Oleaceae have petals (olive, lilac, privet).",
                "Ash (Fraxinus excelsior, F. angustifolia)"
            )
            return

        result(
            "Amaranthaceae",
            "Amaranth Family",
            "Tiny petalless flowers in dense spikes or clusters. "
            "Closely related to Chenopodiaceae (goosefoot). "
            "Often in disturbed or cultivated ground.",
            "Amaranth (Amaranthus retroflexus — common weed), "
            "Rough pigweed, Love-lies-bleeding (A. caudatus)"
        )
        return

    # ── has petals ────────────────────────────────────────────

    # ── fumitory (very distinctive, check early) ─────────────
    if ask(
        "Do the flowers look like tiny TUBES or POUCHES — "
        "with a rounded spur or pouch at the back — "
        "hanging in small clusters?",
        "Fumitory flowers look like small elongated lockets or tubes. "
        "Each petal has a distinctive shape. Often pink/purple/white. "
        "Corydalis may be yellow."
    ):
        result(
            "Fumariaceae",
            "Fumitory / Corydalis Family",
            "4 petals in two pairs. Outer pair has one or two pouches/spurs. "
            "Delicate, often feathery leaves. Often scrambling or climbing.",
            "Fumitory (Fumaria officinalis — common arable weed), "
            "Corydalis (Corydalis) — yellow, pink, or purple, often in mountains"
        )
        return

    # ── FUSED vs FREE ─────────────────────────────────────────
    if ask(
        "Are the petals JOINED together at the base "
        "into a tube, bell, funnel, or cup — "
        "so that all petals come off together as one piece?",
        "Test: gently try to pull off ONE petal. "
        "If ALL petals detach as one piece = FUSED (YES). "
        "If a single petal peels off alone = FREE (NO)."
    ):

        # ══════════════════════════════════════════════════════
        #  FUSED-PETAL FAMILIES
        # ══════════════════════════════════════════════════════

        if ask(
            "Is what looks like one flower actually HUNDREDS of tiny flowers "
            "packed tightly into a flat or domed HEAD, like a daisy or dandelion?",
            "Look very closely at the centre of a 'daisy'. Each tiny yellow dot "
            "in the centre is a complete flower. Each outer 'petal' is also "
            "a complete tiny flower. A dandelion clock is one such head."
        ):
            result(
                "Compositae (Asteraceae)",
                "Daisy / Sunflower / Thistle Family",
                "THE largest flowering plant family. What looks like one flower is "
                "a HEAD of tens to hundreds of tiny flowers. Outer ray-florets "
                "look like petals; central disc-florets are tiny tubes. "
                "Seeds usually have a feathery parachute (pappus).",
                "Daisy (Bellis), Dandelion (Taraxacum), Chamomile (Anthemis), "
                "Thistle (Cirsium, Carduus), Knapweed (Centaurea), "
                "Ox-eye daisy (Leucanthemum), Groundsel (Senecio), "
                "Hawkweed (Hieracium), Wormwood (Artemisia), "
                "Everlasting (Helichrysum)"
            )
            return

        if ask(
            "Are the leaves arranged in WHORLS — "
            "rings of 4 or more leaves all radiating from the same level on the stem?",
            "Hold the stem and look straight down it: if leaves form a star-like "
            "ring at regular intervals, it is a whorl. "
            "Bedstraw and cleavers have 6-8 narrow leaves in each whorl."
        ):
            result(
                "Rubiaceae",
                "Bedstraw / Madder / Coffee Family",
                "Whorled leaves are the key. Tiny 4-petalled flowers, "
                "often in branched clusters. Stems often square and sticky "
                "(cleavers sticks to clothing). Fruit often in pairs.",
                "Bedstraw (Galium) — many Turkish species, "
                "Cleavers / Goosegrass (Galium aparine — the sticky plant), "
                "Madder (Rubia tinctorum — source of red dye), "
                "Woodruff (Galium odoratum)"
            )
            return

        if ask(
            "Are the flowers in a rounded or domed HEAD (like a pin-cushion), "
            "and does each tiny flower have a small scaly bract beneath it "
            "AND the whole head has a ruff of bracts around the outside?",
            "Scabious and teasel have this structure. "
            "Teasel heads are egg-shaped and very spiky when dry. "
            "Scabious heads are softer and blue/lilac/pink."
        ):
            result(
                "Dipsacaceae",
                "Teasel / Scabious Family",
                "Flowers in a head like Compositae BUT each floret is larger and "
                "individually wrapped in a small cup (epicalyx). "
                "Flowers often 4-lobed. Outer flowers often larger.",
                "Teasel (Dipsacus fullonum — tall, spiky, dried heads used for wool-carding), "
                "Field scabious (Knautia arvensis), "
                "Devil's bit scabious (Succisa pratensis)"
            )
            return

        if ask(
            "Does the plant have a distinctive SMELL — "
            "unpleasant, musky, or medicinal — "
            "AND are the tiny flowers in dense, flat-topped clusters?",
            "Valerian has a smell many people find unpleasant (cats love it). "
            "Flowers are tiny, pale pink or white, in dense flat clusters. "
            "The flower often has a small spur or pouch at the base."
        ):
            result(
                "Valerianaceae",
                "Valerian Family",
                "Small fused 5-petalled flowers in dense flat-topped clusters. "
                "Often asymmetric (1-3 stamens). Basal spur sometimes present. "
                "Distinctive smell. Fruit with feathery pappus.",
                "Valerian (Valeriana officinalis — medicinal), "
                "Red valerian (Centranthus ruber — on walls), "
                "Cornsalad / Lamb's lettuce (Valerianella — edible salad plant)"
            )
            return

        if ask(
            "Is it a SHRUB or small tree (or scrambling climber) "
            "with OPPOSITE leaves and tubular flowers "
            "followed by berries?",
            "Honeysuckle climbs and has fragrant tubular flowers. "
            "Elder is a shrub with flat flower-heads and black/red berries. "
            "Snowberry has white berries."
        ):
            result(
                "Caprifoliaceae",
                "Honeysuckle / Elder Family",
                "Shrubs, small trees, or climbers. OPPOSITE leaves always. "
                "Tubular or 5-lobed flowers. Usually followed by berries.",
                "Honeysuckle (Lonicera) — fragrant, tubular, "
                "Elder (Sambucus nigra) — flat white flower-heads, black berries, "
                "Guelder rose (Viburnum opulus) — white flat heads, red berries, "
                "Snowberry (Symphoricarpos)",
                warning="Elder and snowberry berries can cause sickness if eaten raw."
            )
            return

        if ask(
            "Is the stem clearly SQUARE (4 flat sides) "
            "when you roll it between your fingers?",
            "Most stems are round. A square stem feels blocky — "
            "like a 4-sided pencil. This is one of the most useful "
            "identification clues in the plant world!"
        ):
            result(
                "Labiatae (Lamiaceae)",
                "Mint / Dead-nettle / Sage Family",
                "Square stems + opposite leaves = almost certain Labiatae. "
                "Flowers 2-lipped (upper and lower lip, like a mouth). "
                "Often strongly aromatic — mint, thyme, lavender, sage. "
                "One of the most important families in Turkey.",
                "Mint (Mentha), Thyme (Thymus) — many Turkish species, "
                "Sage (Salvia) — 90+ Turkish species, "
                "Lavender (Lavandula), Rosemary (Rosmarinus), "
                "Dead-nettle (Lamium), Self-heal (Prunella), "
                "Woundwort (Stachys), Marjoram (Origanum), "
                "Basil (Ocimum), Hyssop (Hyssopus)"
            )
            return

        if ask(
            "Are the flowers arranged on a stem that CURLS OVER "
            "like a scorpion's tail or watch-spring, "
            "slowly straightening as more flowers open from the tip?",
            "This coiled arrangement is called a scorpioid cyme. "
            "Forget-me-nots are the classic example — the cluster starts "
            "tightly coiled and unrolls as it blooms."
        ):
            result(
                "Boraginaceae",
                "Borage / Forget-me-not / Bugloss Family",
                "Coiled scorpioid cyme that unrolls as it blooms. "
                "Usually 5 fused petals with a short tube. Often blue, pink, or white. "
                "Leaves and stems usually rough and bristly-hairy. Leaves alternate.",
                "Forget-me-not (Myosotis) — many Turkish species, "
                "Borage (Borago officinalis), Bugloss (Anchusa), "
                "Viper's bugloss (Echium) — tall blue spikes, "
                "Hound's-tongue (Cynoglossum), "
                "Comfrey (Symphytum), Lungwort (Pulmonaria)"
            )
            return

        if ask(
            "Are the flowers in a NODDING or drooping cluster "
            "at the top of a leafless stalk, with petals often swept BACKWARDS?",
            "Primrose and cyclamen are the classic examples. "
            "Cyclamen has dramatically reflexed (swept-back) petals. "
            "Cowslip has nodding yellow bells."
        ):
            result(
                "Primulaceae",
                "Primrose / Cyclamen Family",
                "Usually 5 petals joined at base. Leaves often in a basal rosette. "
                "Flower stalk leafless. Flowers often nodding.",
                "Primrose (Primula vulgaris), Cowslip (Primula veris), "
                "Cyclamen (Cyclamen) — 8 Turkish species including C. coum, "
                "Loosestrife (Lysimachia), Scarlet pimpernel (Anagallis arvensis — "
                "tiny red or blue flowers that close before rain)"
            )
            return

        if ask(
            "Are there exactly 4 petals with exactly 2 stamens, "
            "and are the leaves OPPOSITE?",
            "Olive, lilac, and privet belong here. "
            "Lilac has 4-petalled fragrant purple/white flowers. "
            "Privet has small white 4-petalled flowers."
        ):
            result(
                "Oleaceae",
                "Olive / Lilac / Privet Family",
                "4 fused petals. Always exactly 2 stamens. Opposite leaves. "
                "Often woody shrubs or trees. Many are fragrant.",
                "Olive (Olea europaea) — very important in Turkey, "
                "Lilac (Syringa vulgaris), Privet (Ligustrum), "
                "Jasmine (Jasminum) — 5 petals here, "
                "Phillyrea, Fontanesia"
            )
            return

        if ask(
            "Is the flower IRREGULAR — "
            "does it have a clear TOP and BOTTOM (left side different from right)?",
            "A regular flower looks the same from any direction (like a star). "
            "An irregular flower clearly has an upper half and lower half — "
            "like a snapdragon or foxglove."
        ):
            if ask(
                "Does the flower look like a FOXGLOVE or SNAPDRAGON — "
                "a tube with an upper lip and a lower lip?",
                "Scrophulariaceae flowers look like a small mouth or tunnel. "
                "Mullein is large and yellow; foxglove is tall and tubular; "
                "eyebright is tiny."
            ):
                result(
                    "Scrophulariaceae",
                    "Figwort / Foxglove / Mullein Family",
                    "Irregular 2-lipped tubular flowers. Usually 4 stamens inside "
                    "(sometimes 2 or 5). Very diverse family — 100+ Turkish species. "
                    "Many are semi-parasitic on grass roots.",
                    "Foxglove (Digitalis — several Turkish species), "
                    "Mullein (Verbascum — 100+ Turkish species, large yellow spikes), "
                    "Snapdragon (Antirrhinum), Eyebright (Euphrasia), "
                    "Speedwell (Veronica), Lousewort (Pedicularis), "
                    "Cow-wheat (Melampyrum), Toadflax (Linaria)",
                    warning="Foxglove is HIGHLY POISONOUS — contains digitalis heart drugs."
                )
            else:
                result(
                    "Convolvulaceae",
                    "Bindweed / Morning-glory Family",
                    "Usually twining/climbing plants. Wide funnel or trumpet-shaped flower, "
                    "often with 5 faint stripes. Open in the morning, close by afternoon.",
                    "Bindweed (Convolvulus arvensis — common garden weed), "
                    "Field bindweed, Greater bindweed (Calystegia sepium), "
                    "Morning-glory (Ipomoea)",
                    warning="Some Convolvulaceae contain powerful purgative drugs."
                )
            return

        if ask(
            "Do the petals fold BACK like a star, "
            "with a noticeable yellow or orange CONE of stamens "
            "sticking forward from the centre?",
            "Tomato and potato flowers look like this — "
            "a swept-back star of petals with a pointy yellow column in the middle."
        ):
            result(
                "Solanaceae",
                "Nightshade / Potato Family",
                "5 petals fused at base, reflexed to form a star. "
                "Stamens fused into a yellow cone. Often produces berries. "
                "Leaves can smell unpleasant when crushed.",
                "Tomato (Lycopersicon), Potato (Solanum tuberosum), "
                "Deadly nightshade (Atropa belladonna — shiny black berries), "
                "Henbane (Hyoscyamus niger — sticky, evil-smelling), "
                "Black nightshade (Solanum nigrum), "
                "Tobacco (Nicotiana), Thorn-apple (Datura stramonium)",
                warning="Many are HIGHLY POISONOUS or hallucinogenic. "
                        "NEVER eat any berries from this family unless you are 100% certain."
            )
            return

        if ask(
            "Does the plant have a flat ROSETTE of leaves "
            "with strong, parallel veins running along the leaf, "
            "and a leafless flowering spike growing from the centre?",
            "Plantains are one of the most common lawn weeds — "
            "a flat star of ribbed leaves, with a tall slim spike of tiny flowers."
        ):
            result(
                "Plantaginaceae",
                "Plantain Family",
                "Basal rosette with strongly parallel-veined leaves. "
                "Tiny 4-lobed fused flowers in a spike or oval head. "
                "Extremely common in lawns, paths, and trampled ground.",
                "Ribwort plantain (Plantago lanceolata — narrow leaves, oval head), "
                "Greater plantain (P. major — broad flat leaves, long spike), "
                "Hoary plantain (P. media)"
            )
            return

        if ask(
            "Are the flowers INTENSELY BLUE, violet, or gentian-purple, "
            "with opposite leaves that have NO stalk?",
            "Gentian blue is one of the most vivid colours in the plant world. "
            "Leaves clasping the stem at the base. Flowers often close at night."
        ):
            result(
                "Gentianaceae",
                "Gentian Family",
                "Usually 4-5 fused petals, intensely coloured. "
                "Leaves opposite, stalkless, often clasping the stem. "
                "Flowers often close at night or in cloud. "
                "Many high-mountain species in Turkey.",
                "Gentian (Gentiana) — vivid blue trumpet flowers, "
                "Autumn gentian (Gentianella), "
                "Centaury (Centaurium — small pink star flowers, very common)"
            )
            return

        if ask(
            "Are the flowers bell-shaped or star-shaped, "
            "usually BLUE or VIOLET or WHITE, "
            "with 5 fused petals?",
            "Bellflowers are usually clearly bell or star-shaped and blue/violet. "
            "Not the small tubular flowers of mint or borage — bigger and more showy."
        ):
            result(
                "Campanulaceae",
                "Bellflower Family",
                "5 fused petals forming a bell or star. "
                "Milky sap sometimes present. Leaves alternate. "
                "One of the most diverse families in Turkey — 70+ species.",
                "Bellflower (Campanula) — huge number of Turkish species, "
                "Peach-leaved bellflower (C. persicifolia), "
                "Clustered bellflower (C. glomerata), "
                "Sheep's bit (Jasione montana), "
                "Rampion (Phyteuma)"
            )
            return

        # default fused
        result(
            "Convolvulaceae / Polemoniaceae",
            "Bindweed / Jacob's-ladder Family",
            "5 fused petals forming a regular funnel or wheel. "
            "If it is a twining plant — likely Convolvulaceae. "
            "If it has pinnate leaves and blue flowers — likely Polemonium.",
            "Bindweed (Convolvulus), Morning-glory (Ipomoea), "
            "Jacob's-ladder (Polemonium caeruleum)"
        )
        return

    # ══════════════════════════════════════════════════════════
    #  FREE-PETAL FAMILIES
    # ══════════════════════════════════════════════════════════

    if ask(
        "Are the petals very UNEQUAL in size or shape, "
        "with the upper ones FRINGED or CUT into thin threads, "
        "and all the stamens clustered to ONE SIDE?",
        "Mignonette (Reseda) has a very odd flower — "
        "the upper petals are deeply fringed/divided, "
        "and all stamens pile to one side."
    ):
        result(
            "Resedaceae",
            "Mignonette Family",
            "Irregular flowers with divided/fringed upper petals. "
            "Stamens crowded to one side. Leaves simple or pinnate. "
            "Usually 4-8 petals. Often grows on disturbed ground.",
            "Mignonette (Reseda odorata — grown for scent), "
            "Wild mignonette (R. lutea — yellow, common weed), "
            "Weld (R. luteola — tall yellow, old yellow dye plant)"
        )
        return

    if ask(
        "Are there EXACTLY 4 petals arranged in a CROSS shape?",
        "Count carefully! The cabbage family ALWAYS has exactly 4 petals "
        "arranged in a cross (+ or x shape). "
        "There are usually 6 stamens (4 tall + 2 short)."
    ):
        result(
            "Cruciferae (Brassicaceae)",
            "Cabbage / Mustard Family",
            "ALWAYS exactly 4 petals in a cross. Usually 6 stamens (4 tall + 2 short). "
            "Seeds in a long thin pod (silique) or short round pod (silicula). "
            "Often smells of cabbage when crushed. Enormous family in Turkey.",
            "Cabbage / Kale / Mustard / Radish / Turnip (Brassica, Raphanus, Sinapis), "
            "Wallflower (Erysimum — many Turkish species), "
            "Shepherd's purse (Capsella — heart-shaped pods), "
            "Alyssum (many Turkish species, often white), "
            "Honesty (Lunaria — silvery pods), "
            "Watercress (Nasturtium officinale), Cress (Cardamine)"
        )
        return

    if ask(
        "Does the flower look like a BUTTERFLY or PEA — "
        "with one large upright 'flag' petal, "
        "two side 'wing' petals, "
        "and two bottom petals forming a 'keel' (like a boat hull)?",
        "Pea flowers are very distinctive. Hold one up: "
        "the big upper petal is the flag/standard, "
        "the two side petals are wings, "
        "and the two lower petals are joined into a keel."
    ):
        result(
            "Leguminosae (Fabaceae)",
            "Pea / Bean / Clover Family",
            "Butterfly-shaped flowers (standard, wings, keel). "
            "Seeds always grow in PODS. "
            "Root nodules fix nitrogen — making soil more fertile. "
            "Leaves usually compound (many small leaflets). "
            "Enormous family — 1,000+ Turkish species.",
            "Peas (Pisum), Beans (Vicia faba, Phaseolus), "
            "Clover (Trifolium) — dozens of Turkish species, "
            "Vetch (Vicia), Tare (Vicia), Medick (Medicago), "
            "Broom (Genista, Cytisus), Gorse (Ulex), "
            "Locust tree (Robinia), Wisteria, "
            "Liquorice (Glycyrrhiza), Astragalus (400+ Turkish species!)"
        )
        return

    if ask(
        "Do MANY tiny flowers grow on stalks that all radiate "
        "from the SAME point, making a flat-topped or domed "
        "UMBRELLA shape?",
        "The stalks spread like umbrella ribs from one central point — "
        "and each stalk may branch again the same way (a compound umbel). "
        "Think of fennel, cow parsley, or carrot flowers."
    ):
        result(
            "Umbelliferae (Apiaceae)",
            "Carrot / Parsley / Fennel Family",
            "Flowers in umbels (umbrella-shaped clusters). "
            "Stems often hollow. Leaves usually feathery and divided. "
            "Often aromatic when crushed. "
            "Huge family in Turkey — 400+ species.",
            "Carrot (Daucus carota — wild and cultivated), "
            "Fennel (Foeniculum vulgare), Anise (Pimpinella anisum), "
            "Cow parsley (Anthriscus sylvestris), Angelica, "
            "Hogweed (Heracleum), Coriander, Cumin, Dill, "
            "Eryngium (sea-holly — spiky blue, NOT an umbel at first glance!)",
            warning="Contains some of the DEADLIEST plants: "
                    "Hemlock (Conium maculatum — all parts lethal), "
                    "Hemlock water-dropwort (Oenanthe). NEVER eat anything from "
                    "this family unless you are 100% certain of the ID."
        )
        return

    if ask(
        "Does the lowest petal have a hollow SPUR "
        "pointing backwards behind the flower, "
        "and does the flower have 5 petals "
        "of clearly different sizes?",
        "Violet flowers have one large lower petal with a backward-pointing spur. "
        "The spur often has nectar inside. Usually blue, purple, or yellow."
    ):
        result(
            "Violaceae",
            "Violet / Pansy Family",
            "5 free petals of unequal size. Lowest petal with a backward-pointing spur. "
            "Leaves simple. Some species (Viola) have chasmogamous and cleistogamous flowers "
            "(visible flowers and tiny self-pollinating flowers).",
            "Violet (Viola) — many Turkish species, "
            "Pansy (Viola tricolor and hybrids), "
            "Dog violet (V. canina)"
        )
        return

    if ask(
        "Does the plant have a very distinctive LONG BEAK or "
        "needle-shaped fruit (like a crane's bill or stork's bill) "
        "formed from the seed-pod?",
        "Geranium and Erodium fruits are unmistakable — "
        "a long pointed 'beak' forms in the centre of the flower, "
        "and when ripe it twists and flings seeds away."
    ):
        result(
            "Geraniaceae",
            "Crane's-bill / Stork's-bill Family",
            "5 free petals, usually 10 stamens. "
            "Long beak-shaped fruit (the 'crane's bill' or 'stork's bill'). "
            "Leaves often lobed or deeply divided. Many garden and wild species.",
            "Crane's-bill (Geranium) — many Turkish species, "
            "Stork's-bill (Erodium) — leaves often more feathery, "
            "Garden geranium / Pelargonium (technically a different genus)"
        )
        return

    if ask(
        "Do the leaves have EXACTLY 3 HEART-SHAPED leaflets "
        "(like a shamrock or clover leaf), "
        "which fold downwards at night or when touched?",
        "Wood-sorrel leaves look like clover but each leaflet is perfectly heart-shaped. "
        "The whole leaf droops in the dark. "
        "Tastes pleasantly sour (contains oxalic acid)."
    ):
        result(
            "Oxalidaceae",
            "Wood-sorrel Family",
            "3 heart-shaped leaflets that fold at night. "
            "5 free petals, 10 stamens. "
            "Sour taste from oxalic acid.",
            "Wood-sorrel (Oxalis acetosella — white flowers in shade), "
            "Procumbent yellow-sorrel (Oxalis corniculata — yellow, common garden weed)"
        )
        return

    # ── now branch on number of stamens ──────────────────────
    if ask(
        "Does the flower have MORE THAN 10 STAMENS "
        "(very many pollen-making threads in the centre)?",
        "Rough count: if there are clearly more than 10 "
        "— a messy brush of many threads — say YES. "
        "If you can count them easily (5, 6, 8, 10) — say NO."
    ):

        if ask(
            "Are all the stamens JOINED together at the base "
            "into one central column or tube?",
            "In the mallow family, all stamens are fused into one structure "
            "that looks like a cylinder wrapped around the style in the centre."
        ):
            result(
                "Malvaceae",
                "Mallow Family",
                "5 free petals. Stamens fused into a central column — "
                "the key feature of the mallow family. "
                "Leaves often lobed or rounded with palmate veins.",
                "Mallow (Malva) — several Turkish species, "
                "Tree mallow (Lavatera), Hollyhock (Alcea rosea), "
                "Hibiscus, Cotton (Gossypium hirsutum)"
            )
            return

        if ask(
            "Are the petals very LARGE, deeply coloured (red or pink), "
            "and is the plant a large lush perennial — "
            "like a peony?",
            "Peonies are distinctive — huge silky petals, "
            "many stamens, and large divided leaves."
        ):
            result(
                "Paeoniaceae",
                "Peony Family",
                "Large, showy flowers with many free petals and many stamens. "
                "Leaves large and much-divided. "
                "Fruit a group of large fleshy follicles. "
                "Only one genus (Paeonia) with several Turkish species.",
                "Peony (Paeonia mascula, P. peregrina, "
                "P. kesrouanensis and others — wild in Turkish mountains)"
            )
            return

        if ask(
            "Are the petals very CRINKLED or CRUMPLED when first opening, "
            "as if they came out of a tight bud screwed up, "
            "and do they fall off within a day or two?",
            "Rock-rose (Cistus) and sun-rose (Helianthemum) petals "
            "look crumpled fresh from the bud and are very delicate."
        ):
            result(
                "Cistaceae",
                "Rock-rose / Sun-rose Family",
                "Petals crumpled in bud, delicate, falling quickly. "
                "Many stamens. Leaves often opposite, sometimes sticky or hairy. "
                "Typical of dry, rocky, sunny Mediterranean habitats.",
                "Rock-rose (Cistus) — several Turkish species (sticky shrubs), "
                "Sun-rose / Common rock-rose (Helianthemum) — "
                "many Turkish species, low-growing on rocks"
            )
            return

        if ask(
            "Do the leaves have tiny TRANSLUCENT DOTS "
            "visible when held up to the light?",
            "Hold a leaf up against bright light — "
            "Hypericum leaves have tiny clear windows (oil glands). "
            "Flowers usually yellow with many stamens."
        ):
            result(
                "Guttiferae (Hypericaceae)",
                "St John's-wort Family",
                "Leaves with translucent oil-gland dots (see against light). "
                "Flowers usually yellow, with many stamens in 3 bundles. "
                "Opposite leaves. No stipules.",
                "St John's-wort (Hypericum) — 70+ Turkish species, "
                "H. perforatum (common, medicinal — the dots are most visible here)"
            )
            return

        # many stamens, not the above — Ranunculaceae
        result(
            "Ranunculaceae",
            "Buttercup / Crowfoot Family",
            "Many FREE stamens AND many free pistils (carpels) in the centre — "
            "unusual combination that marks this family. "
            "Petals sometimes shiny (especially in yellow buttercups). "
            "Great variety of flower shapes in this family.",
            "Buttercup (Ranunculus) — many Turkish species, "
            "Anemone, Wood anemone (A. nemorosa), "
            "Clematis (climbing), Delphinium / Larkspur (irregular), "
            "Columbine (Aquilegia — spurred petals), "
            "Hellebore (Helleborus), Pheasant's-eye (Adonis), "
            "Meadow-rue (Thalictrum)",
            warning="Most are poisonous — do not eat."
        )
        return

    # ── 10 or fewer stamens ───────────────────────────────────

    if ask(
        "Are the petals NOTCHED or FORKED at the tip "
        "(as if someone cut a V into each petal), "
        "OR is the green CALYX TUBE below the petals "
        "inflated, striped, or tubular?",
        "Pink and campion flowers have this look. "
        "Hold a petal up: is the tip split into two points? "
        "Also look at the green calyx tube — "
        "Silene (campion) calyx is often very distinctive — striped or inflated."
    ):
        result(
            "Caryophyllaceae",
            "Pink / Campion / Carnation Family",
            "Petals often notched or fringed at the tip. "
            "Leaves in OPPOSITE PAIRS, usually narrow and stalkless. "
            "Stem joints (nodes) often swollen. "
            "Calyx tube often striped or inflated. "
            "One of the biggest dicot families in Turkey.",
            "Carnation / Pink (Dianthus) — 70+ Turkish species, "
            "Campion (Silene) — 100+ Turkish species (largest genus in Turkey!), "
            "Chickweed (Stellaria media — the common low weed), "
            "Stitchwort (Cerastium), Soapwort (Saponaria), "
            "Gypsophila (Baby's-breath) — 30+ Turkish species, "
            "Ragged Robin (Lychnis)"
        )
        return

    if ask(
        "Does the plant have tiny SCALE-LIKE or NEEDLE-LIKE leaves "
        "(not proper flat leaves), "
        "and does it grow near water or in salty/dry ground?",
        "Tamarisk looks feathery and wispy — "
        "the 'leaves' are tiny overlapping scales on pink-tinged twigs. "
        "Small pink or white flowers. Common along Turkish riversides."
    ):
        result(
            "Tamaricaceae",
            "Tamarisk Family",
            "Scale-like or thread-like overlapping leaves. "
            "Flowers tiny, pink or white, in dense spikes. "
            "Tolerates salty and dry conditions. "
            "Feathery, graceful appearance.",
            "Tamarisk (Tamarix) — several Turkish species, "
            "common along rivers and coasts"
        )
        return

    if ask(
        "Are the leaves VERY THICK, FLESHY, and rubbery — "
        "like a succulent houseplant — "
        "often in tight rosettes on rocks or old walls?",
        "Succulent leaves feel plump and full of water. "
        "Much thicker than a normal leaf. "
        "Very common on stony mountain slopes and old walls."
    ):
        result(
            "Crassulaceae",
            "Stonecrop / Houseleek Family",
            "Fleshy succulent leaves storing water. "
            "Often in rosettes. Flowers star-shaped, 5 petals "
            "(or 6, 8 etc — varies by genus). "
            "Very common on rock ledges, walls, and dry slopes in Turkey.",
            "Stonecrop (Sedum) — dozens of Turkish species, "
            "Houseleek (Sempervivum) — fleshy rosette with offsets, "
            "Rosularia — small high-mountain rosette plants"
        )
        return

    if ask(
        "Are the leaves thick and fleshy "
        "AND does the flower open ONLY in sunshine "
        "(closed on cloudy days)?",
        "Purslane is a low, spreading, fleshy-leaved plant "
        "found in cultivated or disturbed ground. "
        "The yellow flowers open only when the sun is bright."
    ):
        result(
            "Portulacaceae",
            "Purslane Family",
            "Succulent, fleshy leaves. Flowers open in sunshine only. "
            "2 sepals (unusual). 4-6 petals. "
            "Common in gardens, cultivated ground.",
            "Purslane (Portulaca oleracea — common flat weed, edible), "
            "Spring beauty (Claytonia)"
        )
        return

    if ask(
        "Is it a small delicate plant of ROCKS or MOUNTAINS, "
        "with leaves in a basal rosette "
        "and flowers in a loose branched cluster?",
        "Saxifrages are classic mountain plants — "
        "often growing in crevices in rocks. "
        "5 petals, 10 stamens, 2 styles."
    ):
        result(
            "Saxifragaceae",
            "Saxifrage Family",
            "Usually 5 free petals, 10 stamens. Basal rosette of leaves. "
            "Flowers in loose clusters. Often on rocks or in mountains. "
            "Leaves sometimes with lime-secreting pores.",
            "Saxifrage (Saxifraga) — many Turkish high-mountain species, "
            "Golden saxifrage (Chrysosplenium)"
        )
        return

    if ask(
        "Does the plant grow in DAMP or WET places, "
        "and does the flower have 6 petals "
        "(sometimes 4 or 8), often pink or purple, "
        "looking slightly crinkled?",
        "Loosestrife (Lythrum salicaria) is common in wet ground — "
        "tall spike of magenta-pink flowers with 6 crinkled petals."
    ):
        result(
            "Lythraceae",
            "Loosestrife / Henna Family",
            "Usually 6 petals (sometimes 4-8), often crinkled. "
            "Flowers with a distinct floral tube. "
            "Often in damp or wet places.",
            "Purple loosestrife (Lythrum salicaria — tall magenta spikes), "
            "Henna (Lawsonia inermis — source of henna dye), "
            "Water purslane (Lythrum portula)"
        )
        return

    if ask(
        "Does the flower have EXACTLY 4 free petals, "
        "and is there a long, narrow SEED POD forming "
        "directly below the petals?",
        "Willowherb has 4 petals and a very long narrow pod "
        "(the ovary) forming below. "
        "When ripe the pods split and release seeds with silky white hairs."
    ):
        result(
            "Onagraceae",
            "Willowherb / Fireweed Family",
            "4 free petals. Long narrow seed pod forming below the flower "
            "(inferior ovary). Seeds with silky white parachute-hairs. "
            "Often in disturbed or burnt ground.",
            "Willowherb (Epilobium) — several Turkish species, "
            "Rosebay willowherb / Fireweed (Chamerion angustifolium — "
            "tall pink spikes on burnt/cleared ground), "
            "Evening-primrose (Oenothera — large yellow 4-petalled flowers)"
        )
        return

    if ask(
        "Does the flower have 5 small, very DELICATE petals "
        "(often blue or yellow) on a plant with "
        "very NARROW or thread-like leaves?",
        "Flax has small, round, pale-blue petals that fall by midday. "
        "Leaves narrow and stalkless. "
        "Flax (linen) is one of the oldest crop plants."
    ):
        result(
            "Linaceae",
            "Flax Family",
            "5 free petals, 5 stamens. Petals delicate, falling quickly. "
            "Leaves narrow, stalkless, alternate. Often in dry grassland.",
            "Flax (Linum usitatissimum — source of linen and linseed oil), "
            "Perennial flax (L. perenne — blue), "
            "Yellow flax (L. flavum), "
            "Many wild Linum species in Turkish mountains"
        )
        return

    if ask(
        "Is it a THORNY SHRUB with leaves in clusters "
        "on short shoots, and small yellow flowers "
        "in drooping clusters, followed by red or black berries?",
        "Barberry (Berberis) has sharp 3-pronged spines, "
        "and small yellow flowers. "
        "The berries are tart and red."
    ):
        result(
            "Berberidaceae",
            "Barberry Family",
            "Thorny shrubs. 6 petals and 6 stamens (unusual!). "
            "Leaves in clusters on short spurs. "
            "Bark and roots contain berberine (yellow dye, antimicrobial).",
            "Barberry (Berberis crataegina and others — several Turkish species), "
            "Epimedium (Epimedium — low plant, unusual spurred flowers)"
        )
        return

    if ask(
        "Does the plant grow in DRY, HOT, stony places, "
        "and do the leaves have just 2 or a FEW pairs of "
        "leaflets arranged opposite each other?",
        "Caltrop (Tribulus terrestris) produces the sharp spiny fruit "
        "that punctures bare feet and bicycle tyres. "
        "Paired leaflets. Small yellow flowers."
    ):
        result(
            "Zygophyllaceae",
            "Caltrop / Bean-caper Family",
            "Leaves pinnate with few pairs of opposite leaflets. "
            "5 petals, 10 stamens. Dry, hot, stony habitats. "
            "Fruit often with spines or ridges.",
            "Caltrop (Tribulus terrestris — the spiny fruit), "
            "Bean-caper (Zygophyllum), Peganum (Harmal / Syrian rue — "
            "strong-smelling, in degraded steppe)",
            warning="Peganum harmala (Syrian rue) contains alkaloids and is toxic."
        )
        return

    if ask(
        "Does the plant have STRONGLY AROMATIC leaves "
        "with tiny TRANSLUCENT DOTS visible when held to the light, "
        "like a citrus or rue leaf?",
        "Rue (Ruta) and similar plants have deeply divided leaves "
        "with a very pungent smell and tiny oil-gland dots — "
        "like miniature citrus leaves."
    ):
        result(
            "Rutaceae",
            "Rue / Citrus Family",
            "Aromatic leaves with translucent oil glands. "
            "4-5 petals, usually as many or twice as many stamens. "
            "Includes all citrus fruits.",
            "Rue (Ruta graveolens — the herb, blue-green leaves, yellow flowers), "
            "Burning bush (Dictamnus albus — flammable oils!), "
            "Haplophyllum — several Turkish species"
        )
        return

    if ask(
        "Are the flowers small and IRREGULAR, looking vaguely "
        "like a tiny pea-flower but with two large coloured WING SEPALS?",
        "Milkwort has small pink/blue/white flowers where two sepals "
        "are large and coloured like petals (the 'wings'), "
        "making them look like a miniature pea-flower."
    ):
        result(
            "Polygalaceae",
            "Milkwort Family",
            "2 large wing-like sepals (coloured like petals). "
            "3 small petals with fringed keel petal. "
            "Leaves simple, alternate. Small plants of grassland.",
            "Milkwort (Polygala) — several Turkish species, "
            "usually blue, pink, or white flowers"
        )
        return

    if ask(
        "Is it a TREE or large SHRUB with OPPOSITE, "
        "LOBED leaves (like a hand), "
        "and paired winged seeds (helicopter 'keys')?",
        "Maple leaves are palmately lobed — "
        "spreading from a central point like fingers. "
        "The seeds always come in pairs with wings, "
        "spinning as they fall."
    ):
        result(
            "Aceraceae (Sapindaceae)",
            "Maple Family",
            "Opposite, palmately lobed leaves. "
            "Paired winged fruits (samaras) that spin. "
            "Small flowers in clusters, usually 5 petals.",
            "Sycamore (Acer pseudoplatanus), "
            "Field maple (A. campestre), "
            "Montpellier maple (A. monspessulanum), "
            "Cappadocian maple (A. cappadocicum) — several Turkish species"
        )
        return

    if ask(
        "Is it a SHRUB or small TREE with OPPOSITE, "
        "untoothed oval leaves and small 4-petalled "
        "WHITE flowers in flat-topped clusters?",
        "Dogwood has oval opposite leaves with veins curving towards the tip. "
        "Small white cross-shaped flowers in flat clusters. "
        "Red twigs in winter."
    ):
        result(
            "Cornaceae",
            "Dogwood / Cornelian cherry Family",
            "Opposite, untoothed leaves with curved veins. "
            "4 free petals. "
            "Cornelian cherry (Cornus mas) is a common Turkish shrub "
            "with yellow flowers on bare branches before leaves appear.",
            "Dogwood (Cornus sanguinea — red-twigged, black berries), "
            "Cornelian cherry (Cornus mas — early yellow flowers, red fruit)"
        )
        return

    if ask(
        "Is it a THORNY SHRUB with small, inconspicuous "
        "4-5 petalled flowers and fruits resembling tiny plums or olives?",
        "Buckthorn and Christ's-thorn are spiny shrubs "
        "with small flowers and small fleshy fruits. "
        "Very common in Turkish scrubland (maquis)."
    ):
        result(
            "Rhamnaceae",
            "Buckthorn Family",
            "Thorny or spiny shrubs or trees. "
            "Flowers small, 4-5 petalled, 4-5 stamens. "
            "Fruit a small drupe (berry-like). "
            "Disc-like nectary inside the flower.",
            "Buckthorn (Rhamnus) — several Turkish species, "
            "Christ's-thorn (Paliurus spina-christi — used for fencing, "
            "the crown-of-thorns plant), "
            "Jujube (Ziziphus jujuba)"
        )
        return

    if ask(
        "Is it a SHRUB or tree with LIME-tree (linden) type "
        "leaves — large, heart-shaped, toothed — "
        "and fragrant clusters of small creamy-yellow flowers "
        "attached to a long narrow bract?",
        "Lime / linden trees have large heart-shaped leaves and "
        "clusters of fragrant small flowers attached to a long leaf-like bract. "
        "Very distinctive in summer."
    ):
        result(
            "Tiliaceae",
            "Lime / Linden Family",
            "Large heart-shaped, toothed leaves. "
            "Clusters of small fragrant yellow-white flowers "
            "attached to a distinctive long narrow bract. "
            "Fruit small, round, woody.",
            "Lime / Linden (Tilia) — several Turkish species, "
            "T. tomentosa (silver lime), T. rubra — important street trees"
        )
        return

    # ── catch-all ─────────────────────────────────────────────
    print(M + BO + """
  ╔═══════════════════════════════════════════════╗
  ║       Needs a closer look...                 ║
  ╚═══════════════════════════════════════════════╝""" + X)
    print("""
  Your plant did not fit neatly into the families covered here.
  Turkey has over 3,000 dicotyledon species — this key covers the most common families,
  but some less common ones are not included.

  Other families to consider:
    Tiliaceae (lime/linden) — large heart-shaped leaves, bract-attached flower cluster
    Aceraceae (maple) — opposite lobed leaves, paired winged seeds
    Anacardiaceae (sumach/pistachio) — compound leaves, resinous smell
    Celastraceae (spindle tree) — orange-seeded capsules
    Aquifoliaceae (holly) — spiny evergreen leaves
    Myrtaceae (myrtle) — aromatic evergreen, white flowers, dark berries
    Araliaceae (ivy) — Hedera helix (ivy), lobed leaves, climbing
    Hamamelidaceae (witch-hazel) — Liquidambar (sweet gum)

  Suggestions:
    1. Try again from the beginning — a second look often helps.
    2. Take a photo and use the iNaturalist app (free) — it identifies plants from photos.
    3. Check a printed Flora of Turkey or a Turkish wildflower guide.
""")


# ──────────────────────────────────────────────────────────────
def main():
    while True:
        clear()
        banner()
        print("  Look carefully at your plant, then answer each question.")
        print("  y = YES   |   n = NO   |   r = restart from the beginning\n")
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
