# IT_APP_WE0730_business_card_reader

Requirements:
    Python 3.6
    Django 2.0
    
    See: https://virtualenv.pypa.io/en/stable/

To create database (sqlite3 by default):
    # Make sure you're in directory where manage.py is located!
    -> python manage.py makemigrations business_cards_reader_app
    -> python manage.py migrate business_card_reader_app
