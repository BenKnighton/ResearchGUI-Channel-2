"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['a4_channel_2_update.py']
DATA_FILES = []
OPTIONS = {}

setup(
    name="Channel_2_Ver_4",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
