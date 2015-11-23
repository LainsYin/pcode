# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

from base_controller import BaseController
from models.media import Media


class MediaController(BaseController):
    """"""

    def get(self, *args, **kwargs):
        """
        下面调用post方法，意思就是http的get和post返回结果一致
        贾中杰好像有个更牛逼的写法，好像是super继承
        """
        return self.post()

    def post(self, *args, **kwargs):
        """"""
        serial_id_list = self.get_argument('serial_id_list', [])

        res = self.query(Media).filter(Media.serial_id.in_(serial_id_list)).all()
        self.do_write([self.pack_media_info(m) for m in res])
        # TODO 这里还可以这么写，这样写就不用下面的function了
        # self.do_write([dict(mid=m.mid, serial_id_list=m.serial_id,  # ====许多信息
        #                     ) for m in res])

    def pack_media_info(self, m):
        """
        在这里把所有需要返回的字段写入一个dict
        """
        return dict(mid=m.mid, serial_id=m.serial_id, name=m.name,
                    language=m.language, type=m.type, singer=m.sinnger,
                    header=m.header)
