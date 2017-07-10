import setuptools

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

from sand import __version__

setuptools.setup(
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
    ],
    keywords=['Architecture', 'Network', 'Graph'],

    packages=['sand'],
    include_package_data=True,

    install_requires=[
        'bokeh==0.12.6',
        'cairocffi==0.8.0',
        'numpy==1.13.1',
        'pandas==0.20.2',
        'py2cytoscape==0.6.2',
        'python-igraph==0.7.1.post6',
    ],

    tests_require=[
        'pytest==3.1.3',
    ]
)
