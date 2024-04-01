# encoding = utf-8
"""
============================
Author:何超
============================
"""
import time
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from djw.page.smart_school_sys.教务管理.教学管理.教学计划.draw_teach_plan_page import DrawTeachPlanPage


class TeachPlanPage(BasePage):
    """教学计划"""
    tab_no_start_class = (By.XPATH, '//div[@id="tab-tab1"]')  # 未开始班次的tab按钮
    tab_current_class = (By.XPATH, '//div[@id="tab-tab2"]')  # 当前班次的tab按钮
    tab_history_class = (By.XPATH, '//div[@id="tab-tab3"]')  # 历史班次的tab按钮
    loading = (By.XPATH, '//div[@type="loading"]')  # 进度条

    @staticmethod
    def _tab_map(tab):
        tab_map = {"未开始班次": "pane-tab1", "当前班次": "pane-tab2", "历史班次": "pane-tab3"}
        return tab_map[tab]

    @allure.step("进入教学计划的当前/未开始/历史班次页面")
    def switch_to_tab(self, tab='当前班次'):
        """
        :param tab:当前班次/未开始班次/历史班次
        """
        id_ = self._tab_map(tab)
        tab = (By.XPATH, '//div[@aria-controls="{}"]'.format(id_))  # 当前/未开始/历史班次的tab按钮
        self.element_click(tab)
        return self

    @allure.step("获取未开始/当前/历史班次的计划信息")
    def get_class_plan_info(self, tab='未开始班次'):
        """
        :param tab:当前班次/未开始班次/历史班次
        """
        tab_id = self._tab_map(tab)
        items = (By.XPATH, '//div[@id="{}"]//div[contains(@class,"is-scrolling")]'.format(tab_id) + '//td[{}]')
        list_items = list(map(lambda x: (items[0], items[1].format(x)), range(3, 9)))
        title = ('班次编号', '班次名称', '培训日期', '班主任', '上课地点', '学员人数')
        time.sleep(0.5)
        list_info = self.publish_get_info(*list_items, title=title)  # 班次编号, 班次名称, 培训日期, 班主任, 上课地点, 学员人数
        return list_info

    @allure.step("搜索未开始/当前/历史班次")
    def search_class_plan_by_class(self, class_name, tab='未开始班次'):
        """
        :param class_name:班次名称
        :param tab:当前班次/未开始班次/历史班次
        :return:返回查询结果的列表项信息
        """
        id_ = self._tab_map(tab)
        input_search = (By.XPATH, f'//div[@id="{id_}"]//div[@class="search-input el-input"]//input')  # 搜索输入框
        self.wait_visibility_ele(input_search)
        time.sleep(0.5)
        self.clear_then_input(input_search, class_name+'\n')
        time.sleep(1)
        return self

    @allure.step("进入未开始/当前/历史班次的制定计划")
    def into_class_draw_plan(self, tab='未开始班次', index=1):
        """
        :param tab:当前班次/未开始班次/历史班次
        :param index:第几个按钮，从1开始
        """
        id_ = self._tab_map(tab)
        btn_draw_plan = (By.XPATH, f'(//*[@id="{id_}"]//*[contains(@class, "is-scrolling")]//*[contains(@class, "small")]//*[contains(text(), "制订")])[{index}]')  # 第n个列表项的制订(计划)按钮
        time.sleep(0.5)
        if not self.is_element_exist(btn_draw_plan):
            btn_draw_plan = (By.XPATH, f'(//*[@id="{id_}"]//*[contains(@class, "is-scrolling")]//*[contains(@class, "small")]//*[contains(text(), "修改")])[{index}]')  # 第n个列表项的修改(计划)按钮
        self.excute_js_click_ele(btn_draw_plan)
        time.sleep(1)
        self.switch_to_handle(index=-1)
        return DrawTeachPlanPage(self.driver)

    @allure.step('进入未开始班次教学计划查看页')
    def view_class_draw_plan(self, index=1):
        """
        :param index:第几个按钮，从1开始
        """
        id_ = self._tab_map(tab='未开始班次')
        btn_view_plan = (By.XPATH, f'(//div[@id="{id_}"]//div[@class="el-table__fixed-right"]//a[@title="查看"])[{index}]')  # 第n个列表项的查看(计划)按钮
        self.excute_js_click_ele(btn_view_plan)
        time.sleep(1)
        self.switch_to_handle(index=-1)
        return DrawTeachPlanPage(self.driver)
