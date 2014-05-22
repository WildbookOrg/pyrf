#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
from utool.util_setup import setuptools_setup
from utool.util_cplat import get_dynamic_lib_globstrs
import sys
import subprocess
import pyrf


def build_command():
    """ Build command run by utool.util_setup """
    if sys.platform.startswith('win32'):
        subprocess.call(['mingw_pyrf_build.bat'])
    else:
        try:
            subprocess.call(['unix_pyrf_build.sh'])
        except OSError:
            # Try fallback
            import os
            os.system('./unix_pyrf_build.sh')

INSTALL_REQUIRES = [
    'detecttools >= 1.0.0.dev1'
]

if __name__ == '__main__':
    setuptools_setup(
        setup_fpath=__file__,
        module=pyrf,
        build_command=build_command,
        description=('Detects objects in images using random forests'),
        url='https://github.com/bluemellophone/pyrf',
        author='Jason Parham',
        author_email='bluemellophone@gmail.com',
        packages=['pyrf'],
        install_requires=INSTALL_REQUIRES,
        package_data={'build': get_dynamic_lib_globstrs()},
    )
