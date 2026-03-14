import streamlit as st
import os
from PIL import Image
import data

# ── Page config ────────────────────────────────────────────
st.set_page_config(
    page_title="Ajuga of Turkey",
    page_icon="🌿",
    layout="wide",
)

PHOTO_DIR = "photos"
ADMIN_PASSWORD = "ajuga2024"   # ← change this to whatever you like

# ── Ensure photo folders exist ──────────────────────────────
for sp in data.SPECIES:
    os.makedirs(os.path.join(PHOTO_DIR, str(sp["id"])), exist_ok=True)

# ── Session state defaults ──────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "key_step" not in st.session_state:
    st.session_state.key_step = "k1"
if "key_history" not in st.session_state:
    st.session_state.key_history = []
if "admin" not in st.session_state:
    st.session_state.admin = False

# ── Sidebar navigation ──────────────────────────────────────
with st.sidebar:
    st.title("🌿 Ajuga of Turkey")
    st.caption("Flora of Turkey · Vol. 7 · P.H. Davis (1982)")
    st.divider()
    if st.button("🏠  Home",          use_container_width=True): st.session_state.page = "home"
    if st.button("🔍  Identify plant", use_container_width=True):
        st.session_state.page = "key"
        st.session_state.key_step = "k1"
        st.session_state.key_history = []
    if st.button("📖  Browse species", use_container_width=True): st.session_state.page = "browse"
    if st.button("🔎  Search",         use_container_width=True): st.session_state.page = "search"
    if st.button("📋  Quick ref",      use_container_width=True): st.session_state.page = "quickref"
    st.divider()
    if st.button("🔒  Admin (add photos)", use_container_width=True): st.session_state.page = "admin"

# ── Helpers ─────────────────────────────────────────────────

def get_photos(species_id):
    folder = os.path.join(PHOTO_DIR, str(species_id))
    if not os.path.isdir(folder):
        return []
    exts = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
    return sorted([
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if os.path.splitext(f)[1].lower() in exts
    ])

def show_species_card(sp, expanded=True):
    photos = get_photos(sp["id"])
    col_info, col_photos = st.columns([3, 2]) if photos else (st.container(), None)

    with col_info:
        st.subheader(sp["name"])
        st.caption(f'*{sp["nickname"]}* · Turkish: {sp["turkish"]}')
        st.divider()
        col1, col2 = st.columns(2)
        col1.metric("Size", sp["size"])
        col2.metric("Life span", sp["type"])
        col1.metric("Flowers", sp["flower_colour"])
        col2.metric("Blooms", sp["when_it_flowers"])
        st.markdown(f"**Where found:** {sp['where_it_grows']}")
        st.divider()
        st.markdown(f"**Leaves:** {sp['leaf_shape']}")
        st.markdown(f"**Hairiness:** {sp['hairiness']}")
        st.divider()
        st.info(f"👁 **How to spot it:** {sp['how_to_spot_it']}")
        st.success(f"💡 **Fun fact:** {sp['fun_fact']}")
        st.caption("Source: Flora of Turkey, Vol. 7 — P.H. Davis (1982)")

    if photos and col_photos:
        with col_photos:
            st.markdown("**Photos**")
            for p in photos:
                try:
                    st.image(Image.open(p), use_container_width=True)
                except Exception:
                    pass

# ══════════════════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════════════════
if st.session_state.page == "home":
    st.title("🌿 Ajuga of Turkey")
    st.markdown(
        """
        **10 species** of *Ajuga* (Bugle) found in Turkey, based on
        *Flora of Turkey*, Vol. 7 (P.H. Davis, 1982).

        Use the sidebar to navigate:
        | Section | What it does |
        |---|---|
        | 🔍 Identify plant | Step-by-step A/B key to name your plant |
        | 📖 Browse species | Read a full card for any of the 10 species |
        | 🔎 Search | Find species by keyword |
        | 📋 Quick ref | One-line summary of all 10 species |
        | 🔒 Admin | Upload your own field photos (password protected) |
        """
    )
    st.divider()
    cols = st.columns(5)
    for i, sp in enumerate(data.SPECIES):
        photos = get_photos(sp["id"])
        with cols[i % 5]:
            if photos:
                try:
                    st.image(Image.open(photos[0]), use_container_width=True)
                except Exception:
                    pass
            colour_tag = "🟡" if "Yellow" in sp["flower_colour"] or "yellow" in sp["flower_colour"] else "🔵"
            st.caption(f"{colour_tag} **{sp['name'].split()[-1]}**")
            if st.button("View", key=f"home_{sp['id']}"):
                st.session_state.page = f"species_{sp['id']}"
                st.rerun()

