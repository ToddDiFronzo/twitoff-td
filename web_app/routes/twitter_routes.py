
# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify #, request, render_template, request, flash, redirect

# from web_app.models import db, Book, parse_records

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")  # will be dynamic
def fetch_user_data(screen_name):
    print("FETCHING...", screen_name)

    # TODO: fetch user info

    # TODO: fetch their tweets
    # TODO: fetch embedding for each tweet

    # TODO: store user in database

    # TODO: store tweets in database (w/ embeddings)
    return f"FETCHED {screen_name} OK"



