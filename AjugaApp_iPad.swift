// ============================================================
// AJUGA OF TURKEY — iPad App (Swift Playgrounds 4)
//
// Based on: Flora of Turkey, Vol. 7 — P.H. Davis (1982)
// Written in plain English — 14-year-old friendly!
//
// HOW TO USE:
//   1. Open Swift Playgrounds on your iPad
//   2. Tap + → App Playground → Create
//   3. Tap the default file in the sidebar
//   4. SELECT ALL and DELETE everything
//   5. Paste THIS entire file
//   6. Tap Run ▶
//
// Photos are saved permanently on your iPad.
// ============================================================

import SwiftUI
import PhotosUI

// ============================================================
// MARK: - DATA MODEL
// A 'struct' is a box that holds related information together.
// ============================================================

struct AjugaSpecies: Identifiable {
    let id: Int
    let name: String            // Latin scientific name
    let nickname: String        // Plain English name
    let turkish: String         // Turkish name
    let size: String
    let lifespan: String        // Annual / perennial
    let flowerColour: String
    let flowerEmoji: String     // 🟡 or 💜
    let leafShape: String
    let hairiness: String
    let whereItGrows: String
    let whenItFlowers: String
    let howToSpotIt: String     // one-line ID tip
    let funFact: String
}

// ============================================================
// MARK: - ALL 10 SPECIES
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
        flowerColour: "Yellow, often with red-purple streaks",
        flowerEmoji: "🟡",
        leafShape: "Deeply cut into 3 narrow finger-like strips — looks like a tiny pine seedling! Crush a leaf and it smells like pine trees.",
        hairiness: "Hairy all over",
        whereItGrows: "Arable fields, rocky hillsides, disturbed ground. All over Turkey, especially W, C, S Anatolia. 0–1800 m.",
        whenItFlowers: "March to July",
        howToSpotIt: "Yellow flowers + 3 pine-needle-like leaf strips + smells of pine when crushed",
        funFact: "The most common Ajuga in Turkey! Its pine smell is how it got the name Ground Pine — even though it is not related to pine trees at all."
    ),

    AjugaSpecies(
        id: 2,
        name: "Ajuga chamaepitys subsp. chia",
        nickname: "Chian Ground Pine",
        turkish: "Sakız mayasıl otu",
        size: "5–20 cm tall",
        lifespan: "Annual — lives just one year",
        flowerColour: "Yellow, sometimes with purple streaks",
        flowerEmoji: "🟡",
        leafShape: "Like subsp. chamaepitys (3 strips) but the strips are SHORTER and WIDER. Still smells like pine.",
        hairiness: "Hairy",
        whereItGrows: "Dry rocky hillsides. W and SW Turkey — Aegean coast and islands. 0–1000 m.",
        whenItFlowers: "March to June",
        howToSpotIt: "Yellow flowers + shorter stubbier leaf strips + coastal W Turkey near the Aegean",
        funFact: "'Chia' refers to the Greek island of Chios, right next to the Turkish coast where this plant mainly lives."
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
        leafShape: "Simple oblong leaves with slightly wavy edges — NOT cut into strips like Ground Pine. No pine smell.",
        hairiness: "Covered in sticky glandular hairs — feels slightly sticky, like tiny glue dots",
        whereItGrows: "Dry open hillsides, rocky slopes. W, S, and C Turkey. 0–1500 m.",
        whenItFlowers: "March to June",
        howToSpotIt: "Yellow flowers + simple whole leaves (not cut) + feels slightly sticky + no pine smell",
        funFact: "Those sticky hairs can trap tiny insects! Used in Turkish folk medicine for skin conditions for hundreds of years."
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
        leafShape: "Oval leaves with scalloped (wavy) edges. Big leaves at the base, smaller ones higher up.",
        hairiness: "Softly hairy — feels gentle to touch",
        whereItGrows: "Meadows, forest clearings, stream sides. All over Turkey — very common in N, E, C Anatolia. 200–2200 m.",
        whenItFlowers: "April to July",
        howToSpotIt: "Blue-violet flowers + soft oval leaves + very widespread across Turkey — the most common blue Ajuga",
        funFact: "You are very likely to see this one! It can form huge carpets of blue-violet flowers in mountain meadows in spring."
    ),

    AjugaSpecies(
        id: 5,
        name: "Ajuga reptans",
        nickname: "Creeping Bugle",
        turkish: "Sürünücü mayasıl otu",
        size: "10–30 cm tall",
        lifespan: "Perennial — lives for many years",
        flowerColour: "Blue-violet (rarely pink or white)",
        flowerEmoji: "💜",
        leafShape: "Shiny oval leaves with wavy edges. Leaves near the ground are often bronze-purple coloured.",
        hairiness: "Slightly hairy on the stem; leaves fairly smooth and shiny",
        whereItGrows: "Damp meadows, shaded woodland edges. N and NW Turkey — mainly the Black Sea coast. 0–1500 m.",
        whenItFlowers: "April to June",
        howToSpotIt: "Blue-violet flowers + LONG CREEPING RUNNERS along the ground (like strawberry plants!) + Black Sea region",
        funFact: "The ONLY Turkish Ajuga that sends out long creeping stems (stolons) across the ground — just like a strawberry plant! Each runner makes a new plant."
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
        leafShape: "Oval leaves with coarse teeth. Looks grey-green because of dense hairs.",
        hairiness: "Densely hairy — makes the whole plant look grey-green instead of bright green",
        whereItGrows: "Dry grassland, meadows, roadsides. N, W, and C Turkey. 500–2000 m.",
        whenItFlowers: "April to June",
        howToSpotIt: "Blue-violet flowers + grey-green hairy leaves + NO creeping runners",
        funFact: "Looks similar to Creeping Bugle but has no creeping stems at all. 'Genevensis' means 'from Geneva', Switzerland."
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
        leafShape: "Oblong leaves with smooth or slightly wavy edges. Covered in such thick white woolly hairs it looks almost white!",
        hairiness: "VERY densely white-woolly — like the plant is wrapped in cotton wool",
        whereItGrows: "Dry stony slopes, steppe grassland. C, E, and SE Turkey — drier inland areas. 600–2000 m.",
        whenItFlowers: "May to July",
        howToSpotIt: "Pale yellow flowers + VERY thick white woolly covering all over — unmistakable once you see it",
        funFact: "The wooliest Ajuga in Turkey! The thick white wool acts like sunscreen and insulation for the scorching hot summers of central Anatolia."
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
        leafShape: "VERY NARROW long leaves that look just like willow tree leaves — unlike any other Ajuga! Smooth or faintly toothed edges.",
        hairiness: "Lightly hairy",
        whereItGrows: "Mountain meadows, stream sides. E and NE Turkey — Pontic mountains near the Black Sea. 800–2500 m.",
        whenItFlowers: "June to August",
        howToSpotIt: "Blue-violet flowers + VERY NARROW willow-like leaves + mountain streams in E Turkey",
        funFact: "'Salicifolia' means 'willow-leaved' in Latin. Those narrow strap-like leaves make it impossible to confuse with any other Ajuga."
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
        leafShape: "Oval-spoon shaped with smooth edges. Completely covered in LONG SHINY SILVER HAIRS that feel like a silk scarf.",
        hairiness: "Long silky silver hairs — soft, shiny, and beautiful",
        whereItGrows: "Limestone rocks, cliffs, rocky slopes in the Taurus Mountains. S Turkey only. 500–2000 m.",
        whenItFlowers: "April to June",
        howToSpotIt: "Pale yellow/white flowers + SILKY SILVER SHEEN all over + Taurus Mountains (S Turkey only)",
        funFact: "'Bombycina' is the Latin word for silkworm! It ONLY grows in Turkey's Taurus Mountains — nowhere else on Earth."
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
        leafShape: "Oval to spoon-shaped leaves with rounded teeth. Moderately hairy. Similar to Eastern Bugle but smaller.",
        hairiness: "Moderately hairy",
        whereItGrows: "Rocky hillsides, scrubby areas, forest margins. S and SE Turkey — Cilicia region (Adana, Mersin). 200–1500 m.",
        whenItFlowers: "March to May",
        howToSpotIt: "Blue-violet flowers + oval toothed leaves + only in SE Turkey (Adana/Mersin/Cilicia area)",
        funFact: "Named after Georg Post, a botanist who explored Middle Eastern plants on horseback in the 1800s."
    ),
]

