import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.Measurement
Station = Base.classes.Station

session = Session(engine)


recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
recent_date

one_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)

session.close()
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available routes."""
    return(
        f"Homepage for Hawaii Climate Analysis!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

#################################################
# Run application
################################################# 

if __name__ == "__main__":
    app.run(debug=True)
