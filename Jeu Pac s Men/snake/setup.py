from distutils.core import setup
import py2exe

setup(version = '1.0',
    description = 'A sample snake game.',
    name = 'Snake Game',
    windows = ['game.py'])