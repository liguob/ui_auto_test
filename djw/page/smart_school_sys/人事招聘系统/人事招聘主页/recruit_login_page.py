# encoding=utf-8
"""
============================
Author:何凯
Time:2021/9/6 9:49
============================
"""
from common.tools_packages import *


class RecruitLoginPage(BasePage):
    """人事招聘登录注册页面"""
    recruit_url = 'dsf5/enroll.html#/enroll/index'

    @allure.step("登录招聘系统")
    def login(self, username, password):
        self.locator_search_input(placeholder='请输入账号', value=username)
        self.locator_search_input(placeholder='请输入密码', value=password)
        self.locator_search_input(placeholder='请输入验证码', value='good')
        self.locator_dialog_btn(btn_name='登录')
        return self

    @allure.step("注册账号并登录")
    def register_user(self, data):
        self.locator_dialog_btn(btn_name='注册')
        with allure.step('填写注册信息'):
            self.locator_search_input(placeholder='请输入姓名', value=data['姓名'])
            self.locator_search_input(placeholder='请输入身份证号', value=data['身份证号'])
            self.locator_search_input(placeholder='请输入密码', value=data['设置密码'])
            self.locator_search_input(placeholder='请再次输入密码', value=data['确认密码'])
            self.locator_dialog_btn(btn_name='下一步')
        with allure.step('填写手机验证'):
            self.locator_search_input(placeholder='请输入手机号', value=data['手机号码'])
            self.locator_dialog_btn(btn_name='请点击进行验证')
            time.sleep(3)
            self.locator_dialog_btn(btn_name=' 获取短信验证码')
            self.wait_success_tip()
            self.locator_search_input(placeholder='请输入短信验证码', value='good')
            time.sleep(2)
            self.locator_dialog_btn(btn_name='下一步', dialog_title='dialog')
            self.locator_dialog_btn(btn_name='下一步')
        self.locator_dialog_btn(btn_name='立即登录')

    @allure.step('发送申请岗位')
    def apply_position(self, name, data: dict):
        apply_btn = (By.XPATH, f'//*[text()="{name}"]/../..//*[contains(text(), "申请岗位")]')
        self.element_click(apply_btn)
        if self.find_elements_no_exception((By.CSS_SELECTOR, '[aria-label="选择简历"]')):
            self.locator_dialog_btn(btn_name='选择')
        self.wait_open_new_browser_and_switch()
        if '照片' in data:
            self.locator_text_input(ctrl_id='photo', value=data['照片'], is_file=True)
            time.sleep(2)  # 等待图片上传加载
            self.locator_dialog_btn(btn_name='确 定')
        if '人才类别' in data:
            self.locator_select_list_value(ctrl_id='talent_category', value=data['人才类别'])
        if '一级学科代码及名称' in data:
            self.locator_text_input(ctrl_id='course_name_code', value=data['一级学科代码及名称'])
        if '籍贯' in data:
            self.excute_js_click((By.CSS_SELECTOR, '[ctrl-id="native"] [placeholder="请选择"]'))
            time.sleep(1)
            for i in data['籍贯']:
                self.element_click((By.XPATH, f'//*[contains(text(), "{i}")]'))
        self.locator_button(button_title='发送')
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            self.locator_search_input(placeholder='输入名称', value=data['请选择办理人'], times=3)
            self.locator_tree_node_click(node_value=data['请选择办理人'])
            self.locator_dialog_btn('确定')
            time.sleep(2)
        # self.locator_dialog_btn('确定')
        self.switch_to_window(-1)
        return self

    @allure.step('查看招聘公告')
    def view_notice(self, name):
        view_btn = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//*[contains(text(), "查看")]')
        self.excute_js_click(view_btn)
        self.wait_open_new_browser_and_switch()
        return self.get_ele_text_visitable((By.CSS_SELECTOR, '.notice-title'))

    @allure.step('查看我的申请')
    def view_my_apply(self, name):
        view_btn = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//*[contains(text(), "查看")]')
        self.excute_js_click(view_btn)
        self.wait_open_new_browser_and_switch()
        return self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id="phone"] [title]'))

    @allure.step('修改密码')
    def edit_password(self, old_pw, new_pw):
        self.locator_dialog_btn(btn_name='修改密码')
        self.locator_search_input(placeholder='请输入旧密码', value=old_pw)
        self.locator_search_input(placeholder='请输入新密码', value=new_pw)
        self.locator_search_input(placeholder='请再次输入新密码', value=new_pw)
        time.sleep(1)
        self.locator_dialog_btn(btn_name='下一步')
        info = self.get_ele_text_visitable((By.CSS_SELECTOR, '.success-tip'))
        self.locator_close_dialog_window()
        return info

    def _edit_resume(self, data):
        """简历信息编写"""
        if '简历命名' in data:
            self.locator_text_input(ctrl_id='template_name', value=data['简历命名'])
        if '民族' in data:
            self.locator_select_list_value(ctrl_id='nation', value=data['民族'])
        if '政治面貌' in data:
            self.locator_select_list_value(ctrl_id='part', value=data['政治面貌'])
        if '籍贯' in data:
            self.excute_js_click((By.CSS_SELECTOR, '[ctrl-id="native"] [placeholder="请选择"]'))
            time.sleep(1)
            for i in data['籍贯']:
                self.element_click((By.XPATH, f'//*[contains(text(), "{i}")]'))
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()

    @allure.step('新增简历')
    def add_resume(self, data):
        self.locator_dialog_btn(btn_name='新增简历')
        self.wait_open_new_browser_and_switch()
        self._edit_resume(data)
        return self

    @allure.step('编辑简历')
    def edit_resume(self, name, data):
        edit_btn = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//*[contains(text(), "编辑")]')
        self.element_click(edit_btn)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='nation')
        self._edit_resume(data)
        return self

    @allure.step('删除简历')
    def del_resume(self, name):
        del_btn = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//*[contains(text(), "删除")]')
        self.element_click(del_btn)
        self.locator_dialog_btn(btn_name='确定')
        return self.wait_success_tip()
