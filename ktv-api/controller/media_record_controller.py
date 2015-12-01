# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, TIMESTAMP


class MediaRecord (Base):
    """
+-------+------------------+------+-----+-------------------+-----------------------------+
| Field | Type             | Null | Key | Default           | Extra                       |
+-------+------------------+------+-----+-------------------+-----------------------------+
| id    | int(10) unsigned | NO   | PRI | NULL              | auto_increment              |
| time  | timestamp        | NO   | MUL | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
| boxid | int(10) unsigned | NO   |     | NULL              |                             |
| mid   | int(10)          | NO   |     | NULL              |                             |
+-------+------------------+------+-----+-------------------+-----------------------------+
    """
    __tablename__ = 'media_record'

    id = Column(Integer, primary_key=True)
    time = Column(TIMESTAMP)
    box_id = Column(Integer)
    mid = Column(Integer)