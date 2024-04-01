# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/28 14:25
@Author :李国彬
============================
"""
import os
import hashlib

import requests
from requests import Session


class BaseApi:
    session = Session()
    header = None
    ip = ''

    def __init__(self, cookie: dict = None, host: str = '', ):
        self.host = host if host else os.environ["host"]
        self.ip = f'http://{self.host}/'
        if cookie:
            self.session.cookies.update(cookie)

    def _deal_request_data(self, yml_file, api_name, parameter_data: dict = None):
        """处理接口请求yml数据和参数化"""
        # 读取yml接口定义文件的接口属性,并替换接口请求中的参数，进行参数化
        from common.yml import read_yaml_api_parameter
        data = read_yaml_api_parameter(yml_file=yml_file, api_name=api_name, data=parameter_data)
        # keys = data.keys()
        data['url'] = data['url'] if not str(data['url']).startswith('/') else data['url'][1:]
        data['url'] = self.ip + data['url']
        # （保留方法）自行对params参数进行转码的方法，使其和浏览器的url完全一致，避免单双引号和空格导致的差异
        # if 'params' in keys:
        #     keys = list(data['params'].keys())
        #     for key in keys:
        #         value = data['params'][key]
        #         if not isinstance(value, str):
        #             data['params'][key] = json.dumps(value, separators=(',', ':'))
        #     data['params'] = parse.urlencode(data['params'])
        #     data['url'] = data['url'] + '?' + data['params']
        #     del data['params']
        # else:
        #     data['url'] = data['url']

        # 转化params字典值为str
        # if 'params' in keys:
        #     data['params'] = {k: str(v) for k, v in data['params'].items()}
        # 更新headers,如果接口中有headers
        return data

    def api_request_yml(self, yml_file, api_name, data: dict = None, cookies=None):
        """
        处理请求的param参数
        :param: yml_file是接口定义为yml文件
        :param: api_name接口定义yml文件中的接口名称关键字
        :param: data接口请求中参数化的数据，不需要则不传
        """
        data = self._deal_request_data(yml_file=yml_file, api_name=api_name, parameter_data=data)
        res = self.session.request(cookies=cookies, **data)
        res.encoding = 'utf-8'
        return res

    def api_request(self, data, cookies=None):
        """
        :param: data接口请求中参数化的数据，不需要则不传
        """
        data['url'] = data['url'] if not str(data['url']).startswith('/') else data['url'][1:]
        data['url'] = self.ip + data['url']
        if 'headers' in data:
            data['headers']['Host'] = self.host
        return self.session.request(cookies=cookies, **data)

    @staticmethod
    def md5_encryption(plain_text: str):
        """对明文进行md5加密一次，并返回密文"""
        m = hashlib.md5()
        m.update(f'{plain_text}'.encode(encoding='utf-8'))
        return m.hexdigest()
