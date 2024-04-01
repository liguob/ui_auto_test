# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class CarApplyReview(LogisticsManagePage):

    @allure.step('查询用车申请')
    def search_apply(self, date_time):
        self.locator_tag_search_input(placeholder='用车时间', value=date_time)
        self.locator_tag_search_button()
        return self

    @allure.step('审批-退回用车申请')
    def reject_apply(self, date_time):
        self.locator_view_button(button_title='审核', id_value=date_time)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待按钮元素加载，否则会点击到同意
        self.locator_button(button_title='退回')
        self.locator_search_input(placeholder='请输入退回原因', value=randomTool.random_str())
        self.locator_dialog_btn('确定')
        self.switch_to_window(-1)
        return self

    @allure.step('审批-同意用车申请')
    def agree_apply(self, use_name: str, car_name: str = ''):
        self.locator_view_button(button_title='审核', id_value=use_name)
        self.wait_open_new_browser_and_switch()
        if car_name:
            self.locator_search_magnifier(ctrl_id='car_and_driver')
            self.locator_search_input(placeholder='车牌号', value=car_name, enter=True, times=2)
            self.locator_view_select(id_value=car_name)
            self.locator_dialog_btn(btn_name='确定')
            time.sleep(1)
        self.locator_button(button_title='发送')
        self.wait_browser_close_switch_latest()  # 等待窗口自动关闭
        return self
