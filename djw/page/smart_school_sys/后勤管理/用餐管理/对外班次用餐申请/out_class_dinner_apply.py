import typing
from common.tools_packages import *


class OutClassDinnerApply(BasePage):

    @allure.step('填写对外班/校外人员用餐申请表单')
    def __edit_form(self, data: dict):
        if '班次名称' in data:
            self.locator_search_magnifier(ctrl_id='name')
            self.locator_search_input(placeholder='请输入班次名称', value=data['班次名称'], dialog_title='请选择班次')
            self.locator_tag_search_button()
            checkbox = (By.CSS_SELECTOR, '.el-dialog [class*=is-scrolling] input[type=checkbox]')
            confirm = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')
            self.excute_js_click_ele(checkbox)
            time.sleep(0.5)
            self.poll_click(confirm)
        if '培训人数' in data:
            self.locator_text_input(ctrl_id='num', value=str(data['培训人数']))
        if '用餐需求' in data:
            self.locator_text_input(ctrl_id='demand', value=data['用餐需求'])
        if '用餐事由' in data:
            reason_loc = (By.CSS_SELECTOR, '[ctrl-id=reason] textarea')
            self.clear_then_input(reason_loc, data['用餐事由'])
        if '用餐信息' in data:
            add_btn = (By.CSS_SELECTOR, '[ctrl-id=detail] .ds-subtable-tools .small[title=新增]')
            self.excute_js_click_ele(add_btn)
            time.sleep(0.5)
            script = '''document.querySelector("[module-name='teas.logistics.dined.personnel.edit']").__vue__.$vm.$viewData['teas_logistics_dined_personnel_detail'][0].__ob__.value['teas_logistics_dined_personnel_detail.dined_time'] = arguments[0]'''
            self.driver.execute_script(script, data['用餐信息']['用餐时间'] + ' ' + '00:00:00')
            self.chose_list_option(option_text=data['用餐信息']['用餐类别'])
            amount = (By.CSS_SELECTOR, '[ctrl-id=detail] [form-name*=amount] input')
            self.clear_then_input(amount, data['用餐信息']['用餐金额'])
            confirm = (By.CSS_SELECTOR, '[ctrl-id=detail] .small[title=确定]')
            self.excute_js_click_ele(confirm)
        if unit := data.get('参训单位'):
            if unit.strip():
                self.locator_text_input(ctrl_id='unit', value=unit)
        if contact := data.get('联系人'):
            if contact.strip():
                self.locator_text_input(ctrl_id='contact', value=contact)
        if contact_phone := data.get('联系电话'):
            if contact_phone.strip():
                self.locator_text_input(ctrl_id='contact_phone', value=contact_phone)
        if note := data.get('备注'):
            if note.strip():
                note_loc = (By.CSS_SELECTOR, '[ctrl-id=remark] textarea')
                self.driver.find_element(*note_loc).send_keys(note)

    @allure.step('新增提交对外班次/校外人员用餐申请')
    def send_apply(self, data: dict, checker: str):
        """
        :param data: 申请信息
        :param checker: 审核人
        """
        add_btn = (By.XPATH, '//*[@class="head-right-item"]//*[contains(text(), "新增")]')
        self.excute_js_click_ele(add_btn)
        self.wait_open_new_browser_and_switch()
        self.__edit_form(data)
        self.locator_button(button_title='提交')
        self.process_send(checker=checker)
        self.switch_to_handle(index=-1)
        return self

    @allure.step('新增保存对外班次/校外人员用餐申请')
    def save_apply(self, data: dict):
        """
        :param data: 申请信息
        """
        add_btn = (By.XPATH, '//*[@class="head-right-item"]//*[contains(text(), "新增")]')
        self.excute_js_click_ele(add_btn)
        self.wait_open_new_browser_and_switch()
        self.__edit_form(data)
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self

    @property
    @allure.step('获取对外班次/校外人员用餐申请列表审核状态')
    def check_statuses(self) -> typing.List[str]:
        status = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=status_text__value]')
        return self.trim_texts(self.driver.find_elements(*status))

    @allure.step('检索对外班次/校外人员用餐申请、用餐统计')
    def search(self, keyword: str = ''):
        """
        :param keyword: 检索关键词
        """
        search_input = (By.CSS_SELECTOR, '.head-right-item input')
        search_btn = (By.CSS_SELECTOR, '.head-right-item .search-button')
        self.clear_then_input(search_input, keyword)
        self.poll_click(search_btn)
        time.sleep(0.5)
        self.wait_presence_list_data()
        return self

    @allure.step('对外班次/校外人员用餐申请列表导出')
    def export(self, file_name: typing.Literal['对外班次用餐申请表.xlsx', '校外人员用餐表.xlsx']):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name="导出", dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name=file_name)

    def judge_return_edit(self) -> bool:
        """判断对外班次/校外人原用餐审核退回后是否可编辑"""
        return_edit_btn = (By.XPATH,
                           '//*[contains(@class, "is-scrolling")]//*[contains(@class, "status_text__value") and contains(text(), "退回")]//ancestor::td//following-sibling::td//*[@title="编辑"]')
        return self.is_element_exist(return_edit_btn)

    @allure.step('点击对外班次/校外人员用餐申请编辑按钮')
    def click_edit(self):
        btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=编辑]')
        self.excute_js_click_ele(btn)
        self.wait_open_new_browser_and_switch()
        time.sleep(1)
        return self

    @allure.step('更改对外班用餐需求')
    def update_demand(self, demand: str):
        self.click_edit()
        demand_loc = (By.CSS_SELECTOR, '[ctrl-id=demand] input')
        self.clear_then_input(demand_loc, demand)
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('更改校外人员用餐事由')
    def update_reason(self, reason: str):
        self.click_edit()
        reason_loc = (By.CSS_SELECTOR, '[ctrl-id=reason] textarea')
        self.clear_then_input(reason_loc, reason)
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('删除对外班次/校外人员用餐申请')
    def delete(self):
        btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=删除]')
        self.excute_js_click_ele(btn)
        confirm = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(), "确定")]')
        self.excute_js_click_ele(confirm)
        return self

    @property
    @allure.step('获取对外班用餐需求')
    def demand(self):
        demand_loc = (By.CSS_SELECTOR, '[ctrl-id=demand] input')
        return self.driver.execute_script('return arguments[0].value;', self.driver.find_element(*demand_loc))
