# coding: utf-8
"""
============================
# Time      ：2022/3/9 16:06
# Author    ：李国彬
============================
"""
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class HighLight:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = None
        self.borders = {}

    def highlight(self, elements):
        self.elements = elements
        if isinstance(self.elements, list):
            for element in self.elements:
                if isinstance(element, WebElement):
                    self.borders.update({element: element.value_of_css_property('border')})
                    self.driver.execute_script('arguments[0].style.border="2px solid red";', element)
                else:
                    raise TypeError(f'{element}不是WebElement类型')
        elif isinstance(elements, WebElement):
            self.borders.update({self.elements: self.elements.value_of_css_property('border')})
            self.driver.execute_script('arguments[0].style.border="2px solid red";', self.elements)
        else:
            raise TypeError(f'{self.elements}不是WebElement类型')
        time.sleep(0.1)
        if self.borders:
            for element, border in self.borders.items():
                self.driver.execute_script(f'arguments[0].style.border="{border}";', element)
            self.elements = None
            self.borders = {}
        else:
            return
