#!/usr/bin/python3
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton
from pyshorteners import Shortener
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("shortner.ui",self)
        self.shortURL = self.findChild(QLineEdit,"lineEdit")
        self.showShortURL = self.findChild(QLineEdit,"lineEdit_2")
        self.expendURL = self.findChild(QLineEdit,"lineEdit_3")
        self.showExpendURL = self.findChild(QLineEdit,"lineEdit_4")
        self.shortURLBtn = self.findChild(QPushButton,"pushButton_3")
        self.shortURLBtn.clicked.connect(self.shortUrl)
        self.expendURLBtn = self.findChild(QPushButton,"pushButton_4")
        self.expendURLBtn.clicked.connect(self.expendUrl)
        self.shortner = Shortener()
    
    def shortUrl(self):
        url = self.shortURL.text()
        if ("tinyurl" not in url) or (url is not None):
            self.showShortURL.setText(str(self.shortner.tinyurl.short(url)))

        else:
            print("URL is already Short by tinyurl")
        
        self.shortURL.setText("")
        


    def expendUrl(self):
        url = self.expendURL.text()
        if ("tinyurl" in url) or (url is not None):
            self.showExpendURL.setText(str(self.shortner.tinyurl.expand(url)))

        else:
            print("URL is already Expend by tinyurl")
        
        self.expendURL.setText("")
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())