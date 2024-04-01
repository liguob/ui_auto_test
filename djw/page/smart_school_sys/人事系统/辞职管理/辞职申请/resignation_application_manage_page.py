# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/9 9:41
# Author     ：李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class ResignationApplicationPage(PersonnelSysPage):
    """辞职申请页面"""

    @allure.step('查询辞职类型')
    def search_resignation(self, name):
        self.locator_search_input(placeholder='辞职类型', value=name)
        self.locator_tag_search_button()
        return self

    def _edit_info(self, values: dict):
        keys = values.keys()
        if '辞职类型' in keys:
            self.locator_select_list_value(ctrl_id='type', value=values['辞职类型'])
        if '个人辞职申请报告' in keys:
            self.locator_text_input(ctrl_id='annex', value=values['个人辞职申请报告'], is_file=True)
        if '联系方式' in keys:
            self.locator_text_input(ctrl_id='phone', value=values['联系方式'])
        time.sleep(2)  # 等待数据上传加载
        self.locator_button(button_title='提交')
        # 判断是否有选择办理人弹窗信息
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            self.locator_search_input(placeholder='输入名称', value=values['请选择办理人'])
            time.sleep(1)
            select_name = (By.XPATH, f"""//*[text()="{values['请选择办理人']}"]""")  # 事系统管理员是人事审核的登录角色名称
            self.excute_js_click(select_name)
            self.locator_dialog_btn('确定')
        self.wait_browser_close_switch_latest()  # 页面自动消失

    @allure.step('新增辞职申请')
    def add_resignation(self, values: dict):
        self.locator_button(button_title='辞职申请')
        self.wait_open_new_browser_and_switch()
        self._edit_info(values)
        return self
