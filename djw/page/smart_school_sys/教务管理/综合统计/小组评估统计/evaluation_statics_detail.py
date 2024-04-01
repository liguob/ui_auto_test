# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *


class EvaluationStaticsDetail(BasePage):

    @allure.step('导出评估统计信息')
    def download_file(self):
        self.locator_dialog_btn(btn_name='导出')
        return wait_file_down_and_clean(file_name='小组评估详情.xlsx')

    @allure.step('获取小组评估详情列头信息')
    def get_evaluation_headers(self):
        headers_loc = (By.CSS_SELECTOR, '[class="is-group has-gutter"] th>div')
        headers = [i.get_attribute('textContent').strip() for i in self.find_elms(headers_loc)]
        return headers

    @allure.step('获取小组评估详情课程详情信息')
    def get_evaluation_values(self):
        values_loc = (By.CSS_SELECTOR, '[class*="is-scrolling"] tr td div.cell')
        values = [i.get_attribute('textContent').strip() for i in self.find_elms(values_loc)]
        return values

    @allure.step('查询课程')
    def search_course(self, name):
        self.locator_search_input(placeholder='课程名称，授课教师', enter=True, value=name)
        return self

    @allure.step('查看已评人员')
    def view_evaluation_user(self):
        value_locator = (By.CSS_SELECTOR, '.is-scrolling-none tr td:nth-child(6)')
        value_ele = self.find_elem(value_locator)
        value_ele.click()
