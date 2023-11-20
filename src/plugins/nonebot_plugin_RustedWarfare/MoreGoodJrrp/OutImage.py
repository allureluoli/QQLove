import os

from PIL import Image, ImageDraw, ImageFont
import random


# 创建一个新的图像，大小为宽400，高200，黑色背景


# 设置要添加的文本内容和位置
async def TextImage(UserName: str, DayQuantity: int, Favorability: float, LuckQuantity: int, Inauspicious: int,
                    LuckValue: int, ID: int):
    path = os.getcwd() + '/data/UserImage/res/'
    image = Image.open(f'{path}BaseImage.png')
    # 获取一个字体对象
    font_path = f"{path}/awa.ttc"  # 你需要将"path_to_your_font.ttf"替换为你自己的字体文件路径
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)
    color = "#19ddf7"
    draw = ImageDraw.Draw(image)

    UserName_position = (315, 140)
    DayQuantity_position = (935, 235)
    Favorability_position = (315, 235)
    LuckQuantity_position = (315, 325)
    Inauspicious_position = (800, 320)
    LuckyValue_position = (315, 420)

    draw.text(UserName_position, UserName, fill=color, font=font)

    draw.text(Favorability_position, str(Favorability), fill='#ff8686', font=font)

    draw.text(DayQuantity_position, str(DayQuantity), fill='#ff8f19', font=font)

    draw.text(LuckQuantity_position, str(LuckQuantity), fill='red', font=font)

    draw.text(Inauspicious_position, str(Inauspicious), fill='red', font=font)

    draw.text(LuckyValue_position, str(LuckValue), fill='green', font=font)

    with open(f'{path}text.txt', encoding='utf-8') as f:
        text = f.read()

    text = text.split('\n')

    text = random.choice(text)

    def insert_newlines(s, every=30):
        return '\n'.join(s[i:i + every] for i in range(0, len(s), every))

    text = '每日金句：\n\t\t\t\t' + insert_newlines(text)
    draw.text((100, 570), text, fill='red', font=font)

    # 保存生成的图像
    path = os.getcwd() + '/data/UserImage/'
    image.save(f"{path}{ID}.png")

    return True

# 需要自动对齐
#
# TextImage(UserName='Cure Sky', Favorability=1000, Inauspicious=0, DayQuantity=10, LuckQuantity=188, LuckyValue=9999)
