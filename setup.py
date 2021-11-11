from os import path
from setuptools import find_packages, setup

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    README = f.read()


setup(
    name="ormgrop",
    version="0.2.0",
    description="DevL's own standard library for Python 3",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://devl.github.io/ormgrop",
    author="Lennart Fridén",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="utility library",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires="~=3.8",
    extras_require={"test": ["pytest", "pytest-describe"]},
    project_urls={
        "Bug Reports": "https://github.com/DevL/ormgrop/issues",
        "Source": "https://github.com/DevL/ormgrop",
    },
)
