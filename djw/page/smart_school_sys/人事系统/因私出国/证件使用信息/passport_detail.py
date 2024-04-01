from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class PassportDetail(PersonnelSysPage):
    """因私出国-证件使用信息页面类"""

    @allure.step('查询证件使用信息')
    def search_passport(self, site):
        self.locator_tag_search_input(placeholder='请输入出国地点', value=site)
        self.locator_tag_search_button()
        return self

    def operate_passport(self, site, action):
        with allure.step(action):
            self.locator_view_button(button_title=action, id_value=site)
            self.wait_success_tip()
        return self

    @allure.step('导出证件使用信息文件')
    def download_file(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('因私出国境记录.xlsx')

