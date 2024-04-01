import typing

from selenium.webdriver.common.keys import Keys

from common.tools_packages import *
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class OutClassDinnerCheck(LogisticsManagePage):
    # 未处理/已处理检索表单显示条数
    tr_searched = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] tr')

    @allure.step('切至未处理/已处理')
    def switch_tab(self, tab_name: typing.Literal['未处理', '已处理'] = '未处理'):
        self.locator_switch_tag(tag_name=tab_name)
        return self

    @allure.step('对外班次、校外人员未处理/已处理检索')
    def search_check_list(self, keyword: str = '', tab_num: typing.Literal[1, 2] = 1):
        """
        :param keyword: 检索关键词
        :param tab_num: 第几个标签页
        """
        search_input = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) input[placeholder*=请输入]')
        search_btn = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) .search-button')
        self.clear_then_input(search_input, keyword)
        # self.locator_search_input(placeholder="请输入事由/申请人/所在部门", value=keyword + Keys.ENTER)
        self.poll_click(search_btn)
        time.sleep(1)
        self.wait_presence_list_data(tab_num)
        return self

    @property
    @change_reset_implicit()
    @allure.step('获取对外班次、校外人员未处理/已处理检索条数')
    def table_count_searched(self):
        return len(self.driver.find_elements(*self.tr_searched))

    @property
    @allure.step('获取对外班次、校外人员未处理/已处理审核状态')
    def check_statuses(self) -> typing.List[str]:
        status = (
        By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] [class*=status_text__value]')
        return self.trim_texts(self.driver.find_elements(*status))

    @allure.step('对外班次、校外人员用餐进入审核')
    def go_check(self):
        check_btn = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] .small[title=审核]')
        self.poll_click(check_btn)
        return self

    @allure.step('对外班次、校外人员用餐审核通过')
    def check_pass_dinner(self):
        self.locator_button(button_title='通过')
        self.process_send()
        return self

    @allure.step('对外班次、校外人员用餐审核退回')
    def check_return_dinner(self):
        self.locator_button(button_title='退回')
        self.input_send_keys(loc=(By.XPATH, '//textarea'), value="退回")
        self.locator_dialog_btn(btn_name="确定")
        # self.process_send()
        return self

    @allure.step('对外班次、校外人员用餐审核不通过')
    def check_dispass_dinner(self):
        self.locator_button(button_title='不通过')
        self.process_send()
        return self

    @allure.step('对外班次、校外人员审核未处理/已处理列表导出')
    def export_check_list(self, file_name: typing.Literal['对外班次用餐审核表.xlsx', '校外人员用餐申请表.xlsx']):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name="导出", dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name=file_name)
