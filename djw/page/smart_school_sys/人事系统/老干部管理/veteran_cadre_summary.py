"""
============================
Author:杨德义
============================
"""
import allure
import json
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage
from selenium.webdriver.common.by import By
from collections import namedtuple


class VeteranCadreSummary(PersonnelSysPage):
    """老干部统计页面类"""

    @property
    @allure.step('获取老干部统计具名元组数值')
    def summary_data(self):
        total_num = (By.CSS_SELECTOR, '[class*=total_retire_num__value]')
        retire_num = (By.CSS_SELECTOR, '[class*=retire_cadre_num__value]')
        retired_num = (By.CSS_SELECTOR, '[class*=retired_cadre_num__value]')
        retired_worker_num = (By.CSS_SELECTOR, '[class*=retired_worker_num__value]')

        locators = (total_num, retire_num, retired_num, retired_worker_num)
        SummaryData = namedtuple('SummaryData', ['total_num', 'retire_num', 'retired_num', 'retired_worker_num'])

        return SummaryData._make([json.loads(self.driver.find_element(*loc).text.strip()) for loc in locators])
