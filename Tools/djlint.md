# djlint: Enhanced Linting and Formatting for Django Templates

Unlike general formatters like Prettier, `djlint` is specifically designed to understand and handle the unique syntax of Django templates.

## Installation

The recommended way to install `djlint` is as a development dependency within your project's virtual environment. For `pip` users:

```bash
pip install -U djlint
```

In case you're using Poetry:

1.  **Activate your virtual environment:**

    If your virtual environment isn't already active, activate it using Poetry:

    ```bash
    poetry shell
    ```

2.  **Install `djlint` as a development dependency:**

    Use the following Poetry command to add `djlint` to your project's development dependencies:

    ```bash
    poetry add --dev djlint
    ```

    This command will download and install `djlint` and update your `pyproject.toml` and `poetry.lock` files accordingly.

## VS Code Integration

Integrating `djlint` with VS Code is straightforward and allows for on-demand formatting and linting directly within your editor.

1.  **Install the `djlint` VS Code Extension:**

    Search for the `djlint` extension in the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=monosans.djlint) (Ctrl+Shift+X or Cmd+Shift+X) and install it. The extension is typically named "djlint".

2.  **Configure VS Code Settings (Optional but Recommended):**

    To enable formatting on save and customize `djlint`'s behavior, you can modify your VS Code settings.

    - Open VS Code settings (Ctrl+, or Cmd+,).
    - Search for `djlint`.

    Here are some useful settings you might want to configure:

    - **`djlint.enable`**: Set this to `true` to enable the `djlint` extension.
    - **`editor.formatOnSave`**: If you want VS Code to automatically format your Django templates every time you save, set this to `true`. You might want to conditionally enable this for `.html` or `.djhtml` files if you are using other template languages.
    - **`editor.defaultFormatter`**: To make `djlint` the default formatter for Django template files, you can set this. You might need to identify the specific identifier for the `djlint` extension (check the extension's details in the Marketplace). A common pattern is `<publisher>.<extension-name>`, e.g., `monokai.djlint`.
    - **`djlint.configuration`**: This allows you to specify a `djlint.toml` configuration file for more advanced settings.
    - **`djlint.formatterPath`**: If `djlint` executable is not in your system's PATH, you can specify the full path to the `djlint` executable within your virtual environment (e.g., `./.venv/bin/djlint` or the path provided by `poetry show --directory djlint`).
    - **`djlint.linterPath`**: Similar to `formatterPath`, but for the `djlint` linter.
    - **`djlint.formatOnSaveExtensions`**: You can specify the file extensions that `djlint` should format on save (e.g., `[".html", ".djhtml"]`).

    **Example `settings.json` snippet:**

    ```json
    {
      // Other settings...
      "emmet.includeLanguages": {
        "django-html": "html",
        "jinja-html": "html"
      },
      "editor.formatOnSave": true,
      "[html][django-html][handlebars][hbs][mustache][jinja][jinja-html][nj][njk][nunjucks][twig]": {
        "editor.defaultFormatter": "monosans.djlint"
      }
    }
    ```

## Usage in VS Code

Once installed and configured, `djlint` will automatically format your Django template files according to your settings.

- **Format Document:** You can manually format the current Django template file by using the VS Code command `Format Document` (Shift+Alt+F or Shift+Option+F). If you have set `djlint` as the default formatter for `.html` or `.djhtml` files, it will be used.
- **Format on Save:** If you have enabled `editor.formatOnSave`, your Django templates will be automatically formatted every time you save the file.
- **Linting:** The `djlint` extension will also provide linting warnings and errors in the VS Code "Problems" panel, helping you identify potential issues in your templates.
