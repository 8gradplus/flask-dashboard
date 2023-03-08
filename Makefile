install:
	pipenv install --dev
run-backend-local:
	pipenv run python dashboard.py
init-db:
	pipenv run flask db init
migrate-users:
	pipenv run flask db migrate -m "users table"
upgrade-db:
	pipenv run flask db upgrade
docker-build:
	docker build -t flask-app .
docker-build-linux:
	docker buildx build --platform linux/amd64 -t flask-app .
docker-run:
	docker run -dp 5000:5000 flask-app
