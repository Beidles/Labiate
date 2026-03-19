import ui
import os

# =========================================================
# GLOSSARY
# =========================================================

GLOSSARY = {
    "annual": "A plant that lives for one growing season, then dies.",
    "perennial": "A plant that lives for more than two years.",
    "herb": "A plant with soft stems, not woody.",
    "shrub": "A woody plant smaller than a tree.",
    "woody": "Hard stems like a bush.",
    "stamen": "The male flower part that makes pollen.",
    "fertile stamen": "A stamen that really makes pollen.",
    "sterile": "Not making pollen or seeds.",
    "corolla": "All the petals together.",
    "upper lip": "The top part of a two-lipped flower.",
    "lower lip": "The bottom part of a two-lipped flower.",
    "calyx": "The outer cup of the flower, made of sepals.",
    "calyx tube": "The lower joined part of the calyx.",
    "calyx teeth": "The points or lobes at the top of the calyx.",
    "bilabiate": "Two-lipped.",
    "gynobasic style": "The style comes up from between the 4 little fruit parts.",
    "style": "The thin female part between ovary and stigma.",
    "verticillaster": "A mint-family flower cluster that looks like a ring around the stem.",
    "inflorescence": "The way flowers are arranged on the plant.",
    "spike": "Flowers arranged along a stem.",
    "capitate": "Head-like, flowers crowded into a rounded group.",
    "raceme": "Flowers arranged along a stem, each on a little stalk.",
    "cymose": "A flower cluster where the middle flower opens first.",
    "bract": "A leaf-like part near flowers.",
    "bracteole": "A very small bract.",
    "axil": "The angle where a leaf joins the stem.",
    "subsessile": "Almost without a stalk.",
    "petiolate": "Having a leaf stalk.",
    "ovate": "Egg-shaped.",
    "linear": "Long and very narrow.",
    "lanceolate": "Shaped like a spear point.",
    "suborbicular": "Almost round.",
    "hastate": "Spear-shaped with pointed side lobes.",
    "digitate": "Parts spreading from one point, like fingers.",
    "pinnate": "Leaf parts arranged along both sides of a middle line.",
    "pinnatisect": "Deeply cut almost to the middle line.",
    "lobed": "Divided into parts.",
    "dentate": "Toothed.",
    "entire": "Smooth-edged, no teeth.",
    "conduplicate": "Folded lengthwise.",
    "revolute": "Leaf edge rolled backward.",
    "glabrous": "Without hairs.",
    "pilose": "Soft hairy.",
    "villous": "Long soft hairs.",
    "tomentose": "Densely covered in matted hairs.",
    "lanate": "Woolly.",
    "indumentum": "The hair covering of a plant.",
    "glandular-punctate": "Covered with tiny gland dots, often holding oils.",
    "resupinate": "Twisted upside down.",
    "falcate": "Curved like a sickle.",
    "concave": "Curved inward.",
    "sigmoid": "S-shaped.",
    "appendage": "A small extra part or flap.",
    "declinate": "Bent downward.",
    "exserted": "Sticking out beyond the flower opening.",
    "included": "Kept inside, not sticking out.",
    "deflexed": "Bent downward sharply.",
    "subulate": "Very narrow and pointed.",
    "spinose": "Spiny.",
    "aristate": "Ending in a bristle.",
    "gibbous": "Swollen on one side.",
    "dorsally compressed": "Flattened from the back side.",
    "flange": "A wing-like ridge.",
    "ciliolate": "With tiny hairs on the edge.",
    "veined": "Showing veins clearly.",
    "ribbed": "Showing raised lines clearly.",
    "sinus": "The notch between two lobes.",
    "nutlet": "One of the 4 little seed-like fruit parts in many mint plants.",
    "truncate": "Ending straight across, like cut off.",
    "trigonous": "Three-angled.",
    "stoloniferous": "Making runners that spread along the ground.",
    "rhizome": "An underground stem.",
    "procumbent": "Lying along the ground.",
    "erect": "Standing upright.",
    "suffruticose": "Woody at the base, softer above.",
    "accrescent": "Getting larger as fruit develops.",
    "membranous-reticulate": "Thin and net-veined, like dry paper."
}

# =========================================================
# OPTIONAL IMAGES
# Put photos in images/ folder, same project folder
# =========================================================

