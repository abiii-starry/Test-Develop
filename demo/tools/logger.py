import csv
import datetime

class Logger:
    PATH = "C:/Users/33977/Desktop/logs.csv"

    @staticmethod
    def log(url: str, response_time: float) -> None:
        with open(Logger.PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            # 在文件末尾添加一行记录
            writer.writerow([url, response_time, datetime.datetime.now()])
