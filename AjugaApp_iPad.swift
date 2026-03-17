// ============================================================
// AJUGA OF TURKEY — iPad App (Swift Playgrounds 4)
//
// Based on: Flora of Turkey, Vol. 7 — P.H. Davis (1982)
// Written so a 14-year-old can understand it!
// Includes: browse, step-by-step ID key, search, and photos
//
// HOW TO USE:
//   1. Open Swift Playgrounds on your iPad
//   2. Tap + → App Playground → Create
//   3. Tap the default file in the sidebar
//   4. Select All (tap screen → Select All) and DELETE
//   5. Paste THIS entire file
//   6. Tap Run ▶
//
// Your photos are saved permanently on your iPad.
// ============================================================

import SwiftUI
import PhotosUI

// ============================================================
// MARK: - DATA MODEL
// One struct holds everything we need to know about a species.
// A 'struct' is just a box that holds related information together.
// ============================================================

struct AjugaSpecies: Identifiable {
    let id: Int
    let name: String            // Scientific (Latin) name
    let nickname: String        // Plain English name
    let turkish: String         // Turkish name
    let size: String            // How tall it grows
    let lifespan: String        // Annual / biennial / perennial
    let flowerColour: String    // Colour of the flowers
    let flowerEmoji: String     // 🟡 or 💜 for quick scanning
    let leafShape: String       // What the leaves look like
    let hairiness: String       // Hairy? What kind?
    let whereItGrows: String    // Habitat + region in Turkey
    let whenItFlowers: String   // Which months
    let howToSpotIt: String     // Quick ID tip — one sentence
    let funFact: String         // Cool fact for everyone!
}

// ============================================================
// MARK: - SPECIES DATA (all 10 Ajuga found in Turkey)
// Source: Flora of Turkey Vol. 7, P.H. Davis (1982)
// ============================================================

