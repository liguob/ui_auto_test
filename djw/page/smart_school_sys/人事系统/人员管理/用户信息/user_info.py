# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/27    14:51
============================
"""
import time

import allure

from common.base_page import BasePage
from common.file_path import wait_file_down_and_clean


class UserInfoPage(BasePage):
    """用户信息详情页面"""

    @allure.step("填写用户个人详情")
    def edit_info(self, values: dict):
        keys = values.keys()
        if "姓名" in keys:
            self.locator_text_input(ctrl_id='name', value=values["姓名"])
        # if "登录名" in keys:
        #     self.locator_text_input(ctrl_id='loginname', value=values["登录名"])
        if "人员编号" in keys:
            self.locator_text_input(ctrl_id='serial', value=values["人员编号"])
        if "身份证号" in keys:
            self.locator_text_input(ctrl_id='id_card', value=values["身份证号"])
        if "手机号码" in keys:
            self.locator_text_input(ctrl_id='phone', value=values["手机号码"])
        if "显示顺序" in keys:
            self.locator_text_input(ctrl_id='ds_order', value=values["显示顺序"])
        if '人员编制' in keys:
            self.locator_select_list_value(ctrl_id='staffing', value=values['人员编制'])
        if "人员类别" in keys:
            self.locator_select_radio(ctrl_id='person_type', value=values["人员类别"])
        if "职务级别" in keys:
            self.locator_select_list_value(ctrl_id='job_level', value=values["职务级别"])
        if "职级" in keys:
            self.locator_select_list_value(ctrl_id='rank', value=values["职级"])
        if "岗位类别" in keys:
            self.locator_select_list_value(ctrl_id='post_type', value=values["岗位类别"])
        if "岗位层级" in keys:
            self.locator_select_list_value(ctrl_id='post_rank', value=values["岗位层级"])
        time.sleep(1)
        self.locator_button(button_title='保存')
        return self

    @allure.step('关闭用户信息界面，返回主页')
    def back_user_manage(self):
        self.close_current_browser()
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.人事系统.人员管理.用户信息.user_manage import UserManagePage
        return UserManagePage(self.driver)

    @allure.step("进入新增信息界面")
    def go_add_page(self):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待已有用户信息加载
        return self

    @allure.step('进入编辑信息页面')
    def go_edit_page(self, value):
        self.locator_view_button(button_title='编辑', id_value=value)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待已有用户信息加载
        return self

    @allure.step('删除信息')
    def del_info(self, value):
        self.locator_view_button(button_title='删除', id_value=value)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step("导出信息")
    def download_info(self, file_name):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name=file_name)

    @allure.step("查询信息")
    def search_info(self, placeholder, value):
        self.locator_tag_search_input(placeholder=placeholder, value=value)
        self.locator_tag_search_button()
        return self
