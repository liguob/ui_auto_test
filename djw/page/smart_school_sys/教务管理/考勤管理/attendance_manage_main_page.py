# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/1 11:05
@Author :李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class AttendanceManagePage(HomePage):

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入考勤详情')
    def go_attendance_detail(self, name):
        self.locator_view_button(button_title='考勤详情', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.考勤管理.attendance_detail_page import AttendanceDetailPage
        return AttendanceDetailPage(self.driver)

    @allure.step('进入设置考勤')
    def go_attendance_set(self, name):
        self.locator_view_button(button_title='设置考勤', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.考勤管理.attendance_set_page import AttendanceSetPage
        return AttendanceSetPage(driver=self.driver, table_ctrl_type="dsf.teassetting")

    @allure.step('修改班次考勤方式')
    def edit_class_attendance_set(self, name):
        self.locator_view_button(button_title='考勤方式', id_value=name)
        time.sleep(3)
        self.locator_button(button_title='保存')
        return self.wait_success_tip()