# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage
import json


class MeetingAttendance(HomePage):
    """会议考勤"""

    @allure.step('查询会议')
    def search_meeting(self, name):
        self.locator_search_input(placeholder='请输入会议名称', value=name, enter=True, times=2)
        return self

    @allure.step('会议列表导出')
    def download_meeting(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='会议列表.xlsx')

    @allure.step('批量下载会议考勤二维码')
    def download_attendance_qr(self):
        self.locator_view_select_all()
        self.locator_dialog_btn(btn_name='批量下载')
        return wait_file_down_and_clean('会议考勤二维码.zip')

    @allure.step('扫描考勤二维码')
    def scan_attendance_code(self, name):
        """返回二维码扫描数据"""
        self.locator_view_button(button_title='考勤二维码', id_value=name)
        pic_loc = (By.CSS_SELECTOR, 'img[src^="blob"]')
        self.find_elem_visibility(pic_loc)
        pic = self.screenshot_locator(pic_loc)
        return json.loads((self.scan_qr_code(pic)))

    @allure.step('点击查看详情')
    def go_attendance_detail(self, name):
        self.locator_view_button(button_title='查看考勤', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.后勤管理.会议管理.会议考勤.meeting_attendance_detail import \
            MeetingAttendanceDetail
        return MeetingAttendanceDetail(self.driver)