let allAjuga: [AjugaSpecies] = [

    AjugaSpecies(
        id: 1,
        name: "Ajuga chamaepitys subsp. chamaepitys",
        nickname: "Ground Pine",
        turkish: "Sarı mayasıl otu",
        size: "5–30 cm tall",
        lifespan: "Annual — lives just one year, then dies after making seeds",
        flowerColour: "Yellow, often with red-purple streaks on the lower lip",
        flowerEmoji: "🟡",
        leafShape: "Deeply cut into 3 narrow finger-like strips — looks a bit like a tiny pine seedling! Crush a leaf and it actually smells like pine trees.",
        hairiness: "Hairy all over",
        whereItGrows: "Arable fields, rocky hillsides, disturbed ground. Found all over Turkey, especially W, C, and S Anatolia. 0–1800 m altitude.",
        whenItFlowers: "March to July",
        howToSpotIt: "Yellow flowers + leaves cut into 3 pine-needle-like strips + smells of pine when you crush a leaf",
        funFact: "The most common Ajuga in Turkey! Its pine smell is exactly how it got the name 'Ground Pine' — even though it is not related to pine trees at all."
    ),

    AjugaSpecies(
        id: 2,
        name: "Ajuga chamaepitys subsp. chia",
        nickname: "Chian Ground Pine",
        turkish: "Sakız mayasıl otu",
        size: "5–20 cm tall (more compact than subsp. chamaepitys)",
        lifespan: "Annual — lives just one year",
        flowerColour: "Yellow, sometimes with purple streaks",
        flowerEmoji: "🟡",
        leafShape: "Like subsp. chamaepitys (3 strips) but the strips are SHORTER and WIDER — stubbier looking. Still smells like pine.",
        hairiness: "Hairy",
        whereItGrows: "Dry rocky hillsides and scrubby areas. W and SW Turkey — mostly the Aegean coast and nearby islands. 0–1000 m.",
        whenItFlowers: "March to June",
        howToSpotIt: "Yellow flowers + shorter stubbier leaf strips (not long and thin) + coastal W Turkey near the Aegean",
        funFact: "'Chia' refers to the Greek island of Chios, which is right next to the Turkish coast where this plant mainly lives. The two islands are basically next-door neighbours!"
    ),

    AjugaSpecies(
        id: 3,
        name: "Ajuga iva",
        nickname: "Yellow Bugle",
        turkish: "Sarmaşık mayasıl otu",
        size: "5–20 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Yellow or creamy-white, sometimes tinged purple",
        flowerEmoji: "🟡",
        leafShape: "Simple oblong leaves with slightly wavy edges — NOT cut into strips like Ground Pine. Does NOT smell of pine.",
        hairiness: "Covered in sticky glandular hairs — feels slightly sticky when you touch it, like it has tiny glue dots on it",
        whereItGrows: "Dry open hillsides, rocky slopes, stony ground. W, S, and C Turkey. 0–1500 m.",
        whenItFlowers: "March to June",
        howToSpotIt: "Yellow flowers + simple whole leaves (not cut into strips) + feels slightly sticky + no pine smell",
        funFact: "Those sticky hairs can actually trap tiny insects! It has also been used in Turkish folk medicine for hundreds of years to treat skin conditions."
    ),

    AjugaSpecies(
        id: 4,
        name: "Ajuga orientalis",
        nickname: "Eastern Bugle",
        turkish: "Doğu mayasıl otu",
        size: "10–40 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Blue-violet",
        flowerEmoji: "💜",
        leafShape: "Oval leaves with scalloped (wavy) edges. Big leaves at the base, smaller ones higher up. Leaves often have a purple tinge.",
        hairiness: "Softly hairy — feels gentle and pleasant to touch",
        whereItGrows: "Meadows, forest clearings, stream sides, rocky slopes. All over Turkey — very common in N, E, and C Anatolia. 200–2200 m.",
        whenItFlowers: "April to July",
        howToSpotIt: "Blue-violet flowers + soft oval leaves + very widespread across Turkey — the most common blue Ajuga",
        funFact: "You are very likely to see this one! It can form huge carpets of blue-violet flowers in mountain meadows in spring. It is the go-to Ajuga for most of Turkey."
    ),

    AjugaSpecies(
        id: 5,
        name: "Ajuga reptans",
        nickname: "Creeping Bugle",
        turkish: "Sürünücü mayasıl otu",
        size: "10–30 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Blue-violet (very rarely pink or white)",
        flowerEmoji: "💜",
        leafShape: "Shiny oval leaves with wavy edges. Leaves near the ground are often bronze-purple coloured.",
        hairiness: "Slightly hairy on the stem; leaves are fairly smooth and shiny",
        whereItGrows: "Damp meadows, shaded woodland edges, shaded banks. N and NW Turkey — mainly the Black Sea coast. 0–1500 m.",
        whenItFlowers: "April to June",
        howToSpotIt: "Blue-violet flowers + LONG CREEPING RUNNERS along the ground (like strawberry plants!) + shiny leaves + Black Sea region",
        funFact: "This is the ONLY Turkish Ajuga that sends out long creeping stems (called stolons) along the ground — just like a strawberry plant does! Each runner takes root and grows into a whole new plant."
    ),

    AjugaSpecies(
        id: 6,
        name: "Ajuga genevensis",
        nickname: "Blue Bugle",
        turkish: "Cenevre mayasıl otu",
        size: "10–40 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Bright blue-violet (rarely pink)",
        flowerEmoji: "💜",
        leafShape: "Oval leaves with coarse teeth along the edges. The leaves look grey-green because they are covered in dense hairs.",
        hairiness: "Densely hairy — the hairs make the whole plant look grey-green instead of bright green",
        whereItGrows: "Dry grassland, meadows, scrubby areas, roadsides. N, W, and C Turkey. 500–2000 m.",
        whenItFlowers: "April to June",
        howToSpotIt: "Blue-violet flowers + grey-green hairy leaves + NO creeping runners (unlike Creeping Bugle)",
        funFact: "Looks very similar to Creeping Bugle but has absolutely no creeping stems. The grey-green hairy colour is the thing that tells them apart most easily. 'Genevensis' means 'from Geneva', Switzerland."
    ),

    AjugaSpecies(
        id: 7,
        name: "Ajuga laxmannii",
        nickname: "White Woolly Bugle",
        turkish: "Yünlü mayasıl otu",
        size: "10–35 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Pale yellow or creamy-white",
        flowerEmoji: "🟡",
        leafShape: "Oblong leaves with smooth or slightly wavy edges. The whole plant is covered in such thick white woolly hairs it looks almost white!",
        hairiness: "VERY densely white-woolly — like the plant is wrapped in cotton wool",
        whereItGrows: "Dry stony slopes, rocky hillsides, steppe grassland. C, E, and SE Turkey — the drier inland areas. 600–2000 m.",
        whenItFlowers: "May to July",
        howToSpotIt: "Pale yellow flowers + VERY thick white woolly covering all over the plant — unmistakable once you have seen it",
        funFact: "The wooliest Ajuga in Turkey — once you see it you will never forget it! The thick white wool acts like sunscreen and insulation, helping the plant survive the scorching hot summers of central Anatolia."
    ),

    AjugaSpecies(
        id: 8,
        name: "Ajuga salicifolia",
        nickname: "Willow-leaved Bugle",
        turkish: "Söğütyapraklı mayasıl otu",
        size: "20–50 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Blue-violet",
        flowerEmoji: "💜",
        leafShape: "VERY NARROW, long leaves that look just like willow tree leaves — unlike any other Ajuga! The edges are smooth or have very faint teeth.",
        hairiness: "Lightly hairy",
        whereItGrows: "Mountain meadows, stream sides, moist rocky slopes. E and NE Turkey — the Pontic mountains near the Black Sea. 800–2500 m.",
        whenItFlowers: "June to August",
        howToSpotIt: "Blue-violet flowers + VERY NARROW willow-like leaves (much longer than wide) + mountain streams in E Turkey",
        funFact: "'Salicifolia' literally means 'willow-leaved' in Latin — 'salix' is willow. Those narrow strap-like leaves make it impossible to confuse with any other Ajuga. It is a real mountain specialist."
    ),

    AjugaSpecies(
        id: 9,
        name: "Ajuga bombycina",
        nickname: "Silky Bugle",
        turkish: "İpekli mayasıl otu",
        size: "5–20 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Pale yellow or white",
        flowerEmoji: "🟡",
        leafShape: "Oval-spoon shaped with smooth edges. Completely covered in LONG SHINY SILVER HAIRS that feel like stroking a silk scarf.",
        hairiness: "Long silky silver hairs — soft, shiny, and beautiful",
        whereItGrows: "Limestone rocks and cliffs, rocky slopes in the Taurus Mountains. S Turkey only. 500–2000 m.",
        whenItFlowers: "April to June",
        howToSpotIt: "Pale yellow/white flowers + SILKY SILVER SHEEN all over + Taurus Mountains in S Turkey only",
        funFact: "'Bombycina' comes from the Latin word for silkworm! It ONLY grows in Turkey's Taurus Mountains — found nowhere else in the world. The silky hairs reflect sunlight to keep the plant cool on hot exposed limestone."
    ),

    AjugaSpecies(
        id: 10,
        name: "Ajuga postii",
        nickname: "Post's Bugle",
        turkish: "Post'un mayasıl otu",
        size: "10–30 cm tall",
        lifespan: "Annual or biennial — lives 1–2 years",
        flowerColour: "Blue or blue-violet",
        flowerEmoji: "💜",
        leafShape: "Oval to spoon-shaped leaves with rounded teeth along the edges. Moderately hairy. Similar to Eastern Bugle but smaller.",
        hairiness: "Moderately hairy",
        whereItGrows: "Rocky hillsides, scrubby areas, forest margins. S and SE Turkey — the Cilicia region around Adana and Mersin. 200–1500 m.",
        whenItFlowers: "March to May",
        howToSpotIt: "Blue-violet flowers + oval toothed leaves + only in SE Turkey (Adana/Mersin/Cilicia area)",
        funFact: "Named after Georg Post, a botanist who explored plants across the Middle East in the 1800s. Without explorers like him travelling through Turkey on horseback, these species might never have been named!"
    ),
]

