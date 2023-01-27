export

run:
	python3 manage.py run

install:
	pip3 install -r requirements.txt

start-db:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

seed-db:
	python3 manage.py db upgrade
	python3 manage.py seed_db

init-db:
	python3 manage.py db init

upgrade-db:
	python3 manage.py db upgrade

migrate-db:
	python3 manage.py db migrate

downgrade-db:
	python3 manage.py db downgrade

test:
	pytest

test-coverage:
	coverage run -m pytest

run-pre-commit:
	pre-commit run --all-files

lint:
	flake8
