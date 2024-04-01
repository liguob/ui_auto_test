# encoding=utf-8
"""
============================
Author:何超
Time:2021/4/15   10:30
============================
"""
import time
from collections import namedtuple
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class LeaveDetailPage(BasePage):
    """请假描述页面"""

    # 未处理tab统计条数
    pagination_no_handle = (By.CSS_SELECTOR, '#pane-tab1 .el-pagination__total')
    # 已处理tab统计条数
    pagination_handled = (By.CSS_SELECTOR, '#pane-tab2 .el-pagination__total')

    input_search_processed = (
        By.XPATH, '//div[@id="pane-tab2"]//div[@class="search-input el-input"]/input')  # 搜索输入框（已处理）
    btn_apply = (By.CSS_SELECTOR, '.el-table__fixed-right .small')  # 审核按钮
    tip_box_title = (By.XPATH, '//*[contains(text(),"流程已发送到以下人员：")]')  # 同意/退回的弹窗提示
    tip_point_user = (By.CSS_SELECTOR, '.userbox *')  # 提示窗指向下一用户
    btn_tip_box_yes = (By.XPATH, '//*[@role="dialog"]//*[contains(text(),"确定")]/parent::*')  # 提示框确认按钮
    # 请选择办理人窗口
    btn_choice_user_box_no = (By.XPATH, '//*[@aria-label="请选择办理人"]//*[contains(text(),"取消")]/parent::*')  # 选择审批人弹窗取消按钮

    @staticmethod
    def _tab_map(tab):
        tab_map = {"未处理": "pane-tab1", "已处理": "pane-tab2"}
        return tab_map[tab]

    @allure.step("获取页面标题")
    def get_handle_title(self):
        """获取页面标题"""
        btn_not_process = (By.XPATH, '//div[@id="tab-tab1"]')  # 未处理
        self.wait_visibility_ele(btn_not_process)
        title = self.driver.title  # 获取学员请假审批列表主页的标签页标题
        return title

    @allure.step("获取请假描述信息")
    def get_leave_detail_info(self, tab="未处理"):
        """获取请假描述信息(未处理)"""
        id = self._tab_map(tab)
        stu_name = (By.XPATH, '//div[@id="{}"]//div[contains(@class,"is-scrolling")]//td[2]/div'.format(id))  # 学员姓名
        class_name = (By.XPATH, '//div[@id="{}"]//div[contains(@class,"is-scrolling")]//td[3]/div'.format(id))  # 班次名称
        leave_date = (By.XPATH, '//div[@id="{}"]//div[contains(@class,"is-scrolling")]//td[4]/div'.format(id))  # 请假时间
        leave_reason = (By.XPATH, '//div[@id="{}"]//div[contains(@class,"is-scrolling")]//td[5]/div'.format(id))  # 请假事由
        leave_type = (By.XPATH, '//div[@id="{}"]//div[contains(@class,"is-scrolling")]//td[6]/div'.format(id))  # 请假类型
        leave_status = (By.XPATH, '//div[@id="{}"]//div[contains(@class,"is-scrolling")]//td[7]/div'.format(id))  # 审核状态
        title = ("学员姓名", '班次名称', '请假时间', '请假事由', '请假类型', '审核状态')
        time.sleep(1)
        detail_info = self.publish_get_info(stu_name, class_name, leave_date, leave_reason, leave_type, leave_status,
                                            title=title)
        return detail_info

    @allure.step("搜索学生")
    def search_stu(self, stu_name):
        self.locator_tag_search_input(placeholder='姓名', value=stu_name, enter=True)
        return self

    @allure.step("进入请假审核页面")
    def into_leave_apply(self, name):
        self.locator_view_button(button_title='弹出流程意见框', id_value=name)
        time.sleep(2)
        return self

    @allure.step("审核同意")
    def leave_agree(self, user: str):
        self.locator_button(button_title='同意')
        # 判断是否有选择办理人弹窗信息
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            self.locator_search_input(placeholder='输入名称', value=user)
            time.sleep(2)
            self.locator_tree_node_click(node_value=user)
            time.sleep(2)
            self.locator_dialog_btn(btn_name='确定')
            self.locator_dialog_btn(btn_name='确定', dialog_title='流程已发送到以下人员：')
        # self.locator_search_input(placeholder='输入名称', value=user)
        else:
            self.locator_dialog_btn(btn_name='确定', dialog_title='流程已发送到以下人员：')
        return self

    @allure.step("审核同意并结束，获取成功提示")
    def leave_agree_and_over(self):
        # tip_success = (By.XPATH, '//span[contains(text(), "文件已办结")]')  # 发送成功的提示
        btn_agree_and_over = (By.XPATH, '//a[@title="同意并结束"]')  # 同意并结束按钮
        self.wait_visibility_ele(btn_agree_and_over)  # 等待请假单窗口同意并结束按钮出现
        self.excute_js_click_ele(btn_agree_and_over)  # 点击同意并结束按钮
        self.process_send()
        # self.explicit_wait_ele_presence(tip_success, explicit_timeout=20)  # 等待成功提示窗口标题出现
        # time.sleep(0.5)
        # self.poll_click(self.explicit_wait_ele_presence(self.btn_tip_box_yes, explicit_timeout=20))  # 点击成功提示窗口的确认按钮
        return self

    @allure.step("退回请假申请")
    def leave_disagree(self):
        self.locator_button(button_title='退回')
        self.locator_search_input(placeholder='请输入退回原因', value='请假退回')
        self.locator_dialog_btn(btn_name='确定')
        time.sleep(2)
        return self

    @allure.step("进入已处理tab页")
    def into_processed(self):
        btn_processed = (By.XPATH, '//div[@id="tab-tab2"]')  # 已处理
        self.wait_visibility_ele(btn_processed)  # 等待已处理tab按钮出现
        self.excute_js_click_ele(btn_processed)  # 点击已处理tab按钮
        return self

    @allure.step('获取未处理检索统计条数')
    def get_pagination_no_handle(self, stu_name):
        return self.into_no_handle().search_stu(stu_name, tab='未处理').pagination_count(loc=self.pagination_no_handle)

    @allure.step('获取已处理检索统计条数')
    def get_pagination_handled(self, stu_name):
        return self.into_processed().search_stu(stu_name, tab='已处理').pagination_count(loc=self.pagination_handled)
