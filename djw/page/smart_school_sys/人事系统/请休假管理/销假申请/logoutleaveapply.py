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


class LogoutLeaveApply(HomePage):
    """销假申请页面类"""
    # 成功提示
    tip_success = (By.XPATH, '//*[@*="el-message el-message--success"]')

    def __init__(self, driver):
        super().__init__(driver=driver)
        # self.sort_list_by_time_desc(field_name='提交时间')  # 开启提交时间倒序排列列表

    @allure.step("获取销假列表信息")
    def get_logout_leave_list_info(self):
        leave_time = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[2]')  # 请休假时间
        leave_type = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[3]')  # 请休假类型
        commit_time = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[4]')  # 提交时间
        status = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[5]')  # 销假情况
        title = ("leave_time", "leave_type", "commit_time", "status")
        value = self.publish_get_info(leave_time, leave_type, commit_time, status, t=title)
        return value

    @allure.step("查看销假")
    def into_view_logout_leave(self, index=1):
        from djw.page.smart_school_sys.人事系统.请休假管理.销假申请.logoutleaveform import LogoutLeaveFormPage
        btn = (By.XPATH, '(//*[@*="el-table__fixed-right"]//*[text()=" 查看 "]/parent::a)[{}]'.format(index))
        self.element_click(btn)
        return LogoutLeaveFormPage(self.driver)

    @allure.step("销假")
    def logout_leave(self, index=1):
        btn = (By.XPATH, f'(//*[@*="el-table__fixed-right"]//*[contains(text(), "销假")]/parent::a)[{index}]')
        self.element_click(btn)
        return self

    @property
    @allure.step('获取销假情况')
    def logout_status(self, index=1):
        status = (By.XPATH, f'(//*[contains(@*,"is-scrolling")]//td[5])[{index}]')
        return self.get_ele_text_visitable(status).strip()

    @allure.step('通过请假类型检索销假申请')
    def search_logout(self, leave_type=' '):
        self.locator_search_input(placeholder='请输入请假类型', value=leave_type+'\n')
        time.sleep(1)
