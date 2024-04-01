import typing
from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.用餐管理.对外班次用餐审核.out_class_dinner_check import OutClassDinnerCheck


class OutPersonDinnerCheck(OutClassDinnerCheck):

    @allure.step('校外人员用餐审核未处理/已处理检索')
    def search_check_list(self, reason: str = '', tab_num: typing.Literal[1, 2] = 1):
        """
        :param reason: 用餐事由
        :param tab_num: 第几个标签页
        """
        return super().search_check_list(reason, tab_num)
