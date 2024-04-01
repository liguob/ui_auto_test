# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/6/15    9:55
============================
"""
import random
import allure
import pytest
from common.file_path import role_account
from common.yml import read_yaml
from common.random_tool import randomTool
from djw.page.smart_school_sys.主页.home_page import HomePage
from djw.page.smart_school_sys.登录.login_page import LoginPage
from djw.page_app.smart_school_sys.登录.app_login_page import AppLoginPage
from djw.test_base_cases.test_a_01_dept_role_user import RoleUserFileName
from djw.test_base_cases.test_a_03_import_user import UserInfoFileName
from djw.test_base_cases.test_d_01_create_class import CurrentClassFile, HistoryClassFile, FeatureClassFile
from djw.test_base_cases.test_d_01_create_class import ImportCurrentStuFile
from selenium.webdriver.remote.webdriver import WebDriver
from common.path_lib import DJW_CREATE_DIR, DJW_TEST_DIR
from common.excel_tool import DjwPd


def read_login_info(role_name: str):
    """读取智慧校园登录角色账号信息"""
    return read_yaml(role_account)[role_name]


def judge_go_login_page(driver: WebDriver, username, login_sys: str = "djw", password='Aa@jiaowu'):
    """根据driver_type判断登录系统所属的登录类"""
    if login_sys == "djw":  # 大教务系统
        return LoginPage(driver=driver).login(username=username, password=password)
    elif login_sys == "djw_stu":  # 大教务学员登录
        return LoginPage(driver=driver).login_stu_client(username=username, password=password)
    elif login_sys == 'djw_wb':  # 大教务网报系统登录
        return LoginPage(driver=driver).login_network_report_client(username=username, password=password)
    elif login_sys == 'app_stu':
        return AppLoginPage(driver=driver).app_login(username=username, password=password)
    elif login_sys == 'app_gl':
        return AppLoginPage(driver=driver).app_gl_login(username=username, password=password)
    else:
        raise Exception('请指定login_sys正确的登录系统')


@pytest.fixture(scope='function')
def djw_login(open_browser):
    """根据账号自行登录大教务系统"""

    def _login(username, driver_type='web', password='Aa@jiaowu', login_sys="djw"):
        """根据账号密码登录"""
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, username=username, password=password)

    return _login


@pytest.fixture(scope="function")
def djw_login_by_admin(open_browser):
    def _login(driver_type='web', login_sys="djw", role_index=1):
        """
        超级管理员登录
        :param driver_type:指定登录端->web/app,默认web
        :param role_index:使用第几个账号->从1开始
        :return:HomePage
        """
        login_info = read_login_info("admin")[role_index - 1]
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, **login_info)

    return _login


@pytest.fixture(scope="function")
def djw_login_by_class_master(open_browser, djw_base_file_data_info):
    def _login(driver_type='web', login_sys="djw"):
        """
        班主任登录
        :param driver_type:指定登录端->web/app,默认web
        :return:HomePage
        """
        username = djw_base_file_data_info(RoleUserFileName)[0]['手机号码']
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, username=username)

    return _login


@pytest.fixture(scope="function")
def djw_login_by_school_leader(open_browser, djw_base_file_data_info):
    def _login(driver_type='web', login_sys="djw"):
        """
        校领导登录
        :param driver_type:指定登录端->web/app,默认web
        :return:HomePage
        """
        username = djw_base_file_data_info(RoleUserFileName)[2]['手机号码']
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, username=username)

    return _login


@pytest.fixture(scope="function")
def djw_login_by_jwc_leader(open_browser, djw_base_file_data_info):
    def _login(driver_type='web', login_sys="djw"):
        """
        教务处领导登录
        :param driver_type:指定登录端->web/app,默认web
        :return:HomePage
        """
        username = djw_base_file_data_info(RoleUserFileName)[1]['手机号码']
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, username=username)

    return _login


@pytest.fixture(scope="class")
def djw_login_by_admin_scope_class(create_driver):
    def _login(driver_type='web', login_sys="djw", role_index=1):
        """
        超级管理员登录
        :param driver_type:指定登录端->web/app,默认web
        :param role_index:使用第几个账号->从1开始
        :return:HomePage
        """
        login_info = read_login_info("admin")[role_index - 1]
        login_driver = create_driver(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, **login_info)

    return _login


@pytest.fixture(scope='class')
def djw_login_class_driver(create_driver):
    def _login(username, password='Aa@jiaowu'):
        dr = create_driver()
        LoginPage(dr).login(username, password)
        return HomePage(dr)

    return _login


@pytest.fixture(scope='class')
def djw_login_class_driver_mobile(create_mobile_driver):
    def _login(username, password='Aa@jiaowu'):
        dr = create_mobile_driver()
        AppStuHomePage = AppLoginPage(dr).app_login(username, password)
        return AppStuHomePage

    return _login


@pytest.fixture(scope="function")
def djw_login_jwc_pt_account(open_browser, djw_base_file_data_info):
    """人事请休假申请/出境记录申请用户登录"""

    def _login(driver_type='web', login_sys='djw'):
        username = djw_base_file_data_info(UserInfoFileName)[0]['手机号码']
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, username=username)

    return _login


@pytest.fixture(scope="function")
def djw_login_by_teach_research_leader(open_browser, djw_base_file_data_info):
    def _login(driver_type='web', login_sys="djw"):
        """
        教研部领导登录
        :param driver_type:指定登录端->web/app,默认web
        :return:HomePage
        """
        username = djw_base_file_data_info(RoleUserFileName)[3]['手机号码']
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, username=username)

    return _login


@pytest.fixture(scope='function')
def djw_login_by_personnel_admin(open_browser):
    def _login(driver_type='web', login_sys="djw", role_index=1):
        """
        人事管理员登录
        :param driver_type:指定登录端->web/app,默认web
        :return:HomePage
        """
        login_info = read_login_info("admin")[role_index - 1]
        login_driver = open_browser(driver_type=driver_type)
        return judge_go_login_page(driver=login_driver, login_sys=login_sys, **login_info)

    return _login


@pytest.fixture(scope='class')
def current_class_name(djw_base_file_data_info):
    """获取基础用例当前班次名称"""
    class_file = djw_base_file_data_info(CurrentClassFile)
    class_name = random.choice(class_file)['班次名称']
    return class_name


@pytest.fixture(scope='class')
def history_class_name(djw_base_file_data_info):
    """获取基础用例历史班次名称"""
    class_file = djw_base_file_data_info(HistoryClassFile)
    class_name = random.choice(class_file)['班次名称']
    return class_name


@pytest.fixture(scope='class')
def future_class_name(djw_base_file_data_info):
    """获取基础用例未开始班次名称"""
    class_file = djw_base_file_data_info(FeatureClassFile)
    class_name = random.choice(class_file)['班次名称']
    return class_name


@pytest.fixture(scope='function')
def djw_app_login_stu(djw_login):
    """大教务app学员登录"""

    def _stu_app_login(username):
        """username为登录的用户名"""
        return djw_login(driver_type='app', login_sys='app_stu', username=username)

    return _stu_app_login


@pytest.fixture(scope='class')
def login_app_as_current_stu(djw_login_class_driver_mobile):
    """
    使用基础用例当前班次首个学员登录移动端
    pc/app端均需调用
    """
    stu_file = DjwPd.base_data_path(ImportCurrentStuFile)
    stu_phone = DjwPd.read_excel(stu_file)[0]['手机号码']
    app_stu_homepage = djw_login_class_driver_mobile(stu_phone)
    yield app_stu_homepage


@pytest.fixture()
def drop_stu_import(djw_login_class_driver, current_class_name, djw_base_file_data_info):
    """
    基础用例当前班次导入退学/每日报告学员
    返回导入退学/每日报告学员手机号
    """
    # 使用班主任角色账号登录
    bzr_phone = djw_base_file_data_info(RoleUserFileName)[0]['手机号码']
    home_page = djw_login_class_driver(bzr_phone)
    # 进入班主任管理-学员管理
    stu_manage_page = home_page.go_master_manage_page().go_stu_manage_page()
    # 搜索基础用例当前班次-进入管理
    step1 = stu_manage_page.switch_current_class().search_class(current_class_name) \
        .go_student_manage_page(current_class_name)
    # 导入退学学员(带断言)
    path = DJW_TEST_DIR / '学员管理' / '退学管理' / '_data' / '退学学员导入数据.xls'
    drop_stu_file = DjwPd.read_excel_func_save(str(path))
    tip = step1.import_student(drop_stu_file).alert_tip()
    assert tip == '导入成功'
    # 返回导入退学学员手机号
    stu_phone = DjwPd.read_excel(drop_stu_file)[0]['手机号码']
    yield stu_phone


@pytest.fixture()
def new_a_future_class(djw_login_by_admin):
    """新增一个未开始班次->返回班次名"""
    class_manage_page = djw_login_by_admin().go_edu_manage_page().go_class_manage_page()
    data = random.choice(DjwPd.read_excel(DjwPd.read_excel_func_save(DJW_CREATE_DIR / '未开始班次数据.xlsx')))
    new_future_class_name = data['班次名称']
    class_manage_page.add_class(data)
    yield new_future_class_name


@pytest.fixture()
def new_a_current_class(djw_login_by_admin):
    """新增一个当前班次->返回班次名"""
    class_manage_page = djw_login_by_admin().go_edu_manage_page().go_class_manage_page()
    data = random.choice(DjwPd.read_excel(DjwPd.read_excel_func_save(DJW_CREATE_DIR / '当前班次数据.xlsx')))
    new_current_class_name = data['班次名称']
    class_manage_page.add_class(data)
    yield new_current_class_name


@pytest.fixture(scope='class')
def into_app_my_homework_manage_page(login_app_as_current_stu):
    """
    进入我的作业--作业管理页
    tip:pc端+移动端均需调用
    """
    my_homework_manage_page = login_app_as_current_stu.go_more_page().go_my_homework_manage_page()
    yield my_homework_manage_page


@pytest.fixture()
def go_drop_apply_step(drop_stu_import, djw_login_class_driver_mobile):
    """
    使用基础用例当前班次的导入退学学员登录移动端->进入退学申请列表页
    @author:yangdeyi
    tip:pc端+移动端均需调用
    """
    drop_stu_phone = drop_stu_import
    app_stu_home_page = djw_login_class_driver_mobile(drop_stu_phone)
    drop_apply_page = app_stu_home_page.go_more_page().go_drop_apply()
    yield drop_apply_page


@pytest.fixture()
def send_drop_apply_step(go_drop_apply_step) -> dict:
    """
    @author:hc
    学员（移动端）：发送退学申请
    tip:pc端+移动端均需调用
    """
    dict_info = go_drop_apply_step.click_drop_apply_add().edit_drop_apply_form()  # 新建发送退学申请->获取姓名、原因、日期
    go_drop_apply_step.click_apply_send()
    yield dict_info


@pytest.fixture()
def go_class_notice(djw_login_by_class_master):
    """
    @author:hc
    进入班主任管理-班级公告的前置条件
    tip:pc端+移动端均需调用
    """
    class_notice_page = djw_login_by_class_master().go_master_manage_page().go_class_notice()
    yield class_notice_page


@pytest.fixture()
def go_class_notice_by_edu(djw_login_by_jwc_leader):
    """
    @author:hc
    进入教务管理-班级公告的前置条件
    tip:pc端+移动端均需调用
    """
    class_notice_page = djw_login_by_jwc_leader().go_edu_manage_page().go_edu_class_notice()
    yield class_notice_page


@pytest.fixture()
def send_class_notice(go_class_notice, current_class_name):
    """
    @author:hc
    发送班级公告
    tip:pc端+移动端均需调用
    """
    info = go_class_notice.into_class_notice_add_handle().class_notice_send(current_class_name)
    yield info


@pytest.fixture()
def go_leave_manage_step(djw_login_by_class_master):
    """
    @author:hc
    班主任：首页->班主任->请假管理
    """
    pc_leave_manage = djw_login_by_class_master().go_master_manage_page().go_leave_manage()  # 进入到请假管理页面
    yield pc_leave_manage


@allure.step("班主任进入班级通讯录")
@pytest.fixture()
def go_class_address_book(djw_login_by_class_master):
    """
    @author:hc
    班主任（pc）：进入班级通讯录申请
    tip:pc端+移动端均需调用
    """
    addr_book = djw_login_by_class_master().go_master_manage_page().go_class_contact_page()
    yield addr_book


@pytest.fixture(scope='class')
def djw_base_file_data_info():
    """返回获取大教务基础用例生成的文件数据"""

    def _get_file_info(file_name):
        return DjwPd.read_base_data_excel(file_name=file_name)

    return _get_file_info


@pytest.fixture(scope='class')
def class_master_name(djw_base_file_data_info):
    """获取创建数据中的班主任的姓名"""
    name = djw_base_file_data_info(RoleUserFileName)[0]['姓名']
    return name


@pytest.fixture(scope='class')
def get_role_user_names(djw_base_file_data_info):
    """角色用户的所有姓名"""
    name_info = djw_base_file_data_info(RoleUserFileName)
    names = [i['姓名'] for i in name_info]
    return names


@pytest.fixture(scope='class')
def xld_leader_name(get_role_user_names):
    """返回基础数据中校领导名称"""
    return get_role_user_names[2]


@pytest.fixture(scope='class')
def jwc_leader_name(get_role_user_names):
    """返回基础数据中教务领导名称"""
    return get_role_user_names[1]


@pytest.fixture(scope='class')
def course_name():
    """返回课程名称"""
    return DjwPd.read_base_data_excel('课程数据.xlsx')[0]['课程名称']


@pytest.fixture(scope='class')
def current_class_stu_data():
    """当前班次的基础数据学员信息"""
    return DjwPd.read_base_data_excel(ImportCurrentStuFile)
