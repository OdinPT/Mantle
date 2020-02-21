import getpass
import os
import sys
from pathlib import Path

from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QTableWidget, QGridLayout, QApplication, QTableWidgetItem

ArBackups = []


class ShowGB(QWidget):

  def array_2_table(self, array, qtable):
    qtable.setColumnCount(10)
    qtable.setRowCount(600)
    for row in range(600):
      for column in range(10):
        qtable.setItem(row, column, QTableWidgetItem(("%1").arg(array[row][column])))

  def __init__(self):
    super().__init__()

    central_widget = QWidget(self)

    self.title = 'Directory backup '
    self.left = 1
    self.top = 1
    self.width = 500

    self.height = 250


    layout = QFormLayout()

    grid_layout = QGridLayout(self)
    central_widget.setLayout(grid_layout)


    self.tableWidget = QTableWidget()

    self.tableWidget.setColumnCount(1)
    self.tableWidget.setHorizontalHeaderLabels(['Backups '])    # header for table
    self.tableWidget.horizontalHeader().setStretchLastSection(True)     # header size
    self.tableWidget.resizeRowsToContents()

    user = getpass.getuser()
    userx = str(user)

    #loctemp = str("/home/" + userx + "/" + "Backups_Mantle/")
    loctemp = Path('/home/' + userx + '/' + 'Backups_Mantle/')
    print(os.listdir(loctemp))

    print("\n antes do array")
    for entry in loctemp.iterdir():
      print(entry.name)
      ArBackups.insert(1, entry.name.split())


    print("\n depois do for")

    for file in os.listdir(loctemp):
      #ArBackups.insert(1,os.listdir(loctemp))
      print(" ")
      #print(repr(file))


    print("\nline 62 ===")



    numrows = len(ArBackups)  # 6 rows in your example
    numcols = len(ArBackups[0])

    print ("\n num linhas")
    print (numrows )

    print("num colunas : ")
    print(numcols)

    #inverte
    changerows = numcols
    print("troca linha por coluna\n")
    print(changerows)

    changecolums = numrows
    print(changecolums)


    self.tableWidget.setColumnCount(changerows)
    self.tableWidget.setRowCount(changecolums)


    for row in range(numrows):
      for column in range(numcols):
        # Check if value datatime, if True convert to string


        self.tableWidget.setItem(row, column, QTableWidgetItem((ArBackups[row][column])))

    layout.addWidget(self.tableWidget)
    self.setLayout(layout)

    self.initUI()


  def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)

      #

if __name__ == '__main__':



  app = QApplication(sys.argv)
  showGB = ShowGB()
  showGB.show()
  sys.exit(app.exec_())
