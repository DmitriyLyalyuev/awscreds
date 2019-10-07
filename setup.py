# -*- coding: utf-8 -*-
import re
from setuptools import setup

REQUIRES = [
    'keyring'
]


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def readme():
    try:
        with open('Readme.md') as f:
            return f.read()
    except IOError:
        return """
"""

__version__ = find_version("awscreds/__init__.py")

setup(
    name="awscreds",
    version=__version__,
    description="awscreds stores AWS credentials in OS's secure storage",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Dmitriy Lyalyuev",
    author_email="dmitriy@lyalyuev.info",
    url="https://github.com/DmitriyLyalyuev/awscreds",
    packages=["awscreds"],
    install_requires=REQUIRES,
    include_package_data=True,
    license="MIT",
    scripts=['awscreds/awscreds'],
    keywords="ssh aws devops sysadmin",
    classifiers=[
        "Environment :: MacOS X",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
)
