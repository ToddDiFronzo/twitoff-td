
# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify #, request, render_template, request, flash, redirect

# from web_app.models import db, Book, parse_records
from web_app.services.twitter_service import api as twitter_api

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")  # will be dynamic
def fetch_user_data(screen_name):
    print("FETCHING...", screen_name)
    
    # TODO: fetch user info
    user = twitter_api.get_user(screen_name)

    # TODO: fetch their tweets
    statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=35, exclude_replies=True, include_rts=False)

    # TODO: fetch embedding for each tweet

    # TODO: store user in database

    # TODO: store tweets in database (w/ embeddings)
    
    # return f"FETCHED {screen_name} OK"
    return jsonify({"user":user._json, "num_tweets": len(statuses)})


