# -*- coding: utf-8 -*-
"""
===============================
@Time     ：2021/9/3 14:38
@Author   ：李国彬
===============================
"""
import time

import allure

from common.file_path import wait_file_down_and_clean
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class NotRetiredManagePage(PersonnelSysPage):
    """待退休管理主页面"""

    @allure.step('设置退休年龄')
    def set_retire_age(self, values: dict):
        self.locator_tag_button(button_title='待退休年龄设置')
        time.sleep(2)  # 等待已有数据加载
        keys = values.keys()
        if '男性退休年龄' in keys:
            self.locator_text_input(ctrl_id='male', value=values['男性退休年龄'])
        if '女性退休年龄' in keys:
            self.locator_text_input(ctrl_id='female', value=values['女性退休年龄'])
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('导出退休信息')
    def download_retire_info(self, file_name):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name)

    @allure.step('人员退休')
    def user_retire(self, name):
        self.locator_view_button(button_title='退休', id_value=name)
        dialog_title = '退休信息'
        time.sleep(2)
        self.locator_button(dialog_title=dialog_title, button_title='退休')
        self.wait_success_tip()
        return self

    @allure.step('人员延迟退休')
    def user_delay_retire(self, name, date):
        self.locator_view_button(button_title='延迟退休', id_value=name)
        dialog_title = 'dialog'
        self.locator_date(ctrl_id='delay_retire_date', value=date)
        time.sleep(2)  # 等待数据加载，避免失败
        self.locator_button(dialog_title=dialog_title, button_title='确定')
        self.wait_success_tip()
        return self

    @allure.step('查询人员')
    def search_user(self, value=''):
        self.locator_tag_search_input(placeholder='请输入部门/姓名', value=value)
        self.locator_tag_search_button()
        return self
