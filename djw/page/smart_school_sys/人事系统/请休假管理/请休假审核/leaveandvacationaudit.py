# encoding=utf-8
"""
============================
Author:
Time:
============================
"""
import time
import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class LeaveAndVacationAudit(PersonnelSysPage):
    """请休假审核页面类"""

    @staticmethod
    def _map(tab):
        value_dict = {"未处理": "pane-tab1", "已处理": "pane-tab2"}
        return value_dict[tab]

    @allure.step("切换处理页")
    def switch_tab(self, tab='已处理'):
        tab = (By.XPATH, '//*[@aria-controls="{}"]'.format(self._map(tab)))
        self.excute_js_click_ele(tab)
        time.sleep(1)
        return self

    @allure.step("获取请休假审核列表信息")
    def get_vacation_audit_list_info(self, tab_key="未处理"):
        tab = self._map(tab_key)
        name = (By.XPATH, '//*[@*="{}"]//*[contains(@*,"is-scrolling")]//td[2]'.format(tab))  # 姓名
        sex = (By.XPATH, '//*[@*="{}"]//*[contains(@*,"is-scrolling")]//td[3]'.format(tab))  # 性别
        phone = (By.XPATH, '//*[@*="{}"]//*[contains(@*,"is-scrolling")]//td[4]'.format(tab))  # 手机号码
        dept = (By.XPATH, '//*[@*="{}"]//*[contains(@*,"is-scrolling")]//td[5]'.format(tab))  # 部门
        time = (By.XPATH, '//*[@*="{}"]//*[contains(@*,"is-scrolling")]//td[6]'.format(tab))  # 请休假时间
        leave_type = (By.XPATH, '//*[@*="{}"]//*[contains(@*,"is-scrolling")]//td[7]'.format(tab))  # 请休假类型
        status = (By.XPATH, '//*[@*="{}"]//*[contains(@*,"is-scrolling")]//td[8]'.format(tab))  # 流转状态
        title = ('name', 'sex', 'phone', 'dept', 'time', 'vacation_type', 'status')
        try:
            value = self.publish_get_info(name, sex, phone, dept, time, leave_type, status, t=title)
            return value
        except Exception as e:
            return []

    @allure.step("进入审核")
    def into_vacation_audit(self, index=1):
        from djw.page.smart_school_sys.人事系统.请休假管理.请休假审核.leaveandvacationauditdetail import LeaveAndVacationAuditDetail
        self.locator_view_button(button_title="审核", id_value=str(index))
        self.switch_to_handle()
        return LeaveAndVacationAuditDetail(self.driver)

    @allure.step('搜索')
    def search_in_leave_audit(self, keyword, tab='未处理'):
        input_search = (By.XPATH, '//div[@id="{}"]//*[@*="page"]//div[@class="search-input el-input"]/input'.format(
            self._map(tab)))  # 搜索输入框
        self.clear_then_input(input_search, keyword+'\n')
        time.sleep(1.5)
        return self

    @allure.step('获取未处理审核统计条数')
    def get_pagination_no_handle(self):
        loc = (By.CSS_SELECTOR, '#pane-tab1 .el-pagination__total')
        self.switch_tab(tab='未处理')
        return self.pagination_count(loc=loc)

    @allure.step('获取已处理审核统计条数')
    def get_pagination_handled(self):
        loc = (By.CSS_SELECTOR, '#pane-tab2 .el-pagination__total')
        self.switch_tab(tab='已处理')
        return self.pagination_count(loc=loc)
