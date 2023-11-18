# Use an official Python runtime as a parent image
FROM python:3.12-alpine3.18

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Copy project
COPY . /code/