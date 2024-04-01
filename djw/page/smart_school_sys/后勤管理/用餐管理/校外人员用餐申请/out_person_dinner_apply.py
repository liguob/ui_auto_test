from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.用餐管理.对外班次用餐申请.out_class_dinner_apply import OutClassDinnerApply


class OutPersonDinnerApply(OutClassDinnerApply):

    @allure.step('检索校外人员用餐申请列表')
    def search(self, reason: str = ''):
        """
        :param reason: 用餐事由
        """
        return super().search(reason)
