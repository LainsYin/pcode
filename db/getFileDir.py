# -*-coding:utf-8 -*-
__author__ = 'yin'


import os

fileList = []
filePath = '/var/www/lyrics'
fileNames = os.listdir(filePath)
file = open('names.txt', 'w')
print ' file path : %s ' % fileNames
if len(fileNames)>0:
    for fn in fileNames:
        file.write('%s%s' % (fn, os.linesep))
        # fullfilename=os.path.join(findPath, fn)
        # fileList.append(fullfilename)

file.close()
#对文件名排序
# if (len(fileList)>0):
#     fileList.sort()
#
# return fileList