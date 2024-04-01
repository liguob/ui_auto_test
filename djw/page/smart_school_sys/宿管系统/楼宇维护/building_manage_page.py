# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem


class BuildingManage(RoomSystem):

    def __edit_info(self, data: dict):
        if '名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['名称'])
        if '排序码' in data:
            self.locator_text_input(ctrl_id='ds_order', value=data['排序码'])
        self.locator_button(button_title='保存')

    def search_building(self, name):
        with allure.step(f'查询楼宇/楼层：{name}'):
            self.locator_tag_search_input(placeholder='名称', value=name)
            self.locator_tag_search_button()
        return self

    def add_building(self, data: dict):
        with allure.step(f'新增楼宇/楼层：{data["名称"]}'):
            self.locator_button(button_title='新增')
            self.__edit_info(data=data)
            self.wait_success_tip()
        return self

    def del_building(self, name):
        with allure.step(f'删除楼宇/楼层：{name}'):
            self.locator_view_button(button_title='删除', id_value=name)
            self.locator_dialog_btn('确定')
            self.wait_success_tip()
        return self

    def edit_building(self, name, data: dict):
        with allure.step(f'编辑楼宇/楼层：{name}'):
            self.locator_view_button(button_title='编辑', id_value=name)
            self.locator_get_js_input_value(ctrl_id='name')
            self.__edit_info(data)
        return self.wait_success_tip()

    def select_build(self, name):
        with allure.step(f'选中楼宇/楼层：{name}'):
            self.locator_tree_node_click(node_value=name)
        return self
