import time
import kaptcha


def test4():
    start = time.time()
    obj = kaptcha.Captcha(gif=True)
    for _ in range(1000):
        obj.letter_digit()
    print(f"<gif动画>1000次测试平均单次生成时间: {(time.time() - start) / 1000:.5f}")


def test3():
    start = time.time()
    obj = kaptcha.Captcha(imageObj=True)
    for _ in range(1000):
        obj.letter_digit()
    print(f"<Image返回>1000次测试平均单次生成时间: {(time.time() - start) / 1000:.5f}")


def test2():
    start = time.time()
    obj = kaptcha.Captcha(enhance=True, chips=15)
    for _ in range(1000):
        obj.letter_digit()
    print(f"<滤镜渲染、超高干扰点>1000次测试平均单次生成时间: {(time.time() - start) / 1000:.5f}")


def test1():
    start = time.time()
    for _ in range(1000):
        kaptcha.Captcha().letter_digit()
    print(f"1000次测试平均单次生成时间: {(time.time() - start) / 1000:.5f}")


test1()
test2()
test3()
test4()
