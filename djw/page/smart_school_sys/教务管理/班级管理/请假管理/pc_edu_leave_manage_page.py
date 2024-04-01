import time
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.decorators import change_reset_implicit


class PcEduLeaveManagePage(BasePage):
    """教务管理-请假管理"""

    @allure.step("查询请假学员")
    def search_stu(self, stu_name):
        self.locator_tag_search_input(placeholder='姓名', value=stu_name, enter=True)
        return self

    @allure.step("进入请假审核页")
    def into_leave_check(self, value):
        self.locator_view_button(button_title='审核', id_value=value)
        return self

    @allure.step("二审同意请假")
    def leave_agree(self, user):
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
        else:
            self.locator_dialog_btn(btn_name='确定', dialog_title='流程已发送到以下人员：')
        return self

    @allure.step("三审同意请假")
    def leave_agree_last(self):
        self.locator_button(button_title='同意')
        self.locator_dialog_btn(btn_name='确定')
        return self
