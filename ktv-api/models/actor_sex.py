# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from models.dao import Base
from sqlalchemy import Column, Integer, String


class ActorSex(Base):

    """
    +--------+-----------------+------+-----+---------+----------------+
    | Field  | Type            | Null | Key | Default | Extra          |
    +--------+-----------------+------+-----+---------+----------------+
    | id     | int(2) unsigned | NO   | PRI | NULL    | auto_increment |
    | name   | varchar(8)      | YES  |     | NULL    |                |
    | detail | varchar(16)     | YES  |     | NULL    |                |
    +--------+-----------------+------+-----+---------+----------------+
    """

    __tablename__ = 'actor_sex'
    id = Column(Integer, primary_key=True)
    name = Column(String(8))
    detail = Column(String(16))
