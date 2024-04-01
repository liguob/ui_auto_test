"""
============================
Author:何超
Time:2021/3/1   17:30
============================
"""
from __future__ import annotations
import datetime
import sys
import json
import time
import random
import typing
from functools import partial
from typing import Union
import allure
from common.decorators import change_reset_implicit
from common.file_path import common_dir, other_dir
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import *
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from common.decorator import highlight
from common.random_tool import randomTool
from common.re_ import _re


class BasePage:
    """基础的页面类, 封装一些页面中通用的操作方法和属性"""
    EC = EC
    Default_Explicit_Timeout = 20  # 默认显式等待时长
    Default_Implicit_Timeout = 20  # 默认隐式等待时长
    __dialog_ele = (By.CSS_SELECTOR, 'div[type=dialog]')  # 通用对话框
    __load_ele = (By.CSS_SELECTOR, 'div[class$="loading0"]')  # 通用加载条
    WEB_TIP = (By.CSS_SELECTOR, '.el-message__content')  # 通用pc端弹框提示
    XPATH_TAGS = '//*[@role="tabpanel" and not(@aria-hidden)]'  # xpath多页签定位前置
    CSS_TAGS = '[role=tabpanel]:not([aria-hidden]) '  # css多页签定位前置
    CSS_DIALOG = '[role=dialog][aria-label="{}"] '  # 是否属于dialog下的CSS元素定位前置
    XPATH_DIALOG = '//*[@role="dialog" and @aria-label="{}"]'  # 是否属于dialog下的xpath元素定位前置
    APP_XPATH_TAGS = '//*[@role="tabpanel" and not (contains(@style,"display"))]'  # app下xpath多页签定位前置

    def __init__(self,
                 driver: WebDriver = None,
                 driver_type: str = '',
                 web_driver_timeout: Union[int, float] = Default_Explicit_Timeout,
                 implicitly_timeout: Union[int, float] = Default_Implicit_Timeout,
                 poll_frequency: Union[int, float] = 0.5,
                 table_ctrl_type: str = 'dsf.datagrid'
                 ):
        """
        子类super().__init__()可重写显式/隐式时间
        webdriver_timeout:  显式等待默认时长
        implicitly_timeout: 隐式等待默认时长
        driver_type: web/app
        """
        # 判断host参数是否存在，用于调试
        if "host" in os.environ.keys():
            self.host = f'http://{os.environ["host"]}/'
        self.table_ctrl_type = table_ctrl_type
        if driver:
            self.driver = driver
            self.driver.implicitly_wait(time_to_wait=implicitly_timeout)
            self.wait = WebDriverWait(driver=driver, timeout=web_driver_timeout, poll_frequency=poll_frequency)
            self.action_chains = ActionChains(driver=driver)
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')  # 最高权限运行
            options.add_argument('--disable-gpu')  # 官方文档设置该属性规避bug
            options.add_argument('--start-maximized')  # 全屏运行，定位元素准备
            options.add_argument('--window-size=1920,1080')  # 设置浏览器分辨
            options.add_argument('--disable-dev-shm-usage')  # 解决DevToolsActivePort file doesn't exist
            # 设置下载路径，且运行下载多个文件
            prefs = {
                "download.default_directory": DOWNLOAD_PATH,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "profile.default_content_setting_values.automatic_downloads": 1,
                'profile.default_content_settings.popups': 0,
                "safebrowsing.enabled": True
            }
            options.add_experimental_option("prefs", prefs)
            # 判断是参数是否需要无界面运行
            if os.environ["ui"] == 'f':
                options.add_argument('--headless')  # 浏览器无可视化界面参数
            # 判断是否是手机模式
            if driver_type == "app":
                mobile_emulation = {"deviceName": "iPhone 6/7/8"}
                options.add_experimental_option("mobileEmulation", mobile_emulation)
            # 判断是否使用selenium-grid方式运行
            if os.environ["grid"] == "t":
                ds = {'platform': 'ANY', 'browserName': "chrome",
                      'version': '', 'javascriptEnabled': True}
                hub = 'http://192.168.0.200:4444/wd/hub'
                self.driver = webdriver.Remote(command_executor=hub, desired_capabilities=ds, options=options)
            else:
                self.driver = webdriver.Chrome(options=options)
            # if SYSTEM_NAME == 'Linux':
            #     driver_service = Service('/usr/local/python/bin/chromedriver')
            #     driver_service.command_line_args()
            #     driver_service.start()
            #     setattr(self.driver, 'driver_service', driver_service)
            self.wait = WebDriverWait(self.driver, timeout=web_driver_timeout, poll_frequency=poll_frequency)
            self.action_chains = ActionChains(driver=self.driver)
            self.driver.maximize_window()
            self.driver.implicitly_wait(implicitly_timeout)

    def wait_presence_ele(self, loc):
        """等待元素加载并返回"""
        ele = self.wait.until(EC.presence_of_element_located(loc))
        return ele

    @highlight
    def find_elem(self, loc):
        """查找并返回元素"""
        self.wait.until(self.EC.presence_of_element_located(loc))
        return self.driver.find_element(*loc)

    @highlight
    def find_elms(self, loc):
        """查找并返回全部元素"""
        elements = self.wait.until(self.EC.presence_of_all_elements_located(loc))
        # self.HighLight.highlight(elements)
        return elements

    def wait_presence_eles(self, loc):
        """等待所有元素加载并返回"""
        return self.wait.until(EC.presence_of_all_elements_located(loc))

    def find_elements_no_exception(self, loc):
        """查找可见元素，如果找到则返回元素列表，没有元素则返回空列表"""
        try:
            self.wait_visibility_ele(loc)
            return self.driver.find_elements(*loc)
        except Exception:
            return []

    def wait_visibility_ele(self, loc):
        """等待元素可见并返回"""
        return self.wait.until(EC.visibility_of_element_located(loc))

    @highlight
    def find_elements_displayed(self, loc):
        """获取所有可见的元素,过滤不可见的元素"""
        elements = self.find_elms(loc)
        if len(elements) > 0:
            return [i for i in elements if i.is_displayed()]
        else:
            return elements

    def find_elem_visibility(self, loc):
        """查找可见元素并返回元素"""
        self.wait_visibility_ele(loc)
        return self.driver.find_element(*loc)

    def wait_visibility_eles(self, loc):
        """等待所有元素可见并返回"""
        return self.wait.until(EC.visibility_of_all_elements_located(loc))

    def find_elems_visibility(self, loc):
        """查找可见元素并返回元素"""
        self.wait_visibility_eles(loc)
        return self.driver.find_elements(*loc)

    def find_visibility_texts(self, loc):
        result = self.wait_visibility_eles(loc)
        if result:
            return [i.text.strip() for i in result]
        else:
            print('元素无法定位或元素不可见')

    def get_ele_texts_visitable(self, loc):
        """
        获取多个可见元素本文信息
        :param loc:元素定位表达式
        :return: 元素文本信息
        """
        element = self.wait.until(self.EC.visibility_of_all_elements_located(loc))
        return [str(i.get_attribute('textContent')).strip() for i in element]

    @change_reset_implicit()
    def explicit_wait_ele_lost(self,
                               loc: tuple,
                               explicit_timeout: Union[int, float] = 6,
                               poll_frequency: Union[int, float] = 0.5,
                               ignored_exceptions: typing.Iterable[Exception] = None,
                               single: bool = True
                               ):

        """
        显示等待单个/一类元素消失
        :param explicit_timeout: 显式等待超时时间
        :param poll_frequency: 轮询间隔时间
        :param ignored_exceptions: 忽略异常类型
        :param loc: 等待消失的单个/一类元素定位表达式
        :param single: 默认为真等待单个元素消失，为假则等待一类元素消失
        """
        wait = self.explicit_timer(explicit_timeout, poll_frequency, ignored_exceptions)
        wait.until_not(self.EC.presence_of_element_located(loc)) if single else wait.until_not(
            self.EC.presence_of_all_elements_located(loc))
        return self

    @change_reset_implicit()
    def explicit_wait_ele_presence(self,
                                   loc: tuple,
                                   explicit_timeout: Union[int, float] = 6,
                                   poll_frequency: Union[int, float] = 0.5,
                                   ignored_exceptions: typing.Iterable[Exception] = None,
                                   single: bool = True
                                   ) -> Union[WebElement, list[WebElement]]:
        """
        显示等待单个/一类元素加载
        :param explicit_timeout: 显式等待超时时间
        :param poll_frequency: 轮询间隔时间
        :param ignored_exceptions: 忽略异常类型
        :param loc: 等待加载的单个/一类元素定位表达式
        :param single: 默认为真等待单个元素加载，为假则等待一类元素加载
        :return: 返回已加载的单个元素/一类元素列表
        """
        wait = self.explicit_timer(explicit_timeout, poll_frequency, ignored_exceptions)
        return wait.until(self.EC.presence_of_element_located(loc)) if single \
            else self.wait.until(self.EC.presence_of_all_elements_located(loc))

    def explicit_wait_eles_presence(self,
                                    loc: tuple,
                                    explicit_timeout: Union[int, float] = 6,
                                    poll_frequency: Union[int, float] = 0.5,
                                    ignored_exceptions: typing.Iterable[Exception] = None
                                    ) -> list[WebElement]:
        """显示等待一类元素加载"""
        return partial(self.explicit_wait_ele_presence, single=False)(loc, explicit_timeout, poll_frequency,
                                                                      ignored_exceptions)

    def explicit_wait_eles_lost(self,
                                loc: tuple,
                                explicit_timeout: Union[int, float] = 6,
                                poll_frequency: Union[int, float] = 0.5,
                                ignored_exceptions: typing.Iterable[Exception] = None
                                ):
        """显示等待一类元素消失"""
        return partial(self.explicit_wait_ele_lost, single=False)(loc, explicit_timeout, poll_frequency,
                                                                  ignored_exceptions)

    def switch_to_frame(self, loc='', frame_name='', frame_id=''):
        """
        iframe框架切换
        :param loc:frame元素定位表达式
        :param frame_name:frame元素的name
        :param frame_id:frame元素的index
        """
        if loc:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(loc))
        elif frame_name:
            self.driver.switch_to.frame(frame_name)
        elif frame_id:
            self.driver.switch_to.frame(frame_id)

    def switch_to_frame_back(self):
        """切回默认内容范围"""
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self, n: int):
        """
        切换至上 n 级 iframe 内
        n: 上 n 级 iframe
        """
        for i in range(n):
            self.driver.switch_to.parent_frame()

    def input_send_keys(self, loc, value):
        """
        向 input 元素发送数据
        :param loc: 元素定位表达式
        :param value: 发送数据
        """
        ele = self.find_elem(loc)
        ele.send_keys(value)

    def clear_and_input(self, loc, value):
        """清空输入值重新输入"""
        self.find_elem(loc).clear()
        self.find_elem(loc).send_keys(value)

    def clear_and_input_enter(self, loc, value):
        """清空输入重新输入并回车"""
        self.clear_and_input(loc, value)
        self.find_elem(loc).send_keys(Keys.ENTER)

    @staticmethod
    def keyboard_clear(ele: WebElement):
        """
        向input元素发送键盘事件:全选->删除
        返回input元素
        """
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)
        return ele

    def clear_input(self, loc: tuple, keyboard: bool = True):
        """
        清空 input 框已输内容
        :param loc: input元素定位表达式
        :param keyboard: 是否键盘全选删除
        """
        input_ele = self.find_elem(loc)
        if keyboard:
            return self.keyboard_clear(input_ele)
        else:
            input_ele.clear()
            return input_ele

    def clear_then_input(self, loc: tuple, value: str, times: Union[int, float] = 0, keyboard: bool = True):
        """清空 input 框已输内容 -> 重新输入内容"""
        self.clear_input(loc, keyboard).send_keys(value)
        time.sleep(times)

    def clear_input_enter(self, loc, value):
        """
        清空输入框内容、输入关键字并回车
        """
        for keyword in Keys.CONTROL + 'a', value + Keys.ENTER:
            self.input_send_keys(loc, keyword)

    def wait_ele_be_click(self, loc):
        """
        等待元素可点击并返回
        :param loc:元素定位表达式
        """
        return self.wait.until(EC.element_to_be_clickable(loc))

    def move_to_click(self, loc):
        """移动到元素进行点击"""
        actions = ActionChains(self.driver)
        btn = self.find_elem(loc)
        actions.move_to_element(btn).click().perform()

    def move_to_double_click(self, loc):
        actions = ActionChains(self.driver)
        btn = self.find_elem(loc)
        actions.move_to_element(btn).double_click().perform()

    def element_double_click(self, loc):
        """双击元素"""
        ele = self.find_elem(loc)
        ActionChains(self.driver).double_click(ele).perform()
        return self

    def excute_js_click(self, loc):
        """元素可见并且可点击使用js执行click"""
        self.driver.execute_script('arguments[0].click();', self.find_elem(loc))

    def excute_js_click_ele(self, loc: Union[WebElement, tuple]):
        """
        js点击元素
        :param loc: 元素定位表达式或元素对象
        """
        if isinstance(loc, WebElement):
            self.driver.execute_script('arguments[0].click();', loc)
        elif isinstance(loc, tuple):
            self.driver.execute_script('arguments[0].click();', self.wait_presence_ele(loc))

    def element_click(self, loc):
        """
        点击元素
        :param loc: 元素定位表达式
        """
        from selenium.common.exceptions import ElementClickInterceptedException
        try:
            ele = self.wait_ele_be_click(loc)
            ele.click()
        # 如果捕获到元素无法点击，则重新获取元素（避免元素刷新后点击的是刷新前的元素）
        except ElementClickInterceptedException:
            ele = self.wait_ele_be_click(loc)
            ele.click()

    def poll_click(self, loc: Union[WebElement, tuple]):
        """
        轮询点击
        :param loc:元素定位表达式/元素
        """
        ele = None
        if isinstance(loc, WebElement):
            ele = loc
        elif isinstance(loc, tuple):
            ele = self.wait_presence_ele(loc)
        try:
            ele.click()
        except Exception:
            self.driver.execute_script('arguments[0].click()', ele)  # js点击

    def click_to_clickable_ele(self, loc):
        """
        等待元素可点击后执行点击元素
        :param loc:元素定位表达式
        """
        self.wait_ele_be_click(loc)
        self.element_click(loc)

    def click_option(self, input_loc, *args):
        """
        点击下拉框选项
        :param input_loc:元素定位表达式
        :param args:选项的中文/位置
        """
        self.excute_js_click(input_loc)
        for option_text in args:
            if type(option_text) == int:
                loc_str = """(//*[contains(@*,"el-select-dropdown el-popper") and not(contains(@style,"display"))]
                                //li[@class="el-select-dropdown__item"])[{}]""".format(option_text)
            else:
                loc_str = """//*[contains(@*,"el-select-dropdown el-popper") and not(contains(@style,"display"))]
                            //*[text()="{}"]/parent::li""".format(option_text)
            time.sleep(0.5)
            self.excute_js_click((By.XPATH, loc_str))
        return self

    def choice_year(self, *args):
        """
        选择年度
        :param args:年度(2021/2022)
        """
        input_year = (By.XPATH, '//label[@title="年度"]/..//div[contains(@class,"el-input el-input--suffix")]/input')
        input_back = (By.XPATH, '//input[@class="el-select__input"]')
        self.click_option(input_year, *args)
        self.element_click(input_back)
        self.excute_js_click(input_back)
        time.sleep(0.5)
        return self

    def search_and_enter(self, key, **kwargs):
        """
        通用搜索
        :param key:搜索关键字
        :param box:弹窗场景搜索
        :param choice_user:选择系统用户窗口场景搜索
        :param tree:结构树场景搜索
        :param tab:多tab页场景搜索
        """
        search_str = '//*[@class="search-input el-input"]/input[not(@readonly)]'
        if 'app' in kwargs:
            search_str = '//*[@class="van-search"]//input[not(@readonly)]'
            if 'tab' in kwargs:
                search_str = search_str.replace('//*', '//div[@slot-name="{}"]//*'.format(kwargs['tab']))
        else:
            if 'box' in kwargs:
                search_str = search_str.replace('//*', '//div[@role="dialog"]//*')
                if 'choice_user' in kwargs:
                    search_str = search_str.replace('search-input el-input', 'el-input el-input--suffix')
            if 'tree' in kwargs:
                search_str = search_str.replace('search-input ', '')
                search_str = search_str.replace('//*', '//div[contains(@ctrl-id,"navtree")]//*')
            if 'tab' in kwargs:
                search_str = search_str.replace('//*', '//div[@id="{}"]//*'.format(kwargs['tab']))
        self.clear_input_enter((By.XPATH, search_str), key)
        time.sleep(1)
        return self

    def box_search_and_enter(self, key):
        """
        通用弹窗搜索
        :param key:搜索关键字
        """
        return self.search_and_enter(key, box=True)

    def choice_option(self, nums=1, **kwargs):
        """
        勾选复选框
        :param nums:勾选数量，默认勾选1个
        :param box:弹窗复选框场景
        :param tab:多tab复选框场景
        """
        loc = '//*[@class="el-table__fixed"]'
        if 'box' in kwargs:
            loc = loc.replace('//*', '//div[@role="dialog"]//*')
        if 'tab' in kwargs:
            loc = loc.replace('//*', '//div[@id="{}"]//*'.format(kwargs['tab']))
        if type(nums) == int:
            option_str = '({0}//td[1]//span/span)[{1}]'.format(loc, nums)  # 复选框
        else:
            option_str = '{}//thead//span[@class="el-checkbox__input"]'.format(loc)  # 复选框_全选
        self.element_click((By.XPATH, option_str))
        return self

    def box_choice_option(self, nums=1):
        """
        勾选弹窗复选框
        :param nums:勾选数量，默认勾选1个
        """
        return self.choice_option(nums, box=True)

    def judge_academy_switch(self):
        """
        判断多学区开关是否打开
        """
        return True if os.environ['academy'] == 'on' else False

    def choice_academy(self, academy=''):
        """
        选择学区
        :param academy:学区
        """
        if academy and os.environ['academy'] == 'on':
            self.tree_choice(academy)
        else:
            pass
        return self

    def tree_choice(self, keyword=1, **kwargs):
        """
        结构树搜索并选择
        :param keyword:搜索关键词
        :param major:专业搜索开关
        """
        if type(keyword) == int:
            result_str = '(//div[@role="tree"]/div[@role="treeitem"])'
            if 'major' in kwargs:
                result_str = result_str.replace(')', '//div[@role="treeitem"])')
            result = (By.XPATH, result_str + '[{}]'.format(keyword))
        else:
            result = (By.XPATH, '//div[@role="tree"]//span[text()="{}"]/../../..'.format(keyword))
            self.search_and_enter(keyword, tree=True)
        self.excute_js_click(result)
        time.sleep(0.5)
        return self

    def flow_tip(self):
        """流程流转提示"""
        tip_box = (By.XPATH, '//*[text()="流程已发送到以下人员："]/parent::*')  # 提示窗
        btn_sure = (By.XPATH, '//div[@class="el-dialog"]//*[text()="确定"]/..')  # 确定按钮
        self.wait_visibility_ele(tip_box)
        time.sleep(0.5)
        self.element_click(btn_sure)
        self.switch_to_handle()
        return self

    def flow_over_tip(self):
        """流程流转结束提示"""
        tip_box = (By.XPATH, '//*[text()="文件已办结"]/parent::*')  # 提示窗
        btn_sure = (By.XPATH, '//*[text()="确定"]/parent::*')  # 确定按钮
        self.wait_visibility_ele(tip_box)
        time.sleep(0.5)
        self.element_click(btn_sure)
        self.switch_to_handle()
        return self

    @allure.step('Web端流程发送')
    def process_send(self, checker: str = None):
        """
        判断是否选人->确定流转提示
        :param checker: 审核人姓名
        """
        window = (By.CSS_SELECTOR, '.el-dialog[aria-label=请选择办理人]')
        confirm_process = (By.CSS_SELECTOR, '.el-dialog[aria-label] .el-dialog__footer .sendFlow')
        if self.is_element_exist(confirm_process, implicitly_timeout=4):
            # 可选人仅 1 人: 直接发送
            self.excute_js_click_ele(self.driver.find_element(*confirm_process))
        elif self.is_element_exist(window, implicitly_timeout=2):
            # 可选人 > 1人: 弹窗选择
            self.clear_and_input(loc=(By.XPATH, '//input[@placeholder="输入名称"]'),value=checker+Keys.ENTER)
            checker_loc = (By.XPATH,
                           f'//*[@class="el-dialog" and @aria-label="请选择办理人"]//*[contains(@class,"custom-tree-node")]//*[contains(text(), "{checker}")]')
            self.excute_js_click_ele(self.explicit_wait_ele_presence(checker_loc))
            content = (By.XPATH, f'//*[@class="cell" and contains(text(), "{checker}")]')
            self.explicit_wait_ele_presence(content)
            confirm_checker = (By.XPATH,
                               '//*[@class="el-dialog" and @aria-label="请选择办理人"]//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')
            self.poll_click(confirm_checker)
            self.excute_js_click_ele(self.explicit_wait_ele_presence(confirm_process))
        return self

    def get_text_implicitly(self, loc):
        """隐式等待获取元素文本"""
        return self.driver.find_element(*loc).text

    def get_ele_text_visitable(self, loc):
        """
        获取可见元素本文信息
        :param loc:元素定位表达式
        :return: 元素文本信息
        """
        ele = self.wait_visibility_ele(loc)
        time.sleep(0.5)  # 等待文本加载成功
        return str(ele.text).strip()

    def get_ele_attr(self, loc, attrname):
        """
        获取元素本文信息
        :param loc:元素定位表达式
        :param attrname:元素属性名
        :return: 元素属性
        """
        attribute = self.find_elem(loc).get_attribute(attrname)
        return attribute

    def get_ele_value(self, loc):
        """
        获取元素value值
        :param loc:元素定位表达式
        :return: 元素value值
        author:yangdeyi
        """
        ele = self.find_elem(loc)
        time.sleep(0.5)  # 多系统交互强制等待
        return self.driver.execute_script('return arguments[0].value;', ele)

    def wait_no_presence_ele(self, loc):
        """等待元素无法定位"""
        self.wait.until(EC.invisibility_of_element_located(loc))

    def wait_invisibility_ele(self, loc):
        """等待元素不可见"""
        self.wait.until(EC.invisibility_of_element(loc))

    def switch_to_handle(self, index=-1):
        """
        跳转至新打开的标签页
        :param index: 标签页的句柄索引
        :return: 新打开的标签页面的标题
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])
        return self.driver.title

    def close_and_return_page(self):
        """关闭当前页面，并切回上个页面"""
        self.close_current_browser()
        self.switch_to_handle()
        time.sleep(0.5)
        return self

    def move_to_ele(self, loc: Union[WebElement, tuple]):
        """
        移动滚动条，使页面可见指定元素
        :param loc: 元素定位表达式
        """
        if isinstance(loc, tuple):
            self.driver.execute_script("arguments[0].scrollIntoView(false)", self.driver.find_element(*loc))
        elif isinstance(loc, WebElement):
            self.driver.execute_script("arguments[0].scrollIntoView(false)", loc)

    def move_to_ele_and_get_text(self, loc):
        """
        移动滚动条，使页面可见指定元素并获取可见元素本文信息
        :param loc: 元素定位表达式
        :return:元素本文信息
        """
        self.move_to_ele(loc)
        text = self.get_ele_text_visitable(loc)
        return text

    def mouse_hover_to_ele(self, loc):
        """
        鼠标悬停到指定元素位置
        :param loc: 元素定位表达式
        :return:
        """
        ele = self.find_elem(loc)
        self.action_chains.move_to_element(ele).perform()

    def mouse_double_click(self, ele):
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()

    def drag_and_drop(self, drag_from: Union[WebElement, tuple],
                      drop_to: Union[WebElement, tuple]):
        """
        拖拽操作
        :param drag_from: 要拖拽的元素定位器或者元素
        :param drop_to: 拖拽至的元素定位器或者元素
        """
        action_chains = ActionChains(driver=self.driver)
        if isinstance(drag_from, tuple) and isinstance(drop_to, tuple):
            drag_from_ele, drop_to_ele = self.wait_presence_ele(drag_from), self.wait_presence_ele(drop_to)
            action_chains.drag_and_drop(drag_from_ele, drop_to_ele).perform()
        elif isinstance(drag_from, WebElement) and isinstance(drop_to, WebElement):
            action_chains.drag_and_drop(drag_from, drop_to).perform()

    def drag_pause_drop(self, drag_from, drop_to, pause_time=1):
        """拖拽过程中加入等待，防止拖拽位置未达到期望位置时，drag_and_drop方法无效时可使用该方法
        @param drag_from: 要拖拽的元素定位器或者元素
        @param drop_to: 拖拽至的元素定位器或者元素
        @param pause_time: 拖拽暂停时间
        """
        drag_from_ele = self.wait_presence_ele(drag_from)
        drop_to_ele = self.wait_presence_ele(drop_to)
        self.action_chains.click_and_hold(drag_from_ele).pause(pause_time).move_to_element(drop_to_ele).release(
            drop_to_ele).perform()

    def input_readonly_js(self, loc, value, need_clear: bool = False):
        """删除readonly属性，并传值"""
        ele = self.find_elem(loc)
        self.clear_readonly_input(loc)
        if need_clear:  # 有默认值需要清理
            ele.send_keys('')
            time.sleep(1)
            ele.clear()
        ele.send_keys(value)

    @staticmethod
    def upload(filepath, exe_path=os.path.join(common_dir, 'upload.exe'), windows_class="[CLASS:#32770]",
               windows_title="打开", control_id_edit="Edit1", control_id_btn="Button1", wait_time="1000"):
        """
        上传文件:使用AutoIt工具辅助，调用exe脚本执行上传操作实现
        :param filepath:需要上传文件的路径
        :param exe_path: AutoIt脚本执行文件路径（输入上传文件路径->点击上传）
        :param windows_class:windows上传控件的class
        :param windows_title:windows上传控件的title
        :param control_id_edit:windows上传控件的输入框id
        :param control_id_btn:windows上传控件的上传按钮id
        :param wait_time:上传文件超时时间
        :return:
        """
        time.sleep(2)
        script = '{0} {1} {2} {3} {4} {5} {6}'.format(exe_path, filepath, windows_class, windows_title, control_id_edit,
                                                      control_id_btn, wait_time)
        os.system(script)
        time.sleep(1)

    @staticmethod
    def upload2(filePath, browser_type="chrome"):
        """
        通过pywin32模块实现文件上传的操作
        :param filePath: 文件的绝对路径
        :param browser_type: 浏览器类型（默认值为chrome）
        :return:
        """
        import win32gui
        import win32con
        time.sleep(2)
        if browser_type.lower() == "chrome":
            title = "打开"
        elif browser_type.lower() == "firefox":
            title = "文件上传"
        elif browser_type.lower() == "ie":
            title = "选择要加载的文件"
        else:
            title = ""  # 这里根据其它不同浏览器类型来修改
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        # 输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

    def is_element_exist(self, loc: tuple, implicitly_timeout: Union[int, float] = 1) -> bool:
        """
        判断元素是否存在->存在返回True 不存在返回False
        :param loc: 元素定位表达式
        :param implicitly_timeout: 隐式等待时间
        """
        try:
            self.driver.implicitly_wait(time_to_wait=implicitly_timeout)
            exist_element = self.driver.find_elements(*loc)
            return True if exist_element else False
        finally:
            self.driver.implicitly_wait(self.Default_Implicit_Timeout)

    def judge_element_whether_existence(self, loc: tuple, implicitly_timeout: Union[int, float] = 1) -> bool:
        """
        判断元素是否存在->存在返回True 不存在返回False
        :param loc: 元素定位表达式
        :param implicitly_timeout: 隐式等待时间
        """
        try:
            self.driver.implicitly_wait(time_to_wait=implicitly_timeout)
            exist_element = self.driver.find_elements(*loc)
            return True if exist_element else False
        finally:
            self.driver.implicitly_wait(self.Default_Implicit_Timeout)

    @staticmethod
    def scan_qr_code(img_path):
        """
        识别二维码，解析出二维码的data信息
        """
        import numpy as np
        import cv2
        from pyzbar import pyzbar
        cv_img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
        qrcode_data = pyzbar.decode(cv_img)
        qrcode_text = qrcode_data[0].data.decode('utf-8')
        return qrcode_text

    def screenshot_as_file(self, real_time=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")):
        """截图保存"""
        file = os.path.join(other_dir, f"失败截图_{real_time}.png").replace('\\', '/')
        self.driver.get_screenshot_as_file(file)

    def open_browser(self, url):
        """
        最大化浏览器并访问网址
        :param url:访问的网址
        """
        self.driver.maximize_window()
        self.driver.get(url)

    def close_browser(self):
        """退出浏览器"""
        self.driver.quit()
        if sys.platform != 'win32':
            if hasattr(self.driver, 'driver_service'):
                driver_service = getattr(self.driver, 'driver_service')
                driver_service.stop()

    def close_current_browser(self):
        """关闭当前的一个浏览器窗口"""
        self.driver.close()
        time.sleep(0.5)
        return self

    def publish_get_info(self, *args: tuple, **kwargs):
        """
        获取列表项信息的通用方法（1页）
        :param args:元素定位表达式
        :param kwargs:列表项字段，值为列表/元组
        :return :列表项信息
        """
        self.__init__(self.driver, implicitly_timeout=3, web_driver_timeout=3)
        value = map(lambda x: list(map(lambda y: y.text, x)), [self.find_elms(loc) for loc in args])
        info = list(map(lambda *arg: dict(zip(*kwargs.values(), arg)), *value))
        self.__init__(self.driver)
        return info

    def get_list_infos(self, num: int, *args, **kwargs):
        """
        获取列表信息
        :param num:第一个目标列表项标签位置
        :param args:列表项名称
        :param tab:多tab场景获取列表项
        """
        loc_str = '//*[contains(@*,"is-scrolling")]//td[{}]'
        if 'tab' in kwargs:
            loc_str = loc_str.replace('//*', '//div[@id="{}"]//*'.format(kwargs['tab']))
        if 'box' in kwargs:
            loc_str = loc_str.replace('//*', '//div[@role="dialog"]//*')
        time.sleep(1)
        infos = self.publish_get_info(
            *map(lambda x: (By.XPATH, loc_str.format(x)), range(num, num + len(args))), title=args)
        return infos

    def get_pic_code(self, loc):
        """
        获取验证码图片的验证码
        :param loc: 验证码图片元素定位表达式
        :return: 验证码
        """
        import pytesseract
        from PIL import Image
        img2 = Image.open(self.screenshot_locator(loc))
        text = pytesseract.image_to_string(img2)
        code_list = [i for i in text][0:4]
        code = ''.join(code_list)
        return code

    def screenshot_locator(self, locator):
        """对页面元素对象进行截图,并返回页面元素的截图对象"""
        png_path2 = os.path.join(DOWNLOAD_PATH, str(time.time()) + '.png')
        self.wait_visibility_ele(locator)
        self.find_elem(locator).screenshot(png_path2)
        return png_path2

    @staticmethod
    def get_picture_by_url(src, cookies=None, img_name: str = "url图片.png"):
        """
        src:图片的url路径
        imgname:图片名
        headers:登录后的headers
        """
        import requests
        r = requests.get(src, cookies=cookies)
        img_path = os.path.join(DOWNLOAD_PATH, img_name)
        with open(img_path, 'wb') as f:
            f.write(r.content)
        return img_path

    def switch_to_window(self, index: int):
        """切换指定的浏览器窗口，index表示第几个窗口，从0开始"""
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[index])
        return self

    def move_and_move_to_click(self, loc1, loc2):
        """移动到第一个元素后，显示第二个元素，再移动到第二个元素进行点击"""
        action = ActionChains(self.driver)
        ele1 = self.find_elem(loc1)
        action.move_to_element(ele1).perform()
        self.wait_ele_be_click(loc2)
        ele2 = self.find_elem(loc2)
        action.move_to_element(ele2).click().perform()

    def refresh(self, delay=1):
        """
        刷新页面
        delay:刷新后等待时间
        """
        self.driver.refresh()
        time.sleep(delay)
        return self

    @staticmethod
    def get_catalog_file_number(path):
        """获取目录下的文件个数"""
        files = os.listdir(path)
        return len(files)

    def upload_input_file(self, loc1, loc2, file):
        """
        可使用于无界面模式运行
        :param loc1:用于点击导入文件按钮，
        :param loc2:点击按钮后出现的input标签元素
        :param file:文件字符串路径
        """
        self.element_click(loc1)
        self.find_elem(loc2).send_keys(file)
        if sys.platform == "win32":
            from pykeyboard import PyKeyboard
            time.sleep(3)  # 等待弹窗出现
            pyk = PyKeyboard()
            pyk.tap_key(pyk.cancel_key, 1)
        else:
            pass

    def upload_input_file_no_click(self, loc_input, file):
        """
        :param loc_input:上传文件的loc
        :param file:上传文件路径
        """
        if sys.platform == "win32":
            from pykeyboard import PyKeyboard
            time.sleep(2)
            pyk = PyKeyboard()
            pyk.tap_key(pyk.cancel_key, 1)
        else:
            pass
        self.find_elem(loc_input).send_keys(file)

    def get_current_url(self):
        """
        获取并返回当前页面url地址
        """
        current_url = self.driver.current_url
        return current_url

    def delete_path_file(self, path):
        """
        递归删除该路径目录下所有文件（包括子目录下的文件, 慎用）
        :param path: 传入目录路径
        """
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.delete_path_file(c_path)
            else:
                os.remove(c_path)

    def clear_download_dir(self):
        """清空下载目录"""
        from common import DOWNLOAD_PATH
        self.delete_path_file(DOWNLOAD_PATH)

    @staticmethod
    def get_ele_attribute(ele, attribute_name):
        """获取元素属性值"""
        return ele.get_attribute(f'{attribute_name}')

    def del_attribute(self, loc, attribute_name):
        """删除元素属性"""
        self.driver.execute_script('arguments[0].removeAttribute(arguments[1])', self.find_elem(loc), attribute_name)

    def edit_attribute(self, loc, attribute_name, value):
        self.driver.execute_script('arguments[0].setAttribute(arguments[1],arguments[2])', self.find_elem(loc),
                                   attribute_name, value)

    def edit_ele_text(self, loc, value):
        self.driver.execute_script('arguments[0].textContent=arguments[1]', self.find_elem(loc), value)

    def wait_browser_close_switch_latest(self, times=5, window_num: int = 0):
        """浏览器有关闭窗口操作时，判断浏览器窗口是否关闭完成，默认为0时自动获取当前的窗口数量,关闭后返回最新的窗口页面"""
        window_num = window_num if window_num else len(self.driver.window_handles)
        while times > 0:
            current_window = len(self.driver.window_handles)  # 当前浏览器窗口数
            if current_window < window_num:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                return
            else:
                times -= 0.5
            time.sleep(0.5)

    def wait_open_new_browser_and_switch(self, times=5):
        """判断浏览器窗口是否有新增并切入新窗口"""
        current_window = self.driver.current_window_handle
        while times > 0:
            time.sleep(0.5)
            new_window = self.driver.window_handles[-1]
            if current_window != new_window:
                self.driver.switch_to.window(new_window)
                break
            else:
                times -= 0.5

    def custom_show_wait(self, loc, total_time=3, interval=0.2):
        """
        自定义显示等待
        total_time：找寻总时长
        interval：间隔多少时长找一次
        找到后停止找寻并返回该元素
        """
        wait = WebDriverWait(self.driver, total_time, interval)
        return wait.until(lambda driver: self.driver.find_element(*loc))

    def locator_dialog_btn(self, btn_name: str, dialog_title: str = '', times: int = 0.5, need_close: bool = False):
        """
        点击role=dialog弹窗中的操作按钮
        :param btn_name: 按钮名称
        :param dialog_title: 信息框的主题，默认为空
        :param times: 默认等待时长
        :param need_close: 是否需要关闭
        """
        time.sleep(1)
        click_element = WebElement
        btn = (By.XPATH, f'{self._xpath_dialog(dialog_title)}//*[contains(text(),"{btn_name}")]')
        elements = self.find_elements_displayed(btn)
        if len(elements) == 1:
            click_element = elements[0]
        else:
            for i in elements:
                if str(i.text).strip() == btn_name:
                    click_element = i
                    break
        self.excute_js_click_ele(click_element)
        time.sleep(times)
        if need_close:
            self.locator_close_dialog_window(dialog_title=dialog_title)
        return self

    @allure.step('获取提示信息')
    def wait_tip(self):
        """等待提示信息出现,返回提示信息"""
        tip_ele = (By.CSS_SELECTOR, 'div[role=alert] .el-message__content')  # 提示信息
        ele = WebDriverWait(self.driver, 3, 0.2).until(EC.visibility_of_element_located(tip_ele))
        if ele.text:
            return str(ele.text).strip()
        else:
            return False

    @allure.step('获取操作成功提示信息')
    def wait_success_tip(self, times=5):
        """等待成功的提示信息，并返回提示信息"""
        tip_ele = (By.CSS_SELECTOR, 'div[role=alert] [class*=success]+p')  # 提示信息
        ele = WebDriverWait(self.driver, times, 0.2).until(EC.visibility_of_element_located(tip_ele))
        if ele:
            return str(self.find_elem_visibility(tip_ele).text).strip()
        else:
            return False

    @allure.step('获取操作失败提示信息')
    def wait_fail_tip(self, times=5):
        """等待成功的提示信息，并返回提示信息"""
        tip_ele = (By.CSS_SELECTOR, 'div[role=alert] [class*=error]+p')  # 提示信息
        ele = WebDriverWait(self.driver, times, 0.2).until(EC.visibility_of_element_located(tip_ele))
        if ele.text:
            return str(ele.text).strip()
        else:
            return False

    def get_required_prompt(self) -> str:
        """返回必填信息的提示信息"""
        tip_ele = (By.CSS_SELECTOR, '.ds-error-text')
        self.wait_visibility_ele(tip_ele)
        return str(self.driver.find_element(*tip_ele).text).strip()

    def get_all_required_prompt(self):
        """返回所有必填信息的提示信息"""
        return self.get_ele_texts_visitable((By.CSS_SELECTOR, '.ds-error-text'))

    def clear_readonly_input(self, loc):
        """删除readonly属性,并清理输入内容"""
        ele = self.find_elem(loc)
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', ele)
        ele.clear()
        self.driver.execute_script('arguments[0].value=""', ele)

    @staticmethod
    def get_dir_file_path(path):
        """
        :param path: 传入目录路径
        :return:当前目录下所有文件路径
        """
        return [os.path.join(path, i) for i in os.listdir(path)]

    def driver_cookies(self):
        """获取登录后浏览器的cookies信息"""
        cookies = {}
        for i in self.driver.get_cookies():
            cookies[i["name"]] = i["value"]
        return cookies

    def _css_dialog(self, dialog_title: str):
        """返回css定位器dialog定位前缀"""
        return self.CSS_DIALOG.format(dialog_title) if dialog_title else ''

    def _xpath_dialog(self, dialog_title: str):
        """返回xpath定位器dialog定位前缀"""
        return self.XPATH_DIALOG.format(dialog_title) if dialog_title else ''

    def _css_tags(self, dialog_title: str):
        """返回css定位器多tag页签定位前缀"""
        return self.CSS_TAGS if self._is_tags(dialog_title=dialog_title) else ''

    def _xpath_tags(self, dialog_title: str):
        """返回xpath定位器多tag页签定位前缀"""
        return self.XPATH_TAGS if self._is_tags(dialog_title=dialog_title) else ''

    def _is_tags(self, dialog_title: str = ""):
        """
        判断当前页面是否存在多个tag页签
        :param dialog_title: 信息框的主题，默认为空
        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)  # 获取css定位dialog前缀
        tags_locator = (By.CSS_SELECTOR, f'{dialog_css}[role=tabpanel],'
                                         f'{dialog_css}[ctrl_type="{self.table_ctrl_type}"]')
        tags_elements = self.find_elms(tags_locator)
        if len(tags_elements) >= 2:
            tabs = 0  # [role=tabpanel]的数量
            data_grid = 0  # [ctrl_type="dsf.datagrid"]的数量
            for i in tags_elements:
                if i.get_attribute('role') == 'tabpanel':
                    tabs += 1
                    if tabs > 1:
                        return True
                elif i.get_attribute('ctrl_type') == 'dsf.datagrid':
                    data_grid += 1
                    if data_grid > 1:
                        return True
        else:
            return False

    def locator_get_js_input_value(self, ctrl_id: str, times=5):
        """通过js获取input元素的值(当前值无法通过元素定位器获取对应的属性或text)"""
        input_value = (By.CSS_SELECTOR, f'[ctrl-id="{ctrl_id}"] input')
        element = self.find_elem(input_value)
        while times:
            time.sleep(0.5)
            value = self.driver.execute_script(f'return arguments[0].value', element)
            if value:
                return value
            else:
                times -= 0.5
        return

    def locator_close_dialog_window(self, dialog_title: str = '', times: int = 1):
        """
        作者：李国彬
        点击右上角的关闭按钮关闭页面指定弹窗
        :param dialog_title: 窗口的aria-label属性
        :param times: 关闭窗口后元素加载等待时间
        """
        close_btn = (By.CSS_SELECTOR, f'{self._css_dialog(dialog_title=dialog_title)}button[aria-label="Close"]')
        elements = self.find_elements_displayed(close_btn)
        if len(elements) == 1:
            self.excute_js_click_ele(elements[0])
            time.sleep(times)  # 等待元素重新加载
        else:
            raise ValueError(f'{close_btn}元素定位不是唯一可见元素')

    def locator_text_input(self, ctrl_id: str, value, tag_type='input', is_file: bool = False,
                           is_readonly: bool = False, dialog_title: str = ''):
        """
        作者：李国彬
        非时间格式输入框
        :param ctrl_id: 元素的唯一ctrl-id
        :param value: 传入的值
        :param tag_type: 标签类别，默认为input
        :param is_file: 是否上传文件
        :param is_readonly: 是否属于只读属性，如果是则会自动删除只读属性后输入值
        :param dialog_title: 所属的dialog窗口
        """
        dialog_title = self._css_dialog(dialog_title)
        locator = (By.CSS_SELECTOR, f'{dialog_title}[ctrl-id={ctrl_id}] {tag_type}')
        if is_file:
            self.find_elem(locator).send_keys(value)
        elif is_readonly:
            self.input_readonly_js(locator, value)
        else:
            self.clear_and_input(locator, value)

    def locator_select_list_value(self, ctrl_id: str, value: str = None, wait_time=1):
        """
        作者：李国彬
        下拉列表选择框
        @param ctrl_id: 元素的唯一ctrl-id
        @param value: 传入的值,不传值则默认选择第一个有效值
        @param wait_time: 点击下拉框等待时间，默认为0
        """
        click_locator = (By.CSS_SELECTOR, '[ctrl-id={}] input'.format(ctrl_id))
        self.excute_js_click(click_locator)
        if value != '随机':
            value_locator = (By.XPATH, f'//*[@class="el-scrollbar"]//*[contains(text(),"{value}")]')
            elements = self.find_elms(value_locator)
            if len(elements) == 1:
                self.driver.execute_script('arguments[0].click();', elements[0])
            else:
                time.sleep(wait_time)
                for i in elements:
                    if str(i.text) == value:
                        self.driver.execute_script('arguments[0].click();', i)
        else:
            self.excute_js_click((By.XPATH, '//*[@x-placement]//li[2]'))
        return

    def locator_select_radio(self, ctrl_id: str, value):
        """
        作者：李国彬
        radio选项勾选
        :param ctrl_id: 元素的唯一ctrl-id
        :param value: 传入的值
        """

        def click_radio(tmp):
            click_locator = (By.XPATH, f'//*[@ctrl-id="{ctrl_id}"]//*[contains(text(),"{tmp}")]')
            ele = self.find_elms(click_locator)
            for j in ele:
                if str(j.text).strip() == tmp:
                    self.excute_js_click_ele(j)

        # 多勾选
        if isinstance(value, list):
            for i in value:
                click_radio(i)
        # 单勾选
        else:
            click_radio(value)

    def locator_search_magnifier(self, ctrl_id: str, times: int = 1):
        """
        作者：李国彬
        点击对应选项的放大镜查询按钮
        :param ctrl_id: 元素的唯一ctrl-id
        :param times: 默认等待加载时间
        """
        click_magnifier = (By.CSS_SELECTOR, '[ctrl-id={}] .el-icon-search'.format(ctrl_id))
        self.excute_js_click(click_magnifier)
        time.sleep(times)

    def locator_date_range(self, ctrl_id: str, start_date: str, end_date: str, confirm: bool = False):
        """
        作者：李国彬
        输入日期范围的开始日期和结束日期
        :param ctrl_id: 元素的唯一ctrl-id
        :param start_date: 开始日期
        :param end_date: 结束日期
        :param confirm: 是否需要点击确定按钮
        """
        start_date_locator = (By.XPATH, '//*[@ctrl-id="{}"]//input[1]'.format(ctrl_id))
        end_date_locator = (By.XPATH, '//*[@ctrl-id="{}"]//input[2]'.format(ctrl_id))
        click_text = (By.CSS_SELECTOR, '[ctrl-id={}] label'.format(ctrl_id))
        confirm_btn = (By.XPATH, '//*[@x-placement]//*[contains(text(), "确定")]')
        self.input_readonly_js(start_date_locator, start_date)
        self.input_readonly_js(end_date_locator, end_date)
        if confirm:
            element = self.find_elements_displayed(confirm_btn)
            element[0].click()
            # self.element_click(confirm_btn)
        else:
            self.move_to_click(click_text)

    def locator_date_time_range(self, ctrl_id: str, start_date: str, start_time: str, end_date: str, end_time: str):
        """
        作者：李国彬
        输入日期范围的开始日期和结束日期
        :param ctrl_id: 元素的唯一ctrl-id
        :param start_date: 开始日期
        :param start_time: 开始时间
        :param end_date: 结束日期
        :param end_time: 结束时间
        """
        click_i = (By.CSS_SELECTOR, f'[ctrl-id="{ctrl_id}"] i')
        self.element_click(click_i)
        start_day_input1 = (By.XPATH, '//*[@x-placement]//input[@placeholder="开始日期"]')
        start_day_input2 = (By.XPATH, '//*[@x-placement]//input[@placeholder="开始时间"]')
        end_day_input1 = (By.XPATH, '//*[@x-placement]//input[@placeholder="结束日期"]')
        end_day_input2 = (By.XPATH, '//*[@x-placement]//input[@placeholder="结束时间"]')
        self.clear_and_input(start_day_input1, start_date)
        self.clear_and_input(start_day_input2, start_time)
        self.clear_and_input(end_day_input1, end_date)
        self.clear_and_input(end_day_input2, end_time)
        confirm_btn = (By.XPATH, '//*[@x-placement]//span[contains(text(), "确定")]')
        self.element_click(confirm_btn)

    def locator_date(self, ctrl_id: str, value: str, confirm: bool = False, need_clear: bool = False):
        """
        作者：李国彬
        输入单个日期
        :param ctrl_id: 元素的唯一ctrl-id
        :param value: 时间
        :param confirm: 是否需要点击确定按钮
        :param need_clear： 时间是否有默认值需要清理
        """
        locator = (By.CSS_SELECTOR, '[ctrl-id={}] input'.format(ctrl_id))
        click_text = (By.CSS_SELECTOR, '[ctrl-id={}] label'.format(ctrl_id))
        confirm_btn = (By.XPATH, '//*[@x-placement]//*[contains(text(), "确定")]')
        self.input_readonly_js(locator, value, need_clear)
        if confirm:
            element = self.find_elements_displayed(confirm_btn)
            element[0].click()
            # self.element_click(confirm_btn)
        else:
            self.move_to_click(click_text)

    def locator_switch_tag(self, tag_name: str, times=2.0, role_value: str = 'tablist', dialog_title: str = ""):
        """
        作者：李国彬
        点击多页签的tag名称切换页签
        :param tag_name: 页签名称
        :param times: 切换页签时等待时长
        :param role_value: 默认页签列表的role值
        :param dialog_title: 信息框的主题，默认为空
        """
        dialog_xpath = self._xpath_dialog(dialog_title=dialog_title)
        locator = (By.XPATH, f'{dialog_xpath}//*[@role="{role_value}"]//*[contains(text(), "{tag_name}")]')
        self.excute_js_click(locator)
        time.sleep(times)
        return self

    def locator_button(self, button_title: str, dialog_title: str = ""):
        """
        作者：李国彬
        点击按钮定位对象
        :param button_title: 按钮的title属性
        :param dialog_title: 信息框的主题，默认为空
        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        locator = (By.CSS_SELECTOR, f'{dialog_css}[title="{button_title}"].ds-button')
        self.excute_js_click(locator)
        return self

    def locator_tag_button(self, button_title: str, dialog_title: str = "", file_path: str = '', times: int = 2):
        """
        作者：李国彬
        点击有tag页面按钮
        :param button_title: 按钮的title属性
        :param dialog_title: 信息框的主题，默认为空
        :param times: 文件上传加载等待时间
        :param file_path: 上传文件路径
        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        tags_css = self._css_tags(dialog_title=dialog_title)
        if file_path:
            import_input = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}[title={button_title}]+input[type=file]')
            self.find_elem(import_input).send_keys(file_path)
        else:
            locator = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}[title="{button_title}"].ds-button')
            self.excute_js_click(locator)
        time.sleep(times)
        return self

    def locator_click_wait_input_file(self, btn_name, file, times=3):
        """
        作者：李国彬
        :param file: 上传的文件
        :param btn_name: 按钮名称
        :param times: 默认等待上传文件时间
        """
        self.locator_dialog_btn(btn_name=f'{btn_name}')
        time.sleep(1)
        input_loc = (By.CSS_SELECTOR, 'input[type="file"]')
        self.find_elms(input_loc)[-1].send_keys(file)
        time.sleep(times)
        return self

    def locator_view_button(self, button_title: str, id_value: str, dialog_title: str = "", file=''):
        """
        作者：李国彬
        返回展示列表中按钮定位对象(支持存在多个页签时相同按钮的定位)
        :param button_title: 按钮的title属性
        :param id_value:列表中的每行的唯一属性
        :param dialog_title: 信息框的主题，默认为空
        :param file: 操作按钮上传文件时对应的文件路径
        """
        dialog_xpath = self._xpath_dialog(dialog_title=dialog_title)
        tags_xpath = self._xpath_tags(dialog_title=dialog_title)
        if file:
            locator = (By.XPATH, f'{dialog_xpath}{tags_xpath}//*[contains(text(),"{id_value}") or contains(@title, '
                                 f'"{id_value}")]//ancestor::tr//*[@ctrl_type="dsf.buttonbar"]//*[contains(text(),'
                                 f'"{button_title}") or contains(@title, "{button_title}")]/../..//input[@type="file"]')
            self.find_elem(locator).send_keys(file)
        else:
            locator = (By.XPATH, f'{dialog_xpath}{tags_xpath}//*[contains(text(),"{id_value}") or contains(@title, '
                                 f'"{id_value}")]//ancestor::tr//*[@ctrl_type="dsf.buttonbar"]//*[contains(text(),'
                                 f'"{button_title}") or contains(@title, "{button_title}")]')
            self.excute_js_click(locator)
        return self

    def locator_tag_search_input(self, placeholder: str, value: str = "", dialog_title: str = "", times=0,
                                 enter: bool = False):
        """
        作者：李国彬
        有tag页签的查询页面的输入框(支持多页签下的输入框)
        :param placeholder: 输入框的placeholder属性值
        :param value: 输入值，默认为空
        :param dialog_title: 信息框的主题，默认为空
        :param times: 输入后的等待时间
        :param enter: 输入后是否需要回车
        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        tags_css = self._css_tags(dialog_title=dialog_title)
        locator = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}[placeholder="{placeholder}"]')
        if enter:
            times = 2  # 如果回车则等待查询数据刷新
            self.clear_and_input_enter(locator, value)
        else:
            self.clear_and_input(locator, value)
        if times:
            time.sleep(times)

    def locator_search_input(self, placeholder: str, value: str = "", dialog_title: str = "", times=0,
                             enter: bool = False):
        """
        作者：李国彬
        非多页签的查询页面的输入框
        :param placeholder: 输入框的placeholder属性值
        :param value: 输入值，默认为空
        :param dialog_title: 信息框的主题，默认为空
        :param times: 输入后的等待时间
        :param enter: 输入后是否需要回车
        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        locator = (By.CSS_SELECTOR, f'{dialog_css}[placeholder="{placeholder}"]')
        if enter:
            self.clear_and_input_enter(locator, value)
            times = 2
        else:
            self.clear_and_input(locator, value)
        if times:
            time.sleep(times)

    def locator_tag_search_button(self, times=2, dialog_title: str = ""):
        """
        作者：李国彬
        查询页面的点击查询按钮(支持多页签下的输入框)
        :param times: 点击查询后的等待时长
        :param dialog_title: 信息框的主题，默认为空

        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        tags_css = self._css_tags(dialog_title=dialog_title)
        locator = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}button.search-button')
        self.element_click(locator)
        time.sleep(times)

    def locator_view_num(self, dialog_title: str = ""):
        """
        作者：李国彬
        返回展示列表中的数量（int）(支持多页签)
        :param dialog_title: 信息框的主题，默认为空
        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        tags_css = self._css_tags(dialog_title=dialog_title)
        locator = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}.el-pagination__total')
        return int(str(self.find_elem(locator).get_attribute("textContent")).split(' ')[1])

    def _locator_view_header(self, is_tags: bool, dialog_title: str = ""):
        """
        获取列表列头并返回
        :param dialog_title: 信息框的主题，默认为空
        """
        result = {}  # 返回列头索引和列头名称的字典
        dialog_css = self.CSS_DIALOG.format(dialog_title) if dialog_title else ''
        tags_css = self.CSS_TAGS if is_tags else ''
        # heads_name = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}.el-table__header-wrapper th span:first-child')
        # names_ele = self.find_elms(heads_name)  # 列头字段的页面对象
        # result = [str(i.get_attribute('textContent')).strip() for i in names_ele if i.get_attribute('textContent')]

        heads_name = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}.el-table__header-wrapper th')
        names_ele = self.find_elms(heads_name)  # 列头字段的页面对象
        for i in range(len(names_ele)):
            if 'gutter' not in names_ele[i].get_attribute('class'):
                name = names_ele[i].get_attribute('textContent').strip()  # 获取列头名称
                if name:
                    result[i + 1] = name
        return result

    def __locator_view_row_values(self, row_index, names, dialog_css, css_tags, id_values: list = None):
        """
        作者：李国彬
        返回第一个满足表达式的对应行列头-值的字典信息（包括行号）
        :param row_index: 列表数据的行号
        :param names: 列表数据的列头字段列表
        :param dialog_css: dialog弹窗css定位前缀
        :param css_tags: tags页css定位前缀
        :param id_values: 需要获取的列头字段列表
        """
        # values = []  # 初始化当前行的值
        # values_element = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] '
        #                                    f'tr:nth-child({row_index}) td')
        # value_len = len(self.find_elms(values_element))  # 获取当前行值的个数
        # for j in range(1, value_len + 1):
        #     td_value = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] '
        #                                  f'tr:nth-child({row_index}) td:nth-child({j})')
        #     element = self.find_elem(td_value)  # 获取行元素对象
        #     # 筛选掉隐藏的元素列，获取非隐藏元素的列值
        #     if 'sticky' not in element.get_attribute('style') and 'is-hidden' not in element.get_attribute('class'):
        #         value = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] '
        #                                   f'tr:nth-child({row_index}) td:nth-child({j}) [class$=__value],'
        #                                   f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] '
        #                                   f'tr:nth-child({row_index}) td:nth-child({j}) [href],'
        #                                   f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] '
        #                                   f'tr:nth-child({row_index}) td:nth-child({j}) [style]')
        #         # 获取对应行列中匹配的第一个值
        #         # values_ele = [i.get_attribute('textContent') for i in self.find_elms(value)]
        #         # value_ele = list(filter(None, values_ele))[0]
        #         element = self.driver.find_elements(*value)
        #         # 判断元素是否找到，找到则获取文本，没有则复制为空
        #         if element:
        #             values.append(str(element[0].get_attribute('textContent')).strip())
        #         else:
        #             values.append('')
        #     else:
        #         continue
        res = {}
        for index, name in names.items():
            # 获取对应列头的值
            value = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] '
                                      f'tr:nth-child({row_index}) td:nth-child({index})')
            element = self.driver.find_elements(*value)
            # 判断元素是否找到，找到则获取文本，没有则复制为空
            if element:
                res[name] = str(element[0].get_attribute('textContent')).strip()
            else:
                res[name] = ''
        # if len(values) != len(names):
        #     raise Exception("列头字段和列头值字段长度不相同，请检查定位是否准确")
        # elif id_values:
        #     name_value = {name: values[names.index(name)] for name in id_values}  # 根据列头字段列表获取对应的值
        # else:
        #     name_value = dict(zip(names, values))  # 列头和值的键值对
        # return name_value
        return res

    def _locator_view_value_index_list(self, dialog_css, css_tags):
        """用于每一行的值对应td的下标索引"""
        index_list = []
        values_element = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] '
                                           f'tr:nth-child(1) td')
        class_elems = self.find_elms(values_element)
        for index, elem in enumerate(class_elems):
            if 'is-hidden' not in elem.get_attribute('class'):
                index_list.append(index + 1)
        return index_list

    def locator_view_conditions(self, conditions: str = '', dialog_title: str = ""):
        """
        作者：李国彬
        返回第一个满足表达式的对应行列头-值的字典信息（包括行号）
        :param conditions: 条件表达式，例如 '列头1 == 列头2 and "字符串" in "列头1"',为空则返回第一行数据
        :param dialog_title: 信息框的主题，默认为空
        """
        is_tags = self._is_tags(dialog_title=dialog_title)  # 是否多页签
        header_list = self._locator_view_header(is_tags=is_tags, dialog_title=dialog_title)  # 获取列头字段
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        css_tags = self.CSS_TAGS if is_tags else ''
        # total_num = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] tr')
        # num = len(self.find_elms(total_num))  # 当前列表显示数据行数
        # # 获取列表和值的键值对
        # for i in range(1, num + 1):
        #     # 获取每一行的键值对
        #     name_value = self.__locator_view_row_values(row_index=i, names=header_list, dialog_css=dialog_css,
        #                                                 css_tags=css_tags, id_values=[])
        #     # 判断查询条件是否满足
        #     if conditions:
        #         exp_condition = conditions
        #         # 替换表达式的变量
        #         for name in name_value.keys():
        #             if name in conditions:
        #                 exp_condition = exp_condition.replace(name, name_value[name])
        #         # 判断表达式是否满足条件
        #         if eval(exp_condition):
        #             name_value["行号"] = i  # 输出匹配的行号
        #             return name_value
        #     else:
        #         return name_value
        total_num = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] tr')
        num = len(self.find_elms(total_num))  # 当前列表显示数据行数
        # 获取列表和值的键值对
        for i in range(1, num + 1):
            # 获取每一行的键值对
            name_value = self.__locator_view_row_values(row_index=i, names=header_list, dialog_css=dialog_css,
                                                        css_tags=css_tags, id_values=[])
            # 判断查询条件是否满足
            if conditions:
                exp_condition = conditions
                # 替换表达式的变量
                for name, value in name_value.items():
                    if name in conditions:
                        exp_condition = exp_condition.replace(name, value)
                # 判断表达式是否满足条件
                if eval(exp_condition):
                    return name_value
            else:
                return name_value
        return []

    def locator_view_info(self, dialog_title: str = "", id_values: list = None):
        """
        作者：李国彬
        返回展示列表中列头对应键值对列表
        :param id_values: 列头名称参数列表
        :param dialog_title: 信息框的主题，默认为空
        """
        result = []
        is_tags = self._is_tags(dialog_title=dialog_title)
        names = self._locator_view_header(is_tags=is_tags, dialog_title=dialog_title)  # 获取列头字段
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        css_tags = self.CSS_TAGS if is_tags else ''
        total_num = (By.CSS_SELECTOR, f'{dialog_css}{css_tags}[class^="el-table__body-wrapper is-scrolling"] tr')
        num = len(self.find_elms(total_num))
        # 获取列表和值的键值对
        for i in range(1, num + 1):
            # 获取每一行的键值对
            name_value = self.__locator_view_row_values(row_index=i, names=names, dialog_css=dialog_css,
                                                        css_tags=css_tags, id_values=id_values)
            result.append(name_value)
        return result

    def locator_view_value_click(self, id_value: str, header: str, dialog_title: str = ""):
        """
        作者：李国彬
        点击表单中对应的可点击的值
        :param id_value: 数据值区分行数的唯一值，例如：学号的值，姓名等
        :param header: 要点击的值对应的列头名称
        :param dialog_title: 信息框的主题，默认为空
        """
        dialog_xpath = self._xpath_dialog(dialog_title=dialog_title)
        tags_xpath = self._xpath_tags(dialog_title=dialog_title)
        is_tags = self._is_tags(dialog_title=dialog_title)
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        css_tags = self._css_tags(dialog_title=dialog_title)
        header_list = self._locator_view_header(is_tags=is_tags, dialog_title=dialog_title)
        # values_index = self._locator_view_value_index_list(dialog_css=dialog_css, css_tags=css_tags)
        # if len(header_list) != len(values_index):
        #     raise Exception("列头字段和列头值字段长度不相同，请检查定位是否准确")
        # else:
        #     index = values_index[header_list.index(header)]  # 获取对应列头的索引值
        #     click_ele = (By.XPATH, f'{dialog_xpath}{tags_xpath}//*[contains(text(), "{id_value}")]//ancestor::tr'
        #                            f'//td[{index}][not(contains(@class,"is-hidden"))]//*[@href or @style]')
        #     self.element_click(click_ele)
        # 获取对应列头的索引值
        for index, name in header_list.items():
            if name == header:
                click_ele = (By.XPATH, f'{dialog_xpath}{tags_xpath}//*[contains(text(), "{id_value}")]//ancestor::tr'
                                       f'//td[{index}][not(contains(@class,"is-hidden"))]//*[@href or @style]')
                self.element_click(click_ele)
                break

    def get_shelter_ele_text(self, loc):
        """获取遮蔽住的元素文本"""
        return self.driver.execute_script("return arguments[0].innerHTML", self.find_elem(loc))

    def get_input_already_exists_text(self, loc):
        """获取input标签中已存在的value的元素文本"""
        return self.driver.execute_script("return arguments[0].value", self.find_elem(loc))

    def locator_view_select(self, id_value: str, dialog_title: str = ''):
        """
        作者：李国彬
        勾选表单对应的项
        :param id_value: 数据值区分行数的唯一值，例如：学号的值，姓名等
        :param dialog_title: dialog页签名称
        """
        dialog_xpath = self.XPATH_DIALOG.format(dialog_title) if dialog_title else ''
        tags_xpath = self._xpath_tags(dialog_title=dialog_title)
        select = (By.XPATH, f'{dialog_xpath}{tags_xpath}//*[@title="{id_value}"]/ancestor::tr//label')
        if 'is-checked' not in self.find_elem(select).get_attribute('class'):  # 判断是否已勾选
            self.excute_js_click(select)
            time.sleep(1)
        return self

    def locator_view_select_all(self, dialog_title: str = ''):
        """
        作者：李国彬
        全选勾选表单对应的项
        :param dialog_title: dialog页签名称
        """
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        tags_css = self._css_tags(dialog_title=dialog_title)
        select_click = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}table.el-table__header label')
        if 'is-checked' not in self.find_elem(select_click).get_attribute('class'):  # 判断是否已勾选
            self.excute_js_click(select_click)
            time.sleep(1)
        return self

    def locator_more_tip_button(self, button_title: str, file_path: str = '', times: int = 2):
        """
        作者：李国彬
        点击更多按钮下的操作按钮
        :param button_title: 按钮名称
        :param file_path: 上传文件路径
        :param times: 导入文件后等待加载时间
        """
        css_tags = self.CSS_TAGS if self._is_tags() else ''
        more_btn = (By.CSS_SELECTOR, f'{css_tags}[title=更多]')
        self.excute_js_click(more_btn)
        time.sleep(1)
        if file_path:  # 存在文件则向元素input传文件
            import_input = (By.CSS_SELECTOR, f'[role=tooltip][aria-hidden=false] [title="{button_title}"]'
                                             f'+input[type=file]')
            self.find_elem(import_input).send_keys(file_path)
            time.sleep(times)
        else:  # 否则点击对应按钮
            click_btn = (By.CSS_SELECTOR, f'[role=tooltip][aria-hidden=false] [title="{button_title}"]')
            self.excute_js_click(click_btn)
        self.excute_js_click(more_btn)
        return self

    def locator_left_menu_click(self, button_title: str, menu_title: str = '', times=2):
        """
        作者：李国彬
        判断左侧菜单栏的菜单是否展开,没有展开则点击使其展开
        :param menu_title: 需要判断是否展开的菜单名称，默认为空，则没有菜单需要判断是否展开
        :param button_title: 需要点击的菜单名称
        :param times: 点击菜单后默认等待数据加载的时长
        """
        if menu_title:
            # 菜单按钮定位
            menu_status = (By.XPATH, f'//*[@ctrl_type="dsf.virtualscroll"]//*[@title="{menu_title}"]/..')
            # 子菜单定位
            button_click = (By.CSS_SELECTOR, f'[ctrl_type="dsf.virtualscroll"] '
                                             f'[title="{menu_title}"]+div [title="{button_title}"]')
            if 'show' not in self.find_elem(menu_status).get_attribute('class'):
                menu_button = (By.XPATH, f'//*[@ctrl_type="dsf.virtualscroll"]//*[@title="{menu_title}"]')
                self.excute_js_click(menu_button)
        else:
            button_click = (By.CSS_SELECTOR, f'[ctrl_type="dsf.virtualscroll"] [title="{button_title}"]')
        self.excute_js_click(button_click)
        time.sleep(times)
        return self

    def locator_top_menu_click(self, menu_title: str, times: int = 2):
        """
        作者：李国彬
        判断正上方菜单当前是否显示，如果没有则尝试滚动菜单再点击元素
        :param menu_title: 需要判断是否展开的菜单名称，默认为空，则没有菜单需要判断是否展开
        :param times: 点击菜单后界面加载等待时长
        """
        menu = (By.CSS_SELECTOR, '.header-menu-item-box>div')  # 当前显示的菜单栏
        menu_names = [i.text for i in self.find_elms(menu) if i.text]
        click_menu = (By.XPATH, f'//*[@class="header-menu-item-box"]//*[text()="{menu_title}"]')
        if menu_title in menu_names:
            self.wait.until(self.EC.element_to_be_clickable(click_menu))
            time.sleep(1)
            self.excute_js_click(click_menu)
        else:
            more_menu = (By.CSS_SELECTOR, '.header-menu-bt:not([disabled])')  # 菜单栏的左右滚动按钮
            self.element_click(more_menu)
            time.sleep(1)  # 等待滚动菜单后的菜单元素加载
            self.excute_js_click(click_menu)
        time.sleep(times)  # 等待菜单栏对应页面加载
        return self

    def locator_tree_node_click(self, node_value: str, dialog_title: str = '', times: int = 1):
        """
        作者：李国彬
        树状结构元素定位，并点击对应节点
        :param dialog_title: dialog页签名称
        :param node_value: 节点名称
        :param times: 选择元素后默认等待加载时间
        """
        dialog_xpath = self._xpath_dialog(dialog_title=dialog_title)
        tree_node = (By.XPATH, f'{dialog_xpath}//*[@ctrl_type="dsf.tree" '
                               f'or @role="treeitem" or @ctrl_type="dsf.virtualscroll"]'
                               f'//*[contains(text(),"{node_value}")]')
        elements = self.find_elms(tree_node)
        # 判断元素是否匹配
        if len(elements) == 1:
            click_element = elements[0]
            time.sleep(2)
            click_element.click()
            time.sleep(times)  # 等待选中时元素重新加载
        else:
            for i in elements:
                if str(i.get_attribute("textContent")).strip() == node_value:
                    click_element = i
                    click_element.click()
                    time.sleep(times)  # 等待选中时元素重新加载
                    break
        return self

    def pagination_locator(self, dialog_title: str = ""):
        """多页签统计定位表达式"""
        dialog_css = self._css_dialog(dialog_title=dialog_title)
        tags_css = self._css_tags(dialog_title=dialog_title)
        locator = (By.CSS_SELECTOR, f'{dialog_css}{tags_css}.el-pagination__total')
        return locator

    def pagination_count(self, pattern=r'共 (.*?) 条', loc: tuple = (), dialog_title: str = "") -> int:
        """
        获取列表展示数据统计条数（正则匹配+json转换）
        :param pattern: 正则匹配表达式
        :param loc: 统计元素定位表达式
        :param dialog_title: 信息框的主题，默认为空
        """
        from common.explicit_wait import text_to_be_present_in_element_increment
        if not loc:
            loc = self.pagination_locator(dialog_title)
        pagination_text = self.wait.until(text_to_be_present_in_element_increment(loc, '条', self))
        return json.loads(_re(pattern, pagination_text))

    def alert_tip(self, keyword: str = '成功', loc: tuple = (By.CSS_SELECTOR, '.el-message__content'),
                  explicit_timeout: Union[int, float] = 10) -> str:
        """
        获取操作弹框提示文本（js去首尾空格）
        :param loc: 弹框文本元素定位表达式
        :param keyword: 弹框文本增量断言关键字
        :param explicit_timeout: 显示等待超时时间
        """
        from common.explicit_wait import text_to_be_present_in_element_increment
        return self.explicit_timer(explicit_timeout).until(text_to_be_present_in_element_increment(loc, keyword, self))

    def wait_listDataCount_searched(self, tr: tuple = (By.CSS_SELECTOR, '[class*=is-scrolling] tr'), count: int = 1,
                                    explicit_timeout: Union[int, float] = 10):
        """
        显示等待列表检索后显示指定条数据
        :param tr: 列表单行数据定位器
        :param count: 列表检索匹配行数
        :param explicit_timeout: 显示等待超时时间
        """
        from common.explicit_wait import list_searched_to_count
        self.explicit_timer(explicit_timeout, poll_frequency=0.25).until(list_searched_to_count(tr, count, self))

    def poll_search(self, search_btn: WebElement,
                    explicit_timeout: Union[int, float], poll_frequency: Union[int, float],
                    tr_loc: tuple = (By.CSS_SELECTOR, '[class*=is-scrolling] tr'),
                    count: int = 1
                    ):
        """
        轮询点击列表搜索按钮至显示指定条数据(用于定时触发数据流转场景)
        :param search_btn: 列表搜索按钮元素
        :param explicit_timeout: 检索总超时时间
        :param poll_frequency: 检索间隔时间
        :param tr_loc: 列表单行数据定位器
        :param count: 列表检索匹配行数
        """
        from common.explicit_wait import list_poll_search
        self.explicit_timer(explicit_timeout, poll_frequency).until(
            list_poll_search(search_btn, tr_loc, count, self, 2))

    def click_random_selected_ele(self, loc):
        """
        从同类元素等概率挑选一个元素点击
        :param loc: 同类元素定位表达式
        作者:杨德义
        """
        eles = self.driver.find_elements(*loc)
        selected_ele = randomTool.random_element_equal_rate(eles)
        self.excute_js_click_ele(selected_ele)

    def check_multiple(self, loc, start_count=2):
        """
        随机复选多条数据
        :param loc: 复选框定位表达式
        :param start_count: 复选起始数量
        :return: 返回复选数量
        作者:杨德义
        """
        total_checkboxes = self.driver.find_elements(*loc)
        to_check_count = random.randint(start_count, len(total_checkboxes))
        to_check_checkboxes = random.sample(total_checkboxes, k=to_check_count)
        for checkbox in to_check_checkboxes:
            self.excute_js_click_ele(checkbox)
            time.sleep(0.25)  # 列表复选框勾选后 dom 刷新-> 强制等待
        return to_check_count

    def locator_click_more_show(self, option_text: str = '100条/页', dialog_title: str = ''):
        """
        控制分页显示条数
        @param option_text:选择分页显示条数
        @param dialog_title:dialog页签名称
        @return:
        """
        xpath_dialog = self._xpath_dialog(dialog_title=dialog_title)
        xpath_tags = self._xpath_tags(dialog_title=dialog_title)
        import_input = (By.XPATH, f'{xpath_dialog}{xpath_tags}//*[@class="el-select el-select--mini"]//input')
        option = (By.XPATH, f'//div[@x-placement]//*[contains(text(),"{option_text}")]/parent::li')
        self.excute_js_click(import_input)
        self.wait_visibility_ele(option)
        self.excute_js_click(option)
        return self

    def sort_list_by_time_desc(self, field_name: str, dialog_title: str = ""):
        """
        按某一(时间相关)字段倒序排列显示页面列表
        :param field_name: 字段名称
        :param dialog_title: dialog页签名称
        """
        xpath_tags = self._xpath_tags(dialog_title=dialog_title)
        arrow_loc = (By.XPATH,
                     f'{xpath_tags}//*[@class="el-table__header-wrapper"]//*[contains(text(), "{field_name}")]//following-sibling::*[contains(@class, "caret-wrapper-proxy")]')
        arrow_ele = self.driver.find_element(*arrow_loc)
        time.sleep(0.25)  # python->js 多系统交互等待
        # 双击排序箭头按钮-倒序
        self.driver.execute_script('arguments[0].click();', arrow_ele)
        self.driver.execute_script('arguments[0].click();', arrow_ele)

    def chose_list_option(self, option_text):
        """
        点击下拉框选项
        :param option_text: 选项唯一文本
        """
        loc = (By.XPATH, f'//*[@class="el-scrollbar"]//*[contains(text(),"{option_text}")]')
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(*loc))

    def explicit_timer(self,
                       explicit_timeout: Union[int, float] = 6,
                       poll_frequency: Union[int, float] = 0.5,
                       ignored_exceptions: typing.Iterable[Exception] = None
                       ):
        """
        自定义显示等待定时器
        :param explicit_timeout: 显示等待超时时间
        :param poll_frequency: 轮询间隔时间
        :param ignored_exceptions: 忽略异常类型
        """
        return WebDriverWait(self.driver, explicit_timeout, poll_frequency, ignored_exceptions)

    @change_reset_implicit(1)
    def wait_presence_list_data(self, tab_num: int = 1,
                                loading_over: tuple = (),
                                explicit_timeout: Union[int, float] = 6,
                                poll_frequency: Union[int, float] = 0.5):
        """
        显示等待tab页数据加载完毕
        :param tab_num: 第几个tab页, 多页签时默认为1,单页签也为1
        :param explicit_timeout: 显示等待超时时间
        :param loading_over: 列表检索完毕定位器
        :param poll_frequency: 轮询时长
        """
        if not loading_over:
            loading_over = (By.XPATH, f'(//*[@class="el-loading-mask" and @style!=""])[{tab_num}]')
        wait = self.explicit_timer(explicit_timeout, poll_frequency)
        wait.until(self.EC.presence_of_element_located(loading_over))

    def trim_text(self, obj: Union[WebElement, tuple]) -> str:
        """js获取单个元素文本(去两端空格)"""
        if isinstance(obj, WebElement):
            return self.driver.execute_script('return arguments[0].textContent.trim()',
                                              obj)
        elif isinstance(obj, tuple):
            return self.driver.execute_script('return arguments[0].textContent.trim()',
                                              self.driver.find_element(*obj))

    def trim_texts(self, elements: list[WebElement]) -> typing.List[str]:
        """js获取多个元素文本(去两端空格)"""
        return self.driver.execute_script('return arguments[0].map((element) => {return element.textContent.trim()})',
                                          elements)

    def judge_window_alert_is_present(self):
        """判断是否有浏览器的弹窗出现"""
        try:
            alert = self.driver.switch_to.alert
            return alert
        except:
            return False

    @staticmethod
    def _close_windows():
        """关闭上传文件窗口"""
        if sys.platform == "win32":
            from pykeyboard import PyKeyboard
            time.sleep(2)
            pyk = PyKeyboard()
            pyk.tap_key(pyk.cancel_key, 1)

    def get_cookies(self):
        cookies = {}
        for i in self.driver.get_cookies():
            cookies[i['name']] = i['value']
        return cookies

    def add_cookies(self, cookies: dict):
        for name, value in cookies.items():
            self.driver.add_cookie({'name': name, 'value': value, 'domain': os.environ["host"].split(':')[0]})
