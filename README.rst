flask_base
==========

A flask app mvp to be forked and developed by ITW Speer interns.

Derived largely from the official tutorial (http://flask.pocoo.org/docs/1.0/tutorial)


Setup
-----
Install the dependencies from requirements.txt into your environment (remember
to activate your environment with `source activate` once in the project
directory, and then use `pip install -r requirements.txt` to install the
required packages).

Requires FLASK_APP and FLASK_ENV environment variables set. For example:

``$ export FLASK_APP=hello_world``

``$ export FLASK_ENV=development``

Or, set when running commands:

``$ FLASK_APP=hello_world FLASK_ENV=development flask run``

Before running the app the first time, or if making any changes to the database
schema, you'll have to run the init-db command:

``$ flask init-db``


Commands
--------
``flask run`` -- start the server. You'll notice a message saying where the site
is running locally, most likely http://127.0.0.1:5000/. Ctrl-c will shut the
server down.

``flask init-db`` -- run the database setup command, creating a database from
the schema found in <app_name>/schema.sql. **This will also delete all
current data in the database**
