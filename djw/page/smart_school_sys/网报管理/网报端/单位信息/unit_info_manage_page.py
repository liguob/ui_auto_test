# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 17:23
@Author :李国彬
============================
"""
from common.base_page import BasePage


class UnitInfoManagePage(BasePage):
    """单位信息页面"""

    def __edit_unit_info(self, values: dict):
        keys = values.keys()
        if '办公电话' in keys:
            self.locator_text_input(ctrl_id='office_phone', value=values['办公电话'])
        if '详细地址' in keys:
            self.locator_text_input(ctrl_id='address', value=values['详细地址'])
        self.locator_button(button_title='保存')

    def edit_unit_info(self, values:dict):
        self.__edit_unit_info(values)
        self.wait_success_tip()
        return self
