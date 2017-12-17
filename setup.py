# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


from setuptools import setup


version = "1.0.0"

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "nested_print",
    packages = ["nested_print"],
    version = version,
    description = "A lightweight nested printing, for all your function within loops within function needs",
    long_description = long_descr,
    author = "Joey Sham",
    author_email = "sham.joey@gmail.com",
    url = "https://github.com/joeyism/py-nested_print"
    )