// ============================================================
// MARK: - KEY DATA
// A dichotomous key = a series of A-or-B questions.
// 'Dichotomous' just means 'splits into two choices'.
// Follow the questions and you reach the right species!
// ============================================================

enum KeyResult {
    case nextStep(String)   // go to another question
    case species(Int)       // found it — this is the species id
}

struct KeyStep: Identifiable {
    let id: String
    let question: String
    let hint: String
    let optionA: String
    let optionB: String
    let nextA: KeyResult
    let nextB: KeyResult
}

let keySteps: [KeyStep] = [
    KeyStep(
        id: "k1",
        question: "What colour are the FLOWERS?",
        hint: "Look at the petals. Are they yellow/cream, or blue/purple?",
        optionA: "🟡  Yellow or creamy-white",
        optionB: "💜  Blue or blue-violet",
        nextA: .nextStep("k2"),
        nextB: .nextStep("k5")
    ),
    KeyStep(
        id: "k2",
        question: "Are the LEAVES deeply cut into 3 narrow finger-like strips?",
        hint: "Is the leaf cut almost all the way to the stalk into 3 thin strips? Does it smell of pine when you crush it?",
        optionA: "YES — 3 narrow strips, smells of pine when crushed",
        optionB: "NO — leaves are whole (not cut into strips), no pine smell",
        nextA: .nextStep("k3"),
        nextB: .nextStep("k4")
    ),
    KeyStep(
        id: "k3",
        question: "Are the 3 leaf strips SHORT and STUBBY (not long and thin)?",
        hint: "Short and fat, or long and thin like pine needles? Are you near the Aegean coast?",
        optionA: "YES — short and stubby strips; I am in W/SW Turkey near the Aegean",
        optionB: "NO — long and thin strips; I could be anywhere in Turkey",
        nextA: .species(2),
        nextB: .species(1)
    ),
    KeyStep(
        id: "k4",
        question: "Is the whole plant covered in THICK WHITE WOOLLY hairs?",
        hint: "Does the plant look almost white or silver-grey from very thick fluffy hairs — like a woolly jumper?",
        optionA: "YES — very thick woolly white hairs, plant looks almost white",
        optionB: "NO — hairs are silky/silver, OR the plant feels slightly sticky",
        nextA: .species(7),
        nextB: .nextStep("k4b")
    ),
    KeyStep(
        id: "k4b",
        question: "Do the hairs feel SILKY SMOOTH and look SHINY SILVER?",
        hint: "Touch it gently. Silky smooth and shiny? Or does it feel slightly sticky (like tiny glue drops)?",
        optionA: "YES — silky shiny silver hairs; I am in the Taurus Mountains, S Turkey",
        optionB: "NO — plant feels slightly sticky; I am on a dry open hillside",
        nextA: .species(9),
        nextB: .species(3)
    ),
    KeyStep(
        id: "k5",
        question: "Are the LEAVES very NARROW and long, like willow tree leaves?",
        hint: "Is the leaf much longer than wide — like a thin strap? Are you near mountain streams in E Turkey?",
        optionA: "YES — very narrow strap-like leaves; E Turkey near streams",
        optionB: "NO — leaves are broader, oval or oblong",
        nextA: .species(8),
        nextB: .nextStep("k6")
    ),
    KeyStep(
        id: "k6",
        question: "Can you see LONG CREEPING STEMS running along the ground?",
        hint: "Are there stems creeping across the soil making new baby plants, like strawberry runners? Black Sea region?",
        optionA: "YES — long creeping stems along the ground; Black Sea region",
        optionB: "NO — no creeping stems; plant grows as an upright clump",
        nextA: .species(5),
        nextB: .nextStep("k7")
    ),
    KeyStep(
        id: "k7",
        question: "Do the LEAVES look GREY-GREEN (not bright green) from dense hairs?",
        hint: "Are the leaves a dull greyish-green colour from thick hairs, rather than normal bright green?",
        optionA: "YES — leaves look grey-green from very dense hairs; no creeping stems",
        optionB: "NO — leaves are green or shiny, not grey-green",
        nextA: .species(6),
        nextB: .nextStep("k8")
    ),
    KeyStep(
        id: "k8",
        question: "Are you in S or SE Turkey — the Cilicia region (Adana, Mersin, Hatay)?",
        hint: "Eastern Bugle is found all over Turkey. Post's Bugle is mainly in the SE Cilicia region.",
        optionA: "YES — I am in S or SE Turkey (Adana / Mersin / Hatay / Cilicia area)",
        optionB: "NO — I am in N, C, E, or W Turkey (or I am not sure)",
        nextA: .species(10),
        nextB: .species(4)
    ),
]

