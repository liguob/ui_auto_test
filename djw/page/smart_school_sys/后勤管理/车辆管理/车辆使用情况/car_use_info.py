# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class CarUseInfo(LogisticsManagePage):

    @allure.step('查询用车情况')
    def search_car(self, name):
        self.locator_search_input(placeholder='车牌号', value=name, enter=True, times=2)
        return self

    @allure.step('导出车辆使用情况')
    def export_info(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='用车情况.xlsx')

    @allure.step('查看用车情况详情')
    def view_detail(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        car_user_value = (By.CSS_SELECTOR, '[ctrl-id="vehicle_user"] [title]')
        return self.get_ele_text_visitable(car_user_value)
