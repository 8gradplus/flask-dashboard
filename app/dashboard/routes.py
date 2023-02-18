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
    summary = {'issuer': 'Merzedes-Benz Group AG',
              'id_isin': 'DE000A289QR9',
              'period': "Q3 2020",
              'duration': "10 Years",
              'nominal': "1000 mEuro",
              'coupon': "0.75 %",
              'credit_quality': "medium",
              'issue_date': "2020-9-03",
              'settlement_date': "2020-9-10",
              'maturity_date':  "2030-9-10",
              'overall_rating': 5,
              'pricing_rating': 1,
              'timing_rating': 1,
              'duration_rating': 3,
              'quality_rating': 3}
    rating_histogram = (pd.DataFrame({"rating": ["1", "2", "3", "4", "5"],
                            "counts": [16, 43, 89, 32, 22]})
                          .to_dict(orient="list"))

    return render_template('dashboard/dashboard.html',
                           summary=summary,
                           rating_histogram=rating_histogram,
                           time_series=time_series)
