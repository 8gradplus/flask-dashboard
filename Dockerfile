FROM python:3.10.9-buster

# Update Pip and install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Add user and set working dir and switch to user
RUN useradd dashboard
WORKDIR /home/dashboard
# USER dashboard

# Copy pipfiles from here to dockerimage
# Install dependencies
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install
