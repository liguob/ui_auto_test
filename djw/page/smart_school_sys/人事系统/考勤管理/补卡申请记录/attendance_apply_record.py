from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AttendanceApplyRecord(PersonnelSysPage):

    @allure.step('查询补卡申请')
    def search_apply(self, name):
        self.locator_search_input(placeholder='标题', value=name, enter=True)
        return self

    @allure.step('查看补卡详情')
    def view_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        name_loc = (By.CSS_SELECTOR, '[ctrl-id="title"] [title]')
        name = self.get_ele_text_visitable(name_loc)
        self.close_and_return_page()
        return name

    @allure.step('撤回补卡申请')
    def rollback_apply(self, name):
        self.locator_view_button(button_title='撤回', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('导出补卡申请记录文件')
    def download_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='确定')
        return wait_file_down_and_clean(file_name='数据导出.xlsx')

    @allure.step('删除补卡申请')
    def del_apply(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('编辑保存补卡申请')
    def edit_apply(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self