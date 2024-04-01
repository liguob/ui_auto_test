# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/22 13:50
@Author :李国彬
============================
"""
from common.base_page import BasePage


class ClassCommitteeDetailInfoPage(BasePage):
    """班委详情信息编辑页面"""

    def edit_info(self, values:dict):
        keys = values.keys()
        if '名称' in keys:
            self.locator_text_input(ctrl_id='name', value=values['名称'])
        self.locator_button('保存')

