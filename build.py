#!/usr/bin/env python
import os

source_dir = 'src'
output_dir = 'ftplugin'


def build():
    with open(os.path.join(source_dir, 'rst_tables.py')) as fp:
        py_src = fp.read()
    with open(os.path.join(source_dir, 'base.vim')) as fp:
        vim_src = fp.read()
    combined_src = vim_src.replace('__PYTHON_SOURCE__', py_src)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    output_path = os.path.join(output_dir, 'rst_tables.vim')
    with open(output_path, 'w') as fp:
        fp.write(combined_src)

if __name__ == '__main__':
    build()
