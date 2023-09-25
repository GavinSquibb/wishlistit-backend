# WishListIt Backend

## How to run locally

Create and activate virtual environment using

`python -m venv env`

`source env/bin/activate`

## Install Dependencies

Use the following command to install dependencies from the list in the requirements.txt file

`pip install -r requirements.txt`

## Setup Local Database

Use the following commands to set up the local database

`python manage.py migrate`

Set up a local super user

`python manage.py createsuperuser`

Run the server

`python manage.py runserver`

## Testing

The test suite can be run with the following command

`python manage.py test`
