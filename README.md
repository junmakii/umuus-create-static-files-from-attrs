
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