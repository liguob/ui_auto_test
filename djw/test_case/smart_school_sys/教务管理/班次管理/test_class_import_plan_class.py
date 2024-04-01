# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/5/20    15:44
============================
"""
from common.tools_packages import *

# 导入数据文件路径
from djw.test_base_cases.test_c_01_create_unit_admin import UnitFile

name_class_file = data_path('计划班次导入-姓名.xlsx')
num_class_file = data_path('计划班次导入-名额.xlsx')
import_check_file1 = data_path('计划班次导入-姓名必填校验.xlsx')
import_check_file2 = data_path('计划班次导入-名额必填校验.xlsx')
# 编辑班次数据
date_today = randomTool.random_now_time_calculate()  # 今天日期
date_today_behind2 = randomTool.random_now_time_calculate(days=2)


@allure.epic("李国彬")
@allure.feature("教务管理")
@allure.story("班次管理")
class TestImportClass1:

    def setup(self):
        """构建导入数据"""
        unit_name = DjwPd.read_base_data_excel(UnitFile)[0]['单位名称']
        self.file = DjwPd.read_all_sheet_func_save(num_class_file, replace_to='网报单位', replace_data=unit_name)
        self.class_name = DjwPd.read_excel(self.file, ignore_num=1)[0]['班次名额分配表2']

    @allure.title("计划班次-导入名额表,删除计划班次")
    def test_import_plan_by_num(self, go_class_manage):
        """导入班次数据，删除后查询，获取条数"""
        step0 = go_class_manage.switch_to_plan_class().import_plan_cls(self.file)
        # 获取删除后的班次条数
        step0.search_class(self.class_name).del_class(self.class_name)
        num = step0.locator_view_num()
        assert num == 0

    @allure.title("计划班次-导入名额表，编辑计划班次")
    def test_edit_plan_class2(self, go_class_manage):
        data = {
            "班次分类": "干部教育",
            "学年": "2022年",
            "培训开始时间": date_today_behind2,
            "培训结束时间": date_today_behind2,
            "换人截止时间": date_today,
            "培训形式": "线下班",
            "学期": "秋季",
            "网报形式": "无需网报"
        }
        edit_name = data["班次名称"] = '修改' + self.class_name
        # 导入计划班次并修改计划班次为未开始班次
        step0 = go_class_manage.switch_to_plan_class().import_plan_cls(self.file). \
            edit_plan_class(self.class_name, data).switch_feature_class().search_class(edit_name)
        num = step0.search_class(edit_name).locator_view_num()
        assert num == 1


@allure.epic("李国彬")
@allure.feature("教务管理")
@allure.story("班次管理")
class TestImportClass2:

    def setup(self):
        """构建导入数据"""
        unit_name = DjwPd.read_base_data_excel(UnitFile)[0]['单位名称']
        self.file = DjwPd.read_all_sheet_func_save(name_class_file, replace_to='网报单位', replace_data=unit_name)
        self.class_name = list(DjwPd.read_excel(self.file, ignore_num=2)[0].keys())[1]

    @allure.title("计划班次-导入姓名表,删除计划班次")
    def test_import_plan_by_name(self, go_class_manage):
        """导入班次数据，删除后查询，获取条数"""
        step0 = go_class_manage.switch_to_plan_class().import_plan_cls(self.file)
        # 获取删除后的班次条数
        step0.search_class(self.class_name).del_class(self.class_name)
        num = step0.locator_view_num()
        assert num == 0

    @allure.title("计划班次-导入姓名表，编辑计划班次")
    def test_edit_plan_class1(self, go_class_manage):
        data = {
            "班次分类": "干部教育",
            "学年": "2022年",
            "培训开始时间": date_today_behind2,
            "培训结束时间": date_today_behind2,
            "换人截止时间": date_today,
            "培训形式": "线下班",
            "学期": "秋季",
            "网报形式": "无需网报"
        }
        edit_name = data["班次名称"] = '修改' + self.class_name  # 班次名称（导入的班次名称+带时间戳）
        # 导入计划班次并修改计划班次为未开始班次
        step0 = go_class_manage.switch_to_plan_class().import_plan_cls(self.file). \
            edit_plan_class(self.class_name, data).switch_feature_class().search_class(edit_name)
        num = step0.search_class(edit_name).locator_view_num()
        assert num == 1


@allure.epic("李国彬")
@allure.feature("教务管理")
@allure.story("班次管理")
class TestImportClass3:

    def setup_class(self):
        unit_name = DjwPd.read_base_data_excel(UnitFile)[0]['单位名称']
        self.file_name = DjwPd.read_all_sheet_func_save(import_check_file1, replace_to='网报单位', replace_data=unit_name)
        self.file_num = import_check_file2

    @allure.title('带姓名计划班次导入必填校验')
    def test_import_plan_class_check1(self, go_class_manage):
        info = go_class_manage.switch_to_plan_class().import_plan_cls_check(self.file_name)
        assert '班次名称不能为空' == info

    @allure.title('名额分配计划班次导入网报单位匹配校验')
    def test_import_plan_class_check2(self, go_class_manage):
        info = go_class_manage.switch_to_plan_class().import_plan_unit_check(self.file_num)
        assert 'asdaf班次网报单1位as找不到对应的单位' == info
