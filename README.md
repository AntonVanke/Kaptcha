## Kaptcha:python 验证码生成工具

![Kaptcha](https://github.com/AntonVanke/Kaptcha/raw/master/demos/Kaptcha.jpg)

## 简述

### 优点

- 调用简单
- 高度自定义
- 生成快速

### 示例

| 类型(干扰都为5) | 内容 | 图片                                                         |
| --------------- | ---- | ------------------------------------------------------------ |
| 字母数字混合型  | 7w8W | ![HyGU](https://github.com/AntonVanke/Kaptcha/raw/master/demos/HyGU.jpg) |
| 数字型          | 5244 | ![5244](https://github.com/AntonVanke/Kaptcha/raw/master/demos/5244.jpg) |
| 字母型          | Ehqx | ![jFbF](https://github.com/AntonVanke/Kaptcha/raw/master/demos/jFbF.jpg) |
| 增强型          | wd81 | ![wd81](https://github.com/AntonVanke/Kaptcha/raw/master/demos/wd81.jpg) |
| 边缘凸显        | bpCk | ![bpCk](https://github.com/AntonVanke/Kaptcha/raw/master/demos/bpCk.jpg) |
| 浮雕效果        | MkT6 | ![MkT6](https://github.com/AntonVanke/Kaptcha/raw/master/demos/MkT6.jpg) |
| 轮廓            | qXLT | ![qXLT](https://github.com/AntonVanke/Kaptcha/raw/master/demos/qXLT.jpg) |
| GIF动态图       | VbFe | ![VbFe](https://github.com/AntonVanke/Kaptcha/raw/master/demos/VbFe.gif) |

### 生成速度

| 类型                | 1000次生成平均单次速度 |
| ------------------- | ---------------------- |
| 基本样式(Base64)    | 1.48ms                 |
| 基本样式(PIL.Image) | 1.32ms                 |
| 滤镜渲染(Base64)    | 1.57ms                 |
| GIF动图             | 10.93ms                |

## 如何使用

#### 安装

```bash
pip install kaptcha
```

#### 简单的使用

```python
import kaptcha

x, y = kaptcha.Captcha().letter_digit()
# x 是生成的文字
# y 是生成的 base64 图像
print(x, y)
```

1. 数英混合

   ```PYTHON
   import kaptcha
   
   x, y = kaptcha.Captcha().letter_digit()
   print(x, y)
   ```

2. 纯英文

   ```python
   import kaptcha
   
   x, y = kaptcha.Captcha().letter()
   print(x, y)
   ```

3. 纯数字

   ```python
   import kaptcha
   
   x, y = kaptcha.Captcha().digit()
   print(x, y)
   #4696 data:image/jpeg;base64,/9j/4AAQSkZJR……
   
   ```

#### 详细使用方法

```python
kaptcha.Captcha(width=200,  # 验证码的宽度 px
                 height=80,  # 验证码的高度 px
                 chips=5,  # 干扰点 强度(1-20)
                 mode="RGB",  # 色彩模式 RGB\L
                 imageObj=False,  # 返回 PIL.Image 格式
                 gif=False,  # gif 格式验证码(不可与imageObj同为真)
                 font: list = None,  # 字体路径列表
                 bg="white",  # 背景颜色 颜色代码或 16 进制
                 contour=False,  # 以下四个滤镜只可开启一个
                 enhance=False,
                 edge=False,
                 emboss=False
                 )

# length调整字符串长度(建议同时调整width)
Captcha().letter(length=4)  # 英文
Captcha().digit(length=4)  # 数字
Captcha().letter_digit(length=4)  # 数英
Captcha(gif=True).letter_digit(length=4)  # 动态图
 
# 绘制函数
kaptcha.CaptchaPainter(text="",  # 绘制文字
                       im_x=260,  # 验证码的宽度 px
                       im_y=125,   # 验证码的高度 px
                       gran=5,  # 干扰点 强度(1-20)
                       mode="RGB",  # 色彩模式 RGB\L
                       font: list = None,  # 字体路径列表
                       bg="white"  # 背景颜色 颜色代码或 16 进制
                      )
CaptchaPainter().normal  # 静态图(-> PIL.Image)
CaptchaPainter().gif()  # 动态图(-> BytesIO())
```

##### 返回值

```python
# 当imageObj=False(默认) -> 返回 (str, base64: str)
Captcha().letter(length=4)
print(Captcha().letter(length=4)[1])  # > data:image/jpeg;base64,/9j/4AAQSkZJR......


# 当imageObj=True -> 返回 (str, PIL.Image)
Captcha(imageObj=True).letter(length=4)
Captcha(imageObj=True).letter(length=4)[1].show()
```

## LICENSE

>
> MIT License
>
> Copyright (c) 2022 AntonVanke

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/kaptcha)](https://pypi.org/project/kaptcha/)[![PyPI - License](https://img.shields.io/pypi/l/kaptcha)](https://github.com/AntonVanke/Kaptcha/blob/master/LICENSE)[![GitHub Repo stars](https://img.shields.io/github/stars/antonvanke/kaptcha?style=social)](https://github.com/AntonVanke/Kaptcha)

