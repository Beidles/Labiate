# ============================================================
# AJUGA (Bugle) - Identification App for Turkey
# Source: Flora of Turkey, Vol. 7 — P.H. Davis (1982)
#
# ── HOW TO RUN ON REPLIT ────────────────────────────────────
#  1. Go to replit.com and create a new Python repl
#  2. Paste this whole file into main.py  (or ajuga.py)
#  3. In the Shell tab type:
#       pip install streamlit Pillow
#  4. Then run:
#       streamlit run main.py --server.port=8080 --server.headless=true
#  5. Click the "Open in new tab" button Replit shows — done!
#     (If you added a .replit file, just press the Run button)
#
# ── HOW TO RUN LOCALLY ──────────────────────────────────────
#   pip install streamlit Pillow
#   streamlit run ajuga.py
#
# ── PHOTOS ──────────────────────────────────────────────────
#   Use the Upload button on any species — photos save
#   automatically in a folder called ajuga_photos/
# ============================================================

import streamlit as st
import os
from PIL import Image

st.set_page_config(
    page_title="Ajuga of Turkey",
    page_icon="🌿",
    layout="wide",
)

# ============================================================
# SPECIES DATABASE
# Written in plain English so anyone can understand it!
# Based on Flora of Turkey Vol. 7, P.H. Davis (1982)
# ============================================================

