from flask import Blueprint, request
from connect import *

uploader = Blueprint("uploader", __name__)
downloader = Blueprint("downloader", __name__)

@uploader.route("/upload", methods=["PATCH"])
def upload():
    file = request.files["file"]
    content = request.form["content"]
    resp_bool = upload_file_to_s3(file=file, bucket="wehelpimagetest", object_name=file.filename)
    if(resp_bool):
        resp = create_data_to_rds(message=content, imgurl=f"https://d43czlgw2x7ve.cloudfront.net/{file.filename}")
        return resp
    else:
        return {'failed': True}

@downloader.route("/download_all", methods=["GET"])
def download_all():
    return get_datas_from_rds()

@downloader.route("/download_one", methods=["GET"])
def download_one():
    return get_lastdata_from_rds()