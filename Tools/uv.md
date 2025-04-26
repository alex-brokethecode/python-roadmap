# uv: An Extremely Fast Python Package Installer and Resolver

[uv](https://docs.astral.sh/uv/getting-started/installation/) is a new, incredibly fast Python package installer and resolver, aiming to significantly improve the speed and efficiency of tasks traditionally handled by pip and pip-tools. It's written in Rust and offers substantial performance gains for installing, updating, and managing Python dependencies.

## Installation

The recommended way to install uv is directly using pip:

1.  **Ensure pip is up-to-date:**

    ```bash
    python -m pip install --upgrade pip
    ```

2.  **Install uv:**

    ```bash
    pip install uv
    ```

    It's generally recommended to install uv globally so you can access the `uv` command from any project.

    ```shell
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

## Basic Usage

uv provides its own commands for package management and project tasks. Here are some common use cases:

- **Adding Dependencies:**

  To add a dependency to your project (similar to `pip install <package_name>` and updating `requirements.txt` or `pyproject.toml`):

  ```bash
  uv add requests
  uv add django uvicorn
  uv add --dev pytest  # Add as a development dependency (if using uv project features)
  ```

  **Note:** The behavior of `uv add` might depend on whether you have initialized a uv project (using `uv init`). In a uv project, it will likely update your project manifest (e.g., `pyproject.toml`). Outside of a uv project, it might behave more like a direct installation.

- **Running Scripts:**

  uv can run Python scripts directly, managing their dependencies if declared within the script using inline metadata (`# /// script ... # ///`).

  ```bash
  uv run your_script.py
  ```

  You can also specify dependencies when running a script:

  ```bash
  uv run --with requests your_script.py
  ```

- **Initializing a New Project:**

  To start a new uv-managed project:

  ```bash
  uv init your_project_name
  cd your_project_name

  # optionally
  uv init your_project_name --python 12.3
  ```

- **Managing Python versions**

  ```shell
  uv python list # list available python versions
  uv python install <version>
  uv python uninstall <version>
  ```

- **Managing Virtual Environments:**

  uv can create and manage virtual environments:

  ```bash
  uv venv
  ```

  This creates a `.venv` directory. You can then activate it using the standard commands for your shell (e.g., `source .venv/bin/activate` on Unix-like systems, `.venv\Scripts\activate` on Windows).

- **Installing Project Dependencies:**

  If you have a `pyproject.toml` file (common in modern Python projects), you can install all project dependencies:

  ```bash
  uv pip sync  # Similar to pip install -r requirements.txt, but leverages uv's speed
  ```

  or

  ```bash
  uv sync      # If you are within a uv-initialized project
  ```

- **Resolving Dependencies and Generating Lockfiles:**

  uv can resolve dependencies and generate a `uv.lock` file for reproducible builds:

  ```bash
  uv lock
  ```

- **Running Tools:**

  uv can run Python-based command-line tools:

  ```bash
  uv run ruff .       # Run Ruff linter
  uv run mypy my_package  # Run MyPy type checker
  ```

- **Installing Tools Globally:**

  You can install tools globally using `uv tool install`:

  ```bash
  uv tool install ruff
  uv tool install black
  ```

  These tools become available in your system's PATH.

- **Display tree dependencies**

  ```shell
  uv tree
  ```

- **Display packages**

  ```shell
  uv pip list # list packages
  uv pip show <package> # package info
  ```

## Integration with Development Tools (VS Code Example)

While there isn't a dedicated "uv" extension for VS Code at the time of this writing, you can still leverage its speed by using it in your terminal and configuring Python extensions to use the environment managed by uv.

1.  **Install uv globally.**
2.  **Init your project with `uv init <name> --python <version>`**
3.  **Create and manage your virtual environment using `uv venv`.**
4.  **Activate the virtual environment.**
5.  **Install your project dependencies using `uv pip sync` or `uv add`.**
6.  **Configure your VS Code Python extension:**

    - In VS Code settings (Ctrl+, or Cmd+,), search for `Python: Python Path`.
    - Set the Python Path to the Python executable within your uv-managed virtual environment (e.g., `.venv/bin/python`).

    This ensures that VS Code's linters, formatters, and other Python tools operate within the fast uv environment. For formatters and linters, you would still configure them (e.g., set Ruff or Black as the formatter, and Ruff or Pylint as the linter), and they will use the packages installed by uv in your virtual environment.
