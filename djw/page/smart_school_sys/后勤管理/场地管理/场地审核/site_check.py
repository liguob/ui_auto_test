import typing
from common.tools_packages import *
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class SiteCheck(LogisticsManagePage):
    """场地审核"""
    # 未处理/已处理检索表单显示条数
    tr_searched = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] tr')

    @allure.step('切至未处理/已处理')
    def switch_tab(self, tab_name: typing.Literal['未处理', '已处理'] = '未处理'):
        self.locator_switch_tag(tag_name=tab_name)
        return self

    @allure.step('未处理/已处理检索')
    def search_check_list(self, activity_name, count: int = 1):
        """
        :param activity_name: 活动名称
        :param count:检索预期条数
        """
        self.locator_tag_search_input(placeholder='活动名称', value=activity_name)
        search_btn = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) .search-button')
        self.poll_click(search_btn)
        self.wait_listDataCount_searched(tr=self.tr_searched, count=count)
        return self

    @property
    @change_reset_implicit()
    @allure.step('获取未处理/已处理检索条数')
    def table_count_searched(self):
        return len(self.driver.find_elements(*self.tr_searched))

    @property
    @allure.step('获取未处理/已处理审核状态')
    def check_status(self):
        status = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] [class*=status_text__value]')
        return self.trim_text(status)

    @allure.step('进入审核')
    def go_check(self):
        check_btn = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] .small[title=审核]')
        self.poll_click(check_btn)
        self.wait_open_new_browser_and_switch()
        sleep(1.5)
        return self

    @allure.step('场地审核同意')
    def check_agree_site(self):
        self.locator_button(button_title='同意')
        self.process_send()
        self.switch_to_handle(index=-1)
        return self

    @allure.step('场地审核退回')
    def check_return_site(self):
        # return_btn = (By.XPATH, '//span[contains(text(),"退回")]')
        # self.element_click(return_btn)
        self.locator_button(button_title='退回')
        self.input_send_keys(loc=(By.XPATH, '//textarea'), value="退回")
        self.locator_dialog_btn(btn_name="确定")
        self.wait_browser_close_switch_latest()
        sleep(0.5)
        # self.switch_to_handle(index=-1)
        return self

    @allure.step('场地审核未处理/已处理列表导出')
    def export_check_list(self, file_name='场地审核.xlsx'):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name="导出", dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name=file_name)
