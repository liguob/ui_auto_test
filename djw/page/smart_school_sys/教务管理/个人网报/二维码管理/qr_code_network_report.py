# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/22    15:19
============================
"""
import time
import allure

from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.主页.home_page import HomePage
from common.file_path import *


class QrCodeNetworkReport(HomePage):
    """个人网报-二维码管理"""
    save_btn = (By.CSS_SELECTOR, '[title="保存"]')

    def __edit_info(self, values: dict):
        keys = values.keys()
        if '二维码名称' in keys:
            name = (By.CSS_SELECTOR, '[ctrl-id=name] input')
            self.clear_and_input_enter(name, values["二维码名称"])
        if '班次选择' in keys:
            search_btn = (By.CSS_SELECTOR, '[ctrl-id=classes] i[class*=search]')  # 班次选择
            self.excute_js_click(search_btn)
            search_input = (By.CSS_SELECTOR, '[placeholder="班级名称"]')  # 查询输入
            self.clear_and_input_enter(search_input, values["班次选择"])
            time.sleep(2)
            all_select = (By.CSS_SELECTOR, '[role=dialog] table[class*=header] span[class*=el-checkbox__inner]')  # 全选
            self.excute_js_click(all_select)
            save_btn = (By.XPATH, '//span[text()="确定"]')
            self.excute_js_click(save_btn)
        if '有效开始时间' in keys:
            self.locator_date_range(ctrl_id="effectivet", start_date=values['有效开始时间'],
                                    end_date=values['有效结束时间'])
        time.sleep(1)
        click_ele = (By.CSS_SELECTOR, '.el-dialog__header')  # 点击主题避免元素遮挡
        self.move_to_click(click_ele)

    @allure.step("查询二维码")
    def search_qr_code(self, key: str):
        search = (By.CSS_SELECTOR, '[placeholder="二维码名称"]')
        self.clear_and_input_enter(search, key)
        time.sleep(2)
        return self

    @allure.step("班次生成二维码")
    def create_qr_code_class(self, values: dict):
        self.locator_button(button_title='生成二维码')
        self.__edit_info(values)
        self.locator_button(button_title='保存', dialog_title='生成二维码')
        self.wait_success_tip()
        sleep(3)  # 等待弹窗页面自动关闭
        return self

    @allure.step("删除班次二维码")
    def del_qr_code_class(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn("确定")
        self.wait_tip()
        return self

    @allure.step("编辑班次二维码")
    def edit_qr_code_class(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        sleep(2)
        self.__edit_info(values)
        self.excute_js_click(self.save_btn)
        self.wait_tip()
        sleep(3)  # 等待弹窗页面自动关闭
        return self

    @allure.step("下载班次二维码")
    def download_qr_code(self, name, file_name):
        self.locator_view_button(button_title='二维码下载', id_value=name)
        return wait_file_down_and_clean(file_name)

    @allure.step("获取二维码扫描地址信息")
    def get_qr_code_info(self, name):
        img_element = (By.CSS_SELECTOR, '[ctrl-id="qrcode"] img')
        self.locator_view_button(button_title='编辑', id_value=name)
        time.sleep(2)  # 等待二维码加载，避免无法获取二维码信息
        img = self.screenshot_locator(img_element)
        return self.scan_qr_code(img)
