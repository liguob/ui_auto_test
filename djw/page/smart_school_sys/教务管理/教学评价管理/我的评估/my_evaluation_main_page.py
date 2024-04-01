# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/27 14:17
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.主页.home_page import HomePage
from common.file_path import wait_file_down_and_clean


class MyEvaluationMainPage(HomePage):
    """我的评估主页"""

    @allure.step("导出评价信息")
    def download_evaluation(self, file_name):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name=file_name)

    @allure.step('点击详情获取参评人数')
    def get_evaluation_user_number(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        time.sleep(2)  # 等待数据加载
        number_ele = (By.CSS_SELECTOR, '[ctrl-id="have_appraise_num"] [title]')
        return int(self.find_elem(number_ele).get_attribute('title'))

    @allure.step('查询课程')
    def search_course(self, name):
        self.locator_tag_search_input(placeholder='请输入课程名称', value=name)
        self.locator_tag_search_button()
        return self
