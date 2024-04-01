"""
============================
Author:杨德义
============================
"""
import allure
from djw.page.smart_school_sys.对外培训.经费管理.funds_manage import FundsManage
from selenium.webdriver.common.by import By
from collections import namedtuple
import json


class FundsSummary(FundsManage):
    """对外培训经费汇总页面类"""

    # 增加项预算小计
    budget_add_sum = (By.CSS_SELECTOR, '[ctrl-id=budget_add_sum] [class*=budget_add_sum__value]')
    # 增加项结算小计
    settlement_add_sum = (By.CSS_SELECTOR, '[ctrl-id=settlement_add_sum] [class*=settlement_add_sum__value]')
    # 减免项预算小计
    budget_sub_sum = (By.CSS_SELECTOR, '[ctrl-id=budget_sub_sum] [class*=budget_sub_sum__value]')
    # 减免项结算小计
    settlement_sub_sum = (By.CSS_SELECTOR, '[ctrl-id=settlement_sub_sum] [class*=settlement_sub_sum__value]')
    # 预算合计
    budget_sum = (By.CSS_SELECTOR, '[ctrl-id=budget_sum] [class*=budget_sum__value]')
    # 结算合计
    settlement_sum = (By.CSS_SELECTOR, '[ctrl-id=settlement_sum] [class*=settlement_sum__value]')

    @property
    @allure.step('获取经费汇总详情小计数值具名元组')
    def summary_detail_data(self):
        locators = (
            self.budget_add_sum,
            self.settlement_add_sum,
            self.budget_sub_sum,
            self.settlement_sub_sum,
            self.budget_sum,
            self.settlement_sum)
        SummaryDetail = namedtuple('SummaryDetail',
                                   'budget_add_sum settlement_add_sum budget_sub_sum settlement_sub_sum budget_sum settlement_sum')
        return SummaryDetail._make([float(self.get_ele_text_visitable(locator)) for locator in locators])

    @allure.step('进入班次经费汇总表单页')
    def go_funds_summary_form(self, class_name, class_type='当前班次'):
        self.search_class(class_name, class_type)
        self.locator_view_button(button_title='查看', id_value=class_name)
        self.switch_to_handle(index=-1)
        return self
