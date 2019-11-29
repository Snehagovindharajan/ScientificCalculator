""" setup file to create egg"""
from setuptools import setup, find_packages

setup(

    name='mypackage',
    version='1.0.0',
    data_files=[('.', ["__main__.py"])],
    entry_points={'setuptools.installation': ['mypackage = src.main.main:main'], },
    packages=find_packages(exclude=['*tests*']),
)
