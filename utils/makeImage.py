# -*- coding: utf-8 -*-

"""
@author: heyongchao
@Created on: 2019/12/4 7:59 下午
@Desc: 
"""
import os
from PIL import Image, ImageDraw, ImageFont
from utils import globalvar as gl


def gen_img(size=None):
    if size is None:
        size = 400
        # 生成大小为400x400RGBA是四通道图像，RGB表示R，G，B三通道，A表示Alpha的色彩空間
    image = Image.new(mode='RGBA', size=(1024, 1024), color=(255, 55, 55))
    # ImageDraw.Draw 简单平面绘图
    draw_table = ImageDraw.Draw(im=image)
    # 直接显示图片
    # image.show()


def pic_open(filepath):
    # 图片打开与显示
    image = Image.open(filepath)
    return image


def get_size(image):
    # 获取图像的宽和高
    width, height = image.size
    return width, height


def pic_text(filepath, size, version1, version2, setFont, fillColor, filename, direction=None):
    print(filepath, size, version1, version2, setFont, fillColor)
    # 打开图片
    image = pic_open(filepath)
    # 新建绘图对象
    draw = ImageDraw.Draw(image)
    # 显示图片
    # image.show()
    draw.text((90, 20), version1, font=setFont, fill=fillColor, direction=None)
    draw.text((550, 20), version2, font=setFont, fill=fillColor, direction=None)

    # image.show()
    # 保存
    pic_save(image, filename)


def pic_save(image, filename):
    # 保存
    image.save(filename)


def mark_image(version1, version2):
    size = None
    # gen_img()

    # ** ImageFont模块**
    # 选择文字字体和大小
    dirname = gl.get_value("dirname")
    font_path = '%s/font/microsoft_yahei_bold.ttf' % dirname
    file_default_path = "%s/images/kw_logo.png" % dirname
    file_new_img_path = "%s/images/kw_logo_mark_version.png" % dirname
    print(font_path, file_default_path, file_new_img_path)
    setFont = ImageFont.truetype(font_path, 120)
    # 设置文字颜色
    fillColor = "#ffffff"  # 蓝色
    # version1 = "6.10.1"
    # version2 = "1.0.1"
    size = (1024, 1024)

    # 打开图片
    image = pic_open(file_default_path)
    # 添加文字
    pic_text(file_default_path, size, version1, version2, setFont, fillColor, file_new_img_path, direction=None)


if __name__ == "__main__":
    mark_image()
