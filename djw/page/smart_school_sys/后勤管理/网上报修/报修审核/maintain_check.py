"""
============================
Author:杨德义
============================
"""
from time import sleep

import allure
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from djw.test_case.smart_school_sys.后勤管理.网上报修.conftest import current_date


class MaintainCheck(BasePage):
    """网上报修-报修审核页面类"""

    # 未处理/已处理列表统计数
    pagination = (By.CSS_SELECTOR, '#pane-tab{} .el-pagination__total')

    @allure.step('切至未处理tab')
    def switch_to_handle_tab(self):
        self.locator_switch_tag(tag_name='未处理')
        return self

    @allure.step('切至已处理tab')
    def switch_handled_tab(self):
        self.locator_switch_tag(tag_name='已处理')
        return self

    @allure.step('未处理/已处理列表检索')
    def search(self, date=current_date(), tab_id='#pane-tab1'):
        self.locator_tag_search_input(placeholder='标题', value=date)
        self.locator_tag_search_button()
        tab_num = int(tab_id[-1])
        self.wait_presence_list_data(tab_num=tab_num, explicit_timeout=15)
        return self

    @allure.step('进入指定报修审核页')
    def go_specific_check(self, reason):
        self.switch_to_handle_tab()
        self.search()
        sleep(0.5)
        self.locator_view_button(button_title='审核', id_value=reason)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('审核通过')
    def check_agree(self):
        self.locator_button(button_title='处理完成')
        self.process_send()
        self.switch_to_handle(index=-1)

    @allure.step('审核不通过')
    def check_disagree(self):
        self.locator_button(button_title='退回')
        self.process_send()
        self.clear_and_input(loc=(By.XPATH, '//textarea'), value="退回")
        self.locator_dialog_btn(btn_name="确定")
        self.switch_to_handle(index=-1)

    @property
    @allure.step('未处理检索统计数目')
    def pagination_to_handle(self):
        return self.pagination_count(loc=(self.pagination[0], self.pagination[1].format(1)))

    @property
    @allure.step('已处理检索统计数目')
    def pagination_handled(self):
        return self.pagination_count(loc=(self.pagination[0], self.pagination[1].format(2)))
