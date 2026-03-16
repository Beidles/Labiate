#!/usr/bin/env python3
# coding: utf-8
"""
Labiatae (Mint Family) Genus Key for Turkey
Based on Flora of Turkey, Vol. 7 (P.H. Davis, 1982)
Written for Pythonista 3 on iPad.

This key identifies the GENUS of your plant.
Once you have the genus, use a separate species key.

Features:
  - Native iOS touch interface (big YES / NO buttons)
  - Add a photo from your camera roll to your identification
  - 25 Labiatae genera found in Turkey
  - Written so a 14-year-old can use it with no botanical background

HOW TO RUN IN PYTHONISTA 3:
  Open this file in Pythonista 3 and tap the Run button (▶).
  The app will appear as a full-screen view.
"""

import ui
import photos
import console
import math

# ──────────────────────────────────────────────────────────────
#  COLOUR PALETTE
# ──────────────────────────────────────────────────────────────
C_BG        = '#F5F5F0'   # off-white page background
C_HEADER    = '#2E7D32'   # dark green header bar
C_CARD      = '#FFFFFF'   # white card background
C_CARD2     = '#EAF4EA'   # light-green tinted card
C_YES       = '#2E7D32'   # YES button – green
C_NO        = '#C62828'   # NO button  – red
C_PHOTO     = '#1565C0'   # Add Photo  – blue
C_NEW       = '#E65100'   # New ID     – orange
C_FOUND     = '#1B5E20'   # "FOUND IT" banner – deep green
C_TITLE_TXT = '#FFFFFF'   # white text on coloured background
C_BODY_TXT  = '#212121'   # near-black body text
C_HINT_TXT  = '#5D4037'   # brownish hint text
C_STEP_TXT  = '#A5D6A7'   # pale-green step counter text


# ──────────────────────────────────────────────────────────────
#  THE KEY  (dictionary-based dichotomous key)
#
#  Each entry is either a QUESTION node:
#    { 'q': str, 'hint': str, 'yes': node_id, 'no': node_id }
#
#  or a RESULT node:
#    { 'latin': str, 'common': str, 'about': str,
#      'habitat': str, 'fun': str }
# ──────────────────────────────────────────────────────────────

