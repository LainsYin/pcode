__author__ = 'yin'

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

DB_CONNECT_STRING = 'mysql+mysqldb://root:123@localhost/yiqiding_ktv?charset=utf8'
engine = create_engine(DB_CONNECT_STRING)
metadata = BoundMetaData(engine)

