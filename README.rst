flask_base
==========

A flask app mvp to be forked and developed by ITW Speer interns.

Derived largely from the official tutorial (http://flask.pocoo.org/docs/1.0/tutorial)


Setup
-----
Install the requirements from requirements.txt into your environment.

Requires FLASK_APP and FLASK_ENV environment variables set. For example:

``$ export FLASK_APP=hello_world``
``$ export FLASK_ENV=development``

Or, set when running commands:

``$ FLASK_APP=hello_world FLASK_ENV=development flask run``

Before running the app, you'll have to run the init-db command:

``$ flask init-db``


Commands
--------
``flask run`` -- run the server
``flask init-db`` -- run the database setup command, creating a database from
the schema found in <app_name>/schema.sql. **This will also delete all
current data in the database**
