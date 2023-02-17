FROM python:3.10.9-buster

# Update Pip and install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Add user `dashboard` with homedir `/dashboard` and switch
RUN useradd --create-home --home-dir /dashboard dashboard
USER dashboard
WORKDIR /dashboard

# Copy pipfiles from here to dockerimage
# Install dependencies
COPY  --chown=best Pipfile Pipfile
COPY --chown=best Pipfile.lock Pipfile.lock
RUN pipenv install

# Copy actual flask application
COPY --chown=dashboard config.py config.py
COPY --chown=dashboard app app
# corresponds to "main.py"
COPY --chown=dashboard dashboard.py dashboard.py

# Run application
CMD ["pipenv", "run", "python", "dashboard.py"]
# CMD ["sleep", "3600"]
