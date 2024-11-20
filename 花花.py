from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import sys
import os
import json
import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    current_image_index = 0
    image_files = []
    image_browsing = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # 要看着改
        MainWindow.resize(1312, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 80, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 410, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 50, 121, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 120, 251, 87))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 440, 251, 87))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 560, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(890, 240, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(900, 550, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(720, 620, 321, 271))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("border: 1px solid black;")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(880, 370, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 630, 311, 251))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("border: 1px solid black;")
        self.label_6.setScaledContents(True)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 730, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1080, 687, 121, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1080, 770, 121, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 790, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(705, 100, 481, 111))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(705, 400, 491, 121))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1312, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # 按照你的按钮进行修改
        self.pushButton_2.clicked.connect(self.openFolderDialog)
        self.pushButton.clicked.connect(self.loadHistoryPaths)
        self.pushButton_4.clicked.connect(self.loadFolderData)
        self.pushButton_3.clicked.connect(self.loadHistoryData)
        self.pushButton_5.clicked.connect(self.displayImage)
        self.pushButton_6.clicked.connect(self.previousPage)
        self.pushButton_7.clicked.connect(self.nextPage)
        self.pushButton_8.clicked.connect(self.endImageBrowse)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "上次目录"))
        self.label_2.setText(_translate("MainWindow", "当前分析目录"))
        self.label_3.setText(_translate("MainWindow", "统计各目录数量"))
        self.pushButton.setText(_translate("MainWindow", "查看"))
        self.pushButton_2.setText(_translate("MainWindow", "打开"))
        self.pushButton_3.setText(_translate("MainWindow", "统计"))
        self.pushButton_4.setText(_translate("MainWindow", "统计"))
        self.label_4.setText(_translate("MainWindow", "统计各标签数量"))
        self.pushButton_5.setText(_translate("MainWindow", "结果浏览"))
        self.label_5.setText(_translate("MainWindow", "小小软件"))
        self.pushButton_6.setText(_translate("MainWindow", "上一页"))
        self.pushButton_7.setText(_translate("MainWindow", "下一页"))
        self.pushButton_8.setText(_translate("MainWindow", "结束浏览"))

    def openFolderDialog(self):
        folder_path = QFileDialog.getExistingDirectory(
            None, "选择文件夹", QtCore.QDir.currentPath())

        if folder_path:
            self.textEdit_3.setPlainText(folder_path)  # 要改

            # Save folder_path to text file with a new line
            with open("lishiwenjian.txt", "a") as f:
                f.write(folder_path + "\n")

            # Append folder_path to the existing text in textEdit_2 with a new line
            self.textEdit_2.insertPlainText(folder_path + "\n")  # 要改
        # 选择文件夹，保存在txt里面



    def loadFolderData(self):
        folder_path = self.textEdit_3.toPlainText()

        if folder_path:
            self.tableWidget_2.clear()

            file_names = os.listdir(folder_path)
            label_counts = {}

            for file_name in file_names:
                if file_name.endswith('.json'):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, "r", encoding='gbk') as file:
                        json_data = file.read()
                        data = json.loads(json_data)
                        shapes = data.get('shapes')
                        if shapes:
                            for shape in shapes:
                                label = shape.get('label')
                                if label in label_counts:
                                    label_counts[label] += 1
                                else:
                                    label_counts[label] = 1

            self.tableWidget_2.setColumnCount(len(label_counts))
            self.tableWidget_2.setRowCount(2)
            self.tableWidget_2.setHorizontalHeaderLabels(list(label_counts.keys()))

            column = 0
            for label, count in label_counts.items():
                self.tableWidget_2.setItem(0, column, QtWidgets.QTableWidgetItem(label))
                self.tableWidget_2.setItem(1, column, QtWidgets.QTableWidgetItem(str(count)))
                column += 1
        # 计算文件里面的标签，是当前目录



    def loadHistoryPaths(self):
        if os.path.exists("lishiwenjian.txt"):
            with open("lishiwenjian.txt", "r") as f:
                history_paths = f.read()
            self.textEdit_2.setPlainText(history_paths)
        else:
            self.textEdit_2.setPlainText("无历史路径记录")



    def saveHistoryPaths(self):
        history_paths = self.textEdit_2.toPlainText()
        settings = QtCore.QSettings()
        settings.setValue("history_paths/history_paths", history_paths)

        # Save history paths to file
        with open("lishiwenjian.txt", "w") as f:
            f.write(history_paths)



    # 查看我们所用过的历史文件路径
    def loadHistoryData(self):
        if os.path.exists("lishiwenjian.txt"):
            with open("lishiwenjian.txt", "r") as f:
                history_paths = f.readlines()

            if len(history_paths) >= 2:
                folder_path = history_paths[-2].strip()
                file_names = os.listdir(folder_path)
                label_counts = {}

                for file_name in file_names:
                    if file_name.endswith('.json'):
                        file_path = os.path.join(folder_path, file_name)
                        with open(file_path, "r", encoding='gbk') as file:
                            json_data = file.read()
                            data = json.loads(json_data)
                            shapes = data.get('shapes')
                            if shapes:
                                for shape in shapes:
                                    label = shape.get('label')
                                    if label in label_counts:
                                        label_counts[label] += 1
                                    else:
                                        label_counts[label] = 1

                self.tableWidget.setColumnCount(len(label_counts))
                self.tableWidget.setRowCount(2)
                self.tableWidget.setHorizontalHeaderLabels(list(label_counts.keys()))

                column = 0
                for label, count in label_counts.items():
                    self.tableWidget.setItem(0, column, QtWidgets.QTableWidgetItem(label))
                    self.tableWidget.setItem(1, column, QtWidgets.QTableWidgetItem(str(count)))
                    column += 1
            else:
                self.tableWidget.clear()
        else:
            self.tableWidget.clear()

    def displayImage(self):
        folder_path = self.textEdit_3.toPlainText()
        self.image_files = os.listdir(folder_path)
        self.image_files = [f for f in self.image_files if f.endswith('.png') or f.endswith('.jpg')]  # 如果需要，可以过滤图片文件
        if len(self.image_files) > 0:
            image_path = os.path.join(folder_path, self.image_files[self.current_image_index])
            pixmap = QtGui.QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(self.label_6.width(), self.label_6.height(), QtCore.Qt.KeepAspectRatio)
            self.label_6.setPixmap(scaled_pixmap)
            self.label_6.setScaledContents(True)
            self.label_6.show()

        # 分割图片
        if len(self.image_files) > 0:
            image_path = os.path.join(folder_path, self.image_files[self.current_image_index])
            json_file_path = image_path.replace(".jpg", ".json").replace(".png", ".json")
            if os.path.isfile(json_file_path):
                # 读取JSON文件
                with open(json_file_path, "r", encoding="utf-8") as json_file:
                    json_data = json.load(json_file)
                # 读取图像文件
                image = cv2.imread(image_path)
                # 创建语义分割图像
                label_map = {
                    "pedestrian": (255, 0, 0),  # 红色
                    "car": (0, 255, 0),  # 绿色
                    "rider": (0, 0, 255),  # 蓝色
                    "truck": (0, 120, 120),  # 青色
                    "bus": (120, 120, 0),  # 黄色
                    # 添加更多的标签和对应的颜色
                }
                segmented_image = np.zeros_like(image)

                # 解析JSON数据并在语义分割图像上绘制标注区域
                for shape in json_data["shapes"]:
                    label = shape["label"]
                    points = np.array(shape["points"], dtype=np.int32)

                    # 获取标签对应的颜色
                    color = label_map.get(label)

                    if color is not None:
                        # 在语义分割图像上绘制标注区域
                        cv2.fillPoly(segmented_image, [points], color)
                        x, y, w, h = cv2.boundingRect(points)
                        cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

                # 将语义分割图像与原图融合，保留框框里的颜色不同
                alpha = 0.65  # 设置融合的透明度
                blended_image = cv2.addWeighted(image, alpha, segmented_image, 1 - alpha, 0)

                # 将图像转换为Qt可显示的格式
                height, width, channel = blended_image.shape
                bytes_per_line = channel * width
                qt_image = QtGui.QImage(blended_image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qt_image)

            else:
                pixmap = QtGui.QPixmap(image_path)

            # 将原图与分割图像进行对比显示
            alpha = 0.7  # 设置融合的透明度
            blended_image = cv2.addWeighted(image, alpha, blended_image, 1 - alpha, 0)
            height, width, channel = blended_image.shape
            bytes_per_line = channel * width
            qt_image = QtGui.QImage(blended_image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
            pixmap_comparison = QtGui.QPixmap.fromImage(qt_image)

            scaled_pixmap_comparison = pixmap_comparison.scaled(self.label_7.width(), self.label_7.height(),
                                                                QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(scaled_pixmap_comparison)
            self.label_7.setScaledContents(True)
            self.label_7.show()

    def nextPage(self):
        if self.current_image_index < len(self.image_files) - 1:
            self.current_image_index += 1
            self.displayImage()

    def previousPage(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.displayImage()

    def endImageBrowse(self):
        self.image_browsing = False
        self.label_6.clear()
        self.label_7.clear()

    # 计算上一次的历史路径的文件夹标签



# 要看着改
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
