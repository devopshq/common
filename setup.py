#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
import os

__version__ = '1.0'

devStatus = '4 - Beta'  # Билд-статус по умолчанию, смотрите: https://pypi.python.org/pypi?%3Aaction=list_classifiers

# Логика версионирования в зависимости от веток настраивается ниже:
if 'TRAVIS_BUILD_NUMBER' in os.environ and 'TRAVIS_BRANCH' in os.environ:
    print("This is TRAVIS-CI build")
    print("TRAVIS_BUILD_NUMBER = {}".format(os.environ['TRAVIS_BUILD_NUMBER']))
    print("TRAVIS_BRANCH = {}".format(os.environ['TRAVIS_BRANCH']))

    __version__ += '.{}{}'.format(
        '' if 'release' in os.environ['TRAVIS_BRANCH'] or os.environ['TRAVIS_BRANCH'] == 'master' else 'dev',
        os.environ['TRAVIS_BUILD_NUMBER'],
    )

    devStatus = '5 - Production/Stable' if 'release' in os.environ['TRAVIS_BRANCH'] or os.environ['TRAVIS_BRANCH'] == 'master' else devStatus

else:
    print("This is local build")
    __version__ += '.dev0'  # set version as major.minor.localbuild if local build: python setup.py install

print("dohq-common build version = {}".format(__version__))  # Перед сборкой выведется сообщение о том, какая версия собирается

setup(
    name='dohq-common',

    version=__version__,

    description='Common libs for devopshq tools',

    long_description='Common libs for devopshq tools',

    license='MIT',

    author='Open DevOps Community',

    author_email='devopshq@gmail.com',

    url='https://devopshq.github.io/dohq-common/',

    download_url='https://github.com/devopshq/dohq-common.git',

    entry_points={'console_scripts': ['exampleproject = exampleproject.Main:Main']},  # Точка входа указывает на основной метод, который нужно запустить при запуске программы из консоли. Например, если основной модуль в пакете exampleproject называется Main, то в данном примере будет запущен метод Main() этого скрипта, если вы наберёте в консоли команду "exampleproject".

    classifiers=[
        'Development Status :: {}'.format(devStatus),
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=[
        'DevOpsHQ',
        'devops',
    ],

    packages=[
        'dohq-common',
    ],

    setup_requires=[ 
    ],

    tests_require=[
        'pytest',
    ],

    install_requires=[ 
    ],

    package_data={  # необходимо перечислить ВСЕ файлы, которые должны войти в итоговый пакет, например:
        '': [
            './dohq-common/*.py',
            'LICENSE',  # файл лицензии нужно добавить в пакет
            'README.md',  # файл документации нужно добавить в пакет
            'README_EN.md',  # файл документации на английском нужно также добавить в пакет
        ],
    },

    zip_safe=True,
)
