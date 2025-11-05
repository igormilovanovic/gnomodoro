#!/usr/bin/env python3
"""Setup script for Gnomodoro"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="gnomodoro",
    version="1.0.0",
    description="A simple and elegant Pomodoro timer for GNOME desktop",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Igor Milovanovic",
    author_email="",
    url="https://github.com/igormilovanovic/gnomodoro",
    packages=find_packages(),
    install_requires=[
        "PyGObject>=3.42.0",
        "pycairo>=1.20.0",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "gnomodoro=gnomodoro.app:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Utilities",
    ],
    keywords="pomodoro timer productivity gnome gtk",
    project_urls={
        "Bug Reports": "https://github.com/igormilovanovic/gnomodoro/issues",
        "Source": "https://github.com/igormilovanovic/gnomodoro",
    },
)
