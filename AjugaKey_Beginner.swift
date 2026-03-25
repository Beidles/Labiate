// ============================================================
// AJUGA IDENTIFICATION KEY  —  Swift Playgrounds Beginner
//
// Based on: Flora of Turkey Vol. 7 — P.H. Davis (1982)
// Written so a 14-year-old can read and understand every line!
//
// HOW TO USE IN SWIFT PLAYGROUNDS (iPad/Mac):
//   1. Open Swift Playgrounds app
//   2. Tap "New Playground" → "Blank"
//   3. Delete the starter code
//   4. Paste this ENTIRE file
//   5. Tap the Run ▶ button
//
// You will see a step-by-step plant identification quiz!
// Answer YES or NO at each step to find the species name.
// ============================================================

import SwiftUI

// ============================================================
// STEP 1 — WHAT IS A "KEY STEP"?
//
// A dichotomous key is like a choose-your-own-adventure book
// for plants!  At each step you choose between two options (A or B)
// and it leads you to the next question until you reach an answer.
//
// 'struct' means a custom container that holds related data.
// Think of it like a labelled cardboard box.
// ============================================================

struct KeyStep {
    let id: String          // a short code like "k1", "k2"
    let question: String    // the question you need to answer
    let optionA: String     // choice A
    let optionB: String     // choice B
    let goToA: String       // where to go if you pick A  ("DONE:reptans" = answer!)
    let goToB: String       // where to go if you pick B
}

// ============================================================
// STEP 2 — ALL THE KEY STEPS
//
// This is the exact key from Flora of Turkey (Davis 1982)
// turned into plain English questions.
//
// If goToA / goToB starts with "DONE:" that is the final answer!
// Otherwise it is the id of the next KeyStep to show.
// ============================================================

