#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension
from glob import glob
pysmile_module = Extension('_pysmile',
                           sources=['pysmile_wrap.cpp'],
			   include_dirs=["smile-lib"],
			   extra_objects=[ "smile-lib/libsmile.a", "smile-lib/libsmilearn.a"]
                           )

setup (name = 'pysmile',
       version = '0.1',
       author      = "Kai Londenberg - based on SMILE and SMILEARN Copyright (c) 1996-2006 by Decision Systems Laboratory, University of Pittsburgh.",
       description = """A SWIG generated wrapper around the SMILE and SMILEARN Libraries""",
       ext_modules = [pysmile_module],
       py_modules = ["pysmile"],
       )