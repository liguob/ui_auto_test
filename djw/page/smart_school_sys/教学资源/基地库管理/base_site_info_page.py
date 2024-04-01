# -*- coding: UTF-8 -*-
"""
Created on 2021年04月16日 

@author: 李国彬
"""
import time

import allure

from common.base_page import BasePage


class BaseSiteInfoPage(BasePage):

    def __edit_info(self, values: dict):
        keys = values.keys()
        if '基地名称' in keys:
            self.locator_text_input(ctrl_id='name', value=values['基地名称'])
        if '基地来源' in keys:
            self.locator_text_input(ctrl_id='source', value=values['基地来源'])
        if '基地地址' in keys:
            self.locator_text_input(ctrl_id='address', value=values['基地地址'])
        if '教学主题' in keys:
            self.locator_text_input(ctrl_id='teach_theme', value=values['教学主题'])
        if '基地性质' in keys:
            self.locator_select_list_value(ctrl_id='nature', value=values['基地性质'])
        if '建立时间' in keys:
            self.locator_date(ctrl_id='build_date', value=values['建立时间'])
        if '基地类别' in keys:
            self.locator_text_input(ctrl_id='category', value=values['基地类别'])
        if '接待规模' in keys:
            self.locator_text_input(ctrl_id='scale', value=values['接待规模'])
        if '教学主持人' in keys:
            self.locator_text_input(ctrl_id='teach_host', value=values['教学主持人'])
        if '讲解员' in keys:
            self.locator_text_input(ctrl_id='announcer', value=values['讲解员'])
        if '联系人' in keys:
            self.locator_text_input(ctrl_id='contacts', value=values['联系人'])
        if '联系电话' in keys:
            self.locator_text_input(ctrl_id='phone', value=values['联系电话'])
        if '基地情况' in keys:
            self.locator_text_input(ctrl_id='situation', value=values['基地情况'], is_file=True)
        time.sleep(2)

    @allure.step('填写基地信息')
    def edit_info(self, values: dict = None):
        self.__edit_info(values)
        self.locator_button(button_title='保存')
        time.sleep(2)  # 等待界面自动关闭
        self.switch_to_window(-1)

    @allure.step('保存基地信息必填校验')
    def edit_check_info(self):
        self.__edit_info(values={})
        self.locator_button(button_title='保存')
        return self.get_required_prompt()

