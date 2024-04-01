# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/1   16:00
============================
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from djw.page.smart_school_sys.主页.home_page import HomePage


class LoginPage(BasePage):
    """登录页面"""
    djw_main_url = 'dsf5/page.html#/pc/login'  # 大教务主系统登录地址
    online_register_sys_url = 'dsf5/page.html#/pc/wb/login'  # 大教务网报管理系统登录地址
    recruit_sys_url = 'dsf5/enroll.html#/enroll/index'  # 大教务人事招聘系统
    login_name_input = (By.CSS_SELECTOR, 'input[name=loginName]')
    password_input = (By.CSS_SELECTOR, 'input[name=password]')
    code = (By.CSS_SELECTOR, 'input[name=code]')
    failTips = (By.XPATH, '//*[@class="el-message__content" and text()]')
    pic_code = 'good'  # 万能图片验证码

    def login(self, username, password, picture_code=None):
        """
        大教务web端正常登录操作
        :param username: 登录名
        :param password: 密码
        :param picture_code: 图片验证码
        :return: HomePage类实例对象
        """
        self.driver.get(self.host + self.djw_main_url)
        self.clear_then_input(self.login_name_input, username)
        self.clear_then_input(self.password_input, password)
        if picture_code is None:
            self.clear_then_input(self.code, self.pic_code)
        else:
            self.clear_then_input(self.code, picture_code)
        self.locator_dialog_btn(btn_name='登录')
        self.locator_dialog_btn(btn_name='教务管理')
        home = HomePage(self.driver)
        # 判断首页元素获取到，登录完成
        WebDriverWait(self.driver, 10).until(self.EC.presence_of_element_located(home.user_info))
        return home

    def login_fail(self, username, password, picture_code=None):
        """
        大教务web端异常登录操作
        :param username: 登录名
        :param password: 密码
        :param picture_code: 图片验证码
        :return: 异常登录提示
        """
        self.driver.get(self.host + self.djw_main_url)
        self.clear_then_input(self.login_name_input, username)
        self.clear_then_input(self.password_input, password)
        if picture_code is None:
            self.clear_then_input(self.code, self.pic_code)
        else:
            self.clear_then_input(self.code, picture_code)
        self.locator_dialog_btn(btn_name='登录')

    def login_stu_client(self, username, password):
        """
        大教务学员端登录操作
        :param username: 登录名
        :param password: 密码
        """
        self.driver.get(self.host + self.djw_main_url)
        self.clear_then_input(self.login_name_input, username)
        self.clear_then_input(self.password_input, password)
        self.clear_then_input(self.code, self.pic_code)
        self.locator_dialog_btn(btn_name='登录')
        time.sleep(2)
        from djw.page.smart_school_sys.PC学员端.stu_home_page import StudentHomePage
        return StudentHomePage(self.driver)

    def login_network_report_client(self, username, password):
        """网报网报端登录"""
        self.driver.get(self.host + self.online_register_sys_url)
        self.clear_then_input(self.login_name_input, username)
        self.clear_then_input(self.password_input, password)
        self.clear_then_input(self.code, self.pic_code)
        self.locator_dialog_btn(btn_name='登录')
        from djw.page.smart_school_sys.网报管理.网报端.network_report_apply_manage_main_page import \
            NetworkReportApplyManagePage
        home = NetworkReportApplyManagePage(self.driver)
        self.wait.until(self.EC.presence_of_element_located(home.user_info))
        if self.find_elements_no_exception((By.CSS_SELECTOR, '[aria-label="完善单位信息"] .el-dialog__title')):
            self.locator_button(button_title='保存')
        return home
