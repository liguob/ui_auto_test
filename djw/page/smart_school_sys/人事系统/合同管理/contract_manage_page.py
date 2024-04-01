# -*- coding: UTF-8 -*-
"""
Created on 2021年09月03日 

@author: liudongjie
"""
from common.tools_packages import *

from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class ContractManagePage(PersonnelSysPage):
    """合同管理页面类"""

    @allure.step('查询合同')
    def search_contract(self, name=''):
        self.locator_tag_search_input(placeholder='部门/姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('新增合同')
    def add_contract(self, values: dict):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.合同管理.contract_info import ContractInfoPage
        ContractInfoPage(self.driver).edit_info(values)
        self.wait_success_tip()
        time.sleep(2)
        self.switch_to_window(-1)
        return self

    @allure.step('新增合同必填校验')
    def add_contract_check(self, values: dict = None):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.合同管理.contract_info import ContractInfoPage
        ContractInfoPage(self.driver).edit_info(values)
        return self.get_required_prompt()

    @allure.step('编辑合同')
    def edit_contract(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value('employ_post')
        from djw.page.smart_school_sys.人事系统.合同管理.contract_info import ContractInfoPage
        ContractInfoPage(self.driver).edit_info(values)
        self.wait_success_tip()
        time.sleep(2)
        self.switch_to_window(-1)
        return self

    @allure.step('续签合同')
    def renew_contract(self, name, start_time, end_time, file):
        self.locator_view_button(button_title='续签', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.合同管理.contract_info import ContractInfoPage
        values = {"合同有效开始时间": start_time, "合同有效结束时间": end_time, '附件': file}
        ContractInfoPage(self.driver).edit_info(values)
        self.wait_success_tip()
        self.close_current_browser()
        self.switch_to_window(-1)
        return self

    @allure.step('删除合同')
    def del_contract(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('合同模板下载')
    def download_model(self):
        self.locator_tag_button(button_title='预导入')
        self.locator_dialog_btn('合同导入模版.xlsx')
        return wait_file_down_and_clean('合同导入模版.xlsx')

    @allure.step('合同导入')
    def import_contract(self, file):
        self.locator_tag_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step('合同导入校验')
    def import_contract_check(self, file):
        self.locator_tag_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.wait_fail_tip()
        return self.get_all_required_prompt()
