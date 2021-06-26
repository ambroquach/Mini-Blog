import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Creates the variable basedir pointing to the directory the program is running
basedir = os.path.abspath(os.path.dirname(__file__))

# Uses basedir to create the Connexion application instance and give it the path to thw swagger.yml file
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance initialized by Connexion
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
# echo SQL statements it executes to console -- useful for debugging, turn of for production
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(
        basedir, 'people.db')  # tell Alchemy to use SQLite as the database, people.db as the db file in the current dir
# only for event-driven program -- add lots of overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
# Initialize Alchemy by passing the app config info just set above
# db var will be imported to build_database.py and give it access to Alchemy and the database, also same purpose for server.py and people.py
db = SQLAlchemy(app)

# Initialize Marshmallow and allow it to introspect Alchemy components attached to the app
ma = Marshmallow(app)
