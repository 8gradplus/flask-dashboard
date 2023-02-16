install:
	pipenv install --dev
run-local:
	export FLASK-APP=dashboard.py; pipenv run flask --debug run --port=9000
init-db:
	export FLASK-APP=dashboard.py; pipenv run flask db init
migrate-users:
	export FLASK-APP=dashboard.py; pipenv run flask db migrate -m "users table"
upgrade-db:
	export FLASK-APP=dashboard.py; pipenv run flask db upgrade
docker-build:
	docker build -t flask-appp .
docker-run:
	docker run -p 5000:5000 flask-app
