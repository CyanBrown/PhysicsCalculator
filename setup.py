import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="basic-physics-calculator",
    version="1.0.0",
    description="Calculate basic physics functions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Cyan Brown",
    author_email="cyanbrown29@gmail.com",
    license="None",
    classifiers=[
        "License :: None",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8.3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": []
    },
)
