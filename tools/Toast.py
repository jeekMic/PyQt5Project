# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt


class Toast(QWidget):
    style = '''
#lb_message{
    color:#f7faff;
    font-family:Microsoft YaHei;
}
    '''

    def __init__(self, message='hello', state=0, msc=3000, parent=None):
        super(Toast, self).__init__(parent)

        # 除了成功之外其他消息图标一律使用错误图标（有局限性：成功的具体信息有很多种，但这里没办法区分，待改）
        if state != 0:
            self.iconPath = ':/icon/error.png'
        else:
            self.iconPath = ':/icon/success.png'
        self.message = message  # 需要显示的消息

        self.msc = msc  # 窗口显示时长
        self.timer = QTimer()
        # 由于不知道动画结束的事件，所以借助QTimer来关闭窗口，动画结束就关闭窗口，所以这里的事件要和动画时间一样
        self.timer.singleShot(self.msc, self.close)  # singleShot表示timer只会启动一次

        self.setUpUi()
        self.createAnimation()

    def setUpUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)  # 这样就不会在任务栏上显示
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        self.setObjectName('Toast')
        self.setMinimumSize(QSize(220, 100))
        self.setMaximumSize(QSize(220, 180))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_icon = QLabel()
        self.lb_icon.setText("")
        self.lb_icon.setObjectName("lb_icon")
        self.lb_icon.setPixmap(QPixmap(self.iconPath))
        self.horizontalLayout.addWidget(self.lb_icon)
        self.lb_message = QLabel(self)
        '''实现QLabel自动换行'''
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_message.sizePolicy().hasHeightForWidth())
        self.lb_message.setSizePolicy(sizePolicy)
        self.lb_message.setWordWrap(True)
        self.lb_message.setText(self.message)
        self.lb_message.setTextFormat(Qt.AutoText)
        self.lb_message.setScaledContents(True)
        self.lb_message.setObjectName("lb_message")
        self.lb_message.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.lb_message)

        self.setStyleSheet(self.style)

        self.center()

    def paintEvent(self, a0: QPaintEvent):
        qp = QPainter()
        qp.begin(self)  # 不能掉，不然没效果
        qp.setRenderHints(QPainter.Antialiasing, True)  # 抗锯齿
        qp.setBrush(QBrush(Qt.black))
        qp.setPen(Qt.transparent)
        rect = self.rect()
        rect.setWidth(rect.width() - 1)
        rect.setHeight(rect.height() - 1)
        qp.drawRoundedRect(rect, 15, 15)
        qp.end()

    def createAnimation(self):
        # 1.定义一个动画
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setTargetObject(self)
        # self.animation.setPropertyName(b"windowOpacity")
        # 2.设置属性值
        self.animation.setStartValue(0)
        self.animation.setKeyValueAt(0.2, 0.7)  # 设置插值0.3 表示单本次动画时间的0.3处的时间点
        self.animation.setKeyValueAt(0.8, 0.7)  # 设置插值0.8 表示单本次动画时间的0.3处的时间点
        self.animation.setEndValue(0)
        # 3.设置时长
        self.animation.setDuration(self.msc)
        # 4.启动动画
        self.animation.start()

    def center(self):
        if self.parent() is not None:
            xPos = int((self.parent().width() - self.width()) / 2)
            yPos = int((self.parent().height() - self.height()) / 2 + 40)
            self.move(xPos, yPos)
        else:
            # 屏幕居中
            screen = QDesktopWidget().screenGeometry()
            size = self.geometry()
            self.move(int((screen.width() - size.width()) / 2),
                      int((screen.height() - size.height()) / 2) + 40)


