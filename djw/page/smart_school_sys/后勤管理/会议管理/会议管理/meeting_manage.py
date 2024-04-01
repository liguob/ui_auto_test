# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class MeetingManage(LogisticsManagePage):

    @allure.step('查询会议')
    def search_meeting(self, name):
        self.locator_tag_search_input(placeholder='会议名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('点击新增会议')
    def click_add_btn(self):
        self.locator_tag_button(button_title='打开窗口')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.后勤管理.会议管理.会议管理.meeting_info import MeetingInfo
        return MeetingInfo(self.driver)

    @allure.step('进入编辑会议')
    def click_edit_btn(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.后勤管理.会议管理.会议管理.meeting_info import MeetingInfo
        time.sleep(2)  # 等待信息加载
        self.locator_get_js_input_value(ctrl_id='name', times=5)
        return MeetingInfo(self.driver)

    @allure.step('发布会议')
    def push_meeting(self, name):
        self.locator_view_button(button_title='发布', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('取消发布')
    def cancel_push_meeting(self, name):
        self.locator_view_button(button_title='取消发布', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('删除会议')
    def del_meeting(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导出会议信息文件')
    def download_meeting(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='会议列表.xlsx')

    @allure.step('席卡下载')
    def download_meeting_seats(self, name):
        self.locator_view_select(id_value=name)
        self.locator_dialog_btn(btn_name='席卡下载')
        return wait_file_down_and_clean(file_name=f'{name}.docx')

    @allure.step('点击上传会议文件')
    def click_upload_meeting_file(self, name):
        self.locator_view_button(button_title='上传会议文件', id_value=name)
        return self

    @allure.step('上传会议文件')
    def upload_file(self, file):
        self.locator_dialog_btn(btn_name='上传', dialog_title='dialog')
        file_input = (By.CSS_SELECTOR, 'input[type="file"]')
        self.upload_input_file_no_click(loc_input=file_input, file=file)
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('查询会议文件')
    def search_meeting_file(self, name: str = ''):
        self.locator_search_input(placeholder='文件名称', value=name, enter=True, times=2)
        return self
