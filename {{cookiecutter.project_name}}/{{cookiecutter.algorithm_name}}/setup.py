# encoding: utf-8

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

with open(path.join(this_directory, 'version')) as f:
    version = f.readline()

with open(path.join(this_directory, 'requirements.txt')) as f:
    requires = f.readlines()

formated_requeires = [x.strip() for x in requires if x.strip() != '']
setup(
    name="{{cookiecutter.algorithm_name}}",
    version=version,
    description="{{cookiecutter.project_description}}",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="{{cookiecutter.project_author_name}}",
    author_email="{{cookiecutter.project_author_email}}",
    license='MIT',
    install_requires=formated_requeires,
    packages=find_packages(),
)