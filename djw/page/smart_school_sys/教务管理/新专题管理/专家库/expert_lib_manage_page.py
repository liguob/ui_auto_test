# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/27 10:25
# Author     ：李国彬
============================
"""
import allure
from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage
from common.file_path import wait_file_down_and_clean
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit


class ExpertLibManagePage(EduManagePage):
    """专家库管理页面"""

    @allure.step('查询专家')
    def search_expert(self, name):
        self.locator_search_input(placeholder='姓名', value=name, enter=True)
        self.locator_tag_search_button(times=2)
        return self

    @allure.step('导出专家库信息')
    def download_info(self, file_name):
        """
        :param file_name: 导出文件全名(含格式后缀)
        """
        self.locator_more_tip_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name)

    @allure.step('删除专家')
    def del_expert(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    def edit_status(self, name, status):
        with allure.step(f"专家状态置为{status}"):
            self.locator_view_button(button_title=status, id_value=name)
            self.wait_success_tip()
        return self

    @allure.step('新增专家信息')
    def add_expert(self, values: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.新专题管理.专家库.expert_detail_info_page import ExpertDetailInfoPage
        ExpertDetailInfoPage(self.driver).edit_info(values)
        return self

    @allure.step('修改专家信息')
    def edit_expert(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.新专题管理.专家库.expert_detail_info_page import ExpertDetailInfoPage
        ExpertDetailInfoPage(self.driver).edit_info(values)
        return self

    @property
    @allure.step('获取专家列表职务文本')
    def expert_duty(self):
        duty = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=expert_post__value]')
        duty_text = self.trim_text(duty)
        return duty_text

    @property
    @change_reset_implicit()
    @allure.step('获取专家列表检索结果表单条数')
    def table_count_searched(self):
        tr = (By.CSS_SELECTOR, '.ds-panel-body [class*=is-scrolling] tr')
        table_data = self.driver.find_elements(*tr)
        table_count = len(table_data)
        return table_count
