create_environment:
	python3 -m venv .venv

install_dependencies:
	. .venv/bin/activate && pip install -r requirements.txt

start_server:
	. .venv/bin/activate && python3 manage.py run

start_server_hot_reload:
	. .venv/bin/activate && python3 manage.py hot-reload

start_database:
	. .venv/bin/activate && python3 manage.py db init
	. .venv/bin/activate && python3 manage.py db migrate
	. .venv/bin/activate && python3 manage.py db upgrade

run_tests:
	. .venv/bin/activate && pytest -v app/test/ 

run_lint:
	. .venv/bin/activate && flake8 app/


migrate_poetry:
	cat requirements.txt | xargs poetry add