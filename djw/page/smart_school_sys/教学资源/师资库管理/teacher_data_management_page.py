# -*- coding: utf-8 -*-

"""
============================
Author: 何凯
Time:2021/4/19
============================
"""
import time
from time import sleep
import allure
import random
from common.file_path import wait_file_down_and_clean
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.decorators import change_reset_implicit


class TeacherDataManagePage(BasePage):
    """
    师资库管理
    """

    _find_input = (By.XPATH, '//input[@placeholder="姓名"]')  # 姓名
    _page_iframe = (By.XPATH, '//iframe[contains(@src,"/dsfa/teas/zygl/szk/views")]')  # 主页iframe
    _edit_page_iframe = (By.XPATH, '//iframe[contains(@src,"editteacher.html")]')  # 编辑页面iframe
    _select_page_iframe = (By.XPATH, '//iframe[contains(@src,"/dsfa/teas/zygl/szk/views/listxnxz.html")]')
    _add_button = (By.XPATH, '//a[@title="新增"]')  # 新增按钮
    _view_link = (By.XPATH, '//div[contains(@class,"-none")]//a[@title="查看"]')  # 查看链接
    _view_close_btn = (By.XPATH, '//a[@class="ds_button  ds_button_auxiliary"]')  # 查看框关闭按钮
    _edit_link = (By.XPATH, '//div[contains(@class,"-none")]//a[@title="编辑"]')  # 编辑链接
    _delete_link = (By.XPATH, '//div[contains(@class,"-none")]//a[contains(@title,"删除")]')  # 删除链接
    _delete_confirm_btn = (By.XPATH, '//button[contains(@class,"el-button--primary ")]')

    # 进入校内老师列表
    _search_teacher_input = (By.XPATH, '//input[@placeholder="输入名称"]')  # 搜索老师
    _confirm_button = (By.XPATH, '//a[text()="确定"]')  # 确定按钮
    _cancel_button = (By.XPATH, '//a[text()="取消"]')  # 取消
    _after_delete_tip = (By.XPATH, '//div[@role="alert"]/i[contains(@class,"el-icon")]/following::p')  # 删除后的提示

    # 师资库查询
    _teacher_name_a = (By.XPATH, '(//div[@ctrl_type="Customer"]/a)[1]')  # 第一个师资
    _teacher_info_title = (By.XPATH, '//label[@class="ds_label font_2"]')  # 师资信息title
    _teacher_info_name = (By.XPATH, '//div[@class="layui-input-block ui-widget"]/div')  # 师资信息页面老师姓名

    more_button = (By.XPATH, '//a[@title="更多"]')
    download_buttron = (By.XPATH, '//a[@title="模板下载"]')  # 导入模板下载
    import_buttron = (By.XPATH, '//a[@title="预导入"]')  # 导入按钮
    import_export_save = (By.XPATH, '//*[@btn-index]//*[contains(text(), "确定")]')  # 导入/导出确定按钮
    export_btn = (By.CSS_SELECTOR, '.ds-button--icon-text[title=导出]')  # 导出按钮

    @allure.step("搜索老师")
    def find_teacher(self, name: str = ''):
        self.locator_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button(times=0.25)
        self.wait_presence_list_data(explicit_timeout=20, poll_frequency=0.25)
        return self

    @allure.step("获取师资列表")
    def get_teacher_list_info(self):
        teacher_title = ('姓名', '师资来源', '单位', '部门', '职务', '职称', '是否启用')
        locator = '//*[contains(@class,"is-scrolling")]//tr//td[{}]'
        locators = list(map(lambda x: (By.XPATH, locator.format(x)), range(3, 10)))
        return self.publish_get_info(*locators, title=teacher_title)

    @allure.step("新增老师信息")
    def edit_teacher_info(self, data: dict):
        keys = data.keys()
        if "师资来源" in keys:
            self.locator_select_list_value(ctrl_id="source", value=data["师资来源"])
            if data["师资来源"] == "校内":
                self.locator_button("选择校内教师")
                time.sleep(3)
                self.locator_search_input(placeholder='输入关键字进行过滤', value=data['姓名'])
                self.locator_tree_node_click(data["姓名"])
                self.locator_dialog_btn('确定')
            else:
                self.locator_text_input(ctrl_id="name", value=data["姓名"])

        if "性别" in keys:
            self.locator_select_radio(ctrl_id="sex", value=data["性别"])
        if "身份证号" in keys:
            self.locator_text_input(ctrl_id="idcard", value=data["身份证号"])
        if "出生日期 " in keys:
            self.locator_date(ctrl_id="birthdate", value=data["出生日期 "])
        if "联系电话" in keys:
            self.locator_text_input(ctrl_id="phone", value=data["联系电话"])
        if "专业方向" in keys:
            self.locator_select_list_value(ctrl_id="teas_specialty_direction", value=data["专业方向"])

        if "单位" in keys:
            self.locator_text_input(ctrl_id="work_unit", value=data["单位"])
        if "部门" in keys:
            self.locator_text_input(ctrl_id="unit_text", value=data["部门"])
        if "职务" in keys:
            self.locator_text_input(ctrl_id="post", value=data["职务"])
        if "职称" in keys:
            self.locator_select_list_value(ctrl_id="duty_title", value=data["职称"])

        if "毕业院校" in keys:
            self.locator_text_input(ctrl_id="finish_school", value=data["毕业院校"])
        if "最高学历" in keys:
            self.locator_select_list_value(ctrl_id="finish_school", value=data["最高学历"])
        if "学位" in keys:
            self.locator_select_list_value(ctrl_id="degree", value=data["学位"])
        if "行政级别" in keys:
            self.locator_select_list_value(ctrl_id="administrative_level", value=data["行政级别"])

        if "办公电话" in keys:
            self.locator_text_input(ctrl_id="office_phone", value=data["毕业院校"])
        if "是否启用" in keys:
            self.locator_select_radio(ctrl_id="is_enable", value=data["是否启用"])
        if "备注" in keys:
            self.locator_text_input(ctrl_id="remark", value=data["备注"], tag_type="textarea")
        self.locator_button("保存")
        self.switch_to_handle(0)
        time.sleep(1)
        return self

    @allure.step("新增老师")
    def add_teacher(self, data):
        self.excute_js_click_ele(self._add_button)
        self.switch_to_handle()
        self.edit_teacher_info(data)
        return self

    # @allure.step("选择校内老师")
    # def search_school_teacher_select(self, teachername):
    #     self.input_send_keys(self._search_teacher_input, teachername + Keys.ENTER)
    #     teacher_link = (By.XPATH, '//span[text()="{}"]/parent::a'.format(teachername))
    #     self.excute_js_click(teacher_link)
    #     return self

    @allure.step("查看")
    def view_teacher_detail(self):
        self.excute_js_click(self._view_link)
        return self

    @allure.step("编辑")
    def edit_teacher(self, value, data: dict):
        self.locator_view_button(button_title="编辑", id_value=value)
        self.switch_to_handle()
        self.edit_teacher_info(data)
        return self

    @allure.step("删除")
    def delete_teacher(self, value):
        self.locator_view_button(button_title="删除", id_value=value)
        sure = (By.XPATH, '//span[contains(text(),"确定")]/parent::button')
        self.element_click(sure)
        return self

    @allure.step("下载格式文件")
    def get_file(self):
        self.wait_presence_ele(self.more_button)
        self.excute_js_click_ele(self.more_button)
        self.excute_js_click_ele(self.download_buttron)
        return wait_file_down_and_clean('师资导入模板.xlsx')

    @allure.step("导入师资库数据")
    def import_teacher(self, file):
        # self.locator_tag_button(button_title='预导入', file_path=file)
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn(btn_name='确定', dialog_title='预导入文件编辑', times=1)
        self.wait_success_tip()
        return self

    @allure.step("异常导入师资")
    def import_teacher_error(self, file):
        # self.locator_tag_button(button_title='预导入', file_path=file)
        self.locator_more_tip_button(button_title='预导入')
        self.locator_click_wait_input_file(btn_name='导入数据', file=file)
        self.locator_dialog_btn(btn_name='确定', dialog_title='预导入文件编辑', times=1)
        return self

    @allure.step("导入的弹窗点击确定")
    def import_save_file(self):
        self.excute_js_click(self.import_export_save)
        return self

    @allure.step('关闭师资导入浮页')
    def close_teacher_import_frame(self):
        close_btn = (By.CSS_SELECTOR, '.el-dialog__close')
        self.poll_click(close_btn)

    @allure.step('导出师资列表')
    def export_teacher(self):
        self.excute_js_click_ele(self.more_button)
        self.excute_js_click_ele(self.export_btn)
        return self

    @allure.step('导出设置可选列随机勾选未勾选项')
    def export_items_select(self):
        loc = (By.XPATH,
               '//*[@class="el-checkbox-group"]//span[contains(@class, "el-checkbox__input") and not (contains(@class, "is-checked"))]')
        self.driver.implicitly_wait(1)
        total_checkboxes = self.driver.find_elements(*loc)
        self.driver.implicitly_wait(self.Default_Implicit_Timeout)
        if total_checkboxes:  # 若找到未勾选列
            to_check_count = random.randint(1, len(total_checkboxes))
            to_check_checkboxes = random.sample(total_checkboxes, k=to_check_count)
            for checkbox in to_check_checkboxes:
                self.excute_js_click_ele(checkbox)
                sleep(0.25)  # 勾选后dom刷新等待

    @change_reset_implicit(1)
    @allure.step('判断并操作导出确认')
    def judge_whether_export_confirm(self):
        # export_confirm_btn = (
        # By.XPATH, '//*[@aria-label="导出设置"]//*[contains(@class,"ds-button")]//*[contains(text(),"导出")]')
        # time.sleep(3)
        # self.excute_js_click(export_confirm_btn)
        # # if self.judge_element_whether_existence(export_confirm_btn):
        # #     self.element_click(export_confirm_btn)
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('师资库.xlsx')

    @property
    @change_reset_implicit()
    @allure.step('获取师资库管理列表检索表单结果条数')
    def table_count_searched(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        return len(self.driver.find_elements(*tr))