func findKeyStep(_ id: String) -> KeyStep? {
    keySteps.first { $0.id == id }
}

func findAjuga(_ id: Int) -> AjugaSpecies? {
    allAjuga.first { $0.id == id }
}

// ============================================================
// MARK: - PHOTO STORAGE
// ObservableObject lets SwiftUI redraw views when photos change.
// Photos are saved as JPEG files in the app's Documents folder.
// ============================================================

class PhotoStore: ObservableObject {
    @Published var photos: [Int: UIImage] = [:]

    init() {
        loadAll()
    }

    private func photoURL(for id: Int) -> URL {
        let docs = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        return docs.appendingPathComponent("ajuga_\(id).jpg")
    }

    func hasPhoto(for id: Int) -> Bool {
        return photos[id] != nil
    }

    func save(_ image: UIImage, for id: Int) {
        photos[id] = image
        if let data = image.jpegData(compressionQuality: 0.85) {
            try? data.write(to: photoURL(for: id))
        }
    }

    func delete(for id: Int) {
        photos.removeValue(forKey: id)
        try? FileManager.default.removeItem(at: photoURL(for: id))
    }

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
    @StateObject private var store = PhotoStore()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(store)
        }
    }
}

// ============================================================
// MARK: - CONTENT VIEW
// ============================================================

