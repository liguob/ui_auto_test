from typing import Literal
from common.tools_packages import *
from common.base_page import BasePage
from common.decorators import change_reset_implicit


class BookingSummary(BasePage):
    """房间预定流量统计"""
    mapping = {'单间': 1, '标间': 2, '套房': 3, '多人间': 4}

    @allure.step('楼宇楼层下拉选择')
    def select_building_floor(self, building_name: str, floor_name: str):
        """
        :param building_name: 楼宇名
        :param floor_name: 楼层名
        """
        self.chose_list_option(building_name)
        time.sleep(1)
        self.chose_list_option(floor_name)
        time.sleep(1)
        return self

    @change_reset_implicit()
    @allure.step('获取指定日期指定房型房间流量百分比')
    def booking_percentage(self, booking_date: str, room_type: Literal['单间', '标间', '套房', '多人间']) -> str:
        """
        :param booking_date: (预定)日期 %Y-%m-%d
        :param room_type: 房型
        :return 百分比值(去除百分号)
        """
        num = self.mapping[room_type]
        percentage_loc = (By.XPATH, f'(//*[contains(@class, "is-scrolling")]//span[contains(text(), "{booking_date}")]//ancestor::td//following-sibling::td)[{num}]')
        return self.trim_text(percentage_loc).split('%')[0]
