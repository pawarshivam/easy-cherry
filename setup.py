from distutils.core import setup
import py2exe 
import sys
import os
import configparser
import shutil
import git
import tabulate
import art
import pyperclip
import csv
import datetime
import copy

sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {
            'bundle_files': 1,
            'compressed': True
        },
    },
    console=[{
        'script': 'main.py'
    }],
    zipfile=None,
)
