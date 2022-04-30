import boto3
import mysql.connector
from dotenv import load_dotenv

load_dotenv() 

# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    
data = open('test.txt', 'rb')
s3.Bucket("wehelpimagetest").put_object(Key="test.txt", Body=data)


# config = {
#     'user': os.environ['DB_USER'],
#     'password': os.environ['DB_PASSWORD'],
#     'host': os.environ['DB_HOST'],
#     'database': os.environ['DB_DATABASE']
# }

config = {
    'user': "root",
    'password': "root1234",
    'host': "wehelp-week1.c1ivcdbhk8dx.ap-northeast-1.rds.amazonaws.com",
    'port': 3306,
    'database': 'week_one'
}

cnx = mysql.connector.connect(pool_name="rds",
                              pool_size=5,
                              **config)

def get_datas():
    try:
        cnx = mysql.connector.connect(pool_name="rds")
        cursor = cnx.cursor()
        query = ("select * from board")
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
        
def create_data(message, imgurl):
    try:
        cnx = mysql.connector.connect(pool_name="rds")
        cursor = cnx.cursor()
        query = ("insert into board values (%s, %s)")
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
        