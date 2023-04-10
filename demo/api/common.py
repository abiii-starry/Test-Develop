# 导包
import app
import requests


# 创建接口类——common模块
class CommonAPI:
    # 初始化
    def __init__(self):
        self.url_get_version = app.BASE_URL + "/app/version"
        self.url_get_apps = app.BASE_URL + "/apps"
        self.url_get_token_icon = app.BASE_URL + "/icon/{}"

    # 01.获取app的当前版本信息接口
    def get_version(self):
        return requests.get(url=self.url_get_version, headers=app.headers_data)

    # 02.获取钱包中可用apps接口
    def get_apps(self):
        return requests.get(url=self.url_get_apps, headers=app.headers_data)

    # 03.获取token图标接口
    def get_token_icon(self, token_name):
        url = self.url_get_token_icon.format(token_name)
        return requests.get(url=url, headers=app.headers_data)