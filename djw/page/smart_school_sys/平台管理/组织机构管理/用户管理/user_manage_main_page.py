# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 13:37
@Author :李国彬
============================
"""

from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class UserManageMainPage(HomePage):
    """用户管理主页"""

    @allure.step('查询用户')
    def search_user(self, name=''):
        self.locator_search_input(placeholder='请输入姓名或手机号', value=name, enter=True, times=2)
        return self

    @allure.step('进入用户信息编辑页面')
    def into_user_edit_page(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        return self

    @allure.step('用户设置角色信息')
    def user_set_role(self, roles: list, dept_name: str = None):
        self.locator_switch_tag(tag_name='角色信息')
        self.locator_tag_button(button_title='选择', times=1)
        for i in roles:
            self.locator_search_input(placeholder='输入关键字进行过滤', value=i, times=2, enter=True)
            self.locator_tree_node_click(node_value=i)
        self.locator_dialog_btn('确定')
        # if dept_name:  # 如果部门不为空则选择部门
        #     for i in roles:
        #         search_loc = (By.XPATH, f'//*[text()="{i}"]/ancestor::tr//i[contains(@class,"el-icon-search")]')
        #         self.excute_js_click(search_loc)
        #         self.locator_view_select(dialog_title='部门列表', id_value=dept_name)
        #         self.locator_dialog_btn(dialog_title='部门列表', btn_name='确定')
        #         time.sleep(2)
        time.sleep(2)
        return self

    @allure.step('保存用户信息')
    def save_user(self):
        self.locator_button(button_title='保存')
        info = self.wait_success_tip()
        time.sleep(3)  # 等待数据刷新
        return info
