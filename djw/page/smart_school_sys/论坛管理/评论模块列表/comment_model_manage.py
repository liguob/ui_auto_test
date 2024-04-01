# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2022/1/20 12:35
# Author     ：李国彬
============================
"""
import allure
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class CommentModelManage(BasePage):
    _frame = (By.CSS_SELECTOR, 'iframe[src]')

    def _edit_info(self, data: dict):
        keys = data.keys()
        if '模块名称' in keys:
            self.locator_text_input(ctrl_id='name', value=data['模块名称'])
        if '模块编号' in keys:
            self.locator_text_input(ctrl_id='code', value=data['模块编号'])
        if '是否启用' in keys:
            self.locator_select_radio(ctrl_id='is_use', value=data['是否启用'])
        if '是否开启审核' in keys:
            self.locator_select_radio(ctrl_id='is_audit', value=data['是否开启审核'])
        self.locator_button(button_title='保存')

    @allure.step('修改评论模块信息')
    def edit_comment_model(self, name, data):
        self.switch_to_frame(self._frame)
        self.locator_view_button(button_title='编辑', id_value=name)
        self._edit_info(data)
        self.switch_to_frame_back()
        return self.wait_success_tip()

    @allure.step('查询评论模块')
    def search_comment_model(self, name):
        self.switch_to_frame(self._frame)
        self.locator_search_input(placeholder='请输入模块编号', value=name)
        self.locator_tag_search_button()
        num = self.locator_view_num()
        self.switch_to_frame_back()
        return num

    @allure.step('新增评论模块列表')
    def add_comment_model(self,data):
        self.switch_to_frame(self._frame)
        self.locator_button(button_title='新增')
        self._edit_info(data)
        self.switch_to_frame_back()
        self.wait_success_tip()
        return self
