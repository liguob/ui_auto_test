from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class MyAttendance(PersonnelSysPage):

    @allure.step('发起补卡申请')
    def attendance_apply(self, days_date: str, attend_status: str, data: dict):
        btn_loc = (
            By.XPATH, f'//*[@class="maindiv-day-number" and text()="{days_date}"]/../..//*[text()="{attend_status}"]')
        click_btn = (By.XPATH, '//*[@x-placement]//*[text()="补卡申请"]')
        self.move_to_ele(btn_loc)
        self.move_and_move_to_click(btn_loc, click_btn)
        self.wait_open_new_browser_and_switch()
        if '标题' in data:
            self.locator_text_input(ctrl_id='title', value=data['标题'])
        if '补卡理由' in data:
            self.locator_text_input(ctrl_id='reason', value=data['补卡理由'], tag_type='textarea')
        time.sleep(2)
        self.locator_button(button_title='提交')
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self
