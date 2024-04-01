"""
============================
Author:杨德义
Description: 自定义显示等待
============================
"""
import time
from typing import Union
from selenium.webdriver.remote.webdriver import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from common.decorators import change_reset_implicit


def text_to_be_present_in_element_increment(loc: tuple, text: str, basepage):
    """
    增量判断元素是否加载完对应文本
    :param loc: 元素的定位器
    :param text: 增量文本
    :param basepage: BasePage及其子类实例
    """

    def _predicate(driver) -> Union[str, bool]:
        try:
            ele_text = basepage.trim_text(loc)
            if text in ele_text:
                return ele_text
        except StaleElementReferenceException:
            return False

    return _predicate


def list_searched_to_count(loc: tuple, count: int, basepage):
    """
    显示等待检索后显示指定条数据
    :param loc: 列表单行数据定位器
    :param count: 列表检索匹配行数
    :param basepage: BasePage及其子类实例
    """

    @change_reset_implicit()
    def _predicate(driver) -> bool:
        list_datas = driver.find_elements(*loc)
        return True if len(list_datas) == count else False

    setattr(_predicate, 'basepage', basepage)

    return _predicate


def list_poll_search(search_btn: WebElement,
                     tr_loc: tuple,
                     count: int,
                     basepage,
                     times: Union[int, float] = 2
                     ):
    """
    轮询点击列表搜索按钮至显示指定条数据
    :param search_btn: 列表搜索按钮元素
    :param tr_loc: 列表单行数据定位器
    :param count: 列表检索匹配行数
    :param basepage:  BasePage及其子类实例
    :param times: 检索等待时间
    """

    @change_reset_implicit()
    def _predicate(driver) -> bool:
        basepage.excute_js_click_ele(search_btn)
        time.sleep(times)
        list_datas = driver.find_elements(*tr_loc)
        return True if len(list_datas) == count else False

    setattr(_predicate, 'basepage', basepage)

    return _predicate
