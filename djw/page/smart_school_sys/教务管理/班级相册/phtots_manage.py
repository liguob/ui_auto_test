import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit
from common.file_path import wait_file_down_and_clean


class PhotosManage(BasePage):
    """相册相片管理页"""

    # 相片复选按钮
    photo_radio = (By.CSS_SELECTOR, '.input-radio')

    @allure.step('上传照片')
    def upload_photo(self, photo_path):
        upload_input_btn = (By.CSS_SELECTOR, '.details_head_right input')  # 点击上传按钮
        upload_input = self.wait_presence_ele(upload_input_btn)
        upload_input.send_keys(photo_path)
        time.sleep(1)

    @property
    @change_reset_implicit()
    @allure.step('获取相册内相片数')
    def photos_count(self):
        photo = (By.CSS_SELECTOR, '[module-name="teas.classes.album.album_details"] img[src]')
        photos = self.driver.find_elements(*photo)
        return len(photos)

    @allure.step('下载相片')
    def download_photo(self, photo_name):
        download_btn = (By.CSS_SELECTOR, '.details_head_right .batch_download')  # 下载按钮
        self.excute_js_click_ele(download_btn)
        self.click_random_selected_ele(self.photo_radio)
        self.excute_js_click_ele(download_btn)
        return wait_file_down_and_clean(file_name=photo_name)

    @allure.step('批量删除照片')
    def delete_batch_photo(self):
        delete_batch_btn = (By.CSS_SELECTOR, '.details_head_right .batch_delete')  # 批量删除按钮
        self.excute_js_click_ele(delete_batch_btn)
        delete_count = self.check_multiple(self.photo_radio, start_count=1)
        self.excute_js_click_ele(delete_batch_btn)
        confirm_delete_btn = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(), "确定")]')  # 照片删除确认按钮
        self.poll_click(confirm_delete_btn)
        time.sleep(1)
        return delete_count
