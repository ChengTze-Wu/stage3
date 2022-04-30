from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

app.register_blueprint(api.downloader, url_prefix="/api")
app.register_blueprint(api.uploader, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3500)