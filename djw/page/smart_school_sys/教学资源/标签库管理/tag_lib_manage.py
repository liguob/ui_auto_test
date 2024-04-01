# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/21 15:32
# Author     ：李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage


class TagLibManage(EduSourcePage):
    """标签库管理页面类"""

    @allure.step("查询标签")
    def search_tag(self, name):
        self.locator_search_input(placeholder='名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('删除标签')
    def del_tag(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step('新增标签')
    def add_tag(self, name):
        self.locator_button(button_title='新增')
        self.locator_text_input(ctrl_id='name', value=name)
        self.locator_button('保存')
        self.wait_success_tip()
        self.locator_button('关闭')
        return self

    @allure.step('修改标签')
    def edit_tag(self, name, edit_name):
        self.locator_view_button(button_title='编辑', id_value=name)
        time.sleep(1)
        self.locator_text_input(ctrl_id='name', value=edit_name)
        self.locator_button('保存')
        self.wait_success_tip()
        self.locator_button('关闭')
        return self

    def edit_status(self, name, status):
        with allure.step(f"标签状态置为{status}"):
            self.locator_view_button(button_title=status, id_value=name)
            self.wait_success_tip()
        return self
