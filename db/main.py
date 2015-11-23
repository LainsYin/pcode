__author__ = 'yin'

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


DB_CONNECT_STRING = 'mysql+mysqldb://yqc:yqc2014@localhost/yiqiding_ktv?charset=utf8'
engine = create_engine(DB_CONNECT_STRING)


Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# print session.execute('show columns from media_list').fetchall()
lists = session.execute('show tables').fetchall()
# print lists.index('1111')
print len(lists)

for filed in session.execute('show columns from media_list').fetchall():
    print filed[0]







print 'sqlalchemy version : %s ' % sqlalchemy.__version__

