"""
============================
Author:杨德义
============================
"""
import allure
import time
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage


class TransferArrangedRecords(ArrangTestclassPage):
    """调课记录"""

    # 调课记录班次检索框
    search_input = (By.CSS_SELECTOR, '.search-input input')
    # 调课记录班次检索按钮
    search_btn = (By.CSS_SELECTOR, '.search-button')

    @allure.step('按班次搜索调课记录')
    def search_recording(self, class_name):
        self.locator_search_input(placeholder='请输入班次名称', value=class_name, enter=True)
        return self

    @allure.step('获取调课类型文本')
    def transfer_type(self, index=1):
        transfer_type_loc = (By.XPATH, f'((//*[contains(@class, "is-scrolling")]//*[contains(@class, "el-table__row")])[{index}]//td)[5]')
        return self.driver.find_element(*transfer_type_loc).text.strip()

    @allure.step('调课前排课信息(字典形式)')
    def transfer_info_before(self, index=1):
        # transfer_before = (By.XPATH, f'((//*[contains(@class, "is-scrolling")]//*[contains(@class, "el-table__row")])[{index}]//td)[5]')
        # transfer_before_info_ele = self.driver.find_element(*transfer_before)
        # time.sleep(0.5)
        # original_str = self.driver.execute_script('return arguments[0].textContent', transfer_before_info_ele)
        # time.sleep(0.5)
        # return self.convert_transfer_info_to_dict(original_str)
        course_name = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=before_item_alias__value]')  # 调课后课程名称
        teaching_form = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=before_item_type_text__value]')  # 调课后教学形式
        teacher = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=before_constitutors_text__value]')  # 调课后授课教师
        place = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=before_places_text__value]')  # 调课后授课地点
        stime = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=before_start_datetime__value]')  # 调课后开始时间
        etime = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=before_end_datetime__value]')  # 调课后结束时间
        return {'课程名称': self.trim_text(course_name),
                '教学形式': self.trim_text(teaching_form),
                '授课教师': self.trim_text(teacher),
                '授课地点': self.trim_text(place),
                '开始时间': self.trim_text(stime),
                '结束时间': self.trim_text(etime)}

    @allure.step('调课后排课信息(字典形式)')
    def transfer_info_after(self, index=1):
        # transfer_after = (By.XPATH, f'((//*[contains(@class, "is-scrolling")]//*[contains(@class, "el-table__row")])[{index}]//td)[6]')
        # transfer_after_info_ele = self.driver.find_element(*transfer_after)
        # time.sleep(0.5)
        # original_str = self.driver.execute_script('return arguments[0].textContent', transfer_after_info_ele)
        # time.sleep(0.5)
        # return self.convert_transfer_info_to_dict(original_str)
        course_name = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=after_item_alias__value]')  # 调课后课程名称
        teaching_form = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=after_item_type_text__value]')  # 调课后教学形式
        teacher = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=after_constitutors_text__value]')  # 调课后授课教师
        place = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=after_places_text__value]')  # 调课后授课地点
        stime = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=after_start_datetime__value]')  # 调课后开始时间
        etime = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=after_end_datetime__value]')  # 调课后结束时间
        return {'课程名称': self.trim_text(course_name),
                '教学形式': self.trim_text(teaching_form),
                '授课教师': self.trim_text(teacher),
                '授课地点': self.trim_text(place),
                '开始时间': self.trim_text(stime),
                '结束时间': self.trim_text(etime)}

    @staticmethod
    @allure.step('调课前/后原生字符串信息转字典形式')
    def convert_transfer_info_to_dict(original_transfer_info):
        transfer_info_dict = {}
        for value in original_transfer_info.strip().split('  '):
            if value.startswith('开始时间'):
                transfer_info_dict.update({'开始时间': value.split('开始时间:')[1]})
            elif value.startswith('结束时间'):
                transfer_info_dict.update({'结束时间': value.split('结束时间:')[1]})
            else:
                m = value.split(':')
                transfer_info_dict.update({m[0]: m[1]})
        return transfer_info_dict

    @property
    @change_reset_implicit(1)
    @allure.step('获取按班次检索调课记录检索结果表单条数')
    def table_count_searched(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        table_data = self.driver.find_elements(*tr)
        table_count = len(table_data)
        return table_count
