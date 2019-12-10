#!/bin/bash

#**********************************************************
# * Author        : heyongchao
# * Email         : heyongchao@kuaishou.com
# * Created       : 2019-12-07 11:50
# * Description   : 用于生成icon
#**********************************************************

find . -name "imageProcessing*.zip" | xargs rm -rf
now_date_str=$(date +%Y%m%d-%H%M%S)
zip -r imageProcessing-${now_date_str}.zip ./ -X -9 \
  -x "testAddTextToImage.py" \
  -x "utils/imageMaker.py" \
  -x "*/\.*" -x "\.*" -x "font/msjh.ttf" \
  -x "font/simsun.ttc" \
  -x "images/kw_logo_mark_version.png" \
  -x "utils/__pycache__" \
  -x "*.pyc" \
  -x "build.sh" \
  -x "makeIcon.sh" \
  -x "imageProcessing*.zip" \
  -x "makeIcon.sh.bak"

echo "打包完成"
echo "开始替换makeIcon.sh里面的版本"
need_replace_str="zip_version="$now_date_str
sed -i ".bak" '/^zip_version=/c \
  '$need_replace_str'\
  ' makeIcon.sh
echo "请使用如下命令生成IOS图标："
echo "python imageProcessing.zip 9 32 /Users/heyongchao/gitclone/yourxcodeworkspace/Assets.xcassets/AppIcon.appiconset"