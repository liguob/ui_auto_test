# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *


class MeetingAttendanceDetail(BasePage):
    """会议考勤详情"""

    @allure.step('查询参会人')
    def search_user(self, name):
        self.locator_search_input(placeholder='请输入姓名', times=2, value=name, enter=True)
        return self

    def edit_attendance_status(self, name, action):
        with allure.step(f'参会人考勤状态置为{action}'):
            btn_loc = (
                By.XPATH, f'//*[@role="tabpanel" and not(@aria-hidden)]//span[contains(text(),"{action}")]/ancestor::a')
            self.locator_view_select(id_value=name)
            self.element_click(btn_loc)
            if action == '请假':
                input_loc = (By.CSS_SELECTOR, "[placeholder='请输入']")
                self.find_elem(input_loc).send_keys('请假原因')
                self.locator_dialog_btn(btn_name='确认')
            self.wait_success_tip()
        return self
