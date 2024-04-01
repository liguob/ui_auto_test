# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.平台管理.platform_manage_page import PlatformManagePage


class PersonApplyReportFormSet(PlatformManagePage):
    """个人网报自定义表单"""

    @allure.step('查询表单模板')
    def search_from(self, form_name):
        self.locator_search_input(placeholder='模板名称', value=form_name)
        self.locator_tag_search_button()
        return self

    @allure.step('新增个人网报表单模板')
    def add_form_set(self, form_name):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.input_send_keys(loc=(By.CSS_SELECTOR, "[placeholder='请输入模版名称']"), value=form_name)
        self.find_elem((By.CSS_SELECTOR, '.cell input[type="text"]'))  # 等待默认模板加载
        time.sleep(1)
        self.locator_dialog_btn('保存')
        self.wait_success_tip()
        self.close_and_return_page()
        return self

    @allure.step('设置表单模板为默认模板')
    def set_default_form(self, form_name):
        self.locator_view_button(button_title='设为默认', id_value=form_name)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self
