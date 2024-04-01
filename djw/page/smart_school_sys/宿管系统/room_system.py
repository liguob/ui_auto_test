# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class RoomSystem(HomePage):
    """宿管系统主页"""

    @allure.step('进入楼宇维护')
    def go_building_manage(self):
        self.locator_left_menu_click(button_title='楼宇维护')
        from djw.page.smart_school_sys.宿管系统.楼宇维护.building_manage_page import BuildingManage
        return BuildingManage(self.driver)

    @allure.step('进入房间维护')
    def go_room_manage(self):
        self.locator_left_menu_click(button_title='房间维护')
        from djw.page.smart_school_sys.宿管系统.房间维护.room_manage_page import RoomManage
        return RoomManage(self.driver)

    @allure.step('进入房间停用统计')
    def go_fix_room_manage(self):
        self.locator_left_menu_click(button_title='房间停用统计')
        from djw.page.smart_school_sys.宿管系统.停用房间统计.fix_room_manage import FixRoomManage
        return FixRoomManage(self.driver)

    @allure.step('进入团体管理')
    def go_team_manage(self):
        self.locator_left_menu_click(button_title='团体管理')
        from djw.page.smart_school_sys.宿管系统.团体管理.team_manage import TeamManage
        return TeamManage(self.driver)

    @allure.step('进入房间确认')
    def go_room_confirm(self):
        self.locator_left_menu_click(button_title='房间确认')
        from djw.page.smart_school_sys.宿管系统.房间确认.room_confirm_manage import RoomConfirmManage
        return RoomConfirmManage(self.driver)

    @allure.step('进入房态管理-散客管理')
    def go_individual_manage(self):
        self.locator_left_menu_click(menu_title='房态管理', button_title='散客管理')
        from djw.page.smart_school_sys.宿管系统.房态管理.散客管理.individual_manage import IndividualManage
        return IndividualManage(self.driver)

    @allure.step('进入房态管理-房间分配')
    def go_room_dispatch(self):
        self.locator_left_menu_click(menu_title='房态管理', button_title='房间分配')
        from djw.page.smart_school_sys.宿管系统.房态管理.房间分配.room_dispatch import RoomDispatch
        return RoomDispatch(self.driver)

    @allure.step('进入房态管理-人员安排')
    def go_customer_manage(self):
        self.locator_left_menu_click(menu_title='房态管理', button_title='人员安排')
        from djw.page.smart_school_sys.宿管系统.房态管理.人员安排.customer_manage import CustomerManage
        return CustomerManage(self.driver)

    @allure.step('进入房态管理-房态查询')
    def go_room_situation(self):
        self.locator_left_menu_click(menu_title='房态管理', button_title='房态查询')
        from djw.page.smart_school_sys.宿管系统.房态管理.房态查询.room_situation import RoomSituation
        return RoomSituation(self.driver)

    @allure.step('进入散客入住记录')
    def go_individual_record(self):
        self.locator_left_menu_click(button_title='散客入住记录')
        from djw.page.smart_school_sys.宿管系统.散客入住记录.individual_record import IndividualRecord
        return IndividualRecord(self.driver)

    @allure.step('进入调房/续房记录')
    def go_change_renewal_record(self):
        self.locator_left_menu_click(button_title='调房/续房记录')
        from djw.page.smart_school_sys.宿管系统.调房续房记录.change_renewal_record import ChangeRenewalRecord
        return ChangeRenewalRecord(self.driver)

    @allure.step('进入退房记录')
    def go_check_out_record(self):
        self.locator_left_menu_click(button_title='退房记录')
        from djw.page.smart_school_sys.宿管系统.退房记录.check_out_record import CheckOutRecord
        return CheckOutRecord(self.driver)

    @allure.step('进入过期房管理')
    def go_expired_rooms_manage(self):
        self.locator_left_menu_click(button_title='过期房管理')
        from djw.page.smart_school_sys.宿管系统.过期房管理.expired_rooms_manage import ExpiredRoomsManage
        return ExpiredRoomsManage(self.driver)

    @allure.step('进入房间预定流量统计')
    def go_booking_summary(self):
        self.locator_left_menu_click(button_title='房间预定流量统计')
        from djw.page.smart_school_sys.宿管系统.房间预定流量统计.booking_summary import BookingSummary
        return BookingSummary(self.driver)

    @allure.step('进入团体入住情况')
    def go_team_check_in_summary(self):
        self.locator_left_menu_click(button_title='团体入住情况')
        from djw.page.smart_school_sys.宿管系统.团体入住情况.team_check_in_summary import TeamCheckInSummary
        return TeamCheckInSummary(self.driver)

    @allure.step('进入房间入住统计')
    def go_room_check_in_summary(self):
        self.locator_left_menu_click(button_title='房间入住统计')
        from djw.page.smart_school_sys.宿管系统.房间入住统计.room_check_in_summary import RoomCheckInSummary
        return RoomCheckInSummary(self.driver)
