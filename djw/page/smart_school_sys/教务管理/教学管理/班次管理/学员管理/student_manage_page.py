# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/21    15:50
============================
学员管理页面，设置学员状态等功能
"""

from common.tools_packages import *


class StudentManagePage(BasePage):

    @allure.step("导入学员")
    def import_student(self, file):
        """学员管理中导入学员"""
        self.locator_tag_button(button_title='预导入')
        self.locator_dialog_btn(btn_name='导入数据', dialog_title='提示')
        input_loc = (By.CSS_SELECTOR, 'input[type="file"]')
        self.find_elem(input_loc).send_keys(file)
        time.sleep(3)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step('生成学号')
    def generate_number(self):
        self.locator_tag_button(button_title='生成学号')
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('查询学员')
    def search_stu(self, name=''):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step("修改学员")
    def edit_stu(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        # 等待接口数据返回
        sleep(3)
        # 进入编辑页面
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_student_page import ClassManageEditStudentPage
        ClassManageEditStudentPage(self.driver).edit_student_info(values)
        # 等待窗口关闭学员信息页面
        self.wait_browser_close_switch_latest(times=10)
        return self

    @allure.step("新增学员")
    def add_stu(self, values: dict):
        """新增学员并关闭界面"""
        self.locator_tag_button(button_title='新增')
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_student_page import ClassManageEditStudentPage
        ClassManageEditStudentPage(self.driver).edit_student_info(values)
        # 等待新增学员窗口关闭
        self.wait_browser_close_switch_latest()
        return self

    @allure.step("删除学员")
    def del_selected_stu(self):
        self.locator_tag_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
