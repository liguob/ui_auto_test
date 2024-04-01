# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/23 16:50
# Author     ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.班主任管理.master_manage_page import MasterManagePage
from common.file_path import wait_file_down_and_clean


class TwoBringManagePage(MasterManagePage):
    """班主任管理-两带来页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    def into_user_info(self, class_name, title):
        """进入人数详情页面"""
        with allure.step(f"进入{title}页面信息"):
            self.locator_view_value_click(id_value=class_name, header=title)
        return self

    def search_user(self, dialog, name):
        """人数详情页面查询学员"""
        with allure.step(f"查询{dialog}"):
            self.locator_search_input(placeholder='姓名', dialog_title=dialog, value=name)
            self.locator_tag_search_button(dialog_title=dialog)
        return self

    @allure.step('导出两带来学员信息')
    def download_info(self, file_name):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name)
