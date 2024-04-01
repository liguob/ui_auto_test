# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class CarApply(LogisticsManagePage):

    @allure.step('查询用车申请')
    def search_apply(self, date_time):
        self.locator_search_input(placeholder='使用日期', value=date_time)
        self.locator_tag_search_button()
        return self

    @allure.step('删除用车申请')
    def del_apply(self, date_time):
        self.locator_view_button(button_title='删除', id_value=date_time)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('查看用车申请详情')
    def view_detail(self, date_time):
        user_name_loc = (By.CSS_SELECTOR, '[ctrl-id="vehicle_user"] .ds-form-block')
        self.locator_view_button(button_title='查看', id_value=date_time)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        return self.find_elem(user_name_loc).get_attribute('textContent')

    @allure.step('点击新增进入用车申请填写页面')
    def click_add_apply(self):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.后勤管理.车辆管理.用车申请.edit_car_info import CarInfoEdit
        return CarInfoEdit(self.driver)

    @allure.step('点击编辑进入用车申请填写页面')
    def click_edit_apply(self, date_time):
        self.locator_view_button(button_title='编辑', id_value=date_time)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        from djw.page.smart_school_sys.后勤管理.车辆管理.用车申请.edit_car_info import CarInfoEdit
        return CarInfoEdit(self.driver)
