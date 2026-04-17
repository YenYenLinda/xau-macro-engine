from flask import Flask, request, jsonify

app = Flask(__name__)

def score(text):
    text = text.lower()

    bullish = ["dovish", "cut", "weak jobs", "slow inflation", "gold demand"]
    bearish = ["hawkish", "rate hike", "strong dollar", "hot inflation"]

    s = 0
    for w in bullish:
        if w in text:
            s += 1
    for w in bearish:
        if w in text:
            s -= 1

    return max(-2, min(2, s))


@app.route("/macro", methods=["POST"])
def macro():
    data = request.json

    total = (
        score(data.get("cpi","")) +
        score(data.get("nfp","")) +
        score(data.get("fed","")) +
        score(data.get("geo","")) +
        score(data.get("dxy","")) +
        score(data.get("yields","")) +
        score(data.get("flows",""))
    )

    return jsonify({
        "macroScore": total
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
