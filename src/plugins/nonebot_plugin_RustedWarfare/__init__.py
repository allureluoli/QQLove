import asyncio
import http.server
import nonebot
from nonebot import on_command, get_driver
from nonebot.rule import to_me
from src.plugins.nonebot_plugin_RustedWarfare.HomeList import HomeList
from . import MatchMap, GroupCheck, RWCheck, RandomMap, Course, MoreGoodJrrp
from .ImageHttp import WebRequest

driver = get_driver()
config = nonebot.get_driver().config
YOUR_PUBLIC_IP = config.your_public_ip
PORT = config.your_image_port


def startServer():
    httpd = http.server.HTTPServer(("0.0.0.0", PORT), WebRequest)
    httpd.serve_forever()
    print(f"http://hostlocal:{PORT}") # noqa


@driver.on_startup
def StartServer():
    asyncio.to_thread(startServer())


LOVE = on_command(cmd="love", aliases={'爱!', '爱酱', 'love', 'LOVE酱', 'love酱', '小宝贝', 'Love'}, rule=to_me(),
                  priority=50)


@LOVE.handle()
async def handle_func():
    await LOVE.finish('呐呐呐？是在叫我嘛~')


ceshi = on_command("获取房间列表", to_me())


@ceshi.handle()
async def handle_echo():
    await ceshi.send(message='\n' + HomeList())
