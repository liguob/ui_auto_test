# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/27 13:44
# Author     ：李国彬
============================
"""
import allure
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class PrepareTrialLectureManagePage(EduManagePage):
    """集体备课试讲管理页面"""

    @allure.step('查询试讲')
    def search_lecture(self, name):
        self.locator_search_input(placeholder='标题', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入签到详情')
    def into_lecture_sign_info(self, name):
        self.locator_view_button(button_title='签到详情', id_value=name)
        return self

    @allure.step('进入评分详情')
    def info_lecture_score_info(self, name):
        self.locator_view_button(button_title='评分详情', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('新增集体备课试讲')
    def add_interview(self, values: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.edit_info(values)
        return self

    def __edit_info(self, values: dict):
        """填写集体备课试讲详情信息"""
        keys = values.keys()
        if '标题' in keys:
            pass
        if '试讲时间' in keys:
            pass
        if '试讲地点' in keys:
            pass
        if '评委' in keys:
            self.locator_search_magnifier(ctrl_id='judges')
            self.locator_tag_search_input(placeholder='姓名', value=values['评委'])
            self.locator_tag_search_button(times=1)
            self.locator_view_select(id_value=values['评委'])
            confirm = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')
            self.poll_click(confirm)
        self.locator_button(button_title='保存')

    def edit_info(self, values: dict):
        self.__edit_info(values)
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('新增页-搜索评委')
    def search_expert_by_add(self, name):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.locator_search_magnifier(ctrl_id='judges')
        self.locator_tag_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button(times=1)
        return self

    @property
    @change_reset_implicit()
    @allure.step('获取新增页评委检索结果表单条数')
    def expert_count(self):
        tr = (By.CSS_SELECTOR, '.ds-panel-body [class*=is-scrolling] tr')
        table_data = self.driver.find_elements(*tr)
        table_count = len(table_data)
        return table_count
