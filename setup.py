import re
from setuptools import setup


def find_version(filename):
    """
    Search for assignment of __version__ string in given file and
    return what it is assigned to.
    """
    with open(filename, "r") as filep:
        version_file = filep.read()
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
        )
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")


setup(
    name="rechelpers",
    version=find_version("rechelpers/rechelpers.py"),
    description="My rechelpers shite",
    long_description=open("README.rst", "r").read(),
    url="https://github.com/szero/rechelpers",
    license="ISC",
    author="szero",
    author_email="singleton@tfwno.gf",
    packages=["rechelpers"],
    entry_points={
        "console_scripts": [
            "move2folders = rechelpers._move2folders:run",
            "namefromtags = rechelpers._namefromtags:run",
        ]
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[l.strip() for l in open("requirements.txt").readlines()],
)
