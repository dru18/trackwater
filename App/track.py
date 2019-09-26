#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watertrackerv1.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 198)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_water_tracker = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_water_tracker.setMouseTracking(False)
        self.groupBox_water_tracker.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_water_tracker.setFlat(False)
        self.groupBox_water_tracker.setCheckable(False)
        self.groupBox_water_tracker.setObjectName("groupBox_water_tracker")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_water_tracker)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_set_target = QtWidgets.QLabel(self.groupBox_water_tracker)
        self.label_set_target.setObjectName("label_set_target")
        self.verticalLayout_2.addWidget(self.label_set_target)
        self.label_add_water = QtWidgets.QLabel(self.groupBox_water_tracker)
        self.label_add_water.setObjectName("label_add_water")
        self.verticalLayout_2.addWidget(self.label_add_water)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spinBox_set_target = QtWidgets.QSpinBox(self.groupBox_water_tracker)
        self.spinBox_set_target.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_set_target.setObjectName("spinBox_set_target")
        self.verticalLayout_3.addWidget(self.spinBox_set_target)
        self.lineEdit_count_water = QtWidgets.QLineEdit(self.groupBox_water_tracker)
        self.lineEdit_count_water.setEnabled(False)
        self.lineEdit_count_water.setMaximumSize(QtCore.QSize(16777144, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_count_water.setFont(font)
        self.lineEdit_count_water.setMaxLength(32736)
        self.lineEdit_count_water.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_count_water.setDragEnabled(False)
        self.lineEdit_count_water.setObjectName("lineEdit_count_water")
        self.verticalLayout_3.addWidget(self.lineEdit_count_water)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_set_target = QtWidgets.QPushButton(self.groupBox_water_tracker)
        self.pushButton_set_target.setObjectName("pushButton_set_target")
        self.verticalLayout_4.addWidget(self.pushButton_set_target)
        self.pushButton_add_water = QtWidgets.QPushButton(self.groupBox_water_tracker)
        self.pushButton_add_water.setObjectName("pushButton_add_water")
        self.verticalLayout_4.addWidget(self.pushButton_add_water)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.progressBar_level_water = QtWidgets.QProgressBar(self.groupBox_water_tracker)
        self.progressBar_level_water.setProperty("value", 0)
        self.progressBar_level_water.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_level_water.setObjectName("progressBar_level_water")
        self.horizontalLayout_4.addWidget(self.progressBar_level_water)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_water_tracker, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.read_database()
        self.pushButton_set_target.clicked.connect(self.set_target)
        self.pushButton_set_target.clicked.connect(self.read_database)
        self.pushButton_add_water.clicked.connect(self.add_water)
        self.pushButton_add_water.clicked.connect(self.read_database)
        self.pushButton_add_water.clicked.connect(self.write_log)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Track"))
        self.groupBox_water_tracker.setTitle(_translate("MainWindow", "Water_Tracker"))
        self.label_set_target.setText(_translate("MainWindow", "Set target"))
        self.label_add_water.setText(_translate("MainWindow", "Add water"))
        self.lineEdit_count_water.setText(_translate("MainWindow", "0 Glass"))
        self.pushButton_set_target.setText(_translate("MainWindow", "Set"))
        self.pushButton_add_water.setText(_translate("MainWindow", "Add"))

    def read_database(self):
        water_target_read = open("./data/water/water_target", "r")
        water_target_data = water_target_read.read()
        water_target_read.close()
        water_count_read = open("./data/water/water_count", "r")
        water_count_data = water_count_read.read()
        water_count_read.close()
        water_target_string = str(water_target_data)
        water_target_integer = int(water_target_string)
        self.spinBox_set_target.setProperty("value", water_target_integer)
        water_count_string = str(water_count_data)
        water_count_integer = int(water_count_string)
        self.lineEdit_count_water.setText(water_count_string + " Glass")
        if water_count_integer > 0:
            water_level_integer = water_count_integer/water_target_integer*100
            self.progressBar_level_water.setProperty("value", water_level_integer)
        else:
            self.progressBar_level_water.setProperty("value", water_count_integer)
        if water_count_integer >= water_target_integer:
            self.pushButton_add_water.setEnabled(False)
        else:
            self.pushButton_add_water.setEnabled(True)

    def set_target(self):
        target = self.spinBox_set_target.text()
        water_target_write = open("./data/water/water_target", "w")
        water_target_write.write(target)
        water_target_write.flush()
        water_target_write.close()
        water_count_write = open("./data/water/water_count", "w")
        water_count_write.write('0')
        water_count_write.flush()
        water_count_write.close()
        import os
        os.system('echo "\n**********$USER**********" >> ./log/water/water.log')
        water_log_append = open("./log/water/water.log", "a")
        water_log_append.write("\n=====Target[" + target + "]=====")
        water_log_append.flush()
        water_log_append.close()

    def write_log(self):
        import datetime
        import time
        time = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S")
        time_string = str(time)
        water_target_read = open("./data/water/water_target", "r")
        water_target_data = water_target_read.read()
        water_target_string = str(water_target_data)
        water_count_read = open("./data/water/water_count", "r")
        water_count_data = water_count_read.read()
        water_count_string = str(water_count_data)
        water_log_append = open("./log/water/water.log", "a")
        log = "\n[Target] " + water_target_string + "\t(Done) " + water_count_string + "\t" + time_string
        water_log_append.write(log)
        water_log_append.flush()
        water_log_append.close()
        water_count_read.close()
        water_target_read.close()

    def add_water(self):
        water_count_read = open("./data/water/water_count", "r")
        water_count_data = water_count_read.read()
        water_count_read.close()
        water_count_string = str(water_count_data)
        water_count_integer = int(water_count_string)
        water_count_plus = water_count_integer + 1
        water_count = str(water_count_plus)
        water_count_write = open("./data/water/water_count", "w")
        water_count_write.write(water_count)
        water_count_write.flush()
        water_count_write.close()
        water_target_read = open("./data/water/water_target", "r")
        water_target_data = water_target_read.read()
        water_target_read.close()
        water_target_string = str(water_target_data)
        water_target_integer = int(water_target_string)
        water_level_count = water_count_plus/water_target_integer*100
        water_level = str(water_level_count)
        self.progressBar_level_water.setProperty("value", water_level)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
