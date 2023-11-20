import os
import random
from datetime import date
from pathlib import Path
import http.server
from urllib.parse import urlparse, parse_qs


def UserImage(Id: str):
    Id += '.png'
    """ 返回符合用户ID的图片 """
    path = f'{os.getcwd()}/data/UserImage/'
    path = Path(path+Id)

    if path.is_file():
        with open(path, mode='rb') as f:
            image = f.read()
            return image
    return None


def GameMap(message: str):
    """ 返回随机的地图 """
    path = os.getcwd() + '/data/RustedWarfareData/Map/' + message

    MapList = os.listdir(path)
    message = random.choice(MapList)

    image = str(Path(path + '/' + message))

    with open(image, mode='rb') as f:
        image = f.read()
    return image


def TodayImage(ID: int, ReturnName: bool = False):
    """

    通过ID返回今日抽到的签

    数值ReturnName为True时会返回图像名

    """
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + ID)

    path = os.getcwd() + '/data/RandomImage/'

    ImageList = os.listdir(path)
    image = rnd.choice(ImageList)

    if ReturnName:
        return image.replace(".jpg", '')
    image = str(Path(path + image))
    with open(image, mode='rb') as f:
        image = f.read()
    return image


class WebRequest(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "image/jpeg")
        self.end_headers()
        url_parts = urlparse(self.path)
        query_params = parse_qs(url_parts.query)

        Map = query_params.get('map', [''])[0]

        Today = query_params.get('today', [''])[0]

        UserID = query_params.get('UserID', [''])[0]

        if Today:
            self.wfile.write(TodayImage(int(Today)))
        if Map:
            message = GameMap(Map)
            self.wfile.write(message)
        if UserID:
            self.wfile.write(UserImage(UserID))
