"""Setup file for pypi"""
from pathlib import Path
from setuptools import setup, find_packages
from src.jmc import VERSION


with (Path(__file__).parent / 'README.md').open(encoding="utf-8") as file:
    README = "\n" + file.read()

DESCRIPTION = 'Compiler for JMC (JavaScript-like Minecraft Function), a mcfunction extension language for making Minecraft Datapack.'
version = VERSION.replace("-alpha.", "a").replace("-beta.", "b")[1:]

setup(
    name="jmcfunction",
    version=version,
    author="WingedSeal",
    author_email="<firm09719@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=README,
    packages=find_packages(),
    install_requires=[],
    keywords=[
        'python',
        'minecraft',
        'mcfunction',
        'datapack',
        'compiler'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)