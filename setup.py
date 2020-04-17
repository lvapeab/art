# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='art',
      version='0.1',
      description='Approximate randomization testing.',
      author='Sebastian Martschat',
      url='https://github.com/smartschat/art',
      download_url='https://github.com/smartschat/art/archive/master.zip',
      license='MIT',
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          "License :: OSI Approved :: MIT License"
      ],
      package_dir={'art': 'art',
                   },
      packages=['art',
                ],
      )
