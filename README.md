# Cookicutter for pylint score

This is a cookiecutter template for Python projects. It includes a pre-configured GitHub workflow for Pylint.

## Usage

1. Install cookiecutter if you haven't already:

```sh
pip install cookiecutter
```

2. Navigate to your new project directory:

3. Add the following line to your project's README.md:

```
[![Pylint](https://github.com/yourusername/your-new-project/actions/workflows/pylint-score.yml/badge.svg)](https://github.com/yourusername/your-new-project/actions/workflows/pylint-score.yml)
```
This will display the Pylint score as a badge in your README.

4. Run the following command:

```sh
cookiecutter https://github.com/collectiveai-team/pylint-github-action
```

## Features:
- Pre-configured Pylint GitHub workflow
- Post-generation hook to move .github folder to the correct location

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
MIT

