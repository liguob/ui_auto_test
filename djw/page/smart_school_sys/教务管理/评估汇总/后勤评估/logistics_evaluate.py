"""
============================
Author: 何凯 0519 重构
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class LogisticsEvaluationPage(BasePage):
    """后勤评价汇总页面"""

    @allure.step("查询班次")
    def search_class(self, value):
        self.locator_tag_search_input("请输入班次名称", value)
        self.locator_tag_search_button()
        return self

    @allure.step('进入后勤评价详情')
    def into_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待数据加载
        return self

    @allure.step('进入单项评价详情学员列表')
    def go_stu_detail(self):
        """点击任意一个非0值的项，进入学员评价列表"""
        evaluation_value = (By.CSS_SELECTOR, '[class=appritem]')
        elem = self.find_elms(evaluation_value)
        for i in elem:
            if int(i.text) > 0:
                self.excute_js_click_ele(i)
                break
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.评估汇总.后勤评估.stu_evaluation_detail import StuEvaluationDetail
        return StuEvaluationDetail(self.driver)
