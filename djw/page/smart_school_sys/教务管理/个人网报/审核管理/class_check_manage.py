# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/9/27 17:23
@Author :李国彬
============================
"""
import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class ClassCheckManage(HomePage):
    """个人网报-审核管理"""

    @allure.step('进入班次学员审核页面')
    def go_check_page(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.个人网报.审核管理.stu_check_manage import StuCheckManage
        return StuCheckManage(self.driver)

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班级名称', value=name)
        self.locator_tag_search_button()
        return self
