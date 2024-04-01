# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 16:51
@Author :李国彬
============================
"""
import time

import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class NoticeManagePage(HomePage):
    """网报通知管理"""

    @allure.step('查询网报通知')
    def search_notice(self, name):
        self.locator_tag_search_input(placeholder='标题', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('新增网报通知')
    def add_notice(self, values: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.网报管理.管理端.网报通知管理.notice_info_page import NoticeInfoPage
        NoticeInfoPage(self.driver).edit_notice_info(values)
        self.locator_button(button_title='保存')
        time.sleep(2)  # 等待窗口自动关闭
        self.switch_to_window(-1)
        return self

    @allure.step('编辑网报通知')
    def edit_notice(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待数据加载
        from djw.page.smart_school_sys.网报管理.管理端.网报通知管理.notice_info_page import NoticeInfoPage
        NoticeInfoPage(self.driver).edit_notice_info(values)
        self.locator_button(button_title='保存')
        time.sleep(2)  # 等待窗口自动关闭
        self.switch_to_window(-1)
        return self

    @allure.step('删除网报通知')
    def del_notice(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('发布网报通知')
    def publish_notice(self, name):
        self.locator_view_button(button_title='发布', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('取消发布网报通知')
    def cancel_publish_notice(self, name):
        self.locator_view_button(button_title='撤回', id_value=name)
        self.wait_success_tip()
        return self
