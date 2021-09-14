# API-REST WITH FLASK
Example of API rest with python utils framework flask.

## Creating a new Flask project with pipenv
    
>    -Create the pipenv environment
```bash
$ mkdir project
$ cd project
$ pipenv install
```
    
>    - Install Flask and more dependencies
```bash
    $ pipenv install flask
    $ pipenv install flask-sqlalchemy
    $ pipenv install flask-marshmallow
    $ pipenv install marshmallow-sqlalchemy

```

>    -Structure folders/files:

```bash
mkdir app
touch app/__init__.py
touch app/category.py
touch main.py
```
>    - Change into the pipenv:

```bash
$ pipenv shell
```
>    - Set the FLASK_APP variable:

```bash
$ flask run
```

