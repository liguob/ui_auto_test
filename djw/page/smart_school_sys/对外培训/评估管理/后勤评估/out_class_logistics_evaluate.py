# coding: utf-8
"""
============================
# Time      ：2022/5/24 9:25
# Author    ：李国彬
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.教务管理.评估汇总.后勤评估.logistics_evaluate import LogisticsEvaluationPage


class OutClassLogisticsEvaluationPage(LogisticsEvaluationPage):
    """后勤评估"""

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
        from djw.page.smart_school_sys.对外培训.评估管理.后勤评估.out_class_stu_evaluation_detail import OutClassStuEvaluationDetail
        return OutClassStuEvaluationDetail(self.driver)
