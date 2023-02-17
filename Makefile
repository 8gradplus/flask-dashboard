install:
	pipenv install --dev
run-local:
	pipenv run python dashboard.py
init-db:
	pipenv run flask db init
migrate-users:
	pipenv run flask db migrate -m "users table"
upgrade-db:
	pipenv run flask db upgrade
docker-build:
	docker build -t flask-app .
docker-run:
	docker run -dp 9000:9000 flask-app
