#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Aron C",
    author_email='aronwc@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="utilies for github classroom",
    entry_points={
        'console_scripts': [
            'ghc-utils=ghc_utils.cli:main',
            'grades=ghc_utils.cli:grades',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description_content_type="text/markdown",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ghc_utils',
    name='ghc_utils',
    packages=find_packages(include=['ghc_utils', 'ghc_utils.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/aronwc/ghc_utils',
    version='0.1.0',
    zip_safe=False,
)
