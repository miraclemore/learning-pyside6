# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    app = QApplication()

    # window = QMainWindow()
    window = QWidget()

    window.setWindowTitle("Learning PySide6")

    window.show()

    sys.exit(app.exec())
