# Ruff

[Ruff](https://docs.astral.sh/ruff/tutorial/#getting-started) is a powerful and blazingly fast Python tool that combines linting, code formatting, and import sorting into a single, unified package. It aims to be a drop-in replacement for popular tools like Flake8, pycodestyle, pyflakes, isort, and potentially Black (though its formatting capabilities are a subset of Black's).

## Installation

The recommended way to install Ruff is within your project's virtual environment.

1.  **Activate your virtual environment:**

    Ensure your project's virtual environment is active. If you're using Poetry, it might look like:

    ```bash
    poetry shell
    ```

    If you're using `venv`:

    ```bash
    source .venv/bin/activate
    ```

2.  **Install Ruff:**

    Use `pip` to install Ruff:

    ```bash
    pip install ruff
    ```

    If you want to add it as a development dependency (recommended):

    - **Poetry:**
      ```bash
      poetry add --dev ruff
      ```
    - **pip (with requirements.txt):**
      Add `ruff` to your `requirements.txt` or `requirements-dev.txt` and run `pip install -r requirements-dev.txt`.

## VS Code Integration

To leverage Ruff's capabilities directly within VS Code, you'll want to install the official Ruff [extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

1.  **Install the Ruff VS Code Extension:**

    Open the Extensions view in VS Code (Ctrl+Shift+X or Cmd+Shift+X) and search for "Ruff". Install it.

2.  **Configure VS Code Settings (Recommended):**

    To enable Ruff for linting, formatting, and import sorting on save, you'll need to adjust your VS Code settings.

    - Open VS Code settings (Ctrl+, or Cmd+,).
    - Search for "Ruff".

    A good starting point is:

    ```json
    {
      "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "source.fixAll": "explicit",
          "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff"
      }
    }
    ```

    Optionally, you can add custom settings for Ruff in your `pyproject.toml` file (if you're using Poetry). For example, to change default double quotes to single quotes, you can add:

    ```toml
    [tool.ruff.format]
    quote-style = "single"
    ```

    Here are some key settings you might want to configure:

    - **`python.linting.enabled`**: Set this to `true` to enable Python linting in VS Code.
    - **`python.linting.linter`**: Set this to `"ruff"` to use Ruff as your linter.
    - **`python.formatting.provider`**: Set this to `"ruff"` to use Ruff for code formatting.
    - **`editor.formatOnSave`**: Set this to `true` to automatically format your Python files every time you save.
    - **`editor.codeActionsOnSave`**: You can configure code actions on save to automatically fix fixable linting issues and sort imports.
    - **`ruff.enabled`**: Ensure this is set to `true` to enable the Ruff extension.
    - **`ruff.formatOnSave`**: An alternative way to enable formatting on save specifically through the Ruff extension.
    - **`ruff.organizeImports`**: Enable Ruff's import sorting.
    - **`ruff.lintArgs`**: Allows you to pass command-line arguments to Ruff for linting (e.g., specifying specific error codes to ignore).
    - **`ruff.formatArgs`**: Allows you to pass command-line arguments to Ruff for formatting (though its formatting is currently a subset of Black).
    - **`ruff.path`**: If the `ruff` executable is not in your system's PATH, you can specify the full path here (e.g., `${workspaceFolder}/.venv/bin/ruff`).

## Usage in VS Code

With the extension installed and configured, Ruff will automatically work in your Python files:

- **Linting:** Ruff will analyze your code for potential errors and style violations, highlighting them in the editor and in the "Problems" panel.
- **Formatting:** When you save your Python files (if `editor.formatOnSave` or `ruff.formatOnSave` is enabled), Ruff will automatically format your code.
- **Import Sorting:** On save (if `editor.codeActionsOnSave` with `source.organizeImports.ruff` or `ruff.organizeImports` is enabled), Ruff will automatically sort your import statements according to its rules.
- **Fixing Issues:** You can use VS Code's "Quick Fix" feature (Ctrl+. or Cmd+.) to automatically apply fixes for some of the linting issues reported by Ruff.

## Command Line Usage (Optional)

You can also run Ruff directly from your terminal:

```bash
# Lint the current directory
ruff .

# Lint a specific file
ruff your_script.py

# Format a specific file
ruff format your_script.py

# Sort imports in a specific file
ruff organize-imports your_script.py

# Apply fixes for fixable linting errors
ruff --fix .
```
