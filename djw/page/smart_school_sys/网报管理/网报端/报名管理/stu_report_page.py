# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/15 17:32
@Author :李国彬
============================
"""
import allure

from common.base_page import BasePage


class StuReportPage(BasePage):
    """报名页面"""

    @allure.step('查询学员')
    def search_stu(self, name='', dialog_title=''):
        self.locator_tag_search_input(placeholder='姓名', value=name, dialog_title=dialog_title)
        self.locator_tag_search_button(dialog_title=dialog_title)
        return self

    @allure.step('删除学员')
    def del_stu(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定', dialog_title='提示')
        self.wait_success_tip()
        return self

    @allure.step('提交单个学员')
    def submit_stu(self, name):
        self.locator_view_button(button_title='提交', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('提交所有学员')
    def submit_all_stu(self):
        self.locator_view_select_all()
        self.locator_tag_button(button_title='提交')
        self.wait_success_tip()
        return self
