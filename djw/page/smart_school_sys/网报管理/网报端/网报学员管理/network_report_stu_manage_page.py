# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 17:27
@Author :李国彬
============================
"""
import time

import allure

from common.base_page import BasePage


class NetworkReportApplyStuManagePage(BasePage):
    """网报学员管理主页"""

    def edit_stu_info(self, values: dict):
        keys = values.keys()
        if '姓名' in keys:
            self.locator_text_input(ctrl_id='name', value=values['姓名'])
        if '身份证号' in keys:
            self.locator_text_input(ctrl_id='idcard', value=values['身份证号'])
        if '手机号码' in keys:
            self.locator_text_input(ctrl_id='phone', value=values['手机号码'])
        time.sleep(1)
        self.locator_button(button_title='保存')

    @allure.step('查询网报学员')
    def search_apply_stu(self, name=''):
        self.locator_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step("新增网报学员")
    def add_apply_stu(self, values: dict):
        self.locator_button(button_title='新增')
        self.edit_stu_info(values)
        self.wait_success_tip()
        return self

    @allure.step("编辑网报学员")
    def edit_apply_stu(self, name, values:dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.edit_stu_info(values)
        self.wait_success_tip()
        return self

    @allure.step("删除网报学员")
    def del_apply_stu(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导入网报学员')
    def import_apply_stu(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        time.sleep(3)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('删除批量网报学员')
    def del_more_apply_stu(self):
        self.locator_view_select_all()
        self.locator_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(2)
        return self



