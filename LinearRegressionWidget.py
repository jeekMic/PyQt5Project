'''
    【简介】
	PyQt5中 QTabWidget 例子


'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *


class LinearRegressionWidget(QTabWidget):
    def __init__(self, parent=None):
        super(LinearRegressionWidget, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QHBoxLayout()
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl(QFileInfo("./introduction/线性回归/section1.md").absoluteFilePath()))
        layout.addWidget(self.browser)
        self.setTabText(0, "基础介绍")
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        layout.addRow("原理", QLineEdit())
        self.setTabText(1, "实现原理")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        self.setTabText(2, "案例实现")
        self.tab3.setLayout(layout)
