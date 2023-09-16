#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "a2ln-server",
    version = "1.2",
    author = "Basil",
    author_email = "ocsps2@protonmail.com",
    description= ("A way to display Android phone notifications on Linux (Server)"),
    license = "GPL-3",
    url = "https://github.com/OCsonic/a2ln-server",
    packages = ["src"],
    requires=["argparse"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Package"
        "License :: OSI Approved :: GPL-3"
    ],
)

