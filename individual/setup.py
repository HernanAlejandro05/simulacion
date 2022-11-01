# Setup Project
# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder

from setuptools import setup, find_packages

setup(name='individual', version='0.1', packages=find_packages())

# run `pip install -e .` inside individual folder

# Example:
# $ cd individual
# $ pip install -e .