let keySteps: [KeyStep] = [

    // ---- QUESTION 1 ----------------------------------------
    // The key first splits on how many flowers are in each cluster
    // (a "verticillaster" is just a ring of flowers around the stem)
    // and on flower colour.
    KeyStep(
        id: "k1",
        question: "How many flowers are packed into each ring around the stem?",
        optionA: "A  4 to 12 flowers per ring, and the flowers are BLUE or VIOLET",
        optionB: "B  Only 2 flowers per ring (sometimes 4), and flowers are YELLOW, WHITE or PINK",
        goToA: "k2",   // blue flowers → go to question 2
        goToB: "k5"    // yellow/white/pink → go to question 5
    ),

    // ---- QUESTION 2 ----------------------------------------
    // Checks whether the leaf-like bracts (the small leaves just
    // below each flower ring) look like the main stem leaves.
    KeyStep(
        id: "k2",
        question: "Look at the small leaf-like bracts just below each flower ring.  Do they look almost IDENTICAL to the main stem leaves — narrow, whole-edged, and lanceolate (long and pointed like a spear)?",
        optionA: "A  YES — bracts look like spear-shaped stem leaves, and the corolla upper lip is reduced to just 2 tiny teeth",
        optionB: "B  NO  — bracts look clearly different from the stem leaves, and the upper lip is well developed",
        goToA: "DONE:4. Ajuga relicta",
        goToB: "k3"
    ),

    // ---- QUESTION 3 ----------------------------------------
    // Checks for stolons.
    // A stolon is a creeping stem that runs along the ground
    // and makes new baby plants at its tip — just like strawberries!
    KeyStep(
        id: "k3",
        question: "Does the plant have STOLONS — long smooth leafy runners creeping along the ground (like a strawberry plant)?",
        optionA: "A  YES — smooth leafy runners creep along the ground; the upright flowering stem is hairy on 2 sides only",
        optionB: "B  NO  — no creeping runners; the flowering stem is hairy all the way around",
        goToA: "DONE:3. Ajuga reptans  (Creeping Bugle 💜)",
        goToB: "k4"
    ),

    // ---- QUESTION 4 ----------------------------------------
    // Checks stamens and corolla tube details.
    // Stamens = the pollen-making stalks inside a flower.
    // Exserted = sticking OUT past the petal tube.
    // Included = hidden INSIDE the petal tube.
    // Annulate = has a ring-shaped swelling near the base.
    // Resupinate = the flower is twisted upside-down.
    KeyStep(
        id: "k4",
        question: "Look inside the blue flower.  Are the STAMENS (pollen stalks) poking OUT past the petal tube, and does the petal tube have a ring-like swelling near its base?",
        optionA: "A  YES — stamens stick out; petal tube is straight and has a ring near the base",
        optionB: "B  NO  — stamens stay hidden inside; petal tube is twisted (resupinate) and has NO ring",
        goToA: "DONE:2. Ajuga genevensis  (Blue Bugle 💜)",
        goToB: "DONE:1. Ajuga orientalis  (Eastern Bugle 💜)"
    ),

    // ---- QUESTION 5 ----------------------------------------
    // Now we are in the yellow/white/pink group.
    // Checks whether the leaves are cut into lobes at the tip.
    // Tripartite = divided into 3 parts.
    KeyStep(
        id: "k5",
        question: "Look at the stem leaves.  Are their tips split into 3 lobes or teeth (tripartite / 3-toothed)?",
        optionA: "A  YES — most stem leaves have tips divided into 3 lobes or teeth",
        optionB: "B  NO  — stem leaves are whole or only have teeth along the sides (not 3-lobed at tip)",
        goToA: "k6",
        goToB: "k8"
    ),

    // ---- QUESTION 6 ----------------------------------------
    // Inside the 3-lobed leaf group — checks flower colour and root.
    KeyStep(
        id: "k6",
        question: "What colour are the flowers, and what does the rootstock feel like?",
        optionA: "A  Flowers WHITE or PINK; petal tube much LONGER than the lower petal lip; root very thick and woody (only found in Mardin area)",
        optionB: "B  Flowers YELLOW; petal tube much SHORTER than the lower petal lip; root more slender",
        goToA: "DONE:11. Ajuga vestita",
        goToB: "k7"
    ),

    // ---- QUESTION 7 ----------------------------------------
    // Yellow-flowered 3-lobed group — checks hairiness.
    // Silvery woolly = like dense silver cotton-wool covering the leaf.
    KeyStep(
        id: "k7",
        question: "Look at the hairs on the leaves.  Are the leaves covered in SO MANY dense silvery-woolly hairs that you cannot see the leaf surface underneath?",
        optionA: "A  YES — leaves completely hidden under thick silvery wool (mainly SW Anatolia)",
        optionB: "B  NO  — hairs present but you can still see the leaf surface; OR plant is nearly hairless (widespread)",
        goToA: "DONE:10. Ajuga bombycina  (Silky Bugle 🟡)",
        goToB: "DONE:9. Ajuga chamaepitys  (Ground Pine 🟡)"
    ),

    // ---- QUESTION 8 ----------------------------------------
    // Whole-leaf yellow/white/pink group — checks corolla size and fruit.
    // Baccate = berry-like (soft, juicy fruit).
    // Nutlets = small hard dry fruits.
    KeyStep(
        id: "k8",
        question: "How big is each flower, and what type of fruit does the plant make?",
        optionA: "A  Flower 3–5 cm long, DRIES PURPLE; leaves oval to lance-shaped, lightly hairy; fruit is BERRY-LIKE (soft and juicy)",
        optionB: "B  Flower 1.2–3 cm long, stays YELLOW; leaves linear, oblong or oval, very hairy; fruit is small HARD NUTLETS (dry)",
        goToA: "DONE:5. Ajuga postii  (Post's Bugle 💜)",
        goToB: "k9"
    ),

    // ---- QUESTION 9 ----------------------------------------
    // Small yellow-flowered whole-leaf group — checks leaf shape.
    // Revolute = leaf edges roll under (curl downward).
    KeyStep(
        id: "k9",
        question: "Look at the leaves.  Are they VERY NARROW (like grass blades or thin fingers), sometimes with edges rolled under?",
        optionA: "A  YES — leaves very narrow to almost linear, edges often rolled under; 2–4 flowers per ring",
        optionB: "B  NO  — leaves oblong or oval (clearly wider), lying flat",
        goToA: "DONE:8. Ajuga iva  (Yellow Bugle 🟡)",
        goToB: "k10"
    ),

    // ---- QUESTION 10 ----------------------------------------
    // Last split — checks stem posture and hair type.
    // Procumbent = lying along the ground.
    // Adpressed = hairs pressed flat against the surface.
    // Shaggy = hairs stick out in all directions.
    // Subamplexicaul = leaf base half-wraps around the stem.
    KeyStep(
        id: "k10",
        question: "How does the stem grow, and what are the hairs like?",
        optionA: "A  Stem lies along the ground (procumbent); hairs pressed flat; leaves oval, short-stalked",
        optionB: "B  Stem grows upright and tall; hairs shaggy and fluffy; leaves oblong, base wraps partly around the stem",
        goToA: "DONE:7. Ajuga salicifolia  (Willow-leaved Bugle 🟡)",
        goToB: "DONE:6. Ajuga laxmannii  (Woolly Bugle 🟡)"
    ),
]

