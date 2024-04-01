# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/27    13:58
============================
"""
import time
import allure
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class UserManagePage(PersonnelSysPage):
    """用户信息主页面"""

    @allure.step("新增用户信息")
    def create_user(self, values: dict, dept_name=''):
        if dept_name:
            self.select_dept(dept_name)
        self.locator_button(button_title='新增用户')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.人员管理.用户信息.user_info import UserInfoPage
        time.sleep(2)
        UserInfoPage(self.driver).edit_info(values)
        time.sleep(3)
        self.close_and_return_page()
        return self

    @allure.step("选中部门")
    def select_dept(self, value):
        self.locator_search_input(placeholder='请输入查询关键字', value=value, enter=True, times=2)
        self.locator_tree_node_click(node_value=value, times=2)
        return self

    @allure.step("进入编辑用户信息界面")
    def go_edit_user(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.人员管理.用户信息.user_info import UserInfoPage
        return UserInfoPage(self.driver)

    @allure.step("查询用户")
    def search_user(self, value=''):
        self.locator_search_input(placeholder='姓名', value=value)
        self.locator_tag_search_button(times=5)
        return self

    @allure.step('人员变动')
    def change_dept(self, name, values: dict):
        """修改人员部门"""
        self.locator_view_button(button_title='人员变动', id_value=name)
        dialog_title = '请选择'
        self.locator_search_magnifier(ctrl_id='new_dept')
        self.locator_search_input(dialog_title=dialog_title, placeholder='输入关键字进行过滤', value=values['新部门'],
                                  times=2, enter=True)
        self.locator_tree_node_click(dialog_title=dialog_title, node_value=values['新部门'])
        self.locator_dialog_btn(dialog_title=dialog_title, btn_name='确定')
        self.locator_text_input(ctrl_id='cause', tag_type='textarea', value=values['变更原因'])
        self.locator_button(button_title='保存')
        self.locator_dialog_btn(dialog_title='提示', btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step("进入人员变动记录")
    def go_change_info(self):
        self.locator_more_tip_button(button_title='人员变动记录')
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('删除人员')
    def del_user(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导入人员')
    def import_user(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        time.sleep(2)  # 等待导入数据加载
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip(times=5)
        return self

    @allure.step('导入人员校验')
    def import_user_check(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.wait_fail_tip()
        return self.get_all_required_prompt()
