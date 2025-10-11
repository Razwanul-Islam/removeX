FROM python:3.12.2

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

# Install system dependencies for building packages
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/

# Upgrade pip, setuptools, and wheel to the latest versions
RUN pip install --upgrade pip setuptools wheel
# install peewee 
# RUN pip install --prefer-binary peewee==3.17.8
# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# COPY all file or project
COPY . /code/