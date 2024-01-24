#!/bin/sh

# check_if_installed() {
#   if ! dpkg -s $1 >/dev/null 2>&1; then
#     echo $1 not found, installing...
#     sudo apt install $1
#   else
#     echo $1 is already installed
#   fi
# }

echo creating a venv for python

python -m venv .venv

. .venv/bin/activate

echo virtual environment created

echo installing dependencies

pip install -r requirements.txt

echo dependencies installed

echo running the script... 

python main.py