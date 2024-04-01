"""
============================
Author:杨德义
============================
"""
import allure
from djw.page.smart_school_sys.对外培训.out_traing_page import OutTrainingPage
from selenium.webdriver.common.by import By


class FundsManage(OutTrainingPage):
    """对外培训经费管理页面类"""

    tab_num = {'当前班次': 1, '未开始班次': 2, '历史班次': 3}

    increase_add_btn = (By.CSS_SELECTOR, '[ctrl-id=add]  .ds-subtable-tools [title=新增]')  # 增加项新增按钮
    increase_project_input = (By.CSS_SELECTOR, '[form-name*="teas_externaltrain_fund_add.item"] input')  # 增加项: 项目输入框
    increase_budget_amount = (By.CSS_SELECTOR, '[form-name*="teas_externaltrain_fund_add.budget"] input')  # 增加项: 预算金额输入框
    increase_settlement_amount = (By.CSS_SELECTOR, '[form-name*="teas_externaltrain_fund_add.settlement"] input')  # 增加项: 结算金额输入框
    increase_confirm_btn = (By.CSS_SELECTOR, '[ctrl-id=add] .ds-subtable-box [title=确定]')  # 增加项: 确定按钮
    increase_edit_btn = (By.CSS_SELECTOR, '[ctrl-id=add] .ds-subtable-box [title=编辑]')  # 增加项: 编辑按钮

    deduction_add_btn = (By.CSS_SELECTOR, '[ctrl-id=sub]  .ds-subtable-tools [title=新增]')  # 减免项新增按钮
    deduction_project_input = (By.CSS_SELECTOR, '[form-name*="teas_externaltrain_fund_sub.item"] input')  # 减免项: 项目输入框
    deduction_budget_amount = (By.CSS_SELECTOR, '[form-name*="teas_externaltrain_fund_sub.budget"] input')  # 减免项: 预算金额输入框
    deduction_settlement_amount = (By.CSS_SELECTOR, '[form-name*="teas_externaltrain_fund_sub.settlement"] input')  # 减免项: 结算金额输入框
    deduction_confirm_btn = (By.CSS_SELECTOR, '[ctrl-id=sub] .ds-subtable-box [title=确定]')  # 减免项: 确定按钮
    deduction_edit_btn = (By.CSS_SELECTOR, '[ctrl-id=sub] .ds-subtable-box [title=编辑]')  # 减免项: 编辑按钮

    @allure.step('切换当前/未开始/历史班次 tab')
    def switch_class_tab(self, tag_name='当前班次'):
        self.locator_switch_tag(tag_name=tag_name)
        return self

    @allure.step('检索班次')
    def search_class(self, class_name, class_type='当前班次'):
        self.switch_class_tab(class_type)
        self.locator_tag_search_input(placeholder='请输入班次名称', value=class_name)
        self.locator_tag_search_button()
        self.wait_presence_list_data(self.tab_num[class_type])
        return self

    @allure.step('进入班次经费预算表单页')
    def go_funds_budget_form(self, class_name, class_type='当前班次'):
        self.search_class(class_name, class_type)
        self.locator_view_button(button_title='经费预算', id_value=class_name)
        self.switch_to_handle(index=-1)
        return self

    @allure.step('新增预算')
    def add_budget(self, values: dict):
        self.edit_budget_form(values)
        self.save_form()
        return self

    @allure.step('编辑预算表单')
    def edit_budget_form(self, values: dict):
        # 增加项预算输入
        self.poll_click(self.increase_add_btn)
        self.clear_then_input(self.increase_project_input, values['增加项目名'])
        self.clear_then_input(self.increase_budget_amount, values['增加项预算'])
        self.poll_click(self.increase_confirm_btn)
        # 减免项预算输入
        self.poll_click(self.deduction_add_btn)
        self.clear_then_input(self.deduction_project_input, values['减免项目名'])
        self.clear_then_input(self.deduction_budget_amount, values['减免项预算'])
        self.poll_click(self.deduction_confirm_btn)

    @allure.step('进入班次经费结算表单页')
    def go_funds_settlement_form(self, class_name, class_type='当前班次'):
        self.search_class(class_name, class_type)
        self.locator_view_button(button_title='经费结算', id_value=class_name)
        self.switch_to_handle(index=-1)
        return self

    @allure.step('新增结算')
    def add_settlement(self, values: dict):
        self.edit_settlement_form(values)
        self.save_form()
        return self

    @allure.step('编辑结算表单')
    def edit_settlement_form(self, values: dict):
        # 增加项结算输入
        self.poll_click(self.increase_edit_btn)
        self.clear_then_input(self.increase_settlement_amount, values['增加项结算'])
        self.poll_click(self.increase_confirm_btn)
        # 减免项结算输入
        self.poll_click(self.deduction_edit_btn)
        self.clear_then_input(self.deduction_settlement_amount, values['减免项结算'])
        self.poll_click(self.deduction_confirm_btn)

    @allure.title('表单保存')
    def save_form(self):
        self.locator_button(button_title='保存')
        return self
