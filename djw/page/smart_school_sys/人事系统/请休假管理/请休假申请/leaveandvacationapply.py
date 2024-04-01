# encoding=utf-8
"""
============================
Author:
Time:
============================
"""
import datetime
import random
import time
import allure
from selenium.webdriver.common.by import By
from common.random_tool import randomTool
from djw.page.smart_school_sys.人事系统.请休假管理.请休假申请.leaveandvacation import LeaveAndVacationPage


class LeaveAndVacationApply(LeaveAndVacationPage):
    """请休假申请页面类"""
    success_tip = (By.XPATH, '//*[contains(@class,"el-message el-message--success")]')  # 成功提示
    name = (By.XPATH, '//*[@ctrl-id="person"]//span/span')  # 姓名
    unit = (By.XPATH, '//*[@ctrl-id="unit"]//span/span')  # 所在单位
    dept = (By.XPATH, '//*[@ctrl-id="dept"]//span/span')  # 所在部门

    @allure.step('编辑请休假表单')
    def edit_vacation_apply_form(self, **kwargs):
        random_stime = randomTool.random_date_time_between('now', '+1d')
        random_etime = random_stime + datetime.timedelta(days=1)
        leave_type = ['事假', '病假', '婚假', '产假', '丧假', '年假']
        value_dict = {"type": random.choice(leave_type),
                      "stime": datetime.datetime.strftime(random_stime, "%Y-%m-%d %H:%M"),
                      "etime": datetime.datetime.strftime(random_etime, "%Y-%m-%d %H:%M"),
                      "reason": randomTool.random_str()}
        value_dict.update(kwargs)
        leave_type = (By.XPATH, '//*[@ctrl-id="type"]//span/span')  # 请休假类型
        leave_date = (By.XPATH, '//div[@ctrl-id="leave"]/div/div')  # 请假日期
        sdate = (By.XPATH, '//*[@placeholder="开始日期"]')  # 请休假开始日期
        stime = (By.XPATH, '(//*[@placeholder="开始时间"])[2]')  # 请休假开始时间
        edate = (By.XPATH, '//*[@placeholder="结束日期"]')  # 请休假结束日期
        etime = (By.XPATH, '(//*[@placeholder="结束时间"])[2]')  # 请休假结束时间
        time_btn_yes = (By.XPATH, '//span[contains(text(),"确定")]/..')
        reason = (By.XPATH, '//*[@ctrl-id="cause"]//textarea')  # 请休假事由
        file = (By.XPATH, '//*[@ctrl-id="file"]//*[text()=" 文件上传 "]/parent::a')  # 文件上传
        self.excute_js_click_ele(leave_type)
        time.sleep(1)
        leave_type_tag = (By.XPATH, '//*[@x-placement]//*[contains(text(), "{}")]'.format(value_dict['type']))
        self.excute_js_click_ele(leave_type_tag)
        time.sleep(1)
        self.element_click(leave_date)
        sdate_value, stime_value = value_dict['stime'].split(' ')
        edate_value, etime_value = value_dict['etime'].split(' ')
        self.clear_and_input_enter(sdate, sdate_value)
        self.clear_and_input_enter(stime, stime_value)
        self.clear_and_input_enter(edate, edate_value)
        self.clear_and_input_enter(etime, etime_value)
        self.element_click(time_btn_yes)
        self.clear_and_input_enter(reason, value_dict['reason'])
        title = ("name",  "dept")
        time.sleep(1)
        value = self.publish_get_info(self.name, self.dept, t=title)[0]
        value_dict.update(value)
        return value_dict

    @allure.step("获取请休假信息")
    def get_leave_and_vacation_detail_info(self):
        leave_type = (By.XPATH, '//*[@ctrl-id="type"]//span/span')  # 请休假类型
        time = (By.XPATH, '//*[@ctrl-id="leave"]//span')  # 请休假时间
        reason = (By.XPATH, '//*[@ctrl-id="cause"]//span/span')  # 请休假事由
        title = ("name", "unit", "dept", "type", "time", "reason")
        value = self.publish_get_info(self.name, self.unit, self.dept, leave_type, time, reason, t=title)
        return value[0]

    @allure.step("选择审批人")
    def choice_leave_audit_user(self, user):
        user_option = (By.XPATH, f'//*[text()="{user}"]/../../label/span[@*="el-checkbox__input"]')
        choice_result = (By.XPATH, f'//table[@class="el-table__body"]//td[2]/div[text()="{user}"]')
        btn_yes = (By.XPATH, '//span[text()="确定"]/..')  # 确认按钮
        yes = (By.XPATH, '//div[@*="el-dialog__header"]/../div/a')
        self.excute_js_click_ele(user_option)
        self.wait_visibility_ele(choice_result)
        self.excute_js_click(btn_yes)
        # self.flow_tip()
        return self

    @allure.step("保存请休假")
    def save_vacation_apply(self, **kwargs):
        btn = (By.XPATH, '//span[text()=" 保存 "]/parent::a')
        value = self.edit_vacation_apply_form(**kwargs)
        self.element_click(btn)
        self.explicit_wait_ele_presence(self.WEB_TIP)
        self.explicit_wait_ele_lost(self.WEB_TIP)
        self.switch_to_handle(0)
        return value

    @allure.step('更新请休假事由')
    def update_reason(self, reason: str = randomTool.random_str()):
        reason_loc = (By.XPATH, '//*[@ctrl-id="cause"]//textarea')
        self.clear_then_input(reason_loc, reason)
        save_btn = (By.XPATH, '//span[text()=" 保存 "]/parent::a')
        self.poll_click(save_btn)
        self.explicit_wait_ele_lost(self.WEB_TIP)
        self.switch_to_handle(0)
        return reason

    @allure.step("提交请休假")
    def commmit_vacation_apply(self, user: str, **kwargs):
        send_btn = (By.XPATH, '(//*[@class="ds-page-foot"]//*[@class="ds-button"])[2]')
        please_select_checker = (By.XPATH, '//*[@aria-label="请选择办理人"]//*[@class="el-dialog__title" and contains(text(), "请选择办理人")]')  # 请选择办理人弹框
        confirm_flow_tip = (By.XPATH, '//*[contains(@class, "sendFlow")]//*[contains(text(), "确定")]')  # 流转弹框提示确认按钮
        value = self.edit_vacation_apply_form(**kwargs)
        # 发送申请
        self.poll_click(self.explicit_wait_ele_presence(send_btn))
        print(user)
        self.process_send(checker=user)
        # # 根据可选审核人数量, 进行不同操作
        # if self.is_element_exist(confirm_flow_tip, implicitly_timeout=4):  # 可选人仅 1 人: 直接发送
        #     self.poll_click(self.driver.find_element(*confirm_flow_tip))
        # elif self.is_element_exist(please_select_checker, implicitly_timeout=2):  # 可选人 > 1人: 弹窗选择
        #     self.choice_leave_audit_user(user)
        #     self.poll_click(self.explicit_wait_ele_presence(confirm_flow_tip, explicit_timeout=30))
        time.sleep(4)
        self.switch_to_handle(index=0)
        return value

    @allure.step("关闭")
    def close_vacation_apply(self):
        btn = (By.XPATH, '//span[text()=" 关闭 "]/parent::a')
        self.element_click(btn)
        self.switch_to_handle()
        return LeaveAndVacationPage(self.driver)

    @allure.step('获取指定请假申请流转状态')
    def get_status(self, reason):
        """reason:请假事由"""
        reason = (By.XPATH, f'//*[contains(@class, "is-scrolling")]//*[contains(@class, "personnel_leave_leavelistdata_cause__value") and contains(text(), "{reason}")]//ancestor::td//following-sibling::td//*[contains(@class, "personnel_leave_leavelistdata_status_text__value")]')
        return self.driver.find_element(*reason).text
