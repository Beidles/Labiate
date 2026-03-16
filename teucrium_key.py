#!/usr/bin/env python3
# coding: utf-8
"""
Teucrium (Germander) Species Key for Turkey
Based on Flora of Turkey, Vol. 7 (P.H. Davis, 1982)
Written for Pythonista 3 on iPad.

Features:
  - Native iOS touch interface (big YES / NO buttons)
  - Add a photo from your camera roll to your identification
  - 13 Teucrium species found in Turkey
  - Written so a 14-year-old can use it with no botanical background

HOW TO RUN IN PYTHONISTA 3:
  Open this file in Pythonista 3 and tap the Run button (▶).
  The app will appear as a full-screen view.
"""

import ui
import photos
import console

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
        'q':    'Is the plant a small ANNUAL – soft, low, and will die '
                'completely after one season (not a woody shrub or tough '
                'perennial that comes back every year)?',
        'hint': 'Annual plants are soft and floppy, grow from seed each '
                'year, and die at the end of summer. Perennials are tougher '
                'and either shrubby or regrow from the same roots each year.',
        'yes':  'annual_branch',
        'no':   'q_shrubby',
    },

    # ── annual branch ──────────────────────────────────────────
    'annual_branch': {
        'q':    'Are the LEAVES deeply cut or divided – looking like a '
                'feather or a fern frond, with many narrow lobes?',
        'hint': 'Deeply divided leaves are cut almost to the midrib, '
                'making the leaf look like multiple tiny fingers or a '
                'fern. Simple toothed leaves are NOT divided like this.',
        'yes':  'annual_divided',
        'no':   'r_pseudochamaepitys',
    },

    'annual_divided': {
        'q':    'Does the plant smell strongly of GARLIC or ONION when '
                'you crush a leaf between your fingers?',
        'hint': 'Crush a small piece of leaf and sniff it close up. '
                'Teucrium botrys smells faintly aromatic but NOT of garlic. '
                'If there is a strong garlic/onion smell, answer YES.',
        'yes':  'r_scordotonia_annual',
        'no':   'r_botrys',
    },

    # ── is it shrubby or woody? ────────────────────────────────
    'q_shrubby': {
        'q':    'Is the plant CLEARLY WOODY AND SHRUBBY at the base – '
                'with stiff woody stems that persist through winter '
                '(like a small bush, not a soft herbaceous plant)?',
        'hint': 'Woody = the stems are hard and do not die back in winter. '
                'Many Teucrium species are small shrubs or subshrubs. '
                'If the stems are soft and green right to the base = NOT woody.',
        'yes':  'q_woolly',
        'no':   'q_herbaceous',
    },

    # ── woolly check (for shrubby plants) ─────────────────────
    'q_woolly': {
        'q':    'Is the WHOLE PLANT covered in VERY DENSE WHITE OR GREY '
                'WOOLLY HAIR – making it look silvery, grey, or felted '
                'all over (stems, leaves, and flower heads)?',
        'hint': 'This is much more than normal hairiness. The plant '
                'should look like it has been dusted with thick cotton '
                'wool or grey felt. Normal hairy plants do NOT look like this.',
        'yes':  'q_polium_branch',
        'no':   'q_yellow_shrub',
    },

    # ── yellow flowers? (shrubby, not woolly) ─────────────────
    'q_yellow_shrub': {
        'q':    'Are the FLOWERS YELLOW?',
        'hint': 'Pure yellow petals. Most Teucrium have pink, purple, '
                'white, or cream flowers. Yellow-flowered species are '
                'much less common.',
        'yes':  'r_flavum',
        'no':   'q_shrub_pink',
    },

    # ── shrubby pink branch ────────────────────────────────────
    'q_shrub_pink': {
        'q':    'Do the LEAVES look like tiny OAK LEAVES – oval, shiny '
                'on top, with rounded lobes around the edges '
                '(a bit like a miniature oak leaf)?',
        'hint': 'Teucrium chamaedrys has leaves that really do look like '
                'tiny dark-green oak leaves – oval, glossy, with '
                'rounded lobes. Other species have plainer oval or '
                'oblong leaves without the lobed oak-leaf outline.',
        'yes':  'q_chamaedrys_detail',
        'no':   'q_shrub_other',
    },

    'q_chamaedrys_detail': {
        'q':    'Are you on a rocky hillside, cliff, or old stone wall '
                '(rather than a forest edge or shaded woodland)?',
        'hint': 'T. chamaedrys is most common on sunny rocky places '
                'and old walls. T. divaricatum is similar but tends to '
                'grow in scrub and forest edges. If you are on an open '
                'sunny rocky slope or wall, answer YES.',
        'yes':  'r_chamaedrys',
        'no':   'r_divaricatum',
    },

    'q_shrub_other': {
        'q':    'Are the LEAVES HEART-SHAPED at the base (like a heart '
                'or kidney shape where the stalk joins the leaf), '
                'with deeply toothed or scalloped edges?',
        'hint': 'Heart-shaped base = the leaf is wider than long near '
                'the stalk, with two rounded lobes at the base, like a '
                'Valentine heart. This is called cordate in botany.',
        'yes':  'r_lamiifolium',
        'no':   'q_orientale_check',
    },

    'q_orientale_check': {
        'q':    'Are the LEAVES deeply cut into NARROW PINNATE LOBES '
                '– like a feather, with the main stalk and narrow '
                'side lobes (pinnately divided)?',
        'hint': 'Pinnate means like a feather – a central stalk with '
                'pairs of lobes along it. This is quite distinctive. '
                'Most Teucrium have simple oval leaves. If the leaves '
                'are clearly feather-divided, answer YES.',
        'yes':  'r_orientale',
        'no':   'r_other_pink_shrub',
    },

    # ── woolly shrub branch ────────────────────────────────────
    'q_polium_branch': {
        'q':    'Do the flowers grow in ROUND POMPOM-LIKE HEADS at the '
                'top of the stem – like a small ball of tiny white or '
                'cream flowers?',
        'hint': 'Teucrium polium and relatives have flowers packed into '
                'neat round or oval heads at the top, like small white '
                'pompoms. Teucrium montanum has flowers in a flat-topped '
                'cluster, not a round pompom.',
        'yes':  'q_polium_detail',
        'no':   'r_montanum',
    },

    'q_polium_detail': {
        'q':    'Are you at LOW OR MEDIUM ALTITUDE – below about '
                '1500 m (lowland plains, coastal hills, low mountains)?',
        'hint': 'T. polium grows mainly at lower altitudes (sea level '
                'to about 1500 m) across much of Turkey. T. capitatum '
                'is very similar and grows at similar or higher altitudes. '
                'If unsure, answer YES.',
        'yes':  'r_polium',
        'no':   'r_capitatum',
    },

    # ── herbaceous (non-shrubby) perennial branch ─────────────
    'q_herbaceous': {
        'q':    'Does the plant grow IN OR VERY CLOSE TO WATER – at the '
                'edge of a river, stream, pond, marsh, or wet ditch?',
        'hint': 'Teucrium scordium loves wet places and is rarely found '
                'far from water. If you are in a dry field or rocky '
                'hillside, answer NO.',
        'yes':  'r_scordium',
        'no':   'q_herb_leaf',
    },

    'q_herb_leaf': {
        'q':    'Are the LEAVES NARROW AND ELONGATED – clearly longer '
                'than they are wide, like a strap or oblong shape '
                '(more than 3 times as long as wide)?',
        'hint': 'Strap-shaped leaves are much longer than wide. Most '
                'herbaceous Teucrium have broader oval or heart-shaped '
                'leaves. If you are unsure whether the leaves count as '
                'narrow, answer NO.',
        'yes':  'r_orientale',
        'no':   'q_herb_flower_colour',
    },

    'q_herb_flower_colour': {
        'q':    'Are the flowers YELLOW or YELLOW-GREEN (rather than '
                'pink, white, or purple)?',
        'hint': 'Yellow-flowered herbaceous Teucrium are found in '
                'woodland shade in northern Turkey. If the flowers are '
                'any shade of pink, mauve, white, or cream, answer NO.',
        'yes':  'r_scorodonia',
        'no':   'q_herb_pink',
    },

    'q_herb_pink': {
        'q':    'Are the leaves CLEARLY HEART-SHAPED at the base '
                '(like a Valentine heart where the stalk joins the leaf) '
                'with deeply toothed edges?',
        'hint': 'Heart-shaped (cordate) leaves have two rounded lobes '
                'at the base where the stalk attaches, giving the leaf '
                'a heart-like outline. Look at the base of several leaves.',
        'yes':  'r_lamiifolium',
        'no':   'r_other_herb',
    },

    # ──────────────────────────────────────────────────────────
    #  RESULT NODES
    # ──────────────────────────────────────────────────────────

    'r_botrys': {
        'latin':   'Teucrium botrys L.',
        'common':  'Cut-leaved Germander',
        'about':   'A small annual (lives one year). The leaves are '
                   'deeply cut into narrow lobes, making them look like '
                   'tiny fern fronds. Small pink to purple flowers grow '
                   'in the leaf axils up the stem. Softly hairy plant. '
                   'The deeply divided leaves are the key feature – no '
                   'other common Turkish Teucrium looks quite like this.',
        'habitat': 'Dry rocky places, stony fields, disturbed ground, '
                   'olive groves and vineyards. Found across Turkey, '
                   'mainly at low and medium altitudes.',
        'fun':     'The name botrys comes from the Greek word for a '
                   'bunch of grapes – the clusters of flowers along '
                   'the stem were thought to look like a grape bunch!',
    },

    'r_pseudochamaepitys': {
        'latin':   'Teucrium pseudochamaepitys L.',
        'common':  'False Ground-pine Germander',
        'about':   'A small annual with unusual narrow, strap-like or '
                   'slightly lobed leaves. Pale yellow or whitish flowers. '
                   'Smells slightly resinous. Less common than T. botrys '
                   'and found mainly in the western and southern parts '
                   'of Turkey near the Mediterranean coast.',
        'habitat': 'Dry rocky slopes, garrigue, open scrub, stony '
                   'ground near the sea. Mainly coastal and sub-coastal '
                   'areas of western and southern Turkey.',
        'fun':     'Pseudochamaepitys means false Chamaepitys – it was '
                   'once confused with Ajuga chamaepitys, the Ground-pine, '
                   'because both are small and grow in similar dry stony places!',
    },

    'r_scordotonia_annual': {
        'latin':   'Teucrium scordium L. (check smell carefully)',
        'common':  'Water Germander (garlic-scented form)',
        'about':   'If your plant smells strongly of garlic and has '
                   'divided leaves, double-check whether it might be '
                   'T. scordium (Water Germander), which has a garlic '
                   'smell. However T. scordium usually grows near water '
                   'and has simple (not divided) leaves. Re-check and '
                   'compare with the habitat – if near water with simple '
                   'leaves and garlic smell, it is likely T. scordium.',
        'habitat': 'Near rivers, streams, ponds, and wet ground.',
        'fun':     'The scordium in the name comes from the Greek word '
                   'for garlic – ancient people used this plant as a '
                   'garlic substitute in cooking!',
    },

    'r_chamaedrys': {
        'latin':   'Teucrium chamaedrys L.',
        'common':  'Wall Germander',
        'about':   'A small woody shrub, 10–30 cm tall. The leaves are '
                   'the most distinctive feature – dark green, oval, '
                   'shiny on top, with rounded lobes that really do '
                   'look like tiny oak leaves. Pink to deep pink-purple '
                   'flowers in short spikes at the top. One of the most '
                   'common and easy-to-recognise Teucrium in Turkey.',
        'habitat': 'Rocky hillsides, cliffs, old stone walls, dry scrub, '
                   'open woodland edges. Very widespread across Turkey '
                   'from sea level to about 1500 m.',
        'fun':     'Wall Germander was used as a herbal remedy for gout '
                   'for hundreds of years – even King Charles V of France '
                   'reportedly took it as medicine in the 1500s!',
    },

    'r_divaricatum': {
        'latin':   'Teucrium divaricatum Sieber ex Heldr.',
        'common':  'Spreading Germander',
        'about':   'Very similar to T. chamaedrys and often confused '
                   'with it. Also has the distinctive small oak-like '
                   'leaves but tends to be more spreading and branching '
                   '(divaricatum means spreading). Found more in scrubby '
                   'woodland edges and forest margins than on pure rocky '
                   'cliffs. Flowers pink to purplish.',
        'habitat': 'Scrub, woodland edges, phrygana (low thorny scrub), '
                   'shaded rocky places. Mainly western and southern Turkey.',
        'fun':     'Botanists still argue about whether T. divaricatum '
                   'should be a separate species from T. chamaedrys or '
                   'just a variety of it – they are extremely similar!',
    },

    'r_lamiifolium': {
        'latin':   'Teucrium lamiifolium d\'Urv.',
        'common':  'Dead-nettle-leaved Germander',
        'about':   'Has noticeably heart-shaped leaves with deeply '
                   'toothed edges that look very like dead-nettle '
                   '(Lamium) leaves – hence the name. Pink to purple '
                   'flowers. Can be somewhat woody at the base but '
                   'also has soft leafy stems. Less common than '
                   'T. chamaedrys.',
        'habitat': 'Rocky slopes, scrub, shaded places, woodland margins. '
                   'Found mainly in western and southern Turkey.',
        'fun':     'Lamiifolium literally means Lamium-leaved in Latin. '
                   'Botanists named it after Lamium (dead-nettle) because '
                   'the leaves look so similar – a bit like naming someone '
                   '"looks-like-their-neighbour"!',
    },

    'r_orientale': {
        'latin':   'Teucrium orientale L.',
        'common':  'Oriental Germander',
        'about':   'Has very distinctive PINNATELY DIVIDED leaves – '
                   'the leaves are cut into narrow lobes like a feather, '
                   'unlike most Teucrium which have simple oval leaves. '
                   'Pink to purple flowers with a white or pale lower '
                   'lip. Usually a medium-sized perennial. The divided '
                   'leaves make it easy to identify.',
        'habitat': 'Rocky places, dry hillsides, scrub, stony fields. '
                   'Found across Turkey, especially in central and '
                   'eastern regions.',
        'fun':     'The name orientale just means eastern in Latin – '
                   'it was named by European botanists who found it '
                   'in the eastern Mediterranean world!',
    },

    'r_scordium': {
        'latin':   'Teucrium scordium L.',
        'common':  'Water Germander',
        'about':   'A soft perennial with simple oval to oblong leaves '
                   'that have toothed edges and smell of GARLIC when '
                   'crushed. Pink to purple-pink flowers in the leaf '
                   'axils. The plant loves wet ground and is rarely '
                   'found away from water. The garlic smell is the '
                   'key feature – crush a leaf and sniff!',
        'habitat': 'Riverbanks, stream edges, pond margins, wet '
                   'meadows, ditches and marshes. Found throughout '
                   'Turkey wherever there is standing or running water.',
        'fun':     'Scordium comes from the Greek for garlic. Ancient '
                   'Romans and Greeks used this plant mixed with wine '
                   'as a treatment for snake bites and poisoning!',
    },

    'r_scorodonia': {
        'latin':   'Teucrium scorodonia L.',
        'common':  'Wood Sage',
        'about':   'A perennial with soft, wrinkled, heart-shaped leaves '
                   'that smell faintly of sage when crushed. The flowers '
                   'are PALE YELLOW-GREEN, which is unusual for Teucrium. '
                   'Grows in woodland shade – you will find it under '
                   'trees rather than in the open. Found mainly in '
                   'northern Turkey (Black Sea region) in woodland.',
        'habitat': 'Shaded woodland, forest edges, hedgerows, shaded '
                   'rocky slopes. Mainly in the Black Sea coastal region '
                   'of northern Turkey.',
        'fun':     'Wood Sage was used as a substitute for hops in '
                   'home-brewed ale before hops became widely available – '
                   'people made bitter beer from it for centuries!',
    },

    'r_flavum': {
        'latin':   'Teucrium flavum L.',
        'common':  'Yellow Germander',
        'about':   'A woody shrublet with YELLOW flowers – quite '
                   'unusual in Teucrium, which mostly have pink or '
                   'white flowers. The leaves are small, oval, and '
                   'slightly sticky or resinous. The woody base and '
                   'yellow flowers make it easy to pick out once you '
                   'know what to look for.',
        'habitat': 'Dry rocky hillsides, limestone cliffs, phrygana '
                   '(low Mediterranean scrub), coastal rocky slopes. '
                   'Mainly western and southern Turkey near the '
                   'Mediterranean coast.',
        'fun':     'Flavum means yellow in Latin. Most of the mint '
                   'family (Labiatae) has pink, purple, or white '
                   'flowers, so yellow-flowered members like this '
                   'are always memorable!',
    },

    'r_polium': {
        'latin':   'Teucrium polium L.',
        'common':  'Felty Germander / Poly Mountain',
        'about':   'A low woolly shrublet covered in thick white or '
                   'grey felt-like hair all over. Flowers white or '
                   'pale cream, packed in neat ROUND POMPOM HEADS at '
                   'the top of the stems. Very common and easy to '
                   'recognise once you have seen it. The whole plant '
                   'feels soft and furry to the touch.',
        'habitat': 'Dry rocky hillsides, open stony ground, roadsides, '
                   'dry garrigue and phrygana. Very common across Turkey '
                   'at low and medium altitudes, especially in '
                   'dry sunny places.',
        'fun':     'Teucrium polium has been used in Turkish and '
                   'Greek herbal medicine for centuries – traditionally '
                   'drunk as a tea to help with stomach problems and '
                   'as a tonic. You can still buy it in herb markets!',
    },

    'r_capitatum': {
        'latin':   'Teucrium capitatum L.',
        'common':  'Headed Germander',
        'about':   'Very similar to T. polium and sometimes treated as '
                   'the same species. Also densely woolly-white all over '
                   'with round pompom flower-heads of white or pale '
                   'cream flowers. Tends to grow at higher altitudes '
                   'than typical T. polium. Some botanists think these '
                   'are just varieties of the same species.',
        'habitat': 'Rocky slopes, stony hillsides, mountain grassland. '
                   'Widespread across Turkey at medium to higher altitudes, '
                   'especially in central and eastern Turkey.',
        'fun':     'Capitatum means head-like in Latin – named for the '
                   'round flower-head. Botanists have argued for 200 years '
                   'whether T. polium and T. capitatum are truly different '
                   'species – the debate is still not settled!',
    },

    'r_montanum': {
        'latin':   'Teucrium montanum L.',
        'common':  'Mountain Germander',
        'about':   'A low woody shrublet with dense white woolly hair, '
                   'but instead of round pompom flower-heads, the flowers '
                   'are in a FLAT-TOPPED or slightly elongated cluster. '
                   'Flowers white or cream. Leaves narrow and strap-like, '
                   'white-woolly below. Often found on limestone rocks at '
                   'mountain altitudes.',
        'habitat': 'Rocky limestone slopes, mountain grassland, stony '
                   'places at altitude. Found mainly in mountain areas '
                   'of Turkey, often on limestone.',
        'fun':     'Montanum means mountain in Latin. The woolly coat '
                   'is an adaptation for mountain life – it traps warm '
                   'air near the leaf surface, protecting the plant '
                   'from cold mountain winds and frost!',
    },

    'r_other_pink_shrub': {
        'latin':   'Teucrium sp. (possibly T. kotschyanum or similar)',
        'common':  'Turkish Germander (species uncertain)',
        'about':   'A shrubby pink-flowered Teucrium that did not quite '
                   'fit the other options. Turkey has over 20 Teucrium '
                   'species and some are very hard to tell apart without '
                   'a microscope and the full Flora of Turkey key. This '
                   'could be T. kotschyanum, T. lydium, or another '
                   'local species.',
        'habitat': 'Rocky slopes, scrub, dry hillsides – various habitats.',
        'fun':     'Turkey is one of the most important countries in '
                   'the world for Teucrium diversity – more species '
                   'grow here than almost anywhere else, and botanists '
                   'are still discovering and describing new ones!',
    },

    'r_other_herb': {
        'latin':   'Teucrium sp. (possibly T. chamaedrys or T. polium)',
        'common':  'Germander (species uncertain)',
        'about':   'A herbaceous or slightly woody Teucrium with pink '
                   'or purple flowers that did not clearly fit one of '
                   'the other options. Check again whether the plant '
                   'might have some woolly hair (T. polium group) or '
                   'the tiny oak-like leaves of T. chamaedrys. Turkey '
                   'has many species and some are very similar.',
        'habitat': 'Rocky places, scrub, fields, disturbed ground.',
        'fun':     'Even professional botanists sometimes need the '
                   'full Flora of Turkey and a magnifying glass to '
                   'identify Teucrium species. Try taking a photo '
                   'and uploading it to the free iNaturalist app!',
    },
}


