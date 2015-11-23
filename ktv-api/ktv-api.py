# -*- coding: utf-8 -*-

"""
Description
"""

import os
# import sys
# sys.path.insert(0, './models/')
import tornado.options
from tornado.options import options, define
import tornado.web
from tornado.httpserver import HTTPServer
import tornado.ioloop
import log
from models.dao import Dao
from models.config import Config
from controller.media_controller import MediaController
from controller.hello import Hello

__author__ = 'TT'


class Application(tornado.web.Application):
    """"""
    def __init__(self):
        urls = [
            (Hello.url, Hello),
            (MediaController.url, MediaController),
        ]

        settings = dict(
            xsrf_cookies=False,
            debug=False,
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            cookie_secret='mhKyzj30Sc+Z4xuR2bS2WTGrT96xfkVQiWoxWQQeZfY=',
            login_url='/login/',
        )

        tornado.web.Application.__init__(self, urls, **settings)


if __name__ == '__main__':
    """"""
    options.define(name='config', default='test')
    options.define(name='port', default=38001)
    options.define(name='process', default=1)
    options.define(name='server', default='total')

    tornado.options.parse_command_line()
    config = Config(options.config)
    Dao.init_db_uri(options.config)
    # TODO for dev and test
    # Dao.init_schema()

    app = Application()
    app.config = options.config

    log.info('Starting box api server... Listening port: {}'.format(options.port))
    try:
        server = HTTPServer(app, xheaders=True)
        server.bind(int(options.port))
        server.start(num_processes=int(options.process))
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        log.error('box api can not running:\n{}'.format(e), exc_info=True)
        tornado.ioloop.IOLoop.instance().stop()

