import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
     return (
        f"Welcome to the Hawaii Weather Station API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
     )
@app.route("/api/v1.0/precipitation")
def precipitation():
     # Create session 
    session = Session(engine)

    # Query precipitation amounts
    results = session.query(Measurement.date, func.sum(Measurement.prcp), Measurement.prcp).group_by(Measurement.station).all()

    session.close()

    # Convert result tupples to dictionary
    all_prcp = list(np.ravel(results))

    return jsonify(all_prcp)
@app.route("/api/v1.0/stations")
def stations():
    return (

    )
@app.route("/api/v1.0/tobs")
def tobs():
    return (

    )
@app.route("/api/v1.0/<start>")
def start():
    return (

    )
@app.route("/api/v1.0/<start>/<end>")
def startend():
    return (

    )

if __name__ == "__main__":
    app.run(debug=True)