SPECIES = [
    {
        "id": 1,
        "name": "Ajuga chamaepitys subsp. chamaepitys",
        "nickname": "Ground Pine",
        "turkish": "Sarı mayasıl otu",
        "size": "5–30 cm tall",
        "type": "Annual (lives for one year)",
        "flower_colour": "🟡 Yellow, often with red-purple streaks",
        "leaf_shape": "Deeply cut into 3 narrow finger-like lobes — looks a bit like a tiny pine seedling. "
                      "Crush a leaf and it smells like pine trees!",
        "hairiness": "Hairy all over",
        "where_it_grows": "Arable fields, rocky hillsides, disturbed ground. "
                          "Found all over Turkey, especially W, C, and S Anatolia. 0–1800 m altitude.",
        "when_it_flowers": "March to July",
        "fun_fact": "The most common Ajuga in Turkey. Its pine smell is how it got the name 'Ground Pine'!",
        "how_to_spot_it": "Yellow flowers + deeply cut pine-needle-like leaves + smells of pine",
        "photo_file": "1_chamaepitys_chamaepitys.jpg",
    },
    {
        "id": 2,
        "name": "Ajuga chamaepitys subsp. chia",
        "nickname": "Chian Ground Pine",
        "turkish": "Sakız mayasıl otu",
        "size": "5–20 cm tall (smaller and more compact)",
        "type": "Annual (lives for one year)",
        "flower_colour": "🟡 Yellow, sometimes with purple streaks",
        "leaf_shape": "Like subsp. chamaepitys but the finger-like lobes are SHORTER and WIDER. "
                      "Still smells like pine.",
        "hairiness": "Hairy",
        "where_it_grows": "Dry rocky hillsides and scrubby areas. "
                          "W and SW Turkey — mostly the Aegean coast and nearby islands. 0–1000 m.",
        "when_it_flowers": "March to June",
        "fun_fact": "Very similar to subsp. chamaepitys but lives mainly near the Aegean coast. "
                    "'Chia' refers to the island of Chios.",
        "how_to_spot_it": "Yellow flowers + shorter, stubbier leaf lobes + coastal W Turkey",
        "photo_file": "2_chamaepitys_chia.jpg",
    },
    {
        "id": 3,
        "name": "Ajuga iva",
        "nickname": "Yellow Bugle",
        "turkish": "Sarmaşık mayasıl otu",
        "size": "5–20 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "🟡 Yellow or creamy-white, sometimes tinged purple",
        "leaf_shape": "Simple, oblong leaves with slightly wavy edges — NOT cut into finger-lobes like chamaepitys. "
                      "Does NOT smell of pine.",
        "hairiness": "Covered in sticky glandular hairs — feels a little sticky when you touch it",
        "where_it_grows": "Dry open hillsides, rocky slopes, stony ground. "
                          "W, S, and C Turkey. 0–1500 m.",
        "when_it_flowers": "March to June",
        "fun_fact": "The sticky hairs trap tiny insects. Used in Turkish folk medicine for skin conditions.",
        "how_to_spot_it": "Yellow flowers + simple (not cut) leaves + feels slightly sticky + no pine smell",
        "photo_file": "3_iva.jpg",
    },
    {
        "id": 4,
        "name": "Ajuga orientalis",
        "nickname": "Eastern Bugle",
        "turkish": "Doğu mayasıl otu",
        "size": "10–40 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "💜 Blue-violet",
        "leaf_shape": "Oval leaves with scalloped (wavy) edges. Big leaves at the base of the plant, "
                      "smaller ones higher up. Often has a purple tinge.",
        "hairiness": "Softly hairy",
        "where_it_grows": "Meadows, forest clearings, stream sides, rocky slopes. "
                          "All over Turkey — very common in N, E, and C Anatolia. 200–2200 m.",
        "when_it_flowers": "April to July",
        "fun_fact": "One of the most widespread Ajuga in Turkey — you are very likely to see this one! "
                    "Can form big carpets of blue-violet flowers in mountain meadows.",
        "how_to_spot_it": "Blue-violet flowers + soft oval leaves + very common everywhere in Turkey",
        "photo_file": "4_orientalis.jpg",
    },
    {
        "id": 5,
        "name": "Ajuga reptans",
        "nickname": "Creeping Bugle",
        "turkish": "Sürünücü mayasıl otu",
        "size": "10–30 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "💜 Blue-violet (very rarely pink or white)",
        "leaf_shape": "Shiny oval leaves with wavy edges. Leaves near the ground are often bronze-purple coloured.",
        "hairiness": "Slightly hairy",
        "where_it_grows": "Damp meadows, shaded woodland edges, shaded banks. "
                          "N and NW Turkey — mainly the Black Sea coast. 0–1500 m.",
        "when_it_flowers": "April to June",
        "fun_fact": "This is the ONLY Turkish Ajuga that sends out long creeping runners (called stolons) "
                    "along the ground — just like strawberry plants! The runners take root and make new plants.",
        "how_to_spot_it": "Blue-violet flowers + LONG CREEPING RUNNERS along ground + shiny leaves + Black Sea region",
        "photo_file": "5_reptans.jpg",
    },
    {
        "id": 6,
        "name": "Ajuga genevensis",
        "nickname": "Blue Bugle",
        "turkish": "Cenevre mayasıl otu",
        "size": "10–40 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "💜 Bright blue-violet (rarely pink)",
        "leaf_shape": "Oval leaves with coarse teeth along the edges. Leaves look GREY-GREEN "
                      "because they are covered in dense hairs.",
        "hairiness": "Densely hairy — gives the plant a grey-green colour",
        "where_it_grows": "Dry grassland, meadows, scrubby areas, roadsides. "
                          "N, W, and C Turkey. 500–2000 m.",
        "when_it_flowers": "April to June",
        "fun_fact": "Looks similar to Creeping Bugle (A. reptans) but has NO creeping runners. "
                    "The grey-green hairy look tells them apart.",
        "how_to_spot_it": "Blue-violet flowers + grey-green hairy leaves + NO creeping runners",
        "photo_file": "6_genevensis.jpg",
    },
    {
        "id": 7,
        "name": "Ajuga laxmannii",
        "nickname": "White Woolly Bugle",
        "turkish": "Yünlü mayasıl otu",
        "size": "10–35 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "🟡 Pale yellow or creamy-white",
        "leaf_shape": "Oblong leaves with smooth or slightly wavy edges. "
                      "The whole plant is covered in such thick white woolly hairs that it looks almost white!",
        "hairiness": "VERY densely white-woolly — like the plant is wrapped in cotton wool",
        "where_it_grows": "Dry stony slopes, rocky hillsides, steppe grassland. "
                          "C, E, and SE Turkey — the drier inland areas. 600–2000 m.",
        "when_it_flowers": "May to July",
        "fun_fact": "The thickest, wooliest Ajuga in Turkey — once you have seen it you will never forget it! "
                    "The white wool helps it survive the hot dry summers of central Anatolia.",
        "how_to_spot_it": "Pale yellow flowers + VERY thick white woolly covering all over the plant",
        "photo_file": "7_laxmannii.jpg",
    },
    {
        "id": 8,
        "name": "Ajuga salicifolia",
        "nickname": "Willow-leaved Bugle",
        "turkish": "Söğütyapraklı mayasıl otu",
        "size": "20–50 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "💜 Blue-violet",
        "leaf_shape": "VERY NARROW long leaves that look like willow tree leaves — unlike any other Ajuga! "
                      "The edges are smooth or have very faint teeth.",
        "hairiness": "Lightly hairy",
        "where_it_grows": "Mountain meadows, stream sides, moist rocky slopes. "
                          "E and NE Turkey — the Pontic mountains near the Black Sea. 800–2500 m.",
        "when_it_flowers": "June to August",
        "fun_fact": "Its name literally means 'willow-leaved' and those narrow leaves make it unmistakable. "
                    "A mountain specialist found mainly in eastern Turkey.",
        "how_to_spot_it": "Blue-violet flowers + VERY NARROW willow-like leaves + mountain streams + E Turkey",
        "photo_file": "8_salicifolia.jpg",
    },
    {
        "id": 9,
        "name": "Ajuga bombycina",
        "nickname": "Silky Bugle",
        "turkish": "İpekli mayasıl otu",
        "size": "5–20 cm tall",
        "type": "Perennial (lives for many years)",
        "flower_colour": "🟡 Pale yellow or white",
        "leaf_shape": "Oval-spoon shaped with smooth edges. "
                      "Completely covered in LONG SHINY SILVER HAIRS that feel like silk.",
        "hairiness": "Long silky silver hairs — soft and shiny like a silk scarf",
        "where_it_grows": "Limestone rocks and cliffs, rocky slopes in the Taurus Mountains. "
                          "S Turkey only. 500–2000 m.",
        "when_it_flowers": "April to June",
        "fun_fact": "The silkiest plant in the whole Ajuga genus! 'Bombycina' comes from the Latin word "
                    "for silkworm. It only grows in Turkey's Taurus Mountains.",
        "how_to_spot_it": "Pale yellow/white flowers + SILKY SILVER SHEEN all over the plant + Taurus Mountains",
        "photo_file": "9_bombycina.jpg",
    },
    {
        "id": 10,
        "name": "Ajuga postii",
        "nickname": "Post's Bugle",
        "turkish": "Post'un mayasıl otu",
        "size": "10–30 cm tall",
        "type": "Annual or biennial (lives 1–2 years)",
        "flower_colour": "💜 Blue or blue-violet",
        "leaf_shape": "Oval to spoon-shaped leaves with rounded teeth along the edges. "
                      "Moderately hairy. Nothing very distinctive — similar to A. orientalis but smaller.",
        "hairiness": "Moderately hairy",
        "where_it_grows": "Rocky hillsides, scrubby areas, forest margins. "
                          "S and SE Turkey — Cilicia region (around Adana/Mersin). 200–1500 m.",
        "when_it_flowers": "March to May",
        "fun_fact": "Named after Georg Post, a botanist who studied plants across the Middle East in the 1800s.",
        "how_to_spot_it": "Blue-violet flowers + oval toothed leaves + only in SE Turkey (Cilicia area)",
        "photo_file": "10_postii.jpg",
    },
]

