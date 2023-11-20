import nonebot
from nonebot import on_command
from nonebot.adapters.qq import Event, MessageSegment, Message
from nonebot.params import CommandArg

from src.plugins.nonebot_plugin_RustedWarfare.ImageHttp import TodayImage
from src.plugins.nonebot_plugin_RustedWarfare.MoreGoodJrrp.UserLib import DataSQL

config = nonebot.get_driver().config
YOUR_PUBLIC_IP = config.your_public_ip
PORT = config.your_image_port

JRRP = on_command(cmd='今日抽签', aliases={'jrrp', '今日运势', '运势'}, priority=50)  # noqa


@JRRP.handle()
async def handle_func(event: Event):
    ID = event.get_user_id()
    # await JRRP.send(str(TodayImage(ID=ID,ReturnName=)))
    url = f"http://{YOUR_PUBLIC_IP}:{PORT}/?today={int(ID, 16)}"  # noqa
    image = MessageSegment.image(url)
    User = DataSQL()

    # try:
    User.TodayUpdate(ID=ID, ImageName=TodayImage(ID=int(ID, 16), ReturnName=True))
    # except sqlite3.OperationalError:
    #     User.InIt(ID=ID, ImageName=TodayImage(ID=int(ID, 16), ReturnName=True))

    await JRRP.finish(image)
#
#
UserInfo = on_command(cmd='个人信息', priority=50)


@UserInfo.handle()
async def handle_func(event: Event):
    ID = event.get_user_id()
    User = DataSQL()
    try:
        await User.UserInfoImage(ID=ID)
        url = f"http://{YOUR_PUBLIC_IP}:{PORT}/?UserID={ID}"  # noqa
        image = MessageSegment.image(url)
        await UserInfo.finish(image)

    except TypeError:
        await UserInfo.finish("你还没有抽签过哦！")


ChangeName = on_command(cmd='改名', priority=50)


@ChangeName.handle()
async def handle_func(event: Event, message: Message = CommandArg()):
    ID = event.get_user_id()

    User = DataSQL()
    if await User.ChangeName(ID=ID, Name=message):

        await ChangeName.finish("修改成功")
    else:

        await ChangeName.finish("你还没有签到过哦！")

