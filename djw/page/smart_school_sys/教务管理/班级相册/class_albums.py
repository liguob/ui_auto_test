"""
============================
Author:杨德义
============================
"""
import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By


class ClassAlbums(BasePage):
    """班级相册班次页"""

    # 查看相册按钮
    view_album_btn = (By.CSS_SELECTOR, '.is-scrolling-none .small[title=查看相册]')

    @allure.step('切至当前班次')
    def switch_current_class(self):
        self.locator_switch_tag(tag_name='当前班次', times=1)
        return self

    @allure.step('搜索班次')
    def search_class(self, class_name):
        self.locator_tag_search_input(placeholder='请输入班次', value=class_name)
        self.locator_tag_search_button(times=1)
        return self

    @allure.step('进入指定当前班次查看相册管理页')
    def go_current_class_album_manage_page(self, class_name):
        self.switch_current_class()
        self.search_class(class_name)
        self.excute_js_click_ele(self.view_album_btn)
        time.sleep(0.5)
        self.switch_to_handle(index=-1)
        from djw.page.smart_school_sys.教务管理.班级相册.albums_manage import AlbumsManage
        return AlbumsManage(driver=self.driver)
