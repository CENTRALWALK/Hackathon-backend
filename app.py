from flask import Flask, request, jsonify
import json
from seismic import SeismicProcessor
import pandas as pd

app = Flask(__name__)

FILE = pd.read_csv("./data/nakamura_1979_sm_locations.csv")

seismic = SeismicProcessor(FILE)


@app.route("/seismic/dates", methods=['GET'])
def seismic_get_dates():
    dates = seismic.get_years()
    return jsonify({"years": dates})


@app.route("/seismic/events", methods=['GET'])
def seismic_get_event_by_date():
    args = request.args
    date = args.get("year")
    events = seismic.list_events_by_year(int(date))
    print({"year": date, "events": events})
    return jsonify({"year": date, "events": events})
