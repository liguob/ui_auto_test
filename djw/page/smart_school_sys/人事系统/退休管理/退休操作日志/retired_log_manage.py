# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/20 14:58
# Author     ：李国彬
============================
"""
import allure
from common.file_path import wait_file_down_and_clean

from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class RetiredLogManagePage(PersonnelSysPage):
    """退休操作日志页面"""

    @allure.step('查询人员操作日志')
    def search_user(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('导出退休操作日志')
    def download_retired_log(self, file_name):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name)
