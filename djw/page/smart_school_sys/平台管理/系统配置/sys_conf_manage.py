# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2022/1/20 9:31
# Author     ：李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.主页.home_page import HomePage


class SysConfManege(HomePage):

    def _save_conf(self):
        self.locator_button(button_title='保存')
        self.switch_to_frame_back()
        info = self.wait_success_tip(times=10)
        return info

    def switch_conf(self, conf_type):
        self.switch_to_frame_back()
        config_type = (By.XPATH, f'//*[@role="menuitem" and contains(text(), "{conf_type}")]')
        with allure.step(f'进入{conf_type}'):
            self.excute_js_click(config_type)
            time.sleep(2)
            self.switch_to_frame(self.find_elem((By.CSS_SELECTOR, 'iframe[src]')))
        return self

    @allure.step('修改安全配置')
    def edit_safe_conf(self, data: dict):
        self.switch_conf('安全配置')
        keys = data.keys()
        if '首次登陆是否强制要求修改密码' in keys:
            self.locator_select_radio(ctrl_id='pwd_update_first_login', value=data['首次登陆是否强制要求修改密码'])
        return self._save_conf()

    @allure.step('修改网报配置')
    def edit_network_apply_conf(self, data: dict):
        self.switch_conf('网报配置')
        keys = data.keys()
        if '个人网报是否需要报名密码' in keys:
            self.locator_select_radio(ctrl_id='is_password', value=data['个人网报是否需要报名密码'])
        if '个人网报是否审核' in keys:
            self.locator_select_radio(ctrl_id='personnel_is_audit', value=data['个人网报是否审核'])
        if '是否自动同步' in keys:
            self.locator_select_radio(ctrl_id='student_auto_syn', value=data['是否自动同步'])
        return self._save_conf()

    @allure.step('修改bbs配置')
    def edit_bbs_conf(self, data: dict):
        self.switch_conf('bbs配置')
        keys = data.keys()
        if '是否开启主题审核' in keys:
            self.locator_select_radio(ctrl_id='is_topic_review', value=data['是否开启主题审核'])
        return self._save_conf()

    @allure.step('修改班级配置')
    def edit_class_conf(self, data: dict):
        self.switch_conf('班级配置')
        keys = data.keys()
        if '推送数据' in keys:
            for i in data['推送数据']:
                is_check = (By.XPATH, f'//*[@ctrl-id="push"]//*[contains(text(),"{i}")]/..')
                check_value = self.find_elem(is_check).get_attribute('class')
                if 'is-checked' in check_value:
                    pass
                else:
                    self.locator_select_radio(ctrl_id='push', value=i)
        return self._save_conf()

    @allure.step('修改宿管公用配置')
    def edit_room_sys_conf(self, data: dict):
        self.switch_conf('宿管公用配置')
        confirm_btn = (By.CSS_SELECTOR, '[x-placement] .confirm')
        if '开启分区' in data:
            self.locator_select_radio(ctrl_id='zone', value=data['开启分区'])
        if '开启预分配' in data:
            self.locator_select_radio(ctrl_id='reserve', value=data['开启预分配'])
        if '默认开始时间' in data:
            sdate_loc = (By.CSS_SELECTOR, '[ctrl-id=sdate] input')
            self.input_readonly_js(sdate_loc, data['默认开始时间'])
            time.sleep(1)
            self.poll_click(confirm_btn)
            time.sleep(1.5)
        if '默认结束时间' in data:
            edate_loc = (By.CSS_SELECTOR, '[ctrl-id=edate] input')
            self.input_readonly_js(edate_loc, data['默认结束时间'])
            time.sleep(1)
            self.poll_click(confirm_btn)
            time.sleep(1.5)
        if '人员详情地址' in data:
            self.locator_text_input(ctrl_id='person_detail_url', value=data['人员详情地址'])
        if '入住条件' in data:
            self.locator_select_radio(ctrl_id='unique', value=data['入住条件'])
        return self._save_conf()

    @allure.step('修改个人网报配置')
    def edit_person_report_conf(self, data: dict):
        self.switch_conf('网报配置')
        if '个人网报二维码是否固定' in data:
            self.locator_select_radio(ctrl_id='is_fixed', value=data['个人网报二维码是否固定'])
        if '个人网报是否需要报名码' in data:
            self.locator_select_radio(ctrl_id='is_password', value=data['个人网报是否需要报名码'])
        if '个人网报填写个人信息' in data:
            self.locator_select_radio(ctrl_id='info_type', value=data['个人网报填写个人信息'])
        if '服务器根路径' in data:
            self.locator_text_input(ctrl_id='rootpath', value=data['服务器根路径'])
        return self._save_conf()

    @allure.step('修改初始密码配置')
    def edit_init_pw(self, data: dict):
        self.switch_conf('初始密码配置')
        if '教职工密码规则' in data:
            self.locator_select_radio(ctrl_id='init_pwd_rule_teacher', value=data['教职工密码规则'])
            self.locator_text_input(ctrl_id='customized_origin_pwd_teacher', value=data['教职工自定义密码'])
        if '学员密码规则' in data:
            self.locator_select_radio(ctrl_id='init_pwd_rule_student', value=data['学员密码规则'])
            self.locator_text_input(ctrl_id='customized_origin_pwd_student', value=data['学员自定义密码'])
        if '网报管理员密码规则' in data:
            self.locator_select_radio(ctrl_id='init_pwd_rule_enroll', value=data['网报管理员密码规则'])
            self.locator_text_input(ctrl_id='customized_origin_pwd_enroll', value=data['网报管理员自定义密码'])
        if '对外培训单位用户密码规则' in data:
            self.locator_select_radio(ctrl_id='init_pwd_rule_external', value=data['对外培训单位用户密码规则'])
            self.locator_text_input(ctrl_id='customized_origin_pwd_external', value=data['对外培训单位用户自定义密码'])
        time.sleep(1)
        return self._save_conf()