# ══════════════════════════════════════════════════════════
# PAGE: INDIVIDUAL SPECIES
# ══════════════════════════════════════════════════════════
elif st.session_state.page.startswith("species_"):
    sp_id = int(st.session_state.page.split("_")[1])
    sp = next(s for s in data.SPECIES if s["id"] == sp_id)
    if st.button("← Back"):
        st.session_state.page = "browse"
        st.rerun()
    show_species_card(sp)

# ══════════════════════════════════════════════════════════
# PAGE: IDENTIFICATION KEY
# ══════════════════════════════════════════════════════════
elif st.session_state.page == "key":
    st.title("🔍 Identify Your Plant")
    st.caption("Answer A or B at each step. Use the buttons below to go back or restart.")

    step = data.KEY_MAP[st.session_state.key_step]
    step_id, question, hint, ans_a, ans_b, next_a, next_b = step

    st.divider()
    st.subheader(question)
    st.caption(f"Hint: {hint}")
    st.markdown("")

    col_a, col_b, _, col_back, col_restart = st.columns([2, 2, 1, 1, 1])

    with col_a:
        if st.button(ans_a, use_container_width=True, type="primary"):
            nxt = next_a
            if nxt[0] == "species":
                st.session_state.key_result = nxt[1]
                st.session_state.page = "key_result"
            else:
                st.session_state.key_history.append(st.session_state.key_step)
                st.session_state.key_step = nxt[1]
            st.rerun()

    with col_b:
        if st.button(ans_b, use_container_width=True):
            nxt = next_b
            if nxt[0] == "species":
                st.session_state.key_result = nxt[1]
                st.session_state.page = "key_result"
            else:
                st.session_state.key_history.append(st.session_state.key_step)
                st.session_state.key_step = nxt[1]
            st.rerun()

    with col_back:
        if st.button("← Back"):
            if st.session_state.key_history:
                st.session_state.key_step = st.session_state.key_history.pop()
            st.rerun()

    with col_restart:
        if st.button("↺ Restart"):
            st.session_state.key_step = "k1"
            st.session_state.key_history = []
            st.rerun()

    # Progress indicator
    st.divider()
    total = len(data.KEY)
    done = len(st.session_state.key_history)
    st.progress(done / total, text=f"Step {done + 1} of ~{total}")

# ══════════════════════════════════════════════════════════
# PAGE: KEY RESULT
# ══════════════════════════════════════════════════════════
elif st.session_state.page == "key_result":
    sp = next(s for s in data.SPECIES if s["id"] == st.session_state.key_result)
    st.success(f"## ✅ Your plant is most likely: *{sp['name']}* ({sp['nickname']})")
    show_species_card(sp)
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔍 Identify another plant", use_container_width=True):
            st.session_state.key_step = "k1"
            st.session_state.key_history = []
            st.session_state.page = "key"
            st.rerun()
    with col2:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

# ══════════════════════════════════════════════════════════
# PAGE: BROWSE
# ══════════════════════════════════════════════════════════
elif st.session_state.page == "browse":
    st.title("📖 Browse All 10 Species")
    for sp in data.SPECIES:
        photos = get_photos(sp["id"])
        colour = "🟡" if "Yellow" in sp["flower_colour"] or "yellow" in sp["flower_colour"] else "🔵"
        thumb_col, info_col, btn_col = st.columns([1, 5, 1])
        with thumb_col:
            if photos:
                try:
                    st.image(Image.open(photos[0]), width=80)
                except Exception:
                    st.write(colour)
            else:
                st.write(colour)
        with info_col:
            st.markdown(f"**{sp['name']}** — *{sp['nickname']}*")
            st.caption(sp["how_to_spot_it"])
        with btn_col:
            if st.button("View →", key=f"browse_{sp['id']}"):
                st.session_state.page = f"species_{sp['id']}"
                st.rerun()
        st.divider()

