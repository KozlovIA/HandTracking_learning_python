# from HandControl import Ui_Dialog
from PySide2 import QtGui
from PySide2.QtCore import Qt
import cv2
import time
import numpy as np
import math
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import VolumeHandControlModule as vhc
import sys
import PySide2

# vol = vhc.VolumeHandControl()
# vol.VoulumeControl(False)

#if __name__ == "main":
#    app = QtGui.QGuiApplication(sys.argv)
#    Form = QtGui.QWindow()
#    ui = Ui_Dialog()
#    ui.setupUi(Form)
#    Form.show()
#    sys.exit(app.exec_())


# from PyQt5 import QtWidgets, uic
from PyQt6 import QtWidgets, uic

# app = QtWidgets.QApplication([])

# form = uic.loadUi("C:\PyProject\Create_application\HCtest.ui")

# form.show()

# app.exec()

from gui import HCapp_ui
app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
ui = HCapp_ui.Ui_MainWindow()
# ui.setupUi(main_window)
main_window.show()

RetCode = app.exec()
sys.exit(RetCode)
