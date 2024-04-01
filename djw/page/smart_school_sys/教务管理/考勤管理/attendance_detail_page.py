# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/1 14:17
@Author :李国彬
============================
"""
from common.tools_packages import *

from common.base_page import BasePage


class AttendanceDetailPage(BasePage):
    """考勤详情页面"""

    @allure.step('进入课程管理')
    def into_manage(self, name):
        btn_loc = (By.XPATH, f'//*[contains(text(),"{name}")]//ancestor::tr//*[text()="管理" or @title="管理"]')
        self.excute_js_click(btn_loc)
        return self

    def edit_attendance_status(self, action):
        """修改学员考勤状态"""
        with allure.step(f'学员考勤状态置为{action}'):
            self.locator_dialog_btn(btn_name=action, dialog_title='考勤管理')
            self.wait_success_tip()
            time.sleep(2)
        return self

    @allure.step('查询学员')
    def search_stu(self, name):
        self.locator_tag_search_input(placeholder='学员姓名/考勤状态', value=name, dialog_title='考勤管理')
        self.locator_tag_search_button(dialog_title='考勤管理')
        return self

    @allure.step('查看二维码')
    def view_qr_code(self, name):
        view_qr_btn = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//*[contains(text(), "查看二维码")]')
        img_ele = (By.CSS_SELECTOR, '[module-name*="qrcodeimage"] [src]')
        self.excute_js_click(view_qr_btn)
        # self.locator_view_button(button_title='查看二维码', id_value=name)
        time.sleep(2)
        img_file = self.screenshot_locator(img_ele)
        return self.scan_qr_code(img_file)

    @allure.step('查询课程')
    def search_course(self, name):
        self.locator_search_input(placeholder='课程名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('导出签到表')
    def download_sign_file(self, name):
        btn_loc = (By.XPATH, f'//*[contains(text(),"{name}")]//ancestor::tr//*[@title="导出签到表" or text()="导出签到表"]')
        self.excute_js_click(btn_loc)
        return wait_file_down_and_clean(file_name=f'{name}.doc')
