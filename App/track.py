# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'track.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 138)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 304, 98))
        self.groupBox.setMouseTracking(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_need = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_need.setFont(font)
        self.label_need.setObjectName("label_need")
        self.verticalLayout.addWidget(self.label_need)
        self.label_waterin = QtWidgets.QLabel(self.groupBox)
        self.label_waterin.setObjectName("label_waterin")
        self.verticalLayout.addWidget(self.label_waterin)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_needvalue = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_needvalue.setFont(font)
        self.label_needvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_needvalue.setObjectName("label_needvalue")
        self.verticalLayout_2.addWidget(self.label_needvalue)
        self.lineEdit_waterin = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_waterin.setEnabled(False)
        self.lineEdit_waterin.setMaximumSize(QtCore.QSize(16777144, 16777215))
        self.lineEdit_waterin.setMaxLength(32736)
        self.lineEdit_waterin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_waterin.setDragEnabled(False)
        self.lineEdit_waterin.setObjectName("lineEdit_waterin")
        self.verticalLayout_2.addWidget(self.lineEdit_waterin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar_water = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_water.setProperty("value", 0)
        self.progressBar_water.setObjectName("progressBar_water")
        self.verticalLayout_3.addWidget(self.progressBar_water)
        self.pushButton_waterin = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_waterin.setObjectName("pushButton_waterin")
        self.verticalLayout_3.addWidget(self.pushButton_waterin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_waterin, self.pushButton_waterin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Water level"))
        self.label_need.setText(_translate("MainWindow", "Need"))
        self.label_waterin.setText(_translate("MainWindow", "Water in"))
        self.label_needvalue.setText(_translate("MainWindow", "7"))
        self.lineEdit_waterin.setText(_translate("MainWindow", "0"))
        self.pushButton_waterin.setText(_translate("MainWindow", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
