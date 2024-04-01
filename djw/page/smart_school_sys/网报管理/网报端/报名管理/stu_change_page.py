# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/15 17:32
@Author :李国彬
============================
"""
import allure

from common.base_page import BasePage


class StuChangePage(BasePage):
    """人员变更页面"""

    @allure.step('学员变更')
    def change_check_stu(self, name, change_name):
        self.locator_view_button(button_title='学员变更', id_value=name)
        self.__change_stu(change_name=change_name)
        return self

    @allure.step('查询学员')
    def search_stu(self, name, title=''):
        self.locator_tag_search_input(placeholder='姓名', dialog_title=title, value=name)
        self.locator_tag_search_button(dialog_title=title)
        return self

    @allure.step('申请变更')
    def change_apply_stu(self, name, change_name):
        self.locator_view_button(button_title='申请变更', id_value=name)
        self.__change_stu(change_name=change_name)
        return self

    def __change_stu(self, change_name):
        """学员变更选择人员操作"""
        title = '变更学员选择'
        self.locator_button(button_title='选择')
        self.search_stu(title=title, name=change_name)
        self.locator_view_select(dialog_title=title, id_value=change_name)
        self.locator_dialog_btn(dialog_title=title, btn_name='确定')
        self.locator_text_input(ctrl_id='reason', tag_type='textarea', value='学员变更')
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('删除审核中的学员')
    def del_check_stu(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self


