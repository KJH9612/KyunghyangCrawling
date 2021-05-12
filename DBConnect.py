# pip install PyMySQL
# 패키지 포함
import pymysql

db = pymysql.connect(
    user='root',
    password='qwedf823!@#',
    host='127.0.0.1',
    database='childrens_day',
)
cursor = db.cursor(pymysql.cursors.DictCursor)
