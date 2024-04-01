# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/3/17    17:00
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class ClassMangeMainPage(EduManagePage):

    def __click_confirm(self):
        """点击确定"""
        confirm_btn = (By.CSS_SELECTOR, 'div[role=dialog] button.el-button--primary')  # 确认按钮
        self.switch_to_frame_back()
        self.excute_js_click(confirm_btn)

    @allure.step("进入当前班次页签")
    def switch_current_class(self):
        """切换到当前班次"""
        self.locator_switch_tag("当前班次")
        return self

    @allure.step("进入未开始班次页签")
    def switch_feature_class(self):
        """切换到未开始班次"""
        self.locator_switch_tag("未开始班次")
        return self

    @allure.step("进入历史班次页签")
    def switch_history_class(self):
        """切换到历史班次"""
        self.locator_switch_tag("历史班次")
        return self

    @allure.step("进入计划班次")
    def switch_to_plan_class(self):
        """切换到计划班次"""
        self.locator_switch_tag("计划班次")
        return self

    @allure.step("新增班次")
    def add_class(self, class_value: dict):
        """进入班次新增页面"""
        self.locator_tag_button("新增")
        self.switch_to_window(1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_class_page import ClassManageEditClassPage
        ClassManageEditClassPage(self.driver).edit_class_info(class_value)
        return self

    @allure.step("班次信息校验")
    def add_class_fail(self, class_value: dict = None):
        """进入班次新增页面"""
        self.locator_tag_button("新增")
        self.switch_to_window(1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_class_page import ClassManageEditClassPage
        return ClassManageEditClassPage(self.driver).edit_class_info_fail(class_value)

    @allure.step("修改班次")
    def edit_class(self, name, values: dict):
        """进入班次修改页面"""
        # 班次名称对应的管理按钮
        self.search_class(name)
        self.locator_view_button(button_title="管理", id_value=name)
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_class_page import ClassManageEditClassPage
        ClassManageEditClassPage(self.driver).edit_class_info(values)
        return self

    @allure.step("编辑计划班次")
    def edit_plan_class(self, name, values: dict):
        """进入班次修改页面"""
        # 班次名称对应的管理按钮
        self.search_class(name)
        self.locator_view_button("编辑", name)
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_class_page import ClassManageEditClassPage
        ClassManageEditClassPage(self.driver).edit_class_info(values)
        return self

    @allure.step("进入学员管理页面")
    def go_student_manage(self, name):
        """点击对应班次的学员管理"""
        self.locator_view_button("学员管理", name)
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.学员管理.student_manage_page import StudentManagePage
        return StudentManagePage(self.driver)

    @allure.step('进入班次管理页面')
    def go_class_manage(self, name):
        self.locator_view_button(button_title='管理', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='name')
        time.sleep(1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_class_page import ClassManageEditClassPage
        return ClassManageEditClassPage(self.driver)

    @allure.step("查询班次")
    def search_class(self, value):
        """根据班次名称查询"""
        # 班次名称查询输入框
        self.locator_tag_search_input(placeholder='请输入班次名称', value=value)
        self.locator_tag_search_button()
        return self

    @allure.step("删除班次")
    def del_class(self, name, success=True):
        """根据班次名称删除对应班次"""
        # 班次名称对应的删除按钮
        self.locator_view_button("删除", name)
        self.__click_confirm()
        if success:
            return self.wait_success_tip()
        else:
            return self.wait_fail_tip()

    @allure.step("导入计划班次")
    def import_plan_cls(self, file):
        self.locator_tag_button(button_title='导入', file_path=file)
        self.wait_success_tip()
        return self

    @allure.step("导入计划班次校验")
    def import_plan_cls_check(self, file):
        self.locator_tag_button(button_title='导入', file_path=file)
        return self.wait_fail_tip()

    @allure.step("导入计划班次单位校验")
    def import_plan_unit_check(self, file):
        self.locator_tag_button(button_title='导入', file_path=file)
        tip_info = (By.CSS_SELECTOR, '[role=dialog] tbody tr')
        return self.find_elem_visibility(tip_info).get_attribute('textContent')

    @allure.step("导入班次信息")
    def import_class(self, file):
        self.locator_tag_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip(times=10)
        return self

    @allure.step('导入班次信息校验')
    def import_class_check(self, file):
        self.locator_tag_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        return self.get_all_required_prompt()

    @allure.step('获取个人网报报名密码')
    def get_enroll_class_pw(self, name):
        self.go_class_manage(name)
        pw_css = (By.CSS_SELECTOR, '[ctrl-id="enroll_password"] [class$="enroll_password__value"]')
        pw = self.get_ele_text_visitable(pw_css)
        self.close_and_return_page()
        return pw

    @allure.step('导出班次')
    def export_class(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='班次信息.xlsx')

    # @allure.step('查看修改日志')
    # def view_edit_log(self, name):
    #     self.locator_view_button(button_title='修改日志', id_value=name)
    #     self.wait_open_new_browser_and_switch()

