# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/22 14:20
@Author :李国彬
============================
"""
from common.tools_packages import *


class CertificatePrintInfoPage(BasePage):
    """班次的证书打印管理信息页面"""

    @allure.step('查询学员')
    def search_stu(self, name=''):
        self.locator_tag_search_input(placeholder='姓名', value=name)
        self.locator_tag_search_button(times=3)
        return self

    @allure.step('撤销证书')
    def revoke_certificate(self):
        self.locator_dialog_btn(btn_name='撤销证书')
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('发放证书')
    def provide_certificate(self):
        self.locator_button(button_title='发放证书')
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('生成证书')
    def generate_certificate(self, values: dict):
        self.locator_button(button_title='生成证书')
        keys = values.keys()
        if '证书编号生成' in keys:
            self.locator_select_radio(ctrl_id='generation_rule', value=values['证书编号生成'])
        if '自定义编号' in keys:
            self.locator_text_input(ctrl_id='custom_number', value=values['自定义编号'])
        if '证书模板' in keys:
            self.locator_select_list_value(ctrl_id='certificate_template', value=values['证书模板'])
        if '证书发放时间' in keys:
            self.locator_date(ctrl_id='release_time', value=values['证书发放时间'])
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('预览证书')
    def view_certificate(self, name):
        img_ele = (By.CSS_SELECTOR, 'img[src]')  # 图片定位
        self.locator_view_button(button_title='预览', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self.find_elem(img_ele).get_attribute('src')

    def download_certificate(self, stu_name, class_name, file_type: str):
        with allure.step(f'下载{file_type}证书'):
            self.locator_view_select(id_value=stu_name)
            self.locator_button(button_title='下载证书')
            time.sleep(2)
            self.locator_select_radio(ctrl_id='format', value=file_type)
            self.find_elem((By.XPATH, '//*[@aria-label="下载证书"]//span[contains(text(),"下载证书")]')).click()
        if file_type == 'word格式':
            return wait_file_down_and_clean(f'{class_name}.docx', times=20)
        else:
            return wait_file_down_and_clean(f'{class_name}.pdf', times=20)
