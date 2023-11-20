import time
import ntplib
import datetime


def NtpTime():
    """ 通过Ntp服务器返回时间 """
    MD = True
    num = 1
    ntpurl = f'ntp{num}'
    while MD:
        try:
            ntp_server = f"{ntpurl}.aliyun.com"
            # 创建NTP客户端
            client = ntplib.NTPClient()

            # 发送NTP请求并获取时间信息
            response = client.request(ntp_server)
            MD = False
            timestamp = response.tx_time

            # 将时间戳转换为日期时间格式

            local_time = time.localtime(timestamp)
            formatted_time = time.strftime("%Y,%m,%d", local_time)
            Year, Mouth, Day = formatted_time.split(',')

            Year, Mouth, Day = map(int, [Year, Mouth, Day])
            # 定义两个日期

            date1 = datetime.date(Year, Mouth, Day)
            return str(date1)
        except ntplib.NTPException:
            num += 1

# 定义NTP服务器地址和国家授时中心的标准时间服务地址
# ntp_server = "ntp.ntsc.ac.cn" # noqa

def TimeJudgement(date2):
    """ 通过与ntp服务器交互 判断时间是否更新 输入时间 返回True表示更新 """
    try:

        ntp_server = "ntp.aliyun.com"
        # 创建NTP客户端
        client = ntplib.NTPClient()

        # 发送NTP请求并获取时间信息
        response = client.request(ntp_server)
    # except TimeoutError:
    except ntplib.NTPException:

        ntp_server = "ntp.tencent.com"
        # 创建NTP客户端
        client = ntplib.NTPClient()
        try:
            # 发送NTP请求并获取时间信息
            response = client.request(ntp_server)
        except ntplib.NTPException:

            ntp_server = "ntp2.aliyun.com"
            # 创建NTP客户端
            client = ntplib.NTPClient()
            response = client.request(ntp_server)

    # 从响应中提取时间信息
    timestamp = response.tx_time

    # 将时间戳转换为日期时间格式

    local_time = time.localtime(timestamp)
    formatted_time = time.strftime("%Y,%m,%d", local_time)
    Year, Mouth, Day = formatted_time.split(',')

    Year, Mouth, Day = map(int, [Year, Mouth, Day])
    # 定义两个日期

    date1 = datetime.date(Year, Mouth, Day)

    # 计算日期差 如果时间差为负或0的说明签到过了，如果时间差为正的说明没签到
    # 现在时间减去数据库中用户时间

    Year, Mouth, Day = map(int, date2.split('-'))
    date2 = datetime.date(Year, Mouth, Day)

    delta = date1 - date2

    total_seconds = int(delta.total_seconds())

    if total_seconds > 0:
        return True, str(date1)
    else:
        return False


print(TimeJudgement('2023-11-17'))
#
# date1 = datetime.date(2024, 5, 2)
# print(TimeJudgement(date1))
