export

run:
	python3 manage.py run

install:
	pip3 install -r requirements.txt

start-db:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

init-db:
	python3 manage.py db init

migrate-db:
	python3 manage.py db migrate

upgrade-db:
	python3 manage.py db upgrade

test:
	pytest

test-coverage:
	coverage run -m pytest

run-pre-commit:
	pre-commit run --all-files

lint:
	flake8