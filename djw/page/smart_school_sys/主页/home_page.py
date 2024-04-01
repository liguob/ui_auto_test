# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/2   13::30
============================
"""
import time

import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class HomePage(BasePage):
    """登录后的首页页面"""
    user_info = (By.CSS_SELECTOR, '[ctrl_type="dsf.teasuserinfosetting"]')  # 登录后的个人信息

    @allure.step("进入教务管理")
    def go_edu_manage_page(self):
        self.locator_top_menu_click(menu_title='教务管理')
        from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage
        return EduManagePage(self.driver)

    @allure.step("进入班主任管理")
    def go_master_manage_page(self):
        self.locator_top_menu_click(menu_title='班主任管理')
        from djw.page.smart_school_sys.班主任管理.master_manage_page import MasterManagePage
        return MasterManagePage(self.driver)

    @allure.step("进入教学资源")
    def go_edu_source_page(self):
        self.locator_top_menu_click(menu_title='教学资源')
        from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage
        return EduSourcePage(self.driver)

    @allure.step('进入网报管理')
    def go_network_report_manage_page(self):
        self.locator_top_menu_click(menu_title='网报管理')
        from djw.page.smart_school_sys.网报管理.管理端.network_report_manage_main_page import NetworkReportManagePage
        return NetworkReportManagePage(self.driver)

    @allure.step("进入人事系统")
    def go_personnel_sys(self):
        self.locator_top_menu_click(menu_title='人事系统')
        from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage
        return PersonnelSysPage(self.driver)

    @allure.step("进入后勤管理")
    def go_logistics_manage_page(self):
        self.locator_top_menu_click(menu_title='后勤管理')
        from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage
        return LogisticsManagePage(driver=self.driver)

    @allure.step('进入平台管理')
    def go_platform_manage_page(self):
        self.locator_top_menu_click(menu_title='平台管理')
        from djw.page.smart_school_sys.平台管理.platform_manage_page import PlatformManagePage
        return PlatformManagePage(self.driver)

    @allure.step('进入对外培训')
    def go_out_training_page(self):
        self.locator_top_menu_click(menu_title='对外培训')
        from djw.page.smart_school_sys.对外培训.out_traing_page import OutTrainingPage
        return OutTrainingPage(self.driver)

    @allure.step('进入论坛管理')
    def go_bbs_manage_page(self):
        self.locator_top_menu_click(menu_title='论坛管理')
        from djw.page.smart_school_sys.论坛管理.bbs_manage_page import BBSManagePage
        return BBSManagePage(self.driver)

    @allure.step("切换为人事组")
    def _switch_to_personnel_group(self):
        btn = (By.XPATH, '//div[@class="username"]/i')
        option = (By.XPATH, '//li[contains(text(),"切换为人事组")]')
        self.move_to_ele(btn)
        self.excute_js_click(option)

    @allure.step('进入宿管系统')
    def go_room_system_manage(self):
        self.locator_top_menu_click(menu_title='宿管系统')
        from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem
        return RoomSystem(self.driver)

    def get_login_name(self):
        """获取登录后显示的名称"""
        text = self.get_ele_text_visitable((By.CSS_SELECTOR, '.user_font'))
        return text.split(',')[-1].strip()
