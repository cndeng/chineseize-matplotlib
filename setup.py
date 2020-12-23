# encoding: utf8
from distutils.core import setup
from setuptools import find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['matplotlib']

setup(name='chineseize-matplotlib',
      version='1.2',
      description='自动设置matplotlib的中文字体',
      author='cndeng',
      author_email='cndeng@foxmail.com',
      url='https://github.com/cndeng/chineseize-matplotlib',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=find_packages(),
      install_requires=install_requires,
      include_package_data=True,
      package_data={
          'chineseize_matplotlib': ['fonts/*'],
      })