struct ContentView: View {
    var body: some View {
        TabView {
            BrowseView()
                .tabItem {
                    Label("Browse", systemImage: "list.bullet")
                }
            IdentifyView()
                .tabItem {
                    Label("Identify", systemImage: "questionmark.circle")
                }
            SearchView()
                .tabItem {
                    Label("Search", systemImage: "magnifyingglass")
                }
            AboutView()
                .tabItem {
                    Label("About", systemImage: "info.circle")
                }
        }
        .tint(.green)
    }
}

// ============================================================
// MARK: - BROWSE VIEW
// ============================================================

struct BrowseView: View {
    @EnvironmentObject var store: PhotoStore
    @State private var selected: AjugaSpecies? = nil

    var photoCount: Int {
        allAjuga.filter { store.hasPhoto(for: $0.id) }.count
    }

    var body: some View {
        NavigationStack {
            List(allAjuga) { sp in
                Button {
                    selected = sp
                } label: {
                    BrowseRow(species: sp)
                }
                .buttonStyle(.plain)
            }
            .navigationTitle("🌿 Ajuga of Turkey")
            .safeAreaInset(edge: .bottom) {
                PhotoProgress(count: photoCount, total: 10)
            }
            .sheet(item: $selected) { sp in
                SpeciesDetailView(species: sp)
            }
        }
    }
}

