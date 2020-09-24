import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CyanBrown",  # Replace with your own username
    version="0.0.1",
    author="Cyan Brown",
    author_email="cyanbrown29@gmail.com",
    description="Calculates kinematics and projectiles, has a graphing feature.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CyanBrown/PhysicsCalculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
