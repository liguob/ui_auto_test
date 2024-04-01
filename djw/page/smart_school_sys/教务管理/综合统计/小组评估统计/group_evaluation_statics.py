# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class GroupEvaluationStatics(EduManagePage):

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入班次评估详情页面')
    def go_evaluation_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.综合统计.小组评估统计.evaluation_statics_detail import EvaluationStaticsDetail
        return EvaluationStaticsDetail(self.driver)
