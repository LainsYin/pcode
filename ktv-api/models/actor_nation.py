# -*- coding: utf-8 -*-

"""
Description
"""
__author__ = 'yin'


from models.dao import Base
from sqlalchemy import Column, Integer, String


class ActorNation(Base):

    """
    +--------+-----------------+------+-----+---------+----------------+
    | Field  | Type            | Null | Key | Default | Extra          |
    +--------+-----------------+------+-----+---------+----------------+
    | id     | int(2) unsigned | NO   | PRI | NULL    | auto_increment |
    | nation | varchar(11)     | NO   |     |         |                |
    | detail | varchar(5)      | NO   |     |         |                |
    +--------+-----------------+------+-----+---------+----------------+
    """
    __tablename__ = 'actor_nation'

    id = Column(Integer, primary_key=True)
    nation = Column(String(11))
    detail = Column(String(5))
