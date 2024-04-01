# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/22 10:47
@Author :李国彬
============================
"""
import time

import allure
from djw.page.smart_school_sys.主页.home_page import HomePage


class ClassContactManagePage(HomePage):
    """通讯录主页"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入班级通讯录详情页面')
    def go_contact_info_page(self, name):
        self.locator_view_button(button_title='查看通讯录', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待数据加载
        from djw.page.smart_school_sys.班主任管理.班级通讯录.class_contact_info_page import ClassContactInfoPage
        return ClassContactInfoPage(self.driver)
