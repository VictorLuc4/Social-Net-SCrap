#!/bin/bash

source env/bin/activate
pip install -r ./requirements.txt
export FLASK_APP=webapp/app.py