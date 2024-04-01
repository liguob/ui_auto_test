from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem


class RoomCheckInSummary(RoomSystem):
    """房间入住统计"""

    @allure.step('查询团体')
    def search_team(self, name):
        self.locator_tag_search_input(placeholder='团体名称', value=name, enter=True)
        return self

    @allure.step('点击查看团体详情')
    def view_team_detail(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        name_loc = (By.CSS_SELECTOR, '[ctrl-id="occupy_text"] [title]')  # 团体名称
        info = self.get_ele_text_visitable(name_loc)
        self.locator_close_dialog_window()
        return info

    def click_num_go_detail(self, team_name, header_name):
        with allure.step(f'点击{header_name}进入详情'):
            self.locator_view_value_click(id_value=team_name, header=header_name)
            self.wait_open_new_browser_and_switch()
        return self