// ============================================================
// MARK: - IDENTIFICATION KEY DATA
//
// A 'dichotomous key' works by giving you two choices at each
// step. 'Dichotomous' just means 'splits into two'. You keep
// choosing until you reach a species name. Simple!
// ============================================================

// KeyResult is what happens after you answer a question:
// either move to the next question, or you have found the species!
enum KeyResult {
    case nextStep(String)   // go to another question
    case species(Int)       // you found it! here is the species id
}

struct KeyStep: Identifiable {
    let id: String          // short code like "k1", "k2"...
    let question: String    // the question to ask
    let hint: String        // extra help explaining what to look for
    let optionA: String     // first choice
    let optionB: String     // second choice
    let nextA: KeyResult    // what happens if you pick A
    let nextB: KeyResult    // what happens if you pick B
}

let keySteps: [KeyStep] = [

    KeyStep(
        id: "k1",
        question: "What colour are the FLOWERS?",
        hint: "Look closely at the petals. Are they yellow/cream coloured, or are they blue/purple?",
        optionA: "🟡  Yellow or creamy-white",
        optionB: "💜  Blue or blue-violet (sometimes pale pink or white)",
        nextA: .nextStep("k2"),
        nextB: .nextStep("k5")
    ),

    KeyStep(
        id: "k2",
        question: "Are the LEAVES deeply cut into 3 narrow finger-like strips?",
        hint: "Hold a leaf up to the light. Is it cut almost all the way to the stalk into 3 thin strips? Does it smell of pine when you crush it between your fingers?",
        optionA: "YES — leaves cut into 3 narrow strips, smells of pine when crushed",
        optionB: "NO — leaves are more whole (not cut into strips) and no pine smell",
        nextA: .nextStep("k3"),
        nextB: .nextStep("k4")
    ),

    KeyStep(
        id: "k3",
        question: "Are the 3 leaf strips SHORT and STUBBY (not long and thin)?",
        hint: "Look at the shape of the leaf strips. Short and fat, or long and thin like pine needles? Also — are you near the Aegean coast (Izmir, Muğla, Aegean islands)?",
        optionA: "YES — strips are short and stubby; I am in W/SW Turkey near the Aegean coast",
        optionB: "NO — strips are long and thin (like pine needles); I could be anywhere in Turkey",
        nextA: .species(2),
        nextB: .species(1)
    ),

    KeyStep(
        id: "k4",
        question: "Is the whole plant covered in THICK WHITE WOOLLY hairs — like cotton wool?",
        hint: "Step back and look at the whole plant. Does it look almost white or silver-grey because of very thick fluffy hairs? Like it is wearing a woolly jumper?",
        optionA: "YES — very thick woolly white hairs; the plant looks almost white overall",
        optionB: "NO — the hairs are different (silky/silver, OR the plant feels slightly sticky)",
        nextA: .species(7),
        nextB: .nextStep("k4b")
    ),

    KeyStep(
        id: "k4b",
        question: "Do the hairs look SHINY and feel SILKY SMOOTH (like stroking a cat)?",
        hint: "Touch the plant gently. Do the hairs feel silky-smooth and look shiny silver? Or does the plant feel slightly sticky instead (like tiny glue drops)?",
        optionA: "YES — silky and shiny silver hairs; I am in the Taurus Mountains in S Turkey",
        optionB: "NO — plant feels slightly sticky/gummy; I am on a dry open hillside",
        nextA: .species(9),
        nextB: .species(3)
    ),

    KeyStep(
        id: "k5",
        question: "Are the LEAVES very NARROW and long, like willow tree leaves?",
        hint: "Look at a single leaf. Is it much longer than it is wide — like a thin strap or ribbon? Compare it to a normal oval leaf. Are you near mountain streams in eastern Turkey?",
        optionA: "YES — very narrow strap-like leaves (much longer than wide); E Turkey near streams",
        optionB: "NO — leaves are broader — oval or oblong in shape",
        nextA: .species(8),
        nextB: .nextStep("k6")
    ),

    KeyStep(
        id: "k6",
        question: "Can you see LONG CREEPING STEMS running along the ground?",
        hint: "Look around the base of the plant. Are there stems creeping across the soil surface making new baby plants? (Like a strawberry plant does.) Are you in the Black Sea region?",
        optionA: "YES — long creeping stems running across the ground making new plants; Black Sea region",
        optionB: "NO — no creeping stems; the plant grows as a normal upright clump",
        nextA: .species(5),
        nextB: .nextStep("k7")
    ),

    KeyStep(
        id: "k7",
        question: "Do the LEAVES look GREY-GREEN (not bright green) because of very dense hairs?",
        hint: "Look at the overall leaf colour. Are they a dull greyish-green from thick hairs, or a normal bright green?",
        optionA: "YES — leaves look grey-green because of very dense hairs; no creeping stems",
        optionB: "NO — leaves are green or shiny, not grey-green",
        nextA: .species(6),
        nextB: .nextStep("k8")
    ),

    KeyStep(
        id: "k8",
        question: "Are you in S or SE Turkey — the Cilicia region around Adana or Mersin?",
        hint: "Eastern Bugle (A. orientalis) is the most common blue Ajuga across most of Turkey. Post's Bugle (A. postii) lives mainly in SE Turkey. Which fits you?",
        optionA: "YES — I am in S or SE Turkey (Adana / Mersin / Hatay / Cilicia area)",
        optionB: "NO — I am in N, C, E, or W Turkey (or I am not sure)",
        nextA: .species(10),
        nextB: .species(4)
    ),
]

