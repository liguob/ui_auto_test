# -*- coding: UTF-8 -*-
"""
Created on 2021年07月27日 

@author: liudongjie
"""

from common.tools_packages import *

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class CertificateTemplatePage(EduManagePage):

    @allure.step('批量删除')
    def delete_button_click(self):
        self.locator_tag_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('查询证书模板')
    def search_certificate(self, value):
        self.locator_tag_search_input(placeholder='模板名称', value=value)
        self.locator_tag_search_button()
        return self

    def __edit_info(self, data: dict):
        if '模板名称' in data:
            self.clear_and_input(loc=(By.XPATH, '//*[text()="模板名称"]/..//input'), value=data['模板名称'])
            # self.find_elem((By.XPATH, '//*[text()="模板名称"]/..//input')).send_keys(value=data['模板名称'])
        if '适用证书' in data:
            value = data['适用证书']
            self.element_click((By.XPATH, '//*[@class="el-select"]//input'))
            time.sleep(0.5)
            self.element_click((By.XPATH, f'//*[@x-placement]//*[text()="{value}"]'))
        if '背景图片' in data:
            self.locator_click_wait_input_file(btn_name='点击上传背景图片', file=data['背景图片'])
        self.locator_dialog_btn(btn_name='保存')
        return self

    @allure.step('新增证书模板')
    def add_certificate_template(self, data: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.__edit_info(data)
        self.wait_success_tip()
        self.close_and_return_page()
        # self.wait_browser_close_switch_latest()
        return self

    @allure.step('编辑证书模板')
    def edit_certificate_template(self, name):
        """
        编辑证书模板
        :return:
        """
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.get_input_already_exists_text((By.XPATH, '//*[text()="模板名称"]/..//input'))
        self.locator_dialog_btn(btn_name='保存')
        self.wait_success_tip()
        self.close_and_return_page()
        # self.wait_browser_close_switch_latest()
        return name

    @allure.step('删除证书模板')
    def del_certificate_template(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('禁用启动证书模板')
    def change_certificate_template_status(self, name):
        info = self.locator_view_conditions()
        click_switch = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//span[@class="el-switch__core"]')
        if info['启用状态'] == '启用':
            self.element_click(click_switch)
            # self.locator_view_button(button_title='禁用', id_value=name)
        elif info['启用状态'] == '禁用':
            self.element_click(click_switch)
            # self.locator_view_button(button_title='启用', id_value=name)
        return info['启用状态']
