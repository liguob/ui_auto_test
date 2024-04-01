# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/23 17:14
# Author     ：李国彬
============================
"""
from common.tools_packages import *


class TwoBringDetailPage(BasePage):
    """已提交两带来详情信息页面"""

    @allure.step('汇总查询学员两带来')
    def search_user(self, name):
        self.locator_tag_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('两带来汇总导出')
    def download_total_info(self, class_name):
        self.locator_dialog_btn('导出')
        # self.locator_dialog_btn('确定')
        return wait_file_down_and_clean(class_name + '两带来汇总.xls')

    @allure.step('两带来问题类型导出')
    def download_type_info(self, class_name):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(f'{class_name}_两带来按问题类型汇总.xlsx', times=20)

    @allure.step('两带来附件下载')
    def download_attach_file(self, stu_name, file_name):
        self.locator_view_button(button_title='下载附件', id_value=stu_name)
        return wait_file_down_and_clean(file_name)

    @allure.step('两带来全部附件下载')
    def download_all_attach_file(self, class_name):
        self.locator_button(button_title='下载全部附件')
        return wait_file_down_and_clean(f'{class_name}_两带来相关附件.zip')

    @allure.step('两带来汇总退回')
    def two_bring_back(self, stu_name):
        btn = (By.XPATH, f'//*[text()="{stu_name}"]/ancestor::tr//*[text()="退回"]')
        self.excute_js_click(btn)
        time.sleep(3)
        self.locator_dialog_btn(dialog_title='确定退回至学员重新提交吗？', btn_name='提交')
        return self.wait_success_tip()
