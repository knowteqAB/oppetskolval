# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='oppetskolval',
    version='0.0.0',
    description='School assignment library for the swedish school system',
    long_description=readme,
    author='Knowteq AB',
    author_email='info@knowteq.se',
    url='https://github.com/knowteqAB/oppetskolval',
    license=license,
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