// ============================================================
// STEP 3 — A HELPER FUNCTION
//
// A 'func' is a named block of code you can call whenever you need it.
// This one looks up a KeyStep by its id string.
// ============================================================

func findStep(id: String) -> KeyStep? {
    // 'first(where:)' searches the array and returns the first
    // item where the condition inside the braces is true.
    return keySteps.first(where: { $0.id == id })
}

// ============================================================
// STEP 4 — THE APP'S MEMORY  (@Observable)
//
// '@Observable' tells SwiftUI "watch this object — if any
// stored value changes, update the screen automatically."
//
// Think of it as a whiteboard the app reads and writes on.
// ============================================================

@Observable
class KeyViewModel {

    // The id of the question we are currently showing
    var currentStepID: String = "k1"

    // The complete list of answers the user chose (to show a trail)
    var history: [(question: String, chosenOption: String)] = []

    // If not nil, we have reached a final answer
    var finalAnswer: String? = nil

    // Is the quiz done?
    var isFinished: Bool { finalAnswer != nil }

    // ---- Pick option A ----
    func chooseA() {
        guard let step = findStep(id: currentStepID) else { return }
        history.append((step.question, step.optionA))
        advance(to: step.goToA)
    }

    // ---- Pick option B ----
    func chooseB() {
        guard let step = findStep(id: currentStepID) else { return }
        history.append((step.question, step.optionB))
        advance(to: step.goToB)
    }

    // ---- Move to the next step or record the final answer ----
    private func advance(to destination: String) {
        if destination.hasPrefix("DONE:") {
            // Everything after "DONE:" is the species name
            finalAnswer = String(destination.dropFirst(5))
        } else {
            currentStepID = destination
        }
    }

    // ---- Start over from the beginning ----
    func reset() {
        currentStepID = "k1"
        history = []
        finalAnswer = nil
    }
}

// ============================================================
// STEP 5 — THE MAIN SCREEN
//
// 'View' is a SwiftUI protocol — anything that can appear on screen.
// 'body' describes exactly what to draw.
// ============================================================

struct ContentView: View {

    // '@State' creates a piece of memory that belongs to this view.
    // When it changes, SwiftUI redraws the view automatically.
    @State private var vm = KeyViewModel()

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {

                // Show a different screen depending on whether
                // we are still answering questions or finished.
                if vm.isFinished {
                    ResultView(answer: vm.finalAnswer!, history: vm.history) {
                        vm.reset()
                    }
                } else {
                    QuestionView(vm: vm)
                }
            }
            .navigationTitle("Ajuga Key  🌿")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

// ============================================================
// STEP 6 — THE QUESTION SCREEN
// ============================================================

struct QuestionView: View {

    var vm: KeyViewModel     // the shared memory from ContentView

    // A computed property: run the code in braces whenever we
    // need to know the current step.
    var currentStep: KeyStep? { findStep(id: vm.currentStepID) }

