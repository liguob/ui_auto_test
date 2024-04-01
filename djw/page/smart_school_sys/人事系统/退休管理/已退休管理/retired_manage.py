# -*- coding: utf-8 -*-
"""
===============================
@Time     ：2021/9/3 14:37
@Author   ：李国彬
===============================
"""
import time

import allure

from common.file_path import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class RetiredManagePage(PersonnelSysPage):
    """已退休管理主页面"""

    @allure.step('提前退休')
    def early_retire(self, values: dict):
        self.locator_button(button_title='提前退休')
        keys = values.keys()
        # 填写姓名
        self.locator_search_magnifier(ctrl_id='name')
        time.sleep(2)
        self.locator_search_input(dialog_title='部门人员选择', value=values['姓名'], placeholder='输入关键字进行过滤', enter=True)
        self.locator_tree_node_click(dialog_title='部门人员选择', node_value=values['姓名'])
        self.locator_dialog_btn(dialog_title='部门人员选择', btn_name='确定')
        if '备注' in keys:
            self.locator_text_input(ctrl_id='remark', value=values['备注'], tag_type='textarea')
        if '附件' in keys:
            self.locator_text_input(ctrl_id='attachment', value=values['附件'], is_file=True)
        time.sleep(2)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('查询退休人员')
    def search_user(self, name):
        self.locator_search_input(placeholder='请输入部门/姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('导出退休人员')
    def download_retire_user(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='确定')
        return wait_file_down_and_clean('已退休人员表.xlsx')
