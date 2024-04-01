from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.用餐管理.一周菜单操作.week_menu_handle import WeekMenuHandle


class WeekMenuView(WeekMenuHandle):
    """一周菜单查看"""

    @allure.step('一周菜单查看检索')
    def search(self, menu_title, count: int = 1):
        """
        :param menu_title: 菜单标题
        :param count: 检索预期条数
        """
        return super().search(menu_title, count)
