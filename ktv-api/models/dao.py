# -*- coding: utf-8 -*-

"""
Description
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import redis
from models.config import Config

__author__ = 'TT'

Base = declarative_base()


class Dao(object):
    """"""
    __db_uri = 'sqlite:///:memory:'  # 默认就是sqlite
    __echo = True
    __coding = 'utf8'
    __rds_host = '127.0.0.1'
    __rds_port = 6379
    __rds_passwd = ''
    __session = None
    __redis = None
    __connect = None
    __media_con = None
    __config = None

    @staticmethod
    def init_db_uri(env=None):

        Dao.__config = Config(env)
        Dao.__db_uri = 'mysql://{}:{}@{}/{}?charset=utf8'.format(
            Dao.__config.mysql_user, Dao.__config.mysql_passwd,
            Dao.__config.mysql_host, Dao.__config.mysql_db
        )
        Dao.__rds_host = Dao.__config.redis_host
        Dao.__rds_port = Dao.__config.redis_port
        Dao.__rds_passwd = Dao.__config.redis_passwd

    @staticmethod
    def db_uri(user='root', host='127.0.0.1', password='123', db='lohas'):
        return 'mysql://{}:{}@{}/{}?charset=utf8'.format(user, password, host, db)

    @staticmethod
    def engine():
        """
        pool_recycle: 3500s后会重新连接mysql，把mysql连接的自动断开时间设置成3600s
        解决问题：
        ```
        OperationalError: (_mysql_exceptions.OperationalError) (2006, 'MySQL server has gone away')
        ```
        """
        return create_engine(Dao.__db_uri, echo=Dao.__config.mysql_echo, encoding=Dao.__coding,
                             pool_recycle=3500)

    @staticmethod
    def media_engine(uri):
        """"""
        return create_engine(uri, echo=Dao.__config.mysql_echo, encoding=Dao.__coding)

    @staticmethod
    def db_session():
        """"""
        if Dao.__session is None:  # or Dao.__session.is_active:
            Dao.__session = Session(bind=Dao.engine())
        return Dao.__session

    @staticmethod
    def db_connect():
        """"""
        if Dao.__connect is None:  # or Dao.__connect.invalidated:
            Dao.__connect = Dao.engine().connect()
        return Dao.__connect

    @staticmethod
    def media_connect():
        """"""
        if Dao.__media_con is None:
            Dao.__media_con = Dao.media_engine(Dao.db_uri(
                user='root', host='127.0.0.1', password='123456', db='ktv'))
        return Dao.__media_con

    @staticmethod
    def init_schema():
        """"""
        Base.metadata.create_all(bind=Dao.engine())

    @staticmethod
    def rds(db=0, name=None):
        """
        这是一个redis连接，因为redis有0-15个数据库，每种业务调用不同的redis db，所以，这里指定一下redis的db号
        """
        if name is not None:
            db = Config.redis_db.get(name) or 0
        if Dao.__redis is None:
            Dao.__redis = redis.Redis(
                connection_pool=redis.ConnectionPool(
                    host=Dao.__rds_host,
                    port=Dao.__rds_port,
                    db=db,
                    password=Dao.__rds_passwd
                )
            )
        return Dao.__redis
