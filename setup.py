#!/usr/bin/python3
# setup.py

import setuptools


with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='pyconfig-env',
    version='1.0.0',
    author='Ashish D\'Souza',
    author_email='sudouser512@gmail.com',
    description='Automatic Python Environment Variable Configuration',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/computer-geek64/pyconfig',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
