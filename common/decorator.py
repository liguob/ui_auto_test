# coding: utf-8
"""
============================
# Time      ：2022/3/9 16:06
# Author    ：李国彬
============================
"""
import time

from selenium.webdriver.remote.webelement import WebElement
from functools import wraps


def highlight(func):
    """页面元素高亮装饰器"""

    @wraps(func)
    def wrapper(self, *args, **kw):
        borders = {}  # 所有元素的初始显示border属性
        elements = func(self, *args, **kw)  # 获取查找元素方法返回的所有元素
        if isinstance(elements, list):
            for element in elements:
                if isinstance(element, WebElement):
                    borders.update({element: element.value_of_css_property('border')})
                    self.driver.execute_script('arguments[0].style.border="2px solid red";', element)
                else:
                    raise TypeError(f'{element}不是WebElement类型')
        elif isinstance(elements, WebElement):
            borders.update({elements: elements.value_of_css_property('border')})
            self.driver.execute_script('arguments[0].style.border="2px solid red";', elements)
        else:
            raise TypeError(f'{elements}不是WebElement类型')
        time.sleep(0.1)
        if borders:
            for element, border in borders.items():
                self.driver.execute_script(f'arguments[0].style.border="{border}";', element)
        return elements

    return wrapper
