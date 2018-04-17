#!/usr/bin/env python
#coding=utf-8

import os
from setuptools import setup

# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "calcs",
    version = "0.1.0",
    author = "Maria Telenczuk",
    author_email = "maria@telenczuk.pl",
    description = "simulates neuron and calculates lfp",
    license = "MIT",
    packages = ['calcs'],
    long_description = read('README.md'),
    classifiers = [
        "License :: OSI Approved :: MIT License"
    ],
)