# ──────────────────────────────────────────────────────────────
#  PYTHONISTA 3 APP
# ──────────────────────────────────────────────────────────────

PAD   = 12    # general padding
BPAD  = 16    # button area height padding
BTN_H = 52    # button height
HEADER_H = 64 # header bar height
BTN_AREA_H = BTN_H + BPAD * 2  # total height of the fixed button row


class TeucriumApp(ui.View):
    """Full-screen Pythonista 3 UI for the Teucrium identification key."""

    def __init__(self):
        self.history = []          # list of node_ids for Back button
        self.node    = 'start'     # current node
        self.photo   = None        # ui.Image attached by user (result only)
        self.bg_color = C_BG

        self._mk_header()
        self._mk_scroll()
        self._mk_buttons()
        self._go('start')

    # ── layout helpers ─────────────────────────────────────────

    def _mk_header(self):
        """Dark green header bar with title, Back, and Restart buttons."""
        h = self
        W = h.width if h.width > 0 else 390   # safe default for layout

        bar = ui.View()
        bar.name        = 'header'
        bar.bg_color    = C_HEADER
        bar.frame       = (0, 0, W, HEADER_H)
        bar.flex        = 'W'
        self.add_subview(bar)

        # Back button (left)
        back = ui.Button()
        back.name         = 'back_btn'
        back.title        = '◀ Back'
        back.font         = ('<system-bold>', 15)
        back.tint_color   = C_STEP_TXT
        back.frame        = (8, 14, 80, 36)
        back.action       = self._back
        bar.add_subview(back)

        # Title label (centre)
        title = ui.Label()
        title.name        = 'title_lbl'
        title.text        = 'TEUCRIUM KEY  🌿'
        title.font        = ('<system-bold>', 17)
        title.text_color  = C_TITLE_TXT
        title.alignment   = ui.ALIGN_CENTER
        title.frame       = (90, 10, W - 180, 44)
        title.flex        = 'W'
        bar.add_subview(title)

        # Restart button (right)
        restart = ui.Button()
        restart.name       = 'restart_btn'
        restart.title      = 'Restart ↺'
        restart.font       = ('<system-bold>', 15)
        restart.tint_color = C_STEP_TXT
        restart.frame      = (W - 90, 14, 82, 36)
        restart.flex       = 'L'
        restart.action     = self._restart
        bar.add_subview(restart)

        # Step counter label (below header, overlapping slightly)
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
        W = self.width if self.width > 0 else 390
        H = self.height if self.height > 0 else 844
        top    = HEADER_H + 22
        bottom = BTN_AREA_H
        sv = ui.ScrollView()
        sv.name      = 'scroll'
        sv.frame     = (0, top, W, H - top - bottom)
        sv.flex      = 'WH'
        sv.bg_color  = C_BG
        self.add_subview(sv)

    def _mk_buttons(self):
        """Fixed YES / NO / Add Photo / New ID buttons at the bottom."""
        W = self.width if self.width > 0 else 390
        H = self.height if self.height > 0 else 844

        panel = ui.View()
        panel.name     = 'btn_panel'
        panel.bg_color = '#E8E8E4'
        panel.frame    = (0, H - BTN_AREA_H, W, BTN_AREA_H)
        panel.flex     = 'WT'
        self.add_subview(panel)

        specs = [
            ('yes_btn',   '✓ YES',      C_YES,   self._yes),
            ('no_btn',    '✗ NO',       C_NO,    self._no),
            ('photo_btn', '📷 Photo',   C_PHOTO, self._pick_photo),
            ('new_btn',   '⟳ New ID',  C_NEW,   self._restart),
        ]
        n   = len(specs)
        gap = 8
        bw  = (W - gap * (n + 1)) / n
        for i, (name, title, colour, action) in enumerate(specs):
            btn = ui.Button()
            btn.name       = name
            btn.title      = title
            btn.bg_color   = colour
            btn.tint_color = C_TITLE_TXT
            btn.font       = ('<system-bold>', 15)
            btn.frame      = (gap + i * (bw + gap), BPAD, bw, BTN_H)
            btn.corner_radius = 10
            btn.action     = action
            panel.add_subview(btn)

    # ── navigation ─────────────────────────────────────────────

    def _go(self, node_id):
        """Move to a node, rebuild the scroll content."""
        self.node = node_id
        nd = KEY[node_id]

        # Update step counter
        step_lbl = self['step_lbl']
        if step_lbl:
            if 'q' in nd:
                step_lbl.text = f'Step {len(self.history) + 1}'
            else:
                step_lbl.text = 'Result'

        # Show/hide YES and NO buttons (hidden on result nodes)
        is_result = 'latin' in nd
        for name in ('yes_btn', 'no_btn'):
            btn = self['yes_btn'] if name == 'yes_btn' else self['no_btn']
            if btn:
                btn.hidden = is_result
        # Photo / New ID always visible
        photo_btn = self['photo_btn']
        if photo_btn:
            photo_btn.hidden = not is_result

        # Rebuild scroll content
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
            first = (len(self.history) == 0)
            y = self._render_question(nd, sv, W, y, first)

        sv.content_size = (W, y + PAD)

    # ── render helpers ─────────────────────────────────────────

    def _lbl(self, sv, text, x, y, w, h, font_size=15,
             bold=False, color=C_BODY_TXT, align=ui.ALIGN_LEFT,
             lines=0):
        """Add a ui.Label to sv, return the label."""
        lbl = ui.Label()
        lbl.text        = text
        lbl.font        = (('<system-bold>' if bold else '<system>'), font_size)
        lbl.text_color  = color
        lbl.alignment   = align
        lbl.number_of_lines = lines
        lbl.frame       = (x, y, w, h)
        sv.add_subview(lbl)
        return lbl

    def _card(self, sv, x, y, w, h, bg=C_CARD, radius=12):
        """Add a rounded card view to sv, return the view."""
        card = ui.View()
        card.bg_color      = bg
        card.corner_radius = radius
        card.frame         = (x, y, w, h)
        sv.add_subview(card)
        return card

    def _text_height(self, text, width, font_size=15, bold=False):
        """Estimate label height for multi-line text."""
        # approximate: chars per line ≈ width / (font_size * 0.55)
        import math
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

    def _render_question(self, nd, sv, W, y, first):
        """Build the question card in sv. Returns next y."""
        p = PAD
        cw = W - p * 2

        # ── intro card (shown only on first question) ──────────
        if first:
            intro_text = (
                'This key helps you identify TEUCRIUM (Germander) species '
                'from Turkey. Based on Flora of Turkey Vol. 7 (P.H. Davis).\n\n'
                'Just answer YES or NO to each question!\n\n'
                '◀ Back  –  go to the previous question\n'
                '↺ Restart  –  start over from the beginning\n'
                '📷 Photo  –  attach a photo to your result'
            )
            ih = self._text_height(intro_text, cw - p * 2, font_size=14) + p * 2
            card = self._card(sv, p, y, cw, ih, bg=C_CARD2)
            lbl  = ui.Label()
            lbl.text             = intro_text
            lbl.font             = ('<system>', 14)
            lbl.text_color       = '#1B5E20'
            lbl.number_of_lines  = 0
            lbl.frame            = (p, p, cw - p * 2, ih - p * 2)
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
            hlbl.text            = '💡 Hint:  ' + hint
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
        blbl.text       = '✅  FOUND IT!'
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
        clbl.text            = '🌿 ' + nd['common']
        clbl.font            = ('<system>', 16)
        clbl.text_color      = C_BODY_TXT
        clbl.number_of_lines = 0
        clbl.frame           = (p, p, cw - p * 2, ch)
        ccard.add_subview(clbl)
        y += ch + p * 2 + p

        # ── About / Description ────────────────────────────────
        for icon, key, bg_col in [
            ('📋 About:',    'about',   C_CARD),
            ('📍 Habitat:',  'habitat', '#E3F2FD'),
            ('🎉 Fun fact:', 'fun',     '#FFF9C4'),
        ]:
            text = nd.get(key, '')
            if not text:
                continue
            full = icon + '  ' + text
            th   = self._text_height(full, cw - p * 2, font_size=14) + 4
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
            # scale to fit width
            img   = self.photo
            ratio = img.size[1] / img.size[0] if img.size[0] > 0 else 1
            ph    = int(cw * ratio)
            ph    = min(ph, 340)   # cap height at 340 px

            pcard = self._card(sv, p, y, cw, ph + p * 2 + 24, bg=C_CARD)

            title_lbl = ui.Label()
            title_lbl.text       = '📷 Your Photo'
            title_lbl.font       = ('<system-bold>', 13)
            title_lbl.text_color = '#555555'
            title_lbl.frame      = (p, 6, cw - p * 2, 18)
            pcard.add_subview(title_lbl)

            iv = ui.ImageView()
            iv.image         = img
            iv.content_mode  = ui.CONTENT_SCALE_ASPECT_FIT
            iv.frame         = (p, p + 24, cw - p * 2, ph)
            pcard.add_subview(iv)
            y += ph + p * 2 + 24 + p

        # ── prompt to add a photo ──────────────────────────────
        else:
            ph_lbl = ui.Label()
            ph_lbl.text       = '📷 Tap "Photo" below to attach a photo of your plant'
            ph_lbl.font       = ('<system>', 13)
            ph_lbl.text_color = '#888888'
            ph_lbl.alignment  = ui.ALIGN_CENTER
            ph_lbl.number_of_lines = 0
            ph_lbl.frame      = (p, y, cw, 36)
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
            # Re-render current result with photo
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
            top    = HEADER_H + 22
            bottom = BTN_AREA_H
            sv.frame = (0, top, W, H - top - bottom)

        panel = self['btn_panel']
        if panel:
            panel.frame = (0, H - BTN_AREA_H, W, BTN_AREA_H)
            gap = 8
            n   = 4
            bw  = (W - gap * (n + 1)) / n
            for i, name in enumerate(
                    ('yes_btn', 'no_btn', 'photo_btn', 'new_btn')):
                btn = panel[name] if name in [s.name for s in panel.subviews] else None
                if btn is None:
                    for s in panel.subviews:
                        if s.name == name:
                            btn = s
                            break
                if btn:
                    btn.frame = (gap + i * (bw + gap), BPAD, bw, BTN_H)

        # Re-render content at new width
        self._go(self.node)


# ──────────────────────────────────────────────────────────────
#  LAUNCH
# ──────────────────────────────────────────────────────────────

def main():
    app = TeucriumApp()
    app.name          = 'Teucrium Key'
    app.present('fullscreen')


if __name__ == '__main__':
    main()
