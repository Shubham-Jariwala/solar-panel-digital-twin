from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    # Simulated real-time solar panel data
    data = {
        "voltage": round(random.uniform(18.0, 22.0), 2),
        "current": round(random.uniform(4.0, 6.0), 2),
        "power": lambda v, i: round(v * i, 2),
        "temperature": round(random.uniform(30.0, 50.0), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    data["power"] = data["power"](data["voltage"], data["current"])
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
