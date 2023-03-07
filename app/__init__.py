from dataclasses import dataclass
from datetime import datetime

import pandas as pd
from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'


@dataclass
class Data:
    df: pd.DataFrame
    imported_at: str


data = Data(df=None, imported_at=None)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.upload import bp as upload_bp
    app.register_blueprint(upload_bp)

    from app.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


# todo: remove this. just used to speed up development

df = pd.read_csv("resources/datenbank_20220924.csv", sep=";")
data.df = df
data.imported_at = datetime.utcnow().isoformat()

# This import has to come after the factory because models depend on app instance
from app import models
