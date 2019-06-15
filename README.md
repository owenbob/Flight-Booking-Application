# Flight-Booking-Application

[![Build Status](https://travis-ci.org/owenbob/Flight-Booking-Application.svg?branch=master)](https://travis-ci.org/owenbob/Flight-Booking-Application) [![Coverage Status](https://coveralls.io/repos/github/owenbob/Flight-Booking-Application/badge.svg?branch=master)](https://coveralls.io/github/owenbob/Flight-Booking-Application?branch=master) [![CircleCI](https://circleci.com/gh/owenbob/Flight-Booking-Application.svg?style=svg)](https://circleci.com/gh/owenbob/Flight-Booking-Application)

---

## Product overview 
 Yummy-Recipes-API-Django-GraphQl is a simple  API built with  Django and GraphQl.  Enables you to register a user,login. It aslo provides CRUD functionality for categories and recipes assigned to these categories. 

## Development set up
- Check that python 3, pip, virtualenv and postgres are installed

- Clone  Yummy-Recipes-API-Django-GraphQl  repo and cd into it
    ```
    https://github.com/owenbob/Flight-Booking-Application.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```
- Create Application environment variables and save them in .env file
    ```
    export DBNAME='Your Database name'
    export DBPASSWORD='Your Database password'
    export DBUSER='Your Database user'
    ```
- Run command
    ```
    source .env
    ```
- Running migrations

     ```
     python manage.py db init
    ```
     ```
     python manage.py db migrate
    ```
     ```
     python manage.py db upgrade
    ```
- Run application.
    ```
    python run.py
    ```

## Built with 
- Python version  3
- Flask
- Postgres
- Celery
- Redis
- Google Cloud Storage