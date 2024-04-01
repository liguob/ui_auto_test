# -*- coding: UTF-8 -*-
"""
Created on 2021年04月16日 

@author: liudongjie
"""
import time

import allure

from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage
from common.file_path import wait_file_down_and_clean


class BaseSiteManagePage(EduSourcePage):
    """基地库管理主页"""

    @allure.step("新增基地")
    def add_base_site(self, values: dict):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教学资源.基地库管理.base_site_info_page import BaseSiteInfoPage
        BaseSiteInfoPage(self.driver).edit_info(values)
        return self

    @allure.step('修改基地')
    def edit_base_site(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待数据加载
        from djw.page.smart_school_sys.教学资源.基地库管理.base_site_info_page import BaseSiteInfoPage
        BaseSiteInfoPage(self.driver).edit_info(values)
        return self

    @allure.step('查询基地')
    def search_base_site(self, name):
        self.locator_tag_search_input(placeholder='基地名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('基地必填校验')
    def add_base_site_check(self):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教学资源.基地库管理.base_site_info_page import BaseSiteInfoPage
        return BaseSiteInfoPage(self.driver).edit_check_info()

    @allure.step('基地信息导出')
    def download_base_site(self, file_name):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name=file_name)

    @allure.step('删除场地')
    def del_base_site(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
