# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 17:25
@Author :李国彬
============================
"""
import allure
from selenium.webdriver.common.by import By
from common.random_tool import RandomData

from common.base_page import BasePage

Random_Data = RandomData()


class NetworkReportApplyManagePage(BasePage):
    """网报管理网报端主页"""
    user_info = (By.CSS_SELECTOR, '[ctrl_type="dsf.teasuserinfosetting"]')  # 登录后的个人信息

    def __init__(self, driver):
        super().__init__(driver)
        dialog_locator = (By.CSS_SELECTOR, '[aria-label="完善单位信息"]')  # 弹出的完善单位信息窗口
        result = self.driver.find_elements(*dialog_locator)  # 有弹窗则补全单位信息
        if result:
            from djw.page.smart_school_sys.网报管理.网报端.单位信息.unit_info_manage_page import UnitInfoManagePage
            data = {'办公电话': Random_Data.random_phone(), '详细地址': '地址信息'}
            UnitInfoManagePage(self.driver).edit_unit_info(data)

    @allure.step('进入网报学员管理页面')
    def go_apply_stu_manage_page(self):
        self.locator_left_menu_click(button_title='网报学员管理')
        from djw.page.smart_school_sys.网报管理.网报端.网报学员管理.network_report_stu_manage_page import \
            NetworkReportApplyStuManagePage
        return NetworkReportApplyStuManagePage(self.driver)

    @allure.step('进入报名管理')
    def go_apply_manage_page(self):
        self.locator_left_menu_click(button_title='报名管理')
        from djw.page.smart_school_sys.网报管理.网报端.报名管理.apply_manage_page import ApplyManagePage
        return ApplyManagePage(self.driver)

    @allure.step('进入网报通知查看页面')
    def go_notice_view_manage_page(self):
        self.locator_left_menu_click(button_title='网报通知查看')
        from djw.page.smart_school_sys.网报管理.网报端.网报通知查看.notice_view_manage import NoticeViewManagePage
        return NoticeViewManagePage(self.driver)
