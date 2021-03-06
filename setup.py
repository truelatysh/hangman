#!/usr/bin/env python3.6
# In[ ]:


"""Setup script."""

from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="Gleb Sinyakov",
    author_email="sinyakov@phystech.edu",
    url="http://github.com/truelatysh/hangman",
    license="MIT",
    packages=[
        "hangman",
        "tests"
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'hangman = hangman.__main__:main'
        ]
    }
)
