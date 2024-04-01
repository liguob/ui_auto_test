"""
============================
Author:杨德义
============================
"""
import time
import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.主页.home_page import HomePage


class LogisticsManagePage(HomePage):
    """后勤管理页面类"""

    @allure.step('进入网上报修-网上报修')
    def go_maintain_apply(self):
        self.locator_left_menu_click(menu_title='网上报修', button_title='网上报修')
        from djw.page.smart_school_sys.后勤管理.网上报修.网上报修.maintain_apply import MaintainApply
        self.wait_presence_list_data(explicit_timeout=15)
        return MaintainApply(driver=self.driver)

    @allure.step('进入网上报修-班主任网上报修')
    def go_headmaster_maintain(self):
        self.locator_left_menu_click(menu_title='网上报修', button_title='班主任网上报修')
        from djw.page.smart_school_sys.后勤管理.网上报修.班主任网上报修.headmaster_maintain import HeadmasterMaintain
        return HeadmasterMaintain(driver=self.driver)

    @allure.step('进入网上报修-报修审核')
    def go_maintain_check(self):
        self.locator_left_menu_click(button_title='报修审核')
        from djw.page.smart_school_sys.后勤管理.网上报修.报修审核.maintain_check import MaintainCheck
        self.wait_presence_list_data(explicit_timeout=15)
        return MaintainCheck(driver=self.driver)

    @allure.step('进入网上报修-报修记录')
    def go_maintain_history(self):
        self.locator_left_menu_click(button_title='报修记录')
        from djw.page.smart_school_sys.后勤管理.网上报修.报修记录.maintain_history import MaintainHistory
        self.wait_presence_list_data(explicit_timeout=15)
        return MaintainHistory(driver=self.driver)

    @allure.step('进入用餐管理-一周菜单(操作)')
    def go_week_menu_handle(self):
        loc = (By.CSS_SELECTOR, '[ctrl_type="dsf.virtualscroll"] [title="一周菜单"]')
        self.excute_js_click_ele(self.find_elms(loc)[0])
        time.sleep(0.5)
        self.wait_presence_list_data()
        from djw.page.smart_school_sys.后勤管理.用餐管理.一周菜单操作.week_menu_handle import WeekMenuHandle
        return WeekMenuHandle(driver=self.driver)

    @allure.step('进入用餐管理-一周菜单(查看)')
    def go_week_menu_view(self):
        loc = (By.CSS_SELECTOR, '[ctrl_type="dsf.virtualscroll"] [title="一周菜单"]')
        self.excute_js_click_ele(self.find_elms(loc)[1])
        time.sleep(0.5)
        self.wait_presence_list_data()
        from djw.page.smart_school_sys.后勤管理.用餐管理.一周菜单查看.week_menu_view import WeekMenuView
        return WeekMenuView(driver=self.driver)

    @allure.step('进入用餐管理-对外班次用餐申请')
    def go_out_class_dinner_apply(self):
        self.locator_left_menu_click(menu_title='用餐管理', button_title='对外班次用餐申请')
        from djw.page.smart_school_sys.后勤管理.用餐管理.对外班次用餐申请.out_class_dinner_apply import OutClassDinnerApply
        return OutClassDinnerApply(driver=self.driver)

    @allure.step('进入用餐管理-对外班次用餐审核')
    def go_out_class_dinner_check(self):
        self.locator_left_menu_click(menu_title='用餐管理', button_title='对外班次用餐审核')
        from djw.page.smart_school_sys.后勤管理.用餐管理.对外班次用餐审核.out_class_dinner_check import OutClassDinnerCheck
        return OutClassDinnerCheck(driver=self.driver)

    @allure.step('进入用餐管理-校外人员用餐申请')
    def go_out_person_dinner_apply(self):
        self.locator_left_menu_click(menu_title='用餐管理', button_title='校外人员用餐申请')
        from djw.page.smart_school_sys.后勤管理.用餐管理.校外人员用餐申请.out_person_dinner_apply import OutPersonDinnerApply
        return OutPersonDinnerApply(driver=self.driver)

    @allure.step('进入用餐管理-校外人员用餐管理')
    def go_out_person_dinner_check(self):
        self.locator_left_menu_click(menu_title='用餐管理', button_title='校外人员用餐审核')
        from djw.page.smart_school_sys.后勤管理.用餐管理.校外人员用餐审核.out_person_dinner_check import OutPersonDinnerCheck
        return OutPersonDinnerCheck(driver=self.driver)

    @allure.step('进入用餐管理-校外人员用餐审核')
    def go_dinner_summary(self):
        self.locator_left_menu_click(menu_title='用餐管理', button_title='用餐统计')
        from djw.page.smart_school_sys.后勤管理.用餐管理.用餐统计.dinner_summary import DinnerSummary
        return DinnerSummary(driver=self.driver)

    @allure.step('进入场地管理-场地申请')
    def go_site_apply(self):
        self.locator_left_menu_click(menu_title='场地管理', button_title='场地申请')
        from djw.page.smart_school_sys.后勤管理.场地管理.场地申请.site_apply import SiteApply
        return SiteApply(driver=self.driver)

    @allure.title('进入场地管理-场地审核')
    def go_site_check(self):
        self.locator_left_menu_click(menu_title='场地管理', button_title='场地审核')
        from djw.page.smart_school_sys.后勤管理.场地管理.场地审核.site_check import SiteCheck
        return SiteCheck(driver=self.driver)

    @allure.title('进入场地管理-场地统计')
    def go_site_summary(self):
        self.locator_left_menu_click(menu_title='场地管理', button_title='场地统计')
        from djw.page.smart_school_sys.后勤管理.场地管理.场地统计.site_summary import SiteSummary
        return SiteSummary(driver=self.driver)

    @allure.step('进入车辆管理-车辆列表')
    def go_cars_list(self):
        self.locator_left_menu_click(menu_title='车辆管理', button_title='车辆列表')
        from djw.page.smart_school_sys.后勤管理.车辆管理.车辆列表.cars_list import CarsList
        return CarsList(driver=self.driver)

    @allure.step('进入车辆管理-车辆使用情况')
    def go_cars_use_info(self):
        self.locator_left_menu_click(menu_title='车辆管理', button_title='车辆使用情况')
        from djw.page.smart_school_sys.后勤管理.车辆管理.车辆使用情况.car_use_info import CarUseInfo
        return CarUseInfo(driver=self.driver)

    @allure.step('进入车辆管理-用车申请')
    def go_cars_apply(self):
        self.locator_left_menu_click(menu_title='车辆管理', button_title='用车申请')
        from djw.page.smart_school_sys.后勤管理.车辆管理.用车申请.car_apply import CarApply
        return CarApply(driver=self.driver)

    @allure.step('进入车辆管理-用车审核')
    def go_cars_review(self):
        self.locator_left_menu_click(menu_title='车辆管理', button_title='用车审核')
        from djw.page.smart_school_sys.后勤管理.车辆管理.用车审核.car_apply_review import CarApplyReview
        return CarApplyReview(driver=self.driver)

    @allure.step('进入会议管理-会议管理')
    def go_meeting_manage(self):
        self.locator_left_menu_click(menu_title='会议管理', button_title='会议管理')
        from djw.page.smart_school_sys.后勤管理.会议管理.会议管理.meeting_manage import MeetingManage
        return MeetingManage(driver=self.driver)

    @allure.step('进入会议管理-会议考勤')
    def go_meeting_attendance(self):
        self.locator_left_menu_click(menu_title='会议管理', button_title='会议考勤')
        from djw.page.smart_school_sys.后勤管理.会议管理.会议考勤.meeting_attendance import MeetingAttendance
        return MeetingAttendance(driver=self.driver)

    @allure.step('进入会议管理-我的会议')
    def go_my_meeting(self):
        self.locator_left_menu_click(menu_title='会议管理', button_title='我的会议')
        from djw.page.smart_school_sys.后勤管理.会议管理.我的会议.my_meeting import MyMeeting
        return MyMeeting(driver=self.driver)

    @allure.step('进入会议管理-会议纪要')
    def go_meeting_minutes(self):
        self.locator_left_menu_click(menu_title='会议管理', button_title='会议纪要')
        from djw.page.smart_school_sys.后勤管理.会议管理.会议纪要.meeting_minutes import MeetingMinutes
        return MeetingMinutes(driver=self.driver)

    @allure.step('进入会议管理-会议保障')
    def go_meeting_support(self):
        self.locator_left_menu_click(menu_title='会议管理', button_title='会议保障')
        from djw.page.smart_school_sys.后勤管理.会议管理.会议保障.meeting_support import MeetingSupport
        return MeetingSupport(driver=self.driver)
