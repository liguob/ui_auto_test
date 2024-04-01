# coding: utf-8
"""
============================
# Time      ：2022/6/17 16:34
# Author    ：李国彬
============================
"""
from selenium.webdriver.remote.webdriver import WebDriver

from common.base_page import BasePage


class ManageDriver:
    """管理测试用例运行的driver"""

    def __init__(self):
        self.drivers = list()

    def append_driver(self, driver_type=''):
        """创建driver并返回"""
        driver = BasePage(driver_type=driver_type.lower()).driver
        self.drivers.append(driver)
        return driver

    def close_drivers(self):
        """关闭所有driver"""
        for driver in self.drivers:
            if isinstance(driver, WebDriver):
                try:
                    driver.quit()
                except Exception:
                    pass
        self.drivers.clear()


class CookieManage:
    allCookie = {}

    @staticmethod
    def user_cookie(username):
        return CookieManage.allCookie.get(username, None)

    @staticmethod
    def update_cookie(username, cookie):
        CookieManage.allCookie.update({username: cookie})


CookieManager = CookieManage()
