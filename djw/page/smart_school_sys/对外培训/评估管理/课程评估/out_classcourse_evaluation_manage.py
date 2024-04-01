# coding: utf-8
"""
============================
# Time      ：2022/5/24 9:42
# Author    ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.教务管理.评估汇总.课程评估.course_evaluation_manage import CourseEvaluationSumPage


class OutClassCourseEvaluationSumPage(CourseEvaluationSumPage):
    """课程评估"""
    @allure.step('进入课程评价详情')
    def go_evaluate_info(self, name):
        self.locator_view_button(button_title='课程评价', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.对外培训.评估管理.课程评估.课程评价.out_class_course_evaluation_detail import \
            OutClassCourseEvaluationDetail
        return OutClassCourseEvaluationDetail(self.driver)