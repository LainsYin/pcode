# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, String


class MediaQuality (Base):
    """
+-------+-----------------+------+-----+---------+----------------+
| Field | Type            | Null | Key | Default | Extra          |
+-------+-----------------+------+-----+---------+----------------+
| id    | int(2) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(32)     | YES  |     | NULL    |                |
+-------+-----------------+------+-----+---------+----------------+
    """
    __tablename__ = 'media_quality'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))