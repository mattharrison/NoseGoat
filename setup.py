# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='NoseGoat',
      version='0.1',
      author='Matt Harrison',
      author_email = 'matthewharrison@gmail.com',
      description = 'Use the goat Luke!',
      long_description = 'Nose Plugin for goat enableation',
      platforms = 'goats eat anything',
      url='https://github.com/mattharrison/NoseGoat',
      license = 'PSF',
      py_modules=['nosegoat'],
      install_requires = ['nose>=0.10.0'],
      entry_points = { 'nose.plugins.0.10': ['goat = nosegoat:GoatPlugin']})
