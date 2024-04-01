# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/9 13:51
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class BasePageApp(BasePage):

    def app_locator_text_click(self, value, section_name='', times: int = 0):
        """作者：李国彬，app点击对应模块名称主题，模块名称默认为空"""
        if section_name:
            title_locator = (By.XPATH, f'//*[text()="{section_name}"]/ancestor::div[@ctrl_type="dsf.mobile.section"]'
                                       f'//*[contains(text(),"{value}")]')
        else:
            title_locator = (By.XPATH, f'//*[contains(text(),"{value}")]')
        elms = self.find_elms(title_locator)
        if len(elms) == 1:
            self.excute_js_click_ele(elms[0])
        else:
            for i in elms:
                if str(i.text).strip() == value:
                    self.excute_js_click_ele(i)
                    break
        time.sleep(times)
        return self

    def app_locator_bottom_text_click(self, value):
        """作者：李国彬，app点击下方弹出框的操作按钮"""
        text_button = (By.XPATH, f'//*[contains(@class, "van-popup--bottom") and not(contains(@style, "display"))]'
                                 f'//*[text()="{value}"]')
        self.excute_js_click(text_button)

    def app_locator_tip_info(self):
        """作者：李国彬,获取app的提示信息"""
        tip_info = (By.CSS_SELECTOR, '.van-toast__text')
        self.wait_visibility_ele(tip_info)
        return str(self.driver.find_element(*tip_info).text).strip()

    @allure.step('点击返回')
    def app_click_back(self):
        back_click = (By.XPATH, '//div[@slot-name="head"]//*[contains(text(),"返回")]')
        self.element_click(back_click)
        return self

    @allure.step('获取所有输入校验提示信息')
    def get_all_required_prompt(self):
        return self.get_ele_texts_visitable((By.CSS_SELECTOR, '[class*="error-message"]'))

    # def app_locator_date_range(self, ctrl_id: str, start_date: str, end_date: str):
    #     """
    #     作者：李国彬
    #     输入日期范围的开始日期和结束日期
    #     :param ctrl_id: 元素的唯一ctrl-id
    #     :param start_date: 开始日期
    #     :param end_date: 结束日期
    #     """
    #     date_input = self.find_elms((By.CSS_SELECTOR, f'[ctrl-id="{ctrl_id}"] input'))
    #     # 清除readonly属性
    #     self.driver.execute_script('arguments[0].removeAttribute("readonly")', date_input[0])
    #     self.driver.execute_script('arguments[0].removeAttribute("readonly")', date_input[1])
    #     self.driver.execute_script('arguments[0].value=""', date_input[0])
    #     self.driver.execute_script('arguments[0].value=""', date_input[1])
    #     # 输入值
    #     date_input[0].send_keys(start_date)
    #     date_input[1].send_keys(end_date)
    #     # 点击确定
    #     self.app_locator_bottom_text_click('确定')

