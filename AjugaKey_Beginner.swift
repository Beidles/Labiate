// ============================================================
// AJUGA IDENTIFICATION KEY  —  Swift Playgrounds Beginner
//
// Based on: Flora of Turkey Vol. 7 — P.H. Davis (1982)
// Written so a 14-year-old can read and understand every line!
//
// HOW TO USE IN SWIFT PLAYGROUNDS (iPad):
//   1. Open Swift Playgrounds app
//   2. Tap "New Playground" → choose "App"
//   3. Tap "Create App"
//   4. In the sidebar tap the file (e.g. MyApp.swift)
//   5. Tap inside the code → tap Edit → Select All → Delete
//   6. Paste THIS entire file
//   7. Tap Run ▶
// ============================================================

import SwiftUI

// ============================================================
// WHAT IS A KEY STEP?
//
// A dichotomous key is like a choose-your-own-adventure book
// for plants!  At each step you choose A or B and it leads
// to the next question until you reach a species name.
//
// 'struct' = a custom box that holds labelled pieces of data.
// ============================================================

struct KeyStep: Identifiable {
    let id: String          // short code e.g. "k1"
    let question: String    // the question to answer
    let optionA: String     // choice A text
    let optionB: String     // choice B text
    let goToA: String       // where to go if A is chosen
    let goToB: String       // where to go if B is chosen
    // If goToA/goToB starts with "DONE:" we have the final answer
}

// ============================================================
// ALL KEY STEPS
// Source: Flora of Turkey Vol. 7, P.H. Davis (1982)
// ============================================================

