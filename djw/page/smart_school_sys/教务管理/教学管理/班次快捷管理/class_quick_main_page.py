# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/9 15:49
# Author     ：李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class ClassQuickManagePage(EduManagePage):
    """班次快捷管理页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        input_ele = (By.CSS_SELECTOR, f'{self.CSS_TAGS}input[placeholder]')
        self.clear_and_input_enter(input_ele, name)
        time.sleep(2)
        return self

    @allure.step('保存班次信息')
    def save_class_info(self, name):
        class_btn = (By.XPATH, f'{self.XPATH_TAGS}//*[@title="{name}"]')
        self.excute_js_click(class_btn)
        time.sleep(3)
        self.locator_button(dialog_title=name, button_title='保存')
        return self.wait_success_tip()

    def switch_function_page(self, class_name, btn_name, is_more=False):
        """进入功能页面"""
        with allure.step(f'进入{btn_name}'):
            if is_more:  # 是否属于更多下的按钮
                more_btn = (By.XPATH, f'{self.XPATH_TAGS}//*[@title="{class_name}"]/ancestor::div[@dividerline]'
                                      f'//*[contains(text(),"更多")]')
                self.excute_js_click(more_btn)
                click_btn = (By.XPATH, f'//*[@aria-label="更多"]//*[contains(text(),"{btn_name}")]')
            else:
                click_btn = (By.XPATH, f'{self.XPATH_TAGS}//*[@title="{class_name}"]/ancestor::div[@dividerline]'
                                       f'//*[contains(text(),"{btn_name}")]')
        self.excute_js_click(click_btn)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待信息加载
        return self

    def get_class_name(self, name):
        # 获取调课管理/排课页面/教学计划的班次名称
        name_ele = (By.XPATH, f'//*[contains(text(),"{name}")]')
        return str(self.find_elem(name_ele).text).strip()
