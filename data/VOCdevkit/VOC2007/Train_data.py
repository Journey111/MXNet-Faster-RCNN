# -*- coding: utf-8 -*-
import os
import random

trainval_percent = 0.999
train_percent = 0.99
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)
num=len(total_xml)
list = range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval = random.sample(list, tv)  # zhi zhi ding wei zhi sui ji jie qu zhi ding wei du d wen jian
train = random.sample(trainval, tr)
os.chdir('/root/mx-rcnn/data/VOCdevkit/VOC2007/ImageSets/Main')   #wenjian cunfang lujing 
ftrainval = open('trainval.txt', 'w')  # chuang jian yi ge txt wen jian
ftest = open('test.txt', 'w')
ftrain = open('train.txt', 'w')
fval = open('val.txt', 'w')
for i in list :
  name =total_xml[i][:-4] + '\n'
  if i in trainval:
       ftrainval.write(name)
       if i in train:
            ftrain.write(name)
       else:
            fval.write(name)
  else:
      ftest.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
