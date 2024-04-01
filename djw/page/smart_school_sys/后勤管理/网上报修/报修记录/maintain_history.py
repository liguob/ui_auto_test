"""
============================
Author:杨德义
============================
"""
import allure
from common.base_page import BasePage
from djw.test_case.smart_school_sys.后勤管理.网上报修.conftest import current_date


class MaintainHistory(BasePage):
    """网上报修-报修记录页面类"""

    @allure.step('报修记录检索')
    def search(self, date=current_date()):
        self.locator_tag_search_input(placeholder='标题', value=date)
        self.locator_tag_search_button()
        return self
