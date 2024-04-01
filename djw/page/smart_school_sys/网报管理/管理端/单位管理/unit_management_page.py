# -*- coding: UTF-8 -*-
"""
Created on 2021年07月08日 

@author: liudongjie
"""
import sys
import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from time import sleep
from common.random_tool import random_company, randomTool
from common.file_path import wait_file_down_and_clean
import random
import allure


class UnitManagementPage(BasePage):

    @staticmethod
    def _close_windows():
        """关闭上传文件窗口"""
        if sys.platform == "win32":
            from pykeyboard import PyKeyboard
            time.sleep(2)
            pyk = PyKeyboard()
            pyk.tap_key(pyk.cancel_key, 1)

    @allure.step('点击新增')
    def add_unit_button_click(self):
        self.locator_tag_button(button_title='新增')
        sleep(1)
        return self

    def get_unit_list_name(self):
        unit_name_locator = (By.XPATH,
                             '//div[contains(@class,"is-scrolling-left")]//span[contains(@class,"unit_name__value")]')
        unit_name_dic = self.publish_get_info(unit_name_locator, title=['单位名称', ])
        return [n['单位名称'] for n in unit_name_dic]

    @allure.step('新增单位-全部填写')
    def add_unit_input_all(self):
        """
        新增一个单位-填写全部字段
        """
        with allure.step("填写单位信息"):
            unit_name = random_company()[:-4] + '单位' + randomTool.random_range_str(4, 4)
            self.locator_text_input(ctrl_id='name', value=unit_name)  # 单位名称
            self.locator_text_input(ctrl_id='abbreviation', value=unit_name.split('市')[1][:-2])  # 单位简称
            self.locator_text_input(ctrl_id='office_phone', value=randomTool.random_phone())  # 办公电话
            self.locator_text_input(ctrl_id='dept', value=randomTool.random_range_str())  # 部门
            self.locator_text_input(ctrl_id='ds_order', value=random.randint(20, 50))  # 排序码
            self.locator_text_input(ctrl_id='address', value=randomTool.random_address())  # 详细地址
        with allure.step('填写单位管理员信息'):
            name_loc = (By.CSS_SELECTOR, '[form-name*="teas_enroll_unit_administrator.name"] input')
            login_name_loc = (By.CSS_SELECTOR, '[form-name^="teas_enroll_unit_administrator.loginname"] input')
            phone_loc = (By.CSS_SELECTOR, '[form-name^="teas_enroll_unit_administrator.phone"] input')
            self.locator_button(dialog_title='单位信息', button_title='新增')
            unit_admin_name = randomTool.random_name_long()
            self.find_elem(name_loc).send_keys(unit_admin_name)
            self.find_elem(login_name_loc).send_keys(randomTool.random_range_str(5, 5))
            self.find_elem(phone_loc).send_keys(randomTool.random_phone())
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return unit_name, unit_admin_name

    @allure.step('删除单位校验')
    def del_unit_check(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        return self.wait_fail_tip()

    @allure.step('删除单位')
    def del_unit(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('点击编辑单位')
    def edit_click_unit(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        return self

    @allure.step('删除单位管理员')
    def del_unit_admin(self, name):
        self.excute_js_click((By.XPATH, f'//*[@title="{name}"]/ancestor::tr//*[@title="删除"]'))
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('批量删除单位')
    def del_more_unit(self):
        self.locator_more_tip_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导入网报单位')
    def import_unit(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn(dialog_title='预导入文件编辑', btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('异常导入网报单位')
    def import_unit_error(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn(dialog_title='预导入文件编辑', btn_name='确定')
        return self

    @allure.step('编辑单位')
    def edit_unit_name_input(self, unit_name):
        """编辑单位名称"""
        sleep(2)
        self.locator_text_input(ctrl_id='name', value=unit_name)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('禁用单位')
    def disable_unit(self, name):
        self.locator_view_button(button_title='禁用', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('启用单位')
    def enable_unit(self, name):
        self.locator_view_button(button_title='启用', id_value=name)
        self.wait_success_tip()
        sleep(2)
        return self

    @allure.step("获取单位管理员信息")
    def get_unit_admin_info(self):
        locator = '//div[contains(@class,"scrolling")]//tr/td[{}]'
        locators = list(map(lambda x: (By.XPATH, locator.format(x)), range(3, 7)))
        title = ("单位名称", "姓名", "手机", "账号")
        return self.publish_get_info(*locators, head=title)

    @allure.step('查询单位')
    def search_unit(self, name=''):
        self.locator_tag_search_input(placeholder='单位名称', value=name, times=2)
        self.locator_tag_search_button()
        return self

    @allure.step('单位模板下载')
    def download_model(self, name):
        self.locator_more_tip_button(button_title='模板下载')
        return wait_file_down_and_clean(file_name=name)

    @allure.step('网报管理员导入')
    def import_report_admin(self, unit_name, file):
        self.locator_view_button(button_title='预导入', id_value=unit_name)
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn('确定')
        return self.wait_success_tip()

    @allure.step('网报管理员异常导入')
    def import_report_admin_error(self, unit_name, file):
        self.locator_view_button(button_title='预导入', id_value=unit_name)
        sleep(1)
        self.element_click((By.XPATH, '//span[text()="导入数据"]'))
        self._close_windows()
        self.find_elms((By.CSS_SELECTOR, 'input[type="file"]'))[-1].send_keys(file)
        self.wait_listDataCount_searched(tr=(By.CSS_SELECTOR, '.el-dialog .el-table__row'), count=1)
        self.locator_dialog_btn('确定')
        return self

    @allure.step('重置单位管理员密码')
    def reset_pw(self, unit_name):
        self.locator_view_button(button_title='编辑', id_value=unit_name)
        self.locator_button(button_title='重置全部密码')
        self.locator_dialog_btn('确定')
        return self.wait_success_tip()
