# *_* coding : UTF-8 *_*

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import os


class pet():
    def __init__(self, width=1400, height=600):
        self.image_key = 1
        self.image_url = 'image/main/deskpet'
        self.image = self.image_url + str(self.image_key) + '.png'
        self.birthplace = (0, 0)
        self.ract_x = width
        self.ract_y = height

    def gif(self):
        if self.image_key < 12:
            self.image_key += 1
        else:
            self.image_key = 1
        self.image = self.image_url + str(self.image_key) + '.png'

class MyLabel(QLabel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # 声明
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 开放右键策略
        self.customContextMenuRequested.connect(self.rightMenuShow)

    # 添加右键菜单
    def rightMenuShow(self, pos):
        menu = QMenu(self)
        menu.addAction(QAction(QIcon('image/browser.png'), '浏览器', self, triggered=self.net))
        menu.addAction(QAction(QIcon('image/music.png'), '秋秋音乐', self, triggered=self.music))
        menu.addAction(QAction(QIcon('image/steam.png'), 'steam', self, triggered=self.steam))
        menu.addAction(QAction(QIcon('image/github.png'), 'github', self, triggered=self.github))
        menu.addAction(QAction(QIcon('image/hide.png'), '隐藏', self, triggered=self.hide))
        menu.addAction(QAction(QIcon('image/exit.png'), '退出', self, triggered=self.quit))
        menu.exec_(QCursor.pos())

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):
        self.setVisible(False)

    def music(self):

        try:
            os.startfile(r'D:\Tencent\qqmusic\QQMusic.exe')
        except:
            print('路径不正确')

    def net(self):
        try:
            os.startfile(r'D:\Google\google explorer\RunningCheeseChrome_2019-09-19\chrome.exe')
        except:
            print('路径不正确')
    def steam(self):
        try:
            os.startfile(r'D:\steam\steam.exe')
        except:
            print('路径不正确')
    def github(self):
        try:
            os.system('"D:\Google\google explorer\RunningCheeseChrome_2019-09-19\chrome.exe" https://github.com/lostinbreezes/lostinbreezes.github.io')
        except:
            print('路径不正确')
class TablePet(QWidget):
    def __init__(self):
        super(TablePet, self).__init__()
        self.pet = pet()

        self.is_follow_mouse = False

        self.initUi()
        self.tray()

        # 每隔一段时间执行
        timer_pet = QTimer(self)
        timer_pet.timeout.connect(self.gem)
        timer_pet.start(2500)

    def gem(self):

        self.pet.gif()
       # self.pm_pet = QPixmap(self.pet.image)
       # self.lb_pet.setPixmap(self.pm_pet)
        pixmap = QtGui.QPixmap(self.pet.image)
        scaredPixmap = pixmap.scaled(400, 400, aspectRatioMode=Qt.KeepAspectRatio)
        self.lb_pet.setPixmap(scaredPixmap)

    #def mouseDoubleClickEvent(self, QMouseEvent):

    def initUi(self):

        ##窗口大小
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, 800, 800)


        ##僵尸标签
        self.lb_pet = MyLabel(self)
        pixmap = QPixmap(self.pet.image)
        scaredPixmap = pixmap.scaled(400, 400, aspectRatioMode=Qt.KeepAspectRatio)
        self.lb_pet.setPixmap(scaredPixmap)
        self.lb_pet.move(self.pet.ract_x, self.pet.ract_y)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.showMaximized()








    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True

            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.pet.ract_x = QCursor.pos().x() - 77
            self.pet.ract_y = QCursor.pos().y() - 63
            self.lb_pet.move(self.pet.ract_x, self.pet.ract_y)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 系统托盘
    def tray(self):
        tray = QSystemTrayIcon(self)
        tray.setIcon(QIcon('image/juan.jpg'))

        display = QAction(QIcon('image/eye.png'), '显示', self, triggered=self.display)
        quit = QAction(QIcon('image/exit.png'), '退出', self, triggered=self.quit)
        menu = QMenu(self)
        menu.addAction(quit)
        menu.addAction(display)
        tray.setContextMenu(menu)
        tray.show()

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):

        self.lb_pet.setVisible(False)

    def display(self):
        self.lb_pet.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = TablePet()
    sys.exit(app.exec_())