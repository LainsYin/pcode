#!/usr/bin/env python2.7
# -*-coding:utf-8 -*-
__author__ = 'yin'
import json
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import logging
from optparse import OptionParser
reload(sys)
sys.setdefaultencoding("utf-8")


class DbCheck:

    def __init__(self, session_check, session, is_json = False):
        self.session_check = session_check
        self.session = session
        self.isjson = is_json

    def compare_field(self, table, db):
        try:
            field_check = self.session_check.execute('show columns from `%s`' % table).fetchall()
            field = self.session.execute('show columns from `%s`' % table).fetchall()
        except Exception, e:
            err_str = ' %s : %s ' % table, e
            self.write_file(db_name=db, err_str=err_str)
            return

        for fil in field_check:
            if len(fil) >= 1:
                if fil not in field:
                    self.write_file(db_name=db, table_name=table, field_name=filed[0])

    def compare_tables(self, db):
        try:
            self.session_check.execute('use %s' % db)
            self.session.execute('use %s' % db)
            list_check = self.session_check.execute('show tables').fetchall()
            list_dst = self.session.execute('show tables').fetchall()
        except Exception, e:
            err_str = ' %s %s ' % list_dst[0], e
            self.write_file(db_name=db, err_str=err_str)
            return

        for tables in list_check:
            if tables in list_dst:
                self.compare_field(tables[0], db)
            else:
                self.write_file(db_name=db, table_name=tables[0])

    def write_file(self, db_name, table_name=None, field_name=None, err_str=None):
        w_str = {}
        if err_str is not None:
            w_str["err"] = err_str
        else:
            if db_name is not None:
                w_str["db"] = db_name
            if table_name is not None:
                w_str["table"] = table_name
            if field_name is not None:
                w_str["field"] = field_name
        if self.isjson:
            logging.debug(json.dumps(w_str, indent=4))
        else:
            logging.debug(w_str)


def init_log(log_name):
    logging.basicConfig(
        level=logging.DEBUG,
        filename=log_name,
        filemode='w')

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    logging.getLogger('').addHandler(sh)


def res_option():
    parser = OptionParser()
    parser.add_option("--host", dest="host", default="127.0.0.1", help="specify db host")
    parser.add_option("--port", dest="port", type="int", default=3306, help="specify db port")
    parser.add_option("--dir", dest="dir", default="/Users/yin/Desktop/yin/", help="res directory")
    parser.add_option("-u", "--user", dest="user", default="yqc", help="specify db user")
    parser.add_option("-p", "--pwd", dest="password", default="yqc2014", help="specify db user")
    parser.add_option("-d", "--db", dest="db", default="yiqiding_ktv", help="specify db database")
    parser.add_option("-l", "--log", dest="log_name", default="res.txt", help="log file name")
    parser.add_option("-j", "--json", dest="json",  default=False, help="output json  False/True")
    parser.add_option("-m", "--max", dest="max", default="0", help="spot-check max num")
    parser.add_option("-t", "--type", dest="type", default="all", help='''specify type, \n
                                                                       [mv]             check mv  video,picture,lyric\n
                                                                       [mv_video]       check mv  video,picture\n
                                                                       [mv_lyric]       check mv  lyric\n
                                                                       [mp3]            check mp3 video,lyric\n
                                                                       [mp3_video]      check mp3 video\n
                                                                       [mp3_lyric]      check mp3 lyric\n
                                                                       [fm_jpg]         check fm  picture\n
                                                                       [actor_jpg]      check singer picture\n
                                                                       [picture]        check fm and singer picture\n
                                                                       [video]          check mv and mp3 video\n
                                                                       [lyric]          check mv and mp3 lyric''')
    (options, args) = parser.parse_args()
    return options


def main(arg_v):

    db_connect_src = 'mysql+mysqldb://%s:%s@%s/yiqiding_ktv?charset=utf8' % (SQL_CON_SRC['user'], SQL_CON_SRC['password'], SQL_CON_SRC['host'])
    db_connect_des = 'mysql+mysqldb://%s:%s@%s/yiqiding_ktv?charset=utf8' % (SQL_CON_DES['user'], SQL_CON_DES['password'], SQL_CON_DES['host'])

    engine_src = create_engine(db_connect_src)
    engine_des = create_engine(db_connect_des)

    session_src = sessionmaker(bind=engine_src)
    session_des = sessionmaker(bind=engine_des)

    global SESSION_SRC
    global SESSION_DES
    SESSION_SRC = session_src()
    SESSION_DES = session_des()

    lists_src = []
    for lists in SESSION_SRC.execute('show databases').fetchall():
        lists_src.append(lists[0])

    database_list = []
    if len(arg_v) > 1:
        for arg in arg_v[1:len(arg_v)]:
            tables_list = arg.split('-')
            if tables_list >= 2:
                ##字段
                if tables_list[0] in lists_src:
                    for table in tables_list:
                        compare_field(table, tables_list[0])
                else:
                    write_file(tables_list[0])
                print tables_list[1], tables_list[0]
            elif tables_list == 1:
                database_list.append(arg)
    else:
        database_list = ['yiqiding', 'yiqiding_ktv', 'yiqiding_info', 'yqcchaindb', 'yqcdb']

    # filename = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    # filename = filename + u'_db.txt'
    if database_list > 1:
        for database in database_list:
            if database in lists_src:
                print ' database name : %s ' % database
                compare_tables(database)
            else:
                write_file(database)


if __name__ == '__main__':
    main(sys.argv)

