from selenium.webdriver.common.by import By
from common.base_page import BasePage


class WaitDone(BasePage):
    wait_deal = (By.XPATH, '//div[@class="ds-home-tab-panel ds-home-tab-panel-one"]/div/div/div/div[@ac="true"]')  # 待办菜单
    btn_more = (By.XPATH, '//div[@ctrl-id="hometabpanel37"]//div/i[@class="iconfont icon-gengduo"]')  # 待办—>更多按钮
    td_title = (By.XPATH, '//tr//td[3]/div/div[1]')  # 第一行的标题

    def get_td_title_value(self):
        """"点击待办中的更多"""
        self.excute_js_click(self.wait_deal)
        self.element_click(self.btn_more)
        value = self.find_elem(self.td_title).text
        return value
