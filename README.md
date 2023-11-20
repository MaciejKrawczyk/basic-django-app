# Basic Django App

My notes about the project at the bottom of the readme file.

## Getting Started

Before running these commands, ensure you have created and activated a virtual environment and installed everything from the requirements.txt file:

### Virtual Environment
Create and activate a virtual environment.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Requirements
Install required packages.
```bash
pip install -r requirements.txt
```

## Basic Commands

### Database Migrations
These commands will create a db.

#### Create Migrations
Generate migration files based on Django models.
```bash
python manage.py makemigrations
```

#### Apply Migrations
Apply the migrations to the database.
```bash
python manage.py migrate
```

### Testing
Run tests to ensure the application is working as expected.
```bash
python manage.py test
```

### Superuser Creation
Create a superuser account, which is essential for accessing the admin panel.
```bash
python manage.py createsuperuser # Create a super user to enter the admin panel
```

### Loading Data
Load data from a fixture file into database.
```bash
python manage.py loaddata fixture.json
```

### Running the Server
Start the Django development server.
```bash
python manage.py runserver
```

## My notes

1. The task instructions specify loading data from an external database but do not clarify whether this should be a one-time action or if a scheduler should be set up. I initially configured it to load data just once. However, considering that currency and exchange rates frequently change, it would be more appropriate to regularly update the data.
2. Regarding the choice of libraries, I utilized 'yfinance' as recommended in the task. Additionally, I used the Django REST framework, which simplifies some aspects of the work and is widely recommended.
3. To display the 'View Historical Data' button, navigate to the exchange rates section in the admin panel and then click on the ExchangeRate object.
4. The historical data is fetched with a default period of one month, and the currencies fetched are EURUSD, USDJPY, and PLNUSD. These values can be altered in the currency -> utils -> create_fixture.py file.
5. To enhance performance and reduce the number of requests, I have created a separate table in the local database for storing this data.