GENUS_IMAGES = {
    "Ajuga": "ajuga.jpg",
    "Teucrium": "teucrium.jpg",
    "Salvia": "salvia.jpg",
    "Lamium": "lamium.jpg",
    "Thymus": "thymus.jpg",
    "Stachys": "stachys.jpg",
    "Satureja": "satureja.jpg",
    "Micromeria": "micromeria.jpg",
    "Origanum": "origanum.jpg",
    "Mentha": "mentha.jpg",
    "Melissa": "melissa.jpg",
    "Nepeta": "nepeta.jpg",
    "Ballota": "ballota.jpg",
    "Marrubium": "marrubium.jpg",
    "Prunella": "prunella.jpg",
    "Phlomis": "phlomis.jpg",
    "Lavandula": "lavandula.jpg",
    "Rosmarinus": "rosmarinus.jpg"
}

# =========================================================
# KEY DATA
# Each step has:
# question
# help
# yes -> next step or result
# no  -> next step or result
# =========================================================

KEY = {
    "start": {
        "question": "1. How many fertile stamens do you see?",
        "help": "Stamens are the pollen-making parts. Many mint-family flowers have 4. Count only the stamens that really make pollen.",
        "yes_text": "2 or 3 fertile stamens",
        "no_text": "4 fertile stamens, or upper pair reduced/sterile",
        "yes": "k2",
        "no": "k6"
    },
    "k2": {
        "question": "2. Are the staminal connectives long and stretched out?",
        "help": "This is a more advanced flower detail. In Salvia the stamens are very special and look jointed or lever-like.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Salvia", "Long special stamens strongly point to Salvia."),
        "no": "k3"
    },
    "k3": {
        "question": "3. Is it an evergreen woody shrub with narrow leaves and pale blue flowers?",
        "help": "Think of rosemary-type plants: woody, bushy, narrow leaves.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Rosmarinus", "This matches rosemary in the old Flora treatment."),
        "no": "k4"
    },
    "k4": {
        "question": "4. Are the flower clusters far apart in upper leaf axils, and are the leaves strongly toothed or deeply cut?",
        "help": "Leaf axil means the angle where the leaf joins the stem.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Lycopus", "This combination fits Lycopus."),
        "no": "k5"
    },
    "k5": {
        "question": "5. Is it a woody shrub with hastate leaves and slender upright spikes?",
        "help": "Hastate means spear-shaped with side points near the base.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Dorystoechas", "This combination points to Dorystoechas."),
        "no": ("Ziziphora", "This branch points to Ziziphora.")
    },
    "k6": {
        "question": "6. Is the upper lip of the corolla absent or very tiny?",
        "help": "The corolla is the petals together. In some genera the upper lip is almost missing.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k7",
        "no": "k8"
    },
    "k7": {
        "question": "7. Does the flower look almost one-lipped, with a 5-lobed lower lip?",
        "help": "This helps separate Teucrium and Ajuga.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Teucrium", "A nearly one-lipped flower fits Teucrium."),
        "no": ("Ajuga", "A reduced upper lip and 3-lobed lower lip fits Ajuga.")
    },
    "k8": {
        "question": "8. Does the plant have branched hairs like forked, star-shaped, or tree-like hairs?",
        "help": "Use a hand lens if you can. If each hair branches, choose Yes.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k9",
        "no": "k14"
    },
    "k9": {
        "question": "9. Are the flower clusters in stalked spikes, and does the upper lip of the calyx have a small appendage?",
        "help": "This combination is typical of lavender-type plants.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Lavandula", "This points strongly to Lavandula."),
        "no": "k10"
    },
    "k10": {
        "question": "10. Do the stamens stick out beyond the upper lip, and is the flower twisted upside down?",
        "help": "Upside down here means resupinate.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Cyclotrichium", "This branch points to Cyclotrichium."),
        "no": "k11"
    },
    "k11": {
        "question": "11. Is the upper lip clearly curved like a sickle?",
        "help": "Sickle-shaped means falcate.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Phlomis", "A strongly curved upper lip fits Phlomis."),
        "no": "k12"
    },
    "k12": {
        "question": "12. Is the inside of the calyx tube mostly smooth or only weakly hairy?",
        "help": "Look into the throat of the calyx if possible.",
        "yes_text": "Yes",
        "no_text": "No, obvious long stiff hairs inside",
        "yes": ("Stachys", "This branch points to Stachys."),
        "no": "k13"
    },
    "k13": {
        "question": "13. Are the stamens inside the corolla tube, and is the calyx not widened above?",
        "help": "This separates Marrubium and Ballota.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Marrubium", "Included stamens and a narrower calyx fit Marrubium."),
        "no": ("Ballota", "A widened calyx above fits Ballota.")
    },
    "k14": {
        "question": "14. Does the fruiting calyx become much larger, thin, and net-veined with broad spreading lobes?",
        "help": "This is a very special fruiting calyx shape.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k15",
        "no": "k17"
    },
    "k15": {
        "question": "15. Are the leaves woolly, and is the upper lip yellow while the lower part is orange-ish?",
        "help": "Woolly means lanate.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Eremostachys", "This branch points to Eremostachys."),
        "no": "k16"
    },
    "k16": {
        "question": "16. Is it a shrub with violet upside-down flowers and normal herb-like bracteoles?",
        "help": "If not, the other choice here is the spiny-bracted annual group.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Hymenocrater", "This branch points to Hymenocrater."),
        "no": ("Molucella", "This branch points to Molucella.")
    },
    "k17": {
        "question": "17. Is the calyx strongly 15-veined or 15-ribbed, with the upper stamens longer than the lower?",
        "help": "Look carefully at the calyx ribs and the length of the stamen pairs.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k18",
        "no": "k21"
    },
    "k18": {
        "question": "18. Do the calyx notches have a thickened fold at the base?",
        "help": "The notch between lobes is called a sinus.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k19",
        "no": "k20"
    },
    "k19": {
        "question": "19. Does the upper lip of the corolla have 2 inner folds, and are the bracteoles strongly veined and bristle-toothed?",
        "help": "If yes, this points to one very distinct genus.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Lallemantia", "This branch points to Lallemantia."),
        "no": ("Dracocephalum", "This branch points to Dracocephalum.")
    },
    "k20": {
        "question": "20. Are the flower clusters only 2 to 6 flowers in upper leaf axils, often facing one side, and is the plant creeping by runners?",
        "help": "Runners are stolons that spread along the ground.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Glechoma", "This branch points to Glechoma."),
        "no": ("Nepeta", "This branch points to Nepeta.")
    },
    "k21": {
        "question": "21. Is the corolla tube long and slender, a bit S-shaped, and does the calyx upper lip have a projecting flap?",
        "help": "This is the classic skullcap type flower.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Scutellaria", "This branch points to Scutellaria."),
        "no": "k22"
    },
    "k22": {
        "question": "22. Is the upper lip of the corolla clearly sickle-shaped?",
        "help": "Clearly curved like a sickle = falcate.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k23",
        "no": "k29"
    },
    "k23": {
        "question": "23. Is the calyx clearly two-lipped?",
        "help": "Two-lipped means the top and bottom parts look different.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k24",
        "no": "k25"
    },
    "k24": {
        "question": "24. Are the flowers packed into dense terminal spikes, with bracts hiding the calyces?",
        "help": "If the bracts cover the calyces, that is important here.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Prunella", "This branch points to Prunella."),
        "no": ("Wiedemannia", "This branch points to Wiedemannia.")
    },
    "k25": {
        "question": "25. Do the nutlets have little hair tufts at the tip?",
        "help": "You may need mature fruit and a hand lens to see this well.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k26",
        "no": "k27"
    },
    "k26": {
        "question": "26. Are the flowers small, pinkish-white, and are the leaves finger-like divided or almost entire?",
        "help": "If the flowers are much bigger and more yellowish, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Leonurus", "This branch points to Leonurus."),
        "no": ("Eremostachys", "This branch points to Eremostachys.")
    },
    "k27": {
        "question": "27. Are the pollen sacs smooth, with yellow flowers, and is the plant creeping by runners?",
        "help": "A creeping plant with yellow flowers suggests one choice here.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Galeobdolon", "This branch points to Galeobdolon."),
        "no": "k28"
    },
    "k28": {
        "question": "28. Are the bracteoles spiny, and does the lower lip have two blunt little bumps at its base?",
        "help": "That combination helps separate Galeopsis from Lamium.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Galeopsis", "This branch points to Galeopsis."),
        "no": ("Lamium", "This branch points to Lamium.")
    },
    "k29": {
        "question": "29. Do the stamens clearly stick out beyond the upper lip of the corolla?",
        "help": "If they extend well beyond the flower mouth, choose Yes.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k30",
        "no": "k39"
    },
    "k30": {
        "question": "30. Is the calyx clearly two-lipped, with the lower teeth very different from the upper ones?",
        "help": "This takes you to one important branch of the key.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k31",
        "no": "k35"
    },
    "k31": {
        "question": "31. Is it an annual or short-lived perennial, with stamens bent downward?",
        "help": "If it is woody-based or shrubby, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k32",
        "no": "k33"
    },
    "k32": {
        "question": "32. In fruit, is the calyx bent downward, with a broad rounded upper lip?",
        "help": "This separates Ocimum and Elsholtzia.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Ocimum", "This branch points to Ocimum."),
        "no": ("Elsholtzia", "This branch points to Elsholtzia.")
    },
    "k33": {
        "question": "33. Is the calyx tube NOT flattened on the back and without wing-like flanges?",
        "help": "If it is flattened and has side ridges, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Thymus", "This branch points to Thymus."),
        "no": "k34"
    },
    "k34": {
        "question": "34. Is the inflorescence spike-like, with a 13-veined calyx and folded leaves?",
        "help": "If instead the flowers make a head and the calyx has more veins, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Thymbra", "This branch points to Thymbra."),
        "no": ("Coridothymus", "This branch points to Coridothymus.")
    },
    "k35": {
        "question": "35. Are the flowers arranged in small spikes grouped into larger clusters, with overlapping bracts hiding the calyces?",
        "help": "This is a very oregano-like look.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Origanum", "This branch points to Origanum."),
        "no": "k36"
    },
    "k36": {
        "question": "36. Does the corolla have 4 almost equal lobes, and does the plant grow in damp places with creeping underground stems?",
        "help": "Underground spreading stems are rhizomes.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Mentha", "This branch points to Mentha."),
        "no": "k37"
    },
    "k37": {
        "question": "37. Are the leaves egg-shaped to almost round, and is the flower upside down?",
        "help": "If the leaves are much narrower and the flower is not upside down, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Cyclotrichium", "This branch points to Cyclotrichium."),
        "no": "k38"
    },
    "k38": {
        "question": "38. Is the calyx tubular, about 6 to 8 mm long, with thickened folds at the base of the notches, and are the flowers violet-blue?",
        "help": "If the calyx is smaller and more bell-shaped with white flowers, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Hyssopus", "This branch points to Hyssopus."),
        "no": ("Satureja", "This branch points to Satureja.")
    },
    "k39": {
        "question": "39. Does the throat of the calyx have a beard of thick stiff white hairs?",
        "help": "Look into the inside of the calyx opening.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k40",
        "no": "k52"
    },
    "k40": {
        "question": "40. Does the flower have 4 nearly equal lobes, and does the plant grow in damp places with rhizomes?",
        "help": "This points to the mint group if Yes.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Mentha", "This branch points to Mentha."),
        "no": "k41"
    },
    "k41": {
        "question": "41. Is the calyx flattened on the back and does it have two side flanges?",
        "help": "These side ridges are important here.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k42",
        "no": "k43"
    },
    "k42": {
        "question": "42. Is the inflorescence spike-like, with a 13-veined calyx and folded leaves?",
        "help": "If instead the flowers are in a head and the calyx has more veins, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Thymbra", "This branch points to Thymbra."),
        "no": ("Coridothymus", "This branch points to Coridothymus.")
    },
    "k43": {
        "question": "43. Are the flowers in small spikes grouped into larger clusters, with large bracts hiding the calyces?",
        "help": "This is again the oregano-like branch.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Origanum", "This branch points to Origanum."),
        "no": "k44"
    },
    "k44": {
        "question": "44. Are all parts of the plant covered with long sturdy hairs?",
        "help": "If the hairs are short, crisp, or the plant is less hairy, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k45",
        "no": "k46"
    },
    "k45": {
        "question": "45. Are the stamens inside the corolla tube, and is the calyx not widened above?",
        "help": "This separates Marrubium and Ballota again.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Marrubium", "This branch points to Marrubium."),
        "no": ("Ballota", "This branch points to Ballota.")
    },
    "k46": {
        "question": "46. Are the lower calyx teeth long, narrow, and clearly fringed with hairs, and are the leaves usually hairy at the base edge?",
        "help": "Hairy-edged means ciliate.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Thymus", "This branch points to Thymus."),
        "no": "k47"
    },
    "k47": {
        "question": "47. Is the calyx tube strongly curved or swollen below?",
        "help": "If it is mostly straight, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k48",
        "no": "k49"
    },
    "k48": {
        "question": "48. Is the calyx tube strongly curved, with long hairy teeth, and is the plant perennial?",
        "help": "If instead it is swollen below and narrowed above, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Clinopodium", "This branch points to Clinopodium."),
        "no": ("Acinos", "This branch points to Acinos.")
    },
    "k49": {
        "question": "49. Are the teeth of the lower calyx lip clearly hairy on the edges, and are the leaves stalked?",
        "help": "This helps separate Calamintha from the next group.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Calamintha", "This branch points to Calamintha."),
        "no": "k50"
    },
    "k50": {
        "question": "50. Are the leaves almost stalkless, wedge-based, folded when young, and do the stamens spread apart?",
        "help": "If leaves are stalked and flatter, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Satureja", "This branch points to Satureja."),
        "no": "k51"
    },
    "k51": {
        "question": "51. Is the calyx small, usually 13-veined, with the corolla tube staying inside, and are the flower clusters often cymose?",
        "help": "If the calyx is larger and the corolla tube sticks out, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Micromeria", "This branch points to Micromeria."),
        "no": ("Stachys", "This branch points to Stachys.")
    },
    "k52": {
        "question": "52. Are the bracteoles narrow and spine-like, bent backward, and does the upper lip of the calyx have one strong spine?",
        "help": "A very spiny-looking flower cluster points here.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Molucella", "This branch points to Molucella."),
        "no": "k53"
    },
    "k53": {
        "question": "53. Is the calyx clearly two-lipped?",
        "help": "This takes you to a leafy-bracted versus regular-calyx branch.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k54",
        "no": "k58"
    },
    "k54": {
        "question": "54. Is it a smooth shrub with terminal leafy flower clusters and fleshy black fruit?",
        "help": "This is a very distinct combination.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Prasium", "This branch points to Prasium."),
        "no": "k55"
    },
    "k55": {
        "question": "55. Are the flowers in the axils of upper leaves?",
        "help": "If the flowers are instead in the axils of bracts that do not look like normal leaves, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k56",
        "no": "k57"
    },
    "k56": {
        "question": "56. Are the flowers large, around 35 mm long, with stalks around 6 to 8 mm?",
        "help": "If the flowers are much smaller, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Melittis", "This branch points to Melittis."),
        "no": ("Melissa", "This branch points to Melissa.")
    },
    "k57": {
        "question": "57. Are the leaves almost stalkless, wedge-based, folded when young, dotted with glands, and is the calyx 10 to 13-veined?",
        "help": "If leaves are more often stalked and flatter, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Satureja", "This branch points to Satureja."),
        "no": ("Stachys", "This branch points to Stachys.")
    },
    "k58": {
        "question": "58. Are the bracts leafy and wrapping around the calyces, and are the flowers usually yellow?",
        "help": "If the bracts are not leafy and not wrapping around the calyces, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Sideritis", "This branch points to Sideritis."),
        "no": "k59"
    },
    "k59": {
        "question": "59. Is the calyx tubular with 5 strong angled ridges, and is the throat more or less closed in fruit?",
        "help": "This is a special calyx shape.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Pentapleura", "This branch points to Pentapleura."),
        "no": "k60"
    },
    "k60": {
        "question": "60. Are the leaves rather thick or hard, often clearly dotted with glands?",
        "help": "If the leaves are more herb-like and flatter, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": "k61",
        "no": "k62"
    },
    "k61": {
        "question": "61. Are the leaves almost stalkless and folded when young, with a 10 to 13-veined calyx?",
        "help": "If the leaves are stalked and flatter or have rolled edges, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Satureja", "This branch points to Satureja."),
        "no": ("Micromeria", "This branch points to Micromeria.")
    },
    "k62": {
        "question": "62. Is the calyx tube widened above, with many spreading teeth, and is the upper lip of the corolla rather hairy?",
        "help": "If the calyx is not widened above, choose No.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Ballota", "This branch points to Ballota."),
        "no": "k63"
    },
    "k63": {
        "question": "63. Are the pollen sacs hairy, and are the nutlets flat-ended and sharply three-angled?",
        "help": "If not, the pollen sacs are smooth and nutlets more rounded.",
        "yes_text": "Yes",
        "no_text": "No",
        "yes": ("Lamium", "This branch points to Lamium."),
        "no": ("Stachys", "This branch points to Stachys.")
    }
}

