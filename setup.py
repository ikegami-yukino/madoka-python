# -*- coding: utf-8 -*-
from codecs import open
import glob
import os
import re
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext

with open(os.path.join('madoka', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

MADOKA_FILES = glob.glob('src/*.cc')
setup(
    name='madoka',
    version=version,
    author="Yukino Ikegami",
    author_email='yukinoik@icloud.com',
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

    cmdclass={'build_ext': build_ext},

    license='New BSD License',
    keywords=['Count-Min Sketch', 'counter', 'word count'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
