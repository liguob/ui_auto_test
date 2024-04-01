"""
============================
Author:杨德义
============================
"""
import allure
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from djw.test_case.smart_school_sys.后勤管理.网上报修.conftest import current_date


class MaintainApply(BasePage):
    """网上报修-网上报修"""

    @allure.step('查询报修申请')
    def search_apply(self, date=current_date()):
        self.locator_search_input(placeholder='标题', value=date)
        self.locator_tag_search_button(times=0.5)
        self.wait_presence_list_data(explicit_timeout=30)
        return self

    def __edit_info(self, values: dict):
        """填写报修申请详情信息"""
        if '报修地点' in values:
            self.locator_text_input(ctrl_id='place', value=values['报修地点'])
        if '故障说明' in values:
            self.locator_text_input(ctrl_id='description', value=values['故障说明'])
        if '维修类别' in values:
            self.locator_select_list_value(ctrl_id='category', value=values['维修类别'])

    @allure.step('新增报修申请')
    def save_apply(self, values: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.__edit_info(values)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        self.explicit_wait_ele_lost(self.WEB_TIP)
        self.switch_to_handle(index=0)
        return self

    @allure.step("选择审批人")
    def chose_checker(self, user):
        user_option = (By.XPATH, f'//*[contains(text(), "{user}")]//ancestor::*[@class="el-tree-node__content"]//*[@class="el-checkbox__input"]')
        choice_result = (By.XPATH, f'//*[@class="fl-box"]//*[contains(text(), "{user}")]')
        btn_yes = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')  # 确认按钮
        self.excute_js_click(user_option)  # 点击审批人复选框
        self.wait_visibility_ele(choice_result)  # 等待选择结果出现
        self.excute_js_click(btn_yes)
        return self

    @allure.step('发送报修申请')
    def send_apply(self, checker, values: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.__edit_info(values)
        self.locator_button(button_title='发送')
        self.process_send(checker=checker)
        self.switch_to_handle(index=-1)
        return self

    @allure.step('修改报修申请')
    def edit_apply(self, reason, values: dict):
        self.locator_view_button(button_title='编辑', id_value=reason)
        self.wait_open_new_browser_and_switch()
        self.__edit_info(values)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        self.explicit_wait_ele_lost(self.WEB_TIP)
        self.switch_to_handle(index=0)
        return self

    @allure.step('删除报修申请')
    def del_apply(self, reason):
        self.locator_view_button(button_title='删除', id_value=reason)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        self.explicit_wait_ele_lost(self.WEB_TIP)
        return self

    @property
    @allure.step('获取报修列表流转情况文本')
    def apply_status(self):
        status = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=status_text__value]')
        return self.driver.find_element(*status).text.strip()

    @property
    @allure.step('获取报修列表流转情况文本列表')
    def apply_status_list(self):
        status = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=status_text__value]')
        return [e.text.strip() for e in self.driver.find_elements(*status)]

    @property
    @allure.step('获取报修列表故障说明')
    def apply_reason(self):
        reason = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=description__value]')
        return self.driver.find_element(*reason).text.strip()
