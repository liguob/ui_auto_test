# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/6 16:04
# Author     ：李国彬
============================
"""
import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class OutTrainingPage(HomePage):
    """对外培训"""

    @allure.step('进入对外培训-调课记录')
    def go_transfer_records(self):
        self.locator_left_menu_click(button_title='调课记录')
        from djw.page.smart_school_sys.教务管理.教学管理.调课记录.transfer_arranged_records import TransferArrangedRecords
        return TransferArrangedRecords(self.driver)

    @allure.step('进入对外培训-一周课表')
    def go_week_schedules(self):
        self.locator_left_menu_click(button_title='一周课表')
        from djw.page.smart_school_sys.教务管理.教学管理.一周课表.week_schedules import WeekSchedules
        return WeekSchedules(self.driver)

    @allure.step('进入对外培训-教学计划')
    def go_teach_plans(self):
        self.locator_left_menu_click(button_title='教学计划')
        from djw.page.smart_school_sys.教务管理.教学管理.教学计划.teach_plan_page import TeachPlanPage
        return TeachPlanPage(self.driver)

    @allure.step('进入对外培训-经费管理')
    def go_funds_manage(self):
        self.locator_left_menu_click(button_title='经费管理')
        from djw.page.smart_school_sys.对外培训.经费管理.funds_manage import FundsManage
        return FundsManage(self.driver)

    @allure.step('进入对外培训-经费汇总')
    def go_funds_summary(self):
        self.locator_left_menu_click(button_title='经费汇总')
        from djw.page.smart_school_sys.对外培训.经费汇总.funds_summary import FundsSummary
        return FundsSummary(self.driver)

    @allure.step('进入对外培训-班次管理')
    def go_out_class_manage_page(self):
        self.locator_left_menu_click(button_title='班次管理')
        from djw.page.smart_school_sys.对外培训.班次管理.out_training_class_manage_page import OutTrainingClassManagePage
        return OutTrainingClassManagePage(self.driver)

    @allure.step('进入对外培训-排课管理')
    def go_arrange_manage(self):
        self.locator_left_menu_click(button_title='排课管理')
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_class_page import ArrangeClassPage
        return ArrangeClassPage(self.driver)

    @allure.step('进入对外培训-意见建议统计')
    def go_suggestion_view_page(self):
        self.locator_left_menu_click(button_title='意见建议统计')
        from djw.page.smart_school_sys.对外培训.意见建议统计.suggestion_statics import SuggestionStatics
        return SuggestionStatics(self.driver)

    @allure.step('进入对外培训-意见建议回复')
    def go_suggestion_reply_page(self):
        self.locator_left_menu_click(button_title='意见建议回复')
        from djw.page.smart_school_sys.对外培训.意见建议回复.suggestion_view import SuggestionReply
        return SuggestionReply(self.driver)

    @allure.step('进入评估汇总-课程评估')
    def go_course_evaluation_sum_page(self):
        self.locator_left_menu_click(button_title="课程评估", menu_title='评估汇总')
        from djw.page.smart_school_sys.教务管理.评估汇总.课程评估.course_evaluation_manage import CourseEvaluationSumPage
        return CourseEvaluationSumPage(self.driver)

    @allure.step("进入评估汇总-后勤评估")
    def go_logistics_evaluation_page(self):
        self.locator_left_menu_click(button_title="后勤评估", menu_title='评估汇总')
        from djw.page.smart_school_sys.对外培训.评估管理.后勤评估.out_class_logistics_evaluate import \
            OutClassLogisticsEvaluationPage
        return OutClassLogisticsEvaluationPage(self.driver)

    @allure.step("进入评估汇总->班次评估")
    def go_class_evaluation_page(self):
        self.locator_left_menu_click(button_title="班次评估", menu_title='评估汇总')
        from djw.page.smart_school_sys.对外培训.评估管理.班次评估.out_class_evaluation_manage import OutClassEvaluationManage
        return OutClassEvaluationManage(self.driver)
