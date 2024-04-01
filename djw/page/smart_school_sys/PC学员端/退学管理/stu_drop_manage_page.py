# encoding=utf-8
"""
============================
Author:何超
Time:2021/4/21   10:00
============================
"""
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.random_tool import randomTool


class StuDropManagePage(BasePage):
    """pc学员端的退学管理"""
    menu_drop_manage = (By.XPATH, '//div[@title="退学管理"]')

    def click_drop_apply(self):
        btn_drop_apply = (By.XPATH, '//a[@title="退学申请"]')
        self.element_click(btn_drop_apply)
        self.switch_to_handle()
        return self

    def get_drop_apply_info(self):
        name = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[2]/div')
        class_name = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[3]/div')
        title = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[4]/div')
        status = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[5]/div')
        list_title = ("name", "class_name", "title", "status", "list_title")
        info = self.publish_get_info(name, class_name, title, status, t=list_title)
        return info

    def click_stu_drop_edit(self):
        btn_edit = (By.XPATH,'//div[@class="el-table__fixed-right"]//a[@title="编辑"]')
        self.element_click(btn_edit)
        return self

    def click_stu_drop_detail(self):
        btn_detail = (By.XPATH,'//div[@class="el-table__fixed-right"]//a[@title="详情"]')
        self.element_click(btn_detail)
        return self

    def edit_stu_drop_apply_form(self):
        """有bug"""
        input_name=(By.XPATH,'')
        dict_info={"reason":randomTool.random_str(),"name":self.get_ele_attr(input_name, 'value'),"date":''}
        return self