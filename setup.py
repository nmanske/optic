from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name        = 'optic',
    version     = '0.0.5',
    description = 'Easily display command-line options',
    url         = 'https://github.com/nmanske/optic',
    author      = 'Nathan Manske',
    author_email= 'nathaniel.manske@gmail.com',
    license     = 'GPL3',

    include_package_data = True,
    scripts     = ['bin/optic'],
)
