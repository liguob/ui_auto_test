# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class MyMeeting(HomePage):
    """我的会议"""

    @allure.step('查询会议')
    def search_meeting(self, name):
        self.locator_search_input(placeholder='会议名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('查看请假原因')
    def view_leave(self, name):
        self.locator_view_button(button_title='请假原因', id_value=name)
        info_loc = (By.CSS_SELECTOR, '[aria-label="请假原因"] p')
        return self.get_ele_text_visitable(info_loc)
