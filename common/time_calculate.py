# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/16    15:02
============================
"""
import datetime
import time


def date_calculate(input_time: datetime.datetime, time_format: str = "%Y-%m-%d", days=0, hours=0, minutes=0, seconds=0):
    """
    根据时间戳计算时间，返回指定的时间格式
    :param input_time：传入的时间
    :param days: 与当前时间相差的日期，正数则相加，负数相减
    :param time_format: 指定输出的时间格式
    :param hours: 与输入时间相差的小时，正数则相加，负数相减
    :param minutes: 与当前时间相差的分钟数，正数则相加，负数相减
    :param seconds: 与输入时间相差的秒数，正数则相加，负数相减
    """
    if days or hours or minutes or seconds:
        return (input_time + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)).strftime(time_format)
    else:
        return input_time.strftime(time_format)


def current_time_str():
    """返回整数的时间戳字符串"""
    return str(int(time.time()))
