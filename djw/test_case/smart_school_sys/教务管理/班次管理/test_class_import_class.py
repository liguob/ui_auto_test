# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/5/26    13:35
============================
"""
from common.tools_packages import *

# 导入数据文件路径
import_file = data_path('班次导入数据.xls')
# 导入班次必填校验
import_file_check1 = data_path('班次导入必填校验数据.xls')
# 导入班次数据格式校验
import_file_check2 = data_path('班次导入数据格式校验.xls')


@allure.epic("李国彬")
@allure.feature("教务管理")
@allure.story("班次管理")
class TestImportClass:

    @allure.title("导入班次-导出班次")
    def test_import_class(self, go_class_manage):
        # 导入班次信息后查询班次并获取导入的班次条数
        file = DjwPd.read_excel_func_save(import_file)
        class_names = [i['班次名称'] for i in DjwPd.read_excel(file)]
        step0 = go_class_manage.import_class(file)
        num1 = step0.search_class(class_names[0]).locator_view_num()
        assert num1 == 1
        num2 = step0.switch_feature_class().search_class(class_names[1]).locator_view_num()
        assert num2 == 1
        num3 = step0.switch_history_class().search_class(class_names[2]).locator_view_num()
        assert num3 == 1
        # 导出班次
        assert step0.export_class() == '下载文件成功'

    @allure.title("班次导入必填校验")
    def test_import_class_check(self, go_class_manage):
        info = go_class_manage.import_class_check(import_file_check1)
        assert info == ['该项必须填写', '该项必须填写', '该项必须填写', '该项必须填写', '培训日期必填']

    @allure.title("班次导入数据格式校验")
    def test_import_class_check2(self, go_class_manage):
        info = go_class_manage.import_class_check(import_file_check2)
        assert info == ['该项必须填写', '该项必须填写', '该项必须填写', '该项必须填写', '培训日期必填', '该项必须填写数字']
