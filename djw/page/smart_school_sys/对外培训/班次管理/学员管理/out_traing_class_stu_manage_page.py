# coding: utf-8
"""
============================
# Time      ：2022/5/12 10:26
# Author    ：李国彬
============================
"""
from common.tools_packages import *


class OutTrainingClassStuManage(BasePage):
    """对外培训学员管理"""

    @allure.step('新增对外班次学员')
    def add_stu(self, data: dict):
        self.locator_button('新增学员')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.对外培训.班次管理.学员管理.out_training_class_stu_info import OutTrainingClassStuInfo
        OutTrainingClassStuInfo(self.driver).edit_student_info(data)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('查询学员')
    def search_stu(self, name=''):
        self.locator_search_input(placeholder='请输入姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step("修改对外班次学员")
    def edit_stu(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        # 等待接口数据返回
        sleep(3)
        # 进入编辑页面
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_student_page import ClassManageEditStudentPage
        ClassManageEditStudentPage(self.driver).edit_student_info(values)
        # 等待窗口关闭学员信息页面
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('查看对外班次学员（获取姓名）')
    def view_stu(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        name_loc = (By.CSS_SELECTOR, F"[title='{name}']")
        return self.get_text_implicitly(name_loc)

    @allure.step('导入对外培训学员')
    def import_stu(self, file: str):
        self.locator_tag_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导出对外培训学员')
    def download_stu(self):
        self.locator_button('导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('外培学员表.xlsx')

    @allure.step('删除对外培训学员')
    def del_stu(self):
        self.locator_button(button_title='删除')
        self.locator_dialog_btn('确定')
        return self
