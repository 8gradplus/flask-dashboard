from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import request
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse

from app.auth import bp
from app.models import User, users_schema
from app.auth.forms import LoginForm
from app.auth.forms import RegistrationForm
from app import db
from flask import Response, jsonify

# todo make true api for login, logout and register

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)


@bp.route('/all_users')
def all_users():
    users = User.query.all()
    return users_schema.dump(users)


@bp.route('/delete_user/<string:username>')
def delete_user(username):
    user_to_delete = User.query.filter(User.username == username).one_or_none()
    if not user_to_delete:
        msg = f"Could not find user {user_to_delete.username}"
        return Response(msg, status="404")
    db.session.delete(user_to_delete)
    db.session.commit()
    msg = f"Deleted user {user_to_delete.username}"
    return Response(msg, status="200")

"""
add user via post request and json
@bp.route('add_user', ["POST"])
def add_user():
    form = RegistrationForm()
    if not form.validate_on_submit():
        return jsonify({"message": "Could not create user"})

    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Created user"})
"""



