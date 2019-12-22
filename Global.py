# -*- coding: utf-8 -*-
#图片浏览索引
index =0
path=[]

#图片保存路径
save_path="/root/mx-rcnn-self/output"

#打开图片路径
open_img_dir="/root/mx-rcnn-self/output"

#需要识别的图片路径
img_dir_jpg="/root/mx-rcnn/testimage"
img_dir_JPG="/root/mx-rcnn/testimage"
img_dir_png="/root/mx-rcnn/testimage"


#CLASSES[]
CLASSES=['__background__']

#配置参数全局变量
prefix_value='model/e2e'
conf_thresh_value=0.7
nms_thresh_value=0.3
num_class_value=8

prefix=''

#当前图片的识别信息
PICTURE_INFO=[[],[],[]]