#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
							 QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
							 QSystemTrayIcon, QMenu, QDialog, QMenuBar, QCheckBox)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QIcon, QColor
import PyQt6.QtGui
import webbrowser
import sys
import applescript
import subprocess
import signal
try:
	from AppKit import NSWorkspace
except ImportError:
	print("can't import AppKit -- maybe you're running python from homebrew?")
	print("try running with /usr/bin/python instead")
	exit(1)


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

BasePath = '/Applications/Daisy.app/Contents/Resources/'
# BasePath = ''  # test

# Create the icon
icon = QIcon(BasePath + "daisy-tray.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action3 = QAction("🌼 Switch on Daisy!")
action3.setCheckable(True)
menu.addAction(action3)

menu.addSeparator()

action7 = QAction("⚙️ Settings")
menu.addAction(action7)

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
btna4 = QAction("&Switch on Daisy!")
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(btna4)


class window_about(QWidget):  # 增加说明页面(About)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息
		self.setUpMainWindow()
		self.resize(400, 410)
		self.center()
		self.setWindowTitle('About')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widg1 = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'daisy.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumWidth(100)
		l1.setMaximumHeight(100)
		l1.setScaledContents(True)
		blay1 = QHBoxLayout()
		blay1.setContentsMargins(0, 0, 0, 0)
		blay1.addStretch()
		blay1.addWidget(l1)
		blay1.addStretch()
		widg1.setLayout(blay1)

		widg2 = QWidget()
		lbl0 = QLabel('Daisy', self)
		font = PyQt6.QtGui.QFont()
		font.setFamily("Arial")
		font.setBold(True)
		font.setPointSize(20)
		lbl0.setFont(font)
		blay2 = QHBoxLayout()
		blay2.setContentsMargins(0, 0, 0, 0)
		blay2.addStretch()
		blay2.addWidget(lbl0)
		blay2.addStretch()
		widg2.setLayout(blay2)

		widg3 = QWidget()
		lbl1 = QLabel('Version 1.0.1 (Pro version)', self)
		blay3 = QHBoxLayout()
		blay3.setContentsMargins(0, 0, 0, 0)
		blay3.addStretch()
		blay3.addWidget(lbl1)
		blay3.addStretch()
		widg3.setLayout(blay3)

		widg4 = QWidget()
		lbl2 = QLabel('Thanks for your love🤟.', self)
		blay4 = QHBoxLayout()
		blay4.setContentsMargins(0, 0, 0, 0)
		blay4.addStretch()
		blay4.addWidget(lbl2)
		blay4.addStretch()
		widg4.setLayout(blay4)

		widg5 = QWidget()
		lbl3 = QLabel('感谢您的喜爱！', self)
		blay5 = QHBoxLayout()
		blay5.setContentsMargins(0, 0, 0, 0)
		blay5.addStretch()
		blay5.addWidget(lbl3)
		blay5.addStretch()
		widg5.setLayout(blay5)

		widg6 = QWidget()
		lbl4 = QLabel('♥‿♥', self)
		blay6 = QHBoxLayout()
		blay6.setContentsMargins(0, 0, 0, 0)
		blay6.addStretch()
		blay6.addWidget(lbl4)
		blay6.addStretch()
		widg6.setLayout(blay6)

		widg7 = QWidget()
		lbl5 = QLabel('※\(^o^)/※', self)
		blay7 = QHBoxLayout()
		blay7.setContentsMargins(0, 0, 0, 0)
		blay7.addStretch()
		blay7.addWidget(lbl5)
		blay7.addStretch()
		widg7.setLayout(blay7)

		widg8 = QWidget()
		bt1 = QPushButton('The Author', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.intro)
		bt2 = QPushButton('Github Page', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.homepage)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg8.setLayout(blay8)

		bt7 = QPushButton('Buy me a cup of coffee☕', self)
		bt7.setMaximumHeight(20)
		bt7.setMinimumWidth(215)
		bt7.clicked.connect(self.coffee)

		widg8_5 = QWidget()
		blay8_5 = QHBoxLayout()
		blay8_5.setContentsMargins(0, 0, 0, 0)
		blay8_5.addStretch()
		blay8_5.addWidget(bt7)
		blay8_5.addStretch()
		widg8_5.setLayout(blay8_5)

		widg9 = QWidget()
		bt3 = QPushButton('🍪\n¥5', self)
		bt3.setMaximumHeight(50)
		bt3.setMinimumHeight(50)
		bt3.setMinimumWidth(50)
		bt3.clicked.connect(self.donate)
		bt4 = QPushButton('🥪\n¥10', self)
		bt4.setMaximumHeight(50)
		bt4.setMinimumHeight(50)
		bt4.setMinimumWidth(50)
		bt4.clicked.connect(self.donate2)
		bt5 = QPushButton('🍜\n¥20', self)
		bt5.setMaximumHeight(50)
		bt5.setMinimumHeight(50)
		bt5.setMinimumWidth(50)
		bt5.clicked.connect(self.donate3)
		bt6 = QPushButton('🍕\n¥50', self)
		bt6.setMaximumHeight(50)
		bt6.setMinimumHeight(50)
		bt6.setMinimumWidth(50)
		bt6.clicked.connect(self.donate4)
		blay9 = QHBoxLayout()
		blay9.setContentsMargins(0, 0, 0, 0)
		blay9.addStretch()
		blay9.addWidget(bt3)
		blay9.addWidget(bt4)
		blay9.addWidget(bt5)
		blay9.addWidget(bt6)
		blay9.addStretch()
		widg9.setLayout(blay9)

		widg10 = QWidget()
		lbl6 = QLabel('© 2023 Ryan-the-hito. All rights reserved.', self)
		blay10 = QHBoxLayout()
		blay10.setContentsMargins(0, 0, 0, 0)
		blay10.addStretch()
		blay10.addWidget(lbl6)
		blay10.addStretch()
		widg10.setLayout(blay10)

		main_h_box = QVBoxLayout()
		main_h_box.addWidget(widg1)
		main_h_box.addWidget(widg2)
		main_h_box.addWidget(widg3)
		main_h_box.addWidget(widg4)
		main_h_box.addWidget(widg5)
		main_h_box.addWidget(widg6)
		main_h_box.addWidget(widg7)
		main_h_box.addWidget(widg8)
		main_h_box.addWidget(widg8_5)
		main_h_box.addWidget(widg9)
		main_h_box.addWidget(widg10)
		main_h_box.addStretch()
		self.setLayout(main_h_box)

	def intro(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Ryan-the-hito')

	def homepage(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Daisy')

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def donate(self):
		dlg = CustomDialog()
		dlg.exec()

	def donate2(self):
		dlg = CustomDialog2()
		dlg.exec()

	def donate3(self):
		dlg = CustomDialog3()
		dlg.exec()

	def donate4(self):
		dlg = CustomDialog4()
		dlg.exec()

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()


class CustomDialog(QDialog):  # (About1)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog2(QDialog):  # (About2)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog3(QDialog):  # (About3)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog4(QDialog):  # (About4)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class window_update(QWidget):  # 增加更新页面（Check for Updates）
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息
		lbl = QLabel('Current Version: 1.0.1', self)
		lbl.move(110, 105)

		lbl0 = QLabel('Check Now:', self)
		lbl0.move(30, 20)

		bt1 = QPushButton('Google Drive', self)
		bt1.setFixedWidth(120)
		bt1.clicked.connect(self.upd)
		bt1.move(110, 15)

		bt3 = QPushButton('Dropbox', self)
		bt3.setFixedWidth(120)
		bt3.clicked.connect(self.upd3)
		bt3.move(110, 45)

		bt2 = QPushButton('Baidu Netdisk', self)
		bt2.setFixedWidth(120)
		bt2.clicked.connect(self.upd2)
		bt2.move(110, 75)

		self.resize(300, 140)
		self.center()
		self.setWindowTitle('Check for Updates')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def upd(self):
		webbrowser.open('https://drive.google.com/drive/folders/17DBRL8753yNgwrxiJk74lZXPtrv-Q9JW?usp=drive_link')

	def upd2(self):
		webbrowser.open('https://pan.baidu.com/s/1rQL9_MWh877b7ZK6Zexnmg?pwd=dfu7')

	def upd3(self):
		webbrowser.open('https://www.dropbox.com/scl/fo/g74g4j79r6w0wnnndvxr5/h?rlkey=bae3tfbv3sfquhbwmamx20ra9&dl=0')

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()


class TimeoutException(Exception):
	pass


class window3(QWidget):  # 主窗口
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.mytimer = QTimer(self)
		self.mytimer.timeout.connect(self.onTimer)

	def timeout_handler(self, signum, frame):
		raise TimeoutException("Timeout")

	def notify(self, CMD, title, text):
		subprocess.call(['osascript', '-e', CMD, title, text])

	def onTimer(self):
		active_app = NSWorkspace.sharedWorkspace().activeApplication()
		if active_app['NSApplicationName'] != 'loginwindow':
			resp = applescript.tell.app("System Events", """set myCommand to "shortcuts run \\"Brightness Alarm\\""
			do shell script myCommand""")
			assert resp.code == 0, resp.err
			Brightness = int(float(resp.out)*100)
			UseShortcut = codecs.open(BasePath + 'CertAction.txt', 'r', encoding='utf-8').read()
			if UseShortcut == '1':
				DarkShort = codecs.open(BasePath + 'DarkTime.txt', 'r', encoding='utf-8').read()
				BrightShort = codecs.open(BasePath + 'BrightTime.txt', 'r', encoding='utf-8').read()
				Low = int(codecs.open(BasePath + 'Low.txt', 'r', encoding='utf-8').read())
				High = int(codecs.open(BasePath + 'High.txt', 'r', encoding='utf-8').read())
				signal.signal(signal.SIGALRM, self.timeout_handler)
				signal.alarm(10)
				if Brightness < Low:
					cmd = """set myCommand to "shortcuts run \\"%s\\""
					do shell script myCommand""" % (DarkShort)
					try:
						subprocess.call(['osascript', '-e', cmd])
					except TimeoutException:
						quitcmd = '''tell application "Shortcuts" to quit'''
						subprocess.call(['osascript', '-e', quitcmd])
						CMD = '''
						on run argv
							display notification (item 2 of argv) with title (item 1 of argv)
						end run'''
						self.notify(CMD, "Daisy: Ambient Light Auto-switcher",
									f"The device seems to be out of reach. Please check the connectivity with Home.")
					except Exception:
						quitcmd = '''tell application "Shortcuts" to quit'''
						subprocess.call(['osascript', '-e', quitcmd])
				if Brightness > High:
					cmd = """set myCommand to "shortcuts run \\"%s\\""
					do shell script myCommand""" % (BrightShort)
					try:
						subprocess.call(['osascript', '-e', cmd])
					except TimeoutException:
						quitcmd = '''tell application "Shortcuts" to quit'''
						subprocess.call(['osascript', '-e', quitcmd])
						CMD = '''
						on run argv
							display notification (item 2 of argv) with title (item 1 of argv)
						end run'''
						self.notify(CMD, "Daisy: Ambient Light Auto-switcher",
									f"The device seems to be out of reach. Please check the connectivity with Home.")
					except Exception:
						quitcmd = '''tell application "Shortcuts" to quit'''
						subprocess.call(['osascript', '-e', quitcmd])
				signal.alarm(0)

	def activate(self):  # 设置窗口显示
		if action3.isChecked():
			SetTime = int(codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read())
			self.mytimer.start(1000*SetTime)
		if not action3.isChecked():
			self.mytimer.stop()

	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()

	def cancel(self):  # 设置取消键的功能
		self.close()


class window4(QWidget):  # Customization settings
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 设置窗口内布局
		self.setUpMainWindow()
		self.setFixedSize(500, 210)
		self.center()
		self.setWindowTitle('Customization settings')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		self.lbl1 = QLabel('Detect ambient light every (seconds): ', self)

		self.le1 = QLineEdit(self)
		self.le1.setPlaceholderText('Seconds. Numbers only, no decimal. Default=30')
		text = codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read()
		self.le1.setText(text)

		self.lbl6 = QLabel('Customize range: Too dark  <', self)
		self.le4 = QLineEdit(self)
		self.le4.setPlaceholderText('20')
		Low = codecs.open(BasePath + 'Low.txt', 'r', encoding='utf-8').read()
		self.le4.setText(Low)
		self.lbl7 = QLabel('~ Good ~', self)
		self.le5 = QLineEdit(self)
		self.le5.setPlaceholderText('90')
		High = codecs.open(BasePath + 'High.txt', 'r', encoding='utf-8').read()
		self.le5.setText(High)
		self.lbl8 = QLabel('<  Too bright', self)

		self.checkBox1 = QCheckBox('Run Shortcuts when too dark or too bright:', self)
		LastCert = codecs.open(BasePath + "CertAction.txt", 'r', encoding='utf-8').read()
		if LastCert == '1':
			self.checkBox1.setChecked(True)
		if LastCert == '0':
			self.checkBox1.setChecked(False)
		self.checkBox1.clicked.connect(self.CertAction)

		self.lbl4 = QLabel('   ', self)
		self.lbl2 = QLabel('When it is too dark: ', self)
		self.le2 = QLineEdit(self)
		self.le2.setPlaceholderText('The name of Shortcuts you use when dark')
		text2 = codecs.open(BasePath + 'DarkTime.txt', 'r', encoding='utf-8').read()
		self.le2.setText(text2)

		self.lbl5 = QLabel('   ', self)
		self.lbl3 = QLabel('When it is too bright: ', self)
		self.le3 = QLineEdit(self)
		self.le3.setPlaceholderText('The name of Shortcuts you use when bright')
		text3 = codecs.open(BasePath + 'BrightTime.txt', 'r', encoding='utf-8').read()
		self.le3.setText(text3)

		self.btn_1 = QPushButton('Save', self)
		self.btn_1.clicked.connect(self.SetTime)
		self.btn_1.setFixedSize(150, 20)
		
		qw1 = QWidget()
		vbox1 = QHBoxLayout()
		vbox1.setContentsMargins(0, 0, 0, 0)
		vbox1.addStretch()
		vbox1.addWidget(self.btn_1)
		vbox1.addStretch()
		qw1.setLayout(vbox1)

		qw3 = QWidget()
		vbox3 = QHBoxLayout()
		vbox3.setContentsMargins(0, 0, 0, 0)
		vbox3.addWidget(self.lbl4)
		vbox3.addWidget(self.lbl2)
		vbox3.addWidget(self.le2)
		qw3.setLayout(vbox3)

		qw4 = QWidget()
		vbox4 = QHBoxLayout()
		vbox4.setContentsMargins(0, 0, 0, 0)
		vbox4.addWidget(self.lbl5)
		vbox4.addWidget(self.lbl3)
		vbox4.addWidget(self.le3)
		qw4.setLayout(vbox4)

		qw5 = QWidget()
		vbox5 = QHBoxLayout()
		vbox5.setContentsMargins(0, 0, 0, 0)
		vbox5.addWidget(self.lbl1)
		vbox5.addWidget(self.le1)
		qw5.setLayout(vbox5)

		qw6 = QWidget()
		vbox6 = QHBoxLayout()
		vbox6.setContentsMargins(0, 0, 0, 0)
		vbox6.addWidget(self.lbl6)
		vbox6.addWidget(self.le4)
		vbox6.addWidget(self.lbl7)
		vbox6.addWidget(self.le5)
		vbox6.addWidget(self.lbl8)
		qw6.setLayout(vbox6)

		vbox2 = QVBoxLayout()
		vbox2.setContentsMargins(20, 20, 20, 20)
		vbox2.addWidget(qw5)
		vbox2.addWidget(qw6)
		vbox2.addStretch()
		vbox2.addWidget(self.checkBox1)
		vbox2.addWidget(qw3)
		vbox2.addWidget(qw4)
		vbox2.addWidget(qw1)
		self.setLayout(vbox2)
	
	def SetTime(self):
		if self.le1.text() != '' and self.le1.text() != '0':
			SetTime = str(int(self.le1.text()))
			with open(BasePath + "SetTime.txt", 'w', encoding='utf-8') as f0:
				f0.write(SetTime)
		if self.le2.text() != '':
			DarkTime = str(self.le2.text())
			with open(BasePath + "DarkTime.txt", 'w', encoding='utf-8') as f0:
				f0.write(DarkTime)
		if self.le3.text() != '':
			BrightTime = str(self.le3.text())
			with open(BasePath + "BrightTime.txt", 'w', encoding='utf-8') as f0:
				f0.write(BrightTime)
		if self.le4.text() != '':
			Low = str(self.le4.text())
			with open(BasePath + "Low.txt", 'w', encoding='utf-8') as f0:
				f0.write(Low)
		if self.le5.text() != '':
			High = str(self.le5.text())
			with open(BasePath + "High.txt", 'w', encoding='utf-8') as f0:
				f0.write(High)
		self.close()

	def CertAction(self):
		if self.checkBox1.isChecked():
			with open(BasePath + "CertAction.txt", 'w', encoding='utf-8') as f0:
				f0.write('1')
		if not self.checkBox1.isChecked():
			with open(BasePath + "CertAction.txt", 'w', encoding='utf-8') as f0:
				f0.write('0')
	
	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()
	
	def activate(self):  # 设置窗口显示
		text = codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read()
		self.le1.setText(text)
		text2 = codecs.open(BasePath + 'DarkTime.txt', 'r', encoding='utf-8').read()
		self.le2.setText(text2)
		text3 = codecs.open(BasePath + 'BrightTime.txt', 'r', encoding='utf-8').read()
		self.le3.setText(text3)
		Low = codecs.open(BasePath + 'Low.txt', 'r', encoding='utf-8').read()
		self.le4.setText(Low)
		High = codecs.open(BasePath + 'High.txt', 'r', encoding='utf-8').read()
		self.le5.setText(High)
		LastCert = codecs.open(BasePath + "CertAction.txt", 'r', encoding='utf-8').read()
		if LastCert == '1':
			self.checkBox1.setChecked(True)
		if LastCert == '0':
			self.checkBox1.setChecked(False)

		self.show()
		self.setFocus()
		self.raise_()
		self.activateWindow()
	
	def cancel(self):  # 设置取消键的功能
		self.close()

style_sheet_ori = '''
	QTabWidget::pane {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QTableWidget{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #FFFFFF;
		color: #000000;
		font: 14pt Helvetica;
}
	QWidget#Main {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QPushButton{
		border: 1px outset grey;
		background-color: #FFFFFF;
		border-radius: 4px;
		padding: 1px;
		color: #000000
}
	QPushButton:pressed{
		border: 1px outset grey;
		background-color: #0085FF;
		border-radius: 4px;
		padding: 1px;
		color: #FFFFFF
}
	QPlainTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QPlainTextEdit#edit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #FFFFFF;
		color: rgb(113, 113, 113);
		font: 14pt Helvetica;
}
	QTableWidget#small{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QLineEdit{
		border-radius:4px;
		border: 1px solid gray;
		background-color: #FFFFFF;
}
	QTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QListWidget{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
'''

if __name__ == '__main__':
	w1 = window_about()  # about
	w2 = window_update()  # update
	w3 = window3()  # main1
	w3.setAutoFillBackground(True)
	p = w3.palette()
	p.setColor(w3.backgroundRole(), QColor('#ECECEC'))
	w3.setPalette(p)
	w4 = window4()  # CUSTOMIZING
	action1.triggered.connect(w1.activate)
	action2.triggered.connect(w2.activate)
	action3.triggered.connect(w3.activate)
	action7.triggered.connect(w4.activate)
	btna4.triggered.connect(w3.activate)
	app.setStyleSheet(style_sheet_ori)
	app.exec()
