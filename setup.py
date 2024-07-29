from setuptools import setup, find_packages

setup(
    name="fh-matplotlib",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["matplotlib", "python-fasthtml"],
    extras_require={
        "dev": ["pytest"],
    },
)
