# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from Models.dao import Base
from sqlalchemy import Column, Integer, String, Text


class ConfigResource(Base):

    """
    +--------+------------------+------+-----+---------+----------------+
    | Field  | Type             | Null | Key | Default | Extra          |
    +--------+------------------+------+-----+---------+----------------+
    | cid    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | name   | varchar(20)      | NO   |     |         |                |
    | value  | varchar(50)      | NO   |     | NULL    |                |
    | detail | text             | YES  |     | NULL    |                |
    +--------+------------------+------+-----+---------+----------------+
    """

    __tablename__ = 'config_resource'
    cid = Column(Integer, primary_key=True)
    name = Column(String(20))
    value = Column(String(50))
    detail = Column(Text)
