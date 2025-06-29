from datetime import datetime

from flask import Flask, render_template, request

from conversions import convert_length, convert_temperature, convert_weight
from models.length import Length
from models.temperature import Temperature
from models.weight import Weight

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def length():
    result = None
    if request.method == "POST":
        try:
            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            result = convert_length(value, from_unit, to_unit)
        except (ValueError, KeyError):
            result = "Invalid input"
    return render_template(
        "length.html", result=result, units=Length, year=datetime.now().year
    )


@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None
    if request.method == "POST":
        try:
            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            result = convert_weight(value, from_unit, to_unit)
        except (ValueError, KeyError):
            result = "Invalid input"
    return render_template(
        "weight.html", result=result, units=Weight, year=datetime.now().year
    )


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    result = None
    if request.method == "POST":
        try:
            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            result = convert_temperature(value, from_unit, to_unit)
        except (ValueError, KeyError):
            result = "Invalid input"
    return render_template(
        "temperature.html", result=result, units=Temperature, year=datetime.now().year
    )
