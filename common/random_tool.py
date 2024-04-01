# encoding=utf-8
import datetime
import os
import random

from faker.providers import BaseProvider

from common.file_path import common_dir
from common.time_calculate import date_calculate
from common.yml import read_yaml

major_bank_path = os.path.join(common_dir, '../config/major_bank.yaml')


def random_phone():
    """随机手机号"""
    head = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
            "155", "156", "157", "158", "159", "186", "187", "188"]
    phone = random.choice(head) + ''.join([random.choice('0123456789') for i in range(8)])
    return phone


def random_subject():
    """随机学科"""
    sub = list(read_yaml(major_bank_path)['major'].keys())
    return random.choice(sub)


def random_major(sub_name=''):
    """随机专业"""
    major = read_yaml(major_bank_path)['major']
    sub = random.choice(['哲学', '经济学', '法学', '民族学', '教育学', '文学', '历史学', '理学', '工学', '农学', '医学', '军事学', '管理学'])
    return random.choice(major[sub_name]) if sub_name else random.choice(major[sub]) + randomTool.random_range_str(3, 3)


def random_nation():
    """随机民族"""
    nation = ['汉族', '壮族', '回族', '满族', '维吾尔族', '苗族', '彝族', '土家族', '藏族', '蒙古族', '侗族', '布依族', '瑶族',
              '白族', '朝鲜族', '哈尼族', '黎族', '哈萨克族', '傣族', '畲族', '傈僳族', '东乡族', '仡佬族', '拉祜族', '佤族',
              '水族', '纳西族', '羌族', '土族', '仫佬族', '锡伯族', '柯尔克孜族', '景颇族', '达斡尔族', '撒拉族', '布朗族',
              '毛南族', '塔吉克族', '普米族', '阿昌族', '怒族', '鄂温克族', '京族', '基诺族', '德昂族', '保安族', '俄罗斯族',
              '裕固族', '乌孜别克族', '门巴族', '鄂伦春族', '独龙族', '赫哲族', '高山族', '珞巴族', '塔塔尔族', '其他']
    return random.choice(nation)


def random_name():
    """
    随机2-4字名字
    """
    family_name = ["李", "王", "张", "刘", "陈", "杨", "赵", "黄", "周", "吴", "徐", "孙", "胡", "朱", "高",
                   "林", "何", "郭", "马", "罗", "梁", "宋", "郑", "谢", "韩", "唐", "冯", "于", "董", "萧",
                   "程", "曹", "袁", "邓", "许", "傅", "沈", "曾", "彭", "吕", "苏", "卢", "蒋", "蔡", "贾",
                   "丁", "魏", "薛", "叶", "阎", "余", "潘", "杜", "戴", "夏", "钟", "汪", "田", "任", "姜",
                   "范", "方", "石", "姚", "谭", "廖", "邹", "熊", "金", "陆", "郝", "孔", "白", "崔", "康",
                   "毛", "邱", "秦", "江", "史", "顾", "侯", "邵", "孟", "龙", "万", "段", "漕", "钱", "汤",
                   "尹", "黎", "易", "常", "武", "乔", "贺", "赖", "龚", "文"]
    last_name = ["言", "玉", "意", "泽", "彦", "轩", "景", "正", "程", "诚", "宇", "澄", "安", "青", "泽", "轩", "旭", "恒",
                 "思", "宇", "嘉", "宏", "皓", "成", "宇", "轩", "玮", "桦", "宇", "达", "韵", "磊", "泽", "博", "昌", "信",
                 "彤", "逸", "柏", "新", "劲", "鸿", "文", "恩", "远", "翰", "圣", "哲", "家", "林", "景", "行", "律", "本",
                 "乐", "康", "昊", "宇", "麦", "冬", "景", "武", "茂", "才", "军", "林", "茂", "飞", "昊", "明", "天", "伦",
                 "峰", "志", "辰", "亦", "佳", "彤", "自", "怡", "颖", "宸", "雅", "微", "羽", "馨", "思", "纾", "欣", "元",
                 "凡", "晴", "玥", "宁", "佳", "蕾", "桑", "妍", "萱", "宛", "欣", "灵", "烟", "文", "柏", "艺", "以", "如",
                 "雪", "璐", "言", "青", "安", "昕", "淑", "雅", "颖", "云", "艺", "忻", "梓", "江", "丽", "梦", "雪", "沁",
                 "思", "羽", "羽", "雅", "访", "烟", "萱", "忆", "慧", "娅", "茹", "嘉", "幻", "辰", "妍", "雨", "蕊", "欣",
                 "芸", "亦"]
    name = random.choice(family_name) + ''.join([random.choice(last_name) for i in range(random.randint(1, 3))])
    return name


