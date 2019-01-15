import os

#import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/moving_violations.sqlite"
#db = SQLAlchemy(app)
engine = create_engine("sqlite:///moving_violations.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
#Base.prepare(db.engine, reflect=True)
Base.prepare(engine, reflect=True)

# Save references to each table
Movingviolations = Base.classes.Movingviolations

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")



@app.route("/violationdata")
def violations():
    """Return a detail list of information for each location"""
    # Query all locations
    results = session.query(Movingviolations).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_violations = []
    for violation in results:
        violation_dict = {}
        violation_dict["STREET_ID"] = violation.STREET_ID
        violation_dict["LOCATION"] = violation.LOCATION
        violation_dict["VIOLATION_DESCRIPTION"] = violation.VIOLATION_DESCRIPTION
        violation_dict["TOTAL_PAID"] = violation.TOTAL_PAID
        violation_dict["LONGITUDE"] = violation.LONGITUDE
        violation_dict["LATITUDE"] = violation.LATITUDE
        all_violations.append(violation_dict)

    return jsonify(all_violations)

@app.route("/violationmap")
def violationmap():
    """Return a detail list of information for each location"""
    # Query all locations
    results = session.query(Movingviolations).all()

    var heatArray = [];




    return jsonify(all_violations)


if __name__ == "__main__":
    app.run()
