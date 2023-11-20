import os
from nonebot import on_command
from nonebot.params import RawCommand

Course = on_command(cmd='房间指令教程', aliases={'地图导入教程', '模组导入教程', 'MOD导入教程', '回放导入教程'}, priority=50)


@Course.handle()
async def handle_func(message: str = RawCommand()):

    path = os.getcwd() + '/data/RustedWarfareData/Course/'

    def W(T):
        with open(path + T, encoding='utf-8') as M:
            return M.read()

    match message:
        case '房间指令教程':
            await Course.finish("\n"+W('server_instruct.txt'))
        case '地图导入教程':
            await Course.finish("\n"+W('map_course.txt'))
        case '模组导入教程':
            await Course.finish("\n"+W('mod_course.txt'))
        case 'MOD导入教程':
            await Course.finish("\n"+W('mod_course.txt'))
        case '回放导入教程':
            await Course.finish("\n"+W('replay_course.txt'))
