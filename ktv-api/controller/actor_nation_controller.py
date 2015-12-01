# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'yin'

from base_controller import BaseController
from models.actor_nation import ActorNation


class ActorNationController(BaseController):
    """"""

    url = r'/actor_nation/?'

    def get(self, *args, **kwargs):
        """
        下面调用post方法，意思就是http的get和post返回结果一致
        贾中杰好像有个更牛逼的写法，好像是super继承
        """
        try:
            id_list = self.get_argument('id', []).split(',')
            if len(id_list) == 1 and id_list[0].lower() == 'all':
                res = self.query(ActorNation).all()
            else:
                res = self.query(ActorNation).filter(ActorNation.id.in_(id_list)).all()
            self.do_write([self.pack_nation_info(na) for na in res])
        except Exception, e:
            self.do_write(status=False, error=('argument error.  %s' % e))

    def post(self, *args, **kwargs):
        """"""
        # serial_id_list = self.get_argument('serial_id_list', []).split(',')
        #
        # res = self.query(Media).filter(Media.serial_id.in_(serial_id_list)).all()
        # self.do_write([self.pack_media_info(m) for m in res])
        # TODO 这里还可以这么写，这样写就不用下面的function了
        # self.do_write([dict(mid=m.mid, serial_id_list=m.serial_id,  # ====许多信息
        #                     ) for m in res])

    def pack_nation_info(self, nn):
        """
        在这里把所有需要返回的字段写入一个dict
        """
        print nn
        return dict(id=nn.id, nation=nn.nation, detail=nn.detail)
