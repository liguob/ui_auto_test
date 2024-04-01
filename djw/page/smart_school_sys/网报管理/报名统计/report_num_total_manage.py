# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/22 16:08
# Author     ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.网报管理.管理端.network_report_manage_main_page import NetworkReportManagePage
from common.file_path import wait_file_down_and_clean


class ReportNumTotalManage(NetworkReportManagePage):
    """报名统计页面"""

    @allure.step('选择学年')
    def select_year(self, year):
        self.locator_tree_node_click(node_value=year, times=2)
        return self

    @allure.step('查询网报单位')
    def search_unit(self, name):
        self.locator_search_input(placeholder='单位名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('导出单位报名统计信息')
    def download_unit_info(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('统计信息.xlsx')

    @allure.step('进入单位报名统计详情')
    def into_unit_info(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        return self

    @allure.step('导出班次的报名统计信息')
    def download_class_info(self):
        self.locator_button(button_title='导出', dialog_title='班次列表')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('单位网报班次列表.xlsx')

    def into_class_info(self, name,user_type):
        with allure.step(f'进入班次{user_type}列表'):
            self.locator_search_input(placeholder='班次名称', dialog_title='班次列表', value=name)
            self.locator_tag_search_button(dialog_title='班次列表')
            self.locator_view_value_click(dialog_title='班次列表', header=user_type, id_value=name)
        return self

    def search_user(self, name, title_type):
        with allure.step(f'查询{title_type}'):
            self.locator_search_input(placeholder='姓名', dialog_title=title_type, value=name)
            self.locator_tag_search_button(dialog_title=title_type)
        return self
