# 导包
import app
import requests


# 创建接口类——coin模块
class CoinAPI:
    # 初始化
    def __init__(self):
        self.url_get_coins = app.BASE_URL + "/coins"
        self.url_broadcast_transaction = app.BASE_URL + "/coin/{}/broadcast"

    # 01.获取可用币种接口
    def get_coins(self):
        return requests.get(url=self.url_get_coins, headers=app.headers_data)

    # 02.广播已签名交易接口
    def broadcast_transaction(self, coin, txHex_data):
        url = self.url_broadcast_transaction.format(coin)
        return requests.post(url=url, json=txHex_data, headers=app.headers_data)