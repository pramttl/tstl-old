#-*- coding:utf-8 -*-

from setuptools import setup, find_packages
import sys, os

setup(
    name='tstl',
    version='0.1',
    description='A template scripting testing language based on research by Dr. Alex Groce & Dr. Jervis Pinto.',
    long_description=open('README.md').read(),
    packages=['src',],
    include_package_data = True,
    package_data = {
        'src': ['static/boilerplate.py', 'static/boilerplate_cov.py'],
    },
    entry_points="""
    [console_scripts]
    tstl = src.harnessmaker:main
    """,
    keywords='testing tstl',
)


