# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, String, Date, SmallInteger, Text


class SongListDetail(Base):
    """
+-------+------------------+------+-----+---------+-------+
| Field | Type             | Null | Key | Default | Extra |
+-------+------------------+------+-----+---------+-------+
| lid   | int(10) unsigned | NO   | PRI | NULL    |       |
| index | int(10) unsigned | NO   | PRI | NULL    |       |
| mid   | int(10) unsigned | NO   | MUL | NULL    |       |
+-------+------------------+------+-----+---------+-------+
    """
    __tablename__ = 'songlist_detail'

    lid = Column(Integer, primary_key=True)
    index = Column(Integer, primary_key=True)
    mid = Column(Integer)