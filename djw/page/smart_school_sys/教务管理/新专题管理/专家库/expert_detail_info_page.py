# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/27 10:37
# Author     ：李国彬
============================
"""
from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import allure


class ExpertDetailInfoPage(BasePage):
    """专家详情信息页面"""

    @allure.step('选择师资来源')
    def chose_source(self, source):
        source_input = (By.CSS_SELECTOR, '[ctrl-id=source] input')
        self.poll_click(source_input)
        time.sleep(0.5)
        source_option = (By.XPATH, f'//*[@class="el-scrollbar"]//*[contains(text(), "{source}")]')
        self.poll_click(source_option)
        time.sleep(0.5)

    def __edit_info(self, values: dict):
        """填写专家详情信息"""
        keys = values.keys()
        if '师资来源' in keys:
            self.chose_source(values['师资来源'])
            if values['师资来源'] == '校外' and '姓名' in keys:
                self.locator_text_input(ctrl_id='name', value=values['姓名'])
            elif values['师资来源'] == '校内' and '姓名' in keys:
                self.locator_button(button_title='选择校内教师')
                self.locator_search_input(placeholder='输入关键字进行过滤', value=values['姓名'], enter=True)
                self.locator_tree_node_click(node_value=values['姓名'])
                confirm = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')
                self.poll_click(confirm)
        if '联系电话' in keys:
            self.locator_text_input(ctrl_id='phone', value=values['联系电话'])
        if '职务' in keys:
            self.locator_text_input(ctrl_id='post', value=values['职务'])
        self.locator_button(button_title='保存')

    def edit_info(self, values: dict):
        self.__edit_info(values)
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self
