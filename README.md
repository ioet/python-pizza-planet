# Python Pizza Planet

This is an example software for a pizzeria that takes customizable orders.

## Getting started

You will need the following general tools:

- A Python interpreter installed. [3.8.x](https://www.python.org/downloads/release/python-3810/) is preffered.

- A text editor: preferably [Visual Studio Code](https://code.visualstudio.com/download)

- Extensions such as [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

### Running the backend project

- Create a virtual environment in the root folder

```bash
python3 -m venv venv
```

- Activate the virtual environment

- Install all necessary dependencies:

```bash
pip3 install -r requirements.txt
```

- Start the database:

```bash
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

- Run the project with:

```bash
python3 manage.py run
```

### Testing the backend

- Make sure that you have `pytest` installed

- Run the test command

```bash
python3 manage.py test
```

### Running the frontend

_TBD_ 
