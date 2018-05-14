#
# Author: jun10000 (https://github.com/jun10000)
#

import os
from distutils.core import setup
from Cython.Build import cythonize

pyx_files = []
for file in os.listdir('.'):
    (base, ext) = os.path.splitext(file)
    if ext == '.pyx':
        pyx_files.append(file)

setup(
    ext_modules = cythonize(pyx_files),
    requires=['Cython'])
