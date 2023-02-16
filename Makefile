install:
	pipenv install --dev
run-local:
	export FLASK-APP=dashboard.py; pipenv run flask --debug run
init-db:
	export FLASK-APP=dashboard.py; pipenv run flask db init
migrate-users:
	export FLASK-APP=dashboard.py; pipenv run flask db migrate -m "users table"
upgrade-db:
	export FLASK-APP=dashboard.py; pipenv run flask db upgrade
install-kernel:
	export JUPYTER_DATA_DIR=./jupyter; export JUPYTER_PATH=./jupyter; pipenv run install_kernel
start-notebook:
	export JUPYTER_DATA_DIR=./jupyter; export JUPYTER_PATH=./jupyter; pipenv run notebook
docker-build:
	docker build -t dashbaord .