# coding:utf-8
try:
    from setuptools import setup
    kw = {
        'install_requires':[
            ],
        }
except ImportError:
    from distutils.core import setup
    kw = {}

setup(
    name = 'xml2json',
    version = '1.1',
    description = 'xml2json',
    packages = ['xml2json'],
    author = 'dyf',
    author_email = '1821367759@qq.com',
    package_data={},
    **kw
    )


