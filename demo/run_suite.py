# 导包
import time
import unittest
import app
from scripts.test01_common import TestCommon
from scripts.test02_coin import TestCoin
from tools.chart import Chart
from tools.HTMLTestRunner import HTMLTestRunner

# 组装测试套件
suite = unittest.TestSuite()
# 添加common模块测试用例
suite.addTest(unittest.makeSuite(TestCommon))
# 添加coin模块测试用例
suite.addTest(unittest.makeSuite(TestCoin))

# 指定测试报告的路径
# report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
report = app.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report, "wb") as f:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f, title="API Report")
    # 执行测试套件
    runner.run(suite)

# 生成图表
Chart()