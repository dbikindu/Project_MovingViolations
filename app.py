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



@app.route("/heatmap")
def heatmap():
    """Return the heatmap of moving violations"""

    return render_template("heatmap.html")

@app.route("/mapmarker")
def mapmarker():
    """Return the map showing the cluster with concentration of moving violations"""

    return render_template("marker.html")


@app.route("/chartjs")
def chartjs():
    """Return a chart with the top 10 location with the highest fine"""

    return render_template("my_chartjs.html")


if __name__ == "__main__":
    app.run()
