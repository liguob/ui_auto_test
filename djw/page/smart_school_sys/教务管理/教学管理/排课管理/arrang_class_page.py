import sys
from time import sleep
from selenium.webdriver.common.by import By
from common.base_page import BasePage
import allure


class ArrangeClassPage(BasePage):
    """排课管理页"""

    # 排课管理页未开始班次 tab
    not_started_class_tab = (By.XPATH, '//*[@role="tablist"]//*[contains(text(),"未开始班次")]')
    # 排课管理页当前班次 tab
    current_class_tab = (By.XPATH, '//*[@role="tablist"]//*[contains(text(),"当前班次")]')
    # 排课管理页历史班次 tab
    history_class_tab = (By.XPATH, '//*[@role="tablist"]//*[contains(text(),"历史班次")]')

    # 未开始班次名称搜索框
    class_search_not_started = (By.CSS_SELECTOR, '#pane-NotStarted .el-input__inner[placeholder=请输入班次名称]')
    # 未开始班次名称搜索框右侧搜索按钮
    class_search_button_not_started = (By.CSS_SELECTOR, '#pane-NotStarted .search-button')
    # 未开始班次多班预排课按钮
    multiple_arrang_future_btn = (By.XPATH, '//*[@id="pane-NotStarted"]//*[@class="header-right"]//*[contains(text(), "多班预排课")]')

    # 当前班次名称搜索框
    class_search_current = (By.CSS_SELECTOR, '#pane-underway .el-input__inner[placeholder=请输入班次名称]')
    # 当前班次名称搜索框右侧搜索按钮
    class_search_button_current = (By.CSS_SELECTOR, '#pane-underway .search-button')
    # 当前班次多班预排课按钮
    multiple_arrang_current_btn = (By.XPATH, '//*[@id="pane-underway"]//*[@class="header-right"]//*[contains(text(), "多班预排课")]')
    # 当前班次 tab 检索 tr 行
    current_tr_item = (By.CSS_SELECTOR, '#pane-underway [class*=is-scrolling] tr')
    # 当前班次全选框
    all_checkbox = (By.CSS_SELECTOR, '#pane-underway .el-table__header-wrapper .el-checkbox')

    # 历史班次名称搜索框
    class_search_history = (By.CSS_SELECTOR, '#pane-finished .el-input__inner[placeholder=请输入班次名称]')
    # 历史班次名称搜索框右侧搜索按钮
    class_search_button_history = (By.CSS_SELECTOR, '#pane-finished .search-button')

    # 进入指定班次排课页的排课按钮
    specific_class_arrang_btn = (By.XPATH, '//*[@title="{}"]//ancestor::td[not (contains(@class, "is-hidden"))]//following-sibling::*//*[@title="排课"]')
    # 进入指定班次调课页的调课按钮
    specific_class_transfer_btn = (By.XPATH, '//*[@title="{}"]//ancestor::td[not (contains(@class, "is-hidden"))]//following-sibling::*//*[@title="调课"]')

    # 未开始班次相关
    @allure.step('切至未开始班次tab')
    def switch_not_started_class(self):
        self.excute_js_click_ele(self.not_started_class_tab)
        sleep(1)
        return self

    @allure.step('检索指定未开始班次')
    def search_not_started_class(self, class_name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=class_name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入指定未开始班次排课页')
    def into_specific_not_started_class(self, class_name):
        self.switch_not_started_class()
        self.search_not_started_class(class_name)
        self.excute_js_click_ele((self.specific_class_arrang_btn[0], self.specific_class_arrang_btn[1].format(class_name)))
        sleep(3)
        self.switch_to_handle(index=-1)
        sleep(1)
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage
        return ArrangTestclassPage(driver=self.driver)

    @allure.step('进入指定未开始班次调课页')
    def into_specific_future_transfer_class(self, class_name):
        self.switch_not_started_class()
        self.search_not_started_class(class_name)
        self.excute_js_click_ele((self.specific_class_transfer_btn[0], self.specific_class_transfer_btn[1].format(class_name)))
        sleep(3)
        self.switch_to_handle(index=-1)
        sleep(1)
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage
        return ArrangTestclassPage(driver=self.driver)

    @allure.step('排课管理页-未开始班次-检索指定未开始班次')
    def search_particular_future_class(self, class_name):
        self.switch_not_started_class()
        self.search_not_started_class(class_name)
        return self

    @allure.step('指定未开始班次课表导入')
    def import_course(self, class_name, file):
        """
        :param class_name: 要导入课表文件的班级名
        :param file: 导入课表文件路径
        """
        # self.locator_view_button(button_title='课表导入', id_value=class_name, file=file)
        publish_status = (By.XPATH, '//div[contains(@class,"is-scrolling")]//tr[1]//td[3]/div')  # 发布状态
        arrange_btn = (By.XPATH, '(//td[not (contains(@class, "is-hidden"))]//following-sibling::*//*[@title="排课"])[1]')
        status = self.get_text_implicitly(publish_status)
        if "已发布" == status:
            self.excute_js_click(arrange_btn)
            self.wait_open_new_browser_and_switch()
            cancel_btn = (By.XPATH, '//button/span[contains(text(),"取消发布")]')
            self.element_click(cancel_btn)
            self.wait_success_tip()
            self.close_and_return_page()
        import_btn = (By.CSS_SELECTOR, '#pane-NotStarted [class*=is-scrolling] .small[title*=导入]')
        self.excute_js_click_ele(import_btn)
        sleep(1)
        self.element_click((By.XPATH, '//span[text()="导入数据"]'))
        self._close_windows()
        self.find_elms((By.CSS_SELECTOR, 'input[type=file]'))[-1].send_keys(file)
        sleep(0.5)
        self.locator_dialog_btn('确定')
        sleep(1)
        return self

    @allure.step('指定未开始对外班次课表导入')
    def import_course_out(self, class_name, file):
        import_btn = (By.CSS_SELECTOR, '#pane-futureClassLsit [class*=is-scrolling] .small[title*=导入]')
        self.excute_js_click_ele(import_btn)
        sleep(1)
        self.element_click((By.XPATH, '//span[text()="导入数据"]'))
        self._close_windows()
        self.find_elms((By.CSS_SELECTOR, 'input[type=file]'))[-1].send_keys(file)
        sleep(2)
        self.locator_dialog_btn('确定')
        return self

    @allure.step('关闭课表导入浮页')
    def close_course_import_frame(self):
        close_btn = (By.XPATH, '//*[@role="dialog"]//*[@class="el-dialog__footer"]//*[contains(text(), "关闭")]')
        self.excute_js_click_ele(close_btn)
        sleep(1)

    @allure.step('点击未开始班次多班预排课按钮')
    def click_multiple_arrang_future(self):
        self.excute_js_click_ele(self.multiple_arrang_future_btn)
        return self

    @property
    @allure.step('获取未开始班次列表课程发布状态')
    def publish_status_future(self):
        status = (By.CSS_SELECTOR, '#pane-NotStarted [class*=is-scrolling] [class$=publishStatus]~*')
        return self.driver.find_element(*status).text.strip()

    # 当前班次相关
    @allure.step('切至当前班次tab')
    def switch_current_class(self):
        self.excute_js_click_ele(self.current_class_tab)
        sleep(1)
        return self

    @allure.step('检索指定当前班次')
    def search_current_class(self, class_name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=class_name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入指定当前班次排课页')
    def into_specific_current_class(self, class_name):
        self.switch_current_class()
        self.search_current_class(class_name)
        self.excute_js_click_ele((self.specific_class_arrang_btn[0], self.specific_class_arrang_btn[1].format(class_name)))
        sleep(3)
        self.switch_to_handle(index=-1)
        sleep(1)
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage
        return ArrangTestclassPage(driver=self.driver)

    @allure.step('进入指定当前班次调课页')
    def into_specific_current_transfer_class(self, class_name):
        self.switch_current_class()
        self.search_current_class(class_name)
        self.excute_js_click_ele((self.specific_class_transfer_btn[0], self.specific_class_transfer_btn[1].format(class_name)))
        sleep(3)
        self.switch_to_handle(index=-1)
        sleep(1)
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage
        return ArrangTestclassPage(driver=self.driver)

    @allure.step('点击当前班次多班预排课按钮')
    def click_multiple_arrang_current(self):
        self.excute_js_click_ele(self.multiple_arrang_current_btn)
        return self

    @allure.step('切入多班预排课页')
    def go_multiple_arrang_page(self):
        self.click_multiple_arrang_current().wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage
        return ArrangTestclassPage(driver=self.driver)

    @property
    @allure.step('获取当前班次列表课程发布状态')
    def publish_status_current(self):
        status = (By.CSS_SELECTOR, '#pane-underway [class*=is-scrolling] [class$=publishStatus]~*')
        return self.driver.find_element(*status).text.strip()

    # 历史班次相关
    @allure.step('切至历史班次tab')
    def switch_history_class(self):
        self.excute_js_click_ele(self.history_class_tab)
        sleep(1)
        return self

    @allure.step('检索指定历史班次')
    def search_history_class(self, class_name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=class_name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入指定历史班次排课页')
    def into_specific_history_class(self, class_name):
        self.switch_history_class()
        self.search_history_class(class_name)
        self.excute_js_click_ele((self.specific_class_arrang_btn[0], self.specific_class_arrang_btn[1].format(class_name)))
        sleep(3)
        self.switch_to_handle(index=-1)
        sleep(1)
        from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage
        return ArrangTestclassPage(driver=self.driver)

    @property
    @allure.step('获取历史班次列表课程发布状态')
    def publish_status_history(self):
        status = (By.CSS_SELECTOR, '#pane-underway [class*=is-scrolling] [class$=publishStatus]~*')
        return self.driver.find_element(*status).text.strip()

    @property
    @allure.step('获取操作按钮文本')
    def operate_btns_list(self):
        operate_btn = (By.XPATH, '//*[@class="el-table__body-wrapper is-scrolling-none"]//tr//td[9]')
        original_text = self.trim_text(operate_btn)
        operate_btns = original_text.split('  ')
        return operate_btns

    # 多班预排课相关
    @allure.step('断言未勾选未开始/当前班次多班预排课')
    def msg_click_multiple_arrang(self):
        return self.alert_tip(keyword='请选择班次')
