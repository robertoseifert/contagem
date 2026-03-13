from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/salvar", methods=["POST"])
def salvar():

    data = request.json
    ean = data["ean"]
    quantidade = data["quantidade"]

    with open("contagem.csv", "a") as f:
        f.write(f"{ean};{quantidade}\n")

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
