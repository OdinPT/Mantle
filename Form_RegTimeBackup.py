import os
import pathlib
import sys

import self
from PyQt5 import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFormLayout, QTextEdit, QCheckBox, QComboBox, QPushButton
from Qt import QtCore
from past.builtins import xrange

thislist = []

class FormRegBackup(QMainWindow):
    central_widget = None

    def __init__(self):
        super().__init__()

        self.setAutoFillBackground(True)
        layout = QFormLayout()

        self.setWindowTitle('Agendamento de Backups automáticos')

        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 450
    #Title

        self.textbox = QTextEdit(self)
        self.textbox1 = QTextEdit(self)
        self.textbox2 = QTextEdit(self)

        self.textbox.move(100, 10)
        self.textbox.resize(240, 40)
        self.textbox.setText("Agendamento  de Backups")
        self.textbox.setReadOnly(True)

        self.textbox1.move(10, 50)
        self.textbox1.resize(400, 30)
        self.textbox1.setText("De quanto em quanto tempo pretender realizar backups ? ")
        self.textbox1.setReadOnly(True)

        self.textbox2.move(10, 73)
        self.textbox2.resize(400, 35)
        self.textbox2.setText("Pretende realizar Backups a cada: ")
        self.textbox2.setReadOnly(True)

        self.combo = QComboBox(self)
        self.combo.addItem("A cada 1 dias")
        self.combo.addItem("A cada 7 dias")
        self.combo.addItem("A cada 14 dias")
        self.combo.addItem("A cada 21 dias")

        self.combo.move(20, 120)
        self.combo.resize(200, 35)

        self.inserir = QPushButton('Add', self)

        self.inserir.move(230, 120)
        self.inserir.resize(200, 35)
        #self.inserir.clicked.connect(self.VerificaFicheiro)
        self.inserir.clicked.connect(self.selected)

        self.CSS()
        self.initUI()



# concatenação apra tirar os numeros e gravar no ficheiro
    def selected(self, text):
        s = (self.combo.currentText())
    # show numbers from string
        aux = 0
        for i in xrange(len(s)):
            try:
                aux = aux * 10 + int(s[i])
            except:
                if aux > 0:
                 #convert int to string
                    teste = str(aux)
                    with open('Time_Backup.conf', 'w') as file:
                        file.write(teste)
                aux = 0
                pass

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def CSS(self):
        self.textbox1.setStyleSheet("background-color: white;")
        self.textbox1.setStyleSheet("border: white;")

        self.textbox2.setStyleSheet("background-color: white;")
        self.textbox2.setStyleSheet("border: white;")

        self.textbox.setFont(QFont("Arial", 13))
        self.textbox.setStyleSheet("background-color: white;")
        self.textbox.setStyleSheet("border: white;")

        self.combo.setStyleSheet("background-color:green ;")

        self.setStyleSheet("background-color: white;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = FormRegBackup()
    mw.show()
    sys.exit(app.exec_())

# está a salvar em ficheiro o tempo que o utilizador pretende fazer backup.
# colocar a salvar em ficheiro a data que fez o backup para somar e fazer o backup passados x dias