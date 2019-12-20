# Cookiecutter Blender Addon
An opinionated cookiecutter template for a Blender addon.

## Features
- Easy inclusion of third party dependencies.
- Single command packaging.

## Getting Started
Install the latest Cookiecutter if you haven't installed it yet.

`pip install cookiecutter`

Generate a Blender addon project:

`cookiecutter https://github.com/joshuaskelly/cookiecutter-blender-addon.git`

Then:
- Add custom functionality to `operators.py` or `panels.py`.
- Add any dependencies to the `requirements.txt` [Requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
- Package addon with `python package.py`
- Ship it!
