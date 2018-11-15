#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A package.

umuus-create-static-files-from-attrs
====================================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-create-static-files-from-attrs.git

Usage
-----

    _statis_files_ = [
        {"path": "Dockerfile",
         "type": "content",
         "content": "FROM ..."},
    ]

    $ python umuus_create_static_files_from_attrs.py  run --file FILE.py --output_dir /tmp/OUTPUT_DIR

Example
-------

    $ umuus_create_static_files_from_attrs

    >>> import umuus_create_static_files_from_attrs

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>

"""
import os
import sys
import re
import logging
import functools
import parso
import fire
import shutil
import distutils.dir_util
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-create-static-files-from-attrs'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'parso',
]
__dependency_links__ = [
]
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
]
__entry_points__ = {'console_scripts': ['umuus_create_static_files_from_attrs = umuus_create_static_files_from_attrs:main']}
_statis_files_ = []
umuus_create_static_files_from_attrs = __import__(__name__)
logger = logging.getLogger(__name__)


def get_attr(attr, file):
    module = parso.parse(open(__file__).read())
    for i in range(len(module.children)):
        if (isinstance(module.children[i],
                       parso.python.tree.PythonNode)
            and isinstance(module.children[i].children[0],
                           parso.python.tree.ExprStmt)):
            name = module.children[i].children[0].children[0].value
            if name == attr:
                return eval(module.children[i].children[0].children[0].get_code())


def run(file, output_dir='/tmp'):
    # print(module.get_code())
    for item in get_attr('_statis_files_', __file__) or []:
        if item.get('type') == 'content':
            output = os.path.join(output_dir, item['path'])
            file_output_dir = os.path.dirname(output)
            if not os.path.exists(os.path.dirname(file_output_dir)):
                os.makedirs(file_output_dir)
            open(output, 'w').write(item['content'])
        if item.get('type') == 'copy':
            source = os.path.join(os.path.dirname(file), item['path'])
            output = os.path.join(output_dir, item['path'])
            distutils.dir_util.copy_tree(source, output)
    return


def copy(src, dest):
    if os.path.isdir(src):
        distutils.dir_util.copy_tree(src, dest)
    if os.path.isfile(src):
        shutil.copy2(src, dest)


def main(argv=[]):  # type: int
    args = argv or sys.argv
    fire.Fire()
    return 0


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    sys.exit(main(sys.argv))
