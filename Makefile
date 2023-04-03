install-requirements:
	pip install -r requirements.txt

start-database:
	python3 manage.py db init 
	python3 manage.py db migrate
	python3 manage.py db upgrade

start:
	python3 manage.py run

run-linters:
	flake8 app/ manage.py

pytest:
	pytest -v app/test

populate_db:
	-python3 generate_data.py