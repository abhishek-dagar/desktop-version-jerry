# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from jerry import *
import json
from playsound import playsound
styleData="""
QWidget
{
    color:#00BFFF;
    background-color:black
}

QPushButton:hover
{
    border: 3px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #00BFFF);
}
QLineEdit:hover
{
    border: 3px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1F45FC);
}
"""
class MainWindow(object):
    def setupui(self, MainWindow):
        with open("JSON_FILE\\data.json") as w:
            self.dicts1=json.load(w)
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 576)
        MainWindow.setStyleSheet("color:#00BFFF;background-color:black")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowOpacity(0.7)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 781, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("border-style: solid;""border-color: #00BFFF;" "border-right-width: 5px;"
            "border-left-width: 5px;"
            "border-bottom-style: dotted;")
        self._addShadowEffect(self.frame,50)



        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 360, 781, 191))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("border-style: solid;""border-color: #00BFFF;" "border-right-width: 5px;"
            "border-left-width: 5px;"
            "border-bottom-style: dashed;")
        self._addShadowEffect(self.frame_2,50)




        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(240, 20, 481, 91))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#00BFFF;background-color:black")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.dicts1['name'])




        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(220, 110, 501, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#00BFFF;background-color:black")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(self.dicts1['AI NAME'])
        self.horizontalLayout_4.addWidget(self.lineEdit_3)




        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(120, 190, 601, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#00BFFF;background-color:black")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText(self.dicts1['username'])
        self.horizontalLayout_5.addWidget(self.lineEdit_4)





        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(120, 270, 601, 80))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#00BFFF;background-color:black")
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setText(self.dicts1['password'])
        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(570, 360, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")



        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:#00BFFF;""background-color:black;"
            "border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(550, 390, 158, 42))
        self.pushButton.clicked.connect(lambda: self.update_info())
        self._addShadowEffect(self.pushButton,50)



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:#00BFFF;""background-color:black;"
            "border-radius: 15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(440, 470, 158, 42))
        self.pushButton_2.clicked.connect(lambda: self.main_win())
        self._addShadowEffect(self.pushButton_2,50)


        self._addShadowEffect(self.lineEdit,50)
        self._addShadowEffect(self.lineEdit_2,50)
        self._addShadowEffect(self.lineEdit_3,50)
        self._addShadowEffect(self.lineEdit_4,50)
        #self.frame.raise_()
        self.frame_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)


        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " NAME"))
        self.label_2.setText(_translate("MainWindow", "AI NAME"))
        self.label_3.setText(_translate("MainWindow", "FACEBOOK USER"))
        self.label_4.setText(_translate("MainWindow", "FACEBOOK PASS"))
        self.pushButton.setText(_translate("MainWindow", "UPDATE"))
        self.pushButton_2.setText(_translate("MainWindow", "DONE"))

    def _addShadowEffect(self, item,radius=5,color="#00BFFF"):
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(radius)
        effect.setColor(QtGui.QColor(color))
        effect.setOffset(3,3)
        item.setGraphicsEffect(effect)

    def update_info(self):
        name=self.lineEdit.text()
        AI_name=self.lineEdit_3.text()
        username=self.lineEdit_4.text()
        password=self.lineEdit_2.text()
        dicts={"name": name,
        "AI NAME":AI_name,
        "username": username,
        "password": password}
        with open("JSON_FILE\\data.json", 'w') as f:
            json.dump(dicts,f,indent=4,separators=(',',':'))
        playsound("Sound_Effects\\Media_KeyPress.wav")
    def main_win(self):
        '''self.Window=QtWidgets.QMainWindow()
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self.Window)
        self.Window.showMaximized()'''
        playsound("Sound_Effects\\Media_KeyPress.wav")
        self.MainWindow.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupui(mainWindow)
    mainWindow.setStyleSheet(styleData)
    mainWindow.show()
    sys.exit(app.exec_())
