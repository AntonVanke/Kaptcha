import os
import base64
import random
import time
from string import ascii_letters, digits
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ascii_letters = ascii_letters.replace("i", "").replace("l", "").replace("I", "").replace("Q", "").replace("j",
                                                                                                          "").replace(
    "q", "")
digits = digits.replace("0", "")
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
FONT = [BASE_DIR + "/font1.ttf",
        BASE_DIR + "/font2.ttf",
        BASE_DIR + "/font3.ttf",
        BASE_DIR + "/font4.ttf"]  # https://fonts.google.com/


class CaptchaPainter:
    def __fill_color(self):
        """
        获取颜色
        :return:
        """
        if self.mode == "RGB" or self.mode == "RGBW":
            return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(150, 255)
        else:
            return random.randint(0, 155)

    def __add_chips(self, _draw):
        """
        添加碎片
        :param _draw:
        :return:
        """
        for _chip in range(self.gran * 4):
            # 碎片宽度
            _width = random.randint(self.chip_w - 10, self.chip_w + 10)
            # 碎片高度
            _height = random.randint(self.chip_h - 10, self.chip_h + 10)
            # 碎片左上角 x 轴位置
            _x = random.randint(0, self.im_x)
            # 碎片左上角 y 轴位置
            _y = random.randint(0, self.im_y)
            if _chip % 3 == 1:
                _x2 = random.randint(_x - 50, _x + 50)
                _y2 = random.randint(_y - 50, _y + 50)
                _draw.line((_x, _y, _x2, _y2), fill=self.__fill_color(), width=random.randint(4, 8))
            elif _chip % 3 == 2:
                _draw.ellipse((_x, _y, _x + _width, _y + _height), fill=self.__fill_color())
            else:
                _draw.rectangle((_x, _y, _x + _width, _y + _height), fill=self.__fill_color())

    def __add_text(self):
        """
        添加文字
        :return:
        """
        text_len = len(self.text)
        for _ in range(len(self.text)):
            _x = random.randint(self.im_x // text_len * _, self.im_x // (text_len + 1) * (_ + 1))
            _y = random.randint(self.im_y // 15, self.im_y // 7)
            # print(_x, _y)
            self.draw.text((_x, _y), text=self.text[_], fill=self.__fill_color(),
                           font=ImageFont.truetype(font=random.choice(self.font),
                                                   size=random.randint(self.im_y - (self.im_y // 4),
                                                                       self.im_y - (self.im_y // 16))))

    def scribble(self):
        for _ in range(self.gran * 10):
            _x = random.randint(0, self.im_x)
            _y = random.randint(0, self.im_y)
            self.draw.rectangle((_x, _y, _x + 5, _y + 5), fill=self.bg)

    @property
    def normal(self) -> Image:
        """
        静态图片
        :return:
        """
        self.__add_chips(self.draw)
        return self.im

    def gif(self) -> BytesIO:
        """
        动态图片
        :return:
        """
        pics = []
        for _ in range(5):
            _im = self.im.copy()
            _d = ImageDraw.Draw(_im)
            self.__add_chips(_d)
            pics.append(_im)
        buffer = BytesIO()
        pics[0].save(buffer, save_all=True, format="gif", append_images=pics[1:], transparency=0, duration=500, loop=0,
                     disposal=2, quality=9)
        return buffer

    def __init__(self, text="", im_x=260, im_y=125, gran=5, mode="RGB", font: list = None, bg="white"):
        # 验证码文字
        if font is None:
            font = [BASE_DIR + "/font1.ttf"]
        self.text = text
        self.font = font
        # 背景颜色
        self.bg = bg
        # 验证码宽度
        self.im_x = im_x
        # 验证码高度
        self.im_y = im_y
        # 混淆粒度
        self.gran = gran
        # 色彩模式
        self.mode = mode
        # 创建图片
        self.im = Image.new(self.mode, (im_x, im_y), self.bg)
        self.draw = ImageDraw.Draw(self.im)
        # 混淆平均宽度
        self.chip_w = self.im_x // 15
        # 混淆平均高度
        self.chip_h = self.im_y // 10
        # 添加文字
        self.__add_text()
        # self.scribble()


class Captcha:
    @staticmethod
    def __rand(string, k):
        return "".join(random.choices(string, k=k))

    def __filter(self, _im):
        if self.contour:
            return _im.filter(ImageFilter.CONTOUR)
        elif self.enhance:
            return _im.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif self.edge:
            return _im.filter(ImageFilter.FIND_EDGES)
        elif self.emboss:
            return _im.filter(ImageFilter.EMBOSS)
        else:
            return _im

    def __init__(self,
                 width=200,
                 height=80,
                 chips=5,
                 mode="RGB",
                 imageObj=False,
                 gif=False,
                 font: list = None,
                 bg="white",
                 contour=False,
                 enhance=False,
                 edge=False,
                 emboss=False
                 ):
        """

        :param width: 验证码宽度
        :param height: 验证码高度
        :param chips: 混淆碎片数量
        :param mode: 颜色模式("RGB" | "L")
        :param imageObj: 返回 Image 对象
        :param gif: 返回 gif 图片(默认关闭,降低大小,开启时无法使用滤镜)
        :param font: List 字体
        :param bg: 背景颜色(例如：#000000、white)
        :param contour: 轮廓滤镜(ImageFilter.CONTOUR)
        :param enhance: 增强滤镜(ImageFilter.EDGE_ENHANCE_MORE)
        :param edge: 边缘滤镜(ImageFilter.FIND_EDGES) 黑色背景
        :param emboss: 浮雕滤镜(ImageFilter.EMBOSS)
        """
        self.width = width
        self.height = height
        self.chips = chips
        self.mode = mode
        self.font = FONT or font
        self.bg = bg
        self.imageObj = imageObj
        self.gif = gif

        self.contour = contour
        self.enhance = enhance
        self.edge = edge
        self.emboss = emboss

    def letter(self, length=4):
        """
        纯英文
        :param length: 字符长度
        :return:
        """
        text = self.__rand(ascii_letters, length)
        return self.__handel(text)

    def digit(self, length=4):
        """
        纯数字
        :param length: 字符长度
        :return:
        """
        text = self.__rand(digits, length)
        return self.__handel(text)

    def letter_digit(self, length=4):
        """
        数英混合
        :param length:
        :return:
        """
        text = self.__rand(ascii_letters + digits, length)
        return self.__handel(text)

    def __handel(self, text):
        cp = CaptchaPainter(text=text,
                            im_x=self.width,
                            im_y=self.height,
                            gran=self.chips,
                            mode=self.mode,
                            font=self.font,
                            bg=self.bg)
        if self.gif:
            data = cp.gif()
            if not self.imageObj:
                return text, "data:image/gif;base64," + base64.b64encode(data.getvalue()).decode()
            else:
                # gif 无法载入为动图
                return text, Image.open(data)
        else:
            im = self.__filter(cp.normal)
            if not self.imageObj:
                buffer = BytesIO()
                im.save(buffer, format='JPEG')
                return text, "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode()
            else:
                return text, im


if __name__ == '__main__':
    a = Captcha(imageObj=True)


    def test1():
        start = time.time()
        for _ in range(100):
            a.letter_digit()
        print(f'100次测试平均单张速度:{(time.time() - start) / 100}s')


    def test2():
        credit = 0
        while True:
            t, i = a.letter_digit()
            i.show()
            if t.lower() != input(f"<{credit}>请输入验证码:\t").lower():
                break
            credit += 1


    def example():
        # 创建一个 宽 260px 高 125px 混淆碎片度 10 灰度图，返回 (str, Image)
        e = Captcha(width=260, height=125, chips=5, mode="L", imageObj=True, gif=False)
        e1_t, e1_c = e.letter_digit(5)
        print(e1_t, e1_c.show())
        # 将色彩模式改为彩色
        e.mode = "RGB"
        e1_t, e1_c = e.letter(4)
        print(e1_t, e1_c.show())
        # 将碎片减少为 5
        e.chips = 5
        e1_t, e1_c = e.digit(3)
        print(e1_t, e1_c.show())
        # 将背景改为黑色,并使用 emboss 滤镜
        e.bg = "#000000"
        e.emboss = True
        e1_t, e1_c = e.letter_digit()
        print(e1_t, e1_c.show())
        # 自行创建
        e2 = CaptchaPainter(text="Test", gran=5)
        e2.normal.show()


    test1()
    # test2()
    example()
