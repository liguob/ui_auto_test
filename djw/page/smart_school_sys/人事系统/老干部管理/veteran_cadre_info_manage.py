"""
============================
Author:杨德义
============================
"""
import allure
import time
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage
from selenium.webdriver.common.by import By
from common.file_path import wait_file_down_and_clean


class VeteranCadreInfoManage(PersonnelSysPage):
    """老干部信息管理页面类"""

    add_btn = (By.CSS_SELECTOR, '.header-right .ds-button[title=新增]')
    select_option = (By.XPATH, '//*[contains(@class, "el-select-dropdown__item")]//*[contains(text(), "{}")]')
    edit_btn = (By.CSS_SELECTOR, '.el-table__fixed-right .small[title=编辑]')
    del_btn = (By.CSS_SELECTOR, '.el-table__fixed-right .small[title=删除]')

    def __edit_info(self, data: dict):
        """编辑离退休人员信息"""
        keys = data.keys()
        if '姓名' in keys:
            self.locator_text_input(ctrl_id='name', value=data['姓名'])
        if '性别' in keys:
            self.chose_list_option(data['性别'])
        if '身份证号' in keys:
            self.locator_text_input(ctrl_id='id_card', value=data['身份证号'])
        if '出生日期' in keys:
            self.locator_date(ctrl_id='birthday', value=data['出生日期'])
        if '民族' in keys:
            self.chose_list_option(data['民族'])
        if '政治面貌' in keys:
            self.chose_list_option(data['政治面貌'])
        if '人员状态' in keys:
            self.chose_list_option(data['人员状态'])
        if '电话1' in keys:
            self.locator_text_input(ctrl_id='phone_one', value=data['电话1'])
        if '离退情况' in keys:
            self.chose_list_option(data['离退情况'])
        if '退离身份' in keys:
            self.chose_list_option(data['退离身份'])
        self.locator_button(button_title='保存')

    @allure.step('修改离退休人员信息')
    def edit_info(self, data: dict):
        self.__edit_info(data)
        # self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('搜索离退休人员')
    def search_veteran_cadre(self, data: dict):
        """data：离退情况/人员状态/退离身份/'姓名组合字典或姓名字典"""
        keys = data.keys()
        if '离退情况' in keys:
            self.chose_list_option(data['离退情况'])
        if '人员状态' in keys:
            self.chose_list_option(data['人员状态'])
        if '退离身份' in keys:
            self.chose_list_option(data['退离身份'])
        if '姓名' in keys:
            search_input = (By.CSS_SELECTOR, '.header-right .search-input input')
            search_btn = (By.CSS_SELECTOR, '.header-right .search-button')
            self.clear_then_input(search_input, data['姓名'])
            self.poll_click(search_btn)
            time.sleep(1)
        return self

    @allure.step('新增离退休人员')
    def add_veteran_cadre(self, data: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.edit_info(data)
        return self

    @allure.step('修改离退休人员')
    def edit_veteran_cadre(self, name, data: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.edit_info(data)
        return self

    @allure.step('删除离退休人员')
    def del_veteran_cadre(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导出离退休人员')
    def export_veteran_cadres(self):
        export_btn = (By.CSS_SELECTOR, '.header-right .ds-button[title=导出]')
        self.poll_click(export_btn)
        export_confirm_btn = (
        By.XPATH, '//*[@aria-label="导出设置"]//*[contains(@class,"ds-button")]//*[contains(text(),"导出")]')
        if self.judge_element_whether_existence(export_confirm_btn):
            self.element_click(export_confirm_btn)
        # self.locator_dialog_btn(btn_name='确定')
        return wait_file_down_and_clean(file_name='老干部信息.xlsx', times=15)

    @allure.step('预导入离退休人员')
    def pre_import_veteran_cadres(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        # preview_import_input = (By.CSS_SELECTOR, '.header-right .ds-button[title=预导入]~input')
        # self.driver.find_element(*preview_import_input).send_keys(file)
        tr_data = (By.CSS_SELECTOR, '[role=dialog] [class*=is-scrolling] tr')
        self.explicit_wait_ele_presence(tr_data, explicit_timeout=30)
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('关闭老干部导入浮页')
    def close_course_import_frame(self):
        # close_btn = (By.CSS_SELECTOR, '.el-dialog__close')
        # self.poll_click(close_btn)
        self.locator_dialog_btn(btn_name='关闭')

    @property
    @allure.step('获取老干部信息管理列表电话1文本')
    def first_phone(self):
        first_phone_loc = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=personnel_cadre_phone_one__value]')
        first_phone_text = self.driver.find_element(*first_phone_loc).text.strip()
        return first_phone_text

    @property
    @allure.step('获取老干部信息管理列表表单条数')
    def table_count_searched(self):
        tr = (By.CSS_SELECTOR, '.ds-panel-body [class*=is-scrolling] tr')
        self.driver.implicitly_wait(time_to_wait=1)
        table_data = self.driver.find_elements(*tr)
        self.driver.implicitly_wait(self.Default_Implicit_Timeout)
        table_count = len(table_data)
        return table_count
