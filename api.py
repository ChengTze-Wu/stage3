from flask import Blueprint, request
from connect import *

s3 = Blueprint("s3")

@s3.route("/s3upload", methods=["PATCH"])
def upload_file():
    file = request.files['file']
    # couldfare
    # rds
    return {"ok":True}


rds = Blueprint("rds")

@rds.route("/resources", method=["GET"])
def get_resources():
    return get_datas()


@rds.route("/resource", method=["PATCH"])
def create_resource():
    resp = create_data()
    return resp

