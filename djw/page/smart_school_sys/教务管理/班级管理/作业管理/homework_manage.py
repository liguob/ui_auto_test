# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class HomeWorkManage(EduManagePage):
    """作业管理页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name, times=2, enter=True)
        return self

    @allure.step('进入班次作业管理详情页面')
    def go_class_homework_detail_manage(self, name):
        self.locator_view_button(button_title='管理', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.班级管理.作业管理.homework_detail_manage import HomeworkDetailManage
        return HomeworkDetailManage(self.driver)