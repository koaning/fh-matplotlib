from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="fh-matplotlib",
    description="Make is easy to use matplotlib in FastHTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vincent D. Warmerdam",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["matplotlib", "python-fasthtml"],
    extras_require={
        "dev": ["pytest"],
    },
)
