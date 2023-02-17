# Installation

Use the following make targets as specified in the Makefile.
### Run local 
```
make install
make run-local
```

### Docker
- For docker we need to specify the host to sth like 0.0.0.0
- The default lokal host is not working (find out why!)
- Also we need to migrate the db in the current setup. This should go in the dockerfile?
```
make docker-build
make docker-run 
```

### Migrate Database
- **Todo:** need to incorporate changes from using factory pattern

# Todo:
- Docker
- Use settings from config in dashboard.py (currently hard coded)
- Clean up api structure: https://realpython.com/flask-connexion-rest-api/ (Part 1-3)
- Use a production server (e.g. Waitress) https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/
- Bring to cloud
- Upload files https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
- Error message upon wrong login
- Use Application factory pattern https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure
- Password reset token (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
- Add swagger: https://realpython.com/flask-javascript-frontend-for-rest-api/

# Resources

### Flask

- https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf flask cheat sheet
  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- Datbase migration

### Tables
- using js for pagination et al https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates
# Applications
- https://github.com/app-generator/flask-volt-dashboard
- https://github.com/app-generator/flask-black-dashboard
- https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b (look at github)
- https://github.com/Nadiantara/flask_covid_dashboard dashboard with plotly et al with flask

### Jinja 2:
Template engine that enables
- inheritence 
- variable input
- conditionals

### Bootstrap 
- via Flask
- or, include via web link in html

### wtf-flask
- for creating forms 
- also adds security 


### user managment
- `flask-login`
- `werkzeug` for hashing passwords
- delete users according to: https://www.youtube.com/watch?v=ogZR7OEv1Pk&list=PLU7aW4OZeUzwn6L1txXQ9viaAIR2mDqbv&index=5

### Plotting Chart.js
- https://www.youtube.com/watch?v=ylWoIaSgThk tutorials
