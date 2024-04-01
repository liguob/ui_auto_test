import typing
from common.tools_packages import *
from common.decorators import change_reset_implicit


class HeadmasterMaintain(BasePage):
    """班主任网上报修"""

    @allure.step('切至报修申请/学员报修')
    def switch_tab(self, tab_name: typing.Literal['报修申请', '学员报修'] = '学员报修'):
        self.locator_switch_tag(tag_name=tab_name)
        return self

    @allure.step('检索学员报修')
    def search(self, keyword):
        """
        :param keyword: 标题(姓名某年某月某日维修申请单)
        """
        self.locator_tag_search_input(placeholder='标题', value=keyword)
        self.locator_tag_search_button()
        return self
    
    @allure.step('班主任填写学员报修表单')
    def __edit_info(self, data: dict):
        if '报修地点' in data:
            self.locator_text_input(ctrl_id='place', value=data['报修地点'])
        if '故障说明' in data:
            self.locator_text_input(ctrl_id='description', value=data['故障说明'])
        if '维修类别' in data:
            self.locator_select_list_value(ctrl_id='category', value=data['维修类别'])

    @allure.step('班主任编辑发送学员报修')
    def send_apply(self, data: dict,  checker_name: str):
        edit_btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=编辑]')
        self.excute_js_click_ele(edit_btn)
        self.wait_open_new_browser_and_switch()
        self.__edit_info(data)
        self.locator_button(button_title='发送')
        self.process_send(checker=checker_name)
        self.switch_to_handle(index=-1)
        return self

    @change_reset_implicit()
    @allure.step('获取学员报修列表检索匹配表单条数')
    def table_count_searched(self):
        tr = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] tr')
        return len(self.driver.find_elements(*tr))

    @property
    @change_reset_implicit()
    @allure.step('获取学员报修列表流转情况')
    def statuses(self) -> typing.List[str]:
        status_loc = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] [class*=status_text__value]')
        return self.trim_texts(self.driver.find_elements(*status_loc))
