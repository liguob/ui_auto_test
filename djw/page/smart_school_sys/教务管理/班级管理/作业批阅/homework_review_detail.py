# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *


class HomeworkReviewDetail(BasePage):
    """作业批阅详情页面"""

    @allure.step('批阅等级制作业')
    def review_homework(self, name, data: dict):
        with allure.step(f'批阅{data["作业类型"]}作业'):
            self.locator_view_select(id_value=name)
            self.locator_button(button_title='批阅')
            time.sleep(1)
            if data['作业类型'] == '等级制':
                # 默认等级为优秀
                pass
            if data['作业类型'] == '分数制':
                self.clear_and_input((By.CSS_SELECTOR, 'input[placeholder="分数"]'), data['成绩'])
            if data['作业类型'] == '存档制':
                pass
            self.clear_and_input((By.CSS_SELECTOR, 'textarea[placeholder="请输入内容"]'), data['评语'])
            # self.find_elem((By.CSS_SELECTOR, 'textarea[placeholder="请输入内容"]')).send_keys(data['评语'])
        time.sleep(1)
        self.locator_dialog_btn(btn_name='下一篇')
        self.locator_dialog_btn(btn_name='确定')
        time.sleep(2)  # 等待页面刷新数据

    @allure.step('下载作业')
    def download_homework(self, file_name):
        self.locator_button(button_title='下载全部作业')
        return wait_file_down_and_clean(file_name)

    @allure.step('提交批阅作业结果')
    def submit_review(self, name):
        self.locator_view_select(id_value=name)
        self.locator_button(button_title='提交')
        self.wait_success_tip()
        return self