def random_company():
    """
    随机四川省内公司名字
    """
    area_list = ["成都市", "广元市", "绵阳市", "德阳市", "南充市", "广安市", "遂宁市", "内江市", "乐山市", "自贡市", "泸州市", "宜宾市",
                 "攀枝花市", "巴中市", "达州市", "资阳市", "眉山市", "雅安市", "崇州市", "邛崃市", "都江堰市", "彭州市", "江油市", "什邡市",
                 "广汉市", "绵竹市", "阆中市", "华蓥市", "峨眉山市", "万源市", "简阳市", "西昌市"]
    name_list = ["言", "玉", "意", "泽", "彦", "轩", "景", "正", "程", "诚", "宇", "澄", "安", "青", "泽", "轩", "旭", "恒",
                 "思", "宇", "嘉", "宏", "皓", "成", "宇", "轩", "玮", "桦", "宇", "达", "韵", "磊", "泽", "博", "昌", "信",
                 "彤", "逸", "柏", "新", "劲", "鸿", "文", "恩", "远", "翰", "圣", "哲", "家", "林", "景", "行", "律", "本",
                 "乐", "康", "昊", "宇", "麦", "冬", "景", "武", "茂", "才", "军", "林", "茂", "飞", "昊", "明", "天", "伦",
                 "峰", "志", "辰", "亦", "佳", "彤", "自", "怡", "颖", "宸", "雅", "微", "羽", "馨", "思", "纾", "欣", "元",
                 "凡", "晴", "玥", "宁", "佳", "蕾", "桑", "妍", "萱", "宛", "欣", "灵", "烟", "文", "柏", "艺", "以", "如",
                 "雪", "璐", "言", "青", "安", "昕", "淑", "雅", "颖", "云", "艺", "忻", "梓", "江", "丽", "梦", "雪", "沁",
                 "思", "羽", "羽", "雅", "访", "烟", "萱", "忆", "慧", "娅", "茹", "嘉", "幻", "辰", "妍", "雨", "蕊", "欣",
                 "芸", "亦"]
    company_name = random.choice(area_list) + ''.join([name_list[i] for i in range(random.randint(2, 5))]) + '有限公司'
    return company_name


def random_job():
    """
    随机工作职务
    """
    job_name_list = ["总经理", "副总经理", "人力资源总监", "人力资源总监", "财务总监", "营销总监", "市场总监", "销售总监",
                     "生产总监", "运营总监", "技术总监", "总经理助理", "人力资源经理", "人力资源助理", "人力资源专员", "招聘主管",
                     "员工培训与发展主管", "培训师", "培训专员", "绩效考核主管", "薪资福利主管", "薪酬分析师",
                     "人力资源信息系统经理", "员工记录经理", "财务经理", "财务助理", "预算主管", "财务成本控制主管", "应收账款主管",
                     "会计主管", "资金主管", "投资主管", "融资主管", "财务分析师", "预算专员"]
    job_name = random.choice(job_name_list)
    return job_name


def random_department():
    """
    随机工作部门
    """
    department_name_list = ["总经理办公室", "人力资源部", "财务部", "生产技术部", "计划营销部", "安全监察部", "工会办公室", "保卫部",
                            "后勤部"]
    department_name = random.choice(department_name_list)
    return department_name


