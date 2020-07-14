from setuptools import setup

setup(
    name='uctools',
    version="1.3.0",
    description='Unicode tools.',
    long_description=open('README.rst').read(),
    url='https://github.com/luismsgomes/uctools',
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
    py_modules=['ucinfo', 'ucenum', 'ucnorm'],
    entry_points={
        'console_scripts': [
            'ucinfo=ucinfo:_main',
            'ucenum=ucenum:_main',
            'ucnorm=ucnorm:_main',
        ],
    },
)
