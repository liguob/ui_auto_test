# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class MeetingMinutes(LogisticsManagePage):
    """会议纪要"""

    @allure.step('查询会议')
    def search_meeting(self, name):
        self.locator_search_input(placeholder='会议名称', value=name, times=2, enter=True)
        return self

    @allure.step('导出会议文件')
    def download_meeting(self):
        self.locator_view_select_all()
        self.locator_dialog_btn(btn_name='导出')
        return wait_file_down_and_clean(file_name='会议文件.zip')

    @allure.step('查看会议详情')
    def view_meeting(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        name_loc = (By.CSS_SELECTOR, '[ctrl-id="name"] [title]')
        name = self.get_ele_text_visitable(name_loc)
        self.close_and_return_page()
        return name

    @allure.step('点击查看会议文件')
    def click_meeting_file(self, name):
        self.locator_view_button(button_title='会议文件', id_value=name)
        return self

    @allure.step('批量下载会议文件')
    def download_all_file(self, name):
        self.locator_view_select_all(dialog_title='dialog')
        self.locator_dialog_btn(btn_name='批量下载')
        return wait_file_down_and_clean(f'【{name}】会议文件.zip')

    @allure.step('下载指定会议文件')
    def download_single_file(self, file_name):
        self.locator_view_button(button_title='下载', id_value=file_name, dialog_title='dialog')
        return wait_file_down_and_clean(file_name=file_name)
