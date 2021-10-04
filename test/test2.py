import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebEngineView(QMainWindow):

    def __init__(self):
        super(WebEngineView, self).__init__()
        # self.wetWindowTitle('打开外部网页例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.jd.com'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':  # 防止别的脚本调用这个
    app = QApplication(sys.argv)  # 传入参数
    main = WebEngineView()  # 创建应用程序类
    main.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入程序主循环
