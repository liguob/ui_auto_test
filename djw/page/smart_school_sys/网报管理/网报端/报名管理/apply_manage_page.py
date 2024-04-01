# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/15 16:35
@Author :李国彬
============================
"""
import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class ApplyManagePage(HomePage):
    """报名管理主页"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入人员变更页面')
    def go_stu_change_page(self, name):
        self.locator_view_button(button_title='人员变更', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.网报管理.网报端.报名管理.stu_change_page import StuChangePage
        return StuChangePage(self.driver)

    @allure.step('进入报名页面')
    def go_report_page(self, name):
        self.locator_view_button(button_title='报名', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.网报管理.网报端.报名管理.stu_report_page import StuReportPage
        return StuReportPage(self.driver)



