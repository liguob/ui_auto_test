# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/9/27 17:31
@Author :李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class StuCheckManage(HomePage):
    """班次学员审核详情界面"""

    @allure.step('审核通过')
    def check_pass(self, name):
        self.locator_view_button(button_title='通过', id_value=name)
        self.wait_success_tip()
        time.sleep(3)  # 等待界面自动刷新
        return self

    @allure.step('审核不通过')
    def check_no_pass(self, name, reason):
        self.locator_view_button(button_title='不通过', id_value=name)
        self.locator_text_input(ctrl_id='reason', tag_type='textarea', value=reason)
        self.locator_button(button_title='提交')
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        time.sleep(3)  # 等待界面自动刷新
        return self

    @allure.step('审核退回')
    def check_rollback(self, name, reason):
        self.locator_view_button(button_title='退回', id_value=name)
        self.locator_text_input(ctrl_id='backreason', tag_type='textarea', value=reason)
        self.locator_button(button_title='提交')
        self.wait_success_tip()
        time.sleep(3)  # 等待界面自动刷新
        return self

    @allure.step('查询学员')
    def search_stu(self, name):
        self.locator_tag_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button()
        return self
