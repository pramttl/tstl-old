#-*- coding:utf-8 -*-

from setuptools import setup, find_packages
import sys, os

setup(
    name='tstl',
    version='0.1',
    description='A template scripting testing language based on research by Dr. Alex Groce & Dr. Jervis Pinto.',
    long_description=open('README.md').read(),
    packages=['src',],
    entry_points="""
    [console_scripts]
    tstl = src.harnessmaker
    """,
    keywords='testing tstl',
    classifiers=[
      "Intended Audience :: Developers",
      "Development Status :: 1 - Alpha",
      "Programming Language :: Python :: 2",
      ],
    include_package_data = True,
)


