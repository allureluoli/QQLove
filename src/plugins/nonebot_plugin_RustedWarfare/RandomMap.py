import nonebot
from nonebot import on_command
from nonebot.params import RawCommand
from nonebot.adapters.qq import MessageSegment
config = nonebot.get_driver().config
YOUR_PUBLIC_IP = config.your_public_ip
PORT = config.your_image_port
RandomMap = on_command(cmd='随机单挑图',
                       aliases={'随机2p图', '随机2P图', '随机3P图', '随机3p图', '随机4P图', '随机4p图',
                                '随机6p图', '随机6P图', '随机8p图', '随机8P图',
                                '随机10p图', '随机10P图', 'psc抽图', 'PSC抽图'}, priority=50)


@RandomMap.handle()
async def handle_func(message: str = RawCommand()):
    message = message.replace('/', '')
    if message in ['随机单挑图', '随机2p图', '随机2P图']:
        message = 'p2'
    elif message in ['随机3P图', '随机3p图']:
        message = 'p3'
    elif message in ['随机4P图', '随机4p图']:
        message = 'p4'
    elif message in ['随机6P图', '随机6p图']:
        message = 'p6'
    elif message in ['随机8P图', '随机8p图']:
        message = 'p8'
    elif message in ['随机10P图', '随机10p图']:
        message = 'p10'
    elif message in ['PSC抽图', 'psc抽图']:
        message = 'PSC'

    url = f"http://{YOUR_PUBLIC_IP}:{PORT}/?map=" + message # noqa

    image = MessageSegment.image(url)

    await RandomMap.send(image)
