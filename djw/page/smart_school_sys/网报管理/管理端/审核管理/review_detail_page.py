# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 17:17
@Author :李国彬
============================
"""
import allure

from common.base_page import BasePage


class ReviewDetailPage(BasePage):
    """报名审核详情页面"""

    @allure.step('网报审核通过')
    def stu_review_pass(self, name):
        self.locator_view_button(button_title='通过', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('网报审核不通过')
    def stu_review_no_pass(self, name):
        self.locator_view_button(button_title='不通过', id_value=name)
        self.locator_text_input(ctrl_id='reason', tag_type='textarea', value='不通过')
        self.locator_button(button_title='提交')
        self.wait_success_tip()
        return self

    @allure.step('网报审核通过同步')
    def push_pass_stu(self):
        self.locator_view_select_all()
        self.locator_button(button_title='同步')
        self.wait_success_tip(times=10)
        return self

    @allure.step('查询学员')
    def search_stu(self, name):
        self.locator_tag_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('学员退回')
    def rollback_stu(self, name):
        self.locator_view_button(button_title='退回', id_value=name)
        self.locator_text_input(ctrl_id='reason', tag_type='textarea', value='退回意见')
        self.locator_button(button_title='提交')
        self.wait_success_tip()
        return self

    @allure.step('换人审核不通过')
    def review_change_stu_no_pass(self, name):
        self.locator_view_button(button_title='换人审核', id_value=name)
        self.locator_button(button_title='不同意')
        self.locator_text_input(ctrl_id='reason', tag_type='textarea', value='审核不通过')
        self.locator_button(button_title='提交')
        self.wait_success_tip()
        return self

    @allure.step('换人审核通过')
    def review_change_stu_pass(self, name):
        self.locator_view_button(button_title='换人审核', id_value=name)
        self.locator_button(button_title='同意')
        self.wait_success_tip()
        return self
