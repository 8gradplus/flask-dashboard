from flask import render_template
from flask_login import login_required
import pandas as pd
import numpy as np

from app.dashboard import bp


@bp.route('/dashboard')
@login_required
def dashboard():

    t = np.arange(21)
    y = t ** 2 - 3*t -100
    y_peers = t**2 - 3 * t + 10 * t
    y_market = y - 50
    time_series = {'t': list(t),
                   'y': list(y),
                   'y_peers': list(y_peers),
                   'y_market': list(y_market)}
    rating = {'company': 'Google',
              'id': 'IKL456AB45',
              'issue_date': "2023-2-14",
              'overall': 5,
              'pricing': 1,
              'timing': 1,
              'duration': 3,
              'quality': 3}
    rating_histogram = (pd.DataFrame({"rating": ["1", "2", "3", "4", "5"],
                            "counts": [16, 43, 89, 32, 22]})
                          .to_dict(orient="list"))
    summary = (pd.DataFrame({"key": ["Company", "Domain", "Value", "Quality", "Date", "Another Date"],
                            "value": ["Google", "www.google.com", "1000 mEuro", "Good", "2023-2-14", "2020-6-13"]})
                 .to_dict(orient="record"))
    return render_template('dashboard/dashboard.html',
                           rating = rating,
                           summary=summary,
                           rating_histogram=rating_histogram,
                           time_series=time_series)
