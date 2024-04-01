"""
============================
Author:杨德义
============================
"""
import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.random_tool import randomTool
from collections import namedtuple
from common.decorators import change_reset_implicit


class AlbumsManage(BasePage):
    """班级相册操作页"""

    # 创建相册按钮
    create_album_btn = (By.XPATH, '//*[contains(text(), "创建相册")]//preceding-sibling::*[contains(@class, "item_add")]')
    # 创建相册-相册名称input输入框
    album_name_input = (By.CSS_SELECTOR, '[ctrl-id=album_name] input')
    # 创建相册-相册描述输入框
    album_description = (By.CSS_SELECTOR, '.el-textarea textarea')
    # 创建相册-保存按钮
    save_album_btn = (By.CSS_SELECTOR, '.ds-button[title=保存]')

    # 相册检索input框
    search_album_input = (By.CSS_SELECTOR, '.album_list_head input[placeholder*=相册名称]')
    # 相册检索按钮
    search_album_btn = (By.CSS_SELECTOR, '.album_list_head [type=button]')

    # 相册编辑按钮
    edit_album_btn = (By.XPATH, '//*[@class="album_edit"]//*[contains(text(), "编辑")]')


    @allure.step('创建一个相册')
    def create_a_album(self, album_name=randomTool.random_str()):
        self.excute_js_click_ele(self.create_album_btn)
        self.clear_then_input(self.album_name_input, album_name)
        self.excute_js_click_ele(self.save_album_btn)
        time.sleep(2)
        return self

    @property
    @allure.step('新创建的相册名称')
    def created_album_name(self):
        create_album_name_loc = (By.CSS_SELECTOR, '.name_tit')
        return self.trim_text(create_album_name_loc)

    @property
    @allure.step('新创建的相册初始相片数文本')
    def created_album_default_photos_count(self):
        """预期: 0 张"""
        create_album_default_photos_loc = (By.CSS_SELECTOR, '.name_num')
        return self.trim_text(create_album_default_photos_loc)

    @change_reset_implicit()
    @allure.step('创建一个相册断言')
    def assert_create_a_album(self):
        created_album_name = self.created_album_name
        created_album_default_photos_count = self.created_album_default_photos_count
        album_display = (By.XPATH, '//*[@class="item_name_number"]//preceding-sibling::*[@class="item_box  item_add"]')
        album_display_count = len(self.driver.find_elements(*album_display))
        Data = namedtuple('Data', ['album_display_count', 'album_name', 'default_photos_count'])
        return Data(album_display_count, created_album_name, created_album_default_photos_count)

    @allure.step('搜索相册')
    def search_album(self, album_name):
        self.clear_then_input(self.search_album_input, album_name)
        self.excute_js_click_ele(self.search_album_btn)
        time.sleep(2)
        return self

    @allure.step('编辑相册')
    def edit_album(self, album_name):
        self.excute_js_click_ele(self.edit_album_btn)
        self.clear_then_input(self.album_name_input, album_name)
        self.excute_js_click_ele(self.save_album_btn)
        time.sleep(2)
        return self

    @change_reset_implicit()
    @allure.step('编辑相册断言')
    def assert_edit_delete_album(self):
        album_display = (By.XPATH, '//*[@class="item_name_number"]//preceding-sibling::*[@class="item_box  item_add"]')
        exist_album = self.driver.find_elements(*album_display)
        return exist_album

    @allure.step('删除相册')
    def delete_album(self):
        delete_album_btn = (By.XPATH, '//*[@class="album_edit"]//*[contains(text(), "删除")]')  # 相册删除按钮
        confirm_delete_album_btn = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(), "确定")]')  # 相册删除确认按钮
        self.excute_js_click_ele(delete_album_btn)
        self.excute_js_click_ele(confirm_delete_album_btn)
        return self

    @allure.step('点击进入指定相册内')
    def into_specific_album(self, album_name):
        specific_album = (By.XPATH, f'//*[@class="name_tit" and contains(text(), "{album_name}")]//ancestor::*[@class="item_name_number"]//preceding-sibling::*[@class="item_box  item_add"]')
        self.excute_js_click_ele(specific_album)
        time.sleep(1)
        from djw.page.smart_school_sys.教务管理.班级相册.phtots_manage import PhotosManage
        return PhotosManage(driver=self.driver)
