# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

import traceback
from tornado.web import RequestHandler
from models.dao import Dao
from sqlalchemy.exc import SQLAlchemyError
import log
import json
import itertools
import base64
import math
import time
import hashlib
from models.config import Config
import sys


class BaseController(RequestHandler):
    """
    继承 tornado.web.RequestHandler
    在这里写一些所有Handler都会用的到方法
    实现MVC框架，所以就把Handler改名为Controller
    每一个子Controller都继承BaseController就好
    """

    def do_write(self, data=None, status=True, error="", expect_time=500, send_mail=None):
        """这里做的事情比较简单，返回json对象给app或者机顶盒的时候，都是固定格式。
        status: bool(True/False),
        error: str('error message or ""'),
        result: dict('data object') or True.
        """
        if data is None:
            data = {}
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps(dict(status=status, error=error, result=data), ensure_ascii=False))

    @property
    def db_session(self):
        """返回mysql连接session会话，sqlalchemy的Session，具体用户间sqlalchemy文档。
        大体功能：可以query，add，update某个表对象，执行commit提交。但是报错需rollback()
        """
        return Dao.db_session()

    @property
    def db_connect(self):
        """返回一个数据库连接，跟上面的session不一样，想要裸写sql就调用这个。
        execute("把sql语句写进来就好了")，返回的结果需要注意，是ResultProxy。了解详细见下面连接
        http://docs.sqlalchemy.org/en/rel_1_0/core/connections.html?highlight=resultproxy#sqlalchemy.engine.ResultProxy。
        但是可以调用first(), all()等，差不多了一样用。只是返回的类似dict或mapping，先dict(res.items())比较好。
        """
        return Dao.db_connect()

    def media_con(self):
        """曲库的数据库连接
        """
        return Dao.media_connect()

    @property
    def commit(self):
        """:returns bool
        session的commit操作，如果操作完成，返回True，失败返回False。
        失败的时候，会rollback()，记录log，http返回数据库错误什么的，随意就好了。
        """
        try:
            self.db_session.commit()
            return True
        except SQLAlchemyError:
            self.db_session.rollback()
            log.error(msg='SQLAlchemyError', exc_info=True)
            return False

    def query(self, *entities, **kwargs):
        """
        这里调用sqlalchemry的query
        """
        try:
            return self.db_session.query(*entities, **kwargs)
        except SQLAlchemyError:
            self.db_session.rollback()
            log.error('SQLAlchemryError', exc_info=True)
            return None
