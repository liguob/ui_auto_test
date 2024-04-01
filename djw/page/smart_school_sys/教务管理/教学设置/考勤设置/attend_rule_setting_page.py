# encoding=utf-8
"""
============================
Author:何凯
Time:2021/4/25
============================
"""
import time
from time import sleep
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class AttendRuleSettingPage(BasePage):
    """考勤规则设置页面类"""

    add_btn = (By.XPATH, '//a[@title="新增"]')  # 新增
    delete_btn = (By.XPATH, '//a[@title="删除"]')  # 删除

    edit_operations = (By.XPATH, '//div[contains(@class,"scrolling-none")]//a[@title="编辑"]')  # 编辑
    enable_operations = (By.XPATH, '//div[contains(@class,"scrolling-none")]//a[contains(@title,"启用")]')  # 启用
    disable_operation = (By.XPATH, '//div[contains(@class,"scrolling-none")]//a[contains(@title,"禁用")]')  # 禁用
    delete_operation = (By.XPATH, '//div[contains(@class,"scrolling-none")]//a[@title="删除"]')  # 删除

    confirm_delete_btn = (By.XPATH, '//span[contains(text(),"确定")]/parent::button')  # 删除弹框确定按钮
    cancel_delete_btn = (By.XPATH, '//span[contains(text(),"取消")]/parent::button')  # 删除弹框取消按钮
    position_span = (By.XPATH, '//span[text()=" 定位 "]')  # 定位
    sign_code_span = (By.XPATH, '//span[text()=" 签到码 "]')  # 签到码
    qr_code_span = (By.XPATH, '//span[text()=" 二维码 "]')  # 二维码

    course_mode_span = (By.XPATH, '//span[text()=" 课程模式 "]')  # 课程模式
    am_pm_mode_span = (By.XPATH, '//span[text()=" 午别模式 "]')  # 午别模式
    fix_time = (By.XPATH, '//span[contains(text(),"午别固定时间")]')
    course_time = (By.XPATH, '//span[contains(text(),"午别课程时间")]')
    attend_span = (By.XPATH, '//span[text()=" 出勤 "]')  # 出勤时间
    late_span = (By.XPATH, '//span[text()=" 迟到 "]')  # 迟到
    serious_late_span = (By.XPATH, '//span[text()=" 晚到（严重迟到） "]')  # 晚到
    leave_early_span = (By.XPATH, '//span[text()=" 早退 "]')  # 早退
    sign_out_span = (By.XPATH, '//span[text()=" 签退 "]')
    date_inputs = (By.XPATH, '//input[@placeholder="请输入"]')

    attend_time_start = (By.XPATH, '(//input[@placeholder="请输入"])[1]')  # 出勤开始时间
    attend_time_end = (By.XPATH, '(//input[@placeholder="请输入"])[2]')  # 出勤结束时间
    late_time_start = (By.XPATH, '(//input[@placeholder="请输入"])[3]')  # 迟到开始时间
    late_time_end = (By.XPATH, '(//input[@placeholder="请输入"])[4]')  # 结束开始时间
    serious_late_start = (By.XPATH, '(//input[@placeholder="请输入"])[5]')  # 晚到开始时间

    serious_late_end = (By.XPATH, '(//input[@placeholder="请输入"])[6]')  # 晚到结束时间
    early_leave_start = (By.XPATH, '(//input[@placeholder="请输入"])[7]')  # 早退开始时间
    early_leave_end = (By.XPATH, '(//input[@placeholder="请输入"])[8]')  # 早退结束时间
    sign_out_start = (By.XPATH, '(//input[@placeholder="请输入"])[9]')  # 签退开始时间
    sign_out_end = (By.XPATH, '(//input[@placeholder="请输入"])[10]')  # 签退结束时间
    close_btn = (By.XPATH, '//a[@title="关闭"]')
    after_tip = (By.XPATH, '//div[@role="alert"]/i[contains(@class,"el-icon")]/following::p')  # 删除or保存后的提示

    @allure.step("进入新增页面")
    def into_add_rule_page(self):
        self.excute_js_click(self.add_btn)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        return self

    @allure.step("进入编辑页面")
    def into_edit_rule_page(self):
        # ele = self.driver.find_elements(*self.edit_operations)[0]
        # self.driver.execute_script("arguments[0].click();", ele)
        self.excute_js_click(self.edit_operations)
        self.switch_to_handle(index=-1)
        sleep(1)
        return self

    @allure.step("删除考勤规则")
    def delete_attend_rule(self):
        self.driver.execute_script("arguments[0].click();", self.find_elem(self.delete_operation))
        self.driver.execute_script("arguments[0].click();", self.find_elem(self.confirm_delete_btn))
        return self

    @allure.step("考勤类型设置")
    def set_attend_type(self, *args):
        for arg in args:
            if arg == "定位":
                self.locator_select_radio(ctrl_id='attend_type', value=arg)
            if arg == "二维码":
                self.locator_select_radio(ctrl_id='attend_type', value=arg)
        return self

    @allure.step("考勤模式设置")
    def set_attend_mode(self, mode):
        self.locator_select_radio(ctrl_id='attend_mode', value=mode)
        return self

    @allure.step('设置刷新时间')
    def set_attend_refresh_time(self, times: int = None):
        if times:
            self.locator_text_input(ctrl_id='refresh_second', value=times)
        return self

    @allure.step("考勤状态设置")
    def set_attend_status(self, args):
        for status in args:
            self.locator_select_radio(ctrl_id='attend_status', value=status)
        return self

    @allure.step("清空后输入")
    def clear_after_input(self, loc, text):
        self.input_send_keys(loc, Keys.CONTROL + 'a')
        self.input_send_keys(loc, Keys.DELETE)
        self.input_send_keys(loc, text)
        return self

    @allure.step("关闭")
    def close(self):
        self.excute_js_click(self.close_btn)
        return self

    @allure.step("启用考勤规则")
    def enable_attend_rule(self):
        """启用第一条规则"""
        ele = self.driver.find_element(*self.enable_operations)
        self.driver.execute_script("arguments[0].click();", ele)
        self.wait_success_tip()
        return self

    @allure.step("禁用考勤规则")
    def disable_attend_rule(self):
        """禁用考勤规则，如果没有则启用第一条规则"""
        eles = self.driver.find_elements(*self.disable_operation)
        if len(eles) != 0:
            self.driver.execute_script("arguments[0].click();", eles[0])
        else:
            pass
        return self

    @allure.step
    def get_enable_rule_count(self):
        eles = self.driver.find_elements(*self.enable_operations)
        return len(eles)

    @allure.step("出勤时间设置")
    def set_attend_date(self, kwargs: dict = None):
        if kwargs is None:
            kwargs = {}
        keys = kwargs.keys()
        if "出勤开始时间" in keys:
            self.clear_after_input(self.attend_time_start, kwargs["出勤开始时间"])
        if "出勤结束时间" in keys:
            self.clear_after_input(self.attend_time_end, kwargs["出勤结束时间"])
        if "迟到开始时间" in keys:
            self.input_send_keys(self.late_time_start, kwargs["迟到开始时间"])
        if "迟到结束时间" in keys:
            self.clear_after_input(self.late_time_end, kwargs["迟到结束时间"])
        if "晚到开始时间" in keys:
            self.clear_after_input(self.serious_late_start, kwargs["晚到开始时间"])
        if "晚到结束时间" in keys:
            self.clear_after_input(self.serious_late_end, kwargs["晚到结束时间"])
        if "早退开始时间" in keys:
            self.clear_after_input(self.early_leave_start, kwargs["早退开始时间"])
        if "早退结束时间" in keys:
            self.clear_after_input(self.early_leave_end, kwargs["早退结束时间"])
        if "签退开始时间" in keys:
            self.clear_after_input(self.sign_out_start, kwargs["签退开始时间"])
        if "签退结束时间" in keys:
            self.clear_after_input(self.sign_out_end, kwargs["签退结束时间"])
        self.locator_button("保存")
        self.wait_success_tip()
        self.close_current_browser()
        self.switch_to_window(-1)
        return self

    def get_enable_disable_num(self):
        enable_eles = self.driver.find_elements(*self.enable_operations)
        disable_eles = self.driver.find_elements(*self.disable_operation)
        return enable_eles, disable_eles

    @allure.step('批量全选删除考勤规则')
    def del_more_attend(self):
        self.locator_view_select_all()
        self.locator_tag_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
