# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *


class HomeworkDetailManage(BasePage):
    """班次作业管理详情页面"""

    @allure.step('查询作业')
    def search_homework(self, name):
        self.locator_search_input(placeholder='作业名称', value=name, times=2, enter=True)
        return self

    def _edit_info(self, data: dict):
        if '作业名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['作业名称'])
        if '作业开始时间' in data:
            self.locator_date_range(ctrl_id='homework_date', start_date=data['作业开始时间'], end_date=data['作业结束时间'])
        if '批阅方式' in data:
            self.locator_select_radio(ctrl_id='review_mode', value=data['批阅方式'])
        if '作业分类' in data:
            self.locator_select_list_value(ctrl_id='type', value=data['作业分类'])

    @allure.step('保存作业')
    def edit_save(self, data: dict):
        self._edit_info(data)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        time.sleep(1)
        return self

    @allure.step('保存并发布作业')
    def edit_push(self, data: dict):
        self._edit_info(data)
        self.locator_button(button_title='保存并发布')
        self.wait_success_tip()
        return self

    @allure.step('点击布置作业')
    def click_add(self):
        self.locator_button(button_title='布置作业')
        return self

    @allure.step('点击编辑作业')
    def click_edit(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        return self

    @allure.step('查看作业')
    def view_homework(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        time.sleep(2)
        info = self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id=name] [title]'))
        self.locator_close_dialog_window(dialog_title='查看')
        return info

    @allure.step('修改作业时间')
    def edit_homework_time(self, name):
        self.locator_view_button(button_title='修改时间', id_value=name)
        time.sleep(2)
        self.locator_button(button_title='保存')
        return self.wait_success_tip()

    @allure.step('发布作业')
    def push_homework(self, name):
        self.locator_view_button(button_title='发布', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('取消发布作业')
    def cancel_push_homework(self, name):
        self.locator_view_button(button_title='取消发布', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('删除作业')
    def del_homework(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('查看作业提交情况')
    def view_homework_submit_detail(self, name):
        self.locator_view_button(button_title='提交情况', id_value=name)
        return self

    # @allure.step('代交作业')
    # def submit_homework(self, name, file):
    #     self.locator_view_button(button_title='代交', id_value=name)
    #     self.upload_input_file_no_click(loc_input=(By.CSS_SELECTOR, 'input[type="file"]'), file=file)
    #     self.wait_success_tip()
    #     return self

    @allure.step('退回作业')
    def rollback_homework(self, name):
        self.locator_view_button(button_title='退回', id_value=name)
        return self.wait_success_tip()

    @allure.step('批阅分配作业')
    def assign_homework(self, name, data: dict):
        self.locator_view_button(button_title='批阅分配', id_value=name)
        self.locator_search_magnifier(ctrl_id='reviewer', )
        self.locator_search_input(placeholder='输入关键字进行过滤', value=data['批阅人'], enter=True)
        self.locator_tree_node_click(node_value=data['批阅人'])
        self.locator_dialog_btn(btn_name='确定')
        self.locator_date_range(ctrl_id='review_time', start_date=data['批阅开始时间'], end_date=data['批阅结束时间'], confirm=True)
        self.locator_button(button_title='保存')
        info = self.wait_success_tip()
        self.locator_close_dialog_window()
        return info

    @allure.step('点击查看成绩')
    def view_score(self, name):
        self.locator_view_button(button_title='查看成绩', id_value=name)
        return self

    def operate_homework_level(self, name, action):
        with allure.step(f'作业{action}'):
            self.locator_view_button(button_title=action, id_value=name, dialog_title='查看成绩')
            self.wait_success_tip()
        return self

    @allure.step('下载作业')
    def download_file(self, name, file_name):
        self.locator_view_button(button_title='下载作业', id_value=name, dialog_title='查看成绩')
        return wait_file_down_and_clean(file_name)

    def operate_grade_status(self, action: str):
        with allure.step(action):
            self.locator_button(button_title=action)
            self.wait_success_tip()
            time.sleep(2)  # 等待数据刷新
        return self

    @allure.step('修改成绩')
    def edit_homework_score(self, name, score):
        self.locator_view_button(button_title='修改成绩', id_value=name, dialog_title='查看成绩')
        self.locator_text_input(ctrl_id='result_score', value=score)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self


