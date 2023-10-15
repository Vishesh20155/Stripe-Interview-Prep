# Creating an API endpoint

## File: `application.py`

* `python -m venv .venv`

* `source .venv/bin/activate`

* `pip install flask`

* `pip install flask-sqlalchemy`

*  `pip freeze > requirements.txt`

* Write the code

* Setup the following env variables every time:
    * `export FLASK_APP=(pythn_file.py)`
    * `export FLASK_ENV=development`
    * `export FLASK_DEBUG=1`
    * Run the app: `flask run`

* Source: https://www.kindsonthegenius.com/how-to-create-an-api-in-python-with-flask-step-by-step/


## FILE: main.py

* Source: https://rahmanfadhil.com/flask-rest-api/

* See solution to `db.create_all()`: https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask

* Run using: `python main.py`

* Python APIs using Authentication: https://auth0.com/blog/developing-restful-apis-with-python-and-flask/#-span-id--bootstrapping-flask----span--Bootstrapping-a-Flask-Application

