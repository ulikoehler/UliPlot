#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 0):
    print('ERROR: UliPlot currently requires at least Python 3.0 to run.')
    sys.exit(1)

setup(name='UliPlot',
      version='0.2.1',
      description='Utilities for convenient plotting using matplotlib and other pydata libraries',
      author='Uli Köhler',
      author_email='ukoehler@techoverflow.net',
      url='https://techoverflow.net/',
      license='Apache License v2.0',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=['numpy (>= 1.5)', 'matplotlib', 'openpyxl'],
      extras_require= {
        'SciPy functionality': ['scipy (>= 0.5)'],
        'Pandas functionality': ['pandas'],
      },
      test_suite='tests',
      tests_require=['coverage', 'mock', 'parameterized'],
      platforms="any",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: DFSG approved',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Matplotlib',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Information Analysis'
      ]
)