// Helper functions to find a step or species by id
func findKeyStep(_ id: String) -> KeyStep? { keySteps.first { $0.id == id } }
func findAjuga(_ id: Int) -> AjugaSpecies? { allAjuga.first { $0.id == id } }

// ============================================================
// MARK: - PHOTO STORAGE
//
// Photos are saved as JPEG files in the app's Documents folder
// so they survive app restarts and are kept on your iPad.
// ObservableObject means SwiftUI will redraw views when photos change.
// ============================================================

class PhotoStore: ObservableObject {
    @Published var photos: [Int: UIImage] = [:]

    init() { loadAll() }

    // Where a photo file lives on disk
    private func photoURL(for id: Int) -> URL {
        let docs = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        return docs.appendingPathComponent("ajuga_photo_\(id).jpg")
    }

    func hasPhoto(for id: Int) -> Bool { photos[id] != nil }

    // Save a new photo (or replace the old one)
    func save(_ image: UIImage, for id: Int) {
        photos[id] = image
        if let data = image.jpegData(compressionQuality: 0.85) {
            try? data.write(to: photoURL(for: id))
        }
    }

    // Delete a photo
    func delete(for id: Int) {
        photos.removeValue(forKey: id)
        try? FileManager.default.removeItem(at: photoURL(for: id))
    }

    // Load all saved photos when the app starts
    private func loadAll() {
        for sp in allAjuga {
            let url = photoURL(for: sp.id)
            if let data = try? Data(contentsOf: url),
               let img = UIImage(data: data) {
                photos[sp.id] = img
            }
        }
    }
}

