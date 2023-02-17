Just another Flask Dashboard - but not as pretty as 
[Volt](https://github.com/app-generator/flask-volt-dashboard), 
[Volt black](https://github.com/app-generator/flask-black-dashboard), ...


# Installation

Use the following make targets as specified in the Makefile.
### Run local 
```
make install
make run-local
```

### Docker
- For Docker, we need to specify the host to sth like 0.0.0.0
- The default local host is not working (find out why!)
- Also, we need to migrate the db in the current setup. This should go in the dockerfile?
```
make docker-build
make docker-run 
```

# Resources
### AWS:
- [Set up AWS Environment](https://aws.amazon.com/getting-started/guides/setup-environment/?pg=gs&sec=gtkaws)
- [Elastic Container Service (ECS)](https://docs.aws.amazon.com/ecs/index.html) to manage Docker containers

### Flask

- [Flask Cheat Sheet](https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf)
- [Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- Components we use
  - `Jinja 2` as template engine (Allows inheritance, variable input, conditionals in frontend)
  - `Bootstrap`: either via Flask or CDN in Html
  - `wtf-flask` for creating forms and adding security
  - `flask-login` for user management
  - `werkzeug`for hashing password

### JavaScript for Frontend
- [Chart.js](https://www.chartjs.org/) for Plotting: [tutorials](https://www.youtube.com/watch?v=ylWoIaSgThk)
- Pagination and rendering of **Tables** [Example](https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates)



# Todo:

### Deployment
- Deploy on AWS
- Add C/I from git
- Manage secrets
- Make db remember and track changes remote.


### App
- Clean up api structure [Example](https://realpython.com/flask-connexion-rest-api/) (Part 1-3)
- Use JavaScript consistently in Frontend [Example](https://realpython.com/flask-javascript-frontend-for-rest-api/)
- Upload files [Example](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
- Use settings from config in dashboard.py (currently hard coded)
- [Use a production server](https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/) (e.g. Waitress) 
- Error message upon wrong login
- Password reset token [Example](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
- Add swagger [Example](https://realpython.com/flask-javascript-frontend-for-rest-api/)
- Delete users [Example](https://www.youtube.com/watch?v=ogZR7OEv1Pk&list=PLU7aW4OZeUzwn6L1txXQ9viaAIR2mDqbv&index=5)


