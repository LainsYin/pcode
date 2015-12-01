# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, String, SmallInteger


class MediaLanguage (Base):
    """
+--------+-----------------+------+-----+---------+----------------+
| Field  | Type            | Null | Key | Default | Extra          |
+--------+-----------------+------+-----+---------+----------------+
| id     | int(2) unsigned | NO   | PRI | NULL    | auto_increment |
| name   | varchar(9)      | NO   |     |         |                |
| detail | varchar(3)      | NO   |     |         |                |
| part   | tinyint(2)      | NO   |     | 1       |                |
+--------+-----------------+------+-----+---------+----------------+
    """
    __tablename__ = 'media_language'
    id = Column(Integer, primary_key=True)
    name = Column(String(9))
    detail = Column(String(3))
    part = Column(SmallInteger)