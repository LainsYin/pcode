# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, String


class MediaType (Base):
    """
+--------+-----------------+------+-----+---------+----------------+
| Field  | Type            | Null | Key | Default | Extra          |
+--------+-----------------+------+-----+---------+----------------+
| id     | int(2) unsigned | NO   | PRI | NULL    | auto_increment |
| name   | varchar(16)     | NO   |     |         |                |
| detail | varchar(8)      | NO   |     |         |                |
+--------+-----------------+------+-----+---------+----------------+
    """
    __tablename__ = 'media_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    detail = Column(String(8))