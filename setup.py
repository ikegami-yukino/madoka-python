# -*- coding: utf-8 -*-
import glob
import os
import re

from setuptools import Extension, setup

with open(os.path.join('madoka', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

MADOKA_FILES = glob.glob('src/*.cc')

setup(
    name='madoka',
    version=version,
    author="Yukino Ikegami",
    author_email="yknikgm@gmail.com",
    url='https://github.com/ikegami-yukino/madoka-python',
    description="""Memory-efficient CountMin Sketch key-value structure (based on Madoka C++ library)""",
    long_description='%s\n\n%s' % (open('README.rst', encoding='utf8').read(),
                                   open('CHANGES.rst', encoding='utf8').read()),

    packages=['madoka'],
    ext_modules=[
        Extension('_madoka',
                  sources=['madoka_wrap.cxx'] + MADOKA_FILES,
                  language="c++",
                  extra_compile_args=["-std=c++11"]
                  ),
    ],

    license='New BSD License',
    keywords=['Count-Min Sketch', 'counter', 'word count'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        "Programming Language :: Python :: Free Threading",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
