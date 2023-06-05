from setuptools import setup, find_packages
from arbor import __version__ as current_version

setup(
    name="arbor",
    version=current_version,
    package_dir={"": "src"},
    python_requires=">=3.10",
    url="https://github.com/Huell-Howitzer/arbor",
    author="Ryan M. Howell",
    author_email="rmhowell@protonmail.com",
    description="Create directory structure from output of tree command.",
    # look for packages in 'src/' directory
    packages=find_packages(where="src"),
    # specify the src/ directory as the place to find packages
    install_requires=[],
    extras_require={"dev": ["pytest"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": ["arbor = arbor.__main__:main"],
    },
)
