# -*- coding: utf-8 -*-

"""
@author: heyongchao
@Created on: 2019/12/5 9:37 上午
@Desc: 
"""

import json
import os
import subprocess
import threading
from PIL import Image
from utils import globalvar as gl


class ImgManager(object):
    thread_lock = threading.Lock()
    this_class_dir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, appiconset_path="/Users/heyongchao/gitclone/xx/Assets.xcassets/AppIcon.appiconset"):
        self.default_image_path = '%s/images/kw_logo_mark_version.png' % gl.get_value("dirname")
        self.AppIcon_base_path = appiconset_path

    @classmethod
    def sharedinstance(cls):
        with ImgManager.thread_lock:
            if not hasattr(ImgManager, "instance"):
                ImgManager.instance = ImgManager()
        return ImgManager.instance

    # 运行shell命令
    def runshellCMD(self, cmd, dsr):
        progress = subprocess.Popen(cmd, shell=True)
        progress.wait()
        result = progress.returncode
        if result != 0:
            print("%s失败" % (dsr))
        else:
            print("%s成功" % (dsr))

    # 创建图片
    def createImg(self, model):
        # path = '%s/images/kw_logo.png' % (os.getcwd())
        currentPath = self.AppIcon_base_path + '/' + model.filename
        print("currentPath:"+currentPath)
        im = Image.open(self.default_image_path, 'r')
        w, h = im.size
        print("default_icon_wh:%s,%s" % (str(w), str(h)))
        #
        # new_w, new_h = model.get_wh()
        # im.thumbnail((new_w, new_h))
        im.thumbnail((float(model.get_wh()), float(model.get_wh())))

        if model.filename.endswith('.png'):
            im.save("%s" % currentPath, "png")
            print("save success")
        else:
            # self.runshellCMD("sudo cp %s %s" % (path, currentPath), "拷贝")
            self.addTransparency(im)
            im.save("%s" % (currentPath), "jpeg")
            # r, g, b, alpha = im.split()
            # print("%s"%(str(im.split()[0])))

    # 修改透明度
    def addTransparency(img, factor=0.0):
        img = img.convert('RGBA')
        img_blender = Image.new('RGBA', img.size, (0, 0, 256, 256))
        img = Image.blend(img_blender, img, factor)
        return img

    # 解析Contents.json，这个文件每一个Images.xcassets 的AppIcon文件夹都有，直接复用就可以了
    def handle_icon_images(self):

        # jsonpath = os.getcwd() + "/Contents.json"

        # 目录是否存在,不存在则cp一份过去
        # mkdirlambda = lambda x: os.system("cp -r resource/* " + x) if not os.path.exists(x) else True
        # mkdirlambda(self.AppIcon_base_path)
        # 先强制拷贝进去，以我的为准吧
        os.system("cp -rf %s/resource/AppIcon.appiconset/* %s" % (gl.get_value("dirname"), self.AppIcon_base_path))
        jsonpath = self.AppIcon_base_path + "/Contents.json"
        if not os.path.exists(jsonpath):
            print("Contents.json path not exit")
            return
        with open(jsonpath, 'r') as f:
            jsonstr = f.read()
        modle = json.loads(jsonstr)
        arrs = modle['images']
        print(arrs)
        icon_models = []
        for obj in arrs:
            size = obj["size"]
            idiom = obj["idiom"]
            scale = obj["scale"]
            # 下面的处理其实有问题，还是需要改json
            filename = "Icon-%s-%s-%s.png" % (idiom, size, scale) if 'filename' not in obj else obj["filename"]
            icom = iconImg(size=size, idiom=idiom, filename=filename, scale=scale)
            # icon_models.append(icom)
            self.createImg(icom)
        print("all make success")

    """
  
    "size" : "29x29",
     "idiom" : "iphone",
     "filename" : "Icon-Small@3x.png",
     "scale" : "3x"
    """
    # json 数据里面有效数据的类


class iconImg(object):
    def __init__(self, size, idiom, filename, scale):
        self.size = size
        self.idiom = idiom
        self.filename = filename
        self.scale = scale

    def show(self):
        print("%s,%s,%s,%s" % (self.size, self.idiom, self.filename, self.scale))

    def get_wh(self):
        return (float(self.size.split('x')[0])) * (float(self.scale.split('x')[0]))
        # return (float(self.size.split('x')[0])), (float(self.size.split('x')[1]))


if __name__ == '__main__':
    ImgManager.sharedinstance().handle_icon_images()
    print("maker end")
    os._exit(0)
