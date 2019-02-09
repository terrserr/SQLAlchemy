import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///C:/Users/Teresa Barajas/Anaconda/Anaconda3/envs/SQLAlchemy/hawaii.sqlite", echo = False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs/USC00519281<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precip():
    # Query all precipitation

    sel= [Measurement.date, Measurement.prcp]
	

    results = session.query(*sel).filter(Measurement.date > "2016-08-22").all()

    # Convert list of tuples into normal list
    last_12_months = list(np.ravel(results))

    return jsonify(last_12_months)

@app.route("/api/v1.0/stations")
def station():
    # Query all precipitation

    

    results_2 = session.query(Station.name).all()

    # Convert list of tuples into normal list
    station_names = list(np.ravel(results_2))

    return jsonify(station_names)


@app.route("/api/v1.0/tobs/USC00519281")
def tobs():
    # Query all precipitation

    
	results_3 = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > "2016-08-22").filter(Measurement.station == "USC00519281") .all()
	last_12_months_top_station= list(np.ravel(results_3))

	return jsonify(last_12_months_top_station)

if __name__ == "__main__":
    app.run(debug=True)
