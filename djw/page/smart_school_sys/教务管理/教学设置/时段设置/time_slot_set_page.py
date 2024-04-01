# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/6 14:08
# Author     ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class TimeSlotSetPage(EduManagePage):
    """时段设置页面"""

    @allure.step('查询时段')
    def search_time_slot(self, name):
        self.locator_search_input(placeholder='请输入午别', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('修改时段设置')
    def edit_time_slot(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='schedule_time_category')
        self.locator_button(button_title='保存')
        tip = self.wait_success_tip()
        self.close_and_return_page()
        return tip
