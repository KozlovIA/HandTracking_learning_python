from PyQt6 import QtWidgets
from gui import HCapp_ui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QMainWindow()
    ui = HCapp_ui.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    RetCode = app.exec()
    sys.exit(RetCode)

if __name__ == "__main__":
    main()

