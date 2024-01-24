#!bin/sh

echo creating a venv for python

source .venv/bin/activate

echo virtual enviroment created

echo installing dependencies

pip install -r requirements.txt

echo dependencies installed

echo running the script... 

python main.py