import json
from flask import request

from app import data
from app.api import bp


@bp.route("/get_all_data")
def get_all_data():
    """
    Todo: reponse for not uploaded data
    Todo: parse data correctly with pandas
    """
    description = "Imported Data from input"
    response = {"description": description,
                "import date": data.imported_at,
                "data": data.df.to_dict("list")}
    return json.dumps(response, indent=4)


@bp.route("/filter_data")
def filter_data():
    """Todo make filter more versatile (not only isin) by parsing the argument properly"""
    isin = request.args.get("isin")
    df = data.df
    response = df[df['isin'] == isin].squeeze().to_dict()
    return json.dumps(response, indent=4)

