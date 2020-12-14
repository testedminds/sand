from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

# Read version programmatically to avoid loading dependencies from sand/__init__.py
exec(open('sand/__version__.py').read())

setup(
    name='sand',
    version=__version__,
    description='SAND: System Architecture as a Network of Dependencies',
    long_description=long_description,
    url='https://github.com/testedminds/sand',
    author='Bobby Norton',
    author_email='bobby@testedminds.com',
    license='Apache License 2.0',

    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',

        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',

        'Environment :: Console',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['Architecture', 'Network', 'Graph'],

    packages=find_packages(exclude=('docker', 'docs', 'tests')),
    include_package_data=True,

    install_requires=[
        'bokeh>=2.0,<3.0',
        'cairocffi>=1.0,<2.0',
        'pandas>1.1,<2.0',
        'py2cytoscape>=0.7.1,<1.0',
        'python-igraph>=0.8.3,<1.0',
    ],
)
