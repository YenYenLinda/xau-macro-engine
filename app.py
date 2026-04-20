from flask import Flask, jsonify

app = Flask(__name__)

# ROOT (for testing)
@app.route("/")
def home():
    return "Macro API is running"

# MAIN API (THIS IS WHAT MT5 CALLS)
@app.route("/macro", methods=["GET"])
def macro():
    return jsonify({
        "institutional": {
            "cot_bias": "bullish",
            "long_pct": 62,
            "short_pct": 38,
            "change": 5
        },

        "growth": {
            "gdp": {"actual": 2.4, "forecast": 2.1},
            "manufacturing": {"actual": 51.2, "forecast": 50.5},
            "services": {"actual": 53.0, "forecast": 52.0},
            "retail": {"actual": 0.6, "forecast": 0.3},
            "confidence": {"actual": 102, "forecast": 100}
        },

        "inflation": {
            "cpi": {"actual": 3.1, "forecast": 3.3},
            "ppi": {"actual": 2.8, "forecast": 3.0},
            "pce": {"actual": 2.6, "forecast": 2.8},
            "yield": "falling"
        },

        "jobs": {
            "nfp": {"actual": 150, "forecast": 180},
            "unemployment": {"actual": 4.1, "forecast": 4.0},
            "claims": {"actual": 230, "forecast": 220},
            "adp": {"actual": 120, "forecast": 150},
            "jolts": {"actual": 8.5, "forecast": 8.8}
        }
    })

# REQUIRED FOR RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
