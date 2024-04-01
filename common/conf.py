# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/1   16:30
============================
"""
from configparser import ConfigParser
from common.file_path import config_dir, api_dir
import os

ini_path = os.path.join(config_dir, 'info.ini')
api_ini_path = os.path.join(api_dir, 'api_info.ini')


class Config(ConfigParser):
    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.filename = filename
        self.encoding = encoding

    def read_conf(self, select, option):
        """读取ini配置文件中的数据
        :param select:
        :param option:
        :return: value
        """
        self.read(self.filename, encoding=self.encoding)
        conf = self.get(select, option)
        return conf

    def write_conf(self, select, option, value):
        """
        往配置文件中写入数据
        :param select:
        :param option:
        :param value:
        :return:
        """
        self.set(select, option, value)
        self.write(fp=open(self.filename, "w", encoding=self.encoding))


def conf(select, option):
    """简易版查询配置文件信息"""
    config = ConfigParser()
    config.read(ini_path, encoding='utf-8')
    conf = config.get(select, option)
    return conf


def conf_(select, option):
    """查询api配置文件信息"""
    config = ConfigParser()
    config.read(api_ini_path, encoding='utf-8')
    conf = config.get(select, option)
    return conf


conf1 = Config(ini_path)
