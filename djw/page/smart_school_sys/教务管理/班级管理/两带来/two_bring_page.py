# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/23 17:09
# Author     ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class TwoBringManagePage(EduManagePage):
    """教务管理-两带来页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step("进入已提交详情页面")
    def go_detail_info(self, class_name):
        self.locator_view_value_click(id_value=class_name, header='已提交')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.班级管理.两带来.two_bring_detail_page import TwoBringDetailPage
        return TwoBringDetailPage(self.driver)
