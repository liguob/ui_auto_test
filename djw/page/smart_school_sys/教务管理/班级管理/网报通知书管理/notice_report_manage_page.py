# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/23 16:01
@Author :李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class NoticeReportManagePage(EduManagePage):
    """网报通知书管理页面"""

    @allure.step('查询班次')
    def search_class(self, name=''):
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('单个班次上传通知书模板')
    def upload_model(self, name, file):
        self.locator_view_button(button_title='上传报到通知书模板', file=file, id_value=name)
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('批量班次上传通知书模板')
    def upload_more_model(self, file):
        self.locator_tag_button(button_title='上传报到通知书模板', file_path=file)
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('删除通知书模板')
    def del_model(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.wait_success_tip()
        return self
