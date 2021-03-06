# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Python Projects\Python GUI Projects\PyQt5 Projects\PyQt5 search app\src\Search_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(594, 561)
        window.setStyleSheet("background-color: #343434;\n"
"")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(190, 20, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.heading_label.setFont(font)
        self.heading_label.setStyleSheet("QLabel\n"
"{\n"
"    color: tomato;\n"
"}")
        self.heading_label.setObjectName("heading_label")
        self.search_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.search_entry.setGeometry(QtCore.QRect(40, 110, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.search_entry.setFont(font)
        self.search_entry.setStyleSheet("QLineEdit\n"
"{\n"
"        border: 2px solid aqua;\n"
"         color: limegreen\n"
"}\n"
"")
        self.search_entry.setObjectName("search_entry")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setEnabled(True)
        self.search_button.setGeometry(QtCore.QRect(390, 110, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setStyleSheet("QPushButton\n"
"{\n"
"    color: cyan\n"
"}")
        self.search_button.setObjectName("search_button")
        self.output_area = QtWidgets.QTextEdit(self.centralwidget)
        self.output_area.setGeometry(QtCore.QRect(40, 190, 511, 321))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.output_area.setFont(font)
        self.output_area.setStyleSheet("QTextEdit\n"
"{\n"
"    background-color: #343434;\n"
"    border: 2px solid aqua;\n"
"    color: hotpink;\n"
"}")
        self.output_area.setAcceptRichText(True)
        self.output_area.setObjectName("output_area")
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Search Here"))
        self.heading_label.setText(_translate("window", "Search App"))
        self.search_entry.setPlaceholderText(_translate("window", "Search here"))
        self.search_button.setToolTip(_translate("window", "Search information"))
        self.search_button.setText(_translate("window", "&Search"))
        self.output_area.setPlaceholderText(_translate("window", "Output will appear here"))
