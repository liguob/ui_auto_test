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
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage
from common.decorators import change_reset_implicit


class RuleManagePage(PersonnelSysPage):
    """规章制度管理页面类"""
    tip_success = (By.XPATH, '//*[@*="el-message el-message--success"]')  # 成功提示

    @allure.step('点击新增规章制度')
    def click_add_rule(self):
        from djw.page.smart_school_sys.人事系统.规章制度.规章制度管理.addrule import AddRulePage
        btn_add = (By.XPATH, '//*[contains(text(),"新增")]/parent::a')
        self.element_click(btn_add)
        self.switch_to_handle()
        return AddRulePage(self.driver)

    @allure.step('批量删除规章制度')
    def batch_delete_rules(self):
        btn_delete = (By.XPATH, '//*[@*="ds-panel-header"]//*[contains(text(),"删除")]/..')
        self.excute_js_click(btn_delete)
        return self

    @allure.step('删除规章制度')
    def delete_rule(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step('下载文件')
    def download_file(self, index=1):
        btn_down = (By.XPATH, '(//*[@*="el-table__fixed-right"]//span[text()=" 下载 "]/..)[{}]'.format(index))
        self.excute_js_click(btn_down)
        return self

    @allure.step('编辑规章制度')
    def into_edit_rule(self, index=1):
        from djw.page.smart_school_sys.人事系统.规章制度.规章制度管理.addrule import AddRulePage
        self.locator_view_button(button_title="编辑", id_value=str(index))
        self.switch_to_handle()
        return AddRulePage(self.driver)

    @allure.step('搜索规章制度')
    def search_rule(self, title):
        input_search = (By.XPATH, '//div[@class="ds-supersearch-input"]/*/input')
        self.clear_input_enter(input_search, title)
        time.sleep(0.5)
        self.wait_presence_list_data(explicit_timeout=20)
        return self

    @allure.step('获取规章制度列表项信息')
    def get_rule_list_infos(self):
        item = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[{}]')
        list_items = list(map(lambda x: (item[0], item[1].format(x)), range(3, 7)))
        title = ('title', 'publish_date', 'publisher', 'dept')
        try:
            value = self.publish_get_info(*list_items, t=title)
            return value
        except Exception as e:
            return []

    @property
    @change_reset_implicit()
    @allure.step('获取规章制度管理/查看列表检索表单结果条数')
    def table_searched_count(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        return len(self.driver.find_elements(*tr))

