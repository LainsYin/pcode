# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

import logging
import sys


def error(msg, controller=None, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger.
    """
    if msg == 'SQLAlchemyError' and controller is not None:
        controller.db_session().rollback()
    logging.error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """
    Log a message with severity 'WARNING' on the root logger.
    """
    logging.warning(msg, *args, **kwargs)

warn = warning


def info(msg, *args, **kwargs):
    """
    Log a message with severity 'INFO' on the root logger.
    """
    logging.info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    """
    Log a message with severity 'DEBUG' on the root logger.
    """
    logging.debug(msg, *args, **kwargs)


def log(level, msg, *args, **kwargs):
    """
    Log 'msg % args' with the integer severity 'level' on the root logger.
    """
    logging.log(level, msg, *args, **kwargs)

