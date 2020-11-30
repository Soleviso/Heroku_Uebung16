from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/styles")
def styles():
    return render_template("styles.html")

@app.route("/produkte")
def produkte():
    return render_template("produkte.html")

if __name__ == "__main__":
    app.run()