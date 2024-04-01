# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/5/7    10:34
============================
自定义全部变量参数
"""
import os
import platform

common_path = os.path.dirname(__file__)

# 连接数据库的driver的jar包地址
DRIVER_PATH = os.path.join(os.path.dirname(common_path), "sql_drive_jar")
# 根目录
ROOT_PATH = os.path.dirname(common_path)

SYSTEM_NAME = platform.system()
DOWNLOAD_PATH = ''  # 浏览器下载文件的默认路径

# 根据系统类型获取文件下载路径
if SYSTEM_NAME == 'Windows':
    DOWNLOAD_PATH = 'D:\\downloads\\'
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)
else:
    DOWNLOAD_PATH = r"/home/seluser/Downloads"  # chrome下载文件存储地址
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)
