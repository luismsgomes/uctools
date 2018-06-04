from setuptools import setup, find_packages
from os import path
import re

setup(
    name='uctools',
    version="1.0.1",
    description='Tools for viewing unicode character names.',
    long_description="""This package provides the following tools:
    ucinfo -- writes on stdout the name of each unicode character read from stdin
    ucenum -- enumerates on stdout all unicode characters of a chosen category
    """,
    url='https://github.com/luismsgomes/ucinfo',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: General',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='text unicode character',
    package_dir={'': 'src'},
    py_modules=['ucinfo', 'ucenum'],
    entry_points={
        'console_scripts': [
            'ucinfo=ucinfo:main',
            'ucenum=ucenum:main',
        ],
    },
)
