# encoding=utf-8
"""
============================
Author:何超
Time:2021/4/21   10::00
============================
"""
import time
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class DropManagePage(BasePage):
    """退学管理页面类"""

    menu_drop_manage = (By.XPATH, '//span[contains(text(), "退学管理")]/parent::div')
    tip = (By.XPATH, '//*[contains(text(), "流程已发送到以下人员：")]')
    tip_sure = (By.XPATH, '//*[contains(text(), "流程已发送到以下人员：")]/ancestor::div[@role]//a')
    btn_approve_agree = (By.XPATH, '//*[contains(text(), "审核通过")]/parent::a')  # 审核通过按钮
    approve_disagree_ = (By.XPATH, '//*[contains(text(), "审核不通过")]/parent::a')  # 审核不通过按钮

    @staticmethod
    def _tab_map(tab):
        tab_map = {"未处理": "pane-undisposed", "已处理": "pane-processed"}
        return tab_map[tab]

    @allure.step("切换tab页")
    def switch_tab(self, tab='已处理'):
        tab = (By.XPATH, f'//div[@aria-controls="{self._tab_map(tab)}"]')
        self.excute_js_click_ele(tab)
        return self

    @allure.step("搜索")
    def search_apply_name(self, keyword):
        """keyword:学员姓名/班次名称"""
        self.locator_tag_search_input(placeholder='请输入学员姓名/班次名称', value=keyword, times=2, enter=True)
        return self

    @allure.step("点击审核")
    def click_approve(self, name):
        self.locator_view_button(button_title="审核", id_value=name)
        self.switch_to_handle()
        return self

    @allure.step("点击查看")
    def click_view(self):
        btn_view = (By.XPATH, '//div[@class="el-table__fixed-right"]//a[@title="查看"]')
        self.excute_js_click_ele(btn_view)
        self.switch_to_handle()
        return self

    # @allure.step("点击表单审核的发送并等待选择框出现")
    # def _click_pass_and_choice(self, checker):
    #     box_choice = (By.XPATH, '//*[contains(text(), "请选择办理人")]/parent::div')  # 选择审批人弹窗
    #     btn_yes = (By.XPATH, '//*[contains(text(), "确定")]/parent::a')
    #     self.excute_js_click_ele(self.btn_approve_agree)
    #     # self.explicit_wait_ele_presence(box_choice, explicit_timeout=20)
    #     if self.is_element_exist(box_choice):
    #         if checker.startswith('教务领导'):
    #             jwcjwld = (By.XPATH,
    #                        f'//*[contains(text(), "教务处")]//ancestor::*[@class="el-tree-node__content"]//following-sibling::*[@role]//*[contains(text(), "{checker}")]')
    #             self.poll_click(self.explicit_wait_ele_presence(jwcjwld, explicit_timeout=20))
    #         elif checker.startswith('校领导'):
    #             xld = (By.XPATH,
    #                    f'//*[contains(text(), "校领导")]//ancestor::*[@class="el-tree-node__content"]//following-sibling::*[@role]//*[text()="{checker}"]')
    #             self.poll_click(self.explicit_wait_ele_presence(xld, explicit_timeout=20))
    #         self.excute_js_click_ele(btn_yes)
    #     return self

    @allure.step("审核通过")
    def approve_agree(self, checker):
        """user: 审核人"""
        self.excute_js_click_ele(self.btn_approve_agree)
        self.process_send(checker=checker)
        # self._click_pass_and_choice(checker)
        # self.explicit_wait_ele_presence(self.tip, explicit_timeout=20)
        # self.poll_click(self.explicit_wait_ele_presence(self.tip_sure, explicit_timeout=20))
        self.switch_to_handle(0)
        return self

    @allure.step("审核不同意")
    def approve_disagree(self):
        time.sleep(1)
        button = (By.XPATH, '//a[@title="退回"]')
        self.element_click(button)
        self.input_send_keys(loc=(By.XPATH, '//textarea'), value='退学审核退回')
        self.locator_dialog_btn(btn_name='确定')
        self.switch_to_handle()
        return self

    @allure.step("审核通过结束")
    def approve_agree_and_over(self):
        tip = (By.XPATH, '//*[contains(text(), "文件已办结")]')
        tip_sure = (By.XPATH, '//*[contains(text(), "文件已办结")]/ancestor::*[@class="el-dialog"]//a')
        self.poll_click(self.explicit_wait_ele_presence(self.btn_approve_agree))
        self.process_send()
        self.switch_to_handle(index=-1)
        return self

    @allure.step("获取退学管理列表信息")
    def get_drop_manage_list_info(self, tab='未处理'):
        id_ = self._tab_map(tab)
        name = (By.XPATH, f'//div[@id="{id_}"]//div[contains(@class,"is-scrolling")]//td[2]')  # 学员姓名
        class_name = (By.XPATH, f'//div[@id="{id_}"]//div[contains(@class,"is-scrolling")]//td[3]')  # 班次名称
        title = (By.XPATH, f'//div[@id="{id_}"]//div[contains(@class,"is-scrolling")]//td[4]')  # 标题
        reason = (By.XPATH, f'//div[@id="{id_}"]//div[contains(@class,"is-scrolling")]//td[5]')  # 退学原因
        status = (By.XPATH, f'//div[@id="{id_}"]//div[contains(@class,"is-scrolling")]//td[6]')  # 当前状态
        list_title = ("name", "class_name", "title", "reason", "status")
        try:
            list_info = self.publish_get_info(name, class_name, title, reason, status, t=list_title)
        except Exception:
            return None
        else:
            return list_info

    @allure.step('获取当前状态')
    def status(self, tab='未处理'):
        id_ = self._tab_map(tab)
        current_status = (By.XPATH, f'//div[@id="{id_}"]//div[contains(@class,"is-scrolling")]//td[6]')
        return self.driver.find_element(*current_status).text.strip()

    @allure.step("获取退学管理列表详情信息")
    def get_drop_manage_detail_info(self):
        time.sleep(1)
        drop_key = (By.XPATH, '//tbody//label[@class="ds-form-label"]')
        drop_value = (By.XPATH, '//tbody//div[@class="ds-form-block"]')
        value = self.trim_texts(self.driver.find_elements(*drop_value))
        key = self.trim_texts(self.driver.find_elements(*drop_key))
        dict_info = dict(zip(key, value))
        return dict_info

    @allure.step("进入退学统计")
    def go_drop_count(self):
        from djw.page.smart_school_sys.班主任管理.退学统计.drop_count_page import DropCountPage
        self.excute_js_click_ele(DropCountPage.menu_drop_count)
        return DropCountPage(self.driver)