// Extracted row to help the compiler — keeps BrowseView body simple
struct BrowseRow: View {
    @EnvironmentObject var store: PhotoStore
    let species: AjugaSpecies

    var body: some View {
        HStack(spacing: 12) {
            SpeciesThumbnail(species: species)
            VStack(alignment: .leading, spacing: 3) {
                Text(species.name)
                    .font(.subheadline.italic())
                    .foregroundStyle(.primary)
                Text(species.nickname)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Text(species.howToSpotIt)
                    .font(.caption2)
                    .foregroundStyle(.secondary)
                    .lineLimit(2)
            }
            Spacer()
            if store.hasPhoto(for: species.id) {
                Image(systemName: "checkmark.circle.fill")
                    .foregroundStyle(.green)
            }
        }
        .padding(.vertical, 4)
    }
}

struct SpeciesThumbnail: View {
    @EnvironmentObject var store: PhotoStore
    let species: AjugaSpecies

    var body: some View {
        if let img = store.photos[species.id] {
            Image(uiImage: img)
                .resizable()
                .scaledToFill()
                .frame(width: 56, height: 56)
                .clipShape(RoundedRectangle(cornerRadius: 10))
        } else {
            ZStack {
                RoundedRectangle(cornerRadius: 10)
                    .fill(Color(.secondarySystemBackground))
                    .frame(width: 56, height: 56)
                Text(species.flowerEmoji)
                    .font(.system(size: 28))
            }
        }
    }
}

struct PhotoProgress: View {
    let count: Int
    let total: Int

    var body: some View {
        VStack(spacing: 4) {
            ProgressView(value: Double(count), total: Double(total))
                .tint(.green)
            Text("Photos added: \(count) of \(total) species")
                .font(.caption2)
                .foregroundStyle(.secondary)
        }
        .padding(.horizontal)
        .padding(.vertical, 8)
        .background(.ultraThinMaterial)
    }
}

// ============================================================
// MARK: - SPECIES DETAIL VIEW
// ============================================================

struct SpeciesDetailView: View {
    let species: AjugaSpecies
    @EnvironmentObject var store: PhotoStore
    @State private var photoPickerItem: PhotosPickerItem? = nil
    @Environment(\.dismiss) var dismiss

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 0) {
                    SpeciesPhotoSection(species: species, photoPickerItem: $photoPickerItem)
                    SpeciesHeader(species: species)
                    Divider()
                    SpeciesFactGrid(species: species)
                        .padding()
                    Divider()
                    SpeciesCards(species: species)
                        .padding()
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
}

// ---- Photo section ----

struct SpeciesPhotoSection: View {
    @EnvironmentObject var store: PhotoStore
    let species: AjugaSpecies
    @Binding var photoPickerItem: PhotosPickerItem?

    var body: some View {
        if store.hasPhoto(for: species.id) {
            ExistingPhotoView(species: species, photoPickerItem: $photoPickerItem)
        } else {
            AddPhotoView(species: species, photoPickerItem: $photoPickerItem)
        }
    }
}

struct ExistingPhotoView: View {
    @EnvironmentObject var store: PhotoStore
    let species: AjugaSpecies
    @Binding var photoPickerItem: PhotosPickerItem?

    var body: some View {
        ZStack(alignment: .bottomTrailing) {
            if let img = store.photos[species.id] {
                Image(uiImage: img)
                    .resizable()
                    .scaledToFill()
                    .frame(maxWidth: .infinity)
                    .frame(height: 280)
                    .clipped()
            }
            PhotoControlButtons(species: species, photoPickerItem: $photoPickerItem)
                .padding(12)
        }
        .onChange(of: photoPickerItem) { _, item in
            loadPhoto(item)
        }
    }

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
}

struct PhotoControlButtons: View {
    @EnvironmentObject var store: PhotoStore
    let species: AjugaSpecies
    @Binding var photoPickerItem: PhotosPickerItem?

