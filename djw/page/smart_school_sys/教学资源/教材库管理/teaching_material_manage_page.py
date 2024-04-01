# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/21 14:13
# Author     ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage
from common.file_path import wait_file_down_and_clean


class TeachingMaterialPage(EduSourcePage):
    """教材库管理页面"""

    @allure.step('查询教材')
    def search_material(self, name):
        self.locator_search_input(placeholder='教材名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('导出教材')
    def download_material(self, file_name):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name)

    @allure.step('新增教材')
    def add_material(self, values: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.__edit_info(values)
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('删除教材')
    def del_material(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step('编辑教材')
    def edit_material(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.__edit_info(values)
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self

    def __edit_info(self, values: dict):
        keys = values.keys()
        if '教材名称' in keys:
            self.locator_text_input(ctrl_id='name', value=values['教材名称'])
        if '出版机构' in keys:
            self.locator_text_input(ctrl_id='press', value=values['出版机构'])
        if '主编名称' in keys:
            self.locator_text_input(ctrl_id='chief_editor', value=values['主编名称'])
        if '供书渠道' in keys:
            self.locator_text_input(ctrl_id='channel', value=values['供书渠道'])
        if '备注' in keys:
            self.locator_select_list_value(ctrl_id='note', value=values['备注'])
        if '出版年份' in keys:
            self.locator_date(ctrl_id='publish_year', value=values['出版年份'])
        if '期初数' in keys:
            self.locator_text_input(ctrl_id='periodical_first', value=values['期初数'])
        if '期末数' in keys:
            self.locator_text_input(ctrl_id='periodical_end', value=values['期末数'])
        if '价格' in keys:
            self.locator_text_input(ctrl_id='price', value=values['价格'])
        if '折扣' in keys:
            self.locator_text_input(ctrl_id='discount', value=values['折扣'])
        if '简介' in keys:
            self.locator_text_input(ctrl_id='description', value=values['简介'], tag_type='textarea')
        self.locator_button('保存')
