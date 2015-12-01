# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, String, Date, SmallInteger, Text


class SongList(Base):
    """
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| lid       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| serial_id | int(10)          | NO   | MUL | NULL    |                |
| title     | varchar(20)      | NO   |     |         |                |
| image     | varchar(60)      | NO   |     |         |                |
| type      | varchar(10)      | NO   |     |         |                |
| count     | int(5)           | NO   |     | NULL    |                |
| special   | int(1)           | NO   |     | NULL    |                |
+-----------+------------------+------+-----+---------+----------------+
    """
    __tablename__ = 'songlist'

    lid = Column(Integer, primary_key=True)
    serial_id = Column(Integer, index=True)
    title = Column(String(20))
    image = Column(String(60))
    type = Column(String(10))
    count = Column(Integer)
    special = Column(SmallInteger)