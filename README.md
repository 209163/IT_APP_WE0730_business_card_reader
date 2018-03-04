# IT_APP_WE0730_business_card_reader

The application was created for the purpose of the course
"IT Applications in Business and Commerce" taken at Wrocław University of Science and Technology.

It's purpose is to make easy storing contacts collected through the business card exchange process.

System extracts text from the uploaded card and classifies received information into following groups: name, company, phone number and email address. It's based on the neural network, and therefore can be easily extended to obtain additional information if needed.

## Getting Started

### Prerequisites
#### Python 3.6
#### Django 2.0

See: https://virtualenv.pypa.io/en/stable/

### To create local database (sqlite3 by default):
#### 1. Make sure you're in directory where manage.py is located!
#### 2. Type in your console:
##### python manage.py makemigrations business_card_reader_app
##### python manage.py migrate business_card_reader_app

## Running the server
### Type in your console:
#### python manage.py runserver


## Built With

* [Python]()
* [Django]()

