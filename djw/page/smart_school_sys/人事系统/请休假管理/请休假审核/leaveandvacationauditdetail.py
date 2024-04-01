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

from djw.page.smart_school_sys.人事系统.请休假管理.请休假审核.leaveandvacationaudit import LeaveAndVacationAudit


class LeaveAndVacationAuditDetail(LeaveAndVacationAudit):
    """请休假审核详情页面"""
    btn_sure = (By.XPATH, '//*[text()="确定"]/parent::*')  # 确定按钮

    @allure.step("获取请休假信息")
    def get_vacation_audit_detail_info(self):
        name = (By.XPATH, '//*[@ctrl-id="person"]//span/span')  # 姓名
        unit = (By.XPATH, '//*[@ctrl-id="unit"]//span/span')  # 所在单位
        dept = (By.XPATH, '//*[@ctrl-id="dept"]//span/span')  # 所在部门
        leave_type = (By.XPATH, '//*[@ctrl-id="type"]//span/span')  # 请休假类型
        time = (By.XPATH, '//*[@ctrl-id="leave"]//span')  # 请休假时间
        reason = (By.XPATH, '//*[@ctrl-id="cause"]//span/span')  # 请休假事由
        title = ("name", "unit", "dept", "type", "time", "reason")
        value = self.publish_get_info(name, unit, dept, leave_type, time, reason, t=title)
        return value[0]

    @allure.step("选择审批人")
    def _choice_auditor(self, user):
        user_option = (By.XPATH, '//*[text()="{}"]/../../label/span[@*="el-checkbox__input"]'.format(user))
        choice_result = (By.XPATH, '//table[@class="el-table__body"]//td[2]/div[text()="{}"]'.format(user))
        btn_yes = (By.XPATH, '//span[text()="确定"]/..')  # 确认按钮
        self.excute_js_click(user_option)  # 点击审批人复选框
        self.wait_visibility_ele(choice_result)  # 等待选择结果出现
        self.excute_js_click(btn_yes)
        return self

    def flow_tip(self):
        """确定流转提示"""
        tip_box = (By.XPATH, '//*[text()="流程已发送到以下人员："]/parent::*')  # 提示窗
        btn_sure = (By.XPATH, '//div[@class="el-dialog"]//*[text()="确定"]/..')  # 确定按钮
        self.explicit_wait_ele_presence(tip_box, explicit_timeout=20)
        self.poll_click(self.explicit_wait_ele_presence(btn_sure, explicit_timeout=20))
        self.switch_to_handle()
        return self

    def flow_over_tip(self):
        """流程流转结束提示"""
        tip_box = (By.XPATH, '//*[text()="文件已办结"]/parent::*')  # 提示窗
        btn_sure = (By.XPATH, '//*[text()="确定"]/parent::*')  # 确定按钮
        self.explicit_wait_ele_presence(tip_box, explicit_timeout=20)
        self.poll_click(self.explicit_wait_ele_presence(btn_sure, explicit_timeout=20))
        self.switch_to_handle()
        return self

    @allure.step("同意")
    def agree_leave(self, user):
        # btn = (By.XPATH, '//*[text()=" 同意 "]/parent::a')  # 同意按钮
        btn = (By.XPATH, '(//*[@class="ds-page-foot"]//*[contains(@class, "ds-button") and @title])[1]')  # 同意按钮
        # please_select_checker = (By.XPATH, '//*[@aria-label="请选择办理人"]//*[@class="el-dialog__title" and contains(text(), "请选择办理人")]')  # 请选择办理人弹框
        self.element_click(btn)
        self.process_send(checker=user)
        self.switch_to_handle(index=-1)
        # if self.explicit_wait_ele_presence(please_select_checker):  # 如果出现二审人选择弹框
        # if self.is_element_exist(please_select_checker):
        #     self._choice_auditor(user)
        # self.flow_tip()
        # self.wait_browser_close_switch_latest()
        return LeaveAndVacationAudit(self.driver)

    @allure.step("退回")
    def send_back_leave(self):
        btn = (By.XPATH, '//*[text()=" 退回 "]/parent::a')  # 退回按钮
        self.element_click(btn)
        self.flow_tip()
        return LeaveAndVacationAudit(self.driver)

    @allure.step("办结")
    def agree_over_leave(self):
        # btn = (By.XPATH, '//*[text()=" 办结 "]//parent::a')  # 办结按钮
        btn = (By.XPATH, '(//*[@class="ds-page-foot"]//*[contains(@class, "ds-button") and @title])[1]')  # 办结按钮
        self.element_click(btn)
        self.process_send()
        time.sleep(3)
        # self.flow_over_tip()
        self.switch_to_handle(index=-1)
        return LeaveAndVacationAudit(self.driver)

    @allure.step("关闭")
    def close_in_audit(self):
        btn = (By.XPATH, '//*[text()=" 关闭 "]//parent::a')  # 关闭按钮
        self.element_click(btn)
        self.switch_to_handle()
        return LeaveAndVacationAudit(self.driver)
