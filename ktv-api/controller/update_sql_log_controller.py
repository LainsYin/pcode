# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, String, Date, SmallInteger, Text


class UpdateSqlLog(Base):
    """
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| id          | int(11)     | NO   | PRI | NULL    | auto_increment |
| type        | varchar(50) | YES  |     | NULL    |                |
| version     | varchar(50) | YES  | MUL | NULL    |                |
| create_time | datetime    | YES  |     | NULL    |                |
| update_time | datetime    | YES  | MUL | NULL    |                |
| info        | text        | YES  |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
    """
    __tablename__ = 'update_sql_log'

    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    version = Column(String(50))
    create_time = Column(Date)
    update_time = Column(Date)
    info = Column(Text)