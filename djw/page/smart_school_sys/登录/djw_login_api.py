# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/4 15:16
@Author :李国彬
============================
"""
import os

from common.base_api import BaseApi


class DjwLoginApi(BaseApi):
    """登录api"""
    file = os.path.join(os.path.dirname(__file__), 'djw_login.yml')

    def login(self, data: dict):
        return self.api_request_yml(yml_file=self.file, api_name='登录接口', data=data)

    def app_login(self, data: dict):
        data['password'] = 'ed61bdf4033614f80e4799ce857aee7a'
        # data['password'] = self.md5_encryption(self.md5_encryption(data['password']))
        return self.api_request_yml(yml_file=self.file, api_name='app登录接口', data=data)
