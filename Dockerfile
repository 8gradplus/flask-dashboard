FROM python:3.10.9-buster

# Update Pip and install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Add user `dashboard` with homedir `/dashboard`
RUN useradd --create-home --home-dir /dashboard dashboard
# Become user `dashbaord`
USER dashboard

# Copy pipfiles from here to dockerimage
# Install dependencies
COPY  Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install

# Copy actual flask application
# This needs to be adapted upon rewrite as application factory
COPY app app
COPY dashboard.py dashboard.py
COPY config.py config.py

# Run application
ENV FLASK_APP=dashboard.py
CMD ["pipenv", "run", "flask", "run"]
