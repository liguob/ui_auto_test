# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/9/29 15:38
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.file_path import wait_file_down_and_clean


class CourseEvaluationDetail(BasePage):
    """课程评价详情界面"""

    @allure.step('查询课程')
    def search_course(self, name):
        self.locator_tag_search_input(placeholder='请输入课程名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('查看课程评估详情')
    def check_course_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        time.sleep(2)  # 等待课程数据加载
        name_ele = (By.CSS_SELECTOR, '[ctrl-id="course_name"] [title]')
        return self.find_elem(name_ele).text

    @allure.step('导出课程详情')
    def download_course_info(self, file_name):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name=file_name)

    def change_course_status(self, course_name, button_name):
        with allure.step(f'课程{button_name}'):
            self.locator_view_select(id_value=course_name)
            self.locator_button(button_title=button_name)
            self.wait_success_tip()
        return self
