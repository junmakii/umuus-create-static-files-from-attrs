
from setuptools import setup, find_packages

setup(
    name='umuus_create_static_files_from_attrs',
    description='A package.',
    long_description=('A package.\n'
 '\n'
 'umuus-create-static-files-from-attrs\n'
 '====================================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install '
 'git+https://github.com/junmakii/umuus-create-static-files-from-attrs.git\n'
 '\n'
 'Usage\n'
 '-----\n'
 '\n'
 '    _statis_files_ = [\n'
 '        {"path": "Dockerfile",\n'
 '         "type": "content",\n'
 '         "content": "FROM ..."},\n'
 '    ]\n'
 '\n'
 '    $ python umuus_create_static_files_from_attrs.py  run --file FILE.py '
 '--output_dir /tmp/OUTPUT_DIR\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 '    $ umuus_create_static_files_from_attrs\n'
 '\n'
 '    >>> import umuus_create_static_files_from_attrs\n'
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    py_modules=['umuus_create_static_files_from_attrs'],
    version='0.1',
    url='https://github.com/junmakii/umuus-create-static-files-from-attrs',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['parso'],
    dependency_links=[],
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Natural Language :: English', 'Programming Language :: Python', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3'],
    entry_points={'console_scripts': ['umuus_create_static_files_from_attrs = umuus_create_static_files_from_attrs:main']}
)

