# -*- coding: UTF-8 -*-
"""
Created on 2021年07月09日 

@author: liudongjie
"""
import time

import allure
from common.base_page import BasePage
from common.random_tool import randomTool


class UnitAdministratorsPage(BasePage):

    @allure.step('点击单位名称')
    def click_unit(self, name):
        self.locator_search_input(placeholder='查询（多个关键词空格隔开）', value=name)
        self.locator_tree_node_click(node_value=name)
        return self

    @allure.step('点击新增')
    def add_administrators_button_click(self):
        self.locator_tag_button(button_title='新增')
        return self

    @allure.step('编辑单位管理员')
    def edit_admin(self, name1, name2):
        self.locator_view_button(button_title='编辑', id_value=name1)
        time.sleep(2)
        self.locator_text_input(ctrl_id='name', value=name2)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('删除单位管理员')
    def del_admin(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('批量删除单位管理员')
    def del_more_admin(self):
        self.locator_tag_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('填写新增单元信息')
    def add_administrators(self):
        """
        新增一个单位-只填写必填
        num为生成的登录名位数
        """
        name = randomTool.random_name()
        self.locator_text_input(ctrl_id='loginname', value=randomTool.random_range_str(6, 6))
        self.locator_text_input(ctrl_id='name', value=name)
        self.locator_text_input(ctrl_id='phone', value=randomTool.random_phone())
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return name

    @allure.step('选中单位')
    def selected_unit(self, unit_name):
        self.locator_search_input(placeholder='查询（多个关键词空格隔开）', value=unit_name)
        self.locator_tree_node_click(node_value=unit_name, times=2)
        return self

    @allure.step('查询单位管理员')
    def search_admin(self, value=' '):
        self.locator_search_input(placeholder='单位名称/姓名', value=value)
        # self.locator_search_input(placeholder='请输入检索关键字', value=value)
        self.locator_tag_search_button(times=2)
        return self

    @allure.step('导入单位管理员')
    def import_admin(self, path):
        self.locator_more_tip_button(button_title='预导入', file_path=path)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('异常导入单位管理员')
    def import_admin_error(self, path):
        self.locator_more_tip_button(button_title='预导入', file_path=path)
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('重置密码')
    def reset_pwd(self, name):
        self.locator_view_button(button_title='重置密码', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        return self.wait_success_tip()

