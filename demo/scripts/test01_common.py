# 导包
import unittest
import json
import app
from api.common import CommonAPI
from utils import common_assert
from parameterized import parameterized
from tools.logger import Logger
from PIL import Image
from io import BytesIO

# 构建测试数据
def build_data():
    # 指定文件路径
    # json_file = "../data/token_name.json"
    json_file = app.BASE_DIR + "/data/token_name.json"
    # 打开json文件
    test_data = []
    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            token_name = case_data.get("token_name")
            test_data.append((token_name))
            print("test_data = {}".format((token_name)))
    return test_data

# 创建测试类
class TestCommon(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.common_api = CommonAPI()

    # 01.获取app当前版本信息——测试用例设计
    def test01_get_version(self):
        # 获取响应结果
        response = self.common_api.get_version()
        print(response.json())
        # 写入csv文件
        Logger.log(response.url, response.elapsed.total_seconds() * 1000)
        # 断言
        common_assert(self, response)    # 直接使用公共断言方法的默认值即可

    # 02.获取钱包可用apps——测试用例设计
    def test01_get_apps(self):
        # 获取响应结果
        response = self.common_api.get_apps()
        print(response.json())
        # 写入csv文件
        Logger.log(response.url, response.elapsed.total_seconds() * 1000)
        # 断言
        common_assert(self, response)   # 直接使用公共断言方法的默认值即可

    @parameterized.expand(build_data)
    # 03.获取token图标——测试用例设计
    def test01_get_token_icon(self, token_name):
        # 获取响应结果
        response = self.common_api.get_token_icon(token_name)

        # # 将响应内容转换为Image对象
        # img = Image.open(BytesIO(response.content))
        # # 打印图片到Python控制台
        # img.show()

        # 写入csv文件
        Logger.log(response.url, response.elapsed.total_seconds() * 1000)
        # 断言
        # common_assert(self, response)  # 因为该接口响应的不是json数据，所以不能直接使用公共断言方法的默认值
        self.assertEqual(200, response.status_code)

