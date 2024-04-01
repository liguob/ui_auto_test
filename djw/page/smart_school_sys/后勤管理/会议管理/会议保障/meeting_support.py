# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class MeetingSupport(LogisticsManagePage):
    """会议保障"""

    @allure.step('查看会议')
    def search_meeting(self, name):
        self.locator_tag_search_input(placeholder='会议名称', value=name, times=2, enter=True)
        return self
