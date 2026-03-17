// ============================================================
// FILE 5 of 5: LabiateApp.swift
// App entry point — paste this into your MAIN app file
// (the one with the house icon in Swift Playgrounds sidebar)
// ============================================================

import SwiftUI

// The root view — 4-tab navigation
struct ContentView: View {
    var body: some View {
        TabView {
            BrowseView()
                .tabItem { Label("Browse", systemImage: "list.bullet") }
            IdentifyView()
                .tabItem { Label("Identify", systemImage: "magnifyingglass") }
            SearchView()
                .tabItem { Label("Search", systemImage: "text.magnifyingglass") }
            QuizView()
                .tabItem { Label("Quiz", systemImage: "questionmark.circle") }
        }
        .tint(.green)
    }
}

// @main tells Swift Playgrounds: "start here"
@main
struct LabiateApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
