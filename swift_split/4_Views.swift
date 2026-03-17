// ============================================================
// FILE 4 of 5: Views.swift
// All SwiftUI views for the Labiatae app
// ============================================================

import SwiftUI

// ── Browse Tab ───────────────────────────────────────────────
struct BrowseView: View {
    var body: some View {
        NavigationView {
            List(allPlants) { plant in
                NavigationLink(destination: PlantDetailView(plant: plant)) {
                    VStack(alignment: .leading, spacing: 4) {
                        HStack {
                            Text(String(plant.id) + ".")
                                .font(.caption).foregroundStyle(.secondary)
                            Text(plant.name)
                                .font(.headline).italic()
                            Spacer()
                            Text(plant.common)
                                .font(.caption).foregroundStyle(.secondary)
                        }
                        Text(plant.turkish)
                            .font(.caption).foregroundStyle(.green)
                    }
                    .padding(.vertical, 2)
                }
            }
            .navigationTitle("45 Genera of Labiatae")
        }
    }
}

// ── Plant Detail View ────────────────────────────────────────
struct PlantDetailView: View {
    let plant: Plant

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Genus " + String(plant.id))
                        .font(.caption).foregroundStyle(.secondary)
                    Text(plant.name)
                        .font(.largeTitle).bold().italic()
                    Text(plant.common)
                        .font(.title2).foregroundStyle(.secondary)
                    Label(plant.turkish, systemImage: "flag")
                        .font(.subheadline).foregroundStyle(.green)
                }
                .padding()
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Color.green.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))

                infoCard(icon: "leaf",       title: "Key Features",     text: plant.description)
                infoCard(icon: "mountain.2", title: "Habitat in Turkey", text: plant.habitat)
                infoCard(icon: "star",        title: "Fun Fact",          text: plant.funFact)

                Text("Source: Flora of Turkey, Vol. 7 — P.H. Davis")
                    .font(.caption).foregroundStyle(.secondary)
            }
            .padding()
        }
        .navigationTitle(plant.name)
        .navigationBarTitleDisplayMode(.inline)
    }

    func infoCard(icon: String, title: String, text: String) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            Label(title, systemImage: icon)
                .font(.headline).foregroundStyle(.green)
            Text(text)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color(.secondarySystemBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}

// ── Identify Tab ─────────────────────────────────────────────
struct IdentifyView: View {
    @State private var currentStep: KeyStep? = findStep("s1")
    @State private var foundPlant: Plant?    = nil
    @State private var questionCount: Int    = 0
    @State private var history: [KeyStep]    = []

    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    if let plant = foundPlant {
                        ResultView(plant: plant, questionCount: questionCount)
                    } else if let step = currentStep {
                        questionCard(step: step)
                    }
                    HStack(spacing: 12) {
                        if !history.isEmpty {
                            Button("Back") { goBack() }.buttonStyle(.bordered)
                        }
                        Button("Reset") { reset() }
                            .buttonStyle(.borderedProminent).tint(.green)
                    }
                }
                .padding()
            }
            .navigationTitle("Identify Your Plant")
        }
    }

    func questionCard(step: KeyStep) -> some View {
        VStack(spacing: 16) {
            Text("Question " + String(questionCount + 1))
                .font(.caption).foregroundStyle(.secondary)
            Text(step.question)
                .font(.body).multilineTextAlignment(.center)
                .padding()
                .background(Color.green.opacity(0.08))
                .clipShape(RoundedRectangle(cornerRadius: 12))
            Text("Look carefully at your plant before answering!")
                .font(.caption).foregroundStyle(.secondary).italic()
            answerButton(label: "A", text: step.optionA, color: .blue)  { choose(step.nextA) }
            answerButton(label: "B", text: step.optionB, color: .orange) { choose(step.nextB) }
        }
    }

    func answerButton(label: String, text: String, color: Color, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            HStack(alignment: .top, spacing: 12) {
                Text(label).font(.headline)
                    .frame(width: 28, height: 28)
                    .background(color.opacity(0.2))
                    .clipShape(Circle())
                Text(text).font(.body).multilineTextAlignment(.leading)
                Spacer()
            }
            .padding()
            .frame(maxWidth: .infinity)
            .background(color.opacity(0.06))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .overlay(RoundedRectangle(cornerRadius: 12).stroke(color.opacity(0.3), lineWidth: 1))
        }
        .foregroundStyle(.primary)
    }

    func choose(_ result: KeyResult) {
        if let step = currentStep { history.append(step) }
        questionCount += 1
        switch result {
        case .step(let id):
            currentStep = findStep(id); foundPlant = nil
        case .plant(let id):
            foundPlant = findPlant(id); currentStep = nil
        }
    }

    func goBack() {
        if let prev = history.popLast() {
            currentStep = prev; foundPlant = nil
            questionCount = max(0, questionCount - 1)
        }
    }

    func reset() {
        currentStep = findStep("s1"); foundPlant = nil
        questionCount = 0; history = []
    }
}

