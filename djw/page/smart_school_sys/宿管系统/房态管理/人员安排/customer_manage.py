import typing
from common.tools_packages import *
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.宿管系统.房态管理.房间分配.room_dispatch import RoomDispatch


class CustomerManage(RoomDispatch):
    """人员安排"""

    @allure.step('进入团体人员安排页')
    def go_customer_manage_page(self, team_name: str):
        """
        param team_name: 团体名称
        """
        self.locator_view_button(button_title='人员安排', id_value=team_name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('获取所有房间列表展示信息')
    def get_rooms_info(self):
        info_loc = (By.CSS_SELECTOR, '.room')
        return [str(i.get_attribute('textContent')).strip() for i in self.find_elements_displayed(info_loc)]

    @allure.step('为团体人员安排(入住)房间')
    def arrange_team_customers(self, customer_name: str, room_name: str):
        # 拖拽人员放入房间
        name_loc = (By.XPATH, f'//*[@class="group-person-name" and text()="{customer_name}"]')
        room_loc = (By.CSS_SELECTOR, f'[title="{room_name}"]')
        self.drag_and_drop(name_loc, room_loc)
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('获取团体列表所有姓名')
    def get_customers(self) -> list:
        name_loc = (By.CSS_SELECTOR, '.group-person-box .group-person-name')
        return self.get_ele_texts_visitable(name_loc)

    @allure.step('重置已选房间')
    def reset_checked_rooms(self, to_check_rooms: typing.Iterable[dict]):
        """
        :param to_check_rooms: 重置已选房间时勾选的房间
        """
        self.select_room(to_check_rooms)
        self.locator_dialog_btn(btn_name='重置已选房间')
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('重置全部')
    def reset_all_rooms(self):
        self.locator_dialog_btn(btn_name='重置全部')
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('导出')
    def export_arrange_info(self, file_name: str) -> str:
        self.locator_dialog_btn(btn_name='导出')
        return wait_file_down_and_clean(file_name=file_name)
