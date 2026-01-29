from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(_name_)

@app.route("/api/noise")
def noise_data():
    noise = random.randint(40, 95)

    status = "Safe"
    if noise > 80:
        status = "Danger"
    elif noise > 60:
        status = "Moderate"

    return jsonify({
        "noise": noise,
        "status": status,
        "time": datetime.now().strftime("%H:%M:%S"),
        "source": "Traffic",
        "prediction": noise + random.randint(-5, 5)
    })

app.run(debug=True)