# -*- coding: utf-8 -*-
b'This library requires pypy or Python 2.6, 2.7, 3.3 or newer'
import io
import os
import re
from setuptools import setup, find_packages


def get_path(*args):
    return os.path.join(os.path.dirname(__file__), *args)


def read_from(filepath):
    with io.open(filepath, 'rt', encoding='utf8') as f:
        return f.read()


def get_requirements(filename='requirements.txt'):
    data = read_from(get_path(filename))
    lines = map(lambda s: s.strip(), data.splitlines())
    return [l for l in lines if l and not l.startswith('#')]


data = read_from(get_path('voodoo', '__init__.py'))
version = str(re.search(r"__version__\s*=\s*u?'([^']+)'", data).group(1)).strip()
desc = str(re.search('"""(.+)"""', data, re.DOTALL).group(1)).strip()


setup(
    name='Voodoo',
    version=version,
    author='Juan-Pablo Scaletti',
    author_email='juanpablo@lucumalabs.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='http://github.com/lucuma/voodoo',
    license='MIT license (http://www.opensource.org/licenses/mit-license.php)',
    description='Template system for project skeletons',
    long_description=desc,
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
