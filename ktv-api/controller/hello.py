# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

from base_controller import BaseController


class Hello(BaseController):
    """
    这是一个返回hello的例子
    url 是正则表达式

    self.do_write() 返回一个json结果
    self.render（） 渲染页面模板
    """
    url = r'/hello/?'

    def get(self, *args, **kwargs):
        """
        这是一个http get请求的处理方法
        """

        str_arg = self.get_argument('str_arg_name', 'default_value')
        print str_arg
        try:
            # 这里扑捉程序中的异常
            int_arg_1 = int(self.get_argument('int_arg_1', 0))  # 如果不是必传参数，默认值为0
            int_arg_2 = int(self.get_argument('int_arg_2', None))  # 如果是必传参数，默认值为 None
        except (TypeError, ValueError):  # 执行内置函数 int 的时候，会抛出这两个异常
            # 这里还可以对参数重新赋值
            int_arg_1 = 0
            int_arg_2 = 0
            # 这里还可以response错误信息回去
            return self.do_write(status=False, error='int_arg_2 是必传 int 型参数，参数值错误')
        # 这里原封不动返回传入的参数
        self.do_write(dict(str_arg=str_arg, int_arg_1=int_arg_1, int_arg_2=int_arg_2))

    def post(self, *args, **kwargs):
        """
        这是一个http post请求的处理方法
        获取参数的方法跟上面一样，返回response的方法也一样
        """
        str_arg = self.get_argument('str_arg_name', 'default_value')
        try:
            # 这里扑捉程序中的异常
            int_arg_1 = int(self.get_argument('int_arg_1', 0))  # 如果不是必传参数，默认值为0
            int_arg_2 = int(self.get_argument('int_arg_2', None))  # 如果是必传参数，默认值为 None
        except (TypeError, ValueError):  # 执行内置函数 int 的时候，会抛出这两个异常
            # 这里还可以对参数重新赋值
            int_arg_1 = 0
            int_arg_2 = 0
            # 这里还可以response错误信息回去
            return self.do_write(status=False, error='int_arg_2 是必传 int 型参数，参数值错误')
        self.do_write(dict(str_arg=str_arg, int_arg_1=int_arg_1, int_arg_2=int_arg_2))
