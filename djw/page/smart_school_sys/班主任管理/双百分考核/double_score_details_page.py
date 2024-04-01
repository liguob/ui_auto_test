# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/5/27    10:14
============================
"""
from time import sleep
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class DoubleScoreDetailsPage(BasePage):
    top_frame = (By.CSS_SELECTOR, 'iframe[src*="teaAssessmentList.html"]')  # 页面顶层frame
    save_btn = (By.CSS_SELECTOR, 'a[ds-event=system_form_save]')  # 成绩编辑界面保存按钮
    edit_title = (By.CSS_SELECTOR, 'div.layui-layer-title')  # 编辑信息主题

    def __switch_top_frame(self):
        self.switch_to_frame_back()
        self.switch_to_frame(self.top_frame)

    def __edit_score(self, stu_name, data: dict):
        """编辑学员的分数"""
        keys = data.keys()
        self.__switch_top_frame()
        edit_btn = (By.XPATH, '//div[text()="{}"]//ancestor::tr//a[text()="编辑"]'.format(stu_name))  # 学员名称对应编辑
        edit_frame = (By.CSS_SELECTOR, 'iframe[src*="edit.html"]')  # 编辑成绩frame
        self.move_to_click(edit_btn)
        sleep(2)
        self.switch_to_frame(edit_frame)
        if "类别" in keys:
            click_btn = (By.CSS_SELECTOR, 'input.layui-unselect')  # 点击输入框弹出选项
            select_type = (By.XPATH, '//dd[text()="{}"]'.format(data["类别"]))
            self.excute_js_click(click_btn)
            self.excute_js_click(select_type)
        if "加减" in keys:
            score_operate_btn = (By.XPATH, '//div[text()="{}"]'.format(data["加减"]))  # 加减类型选择
            self.excute_js_click(score_operate_btn)
        if "分数" in keys:
            score_input = (By.CSS_SELECTOR, 'div[caption=score] input')  # 分数输入框
            self.find_elem(score_input).send_keys(data["分数"])
        if "原因" in keys:
            reason_input = (By.CSS_SELECTOR, 'div[caption=reason] textarea')  # 原因输入框
            self.find_elem(reason_input).send_keys(data["原因"])

    @allure.step("修改双百分成绩")
    def edit_score(self, stu_name, data: dict):
        """修改成绩成功"""
        self.__edit_score(stu_name, data)
        self.excute_js_click(self.save_btn)
        sleep(2)
        return self

    @allure.step("修改双百分成绩失败校验")
    def edit_score_fail(self, stu_name, data: dict):
        """修改成绩失败，返回提示信息"""
        info_ele = (By.CSS_SELECTOR, 'p.el-message__content')  # 提示信息元素
        self.__edit_score(stu_name, data)
        self.excute_js_click(self.save_btn)
        self.switch_to_frame_back()
        return self.trim_text(info_ele)

    def __get_key_index(self, score_type):
        """获取成绩类型的顺序，返回对应的data-key"""
        key_ele = (By.XPATH, '//span[text()="{}"]/ancestor::th'.format(score_type))  # 成绩类型所在元素
        return self.find_elem(key_ele).get_attribute("data-key")

    @allure.step("获取双百分成绩")
    def get_score(self, stu_name, score_type):
        """获取对应学员对应成绩类型的得分"""
        self.__switch_top_frame()
        index = self.__get_key_index(score_type)
        score_ele = (By.XPATH, '//div[text()="{}"]/ancestor::tr//td[@data-key="{}"]//div'.format(stu_name, index))
        return float(self.find_elem(score_ele).text)