# =========================================================
# APP
# =========================================================

class KeyApp(ui.View):
    def __init__(self):
        self.name = 'Mint Family Key'
        self.background_color = 'white'
        self.history = []
        self.current_step = "start"
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.project_dir, 'images')
        self.make_ui()
        self.show_step("start")

    def make_ui(self):
        # Title
        self.title_label = ui.Label(frame=(10, 10, self.width - 20, 30), flex='W')
        self.title_label.text = "Labiatae / Mint Family Key"
        self.title_label.font = ('<System-Bold>', 22)
        self.add_subview(self.title_label)

        # Question area
        self.question_view = ui.TextView(frame=(10, 50, self.width - 20, 170), flex='WH')
        self.question_view.editable = False
        self.question_view.font = ('<System>', 18)
        self.question_view.text_color = 'black'
        self.question_view.background_color = (0.96, 0.98, 1.0)
        self.question_view.corner_radius = 8
        self.add_subview(self.question_view)

        # Image view
        self.image_view = ui.ImageView(frame=(10, 230, self.width - 20, 180), flex='W')
        self.image_view.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
        self.image_view.background_color = (0.95, 0.95, 0.95)
        self.image_view.border_width = 1
        self.image_view.border_color = '#cccccc'
        self.image_view.corner_radius = 8
        self.add_subview(self.image_view)

        # Result / status
        self.status_label = ui.Label(frame=(10, 420, self.width - 20, 55), flex='W')
        self.status_label.number_of_lines = 0
        self.status_label.font = ('<System>', 16)
        self.status_label.text_color = '#333333'
        self.add_subview(self.status_label)

        # Buttons
        self.yes_button = ui.Button(frame=(10, 485, self.width - 20, 50), flex='W')
        self.yes_button.background_color = '#d9f2d9'
        self.yes_button.tint_color = 'black'
        self.yes_button.corner_radius = 8
        self.yes_button.font = ('<System-Bold>', 18)
        self.yes_button.action = self.tap_yes
        self.add_subview(self.yes_button)

        self.no_button = ui.Button(frame=(10, 545, self.width - 20, 50), flex='W')
        self.no_button.background_color = '#f7e1c3'
        self.no_button.tint_color = 'black'
        self.no_button.corner_radius = 8
        self.no_button.font = ('<System-Bold>', 18)
        self.no_button.action = self.tap_no
        self.add_subview(self.no_button)

        self.back_button = ui.Button(frame=(10, 605, 90, 44), flex='T')
        self.back_button.title = 'Back'
        self.back_button.background_color = '#dddddd'
        self.back_button.tint_color = 'black'
        self.back_button.corner_radius = 8
        self.back_button.action = self.tap_back
        self.add_subview(self.back_button)

        self.home_button = ui.Button(frame=(110, 605, 90, 44), flex='T')
        self.home_button.title = 'Home'
        self.home_button.background_color = '#dddddd'
        self.home_button.tint_color = 'black'
        self.home_button.corner_radius = 8
        self.home_button.action = self.tap_home
        self.add_subview(self.home_button)

        self.gloss_button = ui.Button(frame=(210, 605, 110, 44), flex='T')
        self.gloss_button.title = 'Glossary'
        self.gloss_button.background_color = '#d8ebff'
        self.gloss_button.tint_color = 'black'
        self.gloss_button.corner_radius = 8
        self.gloss_button.action = self.show_glossary_dialog
        self.add_subview(self.gloss_button)

        self.term_button = ui.Button(frame=(330, 605, 110, 44), flex='T')
        self.term_button.title = 'Find Term'
        self.term_button.background_color = '#e7ddff'
        self.term_button.tint_color = 'black'
        self.term_button.corner_radius = 8
        self.term_button.action = self.find_term_dialog
        self.add_subview(self.term_button)

    def layout(self):
        w = self.width
        self.title_label.frame = (10, 10, w - 20, 30)
        self.question_view.frame = (10, 50, w - 20, 170)
        self.image_view.frame = (10, 230, w - 20, 180)
        self.status_label.frame = (10, 420, w - 20, 55)
        self.yes_button.frame = (10, 485, w - 20, 50)
        self.no_button.frame = (10, 545, w - 20, 50)
        self.back_button.frame = (10, 605, 90, 44)
        self.home_button.frame = (110, 605, 90, 44)
        self.gloss_button.frame = (210, 605, 110, 44)
        self.term_button.frame = (330, 605, 110, 44)

    def load_image(self, genus_name):
        filename = GENUS_IMAGES.get(genus_name)
        if not filename:
            self.image_view.image = None
            return

        path = os.path.join(self.images_dir, filename)
        if not os.path.exists(path):
            self.image_view.image = None
            return

        try:
            with open(path, 'rb') as f:
                data = f.read()
            self.image_view.image = ui.Image.from_data(data)
        except Exception:
            self.image_view.image = None

    def show_step(self, step_id):
        self.current_step = step_id
        step = KEY[step_id]

        text = step["question"] + "\n\n" + "Help: " + step["help"]
        self.question_view.text = text
        self.yes_button.title = step["yes_text"]
        self.no_button.title = step["no_text"]
        self.status_label.text = "Tap the answer that fits best."
        self.image_view.image = None

        self.yes_button.hidden = False
        self.no_button.hidden = False

    def show_result(self, genus_name, note):
        self.question_view.text = (
            "Best match:\n\n"
            + genus_name
            + "\n\n"
            + note
            + "\n\n"
            + "This is the most likely genus from these Flora of Turkey key pages. "
            + "After this, use a species key for that genus."
        )
        self.status_label.text = "You can tap Back to review your choices, or Home to restart."
        self.yes_button.hidden = True
        self.no_button.hidden = True
        self.load_image(genus_name)

    def go_to_target(self, target):
        if isinstance(target, tuple):
            genus_name, note = target
            self.show_result(genus_name, note)
        else:
            self.show_step(target)

    def tap_yes(self, sender):
        step = KEY[self.current_step]
        self.history.append(self.current_step)
        self.go_to_target(step["yes"])

    def tap_no(self, sender):
        step = KEY[self.current_step]
        self.history.append(self.current_step)
        self.go_to_target(step["no"])

    def tap_back(self, sender):
        if not self.history:
            self.status_label.text = "Already at the start."
            return
        previous = self.history.pop()
        self.show_step(previous)

    def tap_home(self, sender):
        self.history = []
        self.show_step("start")

    def show_glossary_dialog(self, sender):
        items = sorted(GLOSSARY.keys())
        dialog = GlossaryListView(items, self)
        dialog.present('sheet')

    def find_term_dialog(self, sender):
        dialog = ui.AlertController(
            title='Find Term',
            message='Type a glossary word exactly, such as calyx, corolla, verticillaster, or nutlet.',
            preferred_style='alert'
        )
        dialog.add_text_field()
        dialog.add_action(ui.AlertAction('Cancel'))
        def show_term(action):
            try:
                term = dialog.text_fields()[0].text.strip().lower()
            except Exception:
                term = ''
            meaning = GLOSSARY.get(term, 'That word is not in the glossary.')
            ui.alert(term if term else 'No term entered', meaning, 'OK', hide_cancel_button=True)
        dialog.add_action(ui.AlertAction('Show', handler=show_term))
        dialog.present()

class GlossaryListView(ui.View):
    def __init__(self, items, app):
        self.app = app
        self.name = 'Glossary'
        self.background_color = 'white'

        self.data = items

        self.table = ui.TableView(frame=self.bounds, flex='WH')
        self.table.data_source = self
        self.table.delegate = self
        self.add_subview(self.table)

    def tableview_number_of_rows(self, tableview, section):
        return len(self.data)

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell('subtitle')
        word = self.data[row]
        cell.text_label.text = word
        cell.detail_text_label.text = GLOSSARY[word]
        cell.detail_text_label.number_of_lines = 2
        return cell

    def tableview_did_select(self, tableview, section, row):
        word = self.data[row]
        ui.alert(word, GLOSSARY[word], 'OK', hide_cancel_button=True)

# =========================================================
# RUN APP
# if __name__ == '__main__':
    app = KeyApp()
    app.present('fullscreen')
    
