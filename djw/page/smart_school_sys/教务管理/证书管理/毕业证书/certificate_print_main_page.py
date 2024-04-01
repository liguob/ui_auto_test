# -*- coding: UTF-8 -*-
"""
Created on 2021年04月22日 

@author: liudongjie
"""
import time

import allure

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class CertificatePrintingMainPage(EduManagePage):
    """毕业证书主页"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入班次证书管理详情页面')
    def go_print_manage_page(self, name):
        self.locator_view_button(button_title='管理', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        from djw.page.smart_school_sys.教务管理.证书管理.毕业证书.certificate_print_info_page import CertificatePrintInfoPage
        return CertificatePrintInfoPage(self.driver)
