#!/bin/sh

check_if_installed() {
  if ! dpkg -s $1 >/dev/null 2>&1; then
    echo $1 not found, installing...
    sudo apt install $1
  else
    echo $1 is already installed
  fi
}

check_python_package() {
	if ! pip show $1 >/dev/null 2>&1; then
		echo $1 not found, installing...
		pip install $1
	fi
#   else
#     echo $1 is already installed
#   fi
}

echo creating a venv for python

python -m venv .venv

. .venv/bin/activate

echo virtual environment created

echo installing dependencies

while read package; do
  check_if_installed $package
done < dependencies.txt

while read package; do
  check_python_package $package
done < requirements.txt

echo dependencies installed

echo running the script...

python main.py