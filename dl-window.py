# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Original.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import time
import Global
import mxnet as mx
from rcnn.config import config
from rcnn.symbol import get_resnet_test, get_vgg_test
from glob import  glob

from result import  get_net,demo_net,parse_args

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import  *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1547, 880)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QtCore.QSize(1000, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 80, 1051, 681))
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(0, 50, 171, 31))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 760, 380, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pre_img = QtGui.QPushButton(self.layoutWidget)
        self.pre_img.setObjectName(_fromUtf8("pre_img"))
        self.horizontalLayout.addWidget(self.pre_img)
        self.label_view = QtGui.QPushButton(self.layoutWidget)
        self.label_view.setObjectName(_fromUtf8("label_view"))
        self.horizontalLayout.addWidget(self.label_view)
        self.next_img = QtGui.QPushButton(self.layoutWidget)
        self.next_img.setObjectName(_fromUtf8("next_img"))
        self.horizontalLayout.addWidget(self.next_img)
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 50, 1051, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1220, 100, 101, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1270, 760, 221, 61))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.train_2 = QtGui.QPushButton(self.layoutWidget1)
        self.train_2.setObjectName(_fromUtf8("train_2"))
        self.horizontalLayout_2.addWidget(self.train_2)
        self.train = QtGui.QPushButton(self.layoutWidget1)
        self.train.setObjectName(_fromUtf8("train"))
        self.horizontalLayout_2.addWidget(self.train)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 90, 171, 671))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setBaseSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 153, 1248))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_42 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_42.setObjectName(_fromUtf8("verticalLayout_42"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_42.addWidget(self.label_2)
        self.label_43 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.verticalLayout_42.addWidget(self.label_43)
        self.label_44 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.verticalLayout_42.addWidget(self.label_44)
        self.lineEdit1_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit1_4.setObjectName(_fromUtf8("lineEdit1_4"))
        self.verticalLayout_42.addWidget(self.lineEdit1_4)
        self.label_45 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.verticalLayout_42.addWidget(self.label_45)
        self.lineEdit2_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit2_4.setObjectName(_fromUtf8("lineEdit2_4"))
        self.verticalLayout_42.addWidget(self.lineEdit2_4)
        self.label_46 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.verticalLayout_42.addWidget(self.label_46)
        self.lineEdit3_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit3_4.setObjectName(_fromUtf8("lineEdit3_4"))
        self.verticalLayout_42.addWidget(self.lineEdit3_4)
        self.label_47 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.verticalLayout_42.addWidget(self.label_47)
        self.lineEdit4_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit4_4.setObjectName(_fromUtf8("lineEdit4_4"))
        self.verticalLayout_42.addWidget(self.lineEdit4_4)
        self.label_48 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.verticalLayout_42.addWidget(self.label_48)
        self.lineEdit5_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit5_4.setObjectName(_fromUtf8("lineEdit5_4"))
        self.verticalLayout_42.addWidget(self.lineEdit5_4)
        self.label_49 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.verticalLayout_42.addWidget(self.label_49)
        self.lineEdit6_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit6_4.setObjectName(_fromUtf8("lineEdit6_4"))
        self.verticalLayout_42.addWidget(self.lineEdit6_4)
        self.label_50 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.verticalLayout_42.addWidget(self.label_50)
        self.lineEdit7_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit7_4.setObjectName(_fromUtf8("lineEdit7_4"))
        self.verticalLayout_42.addWidget(self.lineEdit7_4)
        self.label_51 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.verticalLayout_42.addWidget(self.label_51)
        self.lineEdit8_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit8_4.setObjectName(_fromUtf8("lineEdit8_4"))
        self.verticalLayout_42.addWidget(self.lineEdit8_4)
        self.label_52 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.verticalLayout_42.addWidget(self.label_52)
        self.lineEdit9_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit9_4.setObjectName(_fromUtf8("lineEdit9_4"))
        self.verticalLayout_42.addWidget(self.lineEdit9_4)
        self.label_54 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.verticalLayout_42.addWidget(self.label_54)
        self.lineEdit10_5 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_5.setObjectName(_fromUtf8("lineEdit10_5"))
        self.verticalLayout_42.addWidget(self.lineEdit10_5)
        self.label_55 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.verticalLayout_42.addWidget(self.label_55)
        self.lineEdit10_6 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_6.setObjectName(_fromUtf8("lineEdit10_6"))
        self.verticalLayout_42.addWidget(self.lineEdit10_6)
        self.label_60 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.verticalLayout_42.addWidget(self.label_60)
        self.lineEdit10_11 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_11.setObjectName(_fromUtf8("lineEdit10_11"))
        self.verticalLayout_42.addWidget(self.lineEdit10_11)
        self.label_59 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.verticalLayout_42.addWidget(self.label_59)
        self.lineEdit10_10 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_10.setObjectName(_fromUtf8("lineEdit10_10"))
        self.verticalLayout_42.addWidget(self.lineEdit10_10)
        self.label_58 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.verticalLayout_42.addWidget(self.label_58)
        self.lineEdit10_9 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_9.setObjectName(_fromUtf8("lineEdit10_9"))
        self.verticalLayout_42.addWidget(self.lineEdit10_9)
        self.label_57 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.verticalLayout_42.addWidget(self.label_57)
        self.lineEdit10_8 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_8.setObjectName(_fromUtf8("lineEdit10_8"))
        self.verticalLayout_42.addWidget(self.lineEdit10_8)
        self.label_53 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.verticalLayout_42.addWidget(self.label_53)
        self.lineEdit10_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_4.setObjectName(_fromUtf8("lineEdit10_4"))
        self.verticalLayout_42.addWidget(self.lineEdit10_4)
        self.label_56 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.verticalLayout_42.addWidget(self.label_56)
        self.lineEdit10_7 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_7.setObjectName(_fromUtf8("lineEdit10_7"))
        self.verticalLayout_42.addWidget(self.lineEdit10_7)
        self.label_61 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.verticalLayout_42.addWidget(self.label_61)
        self.lineEdit10_12 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_12.setObjectName(_fromUtf8("lineEdit10_12"))
        self.verticalLayout_42.addWidget(self.lineEdit10_12)
        self.label_62 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.verticalLayout_42.addWidget(self.label_62)
        self.lineEdit10_13 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit10_13.setObjectName(_fromUtf8("lineEdit10_13"))
        self.verticalLayout_42.addWidget(self.lineEdit10_13)
        self.label_43.raise_()
        self.lineEdit1_4.raise_()
        self.label_45.raise_()
        self.lineEdit2_4.raise_()
        self.label_46.raise_()
        self.lineEdit3_4.raise_()
        self.label_47.raise_()
        self.lineEdit4_4.raise_()
        self.label_48.raise_()
        self.lineEdit5_4.raise_()
        self.label_49.raise_()
        self.lineEdit6_4.raise_()
        self.label_50.raise_()
        self.lineEdit7_4.raise_()
        self.label_51.raise_()
        self.lineEdit8_4.raise_()
        self.label_52.raise_()
        self.lineEdit9_4.raise_()
        self.label_54.raise_()
        self.lineEdit10_5.raise_()
        self.label_55.raise_()
        self.lineEdit10_6.raise_()
        self.label_60.raise_()
        self.lineEdit10_11.raise_()
        self.label_59.raise_()
        self.lineEdit10_10.raise_()
        self.label_58.raise_()
        self.lineEdit10_9.raise_()
        self.label_57.raise_()
        self.lineEdit10_8.raise_()
        self.label_53.raise_()
        self.lineEdit10_4.raise_()
        self.label_2.raise_()
        self.label_44.raise_()
        self.lineEdit10_7.raise_()
        self.label_56.raise_()
        self.lineEdit10_12.raise_()
        self.label_61.raise_()
        self.lineEdit10_13.raise_()
        self.label_62.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(1220, 130, 321, 141))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_9 = QtGui.QLabel(self.layoutWidget2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_8 = QtGui.QLabel(self.layoutWidget2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_5.addWidget(self.label_8)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1220, 610, 321, 151))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1220, 280, 67, 23))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1220, 310, 321, 301))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_3.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.toolButton.raise_()
        self.textBrowser_3.raise_()
        self.label_4.raise_()
        self.scrollArea.raise_()
        self.textBrowser_2.raise_()


        self.retranslateUi(MainWindow)
        #打开按钮
        QtCore.QObject.connect(self.train_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.train_path)
        #识别按钮
        QtCore.QObject.connect(self.train, QtCore.SIGNAL(_fromUtf8("clicked()")), self.test_ResNet)
        #图像浏览按钮
        QtCore.QObject.connect(self.label_view, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.showDialog)
        #下一张
        QtCore.QObject.connect(self.next_img, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.nextImg)
        #上一张
        QtCore.QObject.connect(self.pre_img, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.preImg)
        # #类别选取
        # QtCore.QObject.connect(self.checkBox_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Classier)
        #识别结果路径保存
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.savePath)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
            self.label.setText(_translate("MainWindow", "image_show", None))
            self.toolButton.setText(_translate("MainWindow", "识别结果保存路径", None))
            self.pre_img.setText(_translate("MainWindow", "上一张", None))
            self.label_view.setText(_translate("MainWindow", "图片浏览", None))
            self.next_img.setText(_translate("MainWindow", "下一张", None))
            self.textBrowser_3.setHtml(_translate("MainWindow",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                  None))
            self.label_4.setText(_translate("MainWindow", "参数设置：", None))
            self.train_2.setText(_translate("MainWindow", "打开", None))
            self.train.setText(_translate("MainWindow", "识别", None))
            self.label_2.setText(_translate("MainWindow", "类别选取：", None))
            self.label_43.setText(_translate("MainWindow", "类别1：background", None))
            self.label_44.setText(_translate("MainWindow", "类别2:", None))
            self.lineEdit1_4.setText(_translate("MainWindow", "bird_nest", None))
            self.label_45.setText(_translate("MainWindow", "类别3:", None))
            self.lineEdit2_4.setText(_translate("MainWindow", "good_circle1", None))
            self.label_46.setText(_translate("MainWindow", "类别4:", None))
            self.lineEdit3_4.setText(_translate("MainWindow", "bad_circle1", None))
            self.label_47.setText(_translate("MainWindow", "类别5:", None))
            self.lineEdit4_4.setText(_translate("MainWindow", "good_circle2", None))
            self.label_48.setText(_translate("MainWindow", "类别6:", None))
            self.lineEdit5_4.setText(_translate("MainWindow", "good_earthquake_hammer", None))
            self.label_49.setText(_translate("MainWindow", "类别7:", None))
            self.lineEdit6_4.setText(_translate("MainWindow", "bad_earthquake_hammer", None))
            self.label_50.setText(_translate("MainWindow", "类别8:", None))
            self.lineEdit7_4.setText(_translate("MainWindow", "spacer_bar", None))
            self.label_51.setText(_translate("MainWindow", "类别9:", None))
            self.lineEdit8_4.setText(_translate("MainWindow", "9", None))
            self.label_52.setText(_translate("MainWindow", "类别10:", None))
            self.lineEdit9_4.setText(_translate("MainWindow", "10", None))
            self.label_54.setText(_translate("MainWindow", "类别11:", None))
            self.lineEdit10_5.setText(_translate("MainWindow", "11", None))
            self.label_55.setText(_translate("MainWindow", "类别12:", None))
            self.lineEdit10_6.setText(_translate("MainWindow", "12", None))
            self.label_60.setText(_translate("MainWindow", "类别13:", None))
            self.lineEdit10_11.setText(_translate("MainWindow", "13", None))
            self.label_59.setText(_translate("MainWindow", "类别14:", None))
            self.lineEdit10_10.setText(_translate("MainWindow", "14", None))
            self.label_58.setText(_translate("MainWindow", "类别15:", None))
            self.lineEdit10_9.setText(_translate("MainWindow", "15", None))
            self.label_57.setText(_translate("MainWindow", "类别16:", None))
            self.lineEdit10_8.setText(_translate("MainWindow", "16", None))
            self.label_53.setText(_translate("MainWindow", "类别17:", None))
            self.lineEdit10_4.setText(_translate("MainWindow", "17", None))
            self.label_56.setText(_translate("MainWindow", "类别18:", None))
            self.lineEdit10_7.setText(_translate("MainWindow", "18", None))
            self.label_61.setText(_translate("MainWindow", "类别19:", None))
            self.lineEdit10_12.setText(_translate("MainWindow", "19", None))
            self.label_62.setText(_translate("MainWindow", "类别20:", None))
            self.lineEdit10_13.setText(_translate("MainWindow", "20", None))
            self.label_5.setText(_translate("MainWindow", "prefix:", None))
            self.lineEdit.setText(_translate("MainWindow", "model/e2e", None))
            self.label_9.setText(_translate("MainWindow", "num_classes:", None))
            self.lineEdit_5.setText(_translate("MainWindow", "8", None))
            self.label_7.setText(_translate("MainWindow", "conf_thresh:", None))
            self.lineEdit_3.setText(_translate("MainWindow", "0.7", None))
            self.label_8.setText(_translate("MainWindow", "nms_thresh:", None))
            self.lineEdit_4.setText(_translate("MainWindow", "0.3", None))
            self.textBrowser_2.setHtml(_translate("MainWindow",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>",
                                                  None))
            self.label_3.setText(_translate("MainWindow", "日志信息：", None))
            self.textBrowser.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                None))

    #类别选取
    def classier(self,num_classes):

          classes=['__background__', self.lineEdit1_4.text(), self.lineEdit2_4.text(), self.lineEdit3_4.text(),
                          self.lineEdit4_4.text(), self.lineEdit5_4.text(), self.lineEdit6_4.text(), self.lineEdit7_4.text(),
                          self.lineEdit8_4.text(), self.lineEdit9_4.text(), self.lineEdit10_5.text(), self.lineEdit10_6.text(),
                          self.lineEdit10_11.text(), self.lineEdit10_10.text(), self.lineEdit10_9.text(), self.lineEdit10_8.text(),
                          self.lineEdit10_4.text(), self.lineEdit10_7.text(), self.lineEdit10_12.text(), self.lineEdit10_13.text()
                    ]
          Global.CLASSES=classes[0:num_classes]
          self.textBrowser.append(_fromUtf8("识别的类别名称如下："))
          for i in Global.CLASSES:
               self.textBrowser.append(_fromUtf8(i))

    # 打开对话框
    def openDialog(self):
              tmpDir = QtGui.QFileDialog.getExistingDirectory()
              tmpDir_1= unicode(tmpDir, sys.getfilesystemencoding())
              return tmpDir_1


    # 图片保存路径
    def savePath(self):
              self.textBrowser_3.setText("")
              if Global.save_path != "":
                  Global.save_path = ""
              Global.save_path = self.openDialog()
              self.textBrowser_3.append(Global.save_path)
              return Global.save_path

    # 图片浏览功能
    def showDialog(self):
            Global.index=0
            if len(Global.path)>0:
               Global.path=[]
            path=self.openDialog()
            picture_jpg = path+"/*.jpg"
            picture_JPG = path + "/*.JPG"
            picture_png = path + "/*.png"
            ImgPath=glob(str(picture_jpg))+glob(str(picture_JPG))+glob(str(picture_png))
            for i in ImgPath:
                Global.path.append(i)
            self.showImg(Global.path[Global.index])


    #显示图片
    def showImg(self,img_path):
          self.textBrowser_2.setText("")
          img = QtGui.QPixmap(_fromUtf8(img_path)).scaled(self.label.width(),self.label.height())
          self.label.setPixmap(QPixmap(img))
          if img_path in Global.PICTURE_INFO[0] :
             for index,path in enumerate(Global.PICTURE_INFO[0]):
                 if path == img_path:
                    self.textBrowser_2.append("当前图片路径为:"+_fromUtf8(img_path))
                    self.textBrowser_2.append("类别信息："+Global.PICTURE_INFO[1][index])
                    self.textBrowser_2.append("置信率：" +Global.PICTURE_INFO[2][index])
          else:
              self.textBrowser_2.append("当前图片路径为:"+img_path)
    #下一张
    def nextImg(self):
        if(Global.index<len(Global.path)-1):
              Global.index=Global.index + 1
        else:
              Global.index=0
        self.showImg(Global.path[Global.index])

    #上一张
    def preImg(self):
          if(Global.index>0):
            Global.index = Global.index - 1
          else:
            Global.index = len(Global.path)-1
          self.showImg(Global.path[Global.index])


    #配置信息
    def configInfo(self):
          Global.prefix_value=self.lineEdit.text()
          Global.conf_thresh_value=float(self.lineEdit_3.text())
          Global.nms_thresh_value=float(self.lineEdit_4.text())
          Global.num_class_value=int(self.lineEdit_5.text())

    # 打开按钮
    def train_path(self):
        Global.open_img_dir = self.openDialog()
        Global.img_dir_jpg = Global.open_img_dir + "/*.jpg"
        Global.img_dir_JPG = Global.open_img_dir + "/*.JPG"
        Global.img_dir_png = Global.open_img_dir + "/*.png"

    #识别按钮
    def test_ResNet(self):
           args = parse_args()
           self.configInfo()
           Global.index = 0
           Global.PICTURE_INFO=[[],[],[]]
           if len(Global.path) > 0:
                  Global.path = []
           #获取jpg、JPG、png格式的图片
           res = glob(unicode(Global.img_dir_jpg)) + glob(unicode(Global.img_dir_JPG))+ glob(unicode(Global.img_dir_png))
           #清空日志和图片保存栏中上一次的信息
           self.textBrowser_3.setText("")
           self.textBrowser.setText("")
           #获取识别的类别数
           self.classier(Global.num_class_value)
           #设置识别结果保存路径
           self.textBrowser_3.append(Global.save_path)
           self.textBrowser.append('\n')
           count=0
           counter=0
           ctx = mx.gpu(0)
           Global.prefix=Global.prefix_value[0:9]
           print Global.prefix
           # if (Global.prefix == 'model/e2e'):
           symbol = get_resnet_test(num_classes=Global.num_class_value, num_anchors=config.NUM_ANCHORS)
           # if ( Global.prefix == 'model/final'):
           #     symbol = get_vgg_test(num_classes=Global.num_class_value, num_anchors=config.NUM_ANCHORS)
           predictor = get_net(symbol, str(Global.prefix_value),ctx)
           for i in res:
              count = count + 1
              CLASS,SCORE,BOOL=demo_net(predictor, i, args.vis)
              if (BOOL == 1):
                  counter = counter + 1
              info_class="类别信息："+str(CLASS)
              info_score="置信率："+str(SCORE)
              info_img_path="图片路径："+str(i)
              self.textBrowser.append(_fromUtf8(info_class) )
              self.textBrowser.append(_fromUtf8(info_score) )
              self.textBrowser.append(_fromUtf8(info_img_path))
              self.textBrowser.append('\n')
           self.textBrowser.append(_fromUtf8("识别成功数量是：" + str(counter)))
           self.textBrowser.append(_fromUtf8("识别总数量是："+str(count)))
           self.textBrowser.append('map is ' + str(float(counter) / float(count)))
           picture_jpg = Global.save_path + "/*.jpg"
           picture_JPG = Global.save_path + "/*.JPG"
           picture_png = Global.save_path + "/*.png"
           ImgPath = glob(str(picture_jpg))+glob(str(picture_JPG))+glob(str(picture_png))
           for i in ImgPath:
               Global.path.append(i)
           self.showImg(Global.path[Global.index])


if __name__ == "__main__":
    import sys
    codec = QTextCodec.codecForName("utf8")
    QTextCodec.setCodecForLocale(codec)
    QTextCodec.setCodecForCStrings(codec)
    QTextCodec.setCodecForTr(codec)
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())