let allSteps: [KeyStep] = [

    // --- Step 1 ---
    // First split: how many flowers per cluster, and what colour?
    // A "verticillaster" is just a ring of flowers around the stem.
    KeyStep(
        id: "k1",
        question: "How many flowers are in each ring around the stem, and what colour are they?",
        optionA: "A  4–12 flowers per ring  ·  flowers are BLUE or VIOLET 💜",
        optionB: "B  Only 2 flowers per ring (sometimes up to 4)  ·  flowers are YELLOW, WHITE or PINK 🟡",
        goToA: "k2",
        goToB: "k5"
    ),

    // --- Step 2 ---
    // Are the small leaf-like bracts (just below each flower ring)
    // shaped like narrow spear-heads, the same as the stem leaves?
    KeyStep(
        id: "k2",
        question: "Look at the tiny leaf-like bracts just below each flower ring.  Do they look almost identical to the main stem leaves — narrow, whole-edged, and pointed like a spear?",
        optionA: "A  YES — bracts look like spear-shaped stem leaves; the upper petal lip is reduced to just 2 tiny teeth",
        optionB: "B  NO  — bracts look clearly different from stem leaves; the upper petal lip is well developed",
        goToA: "DONE:4. Ajuga relicta",
        goToB: "k3"
    ),

    // --- Step 3 ---
    // Does it have stolons?
    // A stolon = a long creeping stem that runs along the ground
    // and makes new baby plants — exactly like a strawberry plant!
    KeyStep(
        id: "k3",
        question: "Does the plant have long smooth leafy runners creeping along the ground (stolons — like a strawberry plant)?",
        optionA: "A  YES — smooth leafy runners creep along the ground; upright stem has hairs on 2 sides only",
        optionB: "B  NO  — no creeping runners; upright stem has hairs all the way around",
        goToA: "DONE:3. Ajuga reptans  (Creeping Bugle 💜)",
        goToB: "k4"
    ),

    // --- Step 4 ---
    // Checks stamens and petal tube details.
    // Stamens = the pollen-making stalks inside the flower.
    // Exserted = sticking OUT past the petal tube.
    // Included = hidden INSIDE the petal tube.
    // Annulate = has a ring-shaped swelling near the base of the tube.
    // Resupinate = the flower is twisted upside-down.
    KeyStep(
        id: "k4",
        question: "Look inside the flower.  Are the stamens (pollen stalks) poking OUT past the petal tube?  Does the petal tube have a small ring-shaped swelling near its base?",
        optionA: "A  YES — stamens stick out; tube is straight and has a ring near the base",
        optionB: "B  NO  — stamens stay hidden inside the tube; tube is twisted (upside-down) and has NO ring",
        goToA: "DONE:2. Ajuga genevensis  (Blue Bugle 💜)",
        goToB: "DONE:1. Ajuga orientalis  (Eastern Bugle 💜)"
    ),

    // --- Step 5 ---
    // Now we are in the yellow / white / pink group.
    // Are the leaf tips split into 3 lobes?
    // Tripartite = divided into 3 parts.
    KeyStep(
        id: "k5",
        question: "Look at the stem leaves.  Are their TIPS divided into 3 lobes or teeth (tripartite / 3-toothed)?",
        optionA: "A  YES — most stem leaves have tips split into 3 lobes or teeth",
        optionB: "B  NO  — stem leaves are whole or only have teeth along the sides (not 3-lobed at the tip)",
        goToA: "k6",
        goToB: "k8"
    ),

    // --- Step 6 ---
    // Inside the 3-lobed-leaf group.
    // Checks flower colour and root thickness.
    KeyStep(
        id: "k6",
        question: "What colour are the flowers, and what does the root feel like?",
        optionA: "A  Flowers WHITE or PINK; petal tube much LONGER than the lower lip; root very thick and woody  (Mardin area only)",
        optionB: "B  Flowers YELLOW; petal tube much SHORTER than the lower lip; root more slender",
        goToA: "DONE:11. Ajuga vestita",
        goToB: "k7"
    ),

    // --- Step 7 ---
    // Yellow-flowered 3-lobed group.
    // Checks hairiness — are the leaves completely hidden under
    // dense silvery-woolly hairs?
    KeyStep(
        id: "k7",
        question: "Look at the hairs on the leaves.  Are the leaves covered in SO MANY dense silvery-woolly hairs that you cannot see the leaf surface underneath at all?",
        optionA: "A  YES — leaves completely hidden under thick silvery wool  (mainly SW Anatolia)",
        optionB: "B  NO  — hairs present but the leaf surface is still visible; OR plant is nearly hairless  (widespread)",
        goToA: "DONE:10. Ajuga bombycina  (Silky Bugle 🟡)",
        goToB: "DONE:9. Ajuga chamaepitys  (Ground Pine 🟡)"
    ),

    // --- Step 8 ---
    // Whole-leaf yellow / white / pink group.
    // Checks flower size and fruit type.
    // Baccate = berry-like fruit (soft and juicy).
    // Nutlets = small hard dry fruits.
    KeyStep(
        id: "k8",
        question: "How large is each flower, and what kind of fruit does the plant make?",
        optionA: "A  Flower 3–5 cm long, DRIES PURPLE; leaves oval to lance-shaped, lightly hairy; fruit is BERRY-LIKE (soft and juicy)",
        optionB: "B  Flower 1.2–3 cm long, stays YELLOW; leaves very hairy; fruit is small HARD NUTLETS (dry)",
        goToA: "DONE:5. Ajuga postii  (Post's Bugle 💜)",
        goToB: "k9"
    ),

    // --- Step 9 ---
    // Small yellow-flowered whole-leaf group.
    // Checks leaf width.
    // Revolute = leaf edges curl downward (roll under).
    KeyStep(
        id: "k9",
        question: "Look at the leaves.  Are they VERY NARROW (like grass blades), sometimes with edges curled under?",
        optionA: "A  YES — leaves very narrow, almost like grass; edges often curled under; 2–4 flowers per ring",
        optionB: "B  NO  — leaves oblong or oval (clearly wider than grass), lying flat",
        goToA: "DONE:8. Ajuga iva  (Yellow Bugle 🟡)",
        goToB: "k10"
    ),

    // --- Step 10 ---
    // Last split.
    // Procumbent = stem lies along the ground.
    // Adpressed = hairs pressed flat against the surface.
    // Shaggy = hairs stick out in all directions (fluffy).
    // Subamplexicaul = leaf base partly wraps around the stem.
    KeyStep(
        id: "k10",
        question: "How does the stem grow, and what are the hairs like?",
        optionA: "A  Stem lies along the ground; hairs pressed flat against it; leaves oval with a short stalk",
        optionB: "B  Stem grows upright and tall; hairs shaggy and fluffy; leaves oblong, base wraps partly around the stem",
        goToA: "DONE:7. Ajuga salicifolia  (Willow-leaved Bugle 🟡)",
        goToB: "DONE:6. Ajuga laxmannii  (Woolly Bugle 🟡)"
    ),
]

// ============================================================
// HELPER — find a step by its id string
// ============================================================

func findStep(_ id: String) -> KeyStep? {
    allSteps.first { $0.id == id }
}

// ============================================================
// APP MEMORY  (ObservableObject)
//
// 'ObservableObject' tells SwiftUI "watch this object — if any
// @Published value changes, redraw the screen."
//
// Think of it like a whiteboard SwiftUI watches at all times.
// ============================================================

class KeyViewModel: ObservableObject {

    // @Published means: "tell SwiftUI whenever this changes"
    @Published var currentStepID: String = "k1"
    @Published var history: [(question: String, choice: String)] = []
    @Published var finalAnswer: String? = nil

    var isFinished: Bool { finalAnswer != nil }

    func chooseA() {
        guard let step = findStep(currentStepID) else { return }
        history.append((step.question, step.optionA))
        advance(to: step.goToA)
    }

    func chooseB() {
        guard let step = findStep(currentStepID) else { return }
        history.append((step.question, step.optionB))
        advance(to: step.goToB)
    }

    private func advance(to destination: String) {
        if destination.hasPrefix("DONE:") {
            finalAnswer = String(destination.dropFirst(5))
        } else {
            currentStepID = destination
        }
    }

