# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/6 16:11
# Author     ：李国彬
============================
"""
import time

import allure

from common.base_page import BasePage


class OutTrainingClassInfoPage(BasePage):
    """对外班次详情编辑页面"""

    def __edit_info(self, values: dict):
        keys = values.keys()
        if '班次名称' in keys:
            self.locator_text_input(ctrl_id='name', value=values['班次名称'])
        if '学年' in keys:
            self.locator_text_input(ctrl_id='school_year', value=values['学年'], is_readonly=True)
        if '学期' in keys:
            self.locator_select_radio(ctrl_id='xq', value=values['学期'])
        if '班次类型' in keys:
            self.locator_select_list_value(ctrl_id='bclx', value=values['班次类型'], wait_time=0.5)
        if '培训开始时间' in keys:
            self.locator_date_range(ctrl_id='pxsj', start_date=values['培训开始时间'], end_date=values['培训结束时间'])
        if '负责部门' in keys:
            self.locator_select_list_value(ctrl_id='fzbm', value=values['负责部门'])
        if '计划人数' in keys:
            self.locator_text_input(ctrl_id='jhrs', value=values['计划人数'])
        if "班主任" in keys:
            self.__select_master(values["班主任"])
        time.sleep(2)
        self.locator_button(button_title='保存')

    @allure.step("选择班主任")
    def __select_master(self, name):
        """基础信息中查询，并选择班主任"""
        self.locator_search_magnifier(ctrl_id='bzr')
        self.locator_search_input(placeholder='输入关键字进行过滤', value=name, times=2, enter=True)
        self.locator_tree_node_click(node_value=name)
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('填写班次信息')
    def edit_info(self, values: dict):
        self.__edit_info(values)
        self.wait_browser_close_switch_latest()
        from djw.page.smart_school_sys.对外培训.班次管理.out_training_class_manage_page import \
            OutTrainingClassManagePage
        return OutTrainingClassManagePage(self.driver)

    @allure.step('切换到学员管理')
    def go_stu_manage(self):
        self.locator_switch_tag('学员管理')
        from djw.page.smart_school_sys.对外培训.班次管理.学员管理.out_traing_class_stu_manage_page import \
            OutTrainingClassStuManage
        return OutTrainingClassStuManage(self.driver)
