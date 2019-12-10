#!/bin/bash

#**********************************************************
# * Author        : heyongchao
# * Email         : yongchaohe@gmail.com
# * Created       : 2019-12-08 00:57
# * Description   : 用于生成icon
#**********************************************************

zip_version=20191209-135722
imageProcessing_package_url=https://xx.xx.com/imageProcessing-${zip_version}.zip

function make() {
  if [ "$1" ] && [ "$2" ] && [ "$3" ]; then
    curl -sSO $imageProcessing_package_url
    unzip imageProcessing-${zip_version}.zip -d imageProcessing
    python3 imageProcessing $1 $2 $3
  else
    echo "参数缺失,参数列表：version1,version2,appiconset_path"
  fi
}
make "$1" "$2" "$3"
# 下面Python2版本不好使，先直接调用吧
#python_version=`python -V|awk -F ' ' '{print $2}'`
#echo "python_version:"$python_version
#if [[ "$python_version" =~ ^2.* ]] || [[ "$python_version" =~ ^3.* ]]; then
#    echo "已安装Python，继续生成icon"
#    make $1 $2 $3
#else
#    echo "未安装Python，图标无法自动生成了"
#fi
