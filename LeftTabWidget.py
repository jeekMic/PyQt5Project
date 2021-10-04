#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: hongbiao


from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QListWidget, QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import QSize, Qt

from DecisionTree import DecisionTree
from KnnWidget import KnnWidget
from LinearRegressionWidget import LinearRegressionWidget
from LogicRegressionWidget import LogicRegressionWidget
from tools.Toast import Toast


class LeftTabWidget(QWidget):
    '''左侧选项栏'''
    list_str = ['K-近邻算法', '线性回归', '逻辑回归', '决策树算法']
    url_list = ['job_num_wordcloud.md', 'edu_need.md', 'salary_bar.md', 'edu_salary_bar.md']

    def __init__(self):

        super(LeftTabWidget, self).__init__()
        self.setObjectName('LeftTabWidget')
        self.setWindowTitle('LeftTabWidget')
        with open('./qss/qlist.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.list_style = f.read()

        self.main_layout = QHBoxLayout(self, spacing=0)  # 窗口的整体布局
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.left_widget = QListWidget()  # 左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()

    def setCurrentIndex(self, index):
        Toast(message=self.list_str[index]).show()
        self.right_widget.setCurrentIndex(index)

    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.setCurrentIndex)  # list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)  # 去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for i in range(4):
            self.item = QListWidgetItem(self.list_str[i], self.left_widget)  # 左侧选项的添加
            self.item.setSizeHint(QSize(30, 60))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

            # 右侧用QWebView来显示html网页
            if i == 0:
                self.widget = KnnWidget()
            elif i == 1:
                self.widget = LinearRegressionWidget()
            elif i == 2:
                self.widget = LogicRegressionWidget()
            elif i == 3:
                self.widget = DecisionTree()

            self.right_widget.addWidget(self.widget)