// ============================================================
// MARK: - APP ENTRY POINT
// @main tells Swift "this is where the app starts"
// ============================================================

@main
struct AjugaTurkeyApp: App {
    // @StateObject creates the PhotoStore once and keeps it alive
    @StateObject private var store = PhotoStore()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(store)   // share the store with all views
        }
    }
}

// ============================================================
// MARK: - CONTENT VIEW (the tab bar at the bottom)
// ============================================================

struct ContentView: View {
    var body: some View {
        TabView {
            BrowseView()
                .tabItem { Label("Browse", systemImage: "list.bullet") }

            IdentifyView()
                .tabItem { Label("Identify", systemImage: "questionmark.circle") }

            SearchView()
                .tabItem { Label("Search", systemImage: "magnifyingglass") }

            AboutView()
                .tabItem { Label("About", systemImage: "info.circle") }
        }
        .tint(.green)
    }
}

// ============================================================
// MARK: - BROWSE VIEW
// Shows all 10 species as a scrollable list.
// Tap any row to open the full species detail sheet.
// ============================================================

struct BrowseView: View {
    @EnvironmentObject var store: PhotoStore
    @State private var selected: AjugaSpecies? = nil

    // How many photos have been added?
    var photoCount: Int { allAjuga.filter { store.hasPhoto(for: $0.id) }.count }

    var body: some View {
        NavigationStack {
            List(allAjuga) { sp in
                Button { selected = sp } label: {
                    HStack(spacing: 12) {

                        // Photo thumbnail (or emoji placeholder)
                        if let img = store.photos[sp.id] {
                            Image(uiImage: img)
                                .resizable()
                                .scaledToFill()
                                .frame(width: 56, height: 56)
                                .clipShape(RoundedRectangle(cornerRadius: 10))
                        } else {
                            ZStack {
                                RoundedRectangle(cornerRadius: 10)
                                    .fill(Color.secondary.opacity(0.12))
                                    .frame(width: 56, height: 56)
                                Text(sp.flowerEmoji)
                                    .font(.system(size: 28))
                            }
                        }

                        VStack(alignment: .leading, spacing: 3) {
                            Text(sp.name)
                                .font(.subheadline.italic())
                                .foregroundStyle(.primary)
                            Text(sp.nickname)
                                .font(.caption)
                                .foregroundStyle(.secondary)
                            Text(sp.howToSpotIt)
                                .font(.caption2)
                                .foregroundStyle(.secondary)
                                .lineLimit(2)
                        }

                        Spacer()

                        // Tick if photo added
                        if store.hasPhoto(for: sp.id) {
                            Image(systemName: "checkmark.circle.fill")
                                .foregroundStyle(.green)
                                .font(.subheadline)
                        }
                    }
                    .padding(.vertical, 4)
                }
                .buttonStyle(.plain)
            }
            .navigationTitle("🌿 Ajuga of Turkey")
            .navigationSubtitle("10 species — P.H. Davis (1982)")
            .safeAreaInset(edge: .bottom) {
                // Photo progress bar at the bottom
                VStack(spacing: 4) {
                    ProgressView(value: Double(photoCount), total: 10)
                        .tint(.green)
                    Text("Photos: \(photoCount) of 10 species")
                        .font(.caption2)
                        .foregroundStyle(.secondary)
                }
                .padding(.horizontal)
                .padding(.vertical, 8)
                .background(.ultraThinMaterial)
            }
            .sheet(item: $selected) { sp in
                SpeciesDetailView(species: sp)
            }
        }
    }
}

// ============================================================
// MARK: - SPECIES DETAIL VIEW
// Full information about one species, with photo upload.
// ============================================================

struct SpeciesDetailView: View {
    let species: AjugaSpecies
    @EnvironmentObject var store: PhotoStore

