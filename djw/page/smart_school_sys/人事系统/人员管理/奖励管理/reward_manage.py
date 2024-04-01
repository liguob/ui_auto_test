# -*- coding: utf-8 -*-
"""
===============================
@Time     ：2021/9/3 13:48
@Author   ：李国彬
===============================
"""
import time

import allure

from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage
from common.file_path import wait_file_down_and_clean


class RewardManagePage(PersonnelSysPage):
    """奖励管理主页面"""

    @allure.step("新增奖励信息")
    def add_reward(self, values: dict, user_name=''):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.人员管理.奖励管理.reward_info import RewardManageInfo
        RewardManageInfo(self.driver).edit_info(name=user_name, values=values)
        return self

    @allure.step("修改奖励信息")
    def edit_reward(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待数据加载
        from djw.page.smart_school_sys.人事系统.人员管理.奖励管理.reward_info import RewardManageInfo
        RewardManageInfo(self.driver).edit_info(values=values)
        return self

    @allure.step("删除单个奖励信息")
    def del_reward(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(dialog_title='提示', btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step("批量删除奖励信息")
    def del_more_reward(self):
        self.locator_button(button_title='删除')
        self.locator_dialog_btn(dialog_title='提示', btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step("查询奖励信息")
    def search_reward(self, value, placeholder: str = '部门/姓名'):
        self.locator_tag_search_input(placeholder=placeholder, value=value)
        self.locator_tag_search_button()
        return self

    @allure.step("模板导出")
    def download_model(self):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_dialog_btn(btn_name='奖励信息导入模板.xls')
        return wait_file_down_and_clean(file_name='奖励信息导入模板.xls')

    @allure.step("奖励信息导出")
    def download_info(self):
        self.locator_more_tip_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='奖励信息.xlsx')

    @allure.step('导入奖励信息')
    def import_file(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step('导入奖励信息校验')
    def import_data_check(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn('确定')
        time.sleep(2)
        return self.get_all_required_prompt()
