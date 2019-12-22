# -*- coding: utf-8 -*-
import argparse
import os
import cv2
import Global
import mxnet as mx
import numpy as np
from rcnn.logger import logger
from rcnn.config import config
from rcnn.symbol import get_resnet_test, get_vgg_test
from rcnn.io.image import resize, transform
from rcnn.core.tester import Predictor, im_detect, im_proposal,draw_all_detection
from rcnn.utils.load_model import load_param
from rcnn.processing.nms import py_nms_wrapper, cpu_nms_wrapper, gpu_nms_wrapper
import time



#CLASSES = ('__background__',
#             'bird_nest','good_circle1','bad_circle1','good_circle2',
#             'good_earthquake_hammer','bad_earthquake_hammer','spacer_bar')
config.TEST.HAS_RPN = True
SHORT_SIDE = config.SCALES[0][0]
LONG_SIDE = config.SCALES[0][1]
PIXEL_MEANS = config.PIXEL_MEANS
DATA_NAMES = ['data', 'im_info']
LABEL_NAMES = None
DATA_SHAPES = [('data', (1, 3, LONG_SIDE, SHORT_SIDE)), ('im_info', (1, 3))]
LABEL_SHAPES = None
# visualization
# CONF_THRESH = Global.conf_thresh_value
# NMS_THRESH = Global.nms_thresh_value
nms = py_nms_wrapper(Global.nms_thresh_value)


def get_net(symbol, prefix, ctx):
    arg_params, aux_params = load_param(prefix, convert=True, ctx=ctx, process=True)

    # infer shape
    data_shape_dict = dict(DATA_SHAPES)
    arg_names, aux_names = symbol.list_arguments(), symbol.list_auxiliary_states()
    arg_shape, _, aux_shape = symbol.infer_shape(**data_shape_dict)
    arg_shape_dict = dict(zip(arg_names, arg_shape))
    aux_shape_dict = dict(zip(aux_names, aux_shape))

    # check shapes
    for k in symbol.list_arguments():
        if k in data_shape_dict or 'label' in k:
            continue
        assert k in arg_params, k + ' not initialized'
        assert arg_params[k].shape == arg_shape_dict[k], \
            'shape inconsistent for ' + k + ' inferred ' + str(arg_shape_dict[k]) + ' provided ' + str(arg_params[k].shape)
    for k in symbol.list_auxiliary_states():
        assert k in aux_params, k + ' not initialized'
        assert aux_params[k].shape == aux_shape_dict[k], \
            'shape inconsistent for ' + k + ' inferred ' + str(aux_shape_dict[k]) + ' provided ' + str(aux_params[k].shape)

    predictor = Predictor(symbol, DATA_NAMES, LABEL_NAMES, context=ctx,
                          provide_data=DATA_SHAPES, provide_label=LABEL_SHAPES,
                          arg_params=arg_params, aux_params=aux_params)
    return predictor


def generate_batch(im):
    """
    preprocess image, return batch
    :param im: cv2.imread returns [height, width, channel] in BGR
    :return:
    data_batch: MXNet input batch
    data_names: names in data_batch
    im_scale: float number
    """
    im_array, im_scale = resize(im, SHORT_SIDE, LONG_SIDE)
    im_array = transform(im_array, PIXEL_MEANS)
    im_info = np.array([[im_array.shape[2], im_array.shape[3], im_scale]], dtype=np.float32)
    data = [mx.nd.array(im_array), mx.nd.array(im_info)]
    data_shapes = [('data', im_array.shape), ('im_info', im_info.shape)]
    data_batch = mx.io.DataBatch(data=data, label=None, provide_data=data_shapes, provide_label=None)
    return data_batch, DATA_NAMES, im_scale


def demo_net(predictor, image_name, vis=True):
    """
    generate data_batch -> im_detect -> post process
    :param predictor: Predictor
    :param image_name: image name
    :param vis: will save as a new image if not visualized
    :return: None
    """
    BOOL=0
    assert os.path.exists(image_name), image_name + ' not found'
    im = cv2.imread(image_name)
    data_batch, data_names, im_scale = generate_batch(im)
    scores, boxes, data_dict = im_detect(predictor, data_batch, data_names, im_scale)
    all_boxes = [[] for _ in Global.CLASSES]
    for cls in Global.CLASSES:
        cls_ind = Global.CLASSES.index(cls)
        cls_boxes = boxes[:, 4 * cls_ind:4 * (cls_ind + 1)]
        cls_scores = scores[:, cls_ind, np.newaxis]
        keep = np.where(cls_scores >= Global.conf_thresh_value)[0]
        dets = np.hstack((cls_boxes, cls_scores)).astype(np.float32)[keep, :]
        keep = py_nms_wrapper(Global.nms_thresh_value)(dets)
        all_boxes[cls_ind] = dets[keep, :]

    boxes_this_image = [[]] + [all_boxes[j] for j in range(1, len(Global.CLASSES))]

    for ind, boxes in enumerate(boxes_this_image):
        if len(boxes) > 0:
                 BOOL = 1
                 logger.info('---%s---' % Global.CLASSES[ind])
                 logger.info('%s' % boxes)

    result_file = image_name.replace(str(Global.open_img_dir), str(Global.save_path))
    print result_file
    logger.info('results saved to %s' % result_file)
    im, CLASS, SCORE = draw_all_detection(data_dict['data'].asnumpy(), boxes_this_image, Global.CLASSES, im_scale)
    cv2.imwrite(result_file, im)
    Global.PICTURE_INFO[0].append(result_file)
    Global.PICTURE_INFO[1].append(CLASS)
    Global.PICTURE_INFO[2].append(SCORE)
    return CLASS, SCORE, BOOL

def parse_args():
    parser = argparse.ArgumentParser(description='Demonstrate a Faster R-CNN network')
    parser.add_argument('--image', help='custom image', type=str)
    parser.add_argument('--prefix', help='saved model prefix', default='model/e2e',type=str)
    parser.add_argument('--epoch', help='epoch of pretrained model', default=50, type=int)
    parser.add_argument('--gpu', help='GPU device to use', default=0, type=int)
    parser.add_argument('--vis', help='display result', action='store_true')
    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = parse_args()
    ctx = mx.gpu(0)
    if(Global.prefix_value=='model/e2e'):
         symbol = get_resnet_test(num_classes=Global.num_class_value, num_anchors=config.NUM_ANCHORS)
    if(Global.prefix_value=='model/final'):
         symbol = get_vgg_test(num_classes=Global.num_class_value, num_anchors=config.NUM_ANCHORS)
    predictor = get_net(symbol, args.prefix,ctx)
    from glob import glob
    res=glob("/root/mx-rcnn/testimage/bird/*.JPG")
    cnt=0
    for i in res:
        demo_net(predictor, i, False)
        # if cnt>10:
		# break





