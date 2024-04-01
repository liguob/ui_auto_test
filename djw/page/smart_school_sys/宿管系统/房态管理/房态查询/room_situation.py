import typing
from common.tools_packages import *
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.宿管系统.房态管理.散客管理.individual_manage import IndividualManage


class RoomSituation(IndividualManage):
    """房态查询"""

    @property
    @change_reset_implicit(implicit_timeout=2)
    @allure.step('获取指定楼宇的指定楼层所有房间号')
    def rooms_num(self) -> typing.List[str]:
        room_num = (By.XPATH, '//*[@class="ds-dormitory-container"]//*[contains(@class, "floor-container")]//*[@data-id]//*[contains(@class, "num")]')
        nums_list = self.trim_texts(self.driver.find_elements(*room_num))
        return nums_list
