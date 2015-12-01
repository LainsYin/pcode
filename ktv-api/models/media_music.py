# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from models.dao import Base
from sqlalchemy import Column, Integer, String, Date, SmallInteger, Text


class MediaMusic(Base):
    """
+--------------+------------------+------+-----+---------+----------------+
| Field        | Type             | Null | Key | Default | Extra          |
+--------------+------------------+------+-----+---------+----------------+
| mmid         | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| serial_id    | int(10)          | YES  | MUL | NULL    |                |
| name         | varchar(200)     | NO   | MUL |         |                |
| singer       | varchar(100)     | NO   |     |         |                |
| artist_sid_1 | int(10)          | YES  | MUL | NULL    |                |
| artist_sid_2 | int(10)          | YES  | MUL | NULL    |                |
| pinyin       | varchar(200)     | NO   | MUL | NULL    |                |
| header       | varchar(100)     | NO   | MUL | NULL    |                |
| head         | varchar(1)       | YES  | MUL | NULL    |                |
| words        | int(3)           | NO   |     | NULL    |                |
| path         | varchar(100)     | NO   |     | NULL    |                |
| lyric        | text             | YES  |     | NULL    |                |
| prelude      | int(3)           | YES  |     | NULL    |                |
| create_time  | date             | YES  |     | NULL    |                |
| count        | int(10)          | NO   |     | NULL    |                |
| enabled      | int(1)           | NO   |     | NULL    |                |
| update_time  | date             | YES  |     | NULL    |                |
| has_lyric    | tinyint(2)       | NO   |     | 1       |                |
+--------------+------------------+------+-----+---------+----------------+
    """
    __tablename__ = 'media_music'

    mmid = Column(Integer, primary_key=True)
    serial_id = Column(Integer, unique=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    singer = Column(String(100), nullable=False)
    artist_sid_1 = Column(Integer, index=True)
    artist_sid_2 = Column(Integer, index=True)
    pinyin = Column(String(200), nullable=False, index=True)
    header = Column(String(100), nullable=False, index=True)
    head = Column(String(1), nullable=False, index=True)
    words = Column(SmallInteger, nullable=False, index=True)
    path = Column(String(100))
    lyric = Column(Text)
    prelude = Column(SmallInteger)
    create_time = Column(Date)
    count = Column(Integer, nullable=False)
    enabled = Column(SmallInteger, nullable=False, index=True)
    update_time = Column(Date)
    has_lyric = Column(SmallInteger, nullable=False, default=1)