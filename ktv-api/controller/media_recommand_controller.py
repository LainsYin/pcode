# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer


class MediaRecommand (Base):
    """
+-------+------------------+------+-----+---------+-------+
| Field | Type             | Null | Key | Default | Extra |
+-------+------------------+------+-----+---------+-------+
| mid   | int(10) unsigned | NO   | MUL | NULL    |       |
| rmid  | int(10) unsigned | NO   | MUL | NULL    |       |
+-------+------------------+------+-----+---------+-------+
    """
    __tablename__ = 'media_recommand'

    mid = Column(Integer, primary_key=True)
    rmid = Column(Integer)