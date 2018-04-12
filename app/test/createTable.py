from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import config
import pymysql

db= pymysql.connect(host="localhost",user="root",
    password="123456",db="song",port=3306)

stmt = db.cursor()
'''
stmt.execute(''
             create table if not EXISTS  test (id int not null AUTO_INCREMENT,
                               usrname char(30) not null,
                               email char(100),
                               PRIMARY KEY ( id )
             );''
             )
'''

stmt.execute("select * from test")
db.commit()

rs = stmt.fetchall()
print(rs)