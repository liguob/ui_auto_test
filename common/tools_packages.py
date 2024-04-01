# coding: utf-8
"""
============================
# Time      ：2022/2/15 17:30
# Author    ：李国彬
============================
"""
import allure
import pytest
import time
import os
import sys
import pytest_check
import datetime
from common.base_page import BasePage
from common.base_page_app import BasePageApp
from common.file_path import *
from selenium.webdriver.common.by import By

from common.manage.manage_driver import CookieManager
from common.random_tool import randomTool
from common.excel_tool import DjwPd, PlatFormPd, ExamPd
from common.yml import read_yaml
from common import *

"""测试用例-页面相关基础工具包"""
