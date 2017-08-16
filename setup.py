from setuptools import setup, find_packages
from os.path import join, dirname
import prodcal



setup(
    name='production-calendar',
    version=prodcal.__version__,
    packages=find_packages(),
    author='Vladimir Sidorov',
    license='Apache 2.0',
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'License :: Freeware',
                 'License :: OSI Approved :: Apache Software License',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Office/Business',
                 'Topic :: Office/Business :: Scheduling',
                 'Topic :: Utilities'],

)