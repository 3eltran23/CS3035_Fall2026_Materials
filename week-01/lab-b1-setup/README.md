# Lab B1: Development Environment Setup

# Lab B1: Development Environment Setup

---

Students install the required tools for Python, Kotlin, and C. They then verify that each language environment works correctly by running a small program.

## Development Tools and Installation

---

Install the tools for all three languages before completing the verification procedure. Unless your instructor approves an alternative, use the recommended environments below so that course demonstrations and troubleshooting steps match your computer.

### Kotlin: IntelliJ IDEA

---

1. [Install IntelliJ IDEA](https://www.jetbrains.com/help/idea/installation-guide.html).
2. Eligible students may apply for the free [JetBrains Student Pack](https://www.jetbrains.com/shop/eform/v2/students), which includes IntelliJ IDEA Ultimate.
3. IntelliJ IDEA Ultimate is optional; the free IntelliJ IDEA features are sufficient for CS 3035.
4. Follow the official guide to [create and run a Kotlin console application](https://kotlinlang.org/docs/jvm-get-started.html).
5. Open the official [Kotlin Notebook plugin page](https://plugins.jetbrains.com/plugin/16340-kotlin-notebook). In IntelliJ IDEA, open **Settings/Preferences → Plugins → Marketplace**, search for **Kotlin Notebook**, install it, and restart IntelliJ IDEA if prompted.
6. Open the supplied `kotlin/kotlin_setup.ipynb` file in IntelliJ IDEA. Run its code cell by selecting the Run button or pressing **Shift+Enter**. Confirm that the notebook displays `Hello, CS 3035!` and the installed Kotlin version.



### Python: Visual Studio Code, Jupyter, and a Virtual Environment
---

Complete the following five steps.

#### Step 1: Install Python 3.14, Visual Studio Code, and the extensions
---

Follow the prerequisites in the official [Getting Started with Python in VS Code tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites). You must install these three separate components:

1. Python 3.14
2. Visual Studio Code
3. Microsoft's Python extension for Visual Studio Code

Also install Microsoft's [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) so that you can open and run the course's `.ipynb` notebooks in VS Code.

On macOS, install Python 3.14 with [Homebrew](https://formulae.brew.sh/formula/python@3.14):

```bash
brew install python@3.14
```

On Windows and Linux, follow the operating-system instructions in the VS Code Python tutorial. Do not install a Python 3.15 preview or beta release.

#### Step 2: Install Conda
---

Install Conda by following the official [Conda installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). The [Conda package overview](https://anaconda.org/channels/anaconda/packages/conda/overview) provides additional package information.

Conda is required for managing the Python environment in CS 3035.

#### Step 3: Create the `CS3035` environment
---

```bash
conda create --name CS3035 python=3.14 jupyterlab
```

#### Step 4: Activate the `CS3035` environment
---

You may complete all Python activation and verification commands using the integrated terminal in Visual Studio Code. Open it by selecting **Terminal → New Terminal**. Before running the program, confirm that the `CS3035` environment is active and selected as the current Python interpreter.

```bash
conda activate CS3035
```

In VS Code, open the Command Palette and select **Python: Select Interpreter**, then choose the interpreter associated with `CS3035`. When opening a Jupyter notebook, select the same `CS3035` environment as the notebook kernel. The integrated terminal prompt will normally begin with `(CS3035)` when the environment is active.

#### Step 5: Test the environment
---

Keep the `CS3035` environment active and run:

```bash
python --version
python python/hello.py
python -m pip --version
jupyter --version
```

The Python version must begin with `3.14`, and the program must display `Hello, CS 3035!`.

Open and test the supplied Python notebook in VS Code:

1. Open `python/python_setup.ipynb` from the verification folder.
2. Select **Kernel → Python Environments → CS3035** in the upper-right corner of the notebook.
3. Run the supplied code cell and confirm that the output includes `Hello, CS 3035!` and Python `3.14`.

See the official guide to [Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) and [selecting a Jupyter kernel](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).

### C: Visual Studio Code and a C Compiler
---

1. [Install Visual Studio Code](https://code.visualstudio.com/download) if you have not already installed it.
2. Install Microsoft's [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools).
3. Install a compiler using the guide for your operating system:
   - **Windows:** [Install GCC with MinGW-w64 using MSYS2](https://code.visualstudio.com/docs/cpp/config-mingw).
   - **macOS:** [Install Clang using the Xcode Command Line Tools](https://code.visualstudio.com/docs/cpp/config-clang-mac).
   - **Linux:** [Install GCC and configure VS Code](https://code.visualstudio.com/docs/cpp/config-linux).

Visual Studio Code is an editor and does not include a C compiler. Both the C/C++ extension and a compiler are required.

## Verification Procedure
---

Download the `verification` folder and open a terminal in that folder. Complete the three checks in order.

### 1. Python
---

Activate the `CS3035` environment, and then run:

```bash
python --version
python python/hello.py
python -m pip --version
jupyter --version
```

The `.py` program must display `Hello, CS 3035!` and Python `3.14.x`. Then open `python/python_setup.ipynb`, select the `CS3035` kernel, and run its verification cell. The notebook must also display Hello World and Python `3.14.x`.

### 2. Kotlin
---

1. Open `kotlin/Main.kt` in an IntelliJ IDEA Kotlin project.
2. Run `Main.kt` using the green Run button next to `main`. Confirm that the Run window displays Hello World and the Kotlin version.
3. Confirm that the Kotlin Notebook plugin is installed and enabled.
4. Open the supplied `kotlin/kotlin_setup.ipynb` file in IntelliJ IDEA.
5. Run its verification cell using the Run button or **Shift+Enter**.

Both `Main.kt` and `kotlin_setup.ipynb` must display `Hello, CS 3035!` and the installed Kotlin version.

### 3. C
---

On macOS or Linux, run:

```bash
cc --version
cc -std=c11 -Wall -Wextra c/hello.c -o c/hello
./c/hello
```

On Windows with GCC, run:

```powershell
gcc --version
gcc -std=c11 -Wall -Wextra c/hello.c -o c/hello.exe
.\c\hello.exe
```

On macOS, `cc --version` may display Apple Clang. In every operating system, the program should display `Hello, CS 3035!`.

## Required Evidence
---

- Kotlin: successful Hello World and version output from both `Main.kt` and `kotlin_setup.ipynb`
- Python: successful Hello World and Python 3.14 version output from both `hello.py` and `python_setup.ipynb`, using the active `CS3035` environment
- C: Visual Studio Code, C compiler version, successful compilation, and Hello World output



## Platform Notes
---

- A result is valid whether the student uses Windows, macOS, or Linux.
- Output such as version numbers and compiler names may differ by operating system.
- Students are evaluated on successful verification, not on having the same version shown in an example.
- If a command is missing, install that tool, close and reopen the terminal, and run the program again.

