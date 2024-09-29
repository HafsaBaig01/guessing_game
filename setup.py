from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))


setup(
    name="guessing_game",
    version="0.1",
    description="A simple number guessing game",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Hafsa Baig",
    author_email="hafsamughal27@gmail.com",
    url="https://github.com/yourusername/guessing_game",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
