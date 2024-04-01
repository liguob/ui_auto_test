"""
============================
Author:杨德义
============================
"""
import allure
from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from common.file_path import wait_file_down_and_clean
from common.decorators import change_reset_implicit


class PersonnelSummaryPage(BasePage):
    """人事系统-人事信息统计"""

    # 人事信息统计各子菜单
    summary_submenu = (By.XPATH, '//*[@class="ds-aside-menu-item-box" and @title="{}"]')

    # 导出按钮
    export_btn = (By.CSS_SELECTOR, '.ds-button[title=导出]')
    # 导出设置页确定按钮
    export_confirm_btn = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')

    def go_sub_summary(self, title):
        """title: 人事统计子菜单标题"""
        with allure.step(f'进入{title}统计页'):
            title_loc = (self.summary_submenu[0], self.summary_submenu[1].format(title))
            self.move_to_ele(title_loc)  # 移动滚动条使子菜单可见再点击
            self.wait_presence_ele(title_loc).click()
            time.sleep(0.5)
        self.wait_presence_list_data(explicit_timeout=15)  # 等待子统计页面加载

    @allure.step('人事子统计信息导出')
    def export_sub_summary(self):
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(*self.export_btn))
        return self

    @allure.step('判断是否需要导出确认')
    def judge_whether_export_confirm(self, filename):
        """name:文件全名(含后缀格式)"""
        self.driver.implicitly_wait(time_to_wait=0.5)
        exist_export_confirm = self.driver.find_elements(*self.export_confirm_btn)
        if exist_export_confirm:
            self.excute_js_click_ele(exist_export_confirm[0])
        self.driver.implicitly_wait(self.Default_Implicit_Timeout)
        return wait_file_down_and_clean(filename)

    @allure.step('获取子统计表单信息')
    def get_summary_table_info(self, summary_key):
        """key：子统计项"""
        items = (By.XPATH, '//div[contains(@*,"is-scrolling")]//td[{}]')
        table_items = list(map(lambda x: (items[0], items[1].format(x)), range(2, 4)))  # 统计项、人数
        title = (summary_key, 'num')
        value = self.publish_get_info(*table_items, t=title)
        return value

    @property
    @change_reset_implicit(2)
    @allure.step('获取子统计列表行数据')
    def list_data(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        return self.driver.find_elements(*tr)
