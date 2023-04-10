import os

# 项目基础URL -- 测试环境
BASE_URL = "https://api.fxwallet.com"

# token
TOKEN = None

# 请求头数据
headers_data = {
    "Content-Type": "application/json;charset=utf-8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJmeHdhbGxldEBpbnRjaGFpbnMuY29tIiwidHlwZSI6ImFkbWluIiwiaWF0IjoxNjYyNjI0NTE0LCJleHAiOjE2NjUyMTY1MTR9.YNDGv4LGB_14hTRHztlzEpoPMLndZuhkuk1Ebwqzdts"
}

# 设置系统配置信息
# 统一参数化文件和执行文件的基准路径   （./  OR  ../）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# os.path.abspath(__file__)：当前文件的绝对路径
# os.path.dirname()：文件所在项目的绝对路径
print(BASE_DIR)

