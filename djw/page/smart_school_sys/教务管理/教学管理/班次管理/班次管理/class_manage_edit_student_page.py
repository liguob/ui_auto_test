# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/3/26    10:20
============================
用于新增学员或者编辑学员信息
"""
import time

import allure

from time import sleep

from common.base_page import BasePage


class ClassManageEditStudentPage(BasePage):
    """学员基本信息编辑页面"""

    @allure.step("填写学员信息")
    def __edit_student_info(self, values: dict):
        keys = values.keys()
        if '照片' in keys:
            self.locator_text_input(ctrl_id='zp', value=values["照片"], is_file=True)
            time.sleep(2)
            self.locator_dialog_btn('确 定')
            time.sleep(1)
        if "姓名" in keys:
            self.locator_text_input(ctrl_id='xm', value=values["姓名"])
        if "手机号码" in keys:
            self.locator_text_input(ctrl_id='sjhm', value=values["手机号码"])
        if "身份证号" in keys:
            self.locator_text_input(ctrl_id='sfzh', value=values["身份证号"])
            sleep(1)  # 等待填写身份证号后自动刷新性别和出生年月
        if "民族" in keys:
            self.locator_select_list_value(ctrl_id='mz', value=values["民族"])
        if "性别" in keys:
            self.locator_select_list_value(ctrl_id='xb', value=values["性别"])
        time.sleep(2)
        self.locator_button('保存')

    def edit_student_info(self, values):
        """填写学员信息成功"""
        self.__edit_student_info(values)
        return self

    def edit_student_fail(self, values):
        """填写学员信息失败"""
        self.__edit_student_info(values)
        return self.get_all_required_prompt()
