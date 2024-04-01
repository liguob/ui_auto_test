# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class DeptManage(PersonnelSysPage):
    """部门管理"""

    @allure.step('查询并选择部门')
    def select_dept(self, name=''):
        self.locator_search_input(placeholder='请输入查询关键字', value=name, times=2, enter=True)
        self.locator_tree_node_click(node_value=name)
        return self

    def _edit_info(self, data: dict):
        if '部门名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['部门名称'])
        if '简称' in data:
            self.locator_text_input(ctrl_id='alias', value=data['简称'])
        if '部门层级' in data:
            self.locator_select_list_value(ctrl_id='level', value=data['部门层级'])
        if '部门编号' in data:
            self.locator_text_input(ctrl_id='code', value=data['部门编号'])
        if '排序码' in data:
            self.locator_text_input(ctrl_id='ds_order', value=data['排序码'])
        self.locator_button(button_title='保存')

    @allure.step('新增部门')
    def add_dept(self, data):
        self.locator_button(button_title='新增')
        self._edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('编辑部门')
    def edit_dept(self, name, data):
        self.locator_view_button(button_title='编辑', id_value=name)
        self._edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('删除部门')
    def del_dept(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('查询部门列表')
    def search_dept(self, value=''):
        self.locator_search_input(placeholder='请输入部门名称', value=value, times=2, enter=True)
        return self

    @allure.step('模板下载')
    def download_template(self):
        self.locator_more_tip_button(button_title='模板下载')
        return wait_file_down_and_clean('机构部门导入模板.xls')

    @allure.step('部门导出文件')
    def download_dept_file(self):
        self.locator_more_tip_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('部门导出.xlsx')

    @allure.step('批量删除部门')
    def del_more_dept(self):
        self.locator_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