    // photoPickerItem is a temporary holder for the photo being picked
    @State private var photoPickerItem: PhotosPickerItem? = nil
    @Environment(\.dismiss) var dismiss

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 0) {

                    // 1. Photo (or add-photo button)
                    photoSection

                    // 2. Name header
                    VStack(alignment: .leading, spacing: 6) {
                        Text(species.name)
                            .font(.title2.bold().italic())
                        Text(species.nickname)
                            .font(.title3)
                            .foregroundStyle(.secondary)
                        Label(species.turkish, systemImage: "flag")
                            .font(.subheadline)
                            .foregroundStyle(.green)
                    }
                    .padding()

                    Divider()

                    // 3. Quick facts grid
                    quickFactsGrid
                        .padding()

                    Divider()

                    // 4. Detail cards
                    VStack(spacing: 12) {
                        infoCard(
                            title: "🍃 What do the leaves look like?",
                            text: species.leafShape
                        )
                        infoCard(
                            title: "✋ Is it hairy? What kind?",
                            text: species.hairiness
                        )
                        infoCard(
                            title: "⭐ How to spot it quickly",
                            text: species.howToSpotIt,
                            highlight: true
                        )
                        infoCard(
                            title: "💡 Fun fact",
                            text: species.funFact,
                            background: Color.yellow.opacity(0.12)
                        )
                    }
                    .padding()

                    // Source credit
                    Text("Source: Flora of Turkey, Vol. 7 — P.H. Davis (1982)")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                        .padding()
                }
            }
            .navigationTitle(species.nickname)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Close") { dismiss() }
                }
            }
        }
    }

    // ---- Photo Section ----

    @ViewBuilder
    var photoSection: some View {
        if let img = store.photos[species.id] {
            // Show existing photo with Replace / Delete buttons
            ZStack(alignment: .bottomTrailing) {
                Image(uiImage: img)
                    .resizable()
                    .scaledToFill()
                    .frame(maxWidth: .infinity)
                    .frame(height: 280)
                    .clipped()

                HStack(spacing: 8) {
                    PhotosPicker(selection: $photoPickerItem, matching: .images) {
                        Label("Replace", systemImage: "arrow.triangle.2.circlepath")
                            .font(.caption.bold())
                            .padding(.horizontal, 10).padding(.vertical, 6)
                            .background(.ultraThinMaterial)
                            .clipShape(Capsule())
                    }
                    .onChange(of: photoPickerItem) { _, item in loadPhoto(item) }

                    Button(role: .destructive) {
                        store.delete(for: species.id)
                    } label: {
                        Label("Delete", systemImage: "trash")
                            .font(.caption.bold())
                            .padding(.horizontal, 10).padding(.vertical, 6)
                            .background(.ultraThinMaterial)
                            .clipShape(Capsule())
                    }
                }
                .padding(12)
            }

        } else {
            // No photo yet — show a big "Add photo" button
            PhotosPicker(selection: $photoPickerItem, matching: .images) {
                ZStack {
                    Rectangle()
                        .fill(Color.secondary.opacity(0.08))
                        .frame(maxWidth: .infinity)
                        .frame(height: 200)
                    VStack(spacing: 10) {
                        Image(systemName: "camera.badge.plus")
                            .font(.system(size: 50))
                            .foregroundStyle(.secondary)
                        Text("Add a photo")
                            .font(.headline)
                            .foregroundStyle(.secondary)
                        Text("Tap to pick from your Photos library")
                            .font(.caption)
                            .foregroundStyle(.tertiary)
                    }
                }
            }
            .onChange(of: photoPickerItem) { _, item in loadPhoto(item) }
        }
    }

    // Load photo from the picker (runs in background so the UI stays smooth)
    func loadPhoto(_ item: PhotosPickerItem?) {
        guard let item else { return }
        Task {
            if let data = try? await item.loadTransferable(type: Data.self),
               let image = UIImage(data: data) {
                await MainActor.run {
                    store.save(image, for: species.id)
                    photoPickerItem = nil
                }
            }
        }
    }

    // ---- Quick Facts Grid ----

    var quickFactsGrid: some View {
        LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 10) {
            factTile(label: "FLOWER COLOUR", value: "\(species.flowerEmoji) \(species.flowerColour)")
            factTile(label: "SIZE", value: "📏 \(species.size)")
            factTile(label: "FLOWERS IN", value: "📅 \(species.whenItFlowers)")
            factTile(label: "LIFESPAN", value: "⏳ \(species.lifespan)")
            factTile(label: "WHERE IT GROWS", value: "📍 \(species.whereItGrows)")
                .gridCellColumns(2)
        }
    }

    func factTile(label: String, value: String) -> some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(label)
                .font(.caption2.bold())
                .foregroundStyle(.secondary)
            Text(value)
                .font(.caption)
                .fixedSize(horizontal: false, vertical: true)
        }
        .padding(10)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color.secondary.opacity(0.08))
        .clipShape(RoundedRectangle(cornerRadius: 10))
    }

    // ---- Info Card ----

    func infoCard(title: String, text: String,
                  highlight: Bool = false,
                  background: Color = Color.secondary.opacity(0.08)) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(title)
                .font(.subheadline.bold())
            Text(text)
                .font(.body)
                .fixedSize(horizontal: false, vertical: true)
        }
        .padding(14)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(highlight ? Color.green.opacity(0.12) : background)
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .overlay(
            RoundedRectangle(cornerRadius: 12)
                .stroke(highlight ? Color.green.opacity(0.4) : Color.clear, lineWidth: 1.5)
        )
    }
}

// ============================================================
// MARK: - IDENTIFY VIEW (step-by-step dichotomous key)
// ============================================================

