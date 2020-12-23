#!/bin/bash
#------------------------------------
# FileName:     build.sh
# Revision:     0.1                  
# Language:     bash                 
# Author:       liming.wei           
# Date:         2020-12-23
# Description:                      
#------------------------------------

rm -rf dist
python setup.py sdist bdist_wheel
python3 -m twine upload dist/*
