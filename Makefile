install-requirements:
	pip install -r requirements.txt

start-database:
	python3 manage.py db init 
	python3 manage.py db migrate
	python3 manage.py db upgrade

start:
	python3 manage.py run

run-formatter:
	autopep8 --recursive --in-place --max-line-length 79 --aggressive --aggressive app
	autopep8 --in-place --max-line-length 79 --aggressive --aggressive manage.py

run-linters:
	flake8 app/ manage.py

pytest:
	pytest -v app/test
