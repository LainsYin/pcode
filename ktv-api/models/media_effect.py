# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from models.dao import Base
from sqlalchemy import Column, Integer, String


class MediaEffect (Base):
    """
+--------+-----------------+------+-----+---------+----------------+
| Field  | Type            | Null | Key | Default | Extra          |
+--------+-----------------+------+-----+---------+----------------+
| id     | int(2) unsigned | NO   | PRI | NULL    | auto_increment |
| name   | varchar(10)     | YES  |     | NULL    |                |
| detail | varchar(8)      | YES  |     | NULL    |                |
+--------+-----------------+------+-----+---------+----------------+
    """
    __tablename__ = 'media_effect'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    detail = Column(String(8))