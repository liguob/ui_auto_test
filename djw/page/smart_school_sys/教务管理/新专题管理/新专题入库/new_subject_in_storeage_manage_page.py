# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/24 15:50
@Author :李国彬
============================
"""
import allure

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class NewSubjectInStoragePage(EduManagePage):
    """新专题入库页面"""

    @allure.step("新专题入库")
    def subject_in_storage(self, name):
        self.locator_view_button(button_title='入库', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('查询专题')
    def search_subject(self, name):
        self.locator_tag_search_input(placeholder='专题名称', value=name)
        self.locator_tag_search_button()
        return self

