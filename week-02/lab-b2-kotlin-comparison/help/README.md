# Opening the Kotlin Notebook in IntelliJ IDEA

Follow these instructions to download, add, open, and run the course Kotlin Notebook.

## 1. Install IntelliJ IDEA

Download and install IntelliJ IDEA:

[IntelliJ IDEA Download](https://www.jetbrains.com/idea/download/)

For this course, use IntelliJ IDEA **2026.1 or 2026.2**.

## 2. Install the Kotlin Notebook Plugin

Open the Kotlin Notebook plugin page:

[Kotlin Notebook Plugin — JetBrains Marketplace](https://plugins.jetbrains.com/plugin/16340-kotlin-notebook)

You can install the plugin directly from IntelliJ IDEA:

1. Open IntelliJ IDEA.
2. Open the IDE settings:
   - **macOS:** Press `⌘,`
   - **Windows/Linux:** Press `Ctrl+Alt+S`
3. Select **Plugins**.
4. Open the **Marketplace** tab.
5. Search for **Kotlin Notebook**.
6. Click **Install**.
7. Restart IntelliJ IDEA when prompted.

> Install the plugin directly from the Marketplace whenever possible. If you receive a plugin ZIP file, select the complete ZIP file without extracting it. Do not install only the internal `kotlin-jupyter-plugin.jar` file.

## 3. Open Your Local Kotlin Project

Open your `CS3035` Kotlin project in IntelliJ IDEA.

Keep your active project in a local folder:

- **macOS:** `~/IdeaProjects/CS3035`
- **Windows:** `C:\Users\<username>\IdeaProjects\CS3035`

Do not run the active project directly from OneDrive, iCloud, Dropbox, or another cloud-synchronized folder. Cloud synchronization may cause project files to disappear temporarily.

## 4. Download the Course Notebook

1. Open the notebook on GitHub:

   [L022: Kotlin Fundamentals](https://github.com/3eltran23/CS3035_Fall2026_Materials/blob/main/week-02/L022-Kotlin.ipynb)

2. Click the **Download raw file** button near the upper-right corner of the GitHub file viewer.

3. Confirm that the downloaded file is named:

   `L022-Kotlin.ipynb`

## 5. Add the Notebook to Your Project

1. In IntelliJ IDEA, open the **Project** panel.
2. Expand the following folders:

   `CS3035 → src → main → kotlin`

3. Open Finder on macOS or File Explorer on Windows.
4. Locate `L022-Kotlin.ipynb` in your Downloads folder.
5. Drag the notebook into the `kotlin` folder in IntelliJ IDEA.
6. Select **Copy** if IntelliJ IDEA asks whether to copy or move the file.

The project should now contain:

```text
CS3035
├── build.gradle.kts
├── settings.gradle.kts
└── src
    └── main
        └── kotlin
            ├── Main.kt
            └── L022-Kotlin.ipynb
```

## 6. Open and Run the Notebook

1. Double-click `L022-Kotlin.ipynb` in the Project panel.
2. Wait for IntelliJ IDEA to initialize the Kotlin kernel.
3. Locate the first Kotlin code cell.
4. Run the cell by:
   - Clicking the green ▶ button beside the cell, or
   - Pressing `Shift+Return`
5. Continue running the cells from top to bottom.

The first cell may take longer because IntelliJ IDEA must initialize the Kotlin kernel and download required components.

## 7. Test the Kotlin Kernel

Create a code cell containing:

```kotlin
println("Kotlin Notebook is working!")
```

Run the cell.

Expected output:

```text
Kotlin Notebook is working!
```

## Troubleshooting

### “Could not find Jupyter notebook session factory”

1. Save your work.
2. Completely quit IntelliJ IDEA.
3. Reopen IntelliJ IDEA.
4. Open **Settings → Plugins → Installed**.
5. Uninstall **Kotlin Notebook**.
6. Restart IntelliJ IDEA.
7. Install **Kotlin Notebook** again from the Marketplace.
8. Restart IntelliJ IDEA and reopen the notebook.

### The Notebook Opens as JSON or Plain Text

The Kotlin Notebook plugin is missing or disabled. Enable or reinstall the plugin and restart IntelliJ IDEA.

### The Project Files Appear and Disappear

Move the project out of OneDrive, iCloud, or Dropbox. Copy it to the local `IdeaProjects` folder and open the local copy.

### A Cell Cannot Find a Variable or Function

Notebook cells depend on previously executed cells. Restart the Kotlin kernel and run all cells from top to bottom.