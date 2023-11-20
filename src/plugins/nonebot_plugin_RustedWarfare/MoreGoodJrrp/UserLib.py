import os
import sqlite3

# 吉：大吉、大胸、吉、收款码、小吉、中吉
# 凶：急了、寄、绷、孙笑川、凶、小寄、大寄
from src.plugins.nonebot_plugin_RustedWarfare.MoreGoodJrrp.OutImage import TextImage
from src.plugins.nonebot_plugin_RustedWarfare.MoreGoodJrrp.ntp import TimeJudgement, NtpTime


def IfLuck(ImageName: str):
    """ 是凶是吉呢？ 输入返回的图片名罢了 """
    match ImageName:
        case "大吉":
            return 100
        case "吉":
            return 80
        case "收款码":
            return 50
        case "中吉":
            return 50
        case "大胸":
            return 50
        case "小吉":
            return 30
        case "孙笑川":
            return -100
        case "凶":
            return -80
        case "急了":
            return -80
        case "绷":
            return -70
        case "大寄":
            return -70
        case "寄":
            return -50
        case "小寄":
            return -30


# \data\MoreGoodJrrpData
class DataSQL:
    """ 数据库对象 """

    def __init__(self):

        path = os.getcwd() + '/data/MoreGoodJrrpData/MoreGoodJrrpData.db'
        self.conn = sqlite3.connect(path)
        # 连接到数据库（如果不存在则创建）
        self.cursor = self.conn.cursor()
        # 创建一个游标对象

    def InIt(self, ID, ImageName: str):
        """ 初始化新用户的数据 """
        Time = NtpTime()
        LuckValue = 0
        LuckQuantity = 0
        Inauspicious = 0
        Value = IfLuck(ImageName)  # 判断吉凶
        LuckValue += Value

        if Value > 0:
            LuckQuantity += 1
        else:
            Inauspicious += 1

        sql = f"INSERT INTO UserLib VALUES ('{ID}', '未命名用户', 1, 0, '{LuckQuantity}', '{Inauspicious}', '{LuckValue}','{Time}')"

        self.cursor.execute(sql)

        # 保存（提交）更改
        self.conn.commit()

        # 关闭连接
        self.conn.close()

    def TodayUpdate(self, ID, ImageName: str):
        """ 抽签数据更新"""
    # try:
        # self.cursor.execute()
        # 查询时间
        self.cursor.execute(f'''SELECT Time FROM UserLib WHERE UserId = '{ID}';''')
        try:
            Time = self.cursor.fetchone()[0]
            # 判断时间时间否更新
            if not TimeJudgement(str(Time)):
                _ = TimeJudgement(str(Time))
            else:
                _, Time = TimeJudgement(str(Time))
            if _:
                # 查到了，开始更新数据
                self.cursor.execute(
                    f'''SELECT DayQuantity, Favorability, LuckQuantity, Inauspicious, LuckValue  FROM UserLib WHERE UserId = '{ID}';''')
                DayQuantity, Favorability, LuckQuantity, Inauspicious, LuckValue = self.cursor.fetchone()
                DayQuantity += 1
                Favorability += 5
                Value = IfLuck(ImageName)  # 判断吉凶
                LuckValue += Value
                if Value > 0:
                    LuckQuantity += 1
                else:
                    Inauspicious += 1

                self.cursor.execute(f'''
                        UPDATE UserLib
                        SET DayQuantity = {DayQuantity},
                         Favorability = {Favorability},
                         LuckQuantity = {LuckQuantity},
                         Inauspicious = {Inauspicious},
                         LuckValue = {LuckValue},
                         Time = {Time}
                        WHERE UserID = '{ID}';
                                 ''')
                # 更新完了提交保存
                self.conn.commit()
                self.cursor.close()
                return True
            else:
                # "已经签到过了 返回个False赶紧润"
                return False
        except TypeError:
            self.InIt(ID=ID, ImageName=ImageName)
    # 查了个寂寞，这人压根没签到过，给他初始化
    #     except TypeError:
    #         self.InIt(ID=ID, ImageName=ImageName)
    #         return True

    async def ChangeName(self, ID, Name):
        """ 修改名字的方法"""

        self.cursor.execute(f'''SELECT * FROM UserLib WHERE UserId = '{ID}';''')
        if self.cursor.fetchone() is None:
            return False

        self.cursor.execute(f'''
                UPDATE UserLib
                SET Username = '{Name}'
                WHERE UserID = '{ID}';
                         ''')

        self.conn.commit()
        self.conn.close()
        # 究竟哪种断开才对呢。。。

        return True


    async def UserInfoImage(self, ID):

        self.cursor.execute(
            f'''SELECT Username, DayQuantity, Favorability, LuckQuantity,
             Inauspicious, LuckValue FROM UserLib WHERE UserId = '{ID}';''')
        Username, DayQuantity, Favorability, LuckQuantity, Inauspicious, LuckValue = self.cursor.fetchone()
        self.cursor.close()
        if await TextImage(UserName=Username, DayQuantity=DayQuantity, Favorability=Favorability,
                           LuckQuantity=LuckQuantity, LuckValue=LuckValue, Inauspicious=Inauspicious, ID=ID):
            return True




# # 创建一个表

# #                                   用户ID 昵称 签到天数 好感度 吉数 凶数

# print()

# cursor.execute("INSERT INTO UserLib VALUES ('DASDAF', '未命名用户', 1, 1, 1, 1,2)")
# cursor.execute("INSERT INTO UserLib VALUES ('ID1145124', 'Cure Sky', 1, 1, 1, 1,0)")
# cursor.execute("INSERT INTO UserLib VALUES ('UD2145M2', '呆瓜', 1, 1, 1, 1,0)")
# cursor.execute("INSERT INTO UserLib VALUES ('251555', 'gs', 1, 1, 1, 1,0)")
# cursor.execute("INSERT INTO UserLib VALUES ('21515', 'sb', 1, 1, 1, 1,0)")
#                      INFO UserLib是表
