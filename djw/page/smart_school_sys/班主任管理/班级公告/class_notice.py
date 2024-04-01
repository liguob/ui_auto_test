import time
import allure
from selenium.webdriver.common.by import By
from common.path_lib import *
from common.base_page import BasePage
from time import sleep
import re
from common.decorators import change_reset_implicit
from common.random_tool import randomTool


class ClassNotice(BasePage):
    table_name = (By.XPATH, '//div[@class="title"]/label')
    # 通知公告的菜单
    menu_inform_notice = (By.XPATH, '//span[text()="通知公告"]')

    # 通知公告新增或编辑弹窗的iframe
    frame_pop = (By.XPATH, '//div[@class="el-dialog__body"]/div/div/iframe')
    # 新增页面富文本的iframe
    frame_rtf = (By.XPATH, '//iframe[@id="ueditor_0"]')
    # 选择班级的iframe
    frame_class = (By.XPATH, '//div[@aria-label="请选择"]/div[2]/div/div/iframe')
    # 搜索框的input标签
    input_search = (By.XPATH, '//input[@placeholder="标题/发布人" and @handler="search"]')
    # 定位新增—>班次选择列表的搜索框
    input_search_pop = (By.XPATH, '//label[text()=" 班次列表 "]/ancestor::div[@class="ds-panel-header"]//input')
    # 新增页面的标题
    input_title = (By.XPATH, '//*[contains(text(), "标题")]/..//following-sibling::*//input')

    # 列表的表头—>标题
    col_title = (
        By.XPATH, '//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-0"]')
    # 列表的表头—>发布人
    col_person = (
        By.XPATH, '//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-4"]')
    # 列表第一行—>标题
    col_title1 = (By.XPATH,
                  '//tr[@row_index="0"]//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-0"]')
    # 列表第一行—>通知班次
    col_class1 = (By.XPATH,
                  '//tr[@row_index="0"]//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-1"]')
    # 列表第一行—>创建时间
    col_create_time1 = (By.XPATH,
                        '//tr[@row_index="0"]//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-2"]')
    # 列表第一行—>发布状态
    col_status1 = (By.XPATH,
                   '//tr[@row_index="0"]//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-3"]')
    # 列表第一行—>发布人
    col_person1 = (By.XPATH,
                   '//tr[@row_index="0"]//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-4"]')
    # 列表第一行—>发布时间
    col_publish_time1 = (By.XPATH,
                         '//tr[@row_index="0"]//div[@class="ds_control ellipsis ds_container no_padding datagrid-ndLjXuezBKoxhDxq-column-5"]')

    # 新增按钮
    btn_add = (By.XPATH, '//*[contains(text(), "班级公告管理")]/ancestor::*[@class="ds-panel-header"]//*[@title="新增"]')
    # 弹窗班次选择按钮
    btn_class_select = (By.XPATH, '//div[@class="ds-datachoice-input"]//i')
    # 弹窗文件上传按钮
    btn_upload = (By.XPATH, '//button[@handler="uploadMainBtn"]')
    # 弹框的保存按钮
    btn_pop_save = (By.XPATH, '//div[@handler="buttonBox"]/div/a[2]')
    # 弹框的发布按钮
    btn_pop_publish = (By.XPATH, '//div[@handler="buttonBox"]/div/a[1]')
    # 班级列表第一行的发布按钮
    btn_publish = (By.XPATH, '//tr[@row_index="0"]//a[@dsevent="publish"]')
    # 班级列表第一行的取消发布按钮
    btn_unpublish = (By.XPATH, '//tr[@row_index="0"]//a[@dsevent="unPublish"]/div')
    # 班级列表第一行的编辑按钮
    btn_edit = (By.XPATH,
                '//tr[@row_index="0"]//a[@dsevent="system_layer_open"]/i[@class="iconfont icon-bianji"]/following-sibling::div')
    # 班级列表第一行的阅读情况按钮
    btn_read_state1 = (By.XPATH,
                       '//tr[@row_index="0"]//a[@dsevent="system_layer_open"]/i[@class="iconfont icon-icon_wangye"]/following-sibling::div')
    # 班级列表第一行的删除按钮
    btn_delete = (By.XPATH,
                  '//tr[@row_index="0"]//a[@dsevent="system_datagrid_row_delete"]/i[@class="iconfont icon-shanchu"]/following-sibling::div')
    # 内容的文本框定位
    txt_content = (By.XPATH, '//body[@class="view"]/p')
    # 班级选择列表的确定按钮
    btn_sure = (By.XPATH, '//span[text()="确定"]/parent::a[@class="ds-button"]')
    # 共多少条数据的定位
    laypage_count = (By.XPATH, '//span[@class="layui-laypage-count"]')
    # 班次选择必填项的弹窗
    pop_in_class = (By.XPATH, '//div[@id="layui-layer3"]/div[@class="layui-layer-content"]')
    # 标题必填项的弹窗
    pop_in_title = (By.XPATH, '//div[@id="layui-layer4"]/div[@class="layui-layer-content"]')
    # 班次列表的第一个复选框
    btn_lay_class = (
        By.XPATH, '//div[@handler="datagrid_fixed_left"]//tr[@row_index="0"]//i[@class="layui-icon layui-icon-ok"]')
    # 确定删除按钮/提醒未读学员确定按钮
    btn_redelete = (By.XPATH, '//div[@type="dialog"]//div/a[@class="layui-layer-btn0"]')
    # 提醒未读学员按钮
    btn_remind = (By.XPATH, '//div[@handler="buttonsbar"]//a[@ds-event="remind"]/i')
    # 阅读情况页面的班级选择
    onlyread_class = (By.XPATH, '//div[@caption="bjxz"]/div/div')
    # 阅读情况页面的标题
    onlyread_title = (By.XPATH, '//div[@caption="bt"]/div/div')
    # 阅读情况页面的内容
    onlyread_content = (By.XPATH, '//div[@caption="nr"]/div/div')

    # 学员查看列表—>班级
    view_class = (By.XPATH, '//div[@caption="xycklb"]//tbody[@handler="tbody"]//tr/td[3]')
    # 学员查看列表—>学生姓名
    view_name = (By.XPATH, '//div[@caption="xycklb"]//tbody[@handler="tbody"]//tr/td[4]')
    # 学员查看列表—>组别
    view_group = (By.XPATH, '//div[@caption="xycklb"]//tbody[@handler="tbody"]//tr/td[6]')
    # 学员查看列表第五行—>平梦秋的查看时间
    view_time = (By.XPATH, '//div[@caption="xycklb"]//tbody[@handler="tbody"]//tr[@row-index="4"]/td[7]')
    # 学员查看页面的tbody标签
    view_tbody = (By.XPATH, '//tbody[@handler="tbody"]')
    # 列表第一行的标题
    td_title_row1 = (By.XPATH, '//div[@type="list"]//tr[@row_index="0"]//td[3]//div[@handler="readOnlyLabel"]')

    # 班级公告列表页面
    btn_read_condition1 = (By.XPATH, '(//div[@class="el-table__fixed-right"]//td[9]//a[@title="阅读情况"])[1]')  # 第一行的阅读情况
    btn_not_release1 = (By.XPATH, '(//div[@class="el-table__fixed-right"]//td[9]//a[@title="取消发布"])[1]')  # 第一行的取消发布
    btn_edit1 = (By.XPATH, '(//div[@class="el-table__fixed-right"]//td[9]//a[@title="编辑"])[1]')  # 第一行的编辑
    btn_release1 = (By.XPATH, '(//div[@class="el-table__fixed-right"]//td[9]//a[@title="发布"])[1]')  # 第一行的发布
    btn_delete1 = (By.XPATH, '(//div[@class="el-table__fixed-right"]//td[9]//a[@title="删除"])[1]')  # 第一行的删除
    tip_release = (By.XPATH, '//div[@role="alert"]/p')  # 发布成功/发布不成功的提示

    @property
    @allure.step('获取指定公告发布状态')
    def publish_status(self):
        status = (By.CSS_SELECTOR, '[class*=is-scrolling] .teas_jwgl_classnotice_managelistdb_status_text__value')
        return self.driver.find_element(*status).text

    @allure.step("标题关键字检索公告")
    def search_notice(self, title):
        input_search = (By.XPATH, '//*[contains(text(),"班级公告")]/ancestor::*[@class="ds-panel-header"]//input')
        self.clear_then_input(input_search, title+'\n')
        sleep(0.5)
        self.wait_presence_list_data(explicit_timeout=20)
        return self

    def is_all_class(self):
        """"
        新增通知公告时选择所有的当前班次和未开始班次
        （新增的功能已变更，点击新增跳转新标签）
        """
        self.element_click(self.btn_add)  # 点击新增按钮
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_pop)  # 进入弹窗的iframe
        self.element_click(self.btn_class_select)
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_class)  # 进入到班级列表的iframe
        sleep(1)  # 强制等待一秒
        self.count = self.find_elem(self.laypage_count).text
        res = re.findall("\d+", self.count)
        return res

    def is_must_fill(self):
        """"校验新增页面的必填项"""
        self.element_click(self.btn_add)  # 点击新增按钮
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_pop)  # 进入弹窗的iframe
        self.element_click(self.btn_pop_save)  # 点击保存按钮
        sleep(1)
        list = []
        list.append(self.find_elem(self.pop_in_class).text)  # 把班次选择弹窗的值添加至列表
        list.append(self.find_elem(self.pop_in_title).text)  # 把标题弹窗的值添加至列表
        return list

    def addpage_of_save(self, frame_name):
        """"校验新增页面的保存按钮"""

        self.element_click(self.btn_add)  # 点击新增按钮
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
        self.click_to_clickable_ele(self.btn_class_select)
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_class)  # 进入到班级列表的iframe
        self.input_send_keys(self.input_search_pop, "2021春季市管干部一班" + "\n")
        sleep(1)
        self.element_click(self.btn_lay_class)  # 点击第一行的复选框
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        self.element_click(self.btn_sure)
        self.switch_to_frame(self.frame_pop)  # 进入到新增页面的iframe
        self.input_send_keys(self.input_title, "20210420陈蓉发布的通知公告")
        self.element_click(self.btn_upload)
        self.upload2(str(photo_test1))  # 上传文件
        self.switch_to_frame(self.frame_rtf)  # 进入富文本的iframe
        self.find_elem(self.txt_content).send_keys("这是20210420通知公告的内容")
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        sleep(1)
        # self.switch_to_frame(self.frame_pop)   #进入新增页面的iframe
        self.element_click(self.btn_pop_save)
        sleep(1)
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(frame_name)
        list = []
        list.append(self.find_elem(self.col_status1).text)  # 第一条通知公告的发布状态添加值列表
        list.append(self.find_elem(self.btn_publish).text)  # 获取第一行通知公告发布按钮的文本值
        return list

    def addpage_of_release(self, frame_name):
        """"校验新增页面的发布按钮"""
        self.element_click(self.btn_add)  # 点击新增按钮
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
        self.click_to_clickable_ele(self.btn_class_select)
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_class)  # 进入到班级列表的iframe
        self.input_send_keys(self.input_search_pop, "2021春季市管干部一班" + "\n")
        sleep(1)
        self.element_click(self.btn_lay_class)  # 点击第一行的复选框
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        self.element_click(self.btn_sure)
        self.switch_to_frame(self.frame_pop)  # 进入到新增页面的iframe
        self.input_send_keys(self.input_title, "20210420陈蓉发布的通知公告:保存并发布")
        self.element_click(self.btn_upload)
        self.upload2(str(photo_test1))  # 上传文件
        self.switch_to_frame(self.frame_rtf)  # 进入富文本的iframe
        self.find_elem(self.txt_content).send_keys("这是20210420通知公告的内容：保存并发布")
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        sleep(1)
        # self.switch_to_frame(self.frame_pop)   #进入新增页面的iframe
        self.element_click(self.btn_pop_publish)  # 点击发布按钮
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(frame_name)
        sleep(2)
        list = []
        list.append(self.find_elem(self.col_status1).text)  # 第一条通知公告的发布状态添加值列表
        list.append(self.find_elem(self.btn_unpublish).text)  # 获取第一行通知公告取消发布按钮的文本值
        return list

    def publish_notice(self, clas, title):
        """在PC页面新增通知公告并发布"""
        self.element_click(self.btn_add)  # 点击新增按钮
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
        self.click_to_clickable_ele(self.btn_class_select)
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_class)  # 进入到班级列表的iframe
        self.input_send_keys(self.input_search_pop, clas + "\n")
        sleep(1)
        self.element_click(self.btn_lay_class)  # 点击第一行的复选框
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        self.element_click(self.btn_sure)
        self.switch_to_frame(self.frame_pop)  # 进入到新增页面的iframe
        self.input_send_keys(self.input_title, title)
        # self.element_click(self.btn_upload)
        # self.upload2(str(photo_test1))  # 上传文件
        # self.switch_to_frame(self.frame_rtf)  # 进入富文本的iframe
        # self.find_elem(self.txt_content).send_keys("这是20210420通知公告的内容：保存并发布")
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        sleep(1)
        self.switch_to_frame(self.frame_pop)  # 进入新增页面的iframe
        self.element_click(self.btn_pop_publish)  # 点击发布按钮

    def save_notice(self, clas, title):
        """在PC页面新增通知公告并保存"""
        self.element_click(self.btn_add)  # 点击新增按钮
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
        self.click_to_clickable_ele(self.btn_class_select)
        self.driver.switch_to.parent_frame()  # 切换到上一级iframe
        self.switch_to_frame(self.frame_class)  # 进入到班级列表的iframe
        self.input_send_keys(self.input_search_pop, clas + "\n")
        sleep(1)
        self.element_click(self.btn_lay_class)  # 点击第一行的复选框
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        self.element_click(self.btn_sure)
        self.switch_to_frame(self.frame_pop)  # 进入到新增页面的iframe
        self.input_send_keys(self.input_title, title)
        # self.element_click(self.btn_upload)
        # self.upload2(str(photo_test1))  # 上传文件
        # self.switch_to_frame(self.frame_rtf)  # 进入富文本的iframe
        # self.find_elem(self.txt_content).send_keys("这是20210420通知公告的内容：保存并发布")
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        sleep(1)
        self.switch_to_frame(self.frame_pop)  # 进入新增页面的iframe
        self.element_click(self.btn_pop_save)  # 点击保存按钮
        self.driver.switch_to.parent_frame()

    def get_list_detail(self):
        """"获取列表第一行元素的值并返回列表"""
        title = ("theme", "class", "create_time", "status", "teacher", "publish_time")
        value = self.publish_get_info(self.col_title1, self.col_class1, self.col_create_time1, self.col_status1,
                                      self.col_person1, self.col_publish_time1, title=title)
        list_value = [item[key] for item in value for key in item]
        return list_value

    def get_edit_detail(self):
        """"获取详情页面的表单元素文本值"""
        flag = self.find_elem(self.btn_read_state1).text
        if flag == '阅读情况':
            self.element_click(self.btn_read_state1)  # 点击阅读情况按钮
            self.driver.switch_to.parent_frame()  # 退出当前iframe
            self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
            title = ('class', "theme", "content")
            value = self.publish_get_info(self.onlyread_class, self.onlyread_title, self.onlyread_content, title=title)
            list_value = [item[key] for item in value for key in item]  # 将value转换为纯列表
        else:
            self.element_click(self.btn_publish)  # 点击发布按钮
            self.element_click(self.btn_read_state1)  # 点击阅读情况按钮
            self.driver.switch_to.parent_frame()  # 退出当前iframe
            self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
            title = ('class', "theme", "content")
            value = self.publish_get_info(self.onlyread_class, self.onlyread_title, self.onlyread_content, title=title)
            list_value = [item[key] for item in value for key in item]
        return list_value

    def check_student_list(self):
        flag = self.find_elem(self.btn_read_state1).text
        if flag == '阅读情况':
            self.element_click(self.btn_read_state1)  # 点击阅读情况按钮
            self.driver.switch_to.parent_frame()  # 退出当前iframe
            self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
            title = ('name',)
            value = self.publish_get_info(self.view_name, title=title)
            list_value = [item[key] for item in value for key in item]
        else:
            self.element_click(self.btn_publish)  # 点击发布按钮
            self.element_click(self.btn_read_state1)  # 点击阅读情况按钮
            self.driver.switch_to.parent_frame()  # 退出当前iframe
            self.switch_to_frame(self.frame_pop)  # 进入新增页面的的iframe
            title = ('class',)
            value = self.publish_get_info(self.view_name, title=title)
            list_value = [item[key] for item in value for key in item]
        return list_value

    def check_time(self, value, frame_name):
        self.switch_to_frame(frame_name)
        self.element_click(self.btn_read_state1)  # 点击阅读情况按钮
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        self.switch_to_frame(self.frame_pop)  # 进入阅读情况页面的的iframe
        tbody = self.find_elms(loc=self.view_tbody)[1]
        tr_list = tbody.find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            div_list = td_list[3].find_elements_by_xpath('.//div')  # 找出当前目录下的所有div标签
            if div_list[3].text == value:
                div_list1 = td_list[6].find_elements_by_xpath('.//div')
                return div_list1[3].text

    def remind_unread(self):
        """"点击提醒未读学员的按钮并获取列表第一行标题的文本值"""
        value = self.find_elem(self.td_title_row1).text
        self.element_click(self.btn_read_state1)  # 点击阅读情况按钮
        self.driver.switch_to.parent_frame()  # 退出当前iframe
        self.switch_to_frame(self.frame_pop)  # 进入阅读情况页面的的iframe
        self.element_click(self.btn_remind)
        self.element_click(self.btn_redelete)  # 点击提醒未读学员弹框的确定按钮
        return value

    def click_btn_publish_of_list(self, frame_name):
        """"点击列表的发布按钮并获取第一行通知公告的标题"""
        self.switch_to_frame(frame_name)
        value = self.find_elem(self.td_title_row1).text
        self.excute_js_click(self.btn_publish)
        return value

    def click_btn_delete_of_list(self, frame_name):
        """"获取第一行通知公告的标题并点击列表的删除按钮"""
        self.switch_to_frame(frame_name)
        value = self.find_elem(self.td_title_row1).text
        self.excute_js_click(self.btn_delete)
        self.excute_js_click(self.btn_redelete)
        return value

    def click_btn_unpublish_of_list(self, frame_name):
        """点击列表第一行的取消发布按钮并获取第一行通知公告的标题"""
        self.switch_to_frame(frame_name)
        self.excute_js_click(self.btn_unpublish)
        value = self.find_elem(self.td_title_row1).text
        return value

    # def a(self, value):
    #     tbody = self.find_elms(loc=self.view_tbody)[1]
    #     tr_list = tbody.find_elements_by_tag_name('tr')
    #     for tr in tr_list:
    #         td_list = tr.find_elements_by_tag_name('td')
    #         div_list = td_list[2].find_elements_by_xpath('.//div')
    #         if div_list[4].text == value:
    #             div_list1 = td_list[7].find_elements_by_xpath('.//div')
    #             return div_list1[3].text
    @allure.step("获取列表表头的文本值")
    def get_table_name_value(self):
        """获取列表表头的文本值"""
        value = self.find_elem(self.table_name).text
        return value

    @allure.step("进入到新增班级公告的标签")
    def into_class_notice_add_handle(self):
        self.excute_js_click_ele(self.btn_add)  # 点击新增按钮
        self.switch_to_handle()  # 跳转至新标签
        return self

    @allure.step("选择发送公告的班级")
    def choice_class_to_send_notice(self, class_name):
        input_search_pop = (By.XPATH, '//*[contains(text(),"班次列表")]/ancestor::*[@class="ds-panel-header"]//input')
        option = (By.XPATH, '(//div[@class="el-table__fixed"]//td[1]/div/label)[1]')
        choice_yes = (By.XPATH, '//label[contains(text(),"班次列表")]/ancestor::*[@class="el-dialog"]//*[contains(text(),"确定")]/parent::*')
        self.excute_js_click_ele(self.btn_class_select)
        time.sleep(1)
        self.clear_then_input(input_search_pop, class_name+'\n')
        time.sleep(1)
        self.locator_view_select(dialog_title="请选择班次", id_value=class_name)
        time.sleep(0.5)
        self.excute_js_click_ele(choice_yes)
        return self

    @allure.step("表单填写内容")
    def input_send_txt_content(self, value):
        """
        Author:hc
        表单填写内容
        """
        frame = (By.CSS_SELECTOR, 'iframe[id][src]')
        self.switch_to_frame(frame)
        text_area = (By.CSS_SELECTOR, 'body.view')
        self.clear_then_input(text_area, value)
        self.switch_to_frame_back()
        return self

    @allure.step("编辑班级公告表单")
    def edit_class_notice_form(self, class_name='', **kwargs):
        """
        Author:hc
        填写班级公告信息
        """
        info_dict = {"class_name": class_name, "title": randomTool.random_str(),
                     "txt_content": randomTool.random_str()}
        info_dict.update(kwargs)
        if info_dict["class_name"]:
            self.choice_class_to_send_notice(info_dict["class_name"])
        self.clear_then_input(self.input_title, info_dict["title"])
        self.input_send_txt_content(info_dict["txt_content"])
        return info_dict

    @allure.step('修改公告标题保存')
    def update_title(self, title):
        self.clear_then_input(self.input_title, title)
        self.click_class_notice_save()
        self.wait_browser_close_switch_latest()

    @allure.step('单个公告删除')
    def del_notice(self, title):
        self.locator_view_button(button_title="删除", id_value=title)
        # self.poll_click(self.btn_delete1)
        self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('批量删除公告')
    def batch_del_notice(self):
        available_checkbox = (By.CSS_SELECTOR, '[class*="is-scrolling"] [type=checkbox]:not([disabled])')
        del_count = self.check_multiple(available_checkbox, start_count=1)
        self.locator_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        return del_count

    @allure.step("获取成功提示")
    def get_add_class_notice_tip(self):
        """
        Author:hc
        获取创建公告表单的提示
        """
        tip_text = (By.XPATH, '//div[contains(@class,"el-message el-message--success")]/p')
        self.switch_to_handle(0)
        return self.trim_text(tip_text)

    @allure.step("获取失败提示")
    def get_add_fail_class_notice_tip(self):
        """
        Author:hc
        获取创建公告表单失败的提示
        """
        tip_text = (By.XPATH, '//div[@class="ds-error-text"]')
        return self.trim_text(tip_text)

    @allure.step("点击公告新增/编辑页保存按钮")
    def click_class_notice_save(self):
        btn_save = (By.CSS_SELECTOR, '.ds-page-foot [title=保存]')
        self.element_click(btn_save)
        return self

    @allure.step("点击公告新增/编辑页发布按钮")
    def click_class_notice_send(self):
        btn_send = (By.CSS_SELECTOR, '.ds-page-foot [title=发布]')
        self.element_click(btn_send)
        return self

    @allure.step("点击公告新增/编辑页关闭按钮")
    def click_class_notice_close(self):
        btn_close = (By.CSS_SELECTOR, '.ds-page-foot [title=关闭]')
        self.excute_js_click_ele(btn_close)
        return self

    @allure.step("新增班级公告-保存")
    def class_notice_save(self, class_name):
        info = self.edit_class_notice_form(class_name)
        self.click_class_notice_save()
        # tip = self.get_add_class_notice_tip()
        time.sleep(0.5)
        self.switch_to_handle(0)
        time.sleep(1)
        return info

    @allure.step('编辑公告')
    def edit_notice(self, title):
        self.locator_view_button(button_title="编辑", id_value=title)
        return self

    @allure.step("填写表单并发送")
    def class_notice_send(self, class_name):
        """
        Author:hc
        填写公告表单并发送
        """
        info = self.edit_class_notice_form(class_name)
        self.click_class_notice_send()
        time.sleep(0.5)
        self.switch_to_handle(0)
        time.sleep(1)
        return info

    @allure.step("获取班级公告信息")
    def get_class_notice_info(self):
        """
        Author:hc
        获取班级公告信息
        """
        time.sleep(0.5)
        title = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-none"]//td[3]')
        class_name = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-none"]//td[4]')
        create_time = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-none"]//td[5]')
        release_status = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-none"]//td[6]')
        releaser = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-none"]//td[7]')
        releaser_time = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-none"]//td[8]')
        tab_title = ("title", "class_name", "create_time", "release_status", "releaser", "releaser_time")
        value = self.publish_get_info(title, class_name, create_time, release_status, releaser, releaser_time,
                                      t=tab_title)
        return value

    @allure.step("点击公告列表的发布按钮")
    def click_release(self):
        self.excute_js_click_ele(self.btn_release1)
        return self.trim_text(self.tip_release)

    @allure.step("点击公告列表的取消发布按钮")
    def click_not_release(self):
        self.locator_view_button(button_title="取消发布", id_value='1')
        return self.trim_text(self.tip_release)

    @allure.step("获取操作发布/取消发布的提示")
    def get_release_or_not_release_tip(self):
        return self.trim_text(self.tip_release)

    @property
    @change_reset_implicit()
    @allure.step('获取班级公告列表检索表单结果条数')
    def table_searched_count(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        return len(self.driver.find_elements(*tr))