KEY = {

    # ── start ──────────────────────────────────────────────────
    'start': {
        'q':    'Are the flowers ALMOST PERFECTLY REGULAR – all petals '
                'nearly equal in size, like a little star or equal-lobed '
                'tube – NOT clearly split into a top lip and a bottom lip?',
        'hint': 'Most mint-family flowers are clearly 2-lipped: a top lip '
                'arching upward and a lower lip spreading down. A few genera '
                '(Mentha = Mint, Lycopus, Origanum = Oregano) have tiny '
                'nearly-equal flowers. If you can clearly see separate top '
                'and bottom lips, answer NO.',
        'yes':  'q_regular_mint',
        'no':   'q_upper_lip_absent',
    },

    # ── regular flower branch ──────────────────────────────────
    'q_regular_mint': {
        'q':    'Does the plant smell strongly of MINT when you crush '
                'a leaf between your fingers?',
        'hint': 'Mint (Mentha) has an unmistakable cool, fresh, sharp '
                'mint smell – very strong when you crush a leaf. Other '
                'regular-flowered Labiatae (Lycopus, Origanum) have little '
                'or no mint smell.',
        'yes':  'r_mentha',
        'no':   'q_regular_origanum',
    },

    'q_regular_origanum': {
        'q':    'Are the flowers in DENSE ROUNDED CLUSTERS at the branch '
                'tips, surrounded by PURPLE, PINK, or REDDISH BRACTS '
                '(small leaf-like things) that give the whole flowerhead '
                'a distinctly colourful look?',
        'hint': 'Origanum (Oregano / Marjoram) has small clusters of '
                'tiny flowers, each cluster wrapped in noticeable purple '
                'or pink bracts. Lycopus has simple rings of tiny white '
                'flowers around the stem, with no coloured bracts.',
        'yes':  'r_origanum',
        'no':   'r_lycopus',
    },

    # ── upper lip absent branch ────────────────────────────────
    'q_upper_lip_absent': {
        'q':    'Is the UPPER LIP of the flower COMPLETELY ABSENT or so '
                'tiny it almost disappears – so the flower looks as if it '
                'only has a BOTTOM LIP (all the petals seem to point '
                'downward or forward)?',
        'hint': 'Look at a flower from the front. In Ajuga (Bugle) and '
                'Teucrium (Germander) there is almost no top lip – just '
                'a tiny notch at the top and all the petal lobes point '
                'downward. In all other genera there is a clear top lip.',
        'yes':  'q_ajuga_teucrium',
        'no':   'q_calyx_bump',
    },

    'q_ajuga_teucrium': {
        'q':    'Is the plant LOW and CREEPING – spreading along the '
                'ground – with BLUE or BLUE-PURPLE flowers and broad, '
                'slightly wrinkled leaves (sometimes bronze or dark-coloured)?',
        'hint': 'Ajuga (Bugle) creeps along the ground by runners and '
                'produces short upright spikes of vivid blue flowers. '
                'Teucrium (Germander) is more upright, often woody or '
                'shrubby, with pink, white, cream, or pale purple flowers.',
        'yes':  'r_ajuga',
        'no':   'r_teucrium',
    },

    # ── calyx bump – Scutellaria ───────────────────────────────
    'q_calyx_bump': {
        'q':    'Does the CALYX (the green cup below the flower) have a '
                'SMALL ROUNDED BUMP, SCALE, or HELMET-LIKE RIDGE on its '
                'UPPER SURFACE – like a tiny lid or blister sitting on '
                'top of the calyx tube?',
        'hint': 'This tiny round scale on top of the calyx is unique to '
                'Scutellaria (Skullcap). Look at the side of a calyx – '
                'you should see a small rounded bump on the upper side. '
                'No other Turkish Labiatae has this feature.',
        'yes':  'r_scutellaria',
        'no':   'q_stamen_count',
    },

    # ── stamen count ───────────────────────────────────────────
    'q_stamen_count': {
        'q':    'Are there only 2 STAMENS (the pollen-making stalks with '
                'yellow or brown tips) inside the flower? Most Labiatae '
                'have 4 – look carefully inside a fresh open flower.',
        'hint': 'Salvia (Sage) and Rosmarinus (Rosemary) are the main '
                'genera with only 2 stamens. Open a fresh flower and count '
                'the stalks with dusty yellow pollen on their tips. If '
                'you count 4, answer NO.',
        'yes':  'q_salvia_rosmarinus',
        'no':   'q_upper_lip_hood',
    },

    'q_salvia_rosmarinus': {
        'q':    'Does the plant have VERY NARROW, NEEDLE-LIKE LEAVES '
                '(thin like pine needles, not flat and oval) and smell '
                'powerfully of ROSEMARY – the woody aromatic cooking herb?',
        'hint': 'Rosmarinus (Rosemary) has very narrow grey-green needle '
                'leaves and a strong distinctive piney-rosemary scent – '
                'you will recognise it instantly if you have ever smelled '
                'fresh rosemary. Salvia (Sage) has much broader, often '
                'wrinkled, soft or felty leaves.',
        'yes':  'r_rosmarinus',
        'no':   'r_salvia',
    },

    # ── upper lip shape ────────────────────────────────────────
    'q_upper_lip_hood': {
        'q':    'Is the UPPER LIP of the flower clearly HOODED or '
                'HELMET-SHAPED – curving upward into a rounded dome that '
                'arches over the centre of the flower, like a little roof '
                'protecting the stamens underneath?',
        'hint': 'A hooded upper lip curves upward and over the flower '
                'centre, making a rounded arch. Many genera have this '
                '(Lamium, Stachys, Phlomis, Marrubium, Ballota, Prunella). '
                'If the upper lip is more or less FLAT or only gently '
                'curved – not clearly arching into a dome – answer NO.',
        'yes':  'q_very_woolly',
        'no':   'q_flat_lip_branch',
    },

    # ── very woolly check ──────────────────────────────────────
    'q_very_woolly': {
        'q':    'Is the WHOLE PLANT very densely covered in THICK WOOLLY '
                'or MATTED WHITE HAIR – stems, leaves, and calyx all coated '
                'in a heavy white-grey felt, making the plant look silvery-'
                'white and fluffy all over?',
        'hint': 'Marrubium, Ballota, and Moluccella are extremely hairy – '
                'like a plant coated in thick cotton wool or sheep fleece. '
                'This is much more than ordinary hairiness. If the plant '
                'is just moderately hairy or fuzzy but not thickly felted '
                'all over, answer NO.',
        'yes':  'q_calyx_funnel',
        'no':   'q_phlomis_check',
    },

    # ── woolly branch ──────────────────────────────────────────
    'q_calyx_funnel': {
        'q':    'Does each CALYX (the cup holding each flower) look like '
                'a large FUNNEL or BELL – flared wide at the top and much '
                'bigger than the small flower sitting inside it, like a '
                'shell or ear-trumpet?',
        'hint': 'Moluccella laevis (Shell Flower / Bells of Ireland) is '
                'completely unmistakeable: the calyx is a huge green funnel '
                'with a tiny flower inside. Nothing else in Turkish Labiatae '
                'looks like this. If the calyx is a normal small cup, '
                'answer NO.',
        'yes':  'r_moluccella',
        'no':   'q_calyx_teeth_hooked',
    },

    'q_calyx_teeth_hooked': {
        'q':    'Are the tips of the CALYX TEETH (the pointed tips at the '
                'top edge of the calyx) HOOKED BACKWARDS like tiny fish-'
                'hooks or curved spines?',
        'hint': 'Marrubium (Horehound) has distinctive hooked calyx teeth '
                'that catch on clothing like Velcro – and the plant smells '
                'pleasantly aromatic. Ballota (Black Horehound) has '
                'spreading star-like teeth that are NOT hooked, and the '
                'plant has an unpleasant smell when crushed.',
        'yes':  'r_marrubium',
        'no':   'r_ballota',
    },

    # ── phlomis check ──────────────────────────────────────────
    'q_phlomis_check': {
        'q':    'Do the FLOWERS grow in dense GLOBE-SHAPED WHORLS (rings) '
                'around the stem, with each whorl having LARGE, BROAD, '
                'LEAF-LIKE BRACTS below it – almost as big as the regular '
                'stem leaves?',
        'hint': 'Phlomis and Phlomoides (Jerusalem Sage group) are large '
                'robust plants with big felty leaves and distinctive globe '
                'whorls of flowers. The bracts at each whorl are big and '
                'conspicuous. Flowers are yellow or pink. If the bracts '
                'are small and inconspicuous, answer NO.',
        'yes':  'r_phlomis',
        'no':   'q_dense_head',
    },

    # ── dense terminal head ────────────────────────────────────
    'q_dense_head': {
        'q':    'Are all the flowers packed into a SINGLE DENSE OVAL or '
                'OBLONG HEAD at the very TOP of the stem – like a compact '
                'fat egg-shaped cluster – rather than in separate rings '
                'spaced up the stem?',
        'hint': 'Prunella (Self-heal) is a small plant (10–30 cm) of '
                'meadows and roadsides with a very distinctive dense stubby '
                'head of violet-purple flowers at the top. Each whorl has '
                'two large bracts below it. If flowers are in separate '
                'rings spaced up the stem, answer NO.',
        'yes':  'r_prunella',
        'no':   'q_heart_leaves',
    },

    # ── heart leaves ───────────────────────────────────────────
    'q_heart_leaves': {
        'q':    'Are the LEAVES clearly HEART-SHAPED at the base – where '
                'the leaf stalk meets the leaf, the leaf spreads into two '
                'rounded lobes making a heart or kidney outline?',
        'hint': 'Heart-shaped (cordate) leaves have two rounded lobes at '
                'the base, like a Valentine heart. This is very obvious on '
                'Lamium (dead-nettle) and Galeopsis (hemp-nettle). Stachys '
                'leaves are usually more oblong or oval without the heart '
                'shape at the base.',
        'yes':  'q_hollow_stem',
        'no':   'q_stachys_group',
    },

    # ── hollow stem ────────────────────────────────────────────
    'q_hollow_stem': {
        'q':    'Do the STEMS feel HOLLOW when you squeeze them gently '
                'between your fingers – you can feel a gap or empty space '
                'inside the stem?',
        'hint': 'Galeopsis (Hemp-nettle) has distinctly hollow stems – '
                'you can feel the hollow space inside when you squeeze '
                'gently. Lamium (Dead-nettle) has solid stems. Galeopsis '
                'stems are also often swollen at the joints (nodes) and '
                'covered in stiff bristly hairs.',
        'yes':  'r_galeopsis',
        'no':   'r_lamium',
    },

    # ── stachys / sideritis group ──────────────────────────────
    'q_stachys_group': {
        'q':    'Do the BRACTS below each whorl of flowers end in a SHARP '
                'SPINE or STIFF PRICKLY POINT that feels sharp when you '
                'run your finger along it?',
        'hint': 'Sideritis (Ironwort) typically has bracts with sharp '
                'spiny tips. Stachys (Woundwort) has normal pointed bracts '
                'but they are not prickly or spine-tipped. Run your finger '
                'along a bract – if it pricks you, answer YES.',
        'yes':  'r_sideritis',
        'no':   'q_leonurus_stachys',
    },

    'q_leonurus_stachys': {
        'q':    'Are the LEAVES deeply LOBED or DIVIDED – cut into '
                'separate finger-like segments – rather than simply '
                'toothed around the edge?',
        'hint': 'Leonurus (Motherwort) has leaves that are clearly cut '
                'into lobes or separate pointed segments, like a hand '
                'with spread fingers. Stachys (Woundwort) has simple oval '
                'or oblong leaves with teeth but NOT lobed into separate '
                'finger-like parts.',
        'yes':  'r_leonurus',
        'no':   'r_stachys',
    },

    # ── flat lip branch ────────────────────────────────────────
    'q_flat_lip_branch': {
        'q':    'Is the plant VERY SMALL and LOW – under about 20 cm '
                'tall – with TINY LEAVES less than 1 cm long and a STRONG '
                'AROMATIC smell (like thyme, savory, or a sharp herby scent)?',
        'hint': 'Thymus (Thyme), Satureja (Savory), Micromeria, Acinos, '
                'and Ziziphora are all small low-growing aromatic herbs '
                'with tiny leaves. Larger herbs with bigger leaves are '
                'more likely Nepeta, Hyssopus, Dracocephalum, or others.',
        'yes':  'q_thymus_creep',
        'no':   'q_larger_flat',
    },

    # ── thyme group ────────────────────────────────────────────
    'q_thymus_creep': {
        'q':    'Does the plant CREEP along the ground or spread out as '
                'a low flat mat or cushion, with stems that lie flat and '
                'may root where they touch the soil?',
        'hint': 'Thymus (Thyme) typically forms low creeping mats or '
                'cushions, spreading outward close to the ground. Satureja '
                '(Savory), Micromeria, Acinos, and Ziziphora are more '
                'upright little shrubs or herbs, not mat-forming.',
        'yes':  'r_thymus',
        'no':   'r_satureja',
    },

    # ── larger flat-lipped plants ─────────────────────────────
    'q_larger_flat': {
        'q':    'Does the plant smell of CATS or CATNIP when you crush '
                'a leaf – a distinctive musty-minty smell that many cats '
                'are attracted to?',
        'hint': 'Nepeta (Catmint) has a very distinctive musky-minty smell '
                'that many cats find irresistible. Plants are usually grey-'
                'hairy with blue-violet flowers. This smell is quite '
                'different from ordinary mint – it has a musky quality.',
        'yes':  'r_nepeta',
        'no':   'q_lavender_hyssop',
    },

    # ── lavender / hyssop ──────────────────────────────────────
    'q_lavender_hyssop': {
        'q':    'Are the flowers in a LONG NARROW SPIKE at the top of '
                'the stem, with BLUE or BLUE-VIOLET flowers, and is the '
                'plant strongly aromatic with NARROW LEAVES?',
        'hint': 'Lavandula (Lavender) and Hyssopus (Hyssop) both have '
                'narrow-leaved stems topped with blue-purple flower spikes. '
                'Lavender has its flowers on long bare stems, most leaves '
                'low on the plant. Hyssop has leaves more evenly up the '
                'flowering stem.',
        'yes':  'q_lavender_hyssop2',
        'no':   'q_dracocephalum',
    },

    'q_lavender_hyssop2': {
        'q':    'Does the FLOWER SPIKE sit on a LONG BARE or NEARLY '
                'LEAFLESS STEM – with most leaves clustered low on the '
                'plant or at the base, not evenly distributed up the '
                'flowering stem?',
        'hint': 'Lavandula (Lavender) has long bare stems topped by the '
                'flower spike – the leaves are mostly at the base or '
                'low on the plant. Hyssopus (Hyssop) has leaves more '
                'evenly distributed right up to the flowers.',
        'yes':  'r_lavandula',
        'no':   'r_hyssopus',
    },

    # ── dracocephalum ──────────────────────────────────────────
    'q_dracocephalum': {
        'q':    'Are the FLOWERS LARGE – more than 2 cm long – and BLUE '
                'or VIOLET, in whorls, with BRACTS below each whorl that '
                'have TOOTHED or SPINE-TIPPED edges?',
        'hint': 'Dracocephalum (Dragonhead) has large showy blue-violet '
                'flowers – noticeably bigger than those of Nepeta or Salvia. '
                'The bracts have toothed or spiny edges. Clinopodium and '
                'Calamintha have smaller flowers and simpler bracts.',
        'yes':  'r_dracocephalum',
        'no':   'r_clinopodium',
    },

    # ──────────────────────────────────────────────────────────
    #  RESULT NODES
    # ──────────────────────────────────────────────────────────

    'r_mentha': {
        'latin':   'Mentha spp.',
        'common':  'Mint',
        'about':   'Mints are aromatic herbs with opposite leaves and '
                   'small tubular flowers in dense rings around the stem '
                   'or in a terminal spike. The flowers have four nearly '
                   'equal lobes – not clearly 2-lipped. Leaves smell '
                   'powerfully of mint when crushed. Stems are square in '
                   'cross-section, like all Labiatae. Several species '
                   'grow in Turkey, including Spearmint and Watermint.',
        'habitat': 'Wet places: stream and river banks, pond margins, '
                   'wet meadows, ditches, and damp roadsides. Almost '
                   'always near moisture.',
        'fun':     'Mint has been used to flavour food and medicine for '
                   'thousands of years – ancient Greeks and Romans wore '
                   'crowns of mint at feasts! The cool tingling feeling '
                   'from mint comes from menthol, which tricks your '
                   'cold-sensing nerves into feeling coolness.',
    },

    'r_origanum': {
        'latin':   'Origanum spp.',
        'common':  'Oregano / Marjoram',
        'about':   'Oregano and Marjoram are strongly aromatic herbs '
                   'with small oval leaves. The flowers are tiny but '
                   'packed into rounded clusters, each cluster surrounded '
                   'by conspicuous coloured bracts (usually purple, pink, '
                   'or red-purple). This gives the flowerheads a distinctive '
                   'bushy colourful look. The familiar smell of pizza oregano.',
        'habitat': 'Dry rocky hillsides, scrub, garrigue, open forest '
                   'edges. Very common across Turkey, especially on sunny '
                   'rocky slopes and roadsides.',
        'fun':     'Oregano is one of the most important cooking herbs in '
                   'the world – it gives pizza and pasta sauce that '
                   'characteristic Italian smell. In Turkey, dried oregano '
                   '(kekik) is sold in every village market and is mixed '
                   'with olive oil to eat with bread.',
    },

    'r_lycopus': {
        'latin':   'Lycopus spp.',
        'common':  'Gipsywort',
        'about':   'Gipsywort is an upright or creeping plant of wet '
                   'places with small, deeply toothed leaves. The flowers '
                   'are very tiny, white or pale pink, and almost perfectly '
                   'regular. They grow in dense rings around the stem. '
                   'Lycopus has only 2 stamens and almost no scent – both '
                   'features that separate it from Mint.',
        'habitat': 'Wet places: stream banks, riverbanks, pond and lake '
                   'margins, wet ditches and marshy ground. Almost always '
                   'found very close to water.',
        'fun':     'The name Lycopus comes from Greek for wolf-foot – '
                   'the lobed leaf was thought to look like a wolf\'s paw '
                   'print! The plant was once called Gipsywort because '
                   'travellers allegedly used its black juice as a skin '
                   'dye to darken their complexion.',
    },

    'r_ajuga': {
        'latin':   'Ajuga spp.',
        'common':  'Bugle',
        'about':   'Bugle is a low creeping plant that spreads by runners '
                   '(like a strawberry plant). It produces short upright '
                   'spikes of vivid blue flowers. The upper lip is almost '
                   'completely absent – all the petals seem to be at the '
                   'bottom, making a one-lipped flower. The leaves are '
                   'usually broad, somewhat shiny, and sometimes bronze-'
                   'purple. Common in damp meadows and light woodland.',
        'habitat': 'Damp meadows, stream banks, light woodland, shaded '
                   'rocky places, and roadsides with moisture. Found '
                   'throughout Turkey at various altitudes.',
        'fun':     'Bugle spreads by sending out long creeping stems called '
                   'stolons – exactly like strawberry plants. Each stolon '
                   'can root and form a new plant, so one Bugle can '
                   'colonise a large area very quickly!',
    },

    'r_teucrium': {
        'latin':   'Teucrium spp.',
        'common':  'Germander',
        'about':   'Germanders are shrubby or herbaceous plants with pink, '
                   'white, cream, or pale purple flowers that have almost '
                   'no upper lip – all the petal lobes form the lower lip. '
                   'Turkey has over 20 Teucrium species, making it one of '
                   'the most important countries in the world for this genus. '
                   'To identify the species, use the separate Teucrium '
                   'Species Key.',
        'habitat': 'Dry rocky hillsides, old stone walls, scrub, open '
                   'woodland. Very widespread across Turkey.',
        'fun':     'The genus Teucrium was named after the legendary Trojan '
                   'king Teucer, who was said to have used these plants '
                   'as medicine. Turkey (once the land of Troy) is one '
                   'of the world centres for Teucrium diversity!',
    },

    'r_scutellaria': {
        'latin':   'Scutellaria spp.',
        'common':  'Skullcap',
        'about':   'Skullcaps are easily identified by the unique small '
                   'rounded bump or scale on top of the calyx – like a '
                   'tiny helmet or lid. This feature is unique in the whole '
                   'mint family. Flowers are blue-violet, pink, or white, '
                   'clearly 2-lipped. Plants are usually medium-sized herbs '
                   'with opposite toothed leaves. Several species grow '
                   'in Turkey.',
        'habitat': 'Damp meadows, stream banks, wet rocky places, light '
                   'woodland. Found throughout Turkey, especially near '
                   'water.',
        'fun':     'The name Scutellaria comes from the Latin for "little '
                   'dish" or "little shield" – exactly what the bump on '
                   'the calyx looks like! Some Scutellaria species have '
                   'been studied as possible natural medicines for anxiety '
                   'and sleep problems.',
    },

    'r_rosmarinus': {
        'latin':   'Salvia rosmarinus Schleid. (= Rosmarinus officinalis)',
        'common':  'Rosemary',
        'about':   'Rosemary is a woody aromatic shrub with very narrow '
                   'needle-like grey-green leaves and a powerful piney-'
                   'rosemary smell. Flowers are pale blue-violet with only '
                   '2 stamens. Botanists have recently moved Rosemary into '
                   'the Salvia genus because it is so closely related. '
                   'A familiar cooking and garden herb.',
        'habitat': 'Dry rocky hillsides, limestone cliffs, scrub, coastal '
                   'areas. Mainly in western and southern Turkey near '
                   'the Mediterranean coast.',
        'fun':     'Rosemary has been a symbol of remembrance and memory '
                   'for thousands of years – ancient Greeks wore it while '
                   'studying for exams, and it is still placed on graves '
                   'today. Scientists have found compounds in rosemary '
                   'that may genuinely improve memory slightly!',
    },

    'r_salvia': {
        'latin':   'Salvia spp.',
        'common':  'Sage',
        'about':   'Sage is one of the largest genera in the mint family, '
                   'with over 60 species in Turkey alone. Flowers are '
                   'typically blue-purple, pink, red, or white, with only '
                   '2 stamens inside – unusual for the mint family. The '
                   'stamens have a clever hinged mechanism that dusts '
                   'visiting bees with pollen. Leaves are often wrinkled '
                   'or felty.',
        'habitat': 'Very varied: dry rocky hillsides, scrub, woodland '
                   'edges, meadows, roadsides. Found throughout Turkey '
                   'at all altitudes.',
        'fun':     'Sage has one of the cleverest pollen-delivery systems '
                   'in the plant world. Each stamen has a hinged arm – '
                   'when a bee pushes in to reach nectar, the hinge tips '
                   'the stamen and drops pollen squarely on the bee\'s '
                   'back. The plant uses the bee like a living stamp!',
    },

    'r_moluccella': {
        'latin':   'Moluccella laevis L.',
        'common':  'Shell Flower / Bells of Ireland',
        'about':   'This is one of the most unmistakeable plants you will '
                   'ever see. Each tiny white flower sits inside an enormous '
                   'funnel-shaped calyx that looks like a scallop shell or '
                   'ear-trumpet – much bigger than the flower itself. The '
                   'plant has smooth green leaves and white flowers. Very '
                   'popular with florists because the shell-like calyces '
                   'dry beautifully.',
        'habitat': 'Disturbed ground, roadsides, field edges, rocky slopes. '
                   'Found mainly in southeastern Turkey and the Middle East.',
        'fun':     'The name "Bells of Ireland" is misleading – this plant '
                   'has nothing to do with Ireland! It comes from the '
                   'eastern Mediterranean and Middle East, and probably '
                   'reached florists in Ireland via the old spice trade '
                   'routes. It is quite common as a garden plant.',
    },

    'r_marrubium': {
        'latin':   'Marrubium spp.',
        'common':  'Horehound',
        'about':   'Horehound is a densely white-woolly plant with a '
                   'pleasant aromatic smell. The key feature is the HOOKED '
                   'CALYX TEETH – the pointed tips of the calyx are curved '
                   'backwards like fish-hooks that catch on clothing. '
                   'Flowers are white or pale cream in dense whorls up '
                   'the stem. Several species grow in Turkey.',
        'habitat': 'Dry rocky places, roadsides, disturbed ground, old '
                   'walls and village edges. Common across Turkey, '
                   'especially in dry areas.',
        'fun':     'Horehound has been used to make cough medicine and '
                   'throat lozenges for at least 2000 years – ancient '
                   'Romans used it for chest complaints. You can still '
                   'buy horehound cough drops and candy in health food '
                   'shops around the world today!',
    },

    'r_ballota': {
        'latin':   'Ballota spp.',
        'common':  'Black Horehound',
        'about':   'Very similar to Marrubium and also very densely white-'
                   'woolly, but the calyx teeth spread outward like a star '
                   'and are NOT hooked. Black Horehound has a strong, '
                   'unpleasant smell – quite different from the pleasant '
                   'smell of Horehound. Flowers are pink or white. The '
                   'name "black" refers to the unpleasant smell, not the '
                   'colour.',
        'habitat': 'Roadsides, disturbed ground, village edges, rocky '
                   'slopes. Very common in Turkey, especially near '
                   'human habitation.',
        'fun':     'Black Horehound smells so bad that sheep and goats '
                   'avoid eating it – which is probably why it grows well '
                   'near farmyards and roadsides where other plants get '
                   'grazed. The unpleasant smell is the plant\'s defence '
                   'against being eaten!',
    },

    'r_phlomis': {
        'latin':   'Phlomis / Phlomoides spp.',
        'common':  'Jerusalem Sage / Phlomis',
        'about':   'This group includes some of the most distinctive plants '
                   'of Turkey. They are large, robust herbs or shrubs with '
                   'BIG, often felty or woolly leaves. Flowers are packed '
                   'in globe-shaped whorls around the stem, each whorl '
                   'below large leafy bracts. Flowers are yellow, pink, '
                   'or purple with a hooded upper lip. Turkey has many '
                   'species, some found nowhere else on Earth.',
        'habitat': 'Rocky hillsides, scrub, open woodland, roadsides. '
                   'Found throughout Turkey at low to high altitudes.',
        'fun':     'Several Phlomis species are ENDEMIC to Turkey – they '
                   'grow ONLY in Turkey and absolutely nowhere else in '
                   'the world! Turkey has more Phlomis species than any '
                   'other country, making it a world centre for this '
                   'beautiful and distinctive genus.',
    },

    'r_prunella': {
        'latin':   'Prunella spp.',
        'common':  'Self-heal',
        'about':   'Self-heal is a small plant of grasslands and roadsides '
                   'with a very distinctive dense oblong head of violet-'
                   'purple (sometimes pink or white) flowers at the very '
                   'top of each stem. Below the flower head is usually a '
                   'pair of broad leaves. The plant is low and slightly '
                   'creeping. It was used for centuries as a wound-healing '
                   'herb – hence the name.',
        'habitat': 'Grasslands, meadows, lawns, roadsides, open woodland '
                   'and disturbed ground. Very widespread and common '
                   'throughout Turkey.',
        'fun':     'Self-heal was called "All-heal" and "Carpenter\'s herb" '
                   'in medieval Europe – it was used to stop bleeding and '
                   'heal wounds. Modern scientists have found it contains '
                   'compounds with real anti-inflammatory properties, '
                   'so the old herbalists were not completely wrong!',
    },

    'r_galeopsis': {
        'latin':   'Galeopsis spp.',
        'common':  'Hemp-nettle',
        'about':   'Hemp-nettles are annual herbs with distinctive HOLLOW '
                   'STEMS – you can feel the empty space inside when you '
                   'squeeze them. The stems are often swollen at the joints '
                   '(nodes) and covered in stiff bristly hairs. Flowers '
                   'are pink, purple, yellow-white, or variegated. The '
                   'lower lip often has a colourful pattern of spots.',
        'habitat': 'Disturbed ground, arable fields, roadsides, stream '
                   'banks, and woodland clearings. Found throughout Turkey.',
        'fun':     'The hollow stems of Hemp-nettle are very unusual in '
                   'the mint family – most Labiatae have solid stems. '
                   'Engineers know that a hollow tube is actually stronger '
                   'for its weight than a solid rod of the same material – '
                   'that is why bicycle frames and aircraft are made hollow!',
    },

    'r_lamium': {
        'latin':   'Lamium spp.',
        'common':  'Dead-nettle',
        'about':   'Dead-nettles look very like Stinging Nettles – same '
                   'leaf shape, same hairy feel – but they do NOT sting '
                   '(hence "dead" nettle). The flowers are clearly 2-lipped '
                   'with a hooded upper lip. Flowers are pink, purple, red, '
                   'white, or yellow. The base of each leaf is distinctly '
                   'heart-shaped. Common plants of hedgerows and roadsides.',
        'habitat': 'Hedgerows, roadsides, disturbed ground, gardens, '
                   'stream banks. Very widespread and common throughout '
                   'Turkey.',
        'fun':     'Dead-nettles are masters of deception – they look '
                   'exactly like Stinging Nettles to discourage animals '
                   'from eating them, but cannot sting at all. Scientists '
                   'call this Batesian mimicry: a harmless species copying '
                   'the appearance of a harmful one for protection!',
    },

    'r_sideritis': {
        'latin':   'Sideritis spp.',
        'common':  'Ironwort / Mountain Tea',
        'about':   'Ironworts are upright herbs or small shrubs, usually '
                   'hairy, with flowers in whorls. The most distinctive '
                   'feature is the SPINY BRACTS below each whorl. Flowers '
                   'are usually yellow or white-cream. In Turkey, Sideritis '
                   'is very important culturally – several species are used '
                   'to make "dag cayi" (mountain tea), drunk widely '
                   'throughout Turkey.',
        'habitat': 'Rocky hillsides, stony mountain slopes, dry scrub. '
                   'Found throughout Turkey, especially in mountains.',
        'fun':     '"Dag cayi" (Mountain Tea) made from dried Sideritis is '
                   'one of the most popular herbal drinks in Turkey – you '
                   'will find it on every cafe menu in the mountains. It '
                   'is traditionally said to help with colds and stomach '
                   'aches. Turkey is a world centre for Sideritis diversity.',
    },

    'r_leonurus': {
        'latin':   'Leonurus spp.',
        'common':  'Motherwort',
        'about':   'Motherwort is a tall upright plant with distinctive '
                   'deeply lobed leaves – the upper leaves especially are '
                   'cut into separate finger-like lobes, unlike the simple '
                   'toothed leaves of most mint-family plants. Flowers are '
                   'pink to pale purple with a hairy hooded upper lip. '
                   'Whorls of flowers are packed around the upper stem.',
        'habitat': 'Disturbed ground, roadsides, stream banks, hedgerows, '
                   'woodland edges. Scattered throughout Turkey.',
        'fun':     'The name Leonurus comes from Greek for lion\'s tail – '
                   'the flowering spike was thought to look like a lion\'s '
                   'tail! Motherwort has been used in traditional medicine '
                   'for heart conditions for centuries, and modern research '
                   'confirms it contains some heart-active compounds.',
    },

    'r_stachys': {
        'latin':   'Stachys / Betonica spp.',
        'common':  'Woundwort / Betony',
        'about':   'This is a large group of hairy plants with whorls of '
                   'pink, purple, red, or white flowers up the stem. The '
                   'leaves are oval to oblong with toothed edges – NOT '
                   'heart-shaped at the base and NOT lobed. Stems are '
                   'square and hairy. Turkey has many species, including '
                   'the famous Betony (Betonica officinalis).',
        'habitat': 'Hedgerows, woodland edges, meadows, rocky slopes, '
                   'disturbed ground. Found throughout Turkey at various '
                   'altitudes.',
        'fun':     'Betony (Stachys betonica) was considered the most '
                   'important medicinal herb in medieval Europe. There was '
                   'a Latin saying meaning "sell your coat and buy Betony". '
                   'The Romans claimed it cured over 40 different illnesses!',
    },

    'r_thymus': {
        'latin':   'Thymus spp.',
        'common':  'Thyme',
        'about':   'Thymes are low creeping or mat-forming dwarf shrubs '
                   'with tiny aromatic leaves (under 1 cm) and small '
                   'pinkish-purple flowers in short heads or whorls. '
                   'The strong thyme smell is immediately recognisable. '
                   'Turkey has over 60 Thyme species – more than almost '
                   'any other country in the world. The stems are woody '
                   'at the base and the plant creeps outward.',
        'habitat': 'Dry rocky slopes, limestone hillsides, dry grassland, '
                   'stony places. Very widespread across Turkey, '
                   'especially on sunny rocky slopes.',
        'fun':     'Turkey has more wild Thyme species than almost any '
                   'other country in the world! Ancient Greeks burned thyme '
                   'as incense in their temples – the word "thyme" may '
                   'come from the Greek word for sacrifice. Roman soldiers '
                   'bathed in thyme water before battles for courage.',
    },

    'r_satureja': {
        'latin':   'Satureja / Micromeria / Acinos / Ziziphora spp.',
        'common':  'Savory / Calamint group',
        'about':   'This is a group of small upright aromatic herbs and '
                   'dwarf shrubs that look like miniature thyme or savory. '
                   'They grow upright (not creeping like Thymus), with tiny '
                   'aromatic leaves and small pink, purple, or white flowers. '
                   'Turkey has many species: Summer Savory (used in cooking), '
                   'several Micromeria, Acinos (annual), and Ziziphora '
                   '(extremely aromatic, used for tea in eastern Turkey).',
        'habitat': 'Dry rocky slopes, stony ground, open scrub. Found '
                   'throughout Turkey, especially on rocky mountainsides.',
        'fun':     'Savory (Satureja) has been a cooking herb since ancient '
                   'Roman times – Romans called it the "herb of love". '
                   'Ziziphora is used in eastern Turkey and the Caucasus '
                   'to make a delicious and very aromatic herbal tea, '
                   'popular at every roadside chai stall.',
    },

    'r_nepeta': {
        'latin':   'Nepeta spp.',
        'common':  'Catmint / Catnip',
        'about':   'Catmints are usually grey-hairy plants with blue-violet '
                   'flowers and a distinctive musky-minty smell that many '
                   'cats find irresistible. Flowers are 2-lipped with a '
                   'less strongly hooded upper lip than Lamium or Stachys. '
                   'Turkey has many Nepeta species. Plants are popular in '
                   'ornamental gardens for their long-lasting flowers.',
        'habitat': 'Rocky hillsides, dry scrub, stony slopes, roadsides. '
                   'Found throughout Turkey, especially in drier regions.',
        'fun':     'Catnip (Nepeta cataria) causes about 70% of cats to '
                   'become very excited – rolling around and acting "drunk". '
                   'The active chemical is called nepetalactone. Interestingly, '
                   'it only affects domestic cats and some wild cats '
                   '(lions and leopards also respond!), not all animals.',
    },

    'r_lavandula': {
        'latin':   'Lavandula spp.',
        'common':  'Lavender',
        'about':   'Lavender is one of the most recognisable aromatic plants '
                   'in the world. The flowers are in a long narrow spike at '
                   'the top of a long, nearly leafless stem. Flowers are '
                   'blue-violet (rarely pink or white). The narrow grey-'
                   'green leaves are mostly at the base. The famous lavender '
                   'perfume smell. Turkey has a few native Lavender species '
                   'in the south and east.',
        'habitat': 'Dry rocky hillsides, limestone slopes, scrub, open '
                   'garrigue. Found mainly in southern and eastern Turkey.',
        'fun':     'Lavender gets its name from the Latin lavare (to wash) '
                   '– Romans added it to bathwater and laundry. The perfume '
                   'industry uses millions of tonnes of lavender oil every '
                   'year. Scientists have found that lavender scent '
                   'genuinely reduces anxiety slightly – your nose really '
                   'does affect your brain!',
    },

    'r_hyssopus': {
        'latin':   'Hyssopus officinalis L.',
        'common':  'Hyssop',
        'about':   'Hyssop is a small woody-based perennial with narrow '
                   'dark-green leaves and blue-violet (rarely pink or white) '
                   'flowers in whorls among the upper leaves. It smells '
                   'aromatic and slightly bitter. An ancient medicinal '
                   'and culinary herb mentioned in the Bible. The flowers '
                   'are set among leaves along the upper stem, not on a '
                   'bare stem like Lavender.',
        'habitat': 'Rocky hillsides, dry stony slopes, old walls, scrub. '
                   'Found in eastern Turkey and the Caucasus region, '
                   'often on limestone.',
        'fun':     'Hyssop is mentioned in the Bible as a herb used for '
                   'purification – it was used in ceremonies for thousands '
                   'of years. It is also used as a flavouring in Chartreuse, '
                   'the famous green herbal liqueur made by monks in France!',
    },

    'r_dracocephalum': {
        'latin':   'Dracocephalum spp.',
        'common':  'Dragonhead',
        'about':   'Dragonheads have large, showy blue-violet flowers '
                   '(more than 2 cm long) – noticeably bigger than most '
                   'other mint-family plants. The flowers sit in whorls '
                   'with distinctive bracts that have toothed or spiny-'
                   'tipped margins. The large open flower was thought to '
                   'look like a dragon\'s mouth – hence the name. Several '
                   'species grow in Turkey, especially in eastern regions.',
        'habitat': 'Mountain meadows, rocky slopes, stony hillsides, '
                   'especially at higher altitudes. Found mainly in '
                   'eastern and central Turkey.',
        'fun':     'Dracocephalum means dragon-head in Greek – the large '
                   'open flower was imagined to look like a dragon\'s '
                   'open mouth! These plants are very attractive to '
                   'bumblebees, which are often the only insects big '
                   'enough to push inside the large flowers to reach '
                   'the nectar.',
    },

    'r_clinopodium': {
        'latin':   'Clinopodium / Calamintha spp.',
        'common':  'Wild Basil / Calamint',
        'about':   'Wild Basil and Calamint are medium-sized aromatic '
                   'herbs with oval leaves and pink to purple flowers in '
                   'loose whorls. They look like a larger thyme or savory '
                   'but are not small and mat-forming. The flowers are '
                   'clearly 2-lipped. Several species grow in Turkey in '
                   'a range of habitats. They have a pleasant aromatic '
                   'smell when crushed.',
        'habitat': 'Woodland edges, scrub, hedgerows, rocky slopes, '
                   'grassland. Found throughout Turkey.',
        'fun':     'Wild Basil (Clinopodium vulgare) is distantly related '
                   'to the basil (Ocimum basilicum) used in Italian '
                   'cooking, but it smells quite different – more like '
                   'oregano or thyme. Despite the similar name, you would '
                   'not want to use it on your pizza in the same way!',
    },
}


