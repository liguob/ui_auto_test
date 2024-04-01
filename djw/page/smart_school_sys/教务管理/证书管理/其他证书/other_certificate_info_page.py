# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/11/30 14:02
# Author     ：李国彬
============================
"""
from common.tools_packages import *

from common.base_page import BasePage


class OtherCertificateInfoPage(BasePage):
    """班次其他证书管理详情页面"""

    def __edit_info(self, values: dict):
        keys = values.keys()
        if '证书名称' in keys:
            self.locator_text_input(ctrl_id='name', value=values['证书名称'])
        if '证书编号生成' in keys:
            self.locator_select_radio(ctrl_id='generation_rule', value=values['证书编号生成'])
        if '自定义编号' in keys:
            self.locator_text_input(ctrl_id='custom_number', value=values['自定义编号'])
        if '证书模板' in keys:
            self.locator_select_list_value(ctrl_id='certificate_template', value=values['证书模板'])
        if '证书发放时间' in keys:
            self.locator_date(ctrl_id='release_time', value=values['证书发放时间'])
        if '获证学员' in keys:
            self.locator_search_magnifier(ctrl_id='students')
            self.locator_search_input(dialog_title='请选择', placeholder='姓名', value=values['获证学员'])
            self.locator_tag_search_button(dialog_title='请选择')
            self.locator_view_select(dialog_title='请选择', id_value=values['获证学员'])
            self.locator_dialog_btn('确定')
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        time.sleep(2)

    @allure.step('查询证书')
    def search_certificate(self, name):
        self.locator_search_input(placeholder='证书名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('新增证书')
    def add_certificate(self, values: dict):
        self.locator_button(button_title='新增证书')
        self.__edit_info(values)
        return self

    @allure.step('发放证书')
    def provide_certificate(self):
        self.locator_button(button_title='发放证书')
        self.wait_success_tip()
        return self

    @allure.step('撤销证书')
    def revoke_certificate(self):
        self.locator_button(button_title='撤销证书')
        self.wait_success_tip()
        return self

    @allure.step('编辑证书')
    def edit_certificate(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.locator_get_js_input_value(ctrl_id='name')
        self.__edit_info(values)
        return self

    @allure.step('预览证书')
    def view_certificate(self, name):
        img_ele = (By.CSS_SELECTOR, 'img[src]')
        self.locator_view_button(button_title='预览', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self.find_elem(img_ele).get_attribute('src')

    def download_certificate(self, stu_name, class_name, file_type: str):
        with allure.step(f'下载{file_type}证书'):
            self.locator_view_select(id_value=stu_name)
            self.locator_view_button(button_title='下载', id_value=stu_name)
            time.sleep(2)
            self.locator_select_radio(ctrl_id='format', value=file_type)
            self.find_elem((By.XPATH, '//*[@aria-label="下载证书"]//span[contains(text(),"下载证书")]')).click()
        if file_type == 'word格式':
            return wait_file_down_and_clean(f'{class_name}.docx', times=30)
        else:
            return wait_file_down_and_clean(f'{class_name}.pdf', times=30)
