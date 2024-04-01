import allure

from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem


class TeamCheckInSummary(RoomSystem):
    """团体入住情况"""

    @allure.step('团体名称检索团体入住情况查询')
    def search_class(self, team_name: str):
        """
        :param team_name: 团体名称
        """
        self.locator_search_input(placeholder='团体名称', value=team_name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入(指定团体)人员详情(统计)页')
    def go_customer_detail(self, team_name):
        """
        :param team_name: 团体名称
        """
        self.locator_view_button(button_title='人员详情', id_value=team_name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('导出团体入住情况列表文件')
    def download_team_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('数据导出.xlsx', times=20)

    @allure.step('导出指定团体的入住详情文件')
    def down_load_team_user_file(self, name):
        self.locator_view_select(id_value=name)
        time.sleep(1)
        self.locator_dialog_btn(btn_name='人员导出')
        time.sleep(0.5)
        allure.attach(body=self.driver.get_screenshot_as_png(), name="测试截图", attachment_type=allure.attachment_type.PNG)
        return wait_file_down_and_clean(f'{name}.xlsx')

    @allure.step('导出入住详情中的学员文件')
    def download_detail_user_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('数据导出.xlsx')
