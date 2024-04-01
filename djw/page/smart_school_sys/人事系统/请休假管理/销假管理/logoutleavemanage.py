# encoding=utf-8
"""
============================
Author:何超
Time:2021/08/13
============================
"""
import time
import allure
from selenium.webdriver.common.by import By
from graduate_student.page.manage.home.homepage import HomePage


class LogoutLeaveManagePage(HomePage):
    """销假管理页"""

    def __init__(self, driver):
        super().__init__(driver=driver)
        # self.sort_list_by_time_desc(field_name='销假时间')

    @allure.step("获取销假列表信息")
    def get_logout_manage_info(self):
        name = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[2]')  # 姓名
        sex = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[3]')  # 性别
        birthday = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[4]')  # 出生日期
        phone = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[5]')  # 手机号
        dept = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[6]')  # 部门
        leave_time = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[7]')  # 请休假时间
        logout_time = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[8]')  # 销假时间
        leave_type = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[9]')  # 销假培训
        title = ('name', 'sex', 'birthday', 'phone', 'dept', 'leave_time', 'logout_time', 'leave_type')
        value = self.publish_get_info(name, sex, birthday, phone, dept, leave_time, logout_time, leave_type, t=title)
        return value

    @allure.step("查看销假")
    def into_view_logout_leave_manage(self, index=1):
        from djw.page.smart_school_sys.人事系统.请休假管理.销假申请.logoutleaveform import LogoutLeaveFormPage
        btn = (By.XPATH, '(//*[@*="el-table__fixed-right"]//*[text()=" 查看 "]/parent::a)[{}]'.format(index))
        self.element_click(btn)
        self.switch_to_handle()
        return LogoutLeaveFormPage(self.driver)

    @allure.step('搜索')
    def search_in_logout_manage(self, keyword):
        input_search = (By.XPATH, '//*[@*="page"]//div[@class="search-input el-input"]/input')  # 搜索输入框
        self.clear_input_enter(input_search, keyword)
        time.sleep(0.5)
        return self
