<h1 align="center"> Python Pizza Planet </h1>

![python-badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

This is an example software for a pizzeria that takes customizable orders.

## Table of Contents

- [Getting started](#getting-started)
- [Running the backend project](#running-the-backend-project)
- [Running the frontend](#running-the-frontend)
- [Testing the backend](#testing-the-backend)
- [Commit messages format](#commit-messages-format)
- [Branch names format](#branch-names-format)
- [Pull-request names format](#pull-request-names-format)

## Getting started

You will need the following general tools:

- A Python interpreter installed. [3.8.x](https://www.python.org/downloads/release/python-3810/) is preffered.

- A text editor: preferably [Visual Studio Code](https://code.visualstudio.com/download)

- Extensions such as [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

## Running the backend project

- Clone the repo

```bash
git clone https://github.com/ioet/python-pizza-planet.git
```

- Create a virtual environment in the root folder of the project

```bash
python3 -m venv venv
```

- Activate the virtual environment (In vscode if you select the virtual env for your project it will activate once you open a new console window)

_For linux/MacOS users:_

```bash
source venv/bin/activate 
```

_For windows users:_

```cmd
\path\to\env\Scripts\activate
```

- Install all necessary dependencies:

```bash
pip3 install -r requirements.txt
```

- Start the database (Only needed for the first run):

```bash
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

- If you want to use the hot reload feature set FLASK_ENV before running the project:

_For linux/MacOS users:_

```bash
export FLASK_ENV=development 
```

_For windows users:_

```CMD
set FLASK_ENV=development
```

- Run the project with:

```bash
python3 manage.py run
```

## Running the frontend

- Clone git UI submodule

```bash
git submodule update --init
```

- Install Live Server extension if you don't have it from [here](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) on VSCode Quick Open (`Ctrl + P`)

```bash
ext install ritwickdey.LiveServer
```

- To run the frontend, start `ui/index.html` file with Live Server (Right click `Open with Live Server`)

- **Important Note** You have to open vscode in the root folder of the project.

- **To avoid CORS errors** start the backend before the frontend, some browsers have CORS issues otherwise

### Testing the backend

- Make sure that you have `pytest` installed

- Run the test command

```bash
python3 manage.py test
```
## Commit messages format

Below there are some common examples you can use for your commit messages:

- **feat**: A new feature.
- **fix**: A bug fix.
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **test**: Adding missing tests or correcting existing tests.
- **ci**: Changes to our CI or CD configuration files and scripts (example scopes: Azure devops, github actions).
- **docs**: Documentation only changes.

### Example
```shell
fix: orders can now be placed
```
## Branch names format

For your branch name you can follow the next format:

<p align="center"><b>{work-type}/{trello-ticket-name}</b></p>

For the `work-type` we have the next types:

- **bug**: Code changes to fix a known bug.
- **feature**: Development of a new feature.
- **test**: Code changes related to tests.
- **documentation**: Documentation changes.
- **hotfix**: Quick fix for a critical bug.

### Example:

```shell
bug/PIZ1-I-cannot-create-an-order
```
## Pull-request names format
For your PR only use the trello ticket name 

### Example:

```shell
PIZ1: I cannot create an order
```