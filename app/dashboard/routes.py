from flask import render_template
from flask_login import login_required
import pandas as pd

from app import app


@app.route('/dashboard')
@login_required
def dashboard():
    rating = pd.DataFrame({"rating": ["1", "2", "3", "4", "5"], "counts": [16, 43, 89, 32, 22]}).to_dict(orient="list")
    return render_template('dashboard/dashboard.html', rating=rating)