struct IdentifyView: View {
    @State private var stepID = "k1"        // which question we are on
    @State private var result: AjugaSpecies? = nil   // final answer
    @State private var history: [String] = []        // steps we have visited (for Back button)

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {

                if let result {
                    ResultView(species: result)
                } else if let step = findKeyStep(stepID) {
                    KeyStepView(step: step) { answer in
                        history.append(stepID)
                        switch answer {
                        case .nextStep(let id): stepID = id
                        case .species(let id): result = findAjuga(id)
                        }
                    }
                }

                Divider()

                // Back and Restart buttons
                HStack(spacing: 12) {
                    if !history.isEmpty && result == nil {
                        Button("← Back one step") {
                            stepID = history.removeLast()
                        }
                        .buttonStyle(.bordered)
                    }
                    Button("🔄 Start again") {
                        stepID = "k1"
                        result = nil
                        history = []
                    }
                    .buttonStyle(.borderedProminent)
                    .tint(.green)
                }
                .padding()
            }
            .navigationTitle("🔑 Identify My Plant")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

// ---- One question step ----

struct KeyStepView: View {
    let step: KeyStep
    let onAnswer: (KeyResult) -> Void

    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                // Question box
                VStack(spacing: 10) {
                    Text(step.question)
                        .font(.title3.bold())
                        .multilineTextAlignment(.center)
                    Text(step.hint)
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                }
                .padding(20)
                .background(Color.yellow.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 16))
                .overlay(
                    RoundedRectangle(cornerRadius: 16)
                        .stroke(Color.orange.opacity(0.3), lineWidth: 1.5)
                )
                .padding(.horizontal)

                // Two answer buttons
                VStack(spacing: 12) {
                    answerButton(label: step.optionA, colour: .green) {
                        onAnswer(step.nextA)
                    }
                    answerButton(label: step.optionB, colour: .purple) {
                        onAnswer(step.nextB)
                    }
                }
                .padding(.horizontal)
            }
            .padding(.vertical, 20)
        }
    }

    func answerButton(label: String, colour: Color, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            Text(label)
                .font(.body)
                .multilineTextAlignment(.center)
                .padding(16)
                .frame(maxWidth: .infinity)
                .background(colour.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 14))
                .overlay(
                    RoundedRectangle(cornerRadius: 14)
                        .stroke(colour.opacity(0.35), lineWidth: 1.5)
                )
        }
        .buttonStyle(.plain)
    }
}

// ---- Result (when the key has found the species) ----

struct ResultView: View {
    let species: AjugaSpecies
    @EnvironmentObject var store: PhotoStore
    @State private var showDetail = false

    var body: some View {
        ScrollView {
            VStack(spacing: 16) {
                // Success banner
                VStack(spacing: 8) {
                    Text("✅").font(.system(size: 52))
                    Text("Your plant is most likely:")
                        .font(.subheadline).foregroundStyle(.secondary)
                    Text(species.name)
                        .font(.title2.bold().italic())
                        .multilineTextAlignment(.center)
                    Text(species.nickname)
                        .font(.title3)
                    Label(species.turkish, systemImage: "flag")
                        .font(.subheadline).foregroundStyle(.green)
                }
                .padding(20)
                .frame(maxWidth: .infinity)
                .background(Color.green.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 16))
                .overlay(RoundedRectangle(cornerRadius: 16).stroke(Color.green.opacity(0.4), lineWidth: 1.5))
                .padding(.horizontal)

                // Quick facts
                VStack(alignment: .leading, spacing: 8) {
                    factRow("Flower:", "\(species.flowerEmoji) \(species.flowerColour)")
                    factRow("Size:", species.size)
                    factRow("Flowers:", species.whenItFlowers)
                    factRow("Grows:", species.whereItGrows)
                }
                .padding()
                .background(Color.secondary.opacity(0.06))
                .clipShape(RoundedRectangle(cornerRadius: 14))
                .padding(.horizontal)

                // How to spot it
                VStack(alignment: .leading, spacing: 6) {
                    Text("⭐ How to spot it").font(.subheadline.bold())
                    Text(species.howToSpotIt).font(.body)
                }
                .padding()
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Color.green.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 14))
                .padding(.horizontal)

                // Fun fact
                VStack(alignment: .leading, spacing: 6) {
                    Text("💡 Fun fact").font(.subheadline.bold())
                    Text(species.funFact).font(.body)
                }
                .padding()
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Color.yellow.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 14))
                .padding(.horizontal)

                // Open full detail button
                Button("See full details & add a photo →") { showDetail = true }
                    .buttonStyle(.borderedProminent)
                    .tint(.green)
                    .padding(.bottom)
            }
            .padding(.vertical)
        }
        .sheet(isPresented: $showDetail) {
            SpeciesDetailView(species: species)
        }
    }

    func factRow(_ label: String, _ value: String) -> some View {
        HStack(alignment: .top, spacing: 8) {
            Text(label)
                .font(.subheadline.bold())
                .frame(width: 72, alignment: .leading)
            Text(value)
                .font(.subheadline)
                .fixedSize(horizontal: false, vertical: true)
        }
    }
}