// ── Result View ───────────────────────────────────────────────
struct ResultView: View {
    let plant: Plant
    let questionCount: Int

    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "checkmark.circle.fill")
                .font(.system(size: 64)).foregroundStyle(.green)
            Text("Identified in " + String(questionCount) + " questions!")
                .font(.subheadline).foregroundStyle(.secondary)
            Text(plant.name).font(.largeTitle).bold().italic()
            Text(plant.common).font(.title2).foregroundStyle(.secondary)
            Label(plant.turkish, systemImage: "flag").foregroundStyle(.green)

            VStack(alignment: .leading, spacing: 12) {
                factRow(icon: "leaf",       text: plant.description)
                Divider()
                factRow(icon: "mountain.2", text: plant.habitat)
                Divider()
                factRow(icon: "star",        text: plant.funFact)
            }
            .padding()
            .background(Color(.secondarySystemBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))
        }
    }

    func factRow(icon: String, text: String) -> some View {
        HStack(alignment: .top, spacing: 10) {
            Image(systemName: icon).foregroundStyle(.green).frame(width: 20)
            Text(text)
        }
    }
}

// ── Search Tab ────────────────────────────────────────────────
struct SearchView: View {
    @State private var query = ""

    var results: [Plant] {
        guard !query.isEmpty else { return allPlants }
        return allPlants.filter { plant in
            plant.name.localizedCaseInsensitiveContains(query)
            || plant.common.localizedCaseInsensitiveContains(query)
            || plant.turkish.localizedCaseInsensitiveContains(query)
            || plant.description.localizedCaseInsensitiveContains(query)
        }
    }

    var body: some View {
        NavigationView {
            List(results) { plant in
                NavigationLink(destination: PlantDetailView(plant: plant)) {
                    VStack(alignment: .leading, spacing: 4) {
                        Text(plant.name).font(.headline).italic()
                        Text(plant.common + " - " + plant.turkish)
                            .font(.caption).foregroundStyle(.secondary)
                    }
                }
            }
            .searchable(text: $query, prompt: "Try: sage, nane, thyme, lavanta...")
            .navigationTitle("Search Plants")
        }
    }
}

// ── Quiz Tab ──────────────────────────────────────────────────
struct QuizView: View {
    @State private var quizPlants: [Plant] = []
    @State private var index:      Int     = 0
    @State private var score:      Int     = 0
    @State private var guess:      String  = ""
    @State private var showAnswer: Bool    = false
    @State private var isCorrect:  Bool    = false
    @State private var finished:   Bool    = false

