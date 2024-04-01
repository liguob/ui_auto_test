# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/6 13:47
# Author     ：李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class ExternalClassTimeLimitSetPage(EduManagePage):
    """对外班时限设置主页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称或编号', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('修改时限设置')
    def set_time_limit(self, name):
        self.locator_view_button(button_title='时限设置', id_value=name)
        time.sleep(2)  # 等待数据加载
        self.locator_button(button_title='保存')
        return self.wait_success_tip()

    @allure.step('进入课程列表')
    def go_course_set_page(self, name):
        self.locator_view_button(button_title='课程列表', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.教学设置.对外班时限设置.external_class_course_set_detail_page import \
            ExternalClassCourseSetDetailPage
        return ExternalClassCourseSetDetailPage(self.driver)
