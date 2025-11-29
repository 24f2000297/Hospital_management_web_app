#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# Initialize the database
python -c "from app import app, init_db; init_db()"
