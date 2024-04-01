# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class CarsList(LogisticsManagePage):

    def __edit_info(self, info: dict):
        """编辑车辆信息"""
        keys = info.keys()
        if '品牌型号' in keys:
            self.locator_text_input(ctrl_id='brand', value=info['品牌型号'])
        if '车牌号' in keys:
            self.locator_text_input(ctrl_id='car_number', value=info['车牌号'])
        if '车架号' in keys:
            self.locator_text_input(ctrl_id='vehicle_frame', value=info['车架号'])
        if '注册登记时间' in keys:
            self.locator_date(ctrl_id='registration_time', value=info['注册登记时间'])
        if '检车月份' in keys:
            self.locator_text_input(ctrl_id='inspection_month', value=info['检车月份'], is_readonly=True)
        if '车辆状态' in keys:
            self.locator_select_list_value(ctrl_id='status', value=info['车辆状态'])
        time.sleep(1)
        self.locator_button(button_title='保存')

    @allure.step('编辑车辆信息')
    def edit_car(self, name, info: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待信息加载
        self.__edit_info(info)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('新增车辆信息')
    def add_car(self, info: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.__edit_info(info)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('删除车辆')
    def del_car(self, car_num):
        self.locator_view_button(button_title='删除', id_value=car_num)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('搜索车辆')
    def search_car(self, car_num):
        self.locator_tag_search_input(placeholder='车牌号', value=car_num)
        self.locator_tag_search_button()
        return self

    @allure.step('导出车辆列表')
    def export_cars(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='车辆信息.xlsx')
