from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/loaderio-7d439812d414b477181647566d228996.html", methods=["GET"])
def loaderio():
    return render_template('loaderio-7d439812d414b477181647566d228996.html')

app.register_blueprint(api.downloader, url_prefix="/api")
app.register_blueprint(api.uploader, url_prefix="/api")
