"""
============================
Author:杨德义
============================
"""
import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit


class DeceasedManage(BasePage):
    """已故人员管理页面类"""

    name_input = (By.CSS_SELECTOR, 'input[placeholder=姓名]')
    search_btn = (By.CSS_SELECTOR, '.search-button')
    sex_input = (By.CSS_SELECTOR, 'input[placeholder=请输入性别]')
    dept_input = (By.CSS_SELECTOR, 'input[placeholder=请输入部门]')
    nation_input = (By.CSS_SELECTOR, 'input[placeholder=请输入民族]')

    def __edit_info(self, data: dict):
        """编辑已故人员信息"""
        keys = data.keys()
        if '姓名' in keys:
            into_search_btn = (By.CSS_SELECTOR, '[ctrl-id=person] i')  # 进入已故人员选择界面按钮
            self.poll_click(into_search_btn)
            name = data["姓名"]
            person_loc = (By.XPATH, '//*[contains(@class,"tree-node")]//*[contains(text(),"{}")]'.format(name))
            # person = self.explicit_wait_ele_presence(person_loc, explicit_timeout=15)
            self.locator_search_input(placeholder='输入关键字进行过滤', times=0.5, value=name+'\n')
            self.poll_click(person_loc)
            time.sleep(0.5)
            confirm_btn = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')
            self.poll_click(confirm_btn)
            time.sleep(0.5)
        if '死亡日期' in keys:
            self.locator_date(ctrl_id='dead_date', value=data['死亡日期'])
        self.locator_button(button_title='保存')

    @allure.step('编辑已故人员信息')
    def edit_info(self, data: dict):
        self.__edit_info(data)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('新增已故人员')
    def add_deceased(self, data: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.edit_info(data)
        return self

    @allure.step('搜索已故人员')
    def search_deceased(self, info: dict):
        keys = info.keys()
        if 'name' in keys:
            self.clear_then_input(self.name_input, info['name'])
        if 'sex' in keys:
            self.clear_then_input(self.sex_input, info['sex'])
        if 'dept' in keys:
            self.clear_then_input(self.dept_input, info['dept'])
        if 'nation' in keys:
            self.clear_then_input(self.nation_input, info['nation'])
        self.locator_tag_search_button()
        return self
