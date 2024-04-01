# -*- coding: UTF-8 -*-
"""
Created on 2021年04月28日 

@author: liudongjie
"""

from common.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import random

class TeachingEvaluationPage(BasePage):

    top_floor_iframe = (By.XPATH, '//iframe')
    # 培训记录的iframe
    training_records_tbody_loctor = (By.XPATH, '//div[contains(@class,"-none")]//tbody')
    # 培训记录列表位置
    teaching_evaluation_iframe = (By.XPATH, '//iframe[@name="kcpj"]')
    # 教学评价-课程评估iframe位置
    choice_whether_qualified_loctor = (By.XPATH, '//div[@caption="ypfj"]//i')
    # 选择是否合格
    opinion_proposal_send_loctotr = (By.XPATH, '//textarea[@placeholder="请输入"]')
    # 意见和建议搜索框
    curriculum_evaluate_button_loctor = (By.XPATH, '//a[text()="保存"]')
    # 课程评价页面保存按钮位置

    def go_teaching_evaluation_iframe(self):
        """
        进入教学评价iframe
        """
        self.driver.switch_to.default_content()
        self.switch_to_frame(loc=self.top_floor_iframe)
        self.switch_to_frame(loc=self.teaching_evaluation_iframe)

    def choice_whether_qualified(self, valeu):
        """
        进入课程评价页面
        """
        if valeu == '合格':
            self.find_elms(loc=self.choice_whether_qualified_loctor)[0].click()
        elif valeu == '不合格':
            self.find_elms(loc=self.choice_whether_qualified_loctor)[1].click()

    def choice_score(self, degree, num):
        """
        num为1是选择问题导向 num为2是选择教学组织 num为3是选择总结点评
        degree 是评分程度
        """
        defree_dic = {'优秀': str(random.randint(86, 100)), '良好': str(random.randint(76, 85)),
                      '一般': str(random.randint(60, 75)), '差': str(random.randint(0, 60))}
        project_loctor = (By.XPATH, '//input[@placeholder="{}"]'.format(degree))
        self.find_elms(loc=project_loctor)[num-1].click()
        value = '//dd[text()="{}"]'.format(degree+defree_dic[degree])
        self.driver.find_elements_by_xpath('{}'.format(value))[num-1].click()
        sleep(1)

    def opinion_proposal_send(self, value):
        """
        输入意见与建议
        """
        self.find_elem(loc=self.opinion_proposal_send_loctotr).send_keys(value)

    def curriculum_evaluate_button_click(self):
        """
        点击课程保存按钮
        """
        self.find_elem(loc=self.curriculum_evaluate_button_loctor).click()

    def teaching_evaluation_records_tbody(self, value):
        """
        操作培训记录列表
        """
        tbody = self.find_elem(loc=self.training_records_tbody_loctor)
        tr_list = tbody.find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            span_list = td_list[1].find_elements_by_tag_name('span')
            if span_list[1].text == value:
                a = td_list[7].find_element_by_tag_name('a')
                self.driver.execute_script("arguments[0].click();", a)
                break
        sleep(1)

    def go_course_evaluate_page(self):
        """
        进入课程评价页面
        """
        self.switch_to_handle(-1)
