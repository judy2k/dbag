import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dicebag",
    version="0.0.1",
    description="An infinite bag of dice.",
    long_description=long_description,
    author="Mark Smith",
    author_email="judy@judy.co.uk",
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    py_modules="dicebag",
    python_requires=">=3.6.0",  # f-strings
)
