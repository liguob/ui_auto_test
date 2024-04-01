# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/6 16:03
# Author     ：李国彬
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.对外培训.out_traing_page import OutTrainingPage


class OutTrainingClassManagePage(OutTrainingPage):
    """对外培训-班次管理"""

    @allure.step('查询对外班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('新增对外班次')
    def add_class(self, values: dict):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.对外培训.班次管理.班次管理.out_training_class_info_page import \
            OutTrainingClassInfoPage
        OutTrainingClassInfoPage(self.driver).edit_info(values)
        return self

    @allure.step('删除对外班次')
    def del_class(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn('确定')
        time.sleep(2)
        return self

    @allure.step('进入编辑对外班次页面')
    def go_edit_class(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='name')
        time.sleep(1)
        from djw.page.smart_school_sys.对外培训.班次管理.班次管理.out_training_class_info_page import \
            OutTrainingClassInfoPage
        return OutTrainingClassInfoPage(self.driver)

    @allure.step('进入学员列表管理')
    def go_stu_manage(self, name):
        self.locator_view_button(button_title='学员列表', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.对外培训.班次管理.学员管理.out_traing_class_stu_manage_page import \
            OutTrainingClassStuManage
        return OutTrainingClassStuManage(self.driver)

    @allure.step('导出对外培训班次')
    def download_class(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('外培班次表.xlsx')
