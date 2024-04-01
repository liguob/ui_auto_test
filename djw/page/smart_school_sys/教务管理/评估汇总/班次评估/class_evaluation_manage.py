# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/13 15:25
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.主页.home_page import HomePage


class ClassEvaluationManage(HomePage):
    """班次评估页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入评价详情获取班次信息')
    def goto_class_evaluate_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        time.sleep(1)
        return self.get_class_name()

    def get_class_name(self):
        """获取班次名称"""
        name_locator = (By.CSS_SELECTOR, '[ctrl-id=class_name] [title]')
        return self.find_elem(name_locator).text

    @allure.step('点击人数字段进入学员详情')
    def goto_stu_detail(self, header, value):
        self.locator_view_value_click(header=header, id_value=value)
        return self

    @allure.step('学员详情查询学员')
    def search_stu(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name)
        self.locator_tag_search_button(dialog_title='dialog')
        return self
