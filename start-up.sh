#!/bin/bash
pipenv run flask db init
pipenv run flask db migrate -m "users table"
pipenv run flask db upgrade
pipenv run python dashboard.py
