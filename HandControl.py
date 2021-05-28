# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HandControl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(771, 546)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"background-color: #696969")
        Dialog.setSizeGripEnabled(False)
        self.Input = QPushButton(Dialog)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(110, 380, 111, 61))
        self.Input.setStyleSheet(u"background-color: #2F4F4F")
        self.OutputCamera = QCheckBox(Dialog)
        self.OutputCamera.setObjectName(u"OutputCamera")
        self.OutputCamera.setGeometry(QRect(110, 120, 101, 21))
        self.OutputCamera.setStyleSheet(u"background-color: #2F4F4F")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Input.setText(QCoreApplication.translate("Dialog", u"Input", None))
        self.OutputCamera.setText(QCoreApplication.translate("Dialog", u"Output camera", None))
    # retranslateUi