class RandomData:
    def __init__(self):
        from faker import Faker
        self.fake = Faker(locale='zh_CN')
        self.base_provider = BaseProvider(Faker())

    def car_num(self):
        """ 随机车牌号 """
        provinces = (
            "京", "沪", "浙", "苏", "粤", "鲁", "晋", "冀",
            "豫", "川", "渝", "辽", "吉", "黑", "皖", "鄂",
            "津", "贵", "云", "桂", "琼", "青", "新", "藏",
            "蒙", "宁", "甘", "陕", "闽", "赣", "湘"
        )

        num = (
            "A", "B", "C", "D", "E", "F", "G", "H",
            "J", "K", "L", "M", "N", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", "Y", "Z",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
        )
        plate = "{0}{1}{2}".format(self.base_provider.random_element(provinces),
                                   self.base_provider.random_uppercase_letter(),
                                   "".join(self.base_provider.random_choices(elements=num, length=5))
                                   )
        return plate

    def random_credit_card_number(self):
        """随机银行卡号"""
        return self.fake.credit_card_number(card_type=None)

    def random_credit_card_provider(self):
        """随机银行卡开户行"""
        return self.fake.credit_card_provider(card_type=None)

    def random_phone(self):
        """随机手机号"""
        return self.fake.phone_number()

    def random_num(self):
        """1-9随机数字"""
        return self.fake.random_digit_not_null()

    def random_range_number(self, min_num: int = 0, max_num: int = 9999):
        """随机数字,默认0~9999"""
        return self.fake.random_int(min=min_num, max=max_num)

    def random_name(self):
        """随机名字"""
        return self.fake.name()

    def random_name_long(self):
        """随机名字_带2个字符串，减少重名概率"""
        return self.fake.name() + self.random_range_str(2, 2)

    def random_idcard(self, min_age=18, max_age=60):
        """随机身份证号"""
        return self.fake.ssn(min_age, max_age)

    def random_birthdate(self, **kwargs):
        """
        随机出生日期：yyyy-mm-dd
        :param idcard:传入身份证则指定身份证日期输出
        """
        if 'idcard' in kwargs:
            idcard = kwargs['idcard']
        else:
            idcard = randomTool.random_idcard()
        return '{0}-{1}-{2}'.format(idcard[6:10], idcard[10:12], idcard[12:14])

    def random_company(self):
        """随机公司名"""
        company = self.fake.city() + self.fake.company()
        return company

    def random_job(self):
        """随机工作职务"""
        return self.fake.job()

    def random_province(self):
        """随机城市"""
        return self.fake.province()

    def random_address(self):
        """随机地址"""
        return self.fake.address()

    def random_email(self):
        """随机邮箱"""
        return self.fake.email()

    def random_range_str(self, min_num: int = 4, max_num: int = 8):
        """生成指定长度范围内的随机字符串"""
        return self.fake.pystr(min_chars=min_num, max_chars=max_num)

    def random_lower_str(self, min_num: int = 8):
        """生成指定长度的小写字母字符串"""
        i = [random.choice([chr(i) for i in range(97, 123)]) for i in range(min_num)]
        return "".join(i)

    def random_str(self):
        """随机一段话"""
        return self.fake.sentence()

    def random_pystr(self):
        """随机字符"""
        return self.fake.pystr()

    def random_date(self):
        """随机日期"""
        return self.fake.date()

    def random_date_between(self, start_date="-30y", end_date="today"):
        """随机范围日期"""
        return self.fake.date_between(start_date, end_date)

    def random_date_time_between(self, start_date="-30y", end_date="now"):
        """随机范围日期+时间"""
        return self.fake.date_time_between(start_date, end_date)

    def random_texts(self):
        return self.fake.text()

    def random_password(self, length: int = 6, digits: bool = True):
        return self.fake.password(digits=digits, length=length, lower_case=True, special_chars=False, upper_case=False)

    @property
    def random_number(self):
        """随机数字"""
        return self.fake.random_number()

    @property
    def random_city_name(self):
        """随机城市名（不带市）"""
        return self.fake.city_name()

    @property
    def random_street_address(self):
        """随机街道地址"""
        return self.fake.street_address()

    @property
    def random_postcode(self):
        """随机邮编"""
        return self.fake.postcode()

    @property
    def random_bankcard(self):
        """随机信用卡号"""
        return self.fake.credit_card_number()

    @property
    def random_date_time(self):
        """随机日期+时间"""
        return self.fake.date_time()

    @property
    def random_time(self):
        """随机时间"""
        return self.fake.time()

    @property
    def random_academy(self):
        """随机党校学区"""
        return self.random_city_name + '市委党校'

    @property
    def random_tool(self):
        """随机个人档案"""
        return self.fake.pyiterable()

    @property
    def current_date(self):
        """当前日期"""
        return self.random_date_between('today', 'today')

    @staticmethod
    def get_pinyin(name, splitter='', convert='lower'):
        """
        获取中文的拼音
        :params name:
        :params splitter:间隔符
        :params convert:lower/upper/capitalize 小写/大写/首字母大写
        """
        from xpinyin import Pinyin
        return Pinyin().get_pinyin(name, splitter=splitter, convert=convert)

    @staticmethod
    def week_date(date=''):
        """指定日期所在的周(默认当前时间所在的周)"""
        import calendar
        if date:
            day = datetime.datetime.strptime(date, '%Y-%m-%d')
        else:
            day = datetime.datetime.now()
        day_week = day.weekday()
        sunday = calendar.SUNDAY
        sub = sunday - day_week
        Sunday = day + datetime.timedelta(days=sub)
        Monday = day - datetime.timedelta(days=6 - sub)
        return {'week': day.strftime('%W'), 'sdate': datetime.datetime.strftime(Monday, '%Y-%m-%d'),
                'edate': datetime.datetime.strftime(Sunday, '%Y-%m-%d')}

    @staticmethod
    def date_(date):
        """脱敏身份证"""
        value = date.split('-')
        if len(value[1]) == 1:
            value[1] = '0' + value[1]
        return '-'.join(value)

    @staticmethod
    def psw_md5(password):
        """md5*2加密后的密码"""
        import hashlib
        md5 = hashlib.md5(password.encode()).hexdigest()
        return hashlib.md5(md5.encode()).hexdigest()

    @staticmethod
    def hid_idcard(idcard):
        """脱敏身份证"""
        return idcard.replace(idcard[3:15], '************')

    @staticmethod
    def random_nation():
        """随机民族"""
        nations = ['汉族', '壮族', '满族', '回族', '苗族', '维吾尔族', '土家族', '彝族', '蒙古族', '藏族', '布依族', '侗族',
                   '瑶族', '朝鲜族', '白族', '哈尼族', '哈萨克族', '黎族', '傣族', '畲族', '傈僳族', '仡佬族', '东乡族',
                   '拉祜族', '水族', '佤族', '纳西族', '羌族', '土族', '仫佬族', '其他', '锡伯族', '柯尔克孜族', '达斡尔族', '景颇族',
                   '毛南族', '撒拉族', '布朗族', '塔吉克族', '阿昌族', '普米族', '鄂温克族', '怒族', '京族', '基诺族', '保安族', '俄罗斯族',
                   '裕固族', '乌孜别克族', '门巴族', '鄂伦春族', '独龙族', '塔塔尔族', '赫哲族', '高山族', '珞巴族', '外国血统', '德昂族']
        return random.choice(nations)

    @staticmethod
    def random_politics():
        """随机政治面貌"""
        politics = ['中国共产党党员', '中国共产党预备党员', '中国共产主义青年团团员', '中国国民党革命委员会会员', '中国民主同盟盟员',
                    '中国民主建国会会员', '中国民主促进会会员', '中国民工民主党党员', '中国致公党党员', '九三学社社员',
                    '台湾民主自治同盟盟员', '无党派民主人士', '群众']
        return random.choice(politics)

    @staticmethod
    def random_qualification():
        """随机学历"""
        qualifications = ['初中', '中技', '中专', '高中', '大专', '大学', '硕士研究生', '博士研究生']
        return random.choice(qualifications)

    @staticmethod
    def random_randint(n: int, m: int):
        return random.randint(n, m)

    @staticmethod
    def random_element_equal_rate(sequence):
        """
        :param sequence:序列
        从序列中等概率挑选一个元素
        :return:序列元素
        """
        cum_weights = [i for i in range(1, len(sequence) + 1)]
        return random.choices(sequence, cum_weights=cum_weights, k=1)[0]

    @staticmethod
    def random_choice(values: list):
        """从列表值中选择1个"""
        return random.choice(values)

    @staticmethod
    def random_now_time_calculate(time_format="%Y-%m-%d", days=0, hours=0, minutes=0, seconds=0):
        """
        根据当前时间戳计算时间，返回指定的时间格式
        :param days: 与当前时间相差的日期，正数则相加，负数相减
        :param time_format: 指定输出的时间格式，如：%Y-%m-%d %H:%M:%S 2022-01-02 12:12:12
        :param hours: 与输入时间相差的小时，正数则相加，负数相减
        :param minutes: 与输入时间相差的分钟数，正数则相加，负数相减
        :param seconds: 与输入时间相差的秒数，正数则相加，负数相减
        """
        now_time = datetime.datetime.now()
        return date_calculate(input_time=now_time, time_format=time_format, days=days, hours=hours, minutes=minutes,
                              seconds=seconds)

    @staticmethod
    def random_str_join(rand_str, range_start=5, range_end=5):
        return rand_str + randomTool.random_range_str(range_start, range_end)


randomTool = RandomData()
if __name__ == '__main__':
    # print(randomTool.random_name(), randomTool.random_idcard(), randomTool.random_phone())
    # print(randomTool.psw_md5('111111'))

    print(randomTool.random_lower_str())
