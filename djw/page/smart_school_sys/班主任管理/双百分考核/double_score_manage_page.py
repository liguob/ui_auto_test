# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/16    14:37
============================
"""
from time import sleep

import allure
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class DoubleScorePage(BasePage):
    # _top_frame = (By.CSS_SELECTOR, 'iframe[src*="classTab.html"]')  # 班次顶层frame
    # _current_class_frame = (By.CSS_SELECTOR, 'iframe[src*="type=1"]')  # 当前班次frame
    # _feature_class_frame = (By.CSS_SELECTOR, 'iframe[src*="type=0"]')  # 未开始frame
    # _history_class_frame = (By.CSS_SELECTOR, 'iframe[src*="type=2"]')  # 未开始frame

    @allure.step("切换到历史班次")
    def switch_to_history_class(self):
        """进入历史班次界面"""
        click_btn = (By.XPATH, '//div[@role="tablist"]//span[contains(text(),"历史班次")]')  # 历史班次页签按钮
        self.excute_js_click(click_btn)
        sleep(1)  # 切换班次类型短暂数据刷新时间
        return self

    @allure.step("切换到未开始班次")
    def switch_to_feature_class(self):
        """进入未开始班次界面"""
        click_btn = (By.XPATH, '//div[@role="tablist"]//span[contains(text(),"未开始班次")]')  # 未开始班次页签按钮
        self.excute_js_click(click_btn)
        sleep(2)  # 切换班次类型短暂数据刷新时间
        return self

    @allure.step("查询班次")
    def search_class(self, class_name):
        """查询班次"""
        search_input = (By.CSS_SELECTOR, 'div[role=tabpanel]:not([aria-hidden]) input[placeholder="班次名称"]')  # 查询输入框
        self.clear_and_input_enter(search_input, class_name)
        sleep(1)
        return self

    @allure.step("进入双百分详情页面")
    def go_score_details(self, class_name):
        """查询班次，并进入班次的双百分详情界面"""
        self.search_class(class_name)
        # 对应班次的详情页面
        details_btn = (By.CSS_SELECTOR, 'div[role=tabpanel]:not([aria-hidden]) div.is-scrolling-none [title="详情"]>i')
        self.excute_js_click(details_btn)
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.班主任管理.双百分考核.double_score_details_page import DoubleScoreDetailsPage
        return DoubleScoreDetailsPage(self.driver)
