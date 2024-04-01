# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/1 14:16
@Author :李国彬
============================
"""
from common.tools_packages import *

from common.base_page import BasePage


class AttendanceSetPage(BasePage):
    """设置考勤页面"""
    def set_attendance_status(self, name):
        """设置是否考勤"""
        switch_click = (By.XPATH, f'//*[contains(text(),"{name}")]//ancestor::tr//*[@role="switch"]')
        self.element_click(switch_click)
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('查询课程')
    def search_course(self, name):
        self.locator_tag_search_input(placeholder='课程名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('获取考勤状态')
    def get_status(self, name):
        status_loc = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//*[@role="switch"]//span[contains(@class, "is-active")]')
        return self.find_elem(status_loc).get_attribute('textContent')
