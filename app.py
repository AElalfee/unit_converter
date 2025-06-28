from flask import Flask, render_template, request

from conversions import convert_length
from models.length import Length

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
    return render_template("length.html", result=result, units=Length)


@app.route("/weight")
def weight():
    return render_template("weight.html")


@app.route("/temperature")
def temperature():
    return render_template("temperature.html")
