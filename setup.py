
import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='MP_Pandas',
    version='0.1',
    author='josepm,amro-pydev',
    author_email='amrsfmt@yahoo.com',
    maintainer='Amro Tork',
    maintainer_email='amrsfmt@yahoo.com',
    url='https://github.com/amro-pydev/MP_Pandas.git',
    license="BSD",
    description='Pandas Multiprocessing Support',
    long_description='Python Multiprocesing Support',
    packages=['pandas_multiprocessing'],
    install_requires=required,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering'
    ]
)
