# -*- coding: UTF-8 -*-
"""
Created on 2021年04月16日
@author: liudongjie
"""

from common.tools_packages import *
from common.base_page import BasePage


class ResourcesMaterialPage(BasePage):
    resource_dialog = '教学资料详情'

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('单个班次上传文件')
    def upload_file(self, name, file):
        self.locator_view_button(button_title='上传', id_value=name, file=file)
        self.wait_success_tip()
        return self

    @allure.step('批量班次上传文件')
    def upload_more_class_file(self, file):
        self.locator_tag_button(button_title='上传', file_path=file)
        self.wait_success_tip()
        return self

    @allure.step('进入班次资料详情')
    def go_resource_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        time.sleep(2)
        return self

    @allure.step('删除单个资料')
    def del_resource(self, name):
        self.locator_view_button(dialog_title=self.resource_dialog, button_title='删除', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('批量删除资料')
    def del_more_resource(self):
        self.locator_view_select_all(dialog_title=self.resource_dialog)
        self.locator_tag_button(dialog_title=self.resource_dialog, button_title='批量删除')
        return self

    @allure.step('关闭资料详情弹窗')
    def close_detail(self):
        close_button = (By.CSS_SELECTOR, '[role=dialog] [aria-label=Close]')
        self.excute_js_click(close_button)
        time.sleep(1)
        return self

    @allure.step('班次资料查询')
    def search_resource(self, value=''):
        self.locator_tag_search_input(placeholder='附件名称/上传时间/上传人', dialog_title=self.resource_dialog, value=value)
        self.locator_tag_search_button(dialog_title=self.resource_dialog)
        return self

    @allure.step('下载资料附件')
    def download_resource(self, name: str):
        self.locator_view_button(dialog_title=self.resource_dialog, button_title='下载资料', id_value=name.split('.')[0])
        return wait_file_down_and_clean(file_name=name)

    @allure.step('批量下载资料')
    def download_all_resource(self):
        self.locator_view_select_all(dialog_title=self.resource_dialog)
        self.locator_button(dialog_title=self.resource_dialog, button_title='批量下载')
        return wait_file_down_and_clean(file_name='教学资料.zip')
