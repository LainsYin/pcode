__author__ = 'yin'
# -*- coding:utf-8 -*-
import MySQLdb
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class ML(Base):
    __tablename__ = 'media_language'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    detail = Column(String)
    part = Column(Integer)

class Media(Base):
    __tablename__ = 'media'
    mid = Column(Integer, primary_key=True)
    serial_id = Column(Integer)
    name = Column(String)
    pinyin = Column(String)
    count = Column(Integer)


db_config = {
    'host': '127.0.0.1',
    'user': 'yqc',
    'passwd': 'yqc2014',
    'db': 'yiqiding_ktv',
    'charset': 'utf8'
}

engine = create_engine('mysql://%s:%s@%s/%s?charset=%s'%(db_config['user'],
                                                         db_config['passwd'],
                                                         db_config['host'],
                                                         db_config['db'],
                                                         db_config['charset']), echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

for med_lin in session.query(Media).order_by(Media.mid):
    print med_lin.mid, med_lin.serial_id, med_lin.name, med_lin.pinyin, med_lin.count


# for intance in session.query(ML).order_by(ML.id):
#     print intance.id, intance.name, intance.detail, intance.part

# print MLTest.id
# print MLTest.name
# print MLTest.detail
# print MLTest.part

session.close()