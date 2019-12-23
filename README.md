# [![cookiecutter-blender-addon](https://raw.githubusercontent.com/joshuaskelly/cookiecutter-blender-addon/master/.media/logo.svg?sanitize=true)](https://github.com/JoshuaSkelly/cookiecutter-blender-addon)

# Cookiecutter Blender Addon

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)]() [![Discord](https://img.shields.io/badge/discord-chat-7289DA.svg)](https://discord.gg/KvwmdXA)

A sweet and opinionated cookiecutter template for creating a Blender addon.

## Features
- Project is structured as a Python package.
- Easy inclusion of third party dependencies.
- Single command packaging.

## Getting Started
Install the latest Cookiecutter if you haven't installed it yet.

$ `pip install cookiecutter`

Generate a Blender addon project:

$ `cookiecutter https://github.com/joshuaskelly/cookiecutter-blender-addon.git`

Then:
- Add custom functionality to `operators.py` or `panels.py`.
- Add any dependencies to the `requirements.txt` [Requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
- Package addon with $ `python package.py`
- Installable addon zip file will be in the `dist` folder.
