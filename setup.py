# coding=utf-8
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='data-packer3',
    version='2.0.1',
    description='A Python library for packing and unpacking data between different container formats',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='sato',
    author_email='ysudqfs@163.com',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='data packing unpacking container',
)
