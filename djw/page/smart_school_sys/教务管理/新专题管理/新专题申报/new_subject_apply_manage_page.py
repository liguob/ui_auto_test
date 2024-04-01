# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/22 11:21
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class NewSubjectApplyPage(EduManagePage):
    """新专题申报"""

    @allure.step('查询专题')
    def search_subject(self, name):
        self.locator_search_input(placeholder='专题名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('删除专题申请')
    def del_subject(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        time.sleep(1)
        return self

    @allure.step('新增新专题申请信息')
    def add_new_subject(self, data: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        time.sleep(1)  # 等待获取默认信息字段
        from djw.page.smart_school_sys.教务管理.新专题管理.新专题申报.new_subject_apply_detail_page import NewSubjectDetailPage
        return NewSubjectDetailPage(driver=self.driver).edit_info(data)

    @allure.step('修改新专题申请信息')
    def edit_new_subject(self, name, data: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.新专题管理.新专题申报.new_subject_apply_detail_page import NewSubjectDetailPage
        return NewSubjectDetailPage(driver=self.driver).edit_info(data)

    @allure.step('专题详情查看')
    def view_detail(self, name):
        data = {}
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(3)
        process_num = (By.CSS_SELECTOR, '[ctrl-id="wfprocess"] .item')  # 处理流程的元素个数
        data['流程数量'] = len(self.find_elms(process_num))
        name_ele = (By.CSS_SELECTOR, '[ctrl-id="name"] [title]')
        data['专题名称'] = self.find_elem(name_ele).text
        return data
