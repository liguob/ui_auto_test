"""
============================
Author:杨德义
============================
"""
import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit


class TeachPlanMoulds(BasePage):
    """教学计划模板"""

    add_mould_btn = (By.CSS_SELECTOR, '.ds-button[title=新增]')  # (模板)新增按钮
    mould_name_input = (By.CSS_SELECTOR, '[form-name*=name] input')  # 新增/编辑模板浮窗名称输入框
    whether_enable = (By.XPATH, '//*[contains(@form-name, "is_enable")]//*[contains(text(), "{}")]')  # 新增/编辑模板浮窗是否启用选项
    mould_save_btn = (By.CSS_SELECTOR, '.ds-button[title=保存]')  # 新增/编辑模板浮窗保存按钮
    mould_search_input = (By.CSS_SELECTOR, '.search-input input')  # 模板列表搜索框
    mould_search_btn = (By.CSS_SELECTOR, '.search-button')  # 模板列表搜索按钮

    @allure.step('新增教学计划模板')
    def add_mould(self, mould_data: dict):
        self.excute_js_click_ele(self.add_mould_btn)
        self.edit_save_mould_info(mould_data)
        return self

    @allure.step('编辑教学计划模板信息')
    def edit_save_mould_info(self, mould_info: dict):
        keys = mould_info.keys()

        if '名称' in keys:
            self.clear_then_input(self.mould_name_input, mould_info['名称'])
        if '是否启用' in keys:
            self.excute_js_click_ele((self.whether_enable[0], self.whether_enable[1].format(mould_info['是否启用'])))

        self.save_mould()
        return self

    @allure.step('保存教学计划模板信息')
    def save_mould(self):
        self.excute_js_click_ele(self.mould_save_btn)
        return self

    @allure.step('搜索教学计划模板')
    def search_mould(self, mould_name):
        self.locator_search_input(placeholder='请输入模版名称', value=mould_name, enter=True)
        return self

    @allure.step('修改模板')
    def update_mould(self, update_info: dict):
        mould_edit_btn = (By.CSS_SELECTOR, '.is-scrolling-none .small[title=编辑]')  # 模板编辑按钮
        self.excute_js_click_ele(mould_edit_btn)
        self.edit_save_mould_info(update_info)
        self.explicit_wait_ele_presence(self.WEB_TIP)
        self.explicit_wait_ele_lost(self.WEB_TIP)
        return self

    @allure.step('删除模板')
    def delete_mould(self):
        mould_del_btn = (By.CSS_SELECTOR, '.is-scrolling-none .small[title=删除]')  # 模板删除按钮
        confirm_delete_btn = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(), "确定")]')  # 模板删除确认按钮
        self.excute_js_click_ele(mould_del_btn)
        self.excute_js_click_ele(confirm_delete_btn)
        self.wait_success_tip()
        return self

    @allure.step('进入模板设置页')
    def go_mould_set_page(self):
        mould_set_btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=模版设置]')  # 模板设置按钮
        self.excute_js_click_ele(mould_set_btn)
        self.switch_to_handle(index=-1)
        time.sleep(0.5)

    @property
    @change_reset_implicit(1)
    @allure.step('获取模板检索结果表单条数')
    def table_count_searched(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        table_data = self.driver.find_elements(*tr)
        table_count = len(table_data)
        return table_count
