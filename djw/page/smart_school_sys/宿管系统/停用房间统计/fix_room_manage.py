# !/usr/bin/env python
# -*-coding:utf-8 -*-
import allure

from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem
from common.tools_packages import *


class FixRoomManage(RoomSystem):

    @allure.step('查询房间')
    def search_room(self, name):
        self.locator_search_input(placeholder='房间号', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('编辑房间')
    def edit_room(self, name, data: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        from djw.page.smart_school_sys.宿管系统.房间维护.room_manage_page import RoomManage
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='name')
        RoomManage(self.driver).edit_info(data)
        self.wait_success_tip()
        self.locator_dialog_btn('关闭')
        self.switch_to_handle(-1)
        return self
