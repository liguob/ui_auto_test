# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/16    14:37
============================
"""
from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base_page import BasePage


class GradingPage(BasePage):
    _iframe1 = (By.XPATH, "//iframe[@src='/dsfa/teas/jwgl/bjxygl/grade/views/classList.html']")
    _iframe2 = (
        By.XPATH,
        "//iframe[@name='layui-layer-iframe3']")
    _grading_class_list_name = (By.XPATH, "//label[@class='ds_font_3']")
    _grading_class_list_search = (By.XPATH, "//input[@placeholder='班次名称' and @handler='search']")  # 成绩登记班次列表搜索框
    _grading_class_list_classname = (
        By.XPATH,
        "//table[@class='datagrid_table drop-ignore']/tbody/tr/td[3]//div[@class='readOnly']")  # 成绩登记班次列表项：班次名称
    _grading_class_list_grading = (
        By.XPATH, "//table[@class='datagrid_table drop-ignore']/tbody/tr/td[7]//div[@class='nowrap']")  # 成绩登记班次列表项：成绩登记
    _grading_student_list_name = (By.XPATH, '//*[@id="ndLjXuezBKoxhDxq"]/div[1]/div[1]/label')  # 学员成绩登记列表名称
    _grading_student_list_search = (By.XPATH, "//input[@class='layui-input' and @handler='search']")  # 学员成绩登记列表检索框
    _grading_student_list_studentname = (
        By.XPATH, "//table[@class='datagrid_table drop-ignore']/tbody/tr/td[6]//div[@class='readOnly']")  # 学员成绩登记列表项：姓名
    _grading_student_list_level = (
        By.XPATH,
        "//table[@class='datagrid_table drop-ignore']/tbody/tr/td[7]//div[@class='readOnly']")  # 学员成绩登记列表项：成绩等级
    _grading_student_list_level1 = (By.XPATH, "(//table[@class='datagrid_table drop-ignore']/tbody/tr/td[7])[1]")  # 学员成绩登记列表项第一行：等级
    _grading_student_list_level2 = (
    By.XPATH, "(//table[@class='datagrid_table drop-ignore']/tbody/tr/td[7])[2]")  # 学员成绩登记列表项第二行：等级
    _grading_student_list_score1 = (
        By.XPATH, "(//table[@class='datagrid_table drop-ignore']/tbody/tr/td[8]//div[@class='readOnly'])[1]")  # 学员成绩登记列表项第一行：成绩
    _grading_student_list_score2 = (
        By.XPATH,"(//table[@class='datagrid_table drop-ignore']/tbody/tr/td[8]//div[@class='readOnly'])[2]")  # 学员成绩登记列表项第二行：成绩
    _grading_student_list_edit_1 = (
        By.XPATH, "(//table[@class='datagrid_table drop-ignore']/tbody/tr/td[9]//a)[1]")  # 学员成绩登记列表项：第一个：修改
    _grading_student_list_edit_2 = (
        By.XPATH, "(//table[@class='datagrid_table drop-ignore']/tbody/tr/td[9]//a)[1]")  # 学员成绩登记列表项：第二个：修改
    _grading_student_edit_title = (By.XPATH, "//div[@class='layui-layer-title']")  # 修改学员成绩页面标题
    _grading_student_edit_level_select = (By.XPATH, "//input[@class='layui-input layui-unselect']")  # 修改学员成绩登记项：等级
    _grading_student_edit_level_select0 = (By.XPATH, "//dd[@class='layui-select-tips']")  # 等级选项：请选择
    _grading_student_edit_level_select1 = (
        By.XPATH, "//dl[@class='layui-anim layui-anim-upbit']/dd[@lay-value='0']")  # 等级选项：优秀
    _grading_student_edit_level_select2 = (
        By.XPATH, "//dl[@class='layui-anim layui-anim-upbit']/dd[@lay-value='1']")  # 等级选项：良好
    _grading_student_edit_level_select3 = (
        By.XPATH, "//dl[@class='layui-anim layui-anim-upbit']/dd[@lay-value='2']")  # 等级选项：合格
    _grading_student_edit_level_select4 = (
        By.XPATH, "//dl[@class='layui-anim layui-anim-upbit']/dd[@lay-value='3']")  # 等级选项不合格
    _grading_student_edit_score = (By.XPATH, "//input[@class='layui-input']")  # 修改学员成绩登记项：分数
    _grading_student_edit_save = (By.XPATH, "//a[@ds-event='system_form_save']")  # 修改学员成绩登记项：保存按钮
    _grading_student_edit_close = (By.XPATH, "//a[@ds-event='sytem_form_close']")  # 修改学员成绩登记项：关闭按钮
    _grading_student_edit_tip = (By.XPATH, "//div[@class='layui-layer-content layui-layer-padding']")  # 保存的提示

    download_import_loctor = (By.XPATH, '//a[text()="导入模板下载"]')  # 导入模板下载按钮位置
    upload_import_loctor = (By.XPATH, '//a[text()="成绩导入"]')  # 成绩导入按钮位置
    upload_save_button_loctor = (By.XPATH, '//a[text()="确定导入"]')  # 确定导入按钮
    achievement_student_tbody_loctor = (By.XPATH, '//tbody[@handler="datagrid_body_tobdy"]')  # 成绩导入学员列表
    download_student_button_loctor = (By.XPATH, '//a[@class="ds_button"]')  # 导出学员列表按钮位置
    chose_download_row_fix_button_loctor = (By.XPATH, '//a[text()="确定"]')  # 导入页面确定按钮
    achievement_student_search_send_loctor = (By.XPATH, '//input[@placeholder="姓名/学号"]')  # 学员列表搜索字段框
    achievement_student_search_button_loctor = (By.XPATH, '//button[@class="layui-btn"]')  # 学员列表点击按钮

    def get_grading_class_list_name(self):
        """获取成绩批阅班次列表名称"""
        sleep(1)
        self.switch_to_frame(self._iframe1)
        return self.find_elem(self._grading_class_list_name).text

    def grading_class_list_search(self, value):
        """成绩登记班次列表检索"""
        self.switch_to_frame(self._iframe1)
        self.input_send_keys(self._grading_class_list_search, value + Keys.ENTER)
        name = ("name",)
        value = self.publish_get_info(self._grading_class_list_classname, title=name)  # 获取成绩登记班次列表项：班次名称
        return value

    def click_grading_class_list_grading(self):
        """点击列表项：成绩登记"""
        # self.element_click(self._grading_class_list_grading)
        self.find_elem(self._grading_class_list_grading).click()
        sleep(1)
        self.switch_to_handle(-1)
        return self

    def get_grading_list_name(self):
        """获取成绩登记学员列表名称"""
        return self.find_elem(self._grading_student_list_name).text

    def grading_student_list_search(self, value):
        """成绩登记学员列表检索"""
        self.wait_presence_ele(self._grading_student_list_search)
        self.input_send_keys(self._grading_student_list_search, value + Keys.ENTER)
        name = ("name",)
        value = self.publish_get_info(self._grading_student_list_studentname, title=name)  # 获取成绩登记学员列表项：学员姓名
        return value

    def click_grading_student_list_edit1(self):
        """点击列表项：修改"""
        # self.wait_presence_ele(self._grading_student_list_edit_1)
        self.element_click(self._grading_student_list_edit_1)
        sleep(1)
        self.switch_to_handle()
        return self

    def get_grading_edit_title(self):
        """返回成绩修改页面左上角的标题"""
        return self.find_elem(self._grading_student_edit_title).text

    def click_grading_save(self):
        """点击成绩编辑界面的保存按钮"""
        self.switch_to_frame(self._iframe2)
        self.element_click(self._grading_student_edit_save)
        self.driver.switch_to.parent_frame()

    def click_grading_close(self):
        """点击成绩编辑界面的关闭按钮"""
        self.switch_to_frame(self._iframe2)
        self.element_click(self._grading_student_edit_close)
        self.driver.switch_to.parent_frame()

    def grading_edit_score_level(self, value):
        """选择成绩等级"""
        self.switch_to_frame(self._iframe2)
        self.element_click(self._grading_student_edit_level_select) # 点击成绩等级
        sleep(1)
        if value == "优秀":
            self.element_click(self._grading_student_edit_level_select1)
        if value == "良好":
            self.element_click(self._grading_student_edit_level_select2)
        if value == "合格":
            self.element_click(self._grading_student_edit_level_select3)
        if value == "不合格":
            self.element_click(self._grading_student_edit_level_select4)
        self.driver.switch_to.parent_frame()
        return self

    def clear_grading_edit_score(self):
        """清除分数"""
        self.switch_to_frame(self._iframe2)
        self.clear_input(self._grading_student_edit_score)
        self.driver.switch_to.parent_frame()
        return self

    def clear_grading_edit_level(self):
        """清除等级"""
        self.switch_to_frame(self._iframe2)
        self.element_click(self._grading_student_edit_level_select)
        sleep(1)
        # self.element_click(self._grading_student_edit_level_select0)
        self.find_elem(loc=self._grading_student_edit_level_select0).click()
        self.driver.switch_to.parent_frame()
        sleep(1)
        return self

    def input_grading_score(self, value):
        """填写分数"""
        self.switch_to_frame(self._iframe2)
        self.input_send_keys(self._grading_student_edit_score, value)
        self.driver.switch_to.parent_frame()
        return self

    def get_grading_student_list_score1(self):
        """获取第一个学员的分数"""
        return int(self.find_elem(self._grading_student_list_score1).text)

    def get_grading_student_list_level1(self):
        """获取第一个学员的等级"""
        return self.find_elem(self._grading_student_list_level1).text

    def get_grading_save_tip(self):
        """获取保存的提示"""
        self.switch_to_frame(self._iframe2)
        self.driver.switch_to.parent_frame()
        return self.get_ele_text_visitable(self._grading_student_edit_tip)

    def download_import_click(self):
        """
        点击导入模板下载按钮
        """
        self.find_elem(loc=self.download_import_loctor).click()
        sleep(3)

    def achievement_import_click_as_upload(self, file):
        """
        点击成绩导入按钮
        """
        self.upload_input_file(loc1=self.upload_import_loctor, loc2=(By.XPATH, '//input[@class="layui-upload-file"]'),
                               file=file)

    def upload_save_button_click(self):
        """
        点击确定导入按钮
        """
        self.find_elem(loc=self.upload_save_button_loctor).click()

    def get_achievement_student_tbody_text(self, line, row):
        """
        获取成绩设置-学员列表某行某列的text文本值
        """
        tbody = self.find_elem(loc=self.achievement_student_tbody_loctor)
        tr_list = tbody.find_elements_by_tag_name('tr')
        td_list = tr_list[line-1].find_elements_by_tag_name('td')
        div_list = td_list[row].find_elements_by_xpath('.//div')
        return div_list[3].text

    def download_student_button_click(self, value, opt=None):
        """
        点击导出加确定按钮
        value控制大选项，opt传入一个列表，1学号、2性别、3组别、4姓名、5分数等级、6分数
        """

        self.find_elem(loc=self.download_student_button_loctor).click()
        if value == '全选' or value == '清除':
            self.driver.switch_to.frame(0)
            self.find_elem(loc=(By.XPATH, '//a[text()="{}"]'.format(value))).click()
            sleep(1)
            self.driver.switch_to.parent_frame()
            self.find_elem(loc=self.chose_download_row_fix_button_loctor).click()
            sleep(3)
        elif value == '选择':
            self.driver.switch_to.frame(0)
            self.find_elem(loc=(By.XPATH, '//a[text()="{}"]'.format('清除'))).click()
            div = self.find_elem(loc=(By.XPATH, '//div[@class="layui-form-item cols"]'))
            span_list = div.find_elements_by_xpath('.//span')
            if opt == None:
                pass
            else:
                for n in opt:
                    span_list[n].click()
            self.driver.switch_to.parent_frame()
            self.find_elem(loc=self.chose_download_row_fix_button_loctor).click()
            sleep(3)
        elif value == '反选':
            self.driver.switch_to.frame(0)
            self.find_elem(loc=(By.XPATH, '//a[text()="{}"]'.format('清除'))).click()
            div = self.find_elem(loc=(By.XPATH, '//div[@class="layui-form-item cols"]'))
            span_list = div.find_elements_by_xpath('.//span')
            if opt == None:
                pass
            else:
                for n in opt:
                    span_list[n].click()
            self.find_elem(loc=(By.XPATH, '//a[text()="{}"]'.format(value))).click()
            self.driver.switch_to.parent_frame()
            self.find_elem(loc=self.chose_download_row_fix_button_loctor).click()
            sleep(3)

    def achievement_student_search(self, num):
        """
        在成绩设置页面输入并点击搜索按钮
        """
        self.find_elem(loc=self.achievement_student_search_send_loctor).send_keys(num)
        self.find_elem(loc=self.achievement_student_search_button_loctor).click()
        sleep(1)

