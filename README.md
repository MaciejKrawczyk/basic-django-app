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

Here are some of the fundamental commands you will use frequently:

### Testing
Run tests to ensure your application is working as expected.
```bash
python manage.py test
```

### Database Migrations
These commands help in creating and applying database migrations.

#### Create Migrations
Generate migration files based on your Django models.
```bash
python manage.py makemigrations
```

#### Apply Migrations
Apply the migrations to your database.
```bash
python manage.py migrate
```

### Superuser Creation
Create a superuser account, which is essential for accessing the admin panel.
```bash
python manage.py createsuperuser # Create a super user to enter the admin panel
```

### Loading Data
Load data from a fixture file into your database.
```bash
python manage.py loaddata fixture.json
```

### Running the Server
Start the Django development server.
```bash
python manage.py runserver
```

## My notes

1. The instruction for the task says to load data from external database. It doesn't state if it should be done once or a scheduler should be set up. I set it up to load data only once, but the currency and exchange rates are changing very frequently, the data should be updated regularly.
2. In terms of libraries, I used the yfinance because it was recommended in the task. Also used django rest framework as it abstract away some of the work and is widely used and recommended. 
3. To display the view historical data button, in the admin panel you need to enter to exchange rates, then click on ExchangeRate object. 
4. In first version I fetched historical data from an api every time the view historical data button in admin panel. But now I created a separate table in local database to speed up displaying the data and reduce the amount of requests.
