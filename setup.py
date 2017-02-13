#!/usr/bin/env python
from setuptools import setup, find_packages
import unittest

def my_test_suite():
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


long_description = 'python3-vim, python3-vim-bridge'

setup(
    name='vim_bridge3',
    version='3.0rc1',
    description='A Python-to-Vim bridge decorator that allows transparent calls to Python functions in native Vim scripts.',
    author='Hector Acosta, Vincent Driessen, Walter Doekes',
    author_email='wjdoekes+github@wjd.nu',
    url='https://github.com/ossobv/vim-rst-tables-py3/tree/master/vendor',
    platforms=['any'],
    license='BSD',
    package_dir={'': 'vendor'},
    packages=['vim', 'vim_bridge'],
    install_requires=[],
    tests_require=['mock'],
    test_suite='setup.my_test_suite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Topic :: Text Editors',
    ],
    long_description=long_description,
)
