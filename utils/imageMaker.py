# -*- coding: utf-8 -*-

"""
@author: heyongchao
@Created on: 2019/12/4 5:22 下午
@Desc: 
"""

import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 编辑图片路径
bk_img = cv2.imread("../images/kw_logo.png")
# 设置需要显示的字体
font_path = "../font/simsun.ttc"
# 32为字体大小
font = ImageFont.truetype(font_path, 20)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
# 绘制文字信息
# (100,300/350)为字体的位置，(255,255,255)为白色，(0,0,0)为黑色
draw.text((20, 6), "6.10.1", font=font, fill=(255, 255, 255))
# draw.text((100, 350), "你好", font=font, fill=(255, 255, 255))
bk_img = np.array(img_pil)

cv2.imshow("add_text", bk_img)
cv2.waitKey()
# 保存图片路径
cv2.imwrite("add_text.png", bk_img)
