import typing
from common.tools_packages import *
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.后勤管理.用餐管理.对外班次用餐申请.out_class_dinner_apply import OutClassDinnerApply


class DinnerSummary(OutClassDinnerApply):

    @allure.step('检索用餐统计')
    def search(self, dinner_type: typing.Literal['早餐', '午餐', '晚餐'] = ''):
        """
        :param dinner_type: 检索关键词
        """
        return super().search(dinner_type)

    @allure.step('用餐餐别检索申请人')
    def go_search_applyer(self, applyer_name: str):
        """
        :param applyer_name: 申请人姓名
        """
        category_count = (By.XPATH, '//*[contains(@class, "is-scrolling")]//*[contains(@style, "cursor") and text()!=""]')
        self.excute_js_click_ele(category_count)
        from selenium.webdriver.common.keys import Keys
        self.locator_search_input(placeholder='请输入申请人', value=applyer_name+Keys.ENTER)
        return self

    @property
    @change_reset_implicit()
    @allure.step('用餐餐别申请人检索匹配表单条数')
    def table_count_searched_applyer(self):
        tr = (By.CSS_SELECTOR, '.el-dialog [class*=is-scrolling] tr')
        return len(self.driver.find_elements(*tr))
