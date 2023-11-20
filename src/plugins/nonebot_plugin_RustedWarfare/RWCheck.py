import os
from nonebot import on_command
from nonebot.params import CommandArg, RawCommand
from nonebot.rule import to_me
from nonebot.adapters import Message


def RWCheck(name):
    path = os.getcwd() + '/data/RustedWarfareData/Units/ORIGINAL/' + name + '.txt'
    with open(path, encoding='utf-8') as f:
        return f.read()


Check = on_command(cmd='查询', aliases={'cx', 'wq'}, rule=to_me(), priority=60)


@Check.handle()
async def handle_func(message: Message = CommandArg()):
    try:
        await Check.send(RWCheck(str(message)))
    except FileNotFoundError:
        await Check.send('你输入的单位名无法识别。')


nameList = on_command('查看', priority=60)


@nameList.handle()
async def handle_func(message: Message = CommandArg(), message2: str = RawCommand()):
    message = message2.replace('/', '') + str(message).replace(' ', '')
    match message:
        case '查看虫族单位':
            message = '虫族'
        case '查看海军单位':
            message = '海军'
        case '查看建筑单位':
            message = '建筑'
        case '查看旧版单位':
            message = '旧版单位'
        case '查看空军单位':
            message = '空军'
        case '查看陆军单位':
            message = '陆军'
        case '查看特殊单位':
            message = '特殊'

    await nameList.finish('\n'+RWCheck(message))
