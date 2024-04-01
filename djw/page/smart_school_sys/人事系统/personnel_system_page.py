# -*- coding: utf-8 -*-
"""
===============================
@Time     ：2021/9/6 11:22
@Author   ：李国彬
===============================
"""
import allure
from djw.page.smart_school_sys.主页.home_page import HomePage


class PersonnelSysPage(HomePage):
    """人事系统主页面"""

    @allure.step("进入用户信息主页")
    def go_user_info(self):
        self.locator_left_menu_click(menu_title='人员管理', button_title='用户信息')
        from djw.page.smart_school_sys.人事系统.人员管理.用户信息.user_manage import UserManagePage
        self.wait_presence_list_data(explicit_timeout=20)
        return UserManagePage(self.driver)

    @allure.step("进入培养管理主页")
    def go_training_manage(self):
        self.locator_left_menu_click(menu_title='人员管理', button_title='培养管理')
        from djw.page.smart_school_sys.人事系统.人员管理.培养管理.training_manage import TrainingManagePage
        return TrainingManagePage(self.driver)

    @allure.step("进入奖励管理主页")
    def go_reward_manage(self):
        self.locator_left_menu_click(menu_title='人员管理', button_title='奖励管理')
        from djw.page.smart_school_sys.人事系统.人员管理.奖励管理.reward_manage import RewardManagePage
        return RewardManagePage(self.driver)

    @allure.step("进入惩罚管理主页")
    def go_punish_manage(self):
        """进入惩罚管理"""
        self.locator_left_menu_click(menu_title='人员管理', button_title='惩罚管理')
        from djw.page.smart_school_sys.人事系统.人员管理.惩罚管理.punish_manage import PunishManagePage
        return PunishManagePage(self.driver)

    @allure.step("进入职务管理主页")
    def go_post_manage(self):
        self.locator_left_menu_click(menu_title='人员管理', button_title='职务管理')
        from djw.page.smart_school_sys.人事系统.人员管理.职务管理.post_manage import PostManagePage
        return PostManagePage(self.driver)

    @allure.step("进入职称管理主页")
    def go_post_title_manage(self):
        self.locator_left_menu_click(menu_title='人员管理', button_title='职称管理')
        from djw.page.smart_school_sys.人事系统.人员管理.职称管理.post_title_manage import PostTitleManagePage
        return PostTitleManagePage(self.driver)

    @allure.step("进入职级管理主页")
    def go_rank_manage(self):
        self.locator_left_menu_click(menu_title='人员管理', button_title='职级管理')
        from djw.page.smart_school_sys.人事系统.人员管理.职级管理.rank_manage import RankManagePage
        return RankManagePage(self.driver)

    @allure.step("进入待退休管理主页")
    def go_not_retire_manage(self):
        self.locator_left_menu_click(menu_title='退休管理', button_title='待退休管理')
        from djw.page.smart_school_sys.人事系统.退休管理.待退休管理.not_retired_manage import NotRetiredManagePage
        return NotRetiredManagePage(self.driver)

    @allure.step("进入已退休管理主页")
    def go_retired_manage(self):
        self.locator_left_menu_click(menu_title='退休管理', button_title='已退休管理')
        from djw.page.smart_school_sys.人事系统.退休管理.已退休管理.retired_manage import RetiredManagePage
        return RetiredManagePage(self.driver)

    @allure.step("进入退休操作日志主页")
    def go_retired_log_manage(self):
        self.locator_left_menu_click(menu_title='退休管理', button_title='退休操作日志')
        from djw.page.smart_school_sys.人事系统.退休管理.退休操作日志.retired_log_manage import RetiredLogManagePage
        return RetiredLogManagePage(self.driver)

    @allure.step('进入挂职培训主页')
    def go_temporary_train_manage(self):
        self.locator_left_menu_click(menu_title='人员管理', button_title='挂职培训')
        from djw.page.smart_school_sys.人事系统.人员管理.挂职培训.temporary_training_manage import \
            TemporaryTrainingManagePage
        return TemporaryTrainingManagePage(self.driver)

    @allure.step('进入合同管理主页')
    def go_contract_manage(self):
        self.locator_left_menu_click(button_title='合同管理')
        from djw.page.smart_school_sys.人事系统.合同管理.contract_manage_page import ContractManagePage
        return ContractManagePage(self.driver)

    @allure.step("进入评先评优")
    def go_first_and_best(self):
        self.locator_left_menu_click(button_title='评先评优')
        from djw.page.smart_school_sys.人事系统.评先评优.first_and_best_page import FirstAndBestPage
        return FirstAndBestPage(self.driver)

    @allure.step("进入辞职申请")
    def go_resignation_application_page(self):
        self.locator_left_menu_click(button_title='辞职申请', menu_title='辞职管理')
        from djw.page.smart_school_sys.人事系统.辞职管理.辞职申请.resignation_application_manage_page import \
            ResignationApplicationPage
        return ResignationApplicationPage(self.driver)

    @allure.step("进入辞职审批")
    def go_resignation_review_page(self):
        self.locator_left_menu_click(button_title='辞职审批', menu_title='辞职管理')
        from djw.page.smart_school_sys.人事系统.辞职管理.辞职审批.resignation_review_manage_page import \
            ResignationReviewPage
        return ResignationReviewPage(self.driver)

    @allure.step('进入资料管理')
    def go_material_manage(self):
        self.locator_left_menu_click(button_title='资料管理')
        from djw.page.smart_school_sys.人事系统.资料管理.material_manage import MaterialManage
        return MaterialManage(driver=self.driver)

    @allure.step('进入已故人员管理')
    def go_deceased_manage(self):
        self.locator_left_menu_click(button_title='已故人员管理')
        from djw.page.smart_school_sys.人事系统.已故人员管理.deceased_manage import DeceasedManage
        return DeceasedManage(driver=self.driver)

    @allure.step('进入人事信息统计')
    def go_personnel_summary(self):
        self.locator_left_menu_click(button_title='人事信息统计')
        from djw.page.smart_school_sys.人事系统.人事信息统计.personnel_summary_page import PersonnelSummaryPage
        return PersonnelSummaryPage(driver=self.driver)

    @allure.step('进入参公编制汇总')
    def go_public_summary(self):
        self.locator_left_menu_click(menu_title='人事编制汇总', button_title='参公编制汇总')
        from djw.page.smart_school_sys.人事系统.人事编制汇总.public_summary import PublicSummary
        return PublicSummary(driver=self.driver)

    @allure.step('进入事业编制汇总')
    def go_career_summary(self):
        self.locator_left_menu_click(menu_title='人事编制汇总', button_title='事业编制汇总')
        from djw.page.smart_school_sys.人事系统.人事编制汇总.career_summary import CareerSummary
        return CareerSummary(driver=self.driver)

    @allure.step("进入简历库")
    def go_resume_lib(self):
        self.locator_left_menu_click(menu_title='人事招聘', button_title='简历库')
        from djw.page.smart_school_sys.人事系统.人事招聘.简历库.resume_lib import ResumeLib
        return ResumeLib(driver=self.driver)

    @allure.step("进入录用管理")
    def go_admit_manage(self):
        self.locator_left_menu_click(menu_title='人事招聘', button_title='录用管理')
        from djw.page.smart_school_sys.人事系统.人事招聘.录用管理.admit_manage import AdmitManage
        return AdmitManage(driver=self.driver)

    @allure.step("进入简历审核")
    def go_resume_check(self):
        self.locator_left_menu_click(menu_title='人事招聘', button_title='简历审核')
        from djw.page.smart_school_sys.人事系统.人事招聘.简历审核.resume_check import ResumeCheck
        return ResumeCheck(driver=self.driver)

    @allure.step("进入面试通知")
    def go_interview_notice(self):
        self.locator_left_menu_click(menu_title='人事招聘', button_title='面试通知')
        from djw.page.smart_school_sys.人事系统.人事招聘.面试通知.interview_notice import InterviewNotice
        return InterviewNotice(driver=self.driver)

    @allure.step("进入招聘公告")
    def go_recruit_notice(self):
        self.locator_left_menu_click(menu_title='人事招聘', button_title='招聘公告')
        from djw.page.smart_school_sys.人事系统.人事招聘.招聘公告.recruit_notice import RecruitNotice
        return RecruitNotice(driver=self.driver)

    @allure.step("进入岗位信息维护")
    def go_position_maintain(self):
        self.locator_left_menu_click(menu_title='人事招聘', button_title='岗位信息维护')
        from djw.page.smart_school_sys.人事系统.人事招聘.岗位信息维护.position_maintain import PositionMaintain
        return PositionMaintain(driver=self.driver)

    @allure.step('进入规章制度管理')
    def go_rule_manage(self):
        self.locator_left_menu_click(menu_title='规章制度', button_title='规章制度管理')
        from djw.page.smart_school_sys.人事系统.规章制度.规章制度管理.rulemanage import RuleManagePage
        return RuleManagePage(driver=self.driver)

    @allure.step('进入规章制度查看')
    def go_rule_view(self):
        self.locator_left_menu_click(menu_title='规章制度', button_title='规章制度查看')
        from djw.page.smart_school_sys.人事系统.规章制度.规章制度查看.rulecheck import RuleCheckPage
        return RuleCheckPage(driver=self.driver)

    @allure.step("进入请休假申请")
    def go_leave_and_vacation(self):
        self.locator_left_menu_click(menu_title='请休假管理', button_title='请休假申请')
        from djw.page.smart_school_sys.人事系统.请休假管理.请休假申请.leaveandvacation import LeaveAndVacationPage
        self.wait_presence_list_data()
        return LeaveAndVacationPage(driver=self.driver)

    @allure.step("进入请休假审核")
    def go_leave_and_vacation_audit(self):
        self.locator_left_menu_click(menu_title='请休假管理', button_title='请休假审核')
        from djw.page.smart_school_sys.人事系统.请休假管理.请休假审核.leaveandvacationaudit import LeaveAndVacationAudit
        return LeaveAndVacationAudit(driver=self.driver)

    @allure.step("进入销假申请")
    def go_logout_leave_apply(self):
        self.locator_left_menu_click(menu_title='请休假管理', button_title='销假申请')
        from djw.page.smart_school_sys.人事系统.请休假管理.销假申请.logoutleaveapply import LogoutLeaveApply
        return LogoutLeaveApply(driver=self.driver)

    @allure.step("进入销假管理")
    def go_logout_leave_manage(self):
        self.locator_left_menu_click(menu_title='请休假管理', button_title='销假管理')
        from djw.page.smart_school_sys.人事系统.请休假管理.销假管理.logoutleavemanage import LogoutLeaveManagePage
        return LogoutLeaveManagePage(driver=self.driver)

    @allure.step('进入因私出国-证件管理')
    def go_passport_manage(self):
        self.locator_left_menu_click(menu_title='因私出国', button_title='证件管理')
        from djw.page.smart_school_sys.人事系统.因私出国.证件管理.passport_manage import PassportManage
        self.wait_presence_list_data(explicit_timeout=15)
        return PassportManage(driver=self.driver)

    @allure.step('进入因私出国-出境记录')
    def go_abroad_apply(self):
        self.locator_left_menu_click(menu_title='因私出国', button_title='出境记录')
        from djw.page.smart_school_sys.人事系统.因私出国.出境记录.abroad_apply import AbroadApply
        self.wait_presence_list_data(explicit_timeout=15)
        return AbroadApply(driver=self.driver)

    @allure.step('进入因私出国-因私出国管理')
    def go_abroad_manage(self):
        self.locator_left_menu_click(menu_title='因私出国', button_title='因私出国管理')
        from djw.page.smart_school_sys.人事系统.因私出国.因私出国管理.abroad_check import AbroadManage
        self.wait_presence_list_data(explicit_timeout=15)
        return AbroadManage(driver=self.driver)

    @allure.step('进入因私出国-证件使用信息')
    def go_passport_use_info(self):
        self.locator_left_menu_click(menu_title='因私出国', button_title='证件使用信息')
        from djw.page.smart_school_sys.人事系统.因私出国.证件使用信息.passport_detail import PassportDetail
        self.wait_presence_list_data(explicit_timeout=15)
        return PassportDetail(driver=self.driver)

    @allure.step('进入老干部管理-老干部信息管理')
    def go_veteran_cadre_info_manage(self):
        self.locator_left_menu_click(menu_title='老干部管理', button_title='老干部信息管理')
        from djw.page.smart_school_sys.人事系统.老干部管理.veteran_cadre_info_manage import VeteranCadreInfoManage
        return VeteranCadreInfoManage(driver=self.driver)

    @allure.step('进入老干部管理-老干部统计')
    def go_veteran_cadre_summary(self):
        self.locator_left_menu_click(menu_title='老干部管理', button_title='老干部统计')
        from djw.page.smart_school_sys.人事系统.老干部管理.veteran_cadre_summary import VeteranCadreSummary
        return VeteranCadreSummary(driver=self.driver)

    @allure.step('进入工资管理-工资管理')
    def go_salary_manage(self):
        self.locator_left_menu_click(menu_title='工资管理', button_title='工资管理')
        from djw.page.smart_school_sys.人事系统.工资管理.salary_manage import SalaryManage
        return SalaryManage(driver=self.driver)

    @allure.step('进入组织机构管理-部门管理')
    def go_dept_manage(self):
        self.locator_left_menu_click(menu_title='组织机构管理', button_title='部门管理')
        from djw.page.smart_school_sys.人事系统.组织机构管理.部门管理.dept_manage import DeptManage
        return DeptManage(driver=self.driver)

    @allure.step('进入组织机构管理-单位管理')
    def go_institution_manage(self):
        self.locator_left_menu_click(menu_title='组织机构管理', button_title='单位管理')
        from djw.page.smart_school_sys.人事系统.组织机构管理.单位管理.institution_manage import InstitutionManage
        return InstitutionManage(driver=self.driver)

    @allure.step('进入考勤规则设置')
    def go_attendance_rule_set(self):
        self.locator_left_menu_click(button_title='考勤规则设置')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤规则设置.attendance_rule_set import AttendanceRuleSet
        return AttendanceRuleSet(self.driver)

    @allure.step('进入考勤种类')
    def go_attendance_type(self):
        self.locator_left_menu_click(button_title='考勤种类')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤种类.attendance_type import AttendanceType
        return AttendanceType(self.driver)

    @allure.step('进入特殊考勤人员设置')
    def go_special_attendance(self):
        self.locator_left_menu_click(button_title='特殊考勤人员设置')
        from djw.page.smart_school_sys.人事系统.考勤管理.特殊人员考勤设置.special_user_attendance import \
            SpecialUserAttendance
        return SpecialUserAttendance(self.driver)

    @allure.step('进入考勤原始记录')
    def go_attendance_record(self):
        self.locator_left_menu_click(button_title='考勤原始记录')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤原始记录.attendance_record import AttendanceRecord
        return AttendanceRecord(self.driver)

    @allure.step('进入考勤日统计(当前部门)')
    def go_attendance_day_static_cur(self):
        self.locator_left_menu_click(button_title='考勤日统计（当前部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤日统计_当前部门.attendance_day_static_cur import \
            AttendanceDayStaticCur
        return AttendanceDayStaticCur(self.driver)

    @allure.step('进入考勤日统计(所有部门)')
    def go_attendance_day_static_all(self):
        self.locator_left_menu_click(button_title='考勤日统计（所有部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤日统计_所有部门.attendance_day_static_all import \
            AttendanceDayStaticAll
        return AttendanceDayStaticAll(self.driver)

    @allure.step('进入考勤月统计(当前部门)')
    def go_attendance_month_static_cur(self):
        self.locator_left_menu_click(button_title='考勤月统计（当前部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤月统计_当前部门.attendance_month_static_cur import \
            AttendanceMonthStaticCur
        return AttendanceMonthStaticCur(self.driver)

    @allure.step('进入考勤月统计(所有部门)')
    def go_attendance_month_static_all(self):
        self.locator_left_menu_click(button_title='考勤月统计（所有部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤月统计_所有部门.attendance_month_static_cur import \
            AttendanceMonthStaticAll
        return AttendanceMonthStaticAll(self.driver)

    @allure.step('进入特殊考勤人员统计')
    def go_special_attendance_static(self):
        self.locator_left_menu_click(button_title='特殊考勤人员统计')
        from djw.page.smart_school_sys.人事系统.考勤管理.特殊考勤人员统计.special_attendance_static import \
            SpecialAttendanceStatic
        return SpecialAttendanceStatic(self.driver)

    @allure.step('进入异常考勤查询（所有部门）')
    def go_abnormal_attendance_all(self):
        self.locator_left_menu_click(button_title='异常考勤查询（所有部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.异常考勤查询_所有部门.abnormal_attendance_all import \
            AbnormalAttendanceAll
        return AbnormalAttendanceAll(self.driver)

    @allure.step('进入异常考勤查询（当前部门）')
    def go_abnormal_attendance_cur(self):
        self.locator_left_menu_click(button_title='异常考勤查询（当前部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.异常考勤查询_当前部门.abnormal_attendance_cur import \
            AbnormalAttendanceCur
        return AbnormalAttendanceCur(self.driver)

    @allure.step('进入异常考勤调整记录（所有部门）')
    def go_abnormal_attendance_change_record_all(self):
        self.locator_left_menu_click(button_title='异常考勤调整记录（所有部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.异常考勤调整记录_所有部门.abnormal_attendance_change_record_all import \
            AbnormalAttendanceChangeRecordAll
        return AbnormalAttendanceChangeRecordAll(self.driver)

    @allure.step('进入异常考勤调整记录（当前部门）')
    def go_abnormal_attendance_change_record_cur(self):
        self.locator_left_menu_click(button_title='异常考勤调整记录（当前部门）')
        from djw.page.smart_school_sys.人事系统.考勤管理.异常考勤调整记录_当前部门.abnormal_attendance_change_record_cur import \
            AbnormalAttendanceChangeRecordCur
        return AbnormalAttendanceChangeRecordCur(self.driver)

    @allure.step('进入我的考勤')
    def go_my_attendance(self):
        self.locator_left_menu_click(button_title='我的考勤')
        from djw.page.smart_school_sys.人事系统.考勤管理.我的考勤.my_attendance import MyAttendance
        return MyAttendance(self.driver)

    @allure.step('进入补卡申请记录')
    def go_attendance_apply_record(self):
        self.locator_left_menu_click(button_title='补卡申请记录')
        from djw.page.smart_school_sys.人事系统.考勤管理.补卡申请记录.attendance_apply_record import \
            AttendanceApplyRecord
        return AttendanceApplyRecord(self.driver)

    @allure.step('进入补卡审核')
    def go_attendance_apply_check(self):
        self.locator_left_menu_click(button_title='补卡审核')
        from djw.page.smart_school_sys.人事系统.考勤管理.补卡审核.attendance_apply_check import AttendanceApplyCheck
        return AttendanceApplyCheck(self.driver)