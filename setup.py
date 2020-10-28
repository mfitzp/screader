import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="screader",
    version="0.0.1",
    author="Martin Fitzpatrick",
    author_email="martin.fitzpatrick@gmail.com",
    description="Extract text from Sam Coupe Entropy reader files (as seen on FRED).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mfitzp/screader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    entry_points = {
        'console_scripts': ['screader=screader.commands.screader:main'],
    }
)