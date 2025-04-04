# Virtual Environments

## Theory

Virtual environments are isolated Python environments that allow you to manage project dependencies separately. This is crucial for preventing conflicts between different project dependencies and ensuring that your projects are reproducible.

### Key Concepts

- **Dependency Management:** Virtual environments allow you to install and manage project-specific packages without affecting the system-wide Python installation.
- **Isolation:** Each virtual environment is isolated from other environments, ensuring that packages installed in one environment don't interfere with others.
- **Reproducibility:** Virtual environments make it easy to recreate the exact environment used for a project, ensuring that it runs consistently on different machines.

### Tools

- `venv`: A built-in Python module for creating virtual environments (recommended for Python 3.3+).
- `virtualenv`: A third-party tool for creating virtual environments (older, but still widely used).
- `pipenv`: A tool that combines virtual environment and dependency management.
- `conda`: An open-source package management and environment management system.

### Basic venv Commands:

- Creating a Virtual Environment: `python -m venv <environment_name> (e.g., python -m venv myenv)`
- Activating a Virtual Environment:

  - Windows: `<environment_name>\Scripts\activate`
  - macOS/Linux: `source <environment_name>/bin/activate`

- Deactivating a Virtual Environment: `deactivate`
- Installing Packages: `pip install <package_name>`
- Freezing Dependencies: `pip freeze > requirements.txt` (creates a requirements.txt file listing installed packages)
- Installing from requirements.txt: `pip install -r requirements.txt`

### Example Workflow:

1. Create a virtual environment: `python -m venv myenv`
2. Activate the environment: `source myenv/bin/activate` (or `myenv\Scripts\activate` on Windows)
3. Install packages: `pip install requests`
4. Create a requirements.txt file: `pip freeze > requirements.txt`
5. Deactivate the environment: `deactivate`
6. To recreate the same enviroment, in a new folder, create the env, activate it and use: `pip install -r requirements.txt`
