# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2022/7/27 14:35
# Author     ：李国彬
============================
"""
from common.tools_packages import *


class BbsModelInfoPage(BasePage):
    """板块信息"""

    @allure.step('查询板块')
    def search_model(self, key=""):
        self.locator_search_input(placeholder='请输入板块名称', value=key)
        self.locator_tag_search_button()
        return self

    @allure.step('新增板块')
    def add_model(self, name):
        self.locator_button(button_title='新增')
        self.locator_text_input(ctrl_id='catalog_name', value=name)
        self.locator_button(button_title='保存')
        time.sleep(3)
        return self
