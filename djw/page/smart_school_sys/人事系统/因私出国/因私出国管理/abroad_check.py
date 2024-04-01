from common.tools_packages import *

from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AbroadManage(PersonnelSysPage):
    """因私出国-因私出国管理页面类"""

    @allure.step('查询出境申请')
    def search_apply(self, name):
        self.locator_tag_search_input(placeholder='请输入部门/姓名', times=2, enter=True, value=name)
        return self

    @allure.step('出境申请审核通过')
    def agree_apply(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.locator_button(button_title='同意并办结')
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('出境申请审核退回')
    def reject_apply(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.locator_button(button_title='退回')
        self.locator_search_input(placeholder='请输入退回原因', value=randomTool.random_str())
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
