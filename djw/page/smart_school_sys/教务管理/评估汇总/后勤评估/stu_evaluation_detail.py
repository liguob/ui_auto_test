# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/11 15:07
@Author :李国彬
============================
"""
import allure

from common.base_page import BasePage


class StuEvaluationDetail(BasePage):
    """学员评价详情列表"""

    @allure.step('查询学员')
    def search_stu(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name)
        self.locator_tag_search_button()
        return self
