import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noyaki",
    version="0.0.1",
    author="ken",
    author_email="kent.adachi@adachi-honten.net",
    description="character span label to tokenized base label for Japanese text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ken11/noyaki",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
