from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from flask import Blueprint, jsonify, request, flash, redirect #,render_template

from web_app.statsmodels import load_model
stats_routes = Blueprint("stats_routes", __name__)


# TODO: accept some inputs related to the iris training data (x values)
@stats_routes.route("/stats/iris")
def iris():
    X, y = load_iris(return_X_y=True)
    # clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
    clf = load_model()  # make sure to pre-train the model first
    clf.fit(X, y)
    result = str(clf.predict(X[:2, :]))
    print("PREDICTION", result)
    return result   # todo resturn as JSON