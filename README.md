# Testing django project.

## Project's purpose.
RESTful web service for transmission of funds from one account to another.

## How to set up.

### Prerequisites:
 - Python 3 must be installed.

### Setup instructions:
1. Create virtual environment with Python 3.
```
python3 -m venv test_project_env
```
2. Activate virtual environment.
```
source test_project_env/bin/activate
```
3. Make sure you have Python 3 active:
```
python -V
Python 3.6.5
```
4. Upgrade pip.
```
pip install --upgrade pip
```
5. Unpack archive with the test project.
```
tar -xzvf test_project.tar.gz
```
6. Go to test project directory and install dependencies.
```
cd test_project
pip install -r requirements.txt
```
7. Load necessary environment variables.
```
source env.sh
```
8. Make sure that environment variables are loaded:
```
printenv | grep secret_key
printenv | grep django_debug
```
9. Create a database.
```
python manage.py migrate
```
10. Collect static files.
1) Run this command:
```
python manage.py collectstatic
```
2) Type *yes* in the prompt.

## How to run tests.
In the project's directory run:
```
python manage.py test
```

## How to do a code linting.
In the project's directory run:
```
prospector --profile prospector.yaml
```

## How to get API docs.
1. Run the local dev server.
```
python manage.py runserver
```
2. Open Swagger docs in the browser http://localhost:8000/docs/
