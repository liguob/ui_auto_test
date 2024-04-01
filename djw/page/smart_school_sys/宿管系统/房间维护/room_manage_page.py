# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem


class RoomManage(RoomSystem):

    def edit_info(self, data: dict):
        if '房间号' in data:
            self.locator_text_input(ctrl_id='name', value=data['房间号'])
        if '房间类型' in data:
            self.locator_select_list_value(ctrl_id='type', value=data['房间类型'])
        if '房间状态' in data:
            self.locator_select_radio(ctrl_id='status', value=data['房间状态'])
        if '参考价' in data:
            self.locator_text_input(ctrl_id='price', value=data['参考价'])
        if '床位数' in data:
            self.locator_text_input(ctrl_id='beds', value=data['床位数'])
        if '房间排序' in data:
            self.locator_text_input(ctrl_id='ds_order', value=data['房间排序'])
        self.locator_button(button_title='保存')

    def select_build(self, name):
        with allure.step(f'选中楼宇/楼层：{name}'):
            self.locator_tree_node_click(node_value=name)
        return self

    def search_room(self, name: str = ''):
        with allure.step(f'查询房间:{name}'):
            self.locator_tag_search_input(placeholder='房间名称', value=name)
            self.locator_tag_search_button()
        return self

    def add_room(self, data):
        with allure.step(f'新增房间{data["房间号"]}'):
            self.locator_button(button_title='新增房间')
            self.edit_info(data)
            self.wait_success_tip()
        return self

    def edit_room(self, name, data):
        with allure.step(f'编辑房间:{name}'):
            self.locator_view_button(button_title='编辑', id_value=name)
            self.locator_get_js_input_value(ctrl_id='name')
            self.edit_info(data)
        return self.wait_success_tip()

    def del_room(self, name):
        with allure.step(f'删除房间{name}'):
            self.locator_view_button(button_title='删除', id_value=name)
            self.locator_dialog_btn('确定')
            self.wait_success_tip()
        return self

    @allure.step('导入房间')
    def import_room(self, file):
        self.locator_tag_button(button_title='导入', file_path=file)
        self.wait_success_tip(times=10)
        return self

    @allure.step('删除选中的所有房间')
    def del_select_room(self):
        self.locator_button(button_title='删除')
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step('下载模板')
    def download_model(self):
        self.locator_button(button_title='模板下载')
        return wait_file_down_and_clean('房间维护导入模板.xlsx')
