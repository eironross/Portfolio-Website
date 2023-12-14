from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api-documentation")
def get_api_docs():
    return render_template("page-api.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)