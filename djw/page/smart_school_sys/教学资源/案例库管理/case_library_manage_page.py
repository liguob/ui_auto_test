"""
============================
Author:杨德义
============================
"""
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from pathlib import Path
from random import randint
import sys
import time
import random
import allure

_data_path = Path(__file__).resolve(strict=True).parents[0]/'_data'


class CaseLibraryManagePage(BasePage):
    """案例库管理列表页"""

    new_upload_file_path = str(_data_path/'附件.docx')

    keyword_search_input = (By.CSS_SELECTOR, '.search-input input')  # 案例库列表名称关键字检索框
    case_search_btn = (By.CSS_SELECTOR, '.search-button')  # 案例搜索按钮

    add_case_button = (By.CSS_SELECTOR, '.ds-button[title=新增]')  # 新增案例按钮
    case_name_input = (By.XPATH, '//*[contains(text(), "案例")]/..//following-sibling::*//input')  # 案例新增/编辑页-案例名称
    case_author_input = (By.XPATH, '//*[contains(text(), "作者")]/..//following-sibling::*//input')  # 案例新增/编辑页-作者
    class_name_input = (By.XPATH, '//*[contains(text(), "班次名称")]/..//following-sibling::*//input')  # 案例新增/编辑页-班次名称
    case_radio_select = (By.CSS_SELECTOR, '.el-radio__inner')  # 案例新增页-分类单选按钮
    case_radio_no_selected = (By.CSS_SELECTOR, '[role=radio]:not(.is-checked) .el-radio__label')  # 案例编辑页-未选中的分类单选按钮文本
    case_introduce = (By.CSS_SELECTOR, '.el-textarea__inner')  # 案例新增页-简要介绍文本输入
    upload_button = (By.XPATH, '//*[contains(text(),"文件上传")]/parent::a')  # 案例新增页-文件上传按钮
    case_save_button = (By.CSS_SELECTOR, '.ds-button[title=保存]')   # 案例新增页-保存按钮

    case_edit = (By.CSS_SELECTOR, '[class*=is-scrolling] [title=编辑]')  # 案例库列表首个编辑按钮

    case_delete = (By.CSS_SELECTOR, '[class*=is-scrolling] [title=删除]')  # 案例库列表首个删除按钮
    delete_confirm = (By.CLASS_NAME, 'el-button--primary')  # 案例删除弹框确认元素

    @allure.step('案例名关键字检索案例列表')
    def search_case(self, keyword=' '):
        self.locator_search_input(placeholder='案例名称', value=keyword, enter=True, times=2)
        return self

    @allure.step('进入案例新增页')
    def go_add_case_page(self):
        self.excute_js_click_ele(self.add_case_button)
        self.switch_to_handle(index=-1)

    @allure.step('设置新增案例信息')
    def set_new_case_info(self, name='ydy测试案例', author='ydy',
                          class_name='ydy测试班次', introduce_text='ydy案例介绍', upload=False):
        self.clear_then_input(self.case_name_input, name)
        self.clear_then_input(self.case_author_input, author)
        self.clear_then_input(self.class_name_input, class_name)
        self.driver.execute_script('arguments[0].click();', self.wait_presence_eles(self.case_radio_select)[randint(1, 7)-1])
        self.clear_then_input(self.case_introduce, introduce_text)

        if upload:
            if sys.platform == "win32":
                self.excute_js_click_ele(self.upload_button)
                self.upload(self.new_upload_file_path)
            else:
                self.upload_input_file_no_click((By.CSS_SELECTOR, '.ds-button~input'), self.new_upload_file_path)

    @allure.step('新增案例')
    def set_new_case(self, case_name, upload=False):
        self.go_add_case_page()
        self.set_new_case_info(case_name, upload=upload)
        self.excute_js_click_ele(self.case_save_button)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('编辑案例')
    def edit_case(self):
        """
        更新分类
        返回更新分类文本
        """
        self.excute_js_click_ele(self.case_edit)
        self.switch_to_handle(index=-1)
        to_update_radio = random.choice(self.driver.find_elements(*self.case_radio_no_selected))
        selected_radio_text =  to_update_radio.text.strip()
        self.poll_click(to_update_radio)
        self.poll_click(self.case_save_button)
        self.switch_to_handle(index=-2)
        return selected_radio_text

    @property
    @allure.step('获取案例列表分类文本')
    def category_text(self):
        category = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=case_category__value]')
        return self.driver.find_element(*category).text.strip()

    @allure.step('编辑案例断言')
    def msg_edit_case(self):
        self.switch_to_handle(index=-1)
        res = [self.get_ele_value(loc) for loc in (self.case_name_input, self.case_author_input, self.class_name_input, self.case_introduce)]
        if sys.platform == "win32":
            annex_loc = (By.XPATH, '(//*[@class="el-table__row"]//td)[2]')  # 案例新增/编辑页附件全名
            res.append(self.trim_text(annex_loc))
        return res

    @allure.step('删除案例')
    def delete_case(self):
        self.excute_js_click_ele(self.case_delete)
        self.excute_js_click_ele(self.delete_confirm)
        return self
