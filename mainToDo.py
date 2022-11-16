import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from main import Ui_importRawTool
from PyQt5.QtCore import pyqtSignal, Qt, QSettings
import os
import shutil
from os.path import join, getsize
import datetime

class MyMainWindow(QMainWindow, Ui_importRawTool):

    settings = QSettings("config.ini", QSettings.IniFormat)
    # define signals
    part_down_signal = pyqtSignal(int)

    def __init__( self, parent=None ):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.progressBar.hide()
        # config.ini path
        self.initRawSourcePath()
        self.initRawDesPath()
        self.initComlectPath()
        self.initProgramPath()

        self.initFolderPre()



    def initUI( self ):
        # connect
        self.RawSourceB.clicked.connect(self.setRawSourcePath)
        self.RawDesB.clicked.connect(self.setRawDesPath)
        self.ComplectB.clicked.connect(self.setComplectPath)
        self.ProgramB.clicked.connect(self.setProgramPath)
        self.folderNameL.returnPressed.connect(self.createFolder)
        self.StartB.clicked.connect(self.startImport)
        self.part_down_signal.connect(self.update_progress)


    # slots

    def setRawSourcePath(self):
        rawSourcePath = QFileDialog.getExistingDirectory(None, "请选择相机中raw文件路径")
        if rawSourcePath != "":
            self.RawSourceL.setText(rawSourcePath)
            preRawSourcePath = os.path.split(rawSourcePath)[::-1][-1]
            print(preRawSourcePath)
            self.settings.setValue("PATH/preRawSourcePath", preRawSourcePath)
            self.rawSourceLable.clear()
    def setRawDesPath(self):
        rawDesPath = QFileDialog.getExistingDirectory(None, "请选择电脑中Raw存储路径")
        if rawDesPath != "":
            self.RawDesL.setText(rawDesPath)
            self.settings.setValue("PATH/rawDesPath", rawDesPath)
            self.rawDesLable.clear()

    def setComplectPath(self):
        complectPath = QFileDialog.getExistingDirectory(None, "请选择成图存储路径")
        if complectPath != "":
            self.ComplectL.setText(complectPath)
            self.settings.setValue("PATH/complectPath", complectPath)
            self.complectLable.clear()

    def setProgramPath(self):
        programPath = QFileDialog.getOpenFileName(self, "请选择程序exe路径")[0]
        print(programPath)
        if programPath != "":
            self.ProgramL.setText(programPath)
            self.settings.setValue("PATH/programPath", programPath)
            self.complectLable.clear()

    def createFolder(self):
        folderName =self.folderNameL.text();
        print(folderName)

    def startImport(self):
        self.folderLable.clear()
        flage = True

        # Check whether the path exists or is empty, and whether the folder name already exists
        try:
            if self.RawSourceL.text() != "":
                lists = os.listdir(self.RawSourceL.text())
                if len(lists) == 0:
                    self.rawSourceLable.setText("图片源路径下无图片")
                    flage = False
            else:
                self.rawSourceLable.setText("请插入相机存储卡或者选择正确的图片源路径")
                flage = False
        except FileNotFoundError:
            self.rawSourceLable.setText("请插入相机存储卡或者选择正确的图片源路径")
        try:
            if self.RawDesL.text() != "":
                os.listdir(self.RawDesL.text())
            else:
                self.rawDesLable.setText("请选择正确的图片目标路径")
                flage = False
        except FileNotFoundError:
            self.rawDesLable.setText("请选择正确的图片目标路径")

        try:
            if self.ComplectL.text() != "":
                os.listdir(self.ComplectL.text())
            else:
                self.complectLable.setText("请选择正确的成图路径")
                flage = False
        except FileNotFoundError:
            self.complectLable.setText("请选择正确的成图路径")

        if self.folderNameL.text() == "":
            self.folderLable.setText("请输入图片目标文件夹和成图文件夹的名称")
            flage = False
        if self.ComplectL.text() != "" and self.folderNameL.text() in os.listdir(self.ComplectL.text()):
            self.folderLable.setText("成图路径下已存在同名目录，请修改名称")
            flage = False

        # copy
        if flage:
            self.rawSourceLable.clear()
            self.rawDesLable.clear()
            self.complectLable.clear()

            # create folder
            rawSourcePath = self.RawSourceL.text()
            folderName = self.folderNameL.text()
            rawDesPath = self.RawDesL.text() + "/" + folderName + "/"
            complectPath = self.ComplectL.text() + "/" + folderName + "/"
            if not os.path.exists(rawDesPath):
                os.mkdir(rawDesPath)
                self.progressBar.show()
                self.copy_between_folders(rawSourcePath, rawDesPath)
            if not os.path.exists(complectPath):
                os.mkdir(complectPath)


        # open Br
        if self.ProgramL.text() != "":
            try:
                os.startfile(r'C:\Program Files\Adobe\Adobe Bridge 2022\Bridge.exe')
            except:
                pass



    def initRawSourcePath(self):
        try:
            if (self.settings.value("PATH/preRawSourcePath") is not None and self.settings.value(
                    "PATH/preRawSourcePath") != ""):
                preRawSourcePath = self.settings.value("PATH/preRawSourcePath")
                lists = os.listdir(self.settings.value("PATH/preRawSourcePath"))
                # sorted by time
                lists = sorted(lists, key=lambda x: os.path.getctime(
                    os.path.join(self.settings.value("PATH/preRawSourcePath"), x)))
                self.RawSourceL.setText(preRawSourcePath + "/" + lists[-1])
        except FileNotFoundError:
            self.RawSourceL.clear()

    def initRawDesPath(self):
        try:
            if (self.settings.value("PATH/rawDesPath") is not None and self.settings.value("PATH/rawDesPath") != ""):
                os.listdir(self.settings.value("PATH/rawDesPath"))
                self.RawDesL.setText(self.settings.value("PATH/rawDesPath"))
        except FileNotFoundError:
            self.RawDesL.clear()

    def initComlectPath(self):
        try:
            if (self.settings.value("PATH/complectPath") is not None and self.settings.value(
                    "PATH/complectPath") != ""):
                os.listdir(self.settings.value("PATH/complectPath"))
                self.ComplectL.setText(self.settings.value("PATH/complectPath"))
        except FileNotFoundError:
            self.ComplectL.clear()

    def initProgramPath(self):
        try:
            if (self.settings.value("PATH/programPath") is not None and self.settings.value(
                    "PATH/programPath") != ""):
                if os.path.exists(self.settings.value("PATH/programPath")):
                    self.ProgramL.setText(self.settings.value("PATH/programPath"))
        except :
            pass


    def initFolderPre(self):
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        self.folderNameL.setText(str(year) + "-" + str(month) + "-" + str(day))

    def copy_between_folders(self, srcDir, desDir):
        files = os.listdir(srcDir)
        # compute folder size
        source_size = 0
        file_copied = 0
        source_size += sum([getsize(join(srcDir, file)) for file in files])

        # copy
        for f in files:
            filePath = os.path.join(srcDir, f)
            if os.path.isfile(filePath):
                shutil.copy(filePath, desDir)
                file_copied += getsize(filePath)
                if source_size != 0:
                    self.part_down_signal.emit(file_copied * 100 / source_size)
                else:
                    self.part_down_signal.emit(100)

    def update_progress(self, progress):
        self.progressBar.setValue(progress)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())