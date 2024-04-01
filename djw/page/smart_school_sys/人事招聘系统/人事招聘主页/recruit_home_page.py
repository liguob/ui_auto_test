# encoding=utf-8
import time
import typing
import allure
from time import sleep
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from pathlib import Path
from common.random_tool import randomTool

_data_path = Path(__file__).resolve(strict=True).parents[0] / '_data'


class RecruitHomePage(BasePage):
    sure = (By.XPATH, '//*[text()="确定"]/parent::a')  # dialog确定按钮

    @allure.step("申请岗位")
    def apply_position(self, position_name):
        apply_btn = (By.XPATH,
                     f'//*[@class="topcontent-jobtitle" and text()="{position_name}"]/ancestor::*[@class="info-item-topcontent"]//*[contains(text(), "申请岗位")]/parent::button')
        self.move_to_ele(apply_btn)
        self.element_click(apply_btn)
        self.switch_to_window(-1)
        time.sleep(3.5)
        return self

    @allure.step("填写岗位申请表")
    def edit_apply_form(self, checker, **kwargs):
        """
        填写岗位申请表
        @param checker: 简历审核人姓名
        @param kwargs: 如果传关键字参数，则使用关键字参数的填写申请表
        """
        data = {"人才类别": "学科带头人才", "一级学科代码及名称": randomTool.random_range_str(3, 5) + "学科",
                "民族": "汉族", "政治面貌": '中国共产党党员', "籍贯": "北京市-直辖区-东城区", "学历": randomTool.random_qualification()}

        if kwargs:
            data.update(*kwargs.values())
        keys = data.keys()

        if "人才类别" in keys:
            self.chose_list_option(data["人才类别"])
        if "一级学科代码及名称" in keys:
            self.locator_text_input("course_name_code", data["一级学科代码及名称"])
        if "姓名" in keys:
            self.locator_text_input("name", data["姓名"])
        if "性别" in keys:
            self.chose_list_option(data["性别"])
            # self.locator_select_list_value("gender", data["性别"])
        if "身份证号" in keys:
            self.locator_text_input("idcard", data["身份证号"])
        if "年龄" in keys:
            self.locator_text_input("age", data["年龄"])
        if "出生日期" in keys:
            self.locator_date("birthday", data["出生日期"])
        if "民族" in keys:
            self.chose_list_option(data["民族"])
        if "政治面貌" in keys:
            self.chose_list_option(data["政治面貌"])
        if "籍贯" in keys:
            sleep(1.5)
            province = (By.XPATH, '//div[@ctrl-id="native"]//input[@placeholder="请选择"]')
            self.poll_click(self.explicit_wait_ele_presence(province, explicit_timeout=20))
            sleep(0.5)
            native_list = data["籍贯"].split('-')
            province_value, city_value, area_value = native_list[0], native_list[1], native_list[2]
            option = (By.XPATH, '//*[@class="el-cascader-node__label" and contains(text(), "{}")]')
            self.excute_js_click_ele((option[0], option[1].format(province_value)))
            self.poll_click(self.explicit_wait_ele_presence((option[0], option[1].format(city_value))))
            self.poll_click(self.explicit_wait_ele_presence((option[0], option[1].format(area_value))))
            sleep(0.5)
        if "婚姻状况" in keys:
            self.locator_text_input("marriage", data["婚姻状况"])
        if "手机号码" in keys:
            self.locator_text_input("phone", data["手机号码"])
        if "学历" in keys:
            self.chose_list_option(data["学历"])
        self.upload_photo(str(_data_path / 'photo_test1.jpg'))  # 头像必传
        send_btn = (By.XPATH, '(//*[@class="ds-page-foot"]//*[contains(@class, "ds-button") and @title])[1]')
        self.poll_click(self.explicit_wait_ele_presence(send_btn, explicit_timeout=20))
        self.process_send(checker=checker)
        return data

    @allure.step('岗位申请上传头像')
    def upload_photo(self, file):
        photo_input = (By.CSS_SELECTOR, '[ctrl-id=photo] input')
        self.driver.find_element(*photo_input).send_keys(file)
        sleep(1)
        confirm_upload = (By.CSS_SELECTOR, '[aria-label=图片裁剪] .dialog-footer .el-button--primary')
        self.poll_click(confirm_upload)
        sleep(0.5)

    @allure.step("获取招聘岗位信息列表")
    def get_position_info(self):
        position_name = (By.XPATH, '//span[@class="topcontent-jobtitle"]')
        position_detail = (By.XPATH, '//div[@class="info-item-detailinfo"]')
        title = ("position_name", "position_detail")
        return self.publish_get_info(position_name, position_detail, head=title)

    @allure.step("申请岗位并发送简历")
    def apply_position_send_resume(self, value, checker, **kwargs):
        """
        @param value: 申请岗位名称
        @param checker: 简历审核人姓名
        @param kwargs: 填写申请表格
        @return:
        """
        self.apply_position(value)
        applicant_info = self.edit_apply_form(checker, **kwargs)
        self.switch_to_handle(index=0)
        return applicant_info

    @allure.step("获取我的申请列表信息")
    def get_my_apply_info(self) -> typing.List[dict]:
        my_apply_btn = (By.XPATH, '//div[@class="nav-item-name" and text()="我的申请"]')
        self.poll_click(my_apply_btn)
        items = (By.XPATH, '//div[contains(@class,"scrolling")]//tr/td[{}]')
        locators = list(map(lambda x: (items[0], items[1].format(x)), range(3, 11)))
        title = ("审核状态", "公告名称", "岗位名称", "申请时间", "结束时间", "笔试成绩", "面试结果", "录用结果")
        all_info = self.publish_get_info(*locators, head=title)
        # 字符串双端去空格
        for info in all_info:
            for k in info:
                info[k] = info[k].strip()
        return all_info
