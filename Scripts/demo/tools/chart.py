# 导包
import plotly.express as px
import pandas as pd

# 定义图表类
class Chart:
    # 读取CSV文件并仅保留需要的列
    df = pd.read_csv("C:/Users/33977/Desktop/logs.csv", usecols=["URL", "Duration (ms)"])

    # 去除“URL”字段中的通用网址部分，仅保留接口地址
    df["URL"] = df["URL"].apply(lambda url: url.replace("https://api.fxwallet.com", ""))

    # 截断超过20个字符的横坐标数据
    df["display_URL"] = df["URL"].apply(lambda label: label[:20] + "..." if len(label) > 20 else label)

    # 创建鼠标悬停文本
    hover_text = df.apply(lambda row: f"接口：{row['URL']}<br>响应时间：{row['Duration (ms)']:.2f} ms", axis=1)

    # 修改x轴和y轴的范围和标签
    fig = px.scatter(df, x="display_URL", y="Duration (ms)", hover_name=hover_text)
    fig.update_xaxes(range=[-0.5, len(df) - 0.5], tickangle=45, tickfont=dict(size=10))
    fig.update_yaxes(tickformat=".2f")

    # 显示图表
    fig.show()