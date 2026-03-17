// ============================================================
// FILE 1 of 5: Models.swift
// LABIATAE (Mint Family) of Turkey
//
// HOW TO USE IN SWIFT PLAYGROUNDS (iPad):
//   1. Create a new App Playground
//   2. Delete the default MyApp.swift content
//   3. Add 5 NEW files (tap + in sidebar): name them exactly:
//      1_Models.swift, 2_PlantData.swift, 3_KeyData.swift,
//      4_Views.swift, 5_LabiateApp.swift
//   4. Paste each file's code into the matching file
//   5. Tap Run ▶
// ============================================================

import SwiftUI

// Every plant genus has these properties:
struct Plant: Identifiable {
    let id: Int
    let name: String        // Latin genus name
    let common: String      // Common English name
    let turkish: String     // Turkish name
    let description: String // Key features to identify it
    let habitat: String     // Where it grows in Turkey
    let funFact: String     // An interesting fact
}

// 'enum' = a type that can be one of a fixed set of values
enum KeyResult {
    case step(String)   // Go to another question (by its ID)
    case plant(Int)     // You found it! Show this plant number
}

// Each step in the dichotomous key:
struct KeyStep: Identifiable {
    let id: String
    let question: String
    let optionA: String
    let optionB: String
    let nextA: KeyResult
    let nextB: KeyResult
}

// Helper functions
func findStep(_ id: String) -> KeyStep? {
    keySteps.first { $0.id == id }
}

func findPlant(_ id: Int) -> Plant? {
    allPlants.first { $0.id == id }
}
