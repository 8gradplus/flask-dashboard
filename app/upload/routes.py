from app.upload import bp
from flask import request, render_template, url_for
import pandas as pd
import io
from datetime import datetime
from app import data

@bp.route("/upload", methods=["GET", "POST"])
def upload():
    """Todo """
    if request.method != "POST":
        render_template(url_for('index'))
    file = request.files['file']
    f = io.BytesIO(file.read())
    df = pd.read_csv(f, sep=";")
    data.df = df
    data.imported_at = datetime.utcnow().isoformat()
    return "Sucess"
