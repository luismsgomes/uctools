from setuptools import setup, find_packages
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='uctools',
    version="1.1.1",
    description='Tools for showing information about unicode characters.',
    long_description=read('README.rst'),
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
    python_requires='>=3',
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