// ============================================================
// MARK: - SEARCH VIEW
// ============================================================

struct SearchView: View {
    @EnvironmentObject var store: PhotoStore
    @State private var query = ""
    @State private var selected: AjugaSpecies? = nil

    // Filter species by any word matching any field
    var results: [AjugaSpecies] {
        let q = query.trimmingCharacters(in: .whitespaces).lowercased()
        guard !q.isEmpty else { return [] }
        return allAjuga.filter { sp in
            [sp.name, sp.nickname, sp.turkish, sp.flowerColour,
             sp.leafShape, sp.hairiness, sp.whereItGrows,
             sp.whenItFlowers, sp.funFact, sp.howToSpotIt, sp.lifespan]
                .joined(separator: " ").lowercased().contains(q)
        }
    }

    var body: some View {
        NavigationStack {
            List {
                Section {
                    TextField("yellow, woolly, Black Sea, silky, Taurus…", text: $query)
                        .autocorrectionDisabled()
                }

                if query.trimmingCharacters(in: .whitespaces).isEmpty {
                    // Quick reference when nothing typed
                    Section("All 10 species — quick reference") {
                        ForEach(allAjuga) { sp in
                            quickRow(sp)
                        }
                    }
                } else if results.isEmpty {
                    Section {
                        Text("Nothing found for '\(query)'.\nTry: yellow, blue, woolly, silky, sticky, Taurus, annual, perennial, Black Sea, creeping.")
                            .foregroundStyle(.secondary)
                            .font(.subheadline)
                    }
                } else {
                    Section("Found \(results.count) result(s) for '\(query)'") {
                        ForEach(results) { sp in
                            quickRow(sp)
                        }
                    }
                }
            }
            .navigationTitle("🔎 Search")
            .sheet(item: $selected) { sp in
                SpeciesDetailView(species: sp)
            }
        }
    }

    func quickRow(_ sp: AjugaSpecies) -> some View {
        Button { selected = sp } label: {
            VStack(alignment: .leading, spacing: 4) {
                Text("\(sp.flowerEmoji) \(sp.name)")
                    .font(.subheadline.italic())
                    .foregroundStyle(.primary)
                HStack {
                    Text(sp.nickname)
                    if store.hasPhoto(for: sp.id) {
                        Text("✅")
                    }
                }
                .font(.caption)
                .foregroundStyle(.secondary)
                Text(sp.howToSpotIt)
                    .font(.caption2)
                    .foregroundStyle(.secondary)
            }
            .padding(.vertical, 4)
        }
        .buttonStyle(.plain)
    }
}

// ============================================================
// MARK: - ABOUT VIEW
// ============================================================

struct AboutView: View {
    var body: some View {
        NavigationStack {
            List {
                Section {
                    VStack(spacing: 12) {
                        Text("🌿").font(.system(size: 60))
                        Text("Ajuga of Turkey").font(.title2.bold())
                        Text("10 species from P.H. Davis — Flora of Turkey Vol. 7 (1982)\nWritten in plain English so anyone can use it!")
                            .font(.subheadline)
                            .multilineTextAlignment(.center)
                            .foregroundStyle(.secondary)
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 8)
                }

                Section("What is Ajuga?") {
                    Text("""
Ajuga (called 'Bugle' in English) is a group of flowering plants in the mint family (Lamiaceae, also written Labiatae).

All Ajuga have a special flower shape: the upper lip is either very tiny or missing completely, and the lower lip is large with 3 lobes. This makes them look quite different from most other flowers!

Turkey is one of the richest countries in the world for Ajuga — 10 species grow here, from sea level all the way up to 2,500 m in the mountains.
""")
                    .font(.body)
                }

                Section("How to use this app") {
                    Label("Browse — see all 10 species, add your own photos", systemImage: "list.bullet")
                    Label("Identify — answer simple questions to name your plant", systemImage: "questionmark.circle")
                    Label("Search — type any word to find matching species", systemImage: "magnifyingglass")
                    Label("Photos are saved permanently on your iPad", systemImage: "photo.badge.checkmark")
                }

                Section("What is a dichotomous key?") {
                    Text("""
The Identify tab uses a 'dichotomous key'. 'Dichotomous' just means 'splits into two choices'. You are asked a series of yes/no (A or B) questions. Each answer narrows it down until you reach the right species.

Botanists have used this method for hundreds of years! The key in this app is a simplified version of the one in Flora of Turkey.
""")
                    .font(.body)
                }

                Section("Source") {
                    VStack(alignment: .leading, spacing: 4) {
                        Text("Flora of Turkey and the East Aegean Islands")
                            .font(.body.bold())
                        Text("Volume 7 — edited by P.H. Davis (1982)")
                            .font(.subheadline)
                        Text("Edinburgh University Press")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                    .padding(.vertical, 4)
                }
            }
            .navigationTitle("ℹ️ About")
        }
    }
}
