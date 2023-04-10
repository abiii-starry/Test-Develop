# 导包
import unittest
import json
import app
from api.coin import CoinAPI
from utils import common_assert
from tools.logger import Logger
from parameterized import parameterized

# 构建测试数据
def build_data():
    # 指定文件路径
    # json_file = "../data/token_name.json"
    json_file = app.BASE_DIR + "/data/broadcast_transaction.json"
    # 打开json文件
    test_data = []
    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            coin = case_data.get("coin")
            txHex_data = case_data.get("txHex_data")
            test_data.append((coin, txHex_data))
            print("test_data = {}".format((coin, txHex_data)))
    return test_data

# 创建测试类
class TestCoin(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.coin_api = CoinAPI()

    # 01.获取可用币种信息——测试用例设计
    def test02_get_coins(self):
        # 获取响应结果
        response = self.coin_api.get_coins()
        print(response.json())
        # 写入csv文件
        Logger.log(response.url, response.elapsed.total_seconds() * 1000)
        # 断言
        common_assert(self, response)    # 直接使用公共断言方法的默认值即可


    @parameterized.expand(build_data)
    # 02.广播已签名交易——测试用例设计
    def test02_broadcast_transaction(self, coin, txHex_data):
        # 获取响应结果
        response = self.coin_api.broadcast_transaction(coin, txHex_data)
        print(response.json())
        # 写入csv文件
        Logger.log(response.url, response.elapsed.total_seconds() * 1000)
        # 断言
        # common_assert(self, response)   # 不适用公共断言方法的默认值
        self.assertEqual(200, response.status_code)
        self.assertEqual("ok", response.json().get("status"))
        self.assertEqual(20000, response.json().get("code"))

