# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/2   15:20
============================
"""
import os
# 项目的根目录
import sys
import time
from time import sleep
from common import DOWNLOAD_PATH
from shutil import copyfile
import zipfile

base_dir = os.path.dirname(os.path.dirname(__file__))
# 公共类工具的目录路径
common_dir = os.path.join(base_dir, 'common')
# ini 配置文件的目录路径
config_dir = os.path.join(base_dir, 'config')
# api库的目录路径
api_dir = os.path.join(base_dir, 'api')
# 日志的目录路径
log_dir = os.path.join(base_dir, 'test_result/logs')
# 其他的目录路径
other_dir = os.path.join(base_dir, 'others')
# 研究生路径
graduate_dir = os.path.join(base_dir, 'graduate_student')
# 研究生数据路径
graduate_data_dir = os.path.join(graduate_dir, 'test_data_creation')
# 角色账户文件路径
role_account = os.path.join(config_dir, "smart_school_role_login.yaml")
# 研究生角色账户文件路径
gradu_role_account = os.path.join(config_dir, "graduate_stu_role_login.yaml")


def data_path(file_name: str = ''):
    """
    在测试代码中获取测试数据包下相同目录结构的文件,调用时在类外面使用
    :param file_name:文件名,如果不传值，则返回对应测试用例下数据的相对数量
    """
    file_path = sys.path[0]
    if "test_case_app" in file_path:
        directory_name = 'test_case_data_app'
        path = file_path.replace('test_case_app', directory_name)
    elif "test_case" in file_path:
        directory_name = 'test_case_data'
        path = file_path.replace('test_case', directory_name)
    else:
        path = file_path + "_data"
    new_path = os.path.join(path, file_name) if file_name else path
    return new_path


def wait_file_down_and_clean(file_name: str, times=10):
    # 判断文件是否下载成功且不为空，且删除下载文件，返回提示信息
    file_path = os.path.join(DOWNLOAD_PATH, file_name)
    while times > 0:
        sleep(1)
        if os.path.isfile(file_path):
            time.sleep(1)
            os.remove(file_path)
            return '下载文件成功'
        else:
            times -= 0.5
    return "下载文件失败"


def wait_file_down(file_name, times=10):
    # 判断文件是否下载成功且不为空，不删除下载文件，返回提示信息
    file_path = os.path.join(DOWNLOAD_PATH, file_name)
    while times > 0:
        sleep(0.5)
        if os.path.isfile(file_path):
            return file_path
        else:
            times -= 0.5
    return "下载文件失败"


def clean_download_file(file_path):
    """删除下载路径中的文件"""
    os.remove(os.path.join(DOWNLOAD_PATH, file_path))


def get_dir_file_num(dir_path=DOWNLOAD_PATH):
    """获取目录下的文件数量"""
    if not os.path.isdir(dir_path):
        raise FileNotFoundError(f'{dir_path}不是文件目录')
    return len(os.listdir(dir_path))


def get_download_path_all_file():
    """获取下载目录下的所有文件"""
    return os.listdir(DOWNLOAD_PATH)


def case_url(id_number: int):
    """返回测试用例连接地址"""
    url = f'http://117.184.59.230:18821/zentao/testcase-view-{id_number}-1.html'  # 禅道用例地址
    return url, '点我访问_用例链接地址'


def copy_file(file_path: str, copy_file_name: str, new_file_name: str):
    """根据file_path复制copy_file_name文件并命名为new_file_name"""
    file1 = os.path.join(file_path, copy_file_name)
    file2 = os.path.join(file_path, new_file_name)
    copyfile(file1, file2)
    return file2


def zip_file(file_path: str, zip_name: str, sub_files: list):
    """在file_path路径下生成zip文件zip_name，并将sub_files全部压缩进zip文件"""
    zip_file_path = os.path.join(file_path, zip_name)
    with zipfile.ZipFile(zip_file_path, 'w') as f:
        for i in sub_files:
            f.write(os.path.join(file_path, i), i)
    return zip_file_path
