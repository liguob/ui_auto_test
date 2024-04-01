# encoding=utf-8
"""
============================
Author:罗程
Time:2021/5/17  18:25
============================
"""
from time import sleep

import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.教学资源.师资库管理.teacher_data_management_page import TeacherDataManagePage


class FindTeacherDatePage(TeacherDataManagePage):
    """师资库查询"""

    @allure.step('查询教师')
    def search_teacher(self, name):
        self.locator_tag_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('选中师资来源进行筛选')
    def select_teacher_type(self, type_name):
        self.locator_tree_node_click(node_value=type_name)
        return self

    @allure.step('点击详情查看')
    def see_detail(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('点击教师名称查看详情')
    def see_teacher_detail(self, name):
        self.locator_view_value_click(header='姓名', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('获取师资详情信息的姓名')
    def get_detail_name(self):
        name_locator = (By.CSS_SELECTOR, '[ctrl-id="name"] [title]')
        return self.find_elem(name_locator).text
