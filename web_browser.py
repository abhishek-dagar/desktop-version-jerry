import sys
from PyQt5 import QtCore
from PyQt5.Qt import QUrl
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
 
 
class webbrowser(object):
    def web_bro(self,web,url=None):
        #web.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        web.setWindowTitle("Jerry browser")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("browser.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        web.setWindowIcon(icon)
        if url!=None:
            url=QUrl(url)
            print(url)
            web.load(url)
        else:
            web.load(QUrl("https://www.google.com"))


'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = QWebEngineView()
    ui = webbrowser()
    url='youtube.com'
    ui.web_bro(web)
    web.show()
    sys.exit(app.exec_())'''
 


 
