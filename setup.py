# -*- coding: utf-8 -*-
from setuptools import setup

extra_requires = []

setup(name='NoseGoat',
      version='0.1',
      author='Matt Harrison',
      author_email = 'matthewharrison@gmail.com',
      description = 'Use the goat Luke!',
      license = 'PSF',
      py_modules=['nosegoat'],
      install_requires = ['nose>=0.10.0'] + extra_requires,
      entry_points = { 'nose.plugins.0.10': ['goat = nosegoat:GoatPlugin']})
