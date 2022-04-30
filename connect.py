import boto3
from botocore.exceptions import ClientError
import logging
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() 

config = {
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'database': os.environ['DB_DATABASE']
}

# s3
def upload_file_to_s3(file, bucket, object_name=None):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(file, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# rds
cnx = mysql.connector.connect(pool_name="rds",
                              pool_size=5,
                              **config)

def get_lastdata_from_rds():
    try:
        cnx = mysql.connector.connect(pool_name="rds")
        cursor = cnx.cursor()
        query = ("SELECT * FROM board ORDER BY id DESC LIMIT 0,1")
        cursor.execute(query)
        data = cursor.fetchone()
        return {"data": data}
    except Exception as e:
        raise e
    finally:
        if cnx.in_transaction:
            cnx.rollback()
        cursor.close()
        cnx.close()

def get_datas_from_rds():
    try:
        cnx = mysql.connector.connect(pool_name="rds")
        cursor = cnx.cursor()
        query = ("select * from board")
        cursor.execute(query)
        data = cursor.fetchall()
        return {"data": data}
    except Exception as e:
        raise e
    finally:
        if cnx.in_transaction:
            cnx.rollback()
        cursor.close()
        cnx.close()
        
def create_data_to_rds(message, imgurl):
    try:
        cnx = mysql.connector.connect(pool_name="rds")
        cursor = cnx.cursor()
        query = ("insert into board (message, imgurl) values (%s, %s)")
        data = (message, imgurl)
        
        cursor.execute(query, data)
        cnx.commit()
        return {"ok": True}
    except Exception as e:
        raise e
    finally:
        if cnx.in_transaction:
            cnx.rollback()
        cursor.close()
        cnx.close()
        