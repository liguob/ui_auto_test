# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class InstitutionManage(PersonnelSysPage):
    """单位管理"""

    @allure.step('查询并选择机构')
    def select_dept(self, name):
        self.locator_search_input(placeholder='请输入查询关键字', value=name, times=2)
        self.locator_tree_node_click(node_value=name)
        return self

    def _edit_info(self, data: dict, dialog_title: str):
        time.sleep(3)
        if '机构名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['机构名称'], dialog_title=dialog_title)
        if '简称' in data:
            self.locator_text_input(ctrl_id='alias', value=data['简称'], dialog_title=dialog_title)
        if '机构编号' in data:
            self.locator_text_input(ctrl_id='code', value=data['机构编号'], dialog_title=dialog_title)
        if '排序码' in data:
            self.locator_text_input(ctrl_id='ds_order', value=data['排序码'], dialog_title=dialog_title)
        time.sleep(1)
        self.locator_button(button_title='保存', dialog_title=dialog_title)

    @allure.step('新增机构')
    def add_dept(self, data):
        self.locator_button(button_title='新增机构')
        self._edit_info(data=data, dialog_title='新增机构')
        self.wait_success_tip()
        return self

    @allure.step('编辑机构')
    def edit_dept(self, name, data):
        self.locator_view_button(button_title='编辑', id_value=name)
        self._edit_info(data=data, dialog_title='编辑')
        self.wait_success_tip()
        return self

    @allure.step('删除机构')
    def del_dept(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(1)
        return self

    @allure.step('查询机构列表')
    def search_dept(self, value):
        self.locator_search_input(placeholder='请输入名称', value=value, times=2, enter=True)
        return self

    @allure.step('模板下载')
    def download_template(self):
        self.locator_more_tip_button(button_title='模板下载')
        return wait_file_down_and_clean('机构部门导入模板.xls')

    @allure.step('机构导出文件')
    def download_dept_file(self):
        self.locator_more_tip_button(button_title='导出')
        return wait_file_down_and_clean('机构导出.xlsx')

    @allure.step('导入部门文件')
    def import_dept(self, file):
        self.locator_button(button_title='导入')
        self.upload_input_file_no_click((By.CSS_SELECTOR, 'input[type="file"]'), file)
        self.wait_success_tip()
        time.sleep(1)
        return self

    @allure.step('批量删除机构')
    def del_more_dept(self):
        self.locator_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(1)
        return self
