from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # couldfare
    # rds
    return render_template('index.html')


@app.route("/upload", methods=["POST"])
def upload_file():
    # couldfare
    # rds
    return {"ok":True}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3500)