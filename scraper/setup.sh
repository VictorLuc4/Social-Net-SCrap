#!/bin/bash

source env/bin/activate
pip install -r ./requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS=key.json
