# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_importRawTool(object):
    def setupUi(self, importRawTool):
        importRawTool.setObjectName("importRawTool")
        importRawTool.resize(500, 600)
        importRawTool.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)    # 只显示关闭按钮
        importRawTool.setFixedSize(importRawTool.width(), importRawTool.height());  # 禁止调整窗口大小
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        importRawTool.setWindowIcon(icon)
        importRawTool.setStyleSheet("margin-size:10px;")
        importRawTool.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(importRawTool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 518, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(99, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setEnabled(False)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.RawSourceL = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.RawSourceL.setEnabled(False)
        self.RawSourceL.setMinimumSize(QtCore.QSize(0, 0))
        self.RawSourceL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        self.RawSourceL.setPalette(palette)
        self.RawSourceL.setAutoFillBackground(False)
        self.RawSourceL.setStyleSheet("border-width:0;")
        self.RawSourceL.setObjectName("RawSourceL")
        self.verticalLayout_2.addWidget(self.RawSourceL)
        self.rawSourceLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rawSourceLable.setFont(font)
        self.rawSourceLable.setStyleSheet("color:rgb(209, 2, 23)")
        self.rawSourceLable.setText("")
        self.rawSourceLable.setObjectName("rawSourceLable")
        self.verticalLayout_2.addWidget(self.rawSourceLable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.RawSourceB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.RawSourceB.setMinimumSize(QtCore.QSize(10, 10))
        self.RawSourceB.setMaximumSize(QtCore.QSize(20, 20))
        self.RawSourceB.setStyleSheet("image: url(:/icon/edit.svg);background-color:transparent;")
        self.RawSourceB.setText("")
        self.RawSourceB.setObjectName("RawSourceB")
        self.horizontalLayout_2.addWidget(self.RawSourceB)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(40, 40))
        self.label_3.setMaximumSize(QtCore.QSize(40, 40))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(40, 0))
        self.label_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setEnabled(True)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(99, 99))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.RawDesL = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.RawDesL.setEnabled(False)
        self.RawDesL.setMinimumSize(QtCore.QSize(0, 0))
        self.RawDesL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RawDesL.setObjectName("RawDesL")
        self.verticalLayout_3.addWidget(self.RawDesL)
        self.rawDesLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rawDesLable.setFont(font)
        self.rawDesLable.setStyleSheet("color:rgb(209, 2, 23)")
        self.rawDesLable.setText("")
        self.rawDesLable.setObjectName("rawDesLable")
        self.verticalLayout_3.addWidget(self.rawDesLable)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.RawDesB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.RawDesB.setMinimumSize(QtCore.QSize(20, 20))
        self.RawDesB.setMaximumSize(QtCore.QSize(20, 20))
        self.RawDesB.setStyleSheet("image: url(:/icon/edit.svg);background-color:transparent;")
        self.RawDesB.setText("")
        self.RawDesB.setObjectName("RawDesB")
        self.horizontalLayout_4.addWidget(self.RawDesB)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(40, 0))
        self.label_7.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(40, 0))
        self.label_8.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(99, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.ComplectL = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ComplectL.setEnabled(False)
        self.ComplectL.setMinimumSize(QtCore.QSize(0, 0))
        self.ComplectL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ComplectL.setObjectName("ComplectL")
        self.verticalLayout_4.addWidget(self.ComplectL)
        self.complectLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.complectLable.setFont(font)
        self.complectLable.setStyleSheet("color:rgb(209, 2, 23)")
        self.complectLable.setText("")
        self.complectLable.setObjectName("complectLable")
        self.verticalLayout_4.addWidget(self.complectLable)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.ComplectB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ComplectB.setMinimumSize(QtCore.QSize(20, 20))
        self.ComplectB.setMaximumSize(QtCore.QSize(20, 20))
        self.ComplectB.setStyleSheet("image: url(:/icon/edit.svg);background-color:transparent;")
        self.ComplectB.setText("")
        self.ComplectB.setObjectName("ComplectB")
        self.horizontalLayout_5.addWidget(self.ComplectB)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(40, 0))
        self.label_10.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(40, 66))
        self.label_11.setMaximumSize(QtCore.QSize(40, 66))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(99, 0))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_9.addWidget(self.label_21)
        self.ProgramL = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ProgramL.setEnabled(False)
        self.ProgramL.setMinimumSize(QtCore.QSize(0, 0))
        self.ProgramL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ProgramL.setObjectName("ProgramL")
        self.verticalLayout_9.addWidget(self.ProgramL)
        self.ProgramLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ProgramLable.setText("")
        self.ProgramLable.setObjectName("ProgramLable")
        self.verticalLayout_9.addWidget(self.ProgramLable)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.ProgramB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ProgramB.setMinimumSize(QtCore.QSize(20, 20))
        self.ProgramB.setMaximumSize(QtCore.QSize(20, 20))
        self.ProgramB.setStyleSheet("image: url(:/icon/edit.svg);background-color:transparent;")
        self.ProgramB.setText("")
        self.ProgramB.setObjectName("ProgramB")
        self.horizontalLayout_8.addWidget(self.ProgramB)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(40, 0))
        self.label_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setMinimumSize(QtCore.QSize(40, 60))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setMinimumSize(QtCore.QSize(99, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.folderLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.folderLable.setFont(font)
        self.folderLable.setStyleSheet("color:rgb(209, 2, 23)")
        self.folderLable.setText("")
        self.folderLable.setObjectName("folderLable")
        self.verticalLayout_6.addWidget(self.folderLable)
        self.folderNameL = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.folderNameL.setEnabled(True)
        self.folderNameL.setMinimumSize(QtCore.QSize(0, 0))
        self.folderNameL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.folderNameL.setObjectName("folderNameL")
        self.verticalLayout_6.addWidget(self.folderNameL)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_8.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_8.setStyleSheet("background-color:transparent;")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(40, 0))
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StartB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StartB.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.StartB.setFont(font)
        self.StartB.setObjectName("StartB")
        self.horizontalLayout_3.addWidget(self.StartB)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        importRawTool.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(importRawTool)
        self.statusbar.setObjectName("statusbar")
        importRawTool.setStatusBar(self.statusbar)

        self.retranslateUi(importRawTool)
        QtCore.QMetaObject.connectSlotsByName(importRawTool)

    def retranslateUi(self, importRawTool):
        _translate = QtCore.QCoreApplication.translate
        importRawTool.setWindowTitle(_translate("importRawTool", "Raw导入小助手v1.0"))
        self.label_2.setText(_translate("importRawTool", "<html><head/><body><p><span style=\" font-weight:600;\">图片来源路径</span></p></body></html>"))
        self.label_6.setText(_translate("importRawTool", "<html><head/><body><p><span style=\" font-weight:600;\">图片目标路径：</span></p></body></html>"))
        self.label_9.setText(_translate("importRawTool", "<html><head/><body><p><span style=\" font-weight:600;\">成图存储路径</span></p></body></html>"))
        self.label_12.setText(_translate("importRawTool", "<html><head/><body><p><span style=\" font-weight:600;\">启动应用程序</span></p></body></html>"))
        self.label_19.setText(_translate("importRawTool", "新文件夹名称"))
        self.StartB.setText(_translate("importRawTool", "开始导入"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    importRawTool = QtWidgets.QMainWindow()
    ui = Ui_importRawTool()
    ui.setupUi(importRawTool)
    importRawTool.show()
    sys.exit(app.exec_())
