from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.团体管理.team_manage import TeamManage


class RoomConfirmManage(TeamManage):
    """房间确认"""

    @allure.step('团体确认')
    def team_confirm(self, name):
        self.locator_view_button(button_title='确认', id_value=name)
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('进入人员管理')
    def into_user_manage(self, team_name):
        self.locator_view_button(button_title='人员管理', id_value=team_name)
        from djw.page.smart_school_sys.宿管系统.房间确认.人员管理.user_manage import UserManage
        return UserManage(driver=self.driver, team_name=team_name)
