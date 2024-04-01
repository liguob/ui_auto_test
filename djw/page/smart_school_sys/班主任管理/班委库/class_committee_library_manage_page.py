# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/22 13:50
@Author :李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class ClassCommitteeLibraryPage(HomePage):
    """班委库管理页面"""

    @allure.step('查询班委')
    def search_committee(self, name):
        self.locator_search_input(placeholder='请输入班委名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('新增班委')
    def add_committee(self, data):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.班主任管理.班委库.class_committee_detail_info_page import ClassCommitteeDetailInfoPage
        ClassCommitteeDetailInfoPage(driver=self.driver).edit_info(data)
        self.wait_success_tip()
        self.close_current_browser()
        self.switch_to_handle(-1)
        return self

    @allure.step('修改班委')
    def edit_committee(self, name, data):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        from djw.page.smart_school_sys.班主任管理.班委库.class_committee_detail_info_page import ClassCommitteeDetailInfoPage
        ClassCommitteeDetailInfoPage(driver=self.driver).edit_info(data)
        self.wait_success_tip()
        self.close_current_browser()
        self.switch_to_handle(-1)
        return self

    @allure.step('删除班委')
    def del_committee(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self
