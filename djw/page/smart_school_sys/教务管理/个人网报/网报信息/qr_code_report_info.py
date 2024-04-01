# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/26    11:19
============================
"""
from common.tools_packages import *
from common.base_page_app import BasePageApp


class PersonNetReportPage(BasePageApp):
    """个人网报信息填写页面"""

    @allure.step("个人网报报名")
    def add_id_info(self, values: dict):
        self.app_locator_text_click(value='我要报名')
        time.sleep(3)
        self.element_click((By.CSS_SELECTOR, 'button[class*="signupbutton"]'))
        time.sleep(1)
        if '报名密码' in values:
            with allure.step('填写报名密码'):
                pwd = (By.CSS_SELECTOR, 'input[placeholder="请输入报名码"]')
                self.input_send_keys(pwd, values['报名密码'])
                self.locator_dialog_btn('确定')
        name_ele = (By.CSS_SELECTOR, 'input[placeholder="请输入姓名"]')
        phone_ele = (By.CSS_SELECTOR, 'input[placeholder="请输入手机号码"]')
        code = (By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]')
        with allure.step('填写个人信息'):
            self.input_send_keys(name_ele, values['姓名'])
            self.input_send_keys(phone_ele, values['手机号码'])
            self.input_send_keys(code, 'good')
            self.locator_dialog_btn("确定")
            time.sleep(2)
            required_fields = (By.CSS_SELECTOR, '.van-cell--required .van-field__label')
            required_fields = self.get_ele_texts_visitable(required_fields)
            if '性别' in required_fields:
                self.locator_select_radio(ctrl_id='gender', value='男')
            if '身份证号' in required_fields:
                self.locator_text_input(ctrl_id='idcard', value=randomTool.random_idcard())
            if '民族' in required_fields:
                self.excute_js_click((By.CSS_SELECTOR, '[ctrl-id=nation] .placeholder'))
                self.app_locator_bottom_text_click(value='汉族')
                time.sleep(1)
            if '政治面貌' in required_fields:
                self.excute_js_click(loc=(By.CSS_SELECTOR, '[ctrl-id="part"] .placeholder'))
                self.app_locator_bottom_text_click(value='中国共产党党员')
                time.sleep(1)
            if '联系人' in required_fields:
                self.locator_text_input(ctrl_id='dalxr', value=randomTool.random_name())
        with allure.step('提交报名信息'):
            self.locator_dialog_btn("提交")
            self.locator_dialog_btn("确认")
            time.sleep(1)
        return self

    @allure.step('获取报名状态')
    def get_submit_status(self):
        status = (By.CSS_SELECTOR, 'div.success')
        return self.get_ele_text_visitable(status)
