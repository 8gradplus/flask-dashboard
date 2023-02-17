install:
	pipenv install --dev
run-local:
	pipenv run python dashboard.py
init-db:
	export FLASK-APP=dashboard.py; pipenv run flask db init
migrate-users:
	export FLASK-APP=dashboard.py; pipenv run flask db migrate -m "users table"
upgrade-db:
	export FLASK-APP=dashboard.py; pipenv run flask db upgrade
docker-build:
	docker build -t flask-app .
docker-run:
	docker run -p 9000:9000 flask-app
