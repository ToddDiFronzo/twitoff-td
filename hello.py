# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     print("You visited the Homepage")
#     return 'Hello, World!'


# @app.route("/about")
# def about():
#     print("You visited the about page")
#     return 'About Me (TODO)'


# def create_app(config_filename):
#     app=Flask(__name__)
#     app.config.from_pyfile(config_filename)

#     from your application.model import db
#     db.init_app(app)

#     from yourapplication.views.admin import admin
#     from yourapplication.views.frontend import frontend
#     app.register_blueprint(admin)
#     app.register_blueprint(frontend)

#     return app


#     from flask import current_app, Blueprint, render_template
#     admin = Blueprint('admin', __name__, url_prefix='/admin')

#     @admin.route('/')
#     def index():
#         return render_template(current_app.config['INDEX_TEMPLATE'])
