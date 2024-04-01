# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/9/30 15:30
@Author :李国彬
============================
"""
import time

from selenium.webdriver import ActionChains
from common.tools_packages import *


class ClassSeatsSetPage(BasePage):
    """座位设置页面"""
    tip_info = (By.XPATH, '//*[text()="温馨提示"]')

    def __generate_seats(self, row='', col=''):
        row_input = (By.XPATH, '//*[text()="排"]/..//input')
        col_input = (By.XPATH, '//*[text()="列"]/..//input')
        if row:
            self.clear_and_input(row_input, row)
        if col:
            self.clear_and_input(col_input, col)
        button = (By.XPATH, '//*[text()="生成座位表"]')
        self.element_click(button)

    @allure.step('生成座位表')
    def generate_seats(self, row, col):
        self.__generate_seats(row=row, col=col)
        self.locator_dialog_btn(btn_name='继续生成')
        if self.find_elements_no_exception(self.tip_info):
            self.locator_dialog_btn(btn_name='确定')  # 第一次生成时，没有弹窗提示信息
        time.sleep(2)
        return self

    @allure.step('生成座位表数量校验')
    def generate_seats_check(self, row, col):
        self.__generate_seats(row=row, col=col)
        self.locator_dialog_btn(btn_name='继续生成')
        return self.wait_fail_tip()

    @allure.step('获取学员列表学员')
    def get_stu_list(self):
        stu_ele = (By.CSS_SELECTOR, '.ds_student_name')
        return [str(i.text).strip() for i in self.find_elms(stu_ele)]

    def get_col_stu_list(self, col: int):
        stu_list = (By.CSS_SELECTOR, f'.middleright-tr td:nth-child({col}) .item-studentname')
        with allure.step(f'获取第{col}列学员姓名'):
            return [str(i.text).strip() for i in self.find_elms(stu_list)]

    def get_row_stu_list(self, row: int):
        stu_list = (By.CSS_SELECTOR, f'.middleright-table tr:nth-child({row}) .item-studentname')
        with allure.step(f'获取第{row}行学员姓名'):
            return [str(i.text).strip() for i in self.find_elms(stu_list)]

    @allure.step('获取已排座学员列表')
    def get_seats_stu_list(self):
        stu_ele = (By.CSS_SELECTOR, '[class=item-studentname]')
        return [str(i.get_attribute('textContent')).strip() for i in self.find_elms(stu_ele)]

    @allure.step('获取班次学员总数')
    def get_stu_number(self):
        stu_numbers = (By.CSS_SELECTOR, '[class="groupnumber"]')
        elements = self.find_elms(stu_numbers)
        number = 0
        for i in elements:
            number += int(str(i.get_attribute('textContent')).lstrip('（').rstrip('）'))
        return number

    @allure.step('展开小组学员')
    def open_group(self, group):
        group_ele = (By.XPATH, f'//*[contains(text(),"{group}")]')
        self.excute_js_click(group_ele)
        time.sleep(1)
        return self

    @allure.step('拖动学员排座')
    def stu_seat_by_drag(self, name, row, col):
        action = ActionChains(self.driver)
        stu_ele = (By.XPATH, f'//*[@class="student-name" and contains(text(),"{name}")]')
        position_ele = (By.CSS_SELECTOR, f'.middleright-table tr:nth-child({row}) td:nth-child({col})')
        stu = self.find_elem(stu_ele)
        position = self.find_elem(position_ele)
        action.drag_and_drop(stu, position).perform()
        time.sleep(2)
        return self

    @allure.step('删除排座学员')
    def del_stu_seat(self, name):
        action = ActionChains(self.driver)
        stu_ele = (By.XPATH, f'//*[contains(text(),"{name}")]')
        del_ele = (By.XPATH, f'//*[contains(text(),"{name}")]/..//*[@class="del-button-div"]')
        action.move_to_element(self.find_elem(stu_ele)).pause(1).perform()
        del_btn = self.find_elem(del_ele)
        action.move_to_element(del_btn).click(del_btn).perform()
        time.sleep(2)
        return self

    @allure.step('座位导出')
    def export_seat(self, class_name):
        self.locator_dialog_btn(btn_name='座位导出')
        return wait_file_down_and_clean(f'{class_name}座位表.xlsx')

    @allure.step('席卡打印')
    def export_seat_card(self):
        self.locator_dialog_btn(btn_name='席卡打印')
        return wait_file_down_and_clean('席卡.doc')

    @allure.step('一键排座(保留已排)')
    def one_key_to_seats_with_save(self):
        btn_loc = (By.CSS_SELECTOR, '[title="一键排座(保留已排)"]')
        self.excute_js_click(btn_loc)
        if self.find_elements_no_exception(self.tip_info):
            self.locator_dialog_btn(btn_name='确定')
        time.sleep(1)
        return self

    @allure.step('一键排座(清空已排)')
    def one_key_to_seats(self):
        btn_loc = (By.CSS_SELECTOR, '[title="一键排座(清空已排)"]')
        self.excute_js_click(btn_loc)
        if self.find_elements_no_exception(self.tip_info):
            self.locator_dialog_btn(btn_name='确定')
        time.sleep(1)
        return self

    @allure.step('按组排座(横向)')
    def seats_by_group_row(self):
        btn_loc = (By.CSS_SELECTOR, '[title="按组排座(横向)"]')
        self.excute_js_click(btn_loc)
        if self.find_elements_no_exception(self.tip_info):
            self.locator_dialog_btn(btn_name='确定')
        time.sleep(1)
        return self

    @allure.step('按组排座(纵向)')
    def seats_by_group_col(self):
        btn_loc = (By.CSS_SELECTOR, '[title="按组排座(纵向)"]')
        self.excute_js_click(btn_loc)
        if self.find_elements_no_exception(self.tip_info):
            self.locator_dialog_btn(btn_name='确定')
        time.sleep(1)
        return self

    @allure.step('一键清空')
    def clean_seats(self):
        self.locator_dialog_btn(btn_name='一键清空')
        self.locator_dialog_btn('确定')
        time.sleep(2)
        return self
