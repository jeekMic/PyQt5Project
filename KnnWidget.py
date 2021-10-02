'''
    【简介】
	PyQt5中 QTabWidget 例子


'''
from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from widget.WebEngineView import WebEngineView


class KnnWidget(QTabWidget):
    def __init__(self, parent=None):
        super(KnnWidget, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("Tab 例子")

    def tab1UI(self):
        layout = QHBoxLayout()
        self.browser = WebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl(QFileInfo("./introduction/K-近邻算法/section1.html").absoluteFilePath()))
        self.browser.urlChanged.connect(self.changeurl)
        layout.addWidget(self.browser)
        self.setTabText(0, "基础介绍")
        self.tab1.setLayout(layout)

    def changeurl(self,strs):
        print(strs)
    def tab2UI(self):
        layout = QFormLayout()
        lable = QLabel()
        lable.setText("KNN算法的实现原理")
        lable.setWordWrap(True)
        layout.addRow("原理", lable)
        self.setTabText(1, "实现原理")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QFormLayout()
        lable = QLabel()
        lable.setText("KNN算法案例介绍")
        lable.setWordWrap(True)
        layout.addRow("案例介绍", lable)
        self.setTabText(2, "案例实现")
        self.tab3.setLayout(layout)
