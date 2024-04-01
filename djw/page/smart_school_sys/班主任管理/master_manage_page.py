# -*- coding: utf-8 -*-
import allure
from djw.page.smart_school_sys.主页.home_page import HomePage


class MasterManagePage(HomePage):
    """班主任管理页面类"""

    @allure.step('进入学员管理-班级课表')
    def go_class_schedules(self):
        self.locator_left_menu_click(button_title='班级课表')
        from djw.page.smart_school_sys.班主任管理.班级课表.class_schedules import ClassSchedules
        return ClassSchedules(driver=self.driver)

    @allure.step('进入学员管理-照片审核')
    def go_photos_check(self):
        self.locator_left_menu_click(button_title='照片审核')
        from djw.page.smart_school_sys.班主任管理.照片审核.photos_check import PhotosCheck
        self.wait_presence_list_data(explicit_timeout=15)
        return PhotosCheck(driver=self.driver)

    @allure.step('进入学员管理-健康情况')
    def go_health_condition(self):
        self.locator_left_menu_click(menu_title='学前管理', button_title='健康情况')
        from djw.page.smart_school_sys.班主任管理.健康情况.health_condition import HealthCondition
        return HealthCondition(driver=self.driver)

    @allure.step('进入学员管理-健康报告')
    def go_health_report(self):
        self.locator_left_menu_click(button_title='健康报告', times=1)
        from djw.page.smart_school_sys.班主任管理.健康管理.health_report import HealthReportPage
        return HealthReportPage(driver=self.driver)

    @allure.step('进入学员管理-外出报备')
    def go_out_report(self):
        self.locator_left_menu_click(button_title='外出报备', times=1)
        from djw.page.smart_school_sys.班主任管理.健康管理.out_report import OutReportPage
        return OutReportPage(driver=self.driver)

    @allure.step('进入学员管理-学员管理')
    def go_stu_manage_page(self):
        self.locator_left_menu_click(button_title='学员管理')
        from djw.page.smart_school_sys.班主任管理.学员管理.stu_manage_page import StuManagePage
        return StuManagePage(driver=self.driver)

    @allure.step('进入学员管理-班级公告')
    def go_class_notice(self):
        self.locator_left_menu_click(button_title='班级公告')
        from djw.page.smart_school_sys.班主任管理.班级公告.class_notice import ClassNotice
        return ClassNotice(driver=self.driver)

    @allure.step('进入学员管理-座位安排')
    def go_seating_arrangement_page(self):
        self.locator_left_menu_click(button_title='座位安排', menu_title='学前管理')
        from djw.page.smart_school_sys.班主任管理.座位安排.seating_arrangements_page import SeatingArrangementsPage
        return SeatingArrangementsPage(driver=self.driver)

    @allure.step("进入学员管理-班级通讯录")
    def go_class_contact_page(self):
        self.locator_left_menu_click(button_title='班级通讯录')
        from djw.page.smart_school_sys.班主任管理.班级通讯录.class_contact_manage_page import ClassContactManagePage
        return ClassContactManagePage(driver=self.driver)

    @allure.step("进入学员管理-退学管理")
    def go_drop_manage(self):
        self.locator_left_menu_click(button_title='退学审核')
        from djw.page.smart_school_sys.班主任管理.退学管理.drop_manage_page import DropManagePage
        return DropManagePage(driver=self.driver)

    @allure.step("进入学员管理-退学统计")
    def go_drop_count(self):
        self.locator_left_menu_click(button_title='退学统计')
        from djw.page.smart_school_sys.班主任管理.退学统计.drop_count_page import DropCountPage
        return DropCountPage(driver=self.driver)

    @allure.step("进入学员管理-双百分考核")
    def go_double_score(self):
        self.locator_left_menu_click(button_title='双百分考核')
        from djw.page.smart_school_sys.班主任管理.双百分考核.double_score_manage_page import DoubleScorePage
        return DoubleScorePage(driver=self.driver)

    @allure.step("进入学员管理-请假管理")
    def go_leave_manage(self):
        self.locator_left_menu_click(button_title='请假审核')
        from djw.page.smart_school_sys.班主任管理.请假管理.pc_leave_manage import PcLeaveManage
        return PcLeaveManage(driver=self.driver)

    @allure.step('进入学员管理-班委库')
    def go_class_committee_page(self):
        self.locator_left_menu_click(button_title='班委库')
        from djw.page.smart_school_sys.班主任管理.班委库.class_committee_library_manage_page import ClassCommitteeLibraryPage
        return ClassCommitteeLibraryPage(driver=self.driver)

    @allure.step('进入学员管理-两带来提交情况')
    def go_master_two_bring_page(self):
        self.locator_left_menu_click(button_title='两带来提交情况', menu_title='学前管理')
        from djw.page.smart_school_sys.班主任管理.两带来.two_bring_page import TwoBringManagePage
        return TwoBringManagePage(self.driver)

    @allure.step('进入意见建议回复')
    def go_suggestion_reply_page(self):
        self.locator_left_menu_click(button_title='意见建议回复')
        from djw.page.smart_school_sys.对外培训.意见建议回复.suggestion_view import SuggestionReply
        return SuggestionReply(self.driver)