# ══════════════════════════════════════════════════════════
# PAGE: SEARCH
# ══════════════════════════════════════════════════════════
elif st.session_state.page == "search":
    st.title("🔎 Search Species")
    query = st.text_input("Type a word to search", placeholder="e.g. yellow, woolly, Taurus, annual, Black Sea")
    if query:
        results = []
        for sp in data.SPECIES:
            blob = " ".join([
                sp["name"], sp["nickname"], sp["turkish"],
                sp["flower_colour"], sp["leaf_shape"], sp["hairiness"],
                sp["where_it_grows"], sp["when_it_flowers"],
                sp["fun_fact"], sp["how_to_spot_it"], sp["type"],
            ]).lower()
            if query.lower() in blob:
                results.append(sp)

        if results:
            st.success(f"Found **{len(results)}** result(s) for '{query}'")
            for sp in results:
                colour = "🟡" if "Yellow" in sp["flower_colour"] or "yellow" in sp["flower_colour"] else "🔵"
                col1, col2 = st.columns([6, 1])
                with col1:
                    st.markdown(f"{colour} **{sp['name']}** — *{sp['nickname']}*")
                    st.caption(sp["how_to_spot_it"])
                with col2:
                    if st.button("View →", key=f"search_{sp['id']}"):
                        st.session_state.page = f"species_{sp['id']}"
                        st.rerun()
                st.divider()
        else:
            st.warning(f"Nothing found for '{query}'. Try: yellow, blue, woolly, silky, sticky, runners, Taurus, annual.")

# ══════════════════════════════════════════════════════════
# PAGE: QUICK REFERENCE
# ══════════════════════════════════════════════════════════
elif st.session_state.page == "quickref":
    st.title("📋 Quick Reference")
    st.caption("All 10 species at a glance")
    for sp in data.SPECIES:
        colour = "🟡" if "Yellow" in sp["flower_colour"] or "yellow" in sp["flower_colour"] else "🔵"
        st.markdown(f"{colour} **{sp['id']:02d}. {sp['name']}** ({sp['nickname']}) — {sp['how_to_spot_it']}")
    st.divider()
    st.caption("Source: Flora of Turkey, Vol. 7 — P.H. Davis (1982)")

# ══════════════════════════════════════════════════════════
# PAGE: ADMIN — UPLOAD PHOTOS
# ══════════════════════════════════════════════════════════
elif st.session_state.page == "admin":
    st.title("🔒 Admin — Add Photos")

    if not st.session_state.admin:
        pw = st.text_input("Enter admin password", type="password")
        if st.button("Log in"):
            if pw == ADMIN_PASSWORD:
                st.session_state.admin = True
                st.rerun()
            else:
                st.error("Wrong password.")
    else:
        st.success("Logged in as admin.")
        if st.button("Log out"):
            st.session_state.admin = False
            st.rerun()

        st.divider()
        st.subheader("Upload photos to a species")

        species_names = [f"{sp['id']}. {sp['name']} ({sp['nickname']})" for sp in data.SPECIES]
        choice = st.selectbox("Choose species", species_names)
        sp_id = int(choice.split(".")[0])
        sp = next(s for s in data.SPECIES if s["id"] == sp_id)

        uploaded = st.file_uploader(
            f"Upload photos for {sp['name']}",
            type=["jpg", "jpeg", "png", "webp"],
            accept_multiple_files=True,
        )
        if uploaded:
            folder = os.path.join(PHOTO_DIR, str(sp_id))
            os.makedirs(folder, exist_ok=True)
            for f in uploaded:
                save_path = os.path.join(folder, f.name)
                with open(save_path, "wb") as out:
                    out.write(f.getbuffer())
            st.success(f"Saved {len(uploaded)} photo(s) to species {sp_id}.")

        # Show existing photos with delete buttons
        existing = get_photos(sp_id)
        if existing:
            st.divider()
            st.markdown(f"**Existing photos for {sp['name']}** ({len(existing)} files)")
            cols = st.columns(4)
            for i, path in enumerate(existing):
                with cols[i % 4]:
                    try:
                        st.image(Image.open(path), use_container_width=True)
                    except Exception:
                        pass
                    fname = os.path.basename(path)
                    st.caption(fname)
                    if st.button("🗑 Delete", key=f"del_{sp_id}_{fname}"):
                        os.remove(path)
                        st.rerun()
        else:
            st.info("No photos uploaded yet for this species.")
