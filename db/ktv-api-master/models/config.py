# -*- coding: utf-8 -*-

"""
所有的配置文件都在这里

mysql的配置

redis的配置

"""

__author__ = 'TT'


class Config(object):
    """"""

    # 这里定义redis的db 号码
    redis_db = dict(

    )

    def __init__(self, env=None):
        """
        初始化配置文件，区分测试域名和生产域名，数据库连接等等信息
        """

        if env == 'test':
            self.test_conf()
        elif env == 'ktv':
            self.ktv_conf()
        else:  # if env is None or env == 'dev':
            # debug mode
            self.debug = False
            # mysql config
            self.mysql_user = 'root'
            self.mysql_host = '127.0.0.1'
            self.mysql_passwd = '123456'
            self.mysql_db = 'lohas'
            self.mysql_port = '3306'
            self.mysql_echo = True
            # redis config
            self.redis_host = '127.0.0.1'
            self.redis_port = '6379'
            self.redis_passwd = ''

    def test_conf(self):
        """"""
        # debug mode
        self.debug = False
        # mysql config
        self.mysql_user = 'root'
        self.mysql_host = ''
        self.mysql_passwd = ''
        self.mysql_db = ''
        self.mysql_port = '3306'
        self.mysql_echo = False
        # redis config
        self.redis_host = ''
        self.redis_port = ''
        self.redis_passwd = ''

    def ktv_conf(self):
        """"""
        # debug mode
        self.debug = False
        # mysql config
        self.mysql_user = ''
        self.mysql_host = ''
        self.mysql_passwd = ''
        self.mysql_db = ''
        self.mysql_port = '3306'
        self.mysql_echo = False
        # redis config
        self.redis_host = ''
        self.redis_port = ''
        self.redis_passwd = ''
