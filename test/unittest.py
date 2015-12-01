# -*-coding:utf-8 -*-
__author__ = 'yin'

import re
import sys
import os
lists =  [(u'information_schema', u'etst', u'sdsdfsdf'), (u'mysql',), (u'performance_schema',), (u'sys',), (u'yiqiding',), (u'yiqiding_info',), (u'yiqiding_ktv',), (u'yqcchaindb',), (u'yqcdb',)]

# delobj = (u'mysql', u'information_schema', u'performance_schema')
# for lis in lists:
#     if lis[0] in delobj:
#         lists.remove(lis)
#     else:
#         print lis
    # del lists[lists.index(tuple(u'msyql',))]


# fp = file('13773022.lrc', 'r')
fp = file('1780038925.krc', 'r')
#1780038925.krc
#1780060491.krc
# ly_text = fp.read()

# with open('1780016821.krc', 'r') as file:
#     for f in file:
#         f = re.sub(r'\[(.*?)\]', '', f)
#         f = re.sub(r'(\s)', '', f)
#         if f in ['\xef\xbb\xbf', '']:
#             continue
#         print repr(f)

while True:
    line_data = fp.readline()
    line_data = re.sub('\[(.*?)\]', '', line_data)
    line_data = re.sub('[\\r][\\n]', '', line_data)
    line_data = re.sub('[\\n]', '', line_data)
    if line_data in ['\xef\xbb\xbf', '']:
        continue
    # line_data = re.sub('\<(.*?)\>', '', line_data)
    # if len(line_data) == len(os.linesep):
    #     pass
    #     print '   sdfsdf f sdf sdf sdf sdf '
    else:
        # print line_data, '测试测试测试测试测试'
        data_all = fp.read()
        ly_text = line_data + os.linesep
        ly_text += data_all
        ly_text = re.sub('\[(.*?)\]', '', ly_text)
        ly_text = re.sub('\<(.*?)\>', '', ly_text)
        print ly_text
        break




