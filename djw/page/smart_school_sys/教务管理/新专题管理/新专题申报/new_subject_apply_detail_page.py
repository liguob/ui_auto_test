# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/22 11:24
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class NewSubjectDetailPage(BasePage):
    """新专题信息编辑详情页面"""

    def edit_info(self, values: dict):
        keys = values.keys()
        if '专题名称' in keys:
            self.locator_text_input(ctrl_id='name', value=values['专题名称'])
        if '教学形式' in keys:
            self.locator_select_list_value(ctrl_id='teaching_form', value=values['教学形式'])
        if '使用范围' in keys:
            self.locator_select_radio(ctrl_id='range', value=values['使用范围'])
        if '主要内容' in keys:
            self.locator_text_input(ctrl_id='primary_coverage', value=values['主要内容'], tag_type='textarea')
        time.sleep(2)
        return self

    @allure.step('保存专题')
    def save_info(self):
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        time.sleep(3)  # 等待页面加载避免交互错误
        return self

    @allure.step('发送专题')
    def push_info(self, name=''):
        self.locator_button(button_title='发送')
        # 判断是否有选择办理人弹窗信息
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            self.locator_search_input(placeholder='输入名称', value=name, times=3)
            select_name = (By.XPATH, f'//*[text()="{name}"]')  # 教研领导是教研审核的登录角色名称
            self.excute_js_click(select_name)
            self.locator_dialog_btn('确定')
            self.wait_browser_close_switch_latest(times=5)
        else:
            self.driver.switch_to_window(self.driver.window_handles[-1])
        return self

    @allure.step('退回状态重新发送审核')
    def re_push_info(self, name):
        self.locator_button(button_title='发送')
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            self.locator_search_input(placeholder='输入名称', value=name, times=3)
            self.locator_tree_node_click(node_value=name)
            # select_name = (By.XPATH, f'//*[text()="{name}"]')  # 教研领导是教研审核的登录角色名称
            # self.excute_js_click(select_name)
            self.locator_dialog_btn('确定')
            self.wait_browser_close_switch_latest(times=5)
        else:
            self.switch_to_handle(-1)
        self.wait_browser_close_switch_latest()  # 页面自动消失
        return self
