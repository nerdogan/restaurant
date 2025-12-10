#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, QtCore,QtWidgets
from ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


   
            
