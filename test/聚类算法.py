# from PyQt5 import QtCore, QtGui, QtWidgets
# from mpl_toolkits.basemap import Basemap
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
# import os
#
# class Ui_MainWindow(QMainWindow, Ui_MainWindow):
#
#     def __init__(self, parent=None):
#         super(Ui_MainWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.graph1 = MyCanvas()
#         self.navi_toolbar = NavigationToolbar(self.graph1, self)
#         self.gridLayout_2.addWidget(self.navi_toolbar, 1, 0, 1, 1)
#         self.gridLayout_2.addWidget(self.graph1, 0, 0, 1, 1)
#         self.plot_point()
#
#     def onclick(self, event):
#         print('test')
#
#     def plot_point(self):
#         self.graph1.figure.clf()
#         self.axes = self.graph1.figure.add_subplot(111)
#         self.x = [0, 10, 20, 30]
#         self.y = [0, 10, 20, 30]
#         self.map = Basemap(resolution = 'l')
#         self.map.drawmapboundary(fill_color='#00BFFF',zorder=1)
#         self.map.fillcontinents(color='#F5D0A9',zorder=2,lake_color='aqua')
#         self.axes.scatter(self.y,self.x, color='#FF0080', s=75, marker="*", zorder=4)
#         self.axes.figure.canvas.mpl_connect(self, 'pick_event', self.onclick)
#
# class MyCanvas(FigureCanvas):
#
#     def __init__(self, *args, **kwargs):
#         self.figure = plt.figure()
#         FigureCanvas.__init__(self, self.figure)
#         self.figure.patch.set_facecolor("None")
#         self.figure.subplots_adjust(left=0.019, bottom=0.035, right=0.99, top=0.964)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     prog = Ui_MainWindow()
#     prog.showMaximized()
#     sys.exit(app.exec_())
import numpy as np
import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5 import QtWidgets
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score

class Widget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # 散点图 这里的211 表示的是2行1列画在第一列
        self.axes = fig.add_subplot(111)
        X, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                          cluster_std=[0.4, 0.2, 0.2, 0.2],
                          random_state=9)
        estimator = KMeans(n_clusters=4, random_state=2)
        print(type(X))
        print(X)
        y_pre = estimator.fit_predict(X)
        print(y_pre)
        # 这里的切面是在数据集里面 X是所有的数据集，lable是标签，也就是后面的0, 1
        self.axes.scatter(X[:, 0], X[:, 1], c=y_pre)
        # 模型评估
        # 用calinski_harabaz_score方法评价聚类效果的好坏大概是类间距除以类内距，因此这个值越大越好
        score = calinski_harabasz_score(X,y_pre)
        print(score)
        self.setWindowTitle("聚类算法")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
