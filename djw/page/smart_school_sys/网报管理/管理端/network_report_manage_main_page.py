# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 16:44
@Author :李国彬
============================
"""
import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class NetworkReportManagePage(HomePage):
    """网报管理管理端主页"""

    @allure.step('进入单位管理')
    def go_unit_manage_page(self):
        self.locator_left_menu_click(button_title='单位管理',times=3)
        from djw.page.smart_school_sys.网报管理.管理端.单位管理.unit_management_page import UnitManagementPage
        return UnitManagementPage(self.driver)

    @allure.step('进入单位管理员')
    def go_unit_admin_manage_page(self):
        self.locator_left_menu_click(button_title='单位管理员')
        from djw.page.smart_school_sys.网报管理.管理端.单位管理员.unit_administrators_page import UnitAdministratorsPage
        return UnitAdministratorsPage(self.driver)

    @allure.step('进入审核管理')
    def go_review_manage_page(self):
        self.locator_left_menu_click(button_title='审核管理')
        from djw.page.smart_school_sys.网报管理.管理端.审核管理.review_manage_page import ReviewManagePage
        return ReviewManagePage(self.driver)

    @allure.step('进入网报通知管理')
    def go_notice_manage_page(self):
        self.locator_left_menu_click(button_title='网报通知管理')
        from djw.page.smart_school_sys.网报管理.管理端.网报通知管理.notice_manage_page import NoticeManagePage
        return NoticeManagePage(self.driver)

    @allure.step('进入报名统计')
    def go_report_total_page(self):
        self.locator_left_menu_click(button_title='报名统计')
        from djw.page.smart_school_sys.网报管理.报名统计.report_num_total_manage import ReportNumTotalManage
        return ReportNumTotalManage(self.driver)
