# encoding=utf-8
"""
============================
Author:
Time:
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from common.random_tool import randomTool
from djw.page.smart_school_sys.人事系统.规章制度.规章制度管理.rulemanage import RuleManagePage


class AddRulePage(RuleManagePage):
    """新增规章制度页面类"""
    tip_success = (By.XPATH, '//div[@*="el-message el-message--success"]')  # 成功的提示
    input_title = (By.XPATH, '//div[@ctrl-id="title"]//input')  # 规章制度标题
    save_btn = (By.CSS_SELECTOR, '.foot-inner .ds-button[title=保存]')  # 表单保存按钮

    @allure.step('编辑规章制度')
    def edit_rule(self, **kwargs):
        value = {"title": randomTool.random_str(), "detail": '详情_{}'.format(randomTool.random_str())}
        value.update(kwargs)
        publish_date = (By.CSS_SELECTOR, '[ctrl-id=publish_date] .ds-form-readonly span')  # 发布日期
        detail_frame = (By.XPATH, '//div[@ctrl-id="content"]//iframe[@id]')  # 详情输入框的frame
        detail_input = (By.XPATH, '//body')  # 详情输入框
        self.clear_input_enter(self.input_title, value['title'])  # 输入标题
        value_ = self.publish_get_info(publish_date, t=('publish_date',))[0]
        value.update(value_)
        self.switch_to_frame(detail_frame)
        self.clear_input_enter(detail_input, value['detail'])  # 输入详情
        self.switch_to_frame_back()
        return value

    @allure.step('修改规章制度标题')
    def change_rule_title(self, new_title=randomTool.random_str()):
        self.clear_then_input(self.input_title, new_title)
        self.poll_click(self.save_btn)
        self.switch_to_handle(index=-2)
        time.sleep(2.5)
        return new_title

    @allure.step('新增规章制度')
    def add_rule(self, **kwargs):
        value = self.edit_rule(**kwargs)
        self.poll_click(self.save_btn)
        time.sleep(1)
        self.switch_to_handle(index=-2)
        time.sleep(2.5)
        return value