    var body: some View {
        // 'guard' is like saying "make sure this exists, or stop here"
        guard let step = currentStep else {
            return AnyView(Text("Error — step not found").foregroundStyle(.red))
        }

        return AnyView(
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {

                    // ---- Progress badge ----
                    HStack {
                        Spacer()
                        Text("Step \(vm.history.count + 1)")
                            .font(.caption)
                            .padding(.horizontal, 12)
                            .padding(.vertical, 4)
                            .background(Color.green.opacity(0.2))
                            .clipShape(Capsule())
                    }

                    // ---- The question ----
                    Text(step.question)
                        .font(.title3)
                        .fontWeight(.semibold)
                        .padding()
                        .background(Color(.systemGray6))
                        .clipShape(RoundedRectangle(cornerRadius: 12))

                    // ---- Option A button ----
                    Button(action: { vm.chooseA() }) {
                        HStack(alignment: .top, spacing: 12) {
                            Text("A")
                                .fontWeight(.bold)
                                .frame(width: 24)
                            Text(step.optionA)
                                .multilineTextAlignment(.leading)
                            Spacer()
                        }
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.blue.opacity(0.1))
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                        .overlay(
                            RoundedRectangle(cornerRadius: 12)
                                .stroke(Color.blue.opacity(0.4), lineWidth: 1)
                        )
                    }
                    .foregroundStyle(.primary)

                    // ---- Option B button ----
                    Button(action: { vm.chooseB() }) {
                        HStack(alignment: .top, spacing: 12) {
                            Text("B")
                                .fontWeight(.bold)
                                .frame(width: 24)
                            Text(step.optionB)
                                .multilineTextAlignment(.leading)
                            Spacer()
                        }
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.orange.opacity(0.1))
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                        .overlay(
                            RoundedRectangle(cornerRadius: 12)
                                .stroke(Color.orange.opacity(0.4), lineWidth: 1)
                        )
                    }
                    .foregroundStyle(.primary)

                    // ---- Answer trail (history so far) ----
                    if !vm.history.isEmpty {
                        Divider()
                        Text("Your answers so far:")
                            .font(.caption)
                            .foregroundStyle(.secondary)

                        ForEach(vm.history.indices, id: \.self) { i in
                            HStack(alignment: .top, spacing: 8) {
                                Text("\(i + 1).")
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                                Text(vm.history[i].chosenOption)
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
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
// STEP 7 — THE RESULT SCREEN
// ============================================================

struct ResultView: View {

    let answer: String                  // e.g. "3. Ajuga reptans  (Creeping Bugle 💜)"
    let history: [(question: String, chosenOption: String)]
    let onReset: () -> Void             // closure (a small block of code) to restart

    var body: some View {
        ScrollView {
            VStack(spacing: 24) {

                // ---- Big tick and answer ----
                VStack(spacing: 12) {
                    Text("✅")
                        .font(.system(size: 60))

                    Text("You identified it!")
                        .font(.title2)
                        .fontWeight(.bold)

                    Text(answer)
                        .font(.title3)
                        .multilineTextAlignment(.center)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.green.opacity(0.15))
                        .clipShape(RoundedRectangle(cornerRadius: 14))
                }

                // ---- Full answer trail ----
                VStack(alignment: .leading, spacing: 10) {
                    Text("The choices you made:")
                        .font(.headline)

                    ForEach(history.indices, id: \.self) { i in
                        VStack(alignment: .leading, spacing: 4) {
                            Text("Step \(i + 1)")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                            Text(history[i].chosenOption)
                                .font(.subheadline)
                        }
                        .padding(10)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .background(Color(.systemGray6))
                        .clipShape(RoundedRectangle(cornerRadius: 10))
                    }
                }

                // ---- Start again button ----
                Button(action: onReset) {
                    Label("Start Again", systemImage: "arrow.counterclockwise")
                        .font(.headline)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.green)
                        .foregroundStyle(.white)
                        .clipShape(RoundedRectangle(cornerRadius: 14))
                }

                Spacer(minLength: 40)
            }
            .padding()
        }
    }
}

// ============================================================
// STEP 8 — THE ENTRY POINT
//
// '@main' marks this struct as the starting point of the app.
// SwiftUI calls 'body' to build the first screen.
// ============================================================

@main
struct AjugaKeyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
