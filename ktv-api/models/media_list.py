# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from models.dao import Base
from sqlalchemy import Column, Integer, String


class MediaList (Base):
    """
+-------+------------------+------+-----+---------+-------+
| Field | Type             | Null | Key | Default | Extra |
+-------+------------------+------+-----+---------+-------+
| type  | varchar(20)      | NO   | PRI | NULL    |       |
| index | int(10) unsigned | NO   | PRI | NULL    |       |
| mid   | int(10) unsigned | NO   | MUL | NULL    |       |
+-------+------------------+------+-----+---------+-------+
    """
    __tablename__ = 'media_list'
    type = Column(String(20), primary_key=True)
    index = Column(Integer, primary_key=True)
    mid = Column(Integer)