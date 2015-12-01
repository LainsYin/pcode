#!/usr/bin/env python2.7
# -*-coding:utf-8 -*-
__author__ = 'yin'
__date__ = '2015'

from optparse import OptionParser

import json

class TestClass:

    def __init__(self):
        """

        :rtype : object
        """
        self.num = 10
        pass

    def get_num(self, nums):
        print self.num + nums





def res_option():
    parser = OptionParser()
    parser.add_option("--host", dest="host", default="127.0.0.1", help="specify db host")
    parser.add_option("-u", dest="user", default="yqc", help="specify db user")
    parser.add_option("-p", dest="password", default="yqc2014", help="specify db user")
    parser.add_option("-m", "--max", dest="max", default=5000, help="spot-check max num")
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

if __name__ == '__main__':

    list1 = [1, 2, 3, 4]
    list2 = [7, 8, 9]

    list3 = [list1, list2]
    print list3

    for ii in [for data in list3]:
        print ii

    print json.dumps(list3)


    tc = TestClass()
    print tc.get_num(10)

        # print opt.type
    
        # opt = res_option()
    # nums = opt.max.split(",")
    #
    # for obj in opt.type.split(","):
    #     if len(nums):
    #         check_num = nums[0]
    #         del nums[0]
    #     print obj
    #     print check_num
    #     check_num = 0