# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/11/30 14:01
# Author     ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class OtherCertificateMainPage(EduManagePage):
    """其他证书管理主页"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入班次证书管理详情页面')
    def go_certificate_manage_page(self, name):
        self.locator_view_button(button_title='管理', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.证书管理.其他证书.other_certificate_info_page import OtherCertificateInfoPage
        return OtherCertificateInfoPage(driver=self.driver)
