# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : Time.py
@create time: 2023/4/13 3:35 PM
@modify time: 2023/4/13 3:35 PM
@describe   : 
-------------------------------------------------
"""
from time import strftime, localtime


class Time:
    def curr_time(time_format=None):
        if time_format:
            return strftime(time_format, localtime())
        else:
            return strftime("%Y-%m-%d %H:%M:%S", localtime())
