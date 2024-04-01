import typing
from djw.page.smart_school_sys.宿管系统.房态管理.散客管理.individual_manage import IndividualManage
from common.tools_packages import *


class RoomDispatch(IndividualManage):
    """房间分配"""

    @allure.step('团体名称检索团体列表')
    def search_team(self, team_name: str = ''):
        """
        :param team_name: 团体名称
        """
        self.locator_search_input(placeholder='团体名称', value=team_name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入团体房间分配页')
    def go_dispatch_page(self, team_name: str):
        """
        param team_name: 团体名称
        """
        self.locator_view_button(button_title='分配房间', id_value=team_name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('为团体分配房间')
    def dispatch_rooms(self, rooms: list):
        """
        :param rooms: 选择房间的名称列表
        """
        time.sleep(2)
        for room in rooms:
            self.select_room(room)
        self.locator_dialog_btn(btn_name='确定分配')
        return self

    @allure.step('重置已配房源')
    def reset_dispatched(self):
        self.locator_dialog_btn(btn_name='重置已配房源')
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('勾选房间')
    def select_room(self, room_name):
        select_room = (By.XPATH, f'//*[@title="{room_name}"]/..//div[@class="check-box"]')
        self.excute_js_click(select_room)
        return self

    @allure.step('重置已选房源')
    def reset_checked(self, room_name: str):
        self.select_room(room_name)
        self.locator_dialog_btn(btn_name='重置已选房源')
        self.locator_dialog_btn(btn_name='确定')
        return self
