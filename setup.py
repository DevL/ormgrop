from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="ormgrop",
    version="0.1.0",
    description="DevL's own standard library for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevL/ormgrop",
    author="Lennart Fridén",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="utility library",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires="~=3.5",
    install_requires=[],
    extras_require={"dev": [], "test": []},
    project_urls={
        "Bug Reports": "https://github.com/DevL/ormgrop/issues",
        "Source": "https://github.com/DevL/ormgrop",
    },
)
