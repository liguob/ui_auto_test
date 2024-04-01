# -*- coding: utf-8 -*-

"""
============================
Author: 何凯
Time:2021/4/22
============================
"""
import random
from time import sleep
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class SourceOccupyListPage(BasePage):
    """资源占用一览表"""

    campus_select = (By.XPATH, '//div[@class="el-select search_campus"]//input')  # 校区选择
    campus_dd = (By.XPATH, '//div[@x-placement]//div[@class="el-scrollbar"]//span')
    floor_select = (By.XPATH, '//div[@class="el-select search_floor"]//input')  # 楼宇选择
    floor_dd = (By.XPATH, '//div[@x-placement]//div[@class="el-scrollbar"]//span')

    cycle_type_select = (By.XPATH, '//div[@class="el-select search_type"]//input')  # 查询类型选择
    cycle_type_dd = (By.XPATH, '//div[@x-placement]//div[@class="el-scrollbar"]//span')
    before_button = (By.XPATH, '//a[@class="checkWeek ds-button"]/span[contains(text(),"上")]')  # 上一周or上一月
    after_button = (By.XPATH, '//a[@class="checkWeek ds-button"]/span[contains(text(),"下")]')  # 下一周or下一月
    date_input = (By.XPATH, '//div[@class="el-input is-disabled"]/input')  # date显示框
    table_first_head = (By.XPATH, '//div[@class="head_title"]')  # 资源占用列表第一行title

    can_occupy_tds = (By.XPATH, '//div[@class="table_data"]//div[@class="add_jia"]')  # 可以占用的表格
    manual_occupy_tds = (By.XPATH, '//div[@class="today_data_warp stateThree"]//div[contains(@class,"data_hover")]')  # 手动占用的表格
    course_occupy_tds = (By.XPATH, '//div[@class="today_data_warp stateOne"]//div[contains(@class,"data_hover")]')  # 课程占用的表格
    conflict_occupy_tds = (By.XPATH, '//div[@class="today_data_warp stateTwo"]//div[contains(@class,"data_hover")]')  # 冲突占用的表格
    td_title = ("可以占用", '手动占用', '课程占用', '占用冲突')  # 资源占用列表四种占用方式title
    confirm_btn = (By.XPATH, '//span[contains(text(),"保存")]')  # 保存
    cancel_btn = (By.XPATH, '//span[contains(text(),"关闭")]')  # 关闭

    occupy_reason_input = (By.XPATH, '//div[@ctrl-id="reason"]//input')  # 占用原因
    contact_person_input = (By.XPATH, '//div[@ctrl-id="contact_text"]//input')  # 联系人
    phone_input = (By.XPATH, '//div[@ctrl-id="phone"]//input')  # 电话
    save_btn = (By.XPATH, '//i[@class="iconfont icon-baocun"]')  # 保存
    close_btn = (By.XPATH, '//a[@ds-event="sytem_form_close"]')  # 关闭
    after_occupy_tip = (By.XPATH, '//div[@role="alert"]//p[@class="el-message__content"]')  # 占用/解除占用弹框提示

    @allure.step("刷新")
    def refresh_web(self):
        self.refresh()
        sleep(1)
        return self

    def switch_back_frame(self):
        self.switch_to_frame_back()
        return self

    @allure.step("校区选择")
    def select_campus(self, campusname):
        """点击校区下拉框并选择"""
        self.element_click(self.campus_select)
        self.click_select_span(campusname)
        return self

    @allure.step("楼宇选择")
    def select_floor(self, floorname):
        self.element_click(self.floor_select)
        self.click_select_span(floorname)
        return self

    @allure.step("点击上一周or上一月")
    def click_before(self):
        self.excute_js_click(self.before_button)
        sleep(1)
        return self

    @allure.step("点击下一周or下一月")
    def click_after(self):
        self.excute_js_click(self.after_button)
        sleep(1)
        return self

    @allure.step("获取所有表格元素")
    def get_eles_all_tds(self):
        super().__init__(driver=self.driver, implicitly_timeout=1)
        can_occupy = self.driver.find_elements(*self.can_occupy_tds)
        manual_occupy = self.driver.find_elements(*self.manual_occupy_tds)
        course_occupy = self.driver.find_elements(*self.course_occupy_tds)
        conflict_occupy = self.driver.find_elements(*self.conflict_occupy_tds)
        super().__init__(driver=self.driver)
        tds = (can_occupy, manual_occupy, course_occupy, conflict_occupy)
        td_eles = dict(zip(self.td_title, tds))  # 字典格式分类获取所有表格元素对象
        return td_eles

    @allure.step("随机获取元素")
    def get_random_td_ele(self, title="可以占用"):
        """随机获取一个可以占用的元素"""
        td_eles = self.get_eles_all_tds()
        return random.choice(td_eles[title])

    @allure.step("点击可占用表格")
    def click_occupy_td(self, ele):
        self.driver.execute_script("arguments[0].click();", ele)
        sleep(1)
        return self

    @allure.step("获取元素title属性")
    def get_ele_attr_title(self, ele):
        return ele.get_attribute("title")

    @allure.step("解除占用")
    def cancel_occupy_confirm(self, ele):
        """点击传参进入的元素，并切换出iframe，点击确定按钮"""
        self.action_chains.move_to_element(ele).perform()
        # self.Mouse_hover_to_ele(ele)
        cancle = (By.XPATH, '//a[@class="ds-button"]/span[contains(text(),"解除占用")]')
        self.excute_js_click(cancle)
        return self

    @allure.step("保存")
    def save_occupy(self):
        self.excute_js_click(self.save_btn)
        return self

    @allure.step("输入占用原因")
    def input_manual_occupy_reason(self, reason='', contacter='', phone=''):
        self.input_send_keys(self.occupy_reason_input, reason)
        self.input_send_keys(self.contact_person_input, contacter)
        self.input_send_keys(self.phone_input, phone)
        return self

    @allure.step("关闭")
    def close_occupy(self):
        self.click_to_clickable_ele(self.close_btn)
        return self

    @allure.step("获取date显示框的内容")
    def get_date_input_text(self):
        date = self.find_elem(self.date_input).get_attribute('value')
        return date

    @allure.step("获取资源占用列表的head")
    def get_search_head_texts(self):
        flag = self.judge_element_whether_existence(self.table_first_head)
        if flag:
            self.move_to_ele(self.table_first_head)
            return self.trim_texts(self.driver.find_elements(*self.table_first_head))
        else:
            return False

    @allure.step("获取占用后的提示")
    def get_tip(self):
        try:
            text = self.driver.find_element(*self.after_occupy_tip).text
            return text
        except Exception:
            return False

    def get_campus_info(self):
        self.wait_presence_ele(self.can_occupy_tds)
        self.element_click(self.campus_select)
        sleep(0.5)
        return self.trim_texts(self.driver.find_elements(*self.campus_dd))

    def get_floor_info(self):
        self.wait_presence_ele(self.can_occupy_tds)
        self.element_click(self.floor_select)
        sleep(0.5)
        return self.trim_texts(self.driver.find_elements(*self.floor_dd))

    def get_cycle_info(self):
        # self.wait_presence_ele(self.can_occupy_tds)
        self.element_click(self.cycle_type_select)
        sleep(0.5)
        return self.trim_texts(self.driver.find_elements(*self.cycle_type_dd))

    def click_select_span(self, value):
        select = (By.XPATH, '//div[@x-placement]//div[@class="el-scrollbar"]//span[text()="{}"]'.format(value))
        self.excute_js_click(select)
        return self
