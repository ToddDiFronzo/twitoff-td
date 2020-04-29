# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, flash, redirect #,render_template

from web_app.models import db

admin_routes = Blueprint("admin_routes", __name__)

API_KEY = "abc123"  # TODO: set as secret env var

# GET /admin/db/reset?api_key="2aae2804-16b4-1722-d03c-3448be2ba7ff"
# @admin_routes.route("/admin/db/reset")
# def reset_db():
#     print(type(db))
#     db.drop_all()
#     db.create_all()
#     return jsonify({"message": "DB RESET OK"})

# GET /admin/db/reset?api_key="abc123"
@admin_routes.route("/admin/db/reset")
def reset_db():
    print("URL PARMS", dict(request.args))

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        return jsonify({"message": "DB RESET OK"})
    else:
        print("PERMISSION DENIED SON")
        flash("OOPS Permission Denied", "danger")
        return redirect("/books")












