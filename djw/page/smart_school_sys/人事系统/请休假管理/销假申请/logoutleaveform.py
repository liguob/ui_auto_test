# encoding=utf-8
"""
============================
Author:
Time:
============================
"""
import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.人事系统.请休假管理.销假申请.logoutleaveapply import LogoutLeaveApply


class LogoutLeaveFormPage(LogoutLeaveApply):
    """销假表单"""

    @allure.step("获取请休假信息")
    def get_vacation_audit_detail_info(self):
        name = (By.XPATH, '//*[@ctrl-id="person"]//span/span')  # 姓名
        unit = (By.XPATH, '//*[@ctrl-id="unit"]//span/span')  # 所在单位
        dept = (By.XPATH, '//*[@ctrl-id="dept"]//span/span')  # 所在部门
        leave_type = (By.XPATH, '//*[@ctrl-id="type"]//span/span')  # 请休假类型
        time = (By.XPATH, '//*[@ctrl-id="leave"]//span')  # 请休假时间
        reason = (By.XPATH, '//*[@ctrl-id="cause"]//span/span')  # 请休假事由
        title = ("name", "unit", "dept", "type", "time", "reason")
        value = self.publish_get_info(name, unit, dept, leave_type, time, reason, t=title)[0]
        return value

    # @allure.step("发送")
    # def send_logout_leave(self):
    #     btn = (By.XPATH, '//*[text()=" 发送 "]/parent::a')
    #     self.element_click(btn)
    #     return self

    @allure.step("关闭")
    def cloes_logout_leave(self):
        btn = (By.XPATH, '//*[text()=" 关闭 "]//parent::a')
        self.element_click(btn)
        return self
