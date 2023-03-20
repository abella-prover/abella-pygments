#!/usr/bin/env python

"""Setup abella-pygments."""

from setuptools import setup, find_packages

entry_points = """
[pygments.lexers]
lprolog=abella_lexer:LPrologLexer
abella=abella_lexer:AbellaLexer
"""

setup(
    name = "abella-pygments",
    version = "0.0.1",
    description = "Pygments lexer package for Abella and λProlog",
    author = "Kaustuv Chaudhuri",
    author_email = "kaustuv@chaudhuri.info",
    url = "https://github.com/abella-prover/abella-pygments",
    packages = find_packages(),
    entry_points = entry_points,
    install_requires = ["Pygments>=2.0.1"],
    zip_safe = True,
    license = "Apache-2.0",
    classifiers = [
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Markup :: HTML",
        "Operating System :: OS Independent",
    ]
)
