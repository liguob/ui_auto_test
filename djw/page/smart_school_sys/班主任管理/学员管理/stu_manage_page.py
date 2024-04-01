# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/25    16:35
============================
用于班主任管理-学员管理页面的操作
"""
import allure

from common.base_page import BasePage
from common.tools_packages import *


class StuManagePage(BasePage):

    @allure.step("进入当前班次页签")
    def switch_current_class(self):
        """切换到当前班次"""
        current_class_tag = (By.XPATH, '//div[@role="tablist"]//*[contains(text(), "当前班次")]')  # 当前班次tab页签
        self.excute_js_click(current_class_tag)
        return self

    @allure.step("进入未开始班次页签")
    def switch_feature_class(self):
        """切换到未开始班次"""
        feature_class_tag = (By.XPATH, '//div[@role="tablist"]//*[contains(text(), "未开始班次")]')  # 未开始班次tab页签
        self.excute_js_click(feature_class_tag)
        return self

    @allure.step("进入历史班次页签")
    def switch_history_class(self):
        """切换到历史班次"""
        history_class_tag = (By.XPATH, '//div[@role="tablist"]//*[contains(text(), "历史班次")]')  # 历史班次tab页签
        self.excute_js_click(history_class_tag)
        return self

    @allure.step("进入学员的管理页面")
    def go_student_manage_page(self, name):
        # 点击管理
        self.locator_view_button(button_title='管理', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        from djw.page.smart_school_sys.班主任管理.学员管理.stu_manage_info_page import StuManageInfoPage
        return StuManageInfoPage(self.driver)

    @allure.step("进入学员分组页面")
    def go_student_group_page(self, name):
        # 点击分组
        self.locator_view_button(button_title='分组', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.班主任管理.学员管理.stu_manage_group_manage import StudentGroupManagePage
        return StudentGroupManagePage(self.driver)

    @allure.step("查询班次")
    def search_class(self, name):
        # 查询班次输入框
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('历史班次下载学员手册')
    def export_stu_handle_book(self, name):
        self.locator_view_button(button_title='学员手册', id_value=name)
        return wait_file_down_and_clean(f'{name}-学员手册.doc')

    @allure.step('进入历史班次学员查看')
    def go_history_class_stu_info(self, name):
        self.locator_view_button(button_title='学员查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.班主任管理.学员管理.stu_history_manage_info_page import StuHistoryManageInfo
        return StuHistoryManageInfo(self.driver)

    @allure.step('导出班次')
    def download_class_file(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn('确定')
        return wait_file_down('班级信息.xlxs')
