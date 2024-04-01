"""
保留测试根目录、基本数据文件目录, 具体使用文件路径引用拼接
"""
from pathlib import Path

current_path = Path(__file__)

# 根目录
ROOT_DIR = current_path.parents[1]
# 通用静态资源文件目录
STATIC_DIR = ROOT_DIR/'static'

# 大教务产品目录
DJW_DIR = ROOT_DIR/'djw'
# 智慧校园基本数据文件目录
DJW_CREATE_DIR = DJW_DIR/'test_base_cases_data'
# 智慧校园 web 端测试目录
DJW_TEST_DIR = DJW_DIR/'test_case'/'smart_school_sys'
# 智慧校园 app 端测试目录
DJW_TEST_APP_DIR = DJW_DIR/'test_case_app'/'smart_school_sys'

# # 大教务产品 WEB 测试用例数据存放目录
# DJW_CASEDATA_DIR = DJW_DIR/'test_case_data'
#
# # 研究生产品目录
# GRADUATE_STUDENT_DIR = ROOT_DIR/'graduate_student'
# # 研究生 WEB 测试用例数据存放目录
# GRADUATE_DATA_DIR = GRADUATE_STUDENT_DIR/'test_data_creation'
# # 研究生 WEB 测试造数用例数据存放目录
# GRADUATE_Creation_DATA_DIR = GRADUATE_STUDENT_DIR/'test_data_creation_data'
#
# # 测试用照片路径
# word_test = DJW_CASEDATA_DIR/'smart_school_sys'/'PC学员端'/'首页'/'作业提交'/'测试测试.docx'
# photo_test = GRADUATE_STUDENT_DIR/'test_case_data'/'photo_test.png'
# photo_test1 = DJW_CASEDATA_DIR/'smart_school_sys'/'photo_test1.jpg'

if __name__ == '__main__':
    ...
