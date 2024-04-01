"""
============================
Author:杨德义
============================
"""
import allure
from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from common.decorators import change_reset_implicit


class SchoolrollQuery(BasePage):
    """学籍信息查询"""

    name_input = (By.CSS_SELECTOR, 'input[placeholder=请输入姓名]')  # 姓名检索框
    phone_input = (By.CSS_SELECTOR, 'input[placeholder=请输入手机号码]')  # 手机号码检索框
    politics_select = (By.CSS_SELECTOR, '[item-key*=politics] input[placeholder=请选择]')  # 政治面貌下拉框
    nation_select = (By.CSS_SELECTOR, '[item-key*=nation] input[placeholder=请选择]')  # 民族下拉框
    select_items = (By.XPATH,
                    '//*[@x-placement]//*[contains(@class, "el-select-dropdown__item")]//*[contains(text(), "{}")]')  # 政治面貌/民族下拉选项
    politics_caret = (By.CSS_SELECTOR, '[item-key*=politics] .el-select__caret')  # 政治面貌下拉符
    nation_caret = (By.CSS_SELECTOR, '[item-key*=nation] .el-select__caret')  # 民族下拉符
    search_btn = (
    By.XPATH, '//*[contains(@class, "where-row")]//*[contains(@class, "ds-button")]//*[contains(text(), "查询")]')

    @allure.step('收起政治面貌下拉框')
    def fold_politics(self):
        caret = self.driver.find_element(*self.politics_caret)
        for _ in range(2):
            self.driver.execute_script('arguments[0].click();', caret)

    @allure.step('收起民族下拉框')
    def fold_nation(self):
        caret = self.driver.find_element(*self.nation_caret)
        for _ in range(2):
            self.driver.execute_script('arguments[0].click();', caret)

    @allure.step('搜索学员学籍信息')
    def search_schoolroll(self, **query_fields):
        """query_fields:姓名/政治面貌/民族构成的单一或组合字典"""
        keys = query_fields.keys()

        if 'name' in keys:
            name_value = query_fields['name']
            self.clear_then_input(self.name_input, name_value + '\n')
            time.sleep(0.5)
            self.wait_presence_list_data(explicit_timeout=10)

        if 'politics' in keys:
            self.chose_list_option(option_text=query_fields['politics'])
            time.sleep(0.5)
            self.wait_presence_list_data(explicit_timeout=10)
            self.fold_politics()

        if 'nation' in keys:
            self.chose_list_option(option_text=query_fields['nation'])
            time.sleep(0.5)
            self.wait_presence_list_data(explicit_timeout=10)
            self.fold_nation()

        if 'phone' in keys:
            phone_value = query_fields['phone']
            self.clear_then_input(self.phone_input, phone_value + '\n')
            time.sleep(0.5)
            self.wait_presence_list_data(explicit_timeout=10)
        self.wait_listDataCount_searched()
        return self

    @property
    @change_reset_implicit(implicit_timeout=1.5)
    @allure.step('获取学员学籍检索结果表单条数')
    def table_count_searched(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        table_data = self.driver.find_elements(*tr)
        table_count = len(table_data)
        return table_count

    @allure.step('进入学籍详情查看页')
    def go_schoolroll_detail(self):
        view_btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=查看]')
        self.excute_js_click_ele(view_btn)
        self.switch_to_handle(index=-1)
        time.sleep(1)
        return self

    @property
    @change_reset_implicit()
    @allure.step('获取学员所属班次名称列表')
    def classes_name(self):
        class_name = (By.XPATH, '//div[@class="classitem-name"]')
        return self.get_ele_text_visitable(class_name)

    @allure.step('查询学员姓名')
    def search_student_name(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name, enter=True)
        return self

    @allure.step('查看学员信息')
    def view_student(self, student_name):
        self.locator_view_button(button_title='查看', id_value=student_name)
        self.wait_open_new_browser_and_switch()
        name = (By.CSS_SELECTOR, f"[title='{student_name}']")
        return self.get_ele_text_visitable(name)
