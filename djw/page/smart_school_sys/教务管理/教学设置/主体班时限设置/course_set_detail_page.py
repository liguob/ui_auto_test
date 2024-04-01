# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/6 11:10
# Author     ：李国彬
============================
"""
import time

import allure

from common.base_page import BasePage


class CourseSetDetailPage(BasePage):
    """课程列表页面"""

    @allure.step('设置课程为可评')
    def set_course_can_evaluate(self):
        self.locator_button(button_title='设为可评')
        self.wait_success_tip()
        return self

    @allure.step('设置课程为不可评')
    def set_course_can_not_evaluate(self):
        self.locator_button(button_title='设为不可评')
        self.wait_success_tip()
        return self

    @allure.step('修改时限设置')
    def set_course_limit(self, name):
        self.locator_view_button(button_title='时限设置', id_value=name)
        time.sleep(2)  # 等待数据加载
        self.locator_button(button_title='保存')
        return self.wait_success_tip()

    @allure.step('查询课程')
    def search_course(self, name):
        self.locator_search_input(placeholder='课程名称/教学形式/授课人', value=name)
        self.locator_tag_search_button()
        return self
