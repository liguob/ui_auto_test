# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/3/25    14:03
============================
对班次管理_学员管理中的学员信息功能：新增，导入，删除，修改等
"""

import allure

from djw.page.smart_school_sys.教务管理.教学管理.班次管理.学员管理.student_manage_page import StudentManagePage


class ClassMangeStudentPage(StudentManagePage):
    """班次管理-学员管理信息页面"""

    @allure.step('切换到班次管理')
    def switch_class_manage(self):
        self.locator_switch_tag(tag_name='班次管理')
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_class_page import ClassManageEditClassPage
        return ClassManageEditClassPage(self.driver)
