# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 13:34
@Author :李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class PlatformManagePage(HomePage):
    """平台管理"""

    @allure.step('进入用户管理')
    def go_user_manage_page(self):
        self.locator_left_menu_click(menu_title='组织机构管理', button_title='用户管理')
        from djw.page.smart_school_sys.平台管理.组织机构管理.用户管理.user_manage_main_page import UserManageMainPage
        return UserManageMainPage(self.driver)

    @allure.step('进入系统配置')
    def go_sys_conf_manage_page(self):
        self.locator_left_menu_click(button_title='系统配置')
        from djw.page.smart_school_sys.平台管理.系统配置.sys_conf_manage import SysConfManege
        time.sleep(3)
        return SysConfManege(self.driver)

    @allure.step('进入班级配置')
    def go_class_conf_manage_page(self):
        self.locator_left_menu_click(button_title='班级配置')
        from djw.page.smart_school_sys.平台管理.系统配置.sys_conf_manage import SysConfManege
        return SysConfManege(self.driver)

    @allure.step('进入个人网报自定义表单')
    def go_person_report_form_set_page(self):
        self.locator_left_menu_click(button_title='个人网报自定义表单',menu_title='业务功能配置')
        from djw.page.smart_school_sys.平台管理.业务功能配置.个人网报自定义表单.person_apply_report_form_set import \
            PersonApplyReportFormSet
        return PersonApplyReportFormSet(self.driver)
