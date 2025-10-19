from flask import Flask, render_template, request

app = Flask(__name__)

conversion_factors = {
    "mass": {"milli": 0.001, "centi": 0.01, "deci": 0.1, "": 1.0, "deka": 10, "hecto": 100, "kilo": 1000},
    "length": {"milli": 0.001, "centi": 0.01, "deci": 0.1, "": 1.0, "deka": 10, "hecto": 100, "kilo": 1000},
    "volume": {"milli": 0.001, "centi": 0.01, "deci": 0.1, "": 1.0},
    "time": {"seconds": 1, "minutes": 60, "hours": 3600, "days": 86400},
    "temperature": {}
}

def convert_units(value, category, unit_in, unit_out):
    if category == "temperature":
        if unit_in == "celsius" and unit_out == "fahrenheit":
            return round((value * 9/5) + 32, 2)
        elif unit_in == "fahrenheit" and unit_out == "celsius":
            return round((value - 32) * 5/9, 2)
        elif unit_in == "celsius" and unit_out == "kelvin":
            return round(value + 273.15, 2)
        elif unit_in == "kelvin" and unit_out == "celsius":
            return round(value - 273.15, 2)
        else:
            return "Invalid temperature conversion"
    
    try:
        return round(value * conversion_factors[category][unit_in] / conversion_factors[category][unit_out], 2)
    except KeyError:
        return "Invalid unit selection"

@app.route("/", methods=["GET", "POST"])
def index():
    converted = None
    if request.method == "POST":
        try:
            value = float(request.form.get("value"))
            category = request.form.get("category")
            unit_in = request.form.get("unit_in")
            unit_out = request.form.get("unit_out")

            converted = convert_units(value, category, unit_in, unit_out)
        except (ValueError, TypeError):
            converted = "Invalid input value"
        
    return render_template("index.html", converted=converted)

if __name__ == "__main__":
    app.run(debug=True)