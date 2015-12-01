# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, Text


class MediaLyric (Base):
    """
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| id        | int(11) unsigned | NO   | PRI | NULL    | auto_increment |
| type      | int(8)           | NO   |     | NULL    |                |
| serial_id | int(11)          | YES  |     | NULL    |                |
| lyric     | text             | YES  |     | NULL    |                |
+-----------+------------------+------+-----+---------+----------------+
    """
    __tablename__ = 'media_lyric'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    serial_id = Column(Integer)
    lyric = Column(Text)