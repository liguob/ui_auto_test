"""
============================
Author:杨德义
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AbroadApply(PersonnelSysPage):
    """因私出国-出境记录页面类"""

    @allure.step('编辑出境申请信息')
    def edit_info(self, data: dict):
        if '出国(境)开始时间' in data:
            self.locator_date_range(ctrl_id='abroad_time', start_date=data['出国(境)开始时间'], end_date=data['出国(境)结束时间'])
        if '出国(境)地点' in data:
            self.locator_date(ctrl_id='abroad_site', value=data['出国(境)地点'])
        if '经费来源' in data:
            self.locator_select_radio(ctrl_id='fund_source', value=data['经费来源'])
        if '手机号码' in data:
            self.locator_text_input(ctrl_id='phone', value=data['手机号码'])
        if '出国(境)事由' in data:
            self.locator_text_input(ctrl_id='reason', value=data['出国(境)事由'], tag_type='textarea')
        if '约定返还时间' in data:
            self.locator_date(ctrl_id='return_time', value=data['约定返还时间'])
        if '证件类型' in data:
            self.locator_select_list_value(ctrl_id='certificate_type', value=data['证件类型'])
        time.sleep(1)
        return self

    @allure.step('查询出境记录')
    def search_apply(self, key_type):
        self.locator_search_input(placeholder='请输入经费来源', value=key_type, times=2, enter=True)
        return self

    @allure.step('点击新增出境申请')
    def click_add(self):
        self.locator_button(button_title='新增')
        return self

    @allure.step('点击编辑出境申请')
    def click_edit(self, site):
        self.locator_view_button(button_title='编辑', id_value=site)
        time.sleep(2)  # 等待数据加载
        return self

    @allure.step('保存出境申请')
    def save_apply(self):
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('出境信息校验')
    def add_apply_check(self):
        self.locator_button(button_title='新增')
        self.locator_button(button_title='保存')
        return self.get_all_required_prompt()

    @allure.step('发送出境申请')
    def send_apply(self, name):
        self.locator_button(button_title='发送')
        # 判断是否有选择办理人弹窗信息
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            self.locator_search_input(placeholder='输入名称', value=name, times=3)
            self.locator_tree_node_click(node_value=name)
            self.locator_dialog_btn('确定')  # 点击确认发送
        self.locator_dialog_btn(btn_name='确定', dialog_title='流程已发送到以下人员：')  # 点击确认已发送的弹窗
        return self

    @allure.step('导出因私出国纪律文件')
    def download_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='因私出国.xlsx')

    @allure.step('查看出境申请详情')
    def view_detail(self, site):
        self.locator_view_button(button_title='详情', id_value=site)
        return self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id="abroad_site"] [title]'))
