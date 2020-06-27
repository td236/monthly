#!/bin/bash

echo 'creating virtual environment'
python3 -m venv venv
source venv/bin/activate

echo 'python libraries installation'
pip3 install -r requirements.txt

echo 'creating .flaskenv file'
touch .flaskenv
echo 'FLASK_APP=monthly.py' >> .flaskenv

echo 'to run the website: ./run.sh'
echo 'to run the website with debug mode on: ./debug.sh'