    var body: some View {
        HStack(spacing: 8) {
            PhotosPicker(selection: $photoPickerItem, matching: .images) {
                Label("Replace", systemImage: "arrow.triangle.2.circlepath")
                    .font(.caption.bold())
                    .padding(.horizontal, 10)
                    .padding(.vertical, 6)
                    .background(.ultraThinMaterial)
                    .clipShape(Capsule())
            }
            Button(role: .destructive) {
                store.delete(for: species.id)
            } label: {
                Label("Delete", systemImage: "trash")
                    .font(.caption.bold())
                    .padding(.horizontal, 10)
                    .padding(.vertical, 6)
                    .background(.ultraThinMaterial)
                    .clipShape(Capsule())
            }
        }
    }
}

struct AddPhotoView: View {
    @EnvironmentObject var store: PhotoStore
    let species: AjugaSpecies
    @Binding var photoPickerItem: PhotosPickerItem?

    var body: some View {
        PhotosPicker(selection: $photoPickerItem, matching: .images) {
            ZStack {
                Rectangle()
                    .fill(Color(.secondarySystemBackground))
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
        .onChange(of: photoPickerItem) { _, item in
            loadPhoto(item)
        }
    }

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
}

// ---- Name header ----

struct SpeciesHeader: View {
    let species: AjugaSpecies

    var body: some View {
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
    }
}

// ---- Quick facts grid ----

struct SpeciesFactGrid: View {
    let species: AjugaSpecies

    var body: some View {
        LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 10) {
            FactTile(label: "FLOWER", value: "\(species.flowerEmoji) \(species.flowerColour)")
            FactTile(label: "SIZE", value: "📏 \(species.size)")
            FactTile(label: "FLOWERS IN", value: "📅 \(species.whenItFlowers)")
            FactTile(label: "LIFESPAN", value: "⏳ \(species.lifespan)")
            FactTile(label: "WHERE IT GROWS", value: "📍 \(species.whereItGrows)")
                .gridCellColumns(2)
        }
    }
}

struct FactTile: View {
    let label: String
    let value: String

    var body: some View {
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
        .background(Color(.secondarySystemBackground))
        .clipShape(RoundedRectangle(cornerRadius: 10))
    }
}

// ---- Info cards ----

struct SpeciesCards: View {
    let species: AjugaSpecies

    var body: some View {
        VStack(spacing: 12) {
            InfoCard(
                title: "🍃 What do the leaves look like?",
                text: species.leafShape
            )
            InfoCard(
                title: "✋ Is it hairy? What kind?",
                text: species.hairiness
            )
            InfoCard(
                title: "⭐ How to spot it quickly",
                text: species.howToSpotIt,
                highlight: true
            )
            InfoCard(
                title: "💡 Fun fact",
                text: species.funFact,
                background: Color.yellow.opacity(0.12)
            )
        }
    }
}

struct InfoCard: View {
    let title: String
    let text: String
    var highlight: Bool = false
    var background: Color = Color(.secondarySystemBackground)

    var body: some View {
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
// MARK: - IDENTIFY VIEW  (step-by-step dichotomous key)
// ============================================================

struct IdentifyView: View {
    @State private var stepID: String = "k1"
    @State private var result: AjugaSpecies? = nil
    @State private var history: [String] = []

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                if let result = result {
                    KeyResultView(species: result)
                } else if let step = findKeyStep(stepID) {
                    KeyStepView(step: step) { answer in
                        history.append(stepID)
                        switch answer {
                        case .nextStep(let id):
                            stepID = id
                        case .species(let id):
                            result = findAjuga(id)
                        }
                    }
                }

                Divider()

                KeyNavButtons(
                    canGoBack: !history.isEmpty && result == nil,
                    onBack: {
                        stepID = history.removeLast()
                    },
                    onRestart: {
                        stepID = "k1"
                        result = nil
                        history = []
                    }
                )
                .padding()
            }
            .navigationTitle("🔑 Identify My Plant")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct KeyNavButtons: View {
    let canGoBack: Bool
    let onBack: () -> Void
    let onRestart: () -> Void

    var body: some View {
        HStack(spacing: 12) {
            if canGoBack {
                Button("← Back", action: onBack)
                    .buttonStyle(.bordered)
            }
            Button("🔄 Start again", action: onRestart)
                .buttonStyle(.borderedProminent)
                .tint(.green)
        }
    }
}

// ---- One key question ----

struct KeyStepView: View {
    let step: KeyStep
    let onAnswer: (KeyResult) -> Void

    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                KeyQuestionBox(question: step.question, hint: step.hint)

                VStack(spacing: 12) {
                    KeyAnswerButton(
                        label: step.optionA,
                        colour: .green,
                        action: { onAnswer(step.nextA) }
                    )
                    KeyAnswerButton(
                        label: step.optionB,
                        colour: .purple,
                        action: { onAnswer(step.nextB) }
                    )
                }
                .padding(.horizontal)
            }
            .padding(.vertical, 20)
        }
    }
}

