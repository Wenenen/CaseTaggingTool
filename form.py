# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.current_query = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.current_query.setFont(font)
        self.current_query.setWordWrap(True)
        self.current_query.setObjectName("current_query")
        self.gridLayout.addWidget(self.current_query, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.case_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.case_title.setFont(font)
        self.case_title.setWordWrap(True)
        self.case_title.setObjectName("case_title")
        self.gridLayout.addWidget(self.case_title, 2, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.case_cause = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.case_cause.setFont(font)
        self.case_cause.setWordWrap(True)
        self.case_cause.setObjectName("case_cause")
        self.gridLayout.addWidget(self.case_cause, 1, 1, 1, 2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.viewpoint = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.viewpoint.setFont(font)
        self.viewpoint.setObjectName("viewpoint")
        self.verticalLayout_2.addWidget(self.viewpoint)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.content = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.content.setFont(font)
        self.content.setObjectName("content")
        self.verticalLayout_3.addWidget(self.content)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.judge = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.judge.setFont(font)
        self.judge.setObjectName("judge")
        self.verticalLayout_3.addWidget(self.judge)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.last_case_view = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.last_case_view.setFont(font)
        self.last_case_view.setWordWrap(True)
        self.last_case_view.setObjectName("last_case_view")
        self.horizontalLayout_2.addWidget(self.last_case_view)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.last_query_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.last_query_btn.setFont(font)
        self.last_query_btn.setObjectName("last_query_btn")
        self.horizontalLayout_4.addWidget(self.last_query_btn)
        self.last_case_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.last_case_btn.setFont(font)
        self.last_case_btn.setObjectName("last_case_btn")
        self.horizontalLayout_4.addWidget(self.last_case_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.yes_btn.setFont(font)
        self.yes_btn.setObjectName("yes_btn")
        self.horizontalLayout.addWidget(self.yes_btn)
        self.soso_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.soso_btn.setFont(font)
        self.soso_btn.setObjectName("soso_btn")
        self.horizontalLayout.addWidget(self.soso_btn)
        self.no_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.no_btn.setFont(font)
        self.no_btn.setObjectName("no_btn")
        self.horizontalLayout.addWidget(self.no_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.select_file_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.select_file_btn.setFont(font)
        self.select_file_btn.setObjectName("select_file_btn")
        self.verticalLayout.addWidget(self.select_file_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 0, 1, 4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.current_index = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.current_index.setFont(font)
        self.current_index.setObjectName("current_index")
        self.horizontalLayout_6.addWidget(self.current_index)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 3, 2, 1)
        self.label_8.raise_()
        self.case_cause.raise_()
        self.label.raise_()
        self.current_query.raise_()
        self.label_7.raise_()
        self.case_title.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.yes_btn.clicked.connect(MainWindow.set_yes)
        self.soso_btn.clicked.connect(MainWindow.set_soso)
        self.no_btn.clicked.connect(MainWindow.set_no)
        self.save_btn.clicked.connect(MainWindow.save)
        self.select_file_btn.clicked.connect(MainWindow.select_file)
        self.last_query_btn.clicked.connect(MainWindow.last_query)
        self.last_case_btn.clicked.connect(MainWindow.last_case)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.current_query.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "当前问题:"))
        self.label_7.setText(_translate("MainWindow", "案件标题:"))
        self.case_title.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "当前案由:"))
        self.case_cause.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "法院观点"))
        self.label_2.setText(_translate("MainWindow", "案件内容"))
        self.label_9.setText(_translate("MainWindow", "法院判决"))
        self.label_5.setText(_translate("MainWindow", "上一个案件:"))
        self.last_case_view.setText(_translate("MainWindow", "TextLabel"))
        self.last_query_btn.setText(_translate("MainWindow", "上一个问题"))
        self.last_case_btn.setText(_translate("MainWindow", "上一个案件(U)"))
        self.yes_btn.setText(_translate("MainWindow", "正确(1)"))
        self.soso_btn.setText(_translate("MainWindow", "相关(2)"))
        self.no_btn.setText(_translate("MainWindow", "错误(3)"))
        self.save_btn.setText(_translate("MainWindow", "保存(S)"))
        self.select_file_btn.setText(_translate("MainWindow", "选择文件"))
        self.label_3.setText(_translate("MainWindow", "当前索引:"))
        self.current_index.setText(_translate("MainWindow", "TextLabel"))