    var current: Plant? { index < quizPlants.count ? quizPlants[index] : nil }

    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    if quizPlants.isEmpty   { startScreen }
                    else if finished         { resultsScreen }
                    else if let p = current  { questionScreen(p) }
                }
                .padding()
            }
            .navigationTitle("Quiz Mode")
        }
    }

    var startScreen: some View {
        VStack(spacing: 24) {
            Image(systemName: "questionmark.circle.fill")
                .font(.system(size: 80)).foregroundStyle(.green)
            Text("Test Your Knowledge!").font(.title).bold()
            Text("You will be shown 5 plants.\nRead the clues and type the genus name.")
                .multilineTextAlignment(.center).foregroundStyle(.secondary)
            Button("Start Quiz") { startQuiz() }
                .buttonStyle(.borderedProminent).tint(.green).controlSize(.large)
        }
    }

    func questionScreen(_ plant: Plant) -> some View {
        VStack(spacing: 16) {
            ProgressView(value: Double(index), total: 5).tint(.green)
            HStack {
                Text("Question " + String(index + 1) + " of 5")
                    .font(.caption).foregroundStyle(.secondary)
                Spacer()
                Text("Score: " + String(score)).font(.caption.bold()).foregroundStyle(.green)
            }

            VStack(alignment: .leading, spacing: 12) {
                clueRow(icon: "leaf",       label: "Description", text: plant.description)
                Divider()
                clueRow(icon: "mountain.2", label: "Habitat",     text: plant.habitat)
                Divider()
                clueRow(icon: "star",        label: "Fun Fact",    text: plant.funFact)
            }
            .padding()
            .background(Color(.secondarySystemBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))

            if !showAnswer {
                TextField("Type the genus name...", text: $guess)
                    .textFieldStyle(.roundedBorder)
                    .autocorrectionDisabled()
                    .textInputAutocapitalization(.words)
                Button("Submit") { checkAnswer(plant) }
                    .buttonStyle(.borderedProminent).tint(.green)
                    .disabled(guess.trimmingCharacters(in: .whitespaces).isEmpty)
            } else {
                VStack(spacing: 6) {
                    if isCorrect {
                        Label("Correct! Well done!", systemImage: "checkmark.circle.fill")
                            .foregroundStyle(.green).font(.headline)
                    } else {
                        Label("Not quite!", systemImage: "xmark.circle.fill")
                            .foregroundStyle(.red).font(.headline)
                        Text("Answer: " + plant.name + " (" + plant.common + ")")
                            .foregroundStyle(.secondary)
                    }
                }
                .padding()
                .frame(maxWidth: .infinity)
                .background(isCorrect ? Color.green.opacity(0.1) : Color.red.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))
                Button("Next") { nextQuestion() }
                    .buttonStyle(.borderedProminent).tint(.green)
            }
        }
    }

    var resultsScreen: some View {
        VStack(spacing: 20) {
            Image(systemName: score >= 4 ? "star.circle.fill" : "hand.thumbsup.fill")
                .font(.system(size: 80)).foregroundStyle(.green)
            Text("Quiz Complete!").font(.title).bold()
            Text("You scored " + String(score) + " out of 5").font(.title2)
            Text(message).multilineTextAlignment(.center).foregroundStyle(.secondary)
            Button("Play Again") { startQuiz() }
                .buttonStyle(.borderedProminent).tint(.green).controlSize(.large)
        }
    }

    var message: String {
        switch score {
        case 5: return "PERFECT SCORE! You are a Labiatae expert!"
        case 4: return "Excellent! Almost perfect!"
        case 3: return "Good job! Keep studying!"
        case 2: return "Not bad — try again to improve."
        default: return "Keep practising — these plants are tricky!"
        }
    }

    func clueRow(icon: String, label: String, text: String) -> some View {
        VStack(alignment: .leading, spacing: 4) {
            Label(label, systemImage: icon).font(.caption).foregroundStyle(.secondary)
            Text(text)
        }
    }

    func startQuiz() {
        quizPlants = Array(allPlants.shuffled().prefix(5))
        index = 0; score = 0; guess = ""
        showAnswer = false; isCorrect = false; finished = false
    }

    func checkAnswer(_ plant: Plant) {
        isCorrect = guess.trimmingCharacters(in: .whitespaces).lowercased() == plant.name.lowercased()
        if isCorrect { score += 1 }
        showAnswer = true
    }

    func nextQuestion() {
        index += 1; guess = ""; showAnswer = false; isCorrect = false
        if index >= quizPlants.count { finished = true }
    }
}
