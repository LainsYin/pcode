# -*-coding:utf-8 -*-
__author__ = 'yin'


import os

# p3lyric = '/Users/yin/Desktop/yin/lyrics.txt'
# if os.path.isfile(p3lyric):
#     dirlyric = os.path.dirname(p3lyric) + '/' + 'lyrics'
#     print dirlyric
#     if os.path.isdir(dirlyric):
#         pass
#     else:
#         os.mkdir(dirlyric)
#
#     p3file = file(p3lyric, 'r')
#     for p3file in p3file:
#         dir = dirlyric + '/' + p3file.strip(os.linesep)
#         print dir
#         open(dir, 'w')

ydir = '/Users/yin/Desktop/yin/'

filelist = ['lyrics.txt']
# filelist = ['01.txt', '02.txt', '03.txt', '04.txt', '05.txt', '06.txt', '07.txt', '08.txt', '09.txt', 'lyrics.txt']
for filen in filelist:
    curfile = ydir + filen
    if os.path.isfile(curfile):
        readf = file(curfile, 'r')
        curdir = ydir + filen.strip('.txt')
        print curdir
        if os.path.isdir(curdir):
            pass
        else:
            os.mkdir(curdir)

        num = 0
        # print len(readf.readlines())
        for eachline in readf.readlines():
            dir = curdir + '/' + eachline.strip(os.linesep)
            num += 1
            fp = open(dir, 'w')
            fp.close()
            print dir,   num
