# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'

from models.dao import Base
from sqlalchemy import Column, Integer, String, Float, SmallInteger, Text


class Actor(Base):
    """
    +------------------+------------------+------+-----+---------+----------------+
    | Field            | Type             | Null | Key | Default | Extra          |
    +------------------+------------------+------+-----+---------+----------------+
    | sid              | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | serial_id        | int(10)          | NO   | MUL | NULL    |                |
    | name             | varchar(40)      | NO   | MUL |         |                |
    | nation           | int(2)           | NO   |     | NULL    |                |
    | sex              | int(1)           | NO   |     | NULL    |                |
    | pinyin           | varchar(100)     | NO   | MUL |         |                |
    | header           | varchar(30)      | YES  | MUL | NULL    |                |
    | head             | varchar(1)       | YES  | MUL | NULL    |                |
    | words            | int(3)           | NO   |     | NULL    |                |
    | song_count       | int(5)           | NO   |     | NULL    |                |
    | stars            | float(2,1)       | YES  |     | NULL    |                |
    | count            | int(10)          | NO   |     | NULL    |                |
    | order            | int(5)           | YES  |     | NULL    |                |
    | enabled          | int(1)           | NO   |     | NULL    |                |
    | black            | int(1)           | NO   |     | NULL    |                |
    | info             | text             | YES  |     | NULL    |                |
    | baiwei_recommend | int(11)          | YES  |     | 0       |                |
    +------------------+------------------+------+-----+---------+----------------+
    """
    __tablename__ = 'actor'
    sid = Column(Integer, primary_key=True)
    serial_id = Column(Integer, index=True)
    name = Column(String(200), nullable=False, index=True)
    nation = Column(SmallInteger, nullable=False, index=True)
    sex = Column(SmallInteger, nullable=False, index=True)
    pinyin = Column(String(200), nullable=False, index=True)
    header = Column(String(100), index=True)
    head = Column(SmallInteger, index=True)
    words = Column(SmallInteger)
    song_count = Column(Integer)
    stars = Column(Float)
    count = Column(Integer)
    order = Column(Integer)
    enabled = Column(SmallInteger)
    black = Column(SmallInteger)
    info = Column(Text)
    baiwei_recommend = Column(Integer)