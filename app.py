# Import the dependencies.
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
engine = create_engine("sqlite:///Resources/hawaii.sqlite",connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    previus = dt.date(2017, 8, 23)-dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(
        Measurement.date >= previus).all()
    x = {date: prcp for date, prcp in results}

    return jsonify(x)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()

    all_stations = list(np.ravel(results))
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
        # Ensure you're working within the Flask application context
    with app.app_context():
        # Your code to query the database for temperature observations
        previous = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        results=session.query(Measurement.tobs).filter(
            Measurement.date >= previous,
            Measurement.station == "USC00519281"
        ).all()

        # Process the results and return a JSON response
        data = list(np.ravel(results))
        return jsonify(data)


@app.route("/api/v1.0/<start>")
def temperature_stats_start(start):

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    temperature_stats = [{"TMIN": results[0][0],"TAVG": results[0][1], "TMAX": results[0][2]}]

    return jsonify(temperature_stats)


@app.route("/api/v1.0/<start>/<end>")
def temperature_stats_start_end(start, end):

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    temperature_stats = [{"TMIN": results[0][0],
                          "TAVG": results[0][1], "TMAX": results[0][2]}]

    return jsonify(temperature_stats)


if __name__ == '__main__':
    app.run(debug=True)
