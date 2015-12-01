# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from models.dao import Base
from sqlalchemy import Column, Integer, String


class PublicSongIp (Base):
    """
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| type  | varchar(50) | NO   | MUL | NULL    |                |
| ip    | varchar(50) | NO   | UNI | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
    """
    __tablename__ = 'publicsong_ip'

    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    ip = Column(String(50))