from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QUrl
from PyQt5.QtWebEngineWidgets import *
from speech_recog import *
import speech_recognition as sr
from web_browser import *
import os
import datetime
import time
import AI
import requests
import threading
import playsound
import taskmanger
styleData_user="""
QWidget
{
    color:#00BFFF;
    background-color:black
}

QPushButton:hover
{
    border: 3px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #00BFFF);
}
"""
styleData="""
QWidget
{
    background-color: black;
    background-attachment: fixed;
    background-image:url('images/main_screen.jpg')
}
QProgressBar:horizontal {
border: 1px solid gray;
border-top-right-radius: 15px;
border-bottom-left-radius: 15px;
background:black;
color:#82CAFF;
}
QProgressBar::chunk:horizontal {
background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #50EBEC, stop: 1 #1F45FC);
border-bottom-left-radius: 15px;
}
QPushButton
{
    background: transparent;
    border-radius: 6;
}"""

class Ui_mainwindow(object):
    def __init__(self, mainwindow):
        self.count=False
        self.speak_listen=True
        fnt = QtGui.QFont('ROG Fonts', 25)
        font_commands=QtGui.QFont('ROG Fonts',10)
        font_cpu=QtGui.QFont('ROG Fonts',10)
        self.mainwindow=mainwindow
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(1823, 971)
        mainwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #mainwindow.setWindowOpacity(0.3)
        mainwindow.setMouseTracking(False)
        mainwindow.setTabletTracking(False)
        mainwindow.setStyleSheet("background-color: black;\n"
        "background-attachment: fixed;"
        "background-image:url('images/main_screen.jpg');")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\Button1.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        mainwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(840, 423, 241, 231))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(1000000, 1000000))
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.setStyleSheet("background: transparent;")
        self._addShadowEffect(self.pushButton,500,'#0000A0')

        #button for close window
        self.close_window_Button = QtWidgets.QPushButton(self.centralwidget)
        self.close_window_Button.setGeometry(QtCore.QRect(1876, 2, 40, 20))
        self.close_window_Button.setStyleSheet("background-color:black;")
        self.close_window_Button.setObjectName("close_window_Button")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\cross.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_window_Button.setIcon(icon)
        self.close_window_Button.setIconSize(QtCore.QSize(100,60))
        self.close_window_Button.clicked.connect(lambda:self.close_window())

        #setting button
        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setEnabled(True)
        self.setting.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.setting.setMinimumSize(QtCore.QSize(0, 0))
        self.setting.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\user.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon)
        self.setting.setIconSize(QtCore.QSize(50,50))
        self.setting.setAutoDefault(True)
        self.setting.setObjectName("settingButton")
        self.setting.clicked.connect(lambda:self.user())


        #browser button
        self.browser = QtWidgets.QPushButton(self.centralwidget)
        self.browser.setEnabled(True)
        self.browser.setGeometry(QtCore.QRect(1500, 150, 100, 100))
        self.browser.setMinimumSize(QtCore.QSize(0, 0))
        self.browser.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\browser.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browser.setIcon(icon)
        self.browser.setIconSize(QtCore.QSize(100,100))
        self.browser.setObjectName("browserButton")

        #camera button
        self.camera_button = QtWidgets.QPushButton(self.centralwidget)
        self.camera_button.setEnabled(True)
        self.camera_button.setGeometry(QtCore.QRect(760, 10, 80, 80))
        self.camera_button.setMinimumSize(QtCore.QSize(0, 0))
        self.camera_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\camera.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camera_button.setIcon(icon)
        self.camera_button.setIconSize(QtCore.QSize(100,100))
        self.camera_button.setObjectName("camera_button")
        self.camera_button.clicked.connect(lambda:os.system("start microsoft.windows.camera:"))

        
        #calculator button
        self.calculator_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculator_button.setEnabled(True)
        self.calculator_button.setGeometry(QtCore.QRect(330, 410, 100, 100))
        self.calculator_button.setMinimumSize(QtCore.QSize(0, 0))
        self.calculator_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\calculator.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calculator_button.setIcon(icon)
        self.calculator_button.setIconSize(QtCore.QSize(100,100))
        self.calculator_button.setObjectName("calculator_button")
        self.calculator_button.clicked.connect(lambda:os.system("start calculator:"))

        #calendar_button
        self.calendar_button = QtWidgets.QPushButton(self.centralwidget)
        self.calendar_button.setEnabled(True)
        self.calendar_button.setGeometry(QtCore.QRect(650, 190, 100, 100))
        self.calendar_button.setMinimumSize(QtCore.QSize(0, 0))
        self.calendar_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\calendar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendar_button.setIcon(icon)
        self.calendar_button.setIconSize(QtCore.QSize(100,100))
        self.calendar_button.setObjectName("calendar_button")
        self.calendar_button.clicked.connect(lambda:os.system("start outlookcal:"))


        #music_player_button
        self.music_player_button = QtWidgets.QPushButton(self.centralwidget)
        self.music_player_button.setEnabled(True)
        self.music_player_button.setGeometry(QtCore.QRect(1530, 490, 100, 100))
        self.music_player_button.setMinimumSize(QtCore.QSize(0, 0))
        self.music_player_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\music.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_player_button.setIcon(icon)
        self.music_player_button.setIconSize(QtCore.QSize(150,150))
        self.music_player_button.setObjectName("music_player_button")
        self.music_player_button.clicked.connect(lambda:os.system("start spotify:"))

        #File_Explorer_button
        self.File_Explorer_button = QtWidgets.QPushButton(self.centralwidget)
        self.File_Explorer_button.setEnabled(True)
        self.File_Explorer_button.setGeometry(QtCore.QRect(1300, 20, 100, 100))
        self.File_Explorer_button.setMinimumSize(QtCore.QSize(0, 0))
        self.File_Explorer_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\file_exp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.File_Explorer_button.setIcon(icon)
        self.File_Explorer_button.setIconSize(QtCore.QSize(150,150))
        self.File_Explorer_button.setObjectName("File_Explorer_button")
        self.File_Explorer_button.clicked.connect(lambda:os.startfile("C:\\Users\\dagar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.lnk"))


        #label for showing img
        self.label_weather_img = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_img.setGeometry(QtCore.QRect(40, 190, 121, 111))
        self.label_weather_img.setText("")
        self.label_weather_img.setScaledContents(True)
        self.label_weather_img.setObjectName("label_2")

        #time clock
        #label date
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(110, 870, 460, 101)
        self.label_date.setObjectName("lable_date")
        self.label_date.setFont(fnt)
        self.label_date.setStyleSheet('color: #00BFFF; background-color:black;')


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1400, 690, 500, 300))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font_commands)
        self.label_2.setText("  command\n\n\n computer said:")
        self.label_2.setStyleSheet("background-color:black;""color:#00BFFF;""border-style: solid;""border-color: #00BFFF;" "border-right-width: 5px;"
            "border-left-width: 5px;")
            #"border-top-right-radius: 50px;"
            #"border-radius:100px")
        self._addShadowEffect(self.label_2,50)

        


        #printing the weather info
        self.label_weather = QtWidgets.QLabel(self.centralwidget)
        self.label_weather.setGeometry(160, 170, 450, 100)
        self.label_weather.setObjectName("label_3")
        self.label_weather.setFont(font_cpu)
        self.label_weather.setStyleSheet('color: #00BFFF;background-color:black')

        self.label_weather_name = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_name.setGeometry(80, 90, 600, 100)
        self.label_weather_name.setObjectName("label_3")
        self.label_weather_name.setFont(fnt)
        self.label_weather_name.setText("WEATHER  INFO")
        self.label_weather_name.setStyleSheet('color: #00BFFF;background-color:black')
        
        
        #LCDnumber display hours
        self.lcdNumberhour = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberhour.setGeometry(QtCore.QRect(210, 820, 200, 51))
        self.lcdNumberhour.setStyleSheet('color: #00BFFF; background-color:black;')
        self.lcdNumberhour.setSmallDecimalPoint(False)
        self.lcdNumberhour.setObjectName("lcdNumber")


        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 570, 341, 222))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cpu_precentage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cpu_precentage.setObjectName("cpu_precentage")
        self.cpu_precentage.setFont(font_cpu)
        self.cpu_precentage.setStyleSheet("color:white;background:transparent")
        self.verticalLayout.addWidget(self.cpu_precentage)
        self.cpu_precent = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.cpu_precent.setObjectName("cpu_precent")
        self.verticalLayout.addWidget(self.cpu_precent)
        self.memory_usage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.memory_usage.setObjectName("memory_usage")
        self.memory_usage.setFont(font_cpu)
        self.memory_usage.setStyleSheet("color:white;")
        self.verticalLayout.addWidget(self.memory_usage)
        self.memory_usa = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.memory_usa.setObjectName("memory_usa")
        self.verticalLayout.addWidget(self.memory_usa)


        
        
        
        

        timer = QtCore.QTimer(self.centralwidget)
        timer.timeout.connect(self.show)
        timer.start(1000) # update every second

        timer = QtCore.QTimer(self.centralwidget)
        timer.timeout.connect(self.showTime)
        timer.start(1000) 
        timer = QtCore.QTimer(self.centralwidget)
        timer.timeout.connect(self.showdate)
        timer.start(1000)



        self.pushButton.raise_()
        self.lcdNumberhour.raise_()
        mainwindow.setCentralWidget(self.centralwidget)

        
        #if self.count==0:
        self.pushButton.clicked.connect(lambda: self.on_click())
        #elif self.count==1:
        #    self.pushButton.clicked.connect(lambda: self.set_value())
            


        self.browser.clicked.connect(lambda: self.browser_open())
        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def resizeEvent(self, event):
        self.setMask(QtGui.QRegion(self.rect(), QtGui.QRegion.Ellipse))
        QtWidgets.QPushButton.resizeEvent(self, event)

    def _addShadowEffect(self, item,radius=5,color="#00BFFF"):
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(radius)
        effect.setColor(QtGui.QColor(color))
        effect.setOffset(3,3)
        item.setGraphicsEffect(effect)

    def _opacity(self,item,ops=0.9):
        _opacitys=QtWidgets.QGraphicsOpacityEffect()
        _opacitys.setOpacity(ops)
        item.setGraphicsEffect(_opacitys)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate

        mainwindow.setWindowTitle(_translate("mainwindow", "jerry"))
    def close_window(self):
        apps=taskmanger.appname()
        for i in range(len(apps)):
            if "jerry" in apps[i]:
                os.system("taskkill /F /IM jerry.exe")
        try:
            sys.exit()
        except:
            pass
        mainwindow.close()



    #showing time, date, weather,cpu info
    def showTime(self):
        currentTime = QtCore.QTime.currentTime()
        displayTxt = currentTime.toString('hh:mm')
        self.lcdNumberhour.display(displayTxt)
    def showdate(self):
        lst=datetime.date.today()
        displayTxt = lst.strftime("%d/%B/%Y")
        day_name=lst.strftime("%A")
        self.label_date.setText(displayTxt+'\n    '+day_name)
    def showweather(self):
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city = "Delhi"
        url = api_address + city
        json_data = requests.get(url).json()
        weather_info = json_data['weather'][0]['main'].lower()
        weather_temp = json_data['main']['temp']
        weather_temp = round(weather_temp - 273.15,2)
        if weather_info=='haze':
            img ="images\\50d.png"
        elif weather_info=="clouds":
            img = "images\\02d.png"
        elif weather_info=='thunderstorm':
            img = "images\\09d.png"
        elif 32.0<=weather_temp<33.0:
            img = "images\\10d.png"
        elif 33.0<=weather_temp<34.0:
            img = "images\\11d.png"
        elif 'clear' in weather_info:
            img = "images\\1d.png"
        elif weather_temp<3.0:
            img = "images\\13d.png"
        self.label_weather_img.setPixmap(QtGui.QPixmap(img))
        self.label_weather.setText(str('New Delhi')+"\n"+str(weather_temp)+"⁰C")
    def showcpu(self):
        cpu_per,mem_usg=cpu()
        self.cpu_precentage.setText("CPU  PERCENTAGE     "+str(cpu_per)+"%")
        self.memory_usage.setText("RAM USAGE     "+str(mem_usg)+"%")
        try:
            self.cpu_precent.setValue(cpu_per) 
            self.memory_usa.setValue(mem_usg)
        except:
            pass       
    def show(self):
        show_weath=threading.Thread(target=self.showweather)
        #show_time=threading.Thread(target=self.showTime)
        #show_date=threading.Thread(target=self.showdate)
        show_weath.start()
        #show_time.start()
        #show_date.start()
        try:
            show_cpu=threading.Thread(target=self.showcpu)
            show_cpu.start()
        except:
            pass


    #Opening user setting
    def user(self):
        import user_ui
        self.Window=QtWidgets.QMainWindow()
        self.ui = user_ui.MainWindow()
        self.ui.setupui(self.Window)
        self.Window.setStyleSheet(styleData_user)
        self.Window.show()

     #openning browser
    def browser_open(self,url=None):
        self.app = QApplication(sys.argv)
        self.web = QWebEngineView()
        self.ui = webbrowser()
        self.ui.web_bro(self.web)
        self.web.showMaximized()
    
    #performing AI commands
    def perform(self):
        while self.count==True:
            self.label_2.setText("listening...")
            command=myCommand().lower()
            self.label_2.setText(str("  you said:")+str(command))
            if command=='stop listening':
                AI.speak('listening stoped')
                self.speak_listen=False
            elif command=='start listening':
                AI.speak("listening start")
                self.speak_listen=True
            if self.speak_listen==True:
                if command!="":
                    play=AI.run(command)
                    
            time.sleep(1)
 
    def on_click(self):
        playsound.playsound("Sound_Effects\\Speech_Resume.wav")
        if self.count==True:
            self.count=False
            AI.speak('listening disabled')
            print(self.count)
        else:
            self.count=True
            AI.speak("listening enabled")
            print(self.count)
        if self.count==True:
            self.p1=threading.Thread(target=self.perform)
            self.p1.start()
    

if __name__ == "__main__":
    import sys
    if QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)
    #app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow(mainwindow)
    #ui.setupUi()
    mainwindow.setStyleSheet(styleData) 
    mainwindow.showMaximized()
    sys.exit(app.exec_())
