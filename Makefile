install:
	pipenv install --dev
run-app:
	export FLASK-APP=dashboard.py; pipenv run flask --debug run
init-db:
	export FLASK-APP=dashboard.py; pipenv run flask db init
migrate-users:
	export FLASK-APP=dashboard.py; pipenv run flask db migrate -m "users table"
upgrade-db:
	export FLASK-APP=dashboard.py; pipenv run flask db upgrade