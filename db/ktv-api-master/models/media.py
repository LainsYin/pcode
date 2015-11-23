# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

from models.dao import Base
from sqlalchemy import Column, Integer, String, Float, Date, SmallInteger, Text


class Media(Base):
    """
+----------------+------------------+------+-----+---------+----------------+
| Field          | Type             | Null | Key | Default | Extra          |
+----------------+------------------+------+-----+---------+----------------+
| mid            | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| serial_id      | int(10)          | YES  | MUL | NULL    |                |
| name           | varchar(200)     | NO   | MUL |         |                |
| language       | int(2) unsigned  | NO   | MUL | NULL    |                |
| type           | int(2) unsigned  | NO   | MUL | NULL    |                |
| singer         | varchar(100)     | NO   |     |         |                |
| artist_sid_1   | int(10)          | YES  | MUL | NULL    |                |
| artist_sid_2   | int(10)          | YES  | MUL | NULL    |                |
| pinyin         | varchar(200)     | NO   | MUL | NULL    |                |
| header         | varchar(100)     | NO   | MUL | NULL    |                |
| head           | varchar(1)       | YES  | MUL | NULL    |                |
| words          | int(3)           | NO   | MUL | NULL    |                |
| path           | varchar(100)     | NO   |     | NULL    |                |
| lyric          | text             | YES  |     | NULL    |                |
| original_track | int(1)           | NO   |     | NULL    |                |
| sound_track    | int(1)           | NO   |     | NULL    |                |
| start_volume_1 | int(3)           | YES  |     | NULL    |                |
| start_volume_2 | int(3)           | YES  |     | NULL    |                |
| prelude        | int(3)           | YES  |     | NULL    |                |
| effect         | int(2)           | YES  |     | NULL    |                |
| version        | int(2)           | YES  |     | NULL    |                |
| create_time    | date             | YES  |     | NULL    |                |
| stars          | float(2,1)       | NO   |     | NULL    |                |
| hot            | int(1)           | NO   |     | NULL    |                |
| count          | int(10)          | NO   |     | NULL    |                |
| enabled        | int(1)           | NO   | MUL | NULL    |                |
| black          | int(1)           | NO   |     | NULL    |                |
| match          | int(1)           | YES  |     | NULL    |                |
| update_time    | date             | YES  |     | NULL    |                |
| resolution     | int(2)           | YES  |     | NULL    |                |
| quality        | int(2)           | YES  |     | NULL    |                |
| source         | int(2)           | YES  |     | NULL    |                |
| rhythm         | int(2)           | YES  |     | NULL    |                |
| pitch          | int(2)           | YES  |     | NULL    |                |
| info           | text             | YES  |     | NULL    |                |
| lang_part      | tinyint(2)       | YES  | MUL | NULL    |                |
| desc_count     | int(11)          | YES  |     | NULL    |                |
+----------------+------------------+------+-----+---------+----------------+
    """
    __tablename__ = 'media'

    mid = Column(Integer, primary_key=True)
    serial_id = Column(Integer, unique=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    language = Column(SmallInteger, nullable=False, index=True)
    type = Column(SmallInteger, nullable=False, index=True)
    singer = Column(String(100), nullable=False)
    artist_sid_1 = Column(Integer, index=True)
    artist_sid_2 = Column(Integer, index=True)
    pinyin = Column(String(200), nullable=False, index=True)
    header = Column(String(100), nullable=False, index=True)
    head = Column(String(1), nullable=False, index=True)
    words = Column(SmallInteger, nullable=False, index=True)
    path = Column(String(100))
    lyric = Column(Text)
    original_track = Column(SmallInteger)
    sound_track = Column(SmallInteger)
    start_volume_1 = Column(SmallInteger)
    start_volume_2 = Column(SmallInteger)
    prelude = Column(SmallInteger)
    effect = Column(SmallInteger)
    version = Column(SmallInteger)
    create_time = Column(Date)
    stars = Column(Float(1), nullable=False)
    hot = Column(SmallInteger, nullable=False, default=0)
    count = Column(Integer, nullable=False)
    enabled = Column(SmallInteger, nullable=False, index=True)
    black = Column(SmallInteger, nullable=False, index=True)
    match = Column(SmallInteger)
    update_time = Column(Date)
    resolution = Column(SmallInteger)
    quality = Column(SmallInteger)
    source = Column(SmallInteger)
    rhythm = Column(SmallInteger)
    pitch = Column(SmallInteger)
    info = Column(Text)
    lang_part = Column(SmallInteger, nullable=False, index=True)
    desc_count = Column(Integer)