    func reset() {
        currentStepID = "k1"
        history = []
        finalAnswer = nil
    }
}

// ============================================================
// MAIN SCREEN
// ============================================================

struct ContentView: View {

    // @StateObject creates the KeyViewModel ONCE and keeps it alive
    @StateObject private var vm = KeyViewModel()

    var body: some View {
        NavigationView {
            Group {
                if vm.isFinished {
                    ResultView(vm: vm)
                } else {
                    QuestionView(vm: vm)
                }
            }
            .navigationTitle("Ajuga Key 🌿")
            .navigationBarTitleDisplayMode(.inline)
        }
        .navigationViewStyle(.stack)   // works on both iPhone and iPad
    }
}

// ============================================================
// QUESTION SCREEN
// ============================================================

struct QuestionView: View {

    @ObservedObject var vm: KeyViewModel

    var body: some View {
        // 'guard let' safely unwraps an optional —
        // if the step is not found, show an error instead of crashing.
        guard let step = findStep(vm.currentStepID) else {
            return AnyView(Text("Step not found").foregroundColor(.red))
        }

        return AnyView(
            ScrollView {
                VStack(alignment: .leading, spacing: 18) {

                    // Step counter badge
                    HStack {
                        Spacer()
                        Text("Question \(vm.history.count + 1)")
                            .font(.caption)
                            .padding(.horizontal, 12).padding(.vertical, 4)
                            .background(Color.green.opacity(0.2))
                            .clipShape(Capsule())
                    }

                    // The question text
                    Text(step.question)
                        .font(.body)
                        .fontWeight(.semibold)
                        .padding()
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .background(Color(.systemGray6))
                        .cornerRadius(12)

                    // Option A button
                    Button { vm.chooseA() } label: {
                        HStack(alignment: .top, spacing: 10) {
                            Text("A").fontWeight(.bold).frame(width: 20)
                            Text(step.optionA).multilineTextAlignment(.leading)
                            Spacer()
                        }
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.blue.opacity(0.1))
                        .cornerRadius(12)
                        .overlay(RoundedRectangle(cornerRadius: 12).stroke(Color.blue.opacity(0.4)))
                    }
                    .foregroundColor(.primary)

                    // Option B button
                    Button { vm.chooseB() } label: {
                        HStack(alignment: .top, spacing: 10) {
                            Text("B").fontWeight(.bold).frame(width: 20)
                            Text(step.optionB).multilineTextAlignment(.leading)
                            Spacer()
                        }
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.orange.opacity(0.1))
                        .cornerRadius(12)
                        .overlay(RoundedRectangle(cornerRadius: 12).stroke(Color.orange.opacity(0.4)))
                    }
                    .foregroundColor(.primary)

                    // Trail of previous answers
                    if !vm.history.isEmpty {
                        Divider()
                        Text("Your answers so far:").font(.caption).foregroundColor(.secondary)
                        ForEach(vm.history.indices, id: \.self) { i in
                            HStack(alignment: .top, spacing: 6) {
                                Text("\(i+1).").font(.caption2).foregroundColor(.secondary)
                                Text(vm.history[i].choice).font(.caption).foregroundColor(.secondary)
                            }
                        }
                    }

                    Spacer(minLength: 40)
                }
                .padding()
            }
        )
    }
}

// ============================================================
// RESULT SCREEN
// ============================================================

struct ResultView: View {

    @ObservedObject var vm: KeyViewModel

    var body: some View {
        ScrollView {
            VStack(spacing: 22) {

                Text("✅").font(.system(size: 64))

                Text("You identified it!")
                    .font(.title2).fontWeight(.bold)

                Text(vm.finalAnswer ?? "")
                    .font(.title3)
                    .multilineTextAlignment(.center)
                    .padding()
                    .frame(maxWidth: .infinity)
                    .background(Color.green.opacity(0.15))
                    .cornerRadius(14)

                VStack(alignment: .leading, spacing: 10) {
                    Text("The choices you made:").font(.headline)
                    ForEach(vm.history.indices, id: \.self) { i in
                        VStack(alignment: .leading, spacing: 3) {
                            Text("Step \(i+1)").font(.caption).foregroundColor(.secondary)
                            Text(vm.history[i].choice).font(.subheadline)
                        }
                        .padding(10)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .background(Color(.systemGray6))
                        .cornerRadius(10)
                    }
                }

                Button { vm.reset() } label: {
                    Label("Start Again", systemImage: "arrow.counterclockwise")
                        .font(.headline)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.green)
                        .foregroundColor(.white)
                        .cornerRadius(14)
                }

                Spacer(minLength: 40)
            }
            .padding()
        }
    }
}

// ============================================================
// ENTRY POINT
//
// '@main' marks this as the starting point of the whole app.
// SwiftUI calls 'body' to build the very first screen.
// ============================================================

@main
struct AjugaKeyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
