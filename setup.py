#!/usr/bin/python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gmail-cli',
    version='v0.0.1',
    packages=find_packages(),
    license='BSD',
    description='Send e-mails via the CLI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Florents Tselai',
    author_email='florents@tselai.com',
    url='https://github.com/Florents-Tselai/gmail-cli'
)
