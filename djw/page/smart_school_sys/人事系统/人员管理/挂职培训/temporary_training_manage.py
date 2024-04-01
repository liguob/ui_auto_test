# -*- coding: utf-8 -*-
"""
===============================
@Time     ：2021/9/3 13:46
@Author   ：李国彬
===============================
"""
import time

import allure

from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class TemporaryTrainingManagePage(PersonnelSysPage):
    """挂职培训主页面"""

    @allure.step("新增挂职培训信息")
    def add_training(self, values: dict):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.人员管理.挂职培训.temporary_training_info import TemporaryTrainingInfoPage
        TemporaryTrainingInfoPage(self.driver).edit_info(values=values)
        return self

    @allure.step("修改挂职培训信息")
    def edit_training(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待数据加载
        from djw.page.smart_school_sys.人事系统.人员管理.挂职培训.temporary_training_info import TemporaryTrainingInfoPage
        TemporaryTrainingInfoPage(self.driver).edit_info(values=values)
        return self

    @allure.step("删除挂职培训信息")
    def del_training(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(dialog_title='提示', btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step("批量删除挂职培训信息")
    def del_more_training(self):
        self.locator_button(button_title='删除')
        self.locator_dialog_btn(dialog_title='提示', btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step("查询挂职培训信息")
    def search_training(self, value, placeholder: str = '标题'):
        self.locator_tag_search_input(placeholder=placeholder, value=value)
        self.locator_tag_search_button(times=3)
        return self
