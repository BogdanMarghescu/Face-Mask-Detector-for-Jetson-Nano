# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_cam_menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_cam_menu(object):
    def setupUi(self, new_cam_menu):
        new_cam_menu.setObjectName("new_cam_menu")
        new_cam_menu.setWindowModality(QtCore.Qt.ApplicationModal)
        new_cam_menu.resize(610, 310)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(new_cam_menu.sizePolicy().hasHeightForWidth())
        new_cam_menu.setSizePolicy(sizePolicy)
        new_cam_menu.setStyleSheet("background-color: rgb(5, 23, 47);")
        self.formLayoutWidget = QtWidgets.QWidget(new_cam_menu)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 571, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(50)
        self.formLayout.setObjectName("formLayout")
        self.camera_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.camera_name_label.setFont(font)
        self.camera_name_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_name_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: #228B22;\n"
"font: 24pt \"Gill Sans MT\";")
        self.camera_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.camera_name_label.setObjectName("camera_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.camera_name_label)
        self.cam_name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        self.cam_name_input.setFont(font)
        self.cam_name_input.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cam_name_input.setAutoFillBackground(False)
        self.cam_name_input.setStyleSheet("QLineEdit:focus{ border-color:#66afe9;}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(21, 138, 8);\n"
"    background-color: rgb(25, 35, 65);\n"
"    border-style: transparent ;\n"
"    border-radius: 20px;\n"
"    border-width: 1px;\n"
"    border-color: green;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.cam_name_input.setMaxLength(128)
        self.cam_name_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cam_name_input.setClearButtonEnabled(False)
        self.cam_name_input.setObjectName("cam_name_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cam_name_input)
        self.camera_id_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.camera_id_label.setFont(font)
        self.camera_id_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_id_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: #228B22;\n"
"font: 24pt \"Gill Sans MT\";")
        self.camera_id_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.camera_id_label.setObjectName("camera_id_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.camera_id_label)
        self.cam_id_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        self.cam_id_input.setFont(font)
        self.cam_id_input.setStyleSheet("QLineEdit:focus{ border-color:#66afe9;}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(21, 138, 8);\n"
"    background-color: rgb(25, 35, 65);\n"
"    border-style: transparent ;\n"
"    border-radius: 20px;\n"
"    border-width: 1px;\n"
"    border-color: green;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.cam_id_input.setText("")
        self.cam_id_input.setMaxLength(128)
        self.cam_id_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.cam_id_input.setObjectName("cam_id_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cam_id_input)
        self.create_cam_button = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.create_cam_button.setFont(font)
        self.create_cam_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_cam_button.setStyleSheet("QPushButton{\n"
"font: 75 26pt \"Gill Sans MT\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #228B22;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #006400;\n"
"border: transparent\n"
"}\n"
"\n"
"")
        self.create_cam_button.setObjectName("create_cam_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.create_cam_button)

        self.retranslateUi(new_cam_menu)
        QtCore.QMetaObject.connectSlotsByName(new_cam_menu)

    def retranslateUi(self, new_cam_menu):
        _translate = QtCore.QCoreApplication.translate
        new_cam_menu.setWindowTitle(_translate("new_cam_menu", "Face Mask Detector: Add New Camera"))
        self.camera_name_label.setText(_translate("new_cam_menu", "Camera Name:"))
        self.cam_name_input.setPlaceholderText(_translate("new_cam_menu", "Camera Name"))
        self.camera_id_label.setText(_translate("new_cam_menu", "Camera ID:"))
        self.cam_id_input.setPlaceholderText(_translate("new_cam_menu", "Camera ID (number or IP)"))
        self.create_cam_button.setText(_translate("new_cam_menu", "Create Camera"))