# ──────────────────────────────────────────────────────────────
#  PYTHONISTA 3 APP
# ──────────────────────────────────────────────────────────────

PAD        = 12     # general padding
BPAD       = 16     # button area height padding
BTN_H      = 52     # button height
HEADER_H   = 64     # header bar height
BTN_AREA_H = BTN_H + BPAD * 2   # total height of the fixed button row


class LabiataeApp(ui.View):
    """Full-screen Pythonista 3 UI for the Labiatae genus key."""

    def __init__(self):
        self.history  = []        # list of node_ids for Back button
        self.node     = 'start'   # current node
        self.photo    = None      # ui.Image attached by user (result only)
        self.bg_color = C_BG

        self._mk_header()
        self._mk_scroll()
        self._mk_buttons()
        self._go('start')

    # ── layout helpers ─────────────────────────────────────────

    def _mk_header(self):
        """Dark green header bar with title, Back, and Restart buttons."""
        h = self
        W = h.width if h.width > 0 else 390

        bar = ui.View()
        bar.name     = 'header'
        bar.bg_color = C_HEADER
        bar.frame    = (0, 0, W, HEADER_H)
        bar.flex     = 'W'
        self.add_subview(bar)

        back = ui.Button()
        back.name       = 'back_btn'
        back.title      = '< Back'
        back.font       = ('<system-bold>', 15)
        back.tint_color = C_STEP_TXT
        back.frame      = (8, 14, 80, 36)
        back.action     = self._back
        bar.add_subview(back)

        title = ui.Label()
        title.name       = 'title_lbl'
        title.text       = 'LABIATAE KEY'
        title.font       = ('<system-bold>', 17)
        title.text_color = C_TITLE_TXT
        title.alignment  = ui.ALIGN_CENTER
        title.frame      = (90, 10, W - 180, 44)
        title.flex       = 'W'
        bar.add_subview(title)

        restart = ui.Button()
        restart.name       = 'restart_btn'
        restart.title      = 'Restart'
        restart.font       = ('<system-bold>', 15)
        restart.tint_color = C_STEP_TXT
        restart.frame      = (W - 90, 14, 82, 36)
        restart.flex       = 'L'
        restart.action     = self._restart
        bar.add_subview(restart)

        step_lbl = ui.Label()
        step_lbl.name       = 'step_lbl'
        step_lbl.text       = 'Step 1'
        step_lbl.font       = ('<system>', 13)
        step_lbl.text_color = '#888888'
        step_lbl.alignment  = ui.ALIGN_CENTER
        step_lbl.frame      = (0, HEADER_H, W, 22)
        step_lbl.flex       = 'W'
        self.add_subview(step_lbl)

    def _mk_scroll(self):
        """Scrollable content area between header and buttons."""
        W   = self.width  if self.width  > 0 else 390
        H   = self.height if self.height > 0 else 844
        top    = HEADER_H + 22
        bottom = BTN_AREA_H
        sv = ui.ScrollView()
        sv.name     = 'scroll'
        sv.frame    = (0, top, W, H - top - bottom)
        sv.flex     = 'WH'
        sv.bg_color = C_BG
        self.add_subview(sv)

    def _mk_buttons(self):
        """Fixed YES / NO / Add Photo / New ID buttons at the bottom."""
        W = self.width  if self.width  > 0 else 390
        H = self.height if self.height > 0 else 844

        panel = ui.View()
        panel.name     = 'btn_panel'
        panel.bg_color = '#E8E8E4'
        panel.frame    = (0, H - BTN_AREA_H, W, BTN_AREA_H)
        panel.flex     = 'WT'
        self.add_subview(panel)

        specs = [
            ('yes_btn',   'YES',     C_YES,   self._yes),
            ('no_btn',    'NO',      C_NO,    self._no),
            ('photo_btn', 'Photo',   C_PHOTO, self._pick_photo),
            ('new_btn',   'New ID',  C_NEW,   self._restart),
        ]
        n   = len(specs)
        gap = 8
        bw  = (W - gap * (n + 1)) / n
        for i, (name, title, colour, action) in enumerate(specs):
            btn = ui.Button()
            btn.name          = name
            btn.title         = title
            btn.bg_color      = colour
            btn.tint_color    = C_TITLE_TXT
            btn.font          = ('<system-bold>', 15)
            btn.frame         = (gap + i * (bw + gap), BPAD, bw, BTN_H)
            btn.corner_radius = 10
            btn.action        = action
            panel.add_subview(btn)

    # ── navigation ─────────────────────────────────────────────

    def _go(self, node_id):
        """Move to a node, rebuild the scroll content."""
        self.node = node_id
        nd = KEY[node_id]

        step_lbl = self['step_lbl']
        if step_lbl:
            if 'q' in nd:
                step_lbl.text = 'Step {}'.format(len(self.history) + 1)
            else:
                step_lbl.text = 'Result'

        is_result = 'latin' in nd
        for name in ('yes_btn', 'no_btn'):
            btn = self['yes_btn'] if name == 'yes_btn' else self['no_btn']
            if btn:
                btn.hidden = is_result
        photo_btn = self['photo_btn']
        if photo_btn:
            photo_btn.hidden = not is_result

        sv = self['scroll']
        if sv is None:
            return
        for sub in list(sv.subviews):
            sv.remove_subview(sub)

        W = sv.width if sv.width > 10 else 390
        y = PAD
        if is_result:
            y = self._render_result(nd, sv, W, y)
        else:
            y = self._render_question(nd, sv, W, y, len(self.history) == 0)

        sv.content_size = (W, y + PAD)

    # ── render helpers ─────────────────────────────────────────

    def _text_height(self, text, width, font_size=15, bold=False):
        """Estimate label height for multi-line text."""
        cpl   = max(1, int(width / (font_size * 0.55)))
        words = text.split()
        lines = 1
        cur   = 0
        for w in words:
            if cur + len(w) + 1 > cpl:
                lines += 1
                cur = len(w)
            else:
                cur += len(w) + 1
        return math.ceil(lines * font_size * 1.45) + 4

    def _card(self, sv, x, y, w, h, bg=C_CARD, radius=12):
        """Add a rounded card view to sv, return the view."""
        card = ui.View()
        card.bg_color      = bg
        card.corner_radius = radius
        card.frame         = (x, y, w, h)
        sv.add_subview(card)
        return card

    def _render_question(self, nd, sv, W, y, first):
        """Build the question card in sv. Returns next y."""
        p  = PAD
        cw = W - p * 2

        # ── intro card (first question only) ───────────────────
        if first:
            intro_text = (
                'This key helps you identify the GENUS of Labiatae '
                '(Mint Family) plants from Turkey.\n'
                'Based on Flora of Turkey Vol. 7 (P.H. Davis, 1982).\n\n'
                'The key identifies GENUS first. Once you know the genus '
                'you can use a species key for more detail.\n\n'
                'Just answer YES or NO to each question!\n\n'
                'Back = previous question\n'
                'Restart = start over\n'
                'Photo = attach a photo to your result'
            )
            ih   = self._text_height(intro_text, cw - p * 2, font_size=14) + p * 2
            card = self._card(sv, p, y, cw, ih, bg=C_CARD2)
            lbl  = ui.Label()
            lbl.text            = intro_text
            lbl.font            = ('<system>', 14)
            lbl.text_color      = '#1B5E20'
            lbl.number_of_lines = 0
            lbl.frame           = (p, p, cw - p * 2, ih - p * 2)
            card.add_subview(lbl)
            y += ih + p

        # ── question card ──────────────────────────────────────
        qtext = nd['q']
        qh    = self._text_height(qtext, cw - p * 2, font_size=16, bold=True)
        qcard = self._card(sv, p, y, cw, qh + p * 2 + 4, bg=C_CARD)

        qlbl = ui.Label()
        qlbl.text            = qtext
        qlbl.font            = ('<system-bold>', 16)
        qlbl.text_color      = '#0D47A1'
        qlbl.number_of_lines = 0
        qlbl.frame           = (p, p, cw - p * 2, qh)
        qcard.add_subview(qlbl)
        y += qh + p * 2 + 4 + p

        # ── hint card ──────────────────────────────────────────
        hint = nd.get('hint', '')
        if hint:
            hh    = self._text_height(hint, cw - p * 2, font_size=14)
            hcard = self._card(sv, p, y, cw, hh + p * 2, bg='#FFF8E1')
            hlbl  = ui.Label()
            hlbl.text            = 'Hint:  ' + hint
            hlbl.font            = ('<system>', 14)
            hlbl.text_color      = C_HINT_TXT
            hlbl.number_of_lines = 0
            hlbl.frame           = (p, p, cw - p * 2, hh)
            hcard.add_subview(hlbl)
            y += hh + p * 2 + p

        return y

    def _render_result(self, nd, sv, W, y):
        """Build the result display in sv. Returns next y."""
        p  = PAD
        cw = W - p * 2

        # ── FOUND IT banner ────────────────────────────────────
        banner = self._card(sv, p, y, cw, 52, bg=C_FOUND, radius=12)
        blbl = ui.Label()
        blbl.text       = 'FOUND IT!'
        blbl.font       = ('<system-bold>', 20)
        blbl.text_color = C_TITLE_TXT
        blbl.alignment  = ui.ALIGN_CENTER
        blbl.frame      = (0, 8, cw, 36)
        banner.add_subview(blbl)
        y += 52 + p

        # ── Latin name ─────────────────────────────────────────
        lh    = self._text_height(nd['latin'], cw - p * 2, font_size=18, bold=True) + 4
        lcard = self._card(sv, p, y, cw, lh + p * 2, bg=C_CARD2)
        llbl  = ui.Label()
        llbl.text            = nd['latin']
        llbl.font            = ('<system-bold>', 18)
        llbl.text_color      = C_FOUND
        llbl.number_of_lines = 0
        llbl.frame           = (p, p, cw - p * 2, lh)
        lcard.add_subview(llbl)
        y += lh + p * 2 + p

        # ── Common name ────────────────────────────────────────
        ch    = self._text_height(nd['common'], cw - p * 2, font_size=16) + 4
        ccard = self._card(sv, p, y, cw, ch + p * 2, bg=C_CARD)
        clbl  = ui.Label()
        clbl.text            = nd['common']
        clbl.font            = ('<system>', 16)
        clbl.text_color      = C_BODY_TXT
        clbl.number_of_lines = 0
        clbl.frame           = (p, p, cw - p * 2, ch)
        ccard.add_subview(clbl)
        y += ch + p * 2 + p

        # ── About / Habitat / Fun fact ─────────────────────────
        for icon, key, bg_col in [
            ('About:',    'about',   C_CARD),
            ('Habitat:',  'habitat', '#E3F2FD'),
            ('Fun fact:', 'fun',     '#FFF9C4'),
        ]:
            text = nd.get(key, '')
            if not text:
                continue
            full  = icon + '  ' + text
            th    = self._text_height(full, cw - p * 2, font_size=14) + 4
            tcard = self._card(sv, p, y, cw, th + p * 2, bg=bg_col)
            tlbl  = ui.Label()
            tlbl.text            = full
            tlbl.font            = ('<system>', 14)
            tlbl.text_color      = C_BODY_TXT
            tlbl.number_of_lines = 0
            tlbl.frame           = (p, p, cw - p * 2, th)
            tcard.add_subview(tlbl)
            y += th + p * 2 + p

        # ── Photo (if one was attached) ────────────────────────
        if self.photo is not None:
            img   = self.photo
            ratio = img.size[1] / img.size[0] if img.size[0] > 0 else 1
            ph    = min(int(cw * ratio), 340)

            pcard = self._card(sv, p, y, cw, ph + p * 2 + 24, bg=C_CARD)

            ptlbl = ui.Label()
            ptlbl.text       = 'Your Photo'
            ptlbl.font       = ('<system-bold>', 13)
            ptlbl.text_color = '#555555'
            ptlbl.frame      = (p, 6, cw - p * 2, 18)
            pcard.add_subview(ptlbl)

            iv = ui.ImageView()
            iv.image        = img
            iv.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
            iv.frame        = (p, p + 24, cw - p * 2, ph)
            pcard.add_subview(iv)
            y += ph + p * 2 + 24 + p

        # ── prompt to add a photo ──────────────────────────────
        else:
            ph_lbl = ui.Label()
            ph_lbl.text            = 'Tap "Photo" below to attach a photo of your plant'
            ph_lbl.font            = ('<system>', 13)
            ph_lbl.text_color      = '#888888'
            ph_lbl.alignment       = ui.ALIGN_CENTER
            ph_lbl.number_of_lines = 0
            ph_lbl.frame           = (p, y, cw, 36)
            sv.add_subview(ph_lbl)
            y += 36 + p

        return y

    # ── button actions ─────────────────────────────────────────

    def _yes(self, sender):
        nd = KEY.get(self.node, {})
        if 'yes' in nd:
            self.history.append(self.node)
            self._go(nd['yes'])

    def _no(self, sender):
        nd = KEY.get(self.node, {})
        if 'no' in nd:
            self.history.append(self.node)
            self._go(nd['no'])

    def _back(self, sender):
        if self.history:
            prev = self.history.pop()
            self._go(prev)
        else:
            console.hud_alert('Already at the beginning!', 'error', 1.2)

    def _restart(self, sender):
        self.history = []
        self.photo   = None
        self._go('start')

    def _pick_photo(self, sender):
        """Let the user pick a photo from their camera roll."""
        img = photos.pick_image(show_albums=True)
        if img is not None:
            self.photo = img
            self._go(self.node)
        else:
            console.hud_alert('No photo chosen', 'error', 1.0)

    # ── ui.View layout callback ────────────────────────────────

    def layout(self):
        """Called by Pythonista when the view is resized / first shown."""
        W = self.width
        H = self.height

        header = self['header']
        if header:
            header.frame = (0, 0, W, HEADER_H)

        title_lbl = self['title_lbl']
        if title_lbl:
            title_lbl.frame = (90, 10, W - 180, 44)

        restart_btn = self['restart_btn']
        if restart_btn:
            restart_btn.frame = (W - 90, 14, 82, 36)

        step_lbl = self['step_lbl']
        if step_lbl:
            step_lbl.frame = (0, HEADER_H, W, 22)

        sv = self['scroll']
        if sv:
            sv.frame = (0, HEADER_H + 22, W, H - HEADER_H - 22 - BTN_AREA_H)

        panel = self['btn_panel']
        if panel:
            panel.frame = (0, H - BTN_AREA_H, W, BTN_AREA_H)
            gap = 8
            bw  = (W - gap * 5) / 4
            for i, name in enumerate(
                    ('yes_btn', 'no_btn', 'photo_btn', 'new_btn')):
                for s in panel.subviews:
                    if s.name == name:
                        s.frame = (gap + i * (bw + gap), BPAD, bw, BTN_H)
                        break

        self._go(self.node)


# ──────────────────────────────────────────────────────────────
#  LAUNCH
# ──────────────────────────────────────────────────────────────

def main():
    app = LabiataeApp()
    app.name = 'Labiatae Key'
    app.present('fullscreen')


if __name__ == '__main__':
    main()
