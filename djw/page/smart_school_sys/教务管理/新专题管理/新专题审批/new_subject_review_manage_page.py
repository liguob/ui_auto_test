# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/24 14:23
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class NewSubjectReviewPage(EduManagePage):
    """新专题审批页面"""

    @allure.step('查询专题')
    def search_subject(self, name):
        self.locator_tag_search_input(placeholder='专题名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('教研部审批-退回新专题申请')
    def jyb_reject_subject(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='退回')
        self.locator_search_input(placeholder='请输入退回原因', times=1, value='退回')
        self.locator_dialog_btn('确定')
        time.sleep(1)
        self.switch_to_window(-1)
        return self

    @allure.step('教研部审批-同意新专题申请')
    def jyb_agree_subject(self, name, leader_name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='同意')
        time.sleep(1)
        # 判断是否有选择办理人弹窗信息
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            # 校领导是校领导审核的登录角色名称
            self.locator_search_input(placeholder='输入名称', value=leader_name, enter=True)
            self.locator_tree_node_click(node_value=leader_name)
            self.locator_dialog_btn('确定')
            time.sleep(1)
        self.locator_dialog_btn('确定')
        time.sleep(1)
        self.switch_to_window(-1)
        return self

    @allure.step('校领导审批-退回新专题申请')
    def xld_reject_subject(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='退回')
        self.locator_search_input(placeholder='请输入退回原因', times=1, value='退回')
        self.locator_dialog_btn('确定')
        time.sleep(1)
        self.switch_to_window(-1)
        return self

    @allure.step('校领导审批-同意新专题申请')
    def xld_agree_subject(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='同意并结束')
        self.locator_dialog_btn('确定')
        time.sleep(1)
        self.switch_to_window(-1)
        return self