# ============================================================
# PHOTO FOLDER — auto-created if it doesn't exist
# ============================================================

PHOTO_DIR = "ajuga_photos"
os.makedirs(PHOTO_DIR, exist_ok=True)

def photo_path(sp):
    return os.path.join(PHOTO_DIR, sp["photo_file"])

def has_photo(sp):
    return os.path.exists(photo_path(sp))

# ============================================================
# HELPER — photo upload widget
# ============================================================

def photo_uploader(sp):
    uploaded = st.file_uploader(
        "📷 Upload a photo for this species",
        type=["jpg", "jpeg", "png"],
        key=f"upload_{sp['id']}",
        help="Upload any JPG or PNG photo. It will be saved automatically.",
    )
    if uploaded:
        img = Image.open(uploaded)
        img.save(photo_path(sp), "JPEG")
        st.success("Photo saved! It will appear next time you open this species.")
        st.rerun()

# ============================================================
# HELPER — show a species card
# ============================================================

def show_species_card(sp):
    col_photo, col_info = st.columns([1, 1])

    with col_photo:
        if has_photo(sp):
            st.image(photo_path(sp), use_container_width=True,
                     caption=sp["name"])
        else:
            st.markdown(
                """
                <div style="background:#f0f0f0; border:2px dashed #bbb;
                            border-radius:12px; padding:50px 20px;
                            text-align:center; color:#888; font-size:1.1em;">
                    📷 No photo yet<br>
                    <small>Use the upload button below to add one!</small>
                </div>
                """,
                unsafe_allow_html=True,
            )
        photo_uploader(sp)

    with col_info:
        # Colour-coded header
        st.markdown(
            f"""
            <div style="background:#e8f5e9; padding:18px; border-radius:12px; margin-bottom:14px;">
                <small style="color:#888;">Species {sp['id']} of 10</small><br>
                <span style="font-size:1.5em; font-weight:bold; font-style:italic;">{sp['name']}</span><br>
                <span style="font-size:1.2em; color:#333;">{sp['nickname']}</span><br>
                <span style="color:green; font-size:1em;">🇹🇷 {sp['turkish']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(f"**📏 Size:** {sp['size']}")
        st.markdown(f"**🌸 Flower colour:** {sp['flower_colour']}")
        st.markdown(f"**📅 Flowers:** {sp['when_it_flowers']}")
        st.markdown(f"**📍 Where it grows:** {sp['where_it_grows']}")

    # Plain-English description boxes
    st.markdown("---")
    b1, b2, b3 = st.columns(3)

    with b1:
        st.markdown("**🍃 What do the leaves look like?**")
        st.write(sp["leaf_shape"])

    with b2:
        st.markdown("**✋ Is it hairy?**")
        st.write(sp["hairiness"])
        st.markdown("**⏳ How long does it live?**")
        st.write(sp["type"])

    with b3:
        st.markdown("**⭐ How to spot it**")
        st.info(sp["how_to_spot_it"])

    st.markdown(f"💡 **Fun fact:** {sp['fun_fact']}")
    st.caption("Source: Flora of Turkey, Vol. 7 — P.H. Davis (1982)")

# ============================================================
# PAGE HEADER
# ============================================================

st.title("🌿 Ajuga in Turkey — Identification Guide")
st.markdown(
    "A beginner-friendly guide to all **10 Ajuga species** found in Turkey.  \n"
    "Source: *Flora of Turkey, Vol. 7* — P.H. Davis (1982)"
)

# Photo progress bar
n_photos = sum(1 for s in SPECIES if has_photo(s))
st.progress(n_photos / len(SPECIES),
            text=f"Photos added: {n_photos} of {len(SPECIES)} species")

st.divider()

# ============================================================
# TABS
# ============================================================

tab_key, tab_browse, tab_search, tab_swift = st.tabs(
    ["🔑 Identify My Plant", "📋 Browse All Species", "🔎 Search", "📱 Swift Code"]
)

# ============================================================
# TAB 1: IDENTIFICATION KEY (beginner-friendly)
# ============================================================

with tab_key:
    st.subheader("What Ajuga do I have?")
    st.write(
        "Answer each question in plain English — no botany knowledge needed! "
        "You will end up with a species name."
    )
    st.info(
        "💡 **How to use this:** Look closely at your plant and answer the questions "
        "below one at a time. Each answer leads you closer to the right species."
    )

    # Key steps — written for a complete beginner
    KEY = {
        "k1": {
            "question": "What colour are the FLOWERS?",
            "hint": "Look at the petals — are they yellow/cream, or blue/purple?",
            "a": "🟡 Yellow or creamy-white",
            "b": "💜 Blue or blue-violet (sometimes pale pink or white)",
            "next_a": "k2",
            "next_b": "k5",
        },
        "k2": {
            "question": "Are the LEAVES deeply cut into 3 narrow finger-like strips?",
            "hint": "Hold a leaf up — is it cut almost all the way to the stalk into 3 thin strips? "
                    "Does it smell of pine when you crush it?",
            "a": "YES — leaves cut into 3 narrow strips, smells of pine",
            "b": "NO — leaves are more whole (not cut into strips) and no pine smell",
            "next_a": "k3",
            "next_b": "k4",
        },
        "k3": {
            "question": "Are the 3 leaf strips SHORT and STUBBY (not long and thin)?",
            "hint": "Compare the length and width of the leaf strips. "
                    "Are you near the Aegean coast (Izmir, Muğla, Aegean islands)?",
            "a": "YES — strips are short and stubby; I am in W/SW Turkey near the coast",
            "b": "NO — strips are long and thin; I am inland or anywhere in Turkey",
            "next_a": ("species", 2),
            "next_b": ("species", 1),
        },
        "k4": {
            "question": "Is the whole plant covered in THICK WHITE WOOLLY hairs — like cotton wool?",
            "hint": "Step back and look at the plant. Does it look almost white or silver-grey "
                    "because of very thick fluffy hairs?",
            "a": "YES — very thick woolly white hairs, looks almost white",
            "b": "NO — hairs are different (silky/silver, OR the plant feels slightly sticky)",
            "next_a": ("species", 7),
            "next_b": "k4b",
        },
        "k4b": {
            "question": "Do the hairs look SHINY and feel SILKY SMOOTH (like stroking a cat)?",
            "hint": "Touch the plant gently. Do the hairs feel silky and look silver-shiny? "
                    "Or does the plant feel slightly sticky instead?",
            "a": "YES — silky and shiny silver hairs; I am in the Taurus Mountains (S Turkey)",
            "b": "NO — plant feels slightly sticky/gummy; dry open hillside",
            "next_a": ("species", 9),
            "next_b": ("species", 3),
        },
        "k5": {
            "question": "Are the LEAVES very NARROW and long, like willow tree leaves?",
            "hint": "Look at a leaf — is it much longer than it is wide, like a thin strap or ribbon? "
                    "Are you near mountain streams in eastern Turkey?",
            "a": "YES — very narrow strap-like leaves; E Turkey near streams",
            "b": "NO — leaves are broader (oval or oblong)",
            "next_a": ("species", 8),
            "next_b": "k6",
        },
        "k6": {
            "question": "Can you see LONG CREEPING STEMS running along the ground?",
            "hint": "Look around the base of the plant. Are there stems creeping along the soil "
                    "like strawberry runners, making new baby plants? "
                    "Are you in the N Turkey Black Sea region?",
            "a": "YES — long creeping stems running across the ground; Black Sea region",
            "b": "NO — no creeping stems; plant grows as a normal upright clump",
            "next_a": ("species", 5),
            "next_b": "k7",
        },
        "k7": {
            "question": "Do the LEAVES look GREY-GREEN (not bright green) because of dense hairs?",
            "hint": "Look at the leaf colour. Are they dull greyish-green from lots of hairs? "
                    "Or are they a brighter or darker green?",
            "a": "YES — leaves look grey-green from very dense hairs; no creeping stems",
            "b": "NO — leaves are greener or shinier",
            "next_a": ("species", 6),
            "next_b": "k8",
        },
        "k8": {
            "question": "Are you in S or SE Turkey (e.g. Adana, Mersin, Hatay area)?",
            "hint": "A. orientalis is the most common blue-flowered species across most of Turkey. "
                    "A. postii is found mainly in the Cilicia/SE region.",
            "a": "YES — I am in S or SE Turkey (Cilicia / Adana / Mersin area)",
            "b": "NO — I am in N, C, E, or W Turkey (or not sure)",
            "next_a": ("species", 10),
            "next_b": ("species", 4),
        },
    }

    # Session state for key
    for key, default in [
        ("ak_step", "k1"), ("ak_result", None), ("ak_history", [])
    ]:
        if key not in st.session_state:
            st.session_state[key] = default

    if st.session_state.ak_result is not None:
        sp = next(s for s in SPECIES if s["id"] == st.session_state.ak_result)
        st.success(
            f"✅ Your plant is most likely: ***{sp['name']}*** "
            f"({sp['nickname']})"
        )
        st.balloons()
        show_species_card(sp)

    else:
        step = KEY[st.session_state.ak_step]

        # Question box
        st.markdown(
            f"""
            <div style="background:#fff9c4; padding:16px; border-radius:10px;
                        border-left:5px solid #f9a825; margin-bottom:10px;">
                <b style="font-size:1.2em;">❓ {step['question']}</b><br>
                <span style="color:#666; font-size:0.95em;">💡 {step['hint']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button(
                f"A — {step['a']}",
                use_container_width=True,
                key="ak_btn_a",
                type="primary",
            ):
                st.session_state.ak_history.append(st.session_state.ak_step)
                nxt = step["next_a"]
                if isinstance(nxt, tuple):
                    st.session_state.ak_result = nxt[1]
                else:
                    st.session_state.ak_step = nxt
                st.rerun()

        with col_b:
            if st.button(
                f"B — {step['b']}",
                use_container_width=True,
                key="ak_btn_b",
            ):
                st.session_state.ak_history.append(st.session_state.ak_step)
                nxt = step["next_b"]
                if isinstance(nxt, tuple):
                    st.session_state.ak_result = nxt[1]
                else:
                    st.session_state.ak_step = nxt
                st.rerun()

        # Progress indicator
        n_answered = len(st.session_state.ak_history)
        if n_answered > 0:
            st.caption(f"Questions answered so far: {n_answered}")

    st.divider()
    col_back, col_reset = st.columns(2)
    with col_back:
        if st.session_state.ak_history:
            if st.button("← Go back one step", use_container_width=True):
                prev = st.session_state.ak_history.pop()
                st.session_state.ak_step = prev
                st.session_state.ak_result = None
                st.rerun()
    with col_reset:
        if st.button("🔄 Start again from the beginning", use_container_width=True):
            st.session_state.ak_step = "k1"
            st.session_state.ak_result = None
            st.session_state.ak_history = []
            st.rerun()

# ============================================================
# TAB 2: BROWSE ALL SPECIES
# ============================================================

with tab_browse:
    st.subheader("All 10 Ajuga Species in Turkey")
    st.write(
        "Click any species below to read about it and add a photo. "
        "A ✅ means a photo has been added."
    )

    for sp in SPECIES:
        badge = "✅" if has_photo(sp) else "📷"
        flower = "🟡" if "Yellow" in sp["flower_colour"] else "💜"
        label = f"{badge} {flower} **{sp['id']}.** *{sp['name']}* — {sp['nickname']}"

        with st.expander(label):
            show_species_card(sp)

# ============================================================
# TAB 3: SEARCH
# ============================================================

with tab_search:
    st.subheader("Search for a Species")
    st.write("Type any word — colour, place, feature — to find matching species.")

    query = st.text_input(
        "",
        placeholder="Try: yellow, woolly, Black Sea, stolons, silky, Taurus, annual...",
    )

    if query:
        q = query.lower()
        results = []
        for sp in SPECIES:
            blob = " ".join([
                sp["name"], sp["nickname"], sp["turkish"],
                sp["flower_colour"], sp["leaf_shape"], sp["hairiness"],
                sp["where_it_grows"], sp["when_it_flowers"],
                sp["fun_fact"], sp["how_to_spot_it"], sp["type"],
            ]).lower()
            if q in blob:
                results.append(sp)

        if results:
            st.write(f"Found **{len(results)}** result(s) for **'{query}'**:")
            for sp in results:
                badge = "✅" if has_photo(sp) else "📷"
                flower = "🟡" if "Yellow" in sp["flower_colour"] else "💜"
                with st.expander(
                    f"{badge} {flower} *{sp['name']}* — {sp['nickname']}"
                ):
                    show_species_card(sp)
        else:
            st.warning(
                f"Nothing found for '{query}'. "
                "Try words like: yellow, blue, woolly, silky, sticky, stolons, Taurus, annual, perennial."
            )
    else:
        # Quick-reference summary
        st.markdown("### Quick Reference — All 10 Species at a Glance")
        for sp in SPECIES:
            flower = "🟡" if "Yellow" in sp["flower_colour"] else "💜"
            badge = "✅" if has_photo(sp) else "📷"
            st.markdown(
                f"{badge} {flower} **{sp['id']}. {sp['name']}** "
                f"({sp['nickname']}) — {sp['how_to_spot_it']}"
            )

# ============================================================
# TAB 4: SWIFT CODE — split into 5 files for Swift Playgrounds
# ============================================================

import os as _os

_SWIFT_DIR = _os.path.join(_os.path.dirname(__file__), "swift_split")

_SWIFT_FILES = [
    ("1_Models.swift",    "File 1 — Models & Helpers",       "Data structures and helper functions"),
    ("2_PlantData.swift", "File 2 — Plant Database",         "All 45 genera of Labiatae in Turkey"),
    ("3_KeyData.swift",   "File 3 — Identification Key",     "Dichotomous key steps (s1–s60)"),
    ("4_Views.swift",     "File 4 — SwiftUI Views",          "Browse, Identify, Search, and Quiz views"),
    ("5_LabiateApp.swift","File 5 — App Entry Point",        "ContentView + @main (paste into main file)"),
]

with tab_swift:
    st.subheader("📱 LabiateApp — Swift Playgrounds (iPad)")
    st.info(
        "The full app is split into **5 smaller files** so Swift Playgrounds on iPad "
        "doesn't freeze. Copy each file one at a time."
    )

    st.markdown("""
**How to set up in Swift Playgrounds:**
1. Open Swift Playgrounds → tap **+** → **App Playground** → Create
2. In the sidebar, tap **+** to add **4 new Swift files** (you'll have 5 total)
3. Rename them: `1_Models`, `2_PlantData`, `3_KeyData`, `4_Views`, `5_LabiateApp`
4. Paste each file's code into the matching file (use the Copy button below)
5. The **main app file** (house icon) = paste **File 5** there
6. Tap **Run ▶**
""")

    st.divider()

    for filename, title, description in _SWIFT_FILES:
        filepath = _os.path.join(_SWIFT_DIR, filename)
        if _os.path.exists(filepath):
            with open(filepath, "r") as f:
                code = f.read()
            line_count = len(code.splitlines())
            with st.expander(f"**{title}** — {description} ({line_count} lines)"):
                st.code(code, language="swift")
        else:
            st.warning(f"File not found: {filename}")
