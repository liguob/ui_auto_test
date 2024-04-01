# encoding=utf-8
import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.主页.home_page import HomePage


class EduManagePage(HomePage):
    """教务管理页面类"""

    @allure.step('进入教务管理-班级相册')
    def go_class_albums(self):
        self.locator_left_menu_click(button_title='班级相册')
        from djw.page.smart_school_sys.教务管理.班级相册.class_albums import ClassAlbums
        return ClassAlbums(driver=self.driver)

    @allure.step('进入教学管理-教学计划模板')
    def go_teach_plan_moulds(self):
        self.locator_left_menu_click(menu_title='教学管理', button_title='教学计划模板')
        from djw.page.smart_school_sys.教务管理.教学管理.教学计划模板.teach_plan_moulds import TeachPlanMoulds
        return TeachPlanMoulds(driver=self.driver)

    @allure.step("进入教学管理-教学计划")
    def go_teach_plan(self):
        self.locator_left_menu_click(menu_title='教学管理', button_title='教学计划')
        from djw.page.smart_school_sys.教务管理.教学管理.教学计划.teach_plan_page import TeachPlanPage
        return TeachPlanPage(driver=self.driver)

    @allure.step('进入教务管理-教学管理-排课管理')
    def go_arrang_manage(self):
        self.locator_left_menu_click(menu_title='教学管理', button_title='排课管理')
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_class_page import ArrangeClassPage
        self.wait_presence_list_data()
        return ArrangeClassPage(driver=self.driver)

    @allure.step('进入教学管理-一周课表')
    def go_week_schedules(self):
        self.locator_left_menu_click(menu_title='教学管理', button_title='一周课表')
        from djw.page.smart_school_sys.教务管理.教学管理.一周课表.week_schedules import WeekSchedules
        return WeekSchedules(driver=self.driver)

    @allure.step('进入教务管理-我的课表')
    def go_my_schedules(self):
        self.locator_left_menu_click(button_title='我的课表')
        from djw.page.smart_school_sys.教务管理.我的课表.my_schedules import MySchedules
        return MySchedules(driver=self.driver)

    @allure.step('进入教学管理-调课记录')
    def go_transfer_arranged_records(self):
        self.locator_left_menu_click(menu_title='教学管理', button_title='调课记录')
        from djw.page.smart_school_sys.教务管理.教学管理.调课记录.transfer_arranged_records import TransferArrangedRecords
        return TransferArrangedRecords(driver=self.driver)

    @allure.step('进入教务管理-纪律承诺')
    def go_discipline_promise_page(self):
        self.locator_left_menu_click(button_title='纪律承诺')
        from djw.page.smart_school_sys.教务管理.纪律承诺.discipline_promise import DisciplinePromise
        return DisciplinePromise(driver=self.driver)

    @allure.step("进入教务管理-班次管理")
    def go_class_manage_page(self):
        self.locator_left_menu_click(button_title='班次管理')
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.class_manage_main_page import ClassMangeMainPage
        return ClassMangeMainPage(self.driver)

    @allure.step('进入教务管理-教学资料')
    def go_teach_resource(self):
        self.locator_left_menu_click(button_title='教学资料')
        from djw.page.smart_school_sys.教务管理.班级管理.教学资料.resources_material_page import ResourcesMaterialPage
        return ResourcesMaterialPage(self.driver)

    @allure.step('进入教务管理-学籍信息查询')
    def go_schoolroll_query(self):
        self.locator_left_menu_click(button_title='学籍信息查询')
        from djw.page.smart_school_sys.教务管理.学籍信息查询.schoolroll_query import SchoolrollQuery
        self.wait_presence_list_data(explicit_timeout=10)
        return SchoolrollQuery(driver=self.driver)

    @allure.step('进入教务管理-证书管理-毕业证书')
    def go_certificate_print_page(self):
        self.locator_left_menu_click(button_title='毕业证书', menu_title='证书管理')
        from djw.page.smart_school_sys.教务管理.证书管理.毕业证书.certificate_print_main_page import CertificatePrintingMainPage
        return CertificatePrintingMainPage(self.driver)

    @allure.step('进入教务管理-证书管理-证书模板')
    def go_certificate_template_page(self):
        self.locator_left_menu_click(button_title='证书模板', menu_title='证书管理')
        from djw.page.smart_school_sys.教务管理.证书管理.证书模板.certificate_template_page import CertificateTemplatePage
        return CertificateTemplatePage(self.driver)

    @allure.step('进入教务管理-证书管理-其他证书')
    def go_other_certificate_manage_page(self):
        self.locator_left_menu_click(button_title='其他证书', menu_title='证书管理')
        from djw.page.smart_school_sys.教务管理.证书管理.其他证书.other_certificate_main_page import OtherCertificateMainPage
        return OtherCertificateMainPage(self.driver)

    @allure.step('进入教学设置-校历设置')
    def go_school_calendar_setting(self):
        self.locator_left_menu_click(menu_title='教学设置', button_title='校历设置')
        from djw.page.smart_school_sys.教务管理.教学设置.校历设置.school_calendar_setting import SchoolCalendarSetting
        return SchoolCalendarSetting(driver=self.driver)

    @allure.step("进入作业管理-成绩登记")
    def go_edu_grading_page(self):
        self.locator_left_menu_click(menu_title='作业管理', button_title='成绩登记')
        from djw.page.smart_school_sys.教务管理.作业管理.成绩登记.grading_page import GradingPage
        return GradingPage(self.driver)

    @allure.step("进入个人网报-二维码管理")
    def go_qr_code_page(self):
        self.locator_left_menu_click(button_title="二维码管理", menu_title='个人网报')
        from djw.page.smart_school_sys.教务管理.个人网报.二维码管理.qr_code_network_report import QrCodeNetworkReport
        return QrCodeNetworkReport(self.driver)

    @allure.step("进入个人网报-审核管理")
    def go_qr_code_check_page(self):
        self.locator_left_menu_click(button_title="网报审核", menu_title='个人网报')
        from djw.page.smart_school_sys.教务管理.个人网报.审核管理.class_check_manage import ClassCheckManage
        return ClassCheckManage(self.driver)

    @allure.step('进入评估汇总-课程评估')
    def go_course_evaluation_sum_page(self):
        self.locator_left_menu_click(button_title="课程评估", menu_title='评估汇总')
        from djw.page.smart_school_sys.教务管理.评估汇总.课程评估.course_evaluation_manage import CourseEvaluationSumPage
        return CourseEvaluationSumPage(self.driver)

    @allure.step("进入评估汇总-后勤评估")
    def go_logistics_evaluation_page(self):
        self.locator_left_menu_click(button_title="后勤评估", menu_title='评估汇总')
        from djw.page.smart_school_sys.教务管理.评估汇总.后勤评估.logistics_evaluate import LogisticsEvaluationPage
        return LogisticsEvaluationPage(self.driver)

    @allure.step("进入评估汇总->班次评估")
    def go_class_evaluation_page(self):
        self.locator_left_menu_click(button_title="班次评估", menu_title='评估汇总')
        from djw.page.smart_school_sys.教务管理.评估汇总.班次评估.class_evaluation_manage import ClassEvaluationManage
        return ClassEvaluationManage(self.driver)

    @allure.step("进入教务管理-退学管理")
    def go_edu_drop_manage(self):
        self.locator_left_menu_click(button_title="退学审核")
        from djw.page.smart_school_sys.教务管理.退学管理.edu_drop_manage_page import EduDropManagePage
        return EduDropManagePage(self.driver)

    @allure.step("进入教务管理-班级公告")
    def go_edu_class_notice(self):
        self.locator_left_menu_click(button_title='班级公告')
        from djw.page.smart_school_sys.班主任管理.班级公告.class_notice import ClassNotice
        return ClassNotice(self.driver)

    @allure.step("进入教务管理-评估查看-我的评估")
    def go_my_evaluation(self):
        self.locator_left_menu_click(menu_title='评估查看', button_title='我的评估')
        from djw.page.smart_school_sys.教务管理.教学评价管理.我的评估.my_evaluation_main_page import MyEvaluationMainPage
        return MyEvaluationMainPage(self.driver)

    @allure.step("进入教务管理-考勤管理")
    def go_attendance_manage(self):
        self.locator_left_menu_click(button_title='考勤管理', menu_title='考勤管理')
        from djw.page.smart_school_sys.教务管理.考勤管理.attendance_manage_main_page import AttendanceManagePage
        return AttendanceManagePage(self.driver)

    @allure.step("进入教务管理-请假审核")
    def go_edu_leave_audit(self):
        self.locator_left_menu_click(menu_title='班级管理', button_title='请假审核')
        from djw.page.smart_school_sys.教务管理.班级管理.请假管理.pc_edu_leave_manage_page import PcEduLeaveManagePage
        return PcEduLeaveManagePage(driver=self.driver)

    @allure.step('进入教务管理-请假统计')
    def go_edu_leave_summary(self):
        self.locator_left_menu_click(menu_title='综合统计', button_title='请假统计')
        from djw.page.smart_school_sys.教务管理.请假统计.leave_summary import LeaveSummary
        return LeaveSummary(self.driver)

    @allure.step('进入教务管理-退学统计')
    def go_edu_drop_summary(self):
        self.locator_left_menu_click(menu_title='综合统计', button_title='退学统计')
        from djw.page.smart_school_sys.教务管理.退学统计.edu_drop_summary import EduDropSummary
        return EduDropSummary(driver=self.driver)

    @allure.step('进入教务管理-学时统计')
    def go_period_summary(self):
        self.locator_left_menu_click(menu_title='综合统计', button_title='学时统计')
        from djw.page.smart_school_sys.教务管理.综合统计.学时统计.period_summary import PeriodSummary
        return PeriodSummary(driver=self.driver)

    @allure.step('进入教务管理-新专题申报')
    def go_new_subject_apply_page(self):
        self.locator_left_menu_click(button_title='新专题申报', menu_title='新专题管理', times=4)
        from djw.page.smart_school_sys.教务管理.新专题管理.新专题申报.new_subject_apply_manage_page import NewSubjectApplyPage
        return NewSubjectApplyPage(driver=self.driver)

    @allure.step('进入教务管理-新专题审批')
    def go_new_subject_review_page(self):
        self.locator_left_menu_click(button_title='新专题审批', menu_title='新专题管理')
        from djw.page.smart_school_sys.教务管理.新专题管理.新专题审批.new_subject_review_manage_page import NewSubjectReviewPage
        return NewSubjectReviewPage(driver=self.driver)

    @allure.step('进入教务管理-新专题入库')
    def go_new_subject_in_storage_page(self):
        self.locator_left_menu_click(button_title='新专题入库', menu_title='新专题管理')
        from djw.page.smart_school_sys.教务管理.新专题管理.新专题入库.new_subject_in_storeage_manage_page import \
            NewSubjectInStoragePage
        return NewSubjectInStoragePage(driver=self.driver)

    @allure.step('进入教务管理-专题试讲-专家库')
    def go_experts_library(self):
        self.locator_left_menu_click(button_title='专家库')
        from djw.page.smart_school_sys.教务管理.新专题管理.专家库.expert_lib_manage_page import ExpertLibManagePage
        return ExpertLibManagePage(driver=self.driver)

    @allure.step('进入教务管理-专题试讲-集体备课试讲')
    def go_group_interview(self):
        self.locator_left_menu_click(button_title='集体备课试讲')
        from djw.page.smart_school_sys.教务管理.新专题管理.集体备课试讲.prepare_trial_lecture_manage_page import \
            PrepareTrialLectureManagePage
        return PrepareTrialLectureManagePage(driver=self.driver)

    @allure.step('进入教务管理-网报通知书管理')
    def go_notice_report_manage_page(self):
        self.locator_left_menu_click(button_title='网报通知书管理')
        from djw.page.smart_school_sys.教务管理.班级管理.网报通知书管理.notice_report_manage_page import NoticeReportManagePage
        return NoticeReportManagePage(driver=self.driver)

    @allure.step('进入教学设置-考勤规则设置')
    def go_submenu_teaching_set_page(self):
        self.locator_left_menu_click(menu_title='教学设置', button_title='考勤规则设置')
        from djw.page.smart_school_sys.教务管理.教学设置.考勤设置.attend_rule_setting_page import AttendRuleSettingPage
        return AttendRuleSettingPage(self.driver)

    @allure.step('进入教学设置-主体班评估时限设置')
    def go_main_class_time_limit_page(self):
        self.locator_left_menu_click(menu_title='教学设置', button_title='主体班评估时限设置')
        from djw.page.smart_school_sys.教务管理.教学设置.主体班时限设置.main_class_time_limit_setting_page import \
            MainClassTimeLimitSetPage
        return MainClassTimeLimitSetPage(self.driver)

    @allure.step('进入教学设置-对外班评估时限设置')
    def go_external_class_time_limit_page(self):
        self.locator_left_menu_click(menu_title='教学设置', button_title='对外班评估时限设置')
        from djw.page.smart_school_sys.教务管理.教学设置.对外班时限设置.external_class_time_limit_setting_page import \
            ExternalClassTimeLimitSetPage
        return ExternalClassTimeLimitSetPage(self.driver)

    @allure.step('进入教学设置-时段设置')
    def go_time_slot_set_page(self):
        self.locator_left_menu_click(menu_title='教学设置', button_title='时段设置')
        from djw.page.smart_school_sys.教务管理.教学设置.时段设置.time_slot_set_page import TimeSlotSetPage
        return TimeSlotSetPage(self.driver)

    @allure.step('进入班次快捷管理')
    def go_class_quick_manage(self):
        self.locator_left_menu_click(button_title='班次快捷管理')
        from djw.page.smart_school_sys.教务管理.教学管理.班次快捷管理.class_quick_main_page import ClassQuickManagePage
        return ClassQuickManagePage(self.driver)

    @allure.step('进入两带来')
    def go_edu_two_bring_page(self):
        self.locator_left_menu_click(button_title='两带来')
        from djw.page.smart_school_sys.教务管理.班级管理.两带来.two_bring_page import TwoBringManagePage
        return TwoBringManagePage(self.driver)

    @allure.step('学籍信息查询_班次')
    def go_stu_status_search_class(self):
        self.locator_left_menu_click(menu_title='综合统计', button_title='学籍信息查询（班次）')
        from djw.page.smart_school_sys.教务管理.综合统计.学籍信息查询_班次.schoolroll_query_class import SchoolRollQueryClass
        return SchoolRollQueryClass(self.driver)

    @allure.step('进入意见建议统计')
    def go_suggestion_statics(self):
        self.locator_left_menu_click(menu_title='综合统计', button_title='意见建议统计')
        from djw.page.smart_school_sys.对外培训.意见建议统计.suggestion_statics import SuggestionStatics
        return SuggestionStatics(self.driver)

    @allure.step('进入教师授课汇总')
    def go_tea_teach_summary_page(self):
        self.locator_left_menu_click(menu_title='综合统计', button_title='教师授课汇总')
        from djw.page.smart_school_sys.教务管理.综合统计.教师授课汇总.tea_teach_summary import TeaTeachSummary
        return TeaTeachSummary(self.driver)

    @allure.step('进入小组评估统计')
    def go_group_evaluation_statics(self):
        self.locator_left_menu_click(menu_title='综合统计', button_title='小组评估统计')
        from djw.page.smart_school_sys.教务管理.综合统计.小组评估统计.group_evaluation_statics import GroupEvaluationStatics
        return GroupEvaluationStatics(self.driver)

    @allure.step('进入综合统计-教室占用情况统计')
    def go_class_occ_condition(self):
        self.locator_left_menu_click(button_title='教室占用情况统计')
        from djw.page.smart_school_sys.教务管理.教室占用情况统计.resource_occupy_census import SiteOccupation
        return SiteOccupation(self.driver)


    @allure.step('进入教务管理-作业管理')
    def go_homework_manege(self):
        self.locator_left_menu_click(menu_title='班级管理', button_title='作业管理')
        from djw.page.smart_school_sys.教务管理.班级管理.作业管理.homework_manage import HomeWorkManage
        return HomeWorkManage(self.driver)

    @allure.step('进入教务管理-作业批阅')
    def go_homework_review(self):
        self.locator_left_menu_click(menu_title='班级管理', button_title='作业批阅')
        from djw.page.smart_school_sys.教务管理.班级管理.作业批阅.homework_review_manage_page import HomeworkReviewManagePage
        return HomeworkReviewManagePage(self.driver)