struct KeyQuestionBox: View {
    let question: String
    let hint: String

    var body: some View {
        VStack(spacing: 10) {
            Text(question)
                .font(.title3.bold())
                .multilineTextAlignment(.center)
            Text(hint)
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
    }
}

struct KeyAnswerButton: View {
    let label: String
    let colour: Color
    let action: () -> Void

    var body: some View {
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

// ---- Result after key completes ----

struct KeyResultView: View {
    let species: AjugaSpecies
    @State private var showDetail: Bool = false

    var body: some View {
        ScrollView {
            VStack(spacing: 16) {
                ResultBanner(species: species)
                ResultFactBox(species: species)
                ResultSpotBox(species: species)
                ResultFunFactBox(species: species)

                Button("See full details & add a photo →") {
                    showDetail = true
                }
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
}

struct ResultBanner: View {
    let species: AjugaSpecies

    var body: some View {
        VStack(spacing: 8) {
            Text("✅").font(.system(size: 52))
            Text("Your plant is most likely:")
                .font(.subheadline)
                .foregroundStyle(.secondary)
            Text(species.name)
                .font(.title2.bold().italic())
                .multilineTextAlignment(.center)
            Text(species.nickname)
                .font(.title3)
            Label(species.turkish, systemImage: "flag")
                .font(.subheadline)
                .foregroundStyle(.green)
        }
        .padding(20)
        .frame(maxWidth: .infinity)
        .background(Color.green.opacity(0.1))
        .clipShape(RoundedRectangle(cornerRadius: 16))
        .overlay(
            RoundedRectangle(cornerRadius: 16)
                .stroke(Color.green.opacity(0.4), lineWidth: 1.5)
        )
        .padding(.horizontal)
    }
}

struct ResultFactBox: View {
    let species: AjugaSpecies

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            ResultFactRow(label: "Flower:", value: "\(species.flowerEmoji) \(species.flowerColour)")
            ResultFactRow(label: "Size:", value: species.size)
            ResultFactRow(label: "Flowers:", value: species.whenItFlowers)
            ResultFactRow(label: "Grows:", value: species.whereItGrows)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color(.secondarySystemBackground))
        .clipShape(RoundedRectangle(cornerRadius: 14))
        .padding(.horizontal)
    }
}

struct ResultFactRow: View {
    let label: String
    let value: String

    var body: some View {
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

struct ResultSpotBox: View {
    let species: AjugaSpecies

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("⭐ How to spot it")
                .font(.subheadline.bold())
            Text(species.howToSpotIt)
                .font(.body)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color.green.opacity(0.1))
        .clipShape(RoundedRectangle(cornerRadius: 14))
        .padding(.horizontal)
    }
}

struct ResultFunFactBox: View {
    let species: AjugaSpecies

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("💡 Fun fact")
                .font(.subheadline.bold())
            Text(species.funFact)
                .font(.body)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color.yellow.opacity(0.1))
        .clipShape(RoundedRectangle(cornerRadius: 14))
        .padding(.horizontal)
    }
}

// ============================================================
// MARK: - SEARCH VIEW
// ============================================================

struct SearchView: View {
    @EnvironmentObject var store: PhotoStore
    @State private var query: String = ""
    @State private var selected: AjugaSpecies? = nil

