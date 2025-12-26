The pyproject.toml file is a TOML file that specifies the project’s build system and many other configurations. In modern Python, this file replaces the setup.py script that you may have used before. 

Inside the rplife/ directory, you have the following files:

__init__.py enables rplife/ as a Python package.
__main__.py works as an entry-point script for the game.
cli.py contains the command-line interface for the game.
grid.py provides the life grid implementation.
patterns.py and patterns.toml handle the game’s patterns.
views.py implements a way to display the life grid and its evolution.