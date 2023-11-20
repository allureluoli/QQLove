import sqlite3

conn = sqlite3.connect('MoreGoodJrrpData.db')
# 连接到数据库（如果不存在则创建）
cursor = conn.cursor()

ID = '687B4349812698E8212C40D7E435F3D7'

# cursor.execute(
#     f'''SELECT Username, DayQuantity, Favorability, LuckQuantity,
#      Inauspicious, LuckValue FROM UserLib WHERE UserId = '{ID}';''')
# Username, DayQuantity, Favorability, LuckQuantity, Inauspicious, LuckValue = cursor.fetchone()[0]
# cursor.execute('''SELECT * FROM UserLib WHERE UserId = '687B4349812698E8212C40D7E435F3D7';''')

# cursor.execute(f'''SELECT Time FROM UserLib WHERE UserId = '{ID}';''')
# print(type(cursor.fetchone()[0]))
cursor.execute(f'''SELECT * FROM UserLib WHERE UserId = '21415125';''')
print(cursor.fetchone())
cursor.execute(f'''
        UPDATE UserLib
        SET DayQuantity = '1',
        LuckValue = '999999999'
        WHERE UserId = '{ID}';
                 ''')
conn.commit()
# cursor.execute('''SELECT * FROM UserLib WHERE UserId = '687B4349812698E8212C40D7E435F3D7';''')

# print(cursor.fetchone())
cursor.close()
# print(cursor.fetchone())

# cursor.execute(f'''SELECT Time FROM UserLib WHERE UserId = '{ID}';''')