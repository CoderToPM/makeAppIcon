# -*- coding: utf-8 -*-

"""
@author: heyongchao
@Created on: 2019/12/7 6:48 下午
@Desc: 
"""
import os
import sys
from utils import makeImage, globalvar as gl
from utils.imgManager import ImgManager

dirname, filename = os.path.split(os.path.abspath(__file__))
gl._init()
gl.set_value('dirname', dirname)
print("当前脚本所在路径：" + dirname)
package_url = dirname + '/site-packages'
sys.path.append(package_url)
if len(sys.argv) != 4:
    print("参数缺失,参数列表：version1,version2,appiconset_path")
    sys.exit(0)
version1 = sys.argv[1]
version2 = sys.argv[2]
appiconset_path = sys.argv[3]
print("version1:%s,version2:%s" % (version1, version2))

print('begin make watermark appIcon ...')
makeImage.mark_image(version1, version2)
print('begin create appIcon ...')
ImgManager(appiconset_path).handle_icon_images()
#sys.exit(0)
