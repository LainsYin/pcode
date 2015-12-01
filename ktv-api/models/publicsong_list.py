# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from models.dao import Base
from sqlalchemy import Column, Integer, String


class PublicSongList (Base):
    """
+-------+------------------+------+-----+---------+-------+
| Field | Type             | Null | Key | Default | Extra |
+-------+------------------+------+-----+---------+-------+
| type  | varchar(20)      | NO   | PRI | NULL    |       |
| index | int(11) unsigned | NO   | PRI | NULL    |       |
| mid   | int(11) unsigned | NO   |     | NULL    |       |
+-------+------------------+------+-----+---------+-------+
    """
    __tablename__ = 'publicsong_list'

    type = Column(String(20), primary_key=True)
    index = Column(Integer, primary_key=True)
    mid = Column(Integer)