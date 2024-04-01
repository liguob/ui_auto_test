"""
============================
Author:杨德义
============================
"""
import random
import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit


class PhotosCheck(BasePage):
    """照片审核"""

    # 待审核照片列表卡片勾选按钮
    radio = (By.CSS_SELECTOR, '.ds-platform-card-list input[type=checkbox]')

    @allure.step('按姓名检索待审核照片列表')
    def search_by_stu_name(self, stu_name):
        search_input = (By.CSS_SELECTOR, '.ds-datagrid-header-right input[placeholder*=姓名]')  # 学员姓名input检索框
        search_btn = (By.CSS_SELECTOR, '.search-button')   # 学员姓名检索按钮
        self.clear_then_input(search_input, stu_name)
        self.excute_js_click_ele(search_btn)
        time.sleep(0.5)

    @allure.step('单个学员照片审核同意')
    def single_agree(self):
        stu_photo = (By.XPATH, '//*[@role="tabpanel" and not(@aria-hidden)]//div[@class="name"]')
        agree_single_btn = (By.XPATH, '//div[@class="btn_item" and text()="同意"]')  # 单个同意按钮
        self.move_and_move_to_click(stu_photo, agree_single_btn)

    @allure.step('单个学员照片审核不同意')
    def single_disagree(self):
        stu_photo = (By.XPATH, '//*[@role="tabpanel" and not(@aria-hidden)]//div[@class="name"]')
        agree_single_btn = (By.XPATH, '//div[@class="btn_item" and text()="不同意"]')  # 单个同意按钮
        self.move_and_move_to_click(stu_photo, agree_single_btn)
        reason_input = (By.XPATH, '//textarea')
        self.edit_ele_text(loc=reason_input, value="自动化测试头像不合格")
        self.locator_dialog_btn(btn_name="确认退回")

    @change_reset_implicit()
    @allure.step('批量学员照片审核同意')
    def batch_agree(self):
        self.locator_button("批量审核")
        all_select = (By.XPATH, '//*[@class="el-checkbox__inner"]')
        self.element_click(all_select)
        self.locator_dialog_btn(btn_name="同意")

    @change_reset_implicit()
    @allure.step('批量学员照片审核不同意')
    def batch_disagree(self):
        self.locator_button("批量审核")
        all_select = (By.XPATH, '//*[@class="el-checkbox__inner"]')
        self.element_click(all_select)
        self.locator_dialog_btn(btn_name="不同意")
        reason_input = (By.XPATH, '//textarea')
        self.edit_ele_text(loc=reason_input, value="自动化测试头像不合格")
        self.locator_dialog_btn(btn_name="确认退回")

    @property
    @change_reset_implicit(1.5)
    @allure.step('获取未审核照片卡片数')
    def to_check_cards_count(self):
        to_check_card_loc = (By.CSS_SELECTOR, '.ds-platform-card-item')  # 未审核照片卡片
        to_check_cards = self.driver.find_elements(*to_check_card_loc)
        return len(to_check_cards)
