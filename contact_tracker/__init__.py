import os

from flask import Flask


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # TODO get from environment variable
        DATABASE=os.path.join(app.instance_path, "contact_tracker.sqlite")
    )

    if test_config is None:
        # load the production config
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import contacts
    app.register_blueprint(contacts.bp)
    app.add_url_rule("/", endpoint="index")

    return app

