import cmd
import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QIcon
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtWidgets
from Qt import QtCore, QtGui

from Form_RegTimeBackup import FormRegBackup
from about import MainWindow

thislist = []

class Dialog(QWidget):

  def __init__(self):
    super().__init__()

    #window = QWidget()

    central_widget = QWidget(self)

    self.title = 'Directory backup '
    self.left = 1
    self.top = 1
    self.width = 600

    self.height = 250


    layout = QFormLayout()

    self.e1 = QLineEdit(self)

    layout.addRow("Diretory name ", self.e1)

    grid_layout = QGridLayout(self)
    central_widget.setLayout(grid_layout)


    self.tableWidget = QTableWidget()
    self.tableWidget.setColumnCount(1)
    self.tableWidget.setHorizontalHeaderLabels(['Localizations '])    # header for table
    self.tableWidget.horizontalHeader().setStretchLastSection(True)     # header size
    self.tableWidget.resizeRowsToContents()


    layout.addWidget(self.tableWidget)
    self.setLayout(layout)

     #Menu app
    menubar = QMenuBar()
    layout.addWidget(menubar)

    # Menu bar horizontal
    actionFile = menubar.addMenu("File")
    helpfile = menubar.addMenu('help')

    #Menu Vertical column 1

    regbackup = QAction(QIcon('exit24.png'), 'Reg Backup', self)
    regbackup.setShortcut('Ctrl+R')
    regbackup.triggered.connect(self.WindowRegBackup)
    actionFile.addAction(regbackup)

    exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
    exitButton.setShortcut('Ctrl+Q')
    exitButton.setStatusTip('Exit application')
    exitButton.triggered.connect(self.close)
    actionFile.addAction(exitButton)

    aboutus = QAction(QIcon('exit24.png'), 'About US', self)
    aboutus.setShortcut('F1')
    aboutus.triggered.connect(self.WindowAboutUS)
    helpfile.addAction(aboutus)

    self.setLayout(layout)

    self.initUI()

  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    inserir = QPushButton('Add', self)
    fechar = QPushButton('Dell', self)


    inserir.move(4,70)
    fechar.move(3,110)

    inserir.clicked.connect(self.on_click)
    inserir.clicked.connect(self.addItem)

    #ideia se não for atribuido um tempo ele coloca como default 0

    fechar.clicked.connect(self.close)

  @pyqtSlot()
  def WindowRegBackup(self):
    self.rb = FormRegBackup()
    self.rb.show()

  def WindowAboutUS(self):
    self.nd = MainWindow()
    self.nd.show()

  def addItem(self):
    local = self.e1.text()

    lastrow = self.tableWidget.rowCount()
    self.tableWidget.insertRow(lastrow)

    item = QTableWidgetItem(local)
    self.tableWidget.setItem(lastrow, 0, item)
    self.e1.clear()

  def on_click(self):
    textboxValue = self.e1.text()

    thislist.append(textboxValue)
    print("array elements")
    print(thislist)

    print("Total elements from array")
    maximo = (len(thislist))
    print(maximo)

    with open('definitions.conf', 'w') as filehandle:
      for listitem in thislist:
        filehandle.write('%s\n' % listitem)

  def FindFilesrecursively(path):
    arquivosTxt = []
    caminhoAbsoluto = os.path.abspath(path)
    for pastaAtual, subPastas, arquivos in os.walk(caminhoAbsoluto):
      arquivosTxt.extend([os.path.join(pastaAtual, arquivo) for arquivo in arquivos if arquivo.endswith('')])
    return arquivosTxt

  def printDir(diretrio):
    print(os.listdir(diretrio))

if __name__ == '__main__':

  app = QApplication(sys.argv)
  dialog = Dialog()
  dialog.show()
  sys.exit(dialog.exec_())
