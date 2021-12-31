import pymysql
from datetime import date, datetime, time, timedelta
import random

db = pymysql.connect(
    user='root', 
    passwd='1234', 
    host='127.0.0.1', 
    db='nutrient'
)
cursor = db.cursor(pymysql.cursors.DictCursor)
today = datetime.today()
min_time = datetime.combine(today, time.min)
max_time = datetime.combine(today, time.max)  
date = min_time + timedelta(minutes=10)

while True:
    if date > max_time:
        break
    f = random.randint(40, 70)
    t = random.randint(20, 30)
    sql = f"INSERT INTO humidity VALUES (%s ,%s,%s);"
    cursor.execute(sql, (None, f, date.isoformat() ))
    sql = f"INSERT INTO temperature VALUES (%s ,%s,%s);"
    cursor.execute(sql, (None, t, date.isoformat() ))
    db.commit()
    date = date + timedelta(minutes=10)
db.close()