# encoding=utf-8
"""
============================
Author:何超
Time:2021/4/21   10::00
============================
"""
import allure
import pytest
import random
from collections import namedtuple
from common.random_tool import randomTool
from djw.test_base_cases.test_b_01_create_edu_source import CourseFile, SchoolFile, BuildingFile, SiteFile, \
    TransferSchoolFile, TransferSiteFile
from djw.page.smart_school_sys.人事招聘系统.人事招聘主页.recruit_login_page import RecruitLoginPage


@pytest.fixture()
def go_drop_manage_step(djw_login_by_class_master):
    """
    @author:hc
    班主任：进入班主任管理-退学管理
    """
    drop_manage_page = djw_login_by_class_master().go_master_manage_page().go_drop_manage()
    yield drop_manage_page


@pytest.fixture()
def approve_drop_step(send_drop_apply_step, go_drop_manage_step, djw_base_file_data_info):
    """
    @author:hc
    班主任：审核通过退学申请->选择二审人(教务领导角色账户)
    """
    stu_name = send_drop_apply_step['name']
    from djw.test_base_cases.test_a_01_dept_role_user import RoleUserFileName
    checker = djw_base_file_data_info(RoleUserFileName)[1]['姓名']
    yield go_drop_manage_step.search_apply_name(stu_name).click_approve().approve_agree(checker=checker)


@pytest.fixture()
def go_edu_drop_manage_step(approve_drop_step, djw_login_by_jwc_leader):
    """
    @author:hc
    教务领导角色登录->进入退学管理
    """
    yield djw_login_by_jwc_leader().go_edu_manage_page().go_edu_drop_manage()


@pytest.fixture()
def base_campus(djw_base_file_data_info):
    """获取基本数据校区名"""
    campus_name = djw_base_file_data_info(SchoolFile)[0]['校区名称']
    yield campus_name


@pytest.fixture()
def base_building(djw_base_file_data_info):
    """获取基本数据楼宇名"""
    building_name = djw_base_file_data_info(BuildingFile)[0]['楼宇名称']
    yield building_name


@pytest.fixture()
def base_transfer_campus(djw_base_file_data_info):
    """获取基本数据调课校区名"""
    transfer_campus_name = djw_base_file_data_info(TransferSchoolFile)[0]['校区名称']
    yield transfer_campus_name


@pytest.fixture()
def base_classroom(djw_base_file_data_info):
    """获取基本数据场地(教室)名"""
    classroom_name = djw_base_file_data_info(SiteFile)[0]['名称']
    yield classroom_name


@pytest.fixture()
def base_transfer_classroom(djw_base_file_data_info):
    """获取基本数据调课场地(教室)名"""
    transfer_classroom_name = djw_base_file_data_info(TransferSiteFile)[0]['名称']
    yield transfer_classroom_name


@pytest.fixture()
def course_name_namedtuple(djw_base_file_data_info):
    """随机获取一个基本用例课程(非活动)名称和活动名称具名元组"""
    all_type_courses = djw_base_file_data_info(CourseFile)
    names = [course['课程名称'] for course in all_type_courses]
    courses_name = [name for name in names if '活动' not in name]
    activities_name = [name for name in names if '活动' in name]
    course_name, activity_name = random.choice(courses_name), random.choice(activities_name)
    CourseName = namedtuple('CourseName', ['course', 'activity'])
    yield CourseName(course_name, activity_name)


@allure.step('进入教务管理-教学管理-教学计划模板')
@pytest.fixture()
def go_teach_plan_moulds_page(djw_login_by_admin):
    teach_plan_moulds_page = djw_login_by_admin().go_edu_manage_page().go_teach_plan_moulds()
    yield teach_plan_moulds_page


@allure.step('新增启用教学计划模板')
@pytest.fixture()
def add_enable_mould(go_teach_plan_moulds_page):
    """返回教学计划模板列表页面类实例对象及新增启用教学计划模板名"""
    mould_name = randomTool.random_str()
    mould_info = {'名称': mould_name, '是否启用': '已启用'}
    go_teach_plan_moulds_page.add_mould(mould_info)
    go_teach_plan_moulds_page.explicit_wait_ele_presence(go_teach_plan_moulds_page.WEB_TIP)
    go_teach_plan_moulds_page.explicit_wait_ele_lost(go_teach_plan_moulds_page.WEB_TIP)
    Res = namedtuple('Res', 'page mould_name')
    yield Res(go_teach_plan_moulds_page, mould_name)


@allure.step('使用新增启用教学计划模板设置模板内容保存')
@pytest.fixture()
def set_new_mould_content_save(add_enable_mould, course_name):
    mould_list, mould_name = add_enable_mould.page, add_enable_mould.mould_name
    mould_list.search_mould(mould_name).go_mould_set_page()
    from djw.page.smart_school_sys.教务管理.教学管理.教学计划.draw_teach_plan_page import DrawTeachPlanPage
    DrawTeachPlanPage(mould_list.driver).add_course_plan(course_name).set_section_course_module_title().save_all()
    yield add_enable_mould