    var results: [AjugaSpecies] {
        let q = query.trimmingCharacters(in: .whitespaces).lowercased()
        guard !q.isEmpty else { return [] }
        return allAjuga.filter { sp in
            let blob = [sp.name, sp.nickname, sp.turkish, sp.flowerColour,
                        sp.leafShape, sp.hairiness, sp.whereItGrows,
                        sp.whenItFlowers, sp.funFact, sp.howToSpotIt, sp.lifespan]
                .joined(separator: " ").lowercased()
            return blob.contains(q)
        }
    }

    var isEmpty: Bool {
        query.trimmingCharacters(in: .whitespaces).isEmpty
    }

    var body: some View {
        NavigationStack {
            List {
                Section {
                    TextField("yellow, woolly, Black Sea, silky, Taurus…", text: $query)
                        .autocorrectionDisabled()
                }

                if isEmpty {
                    Section("All 10 species — quick reference") {
                        ForEach(allAjuga) { sp in
                            SearchRow(species: sp) { selected = sp }
                        }
                    }
                } else if results.isEmpty {
                    Section {
                        Text("Nothing found for '\(query)'. Try: yellow, blue, woolly, silky, sticky, Taurus, annual, perennial, Black Sea, creeping.")
                            .foregroundStyle(.secondary)
                            .font(.subheadline)
                    }
                } else {
                    Section("Found \(results.count) result(s) for '\(query)'") {
                        ForEach(results) { sp in
                            SearchRow(species: sp) { selected = sp }
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
}

struct SearchRow: View {
    @EnvironmentObject var store: PhotoStore
    let species: AjugaSpecies
    let onTap: () -> Void

    var body: some View {
        Button(action: onTap) {
            VStack(alignment: .leading, spacing: 4) {
                Text("\(species.flowerEmoji) \(species.name)")
                    .font(.subheadline.italic())
                    .foregroundStyle(.primary)
                HStack(spacing: 4) {
                    Text(species.nickname)
                    if store.hasPhoto(for: species.id) {
                        Text("✅")
                    }
                }
                .font(.caption)
                .foregroundStyle(.secondary)
                Text(species.howToSpotIt)
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
                        Text("Ajuga of Turkey")
                            .font(.title2.bold())
                        Text("10 species from P.H. Davis\nFlora of Turkey Vol. 7 (1982)\nWritten in plain English!")
                            .font(.subheadline)
                            .multilineTextAlignment(.center)
                            .foregroundStyle(.secondary)
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 8)
                }

                Section("What is Ajuga?") {
                    Text("Ajuga (called 'Bugle' in English) is a group of flowering plants in the mint family (Lamiaceae, also written Labiatae).\n\nAll Ajuga have a special flower shape: the upper lip is either tiny or missing completely, and the lower lip is large with 3 lobes.\n\nTurkey has 10 Ajuga species, from sea level up to 2,500 m in the mountains!")
                        .font(.body)
                }

                Section("How to use this app") {
                    Label("Browse — see all 10 species, add your own photos", systemImage: "list.bullet")
                    Label("Identify — answer A/B questions to name your plant", systemImage: "questionmark.circle")
                    Label("Search — type any word to find matching species", systemImage: "magnifyingglass")
                    Label("Photos are saved permanently on your iPad", systemImage: "photo.badge.checkmark")
                }

                Section("What is a dichotomous key?") {
                    Text("The Identify tab uses a 'dichotomous key'. 'Dichotomous' just means 'splits into two choices'. You answer a series of A or B questions. Each answer narrows it down until you reach the right species.\n\nBotanists have used this method for hundreds of years! No botany knowledge needed — just look at your plant and answer honestly.")
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
