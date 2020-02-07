import sys
import urllib
from _ctypes import resize
from _hashlib import new

import self as self
from PyQt5 import Qt
#from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor
from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QVBoxLayout, QApplication, QLineEdit, QHBoxLayout, \
    QMainWindow, QGridLayout, QTableWidget, QPushButton, QTextEdit, QFileDialog, QGraphicsView, QGraphicsScene
from PyQt5.uic.properties import QtWidgets, QtGui, QtCore


class MainWindow(QMainWindow):

    central_widget = None

    def __init__(self):
        super().__init__()

        self.setAutoFillBackground(True)
        layout = QFormLayout()

        self.setWindowTitle('About Mantle')

        self.left = 10
        self.top = 10
        self.width = 230
        self.height = 240

        self.label1 = QLabel("Mantle ", self)
        self.label1.move(70, 20)
        self.label1.setFont(QFont("Arial", 20))

        self.label2 = QLabel("Follow me on :", self)
        self.label2.move(10, 70)

        urlLink = "<a href=\"https://www.github.com/OdinPT/\"> Github - OdinPT</a>"
        self.label3 =QLabel(urlLink,self)
        self.label3.setOpenExternalLinks(True)
        self.label3.move(100, 70)

        self.label = QLabel ("Versão 1.0",self)
        self.label.move(10, 100)

        self.textbox = QTextEdit(self)
        self.textbox.move(8, 130)
        self.textbox.resize(210, 80)
        self.textbox.setText("O Intuito deste programa é realizar backup automático dos diretórios que o utilizador pretenda. :)")

        self.textbox.setAlignment(Qt.Qt.AlignLeft)
        self.textbox.setReadOnly(True)

        self.textbox.setStyleSheet("background-color: white;")
        self.textbox.setStyleSheet("border: white;")

        self.setStyleSheet("background-color: white;")

        #self.setLayout(layout)
        self.initUI()

    def initUI(self):

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())