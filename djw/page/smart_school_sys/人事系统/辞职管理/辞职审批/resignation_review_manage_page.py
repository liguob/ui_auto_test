# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/9 13:34
# Author     ：李国彬
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class ResignationReviewPage(PersonnelSysPage):
    """辞职审核主页"""

    @allure.step("查询辞职审核")
    def search_resignation(self, name):
        self.locator_tag_search_input(placeholder='部门/姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('辞职审核通过')
    def review_pass(self, name, reason):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        # 填写处理意见
        self.locator_dialog_btn(btn_name='填写处理意见')
        reason_input = (By.CSS_SELECTOR, '[aria-label="处理意见"] textarea')
        self.find_elem(reason_input).send_keys(reason)
        time.sleep(1)
        self.locator_dialog_btn(btn_name='确 定')
        time.sleep(1)
        # 点击同意
        self.locator_button(button_title='同意')
        self.locator_dialog_btn('确定')
        time.sleep(2)
        self.switch_to_window(-1)
        return self

    @allure.step('辞职审核不通过')
    def review_no_pass(self, name, reason):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        # 填写处理意见
        self.locator_dialog_btn(btn_name='填写处理意见')
        reason_input = (By.CSS_SELECTOR, '[aria-label="处理意见"] textarea')
        self.find_elem(reason_input).send_keys(reason)
        time.sleep(1)
        self.locator_dialog_btn(btn_name='确 定')
        # 点击不同意
        self.locator_button(button_title='不同意')
        self.locator_dialog_btn('确定')
        time.sleep(2)
        self.switch_to_window(-1)
        return self

    @allure.step('查看详情页面，获取审核意见')
    def get_check_reason(self, name):
        reason = (By.CSS_SELECTOR, '[ctrl-id="suggest"] .content')
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        return self.find_elem(reason).text
