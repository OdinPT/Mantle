import getpass
import os
import subprocess
import sys
from pathlib import Path

from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QTableWidget, QGridLayout, QApplication, QTableWidgetItem
from Qt import QtCore
import webbrowser as wb
ArBackups = []

user = getpass.getuser()
userx = str(user)
loctemp = Path('/home/' + userx + '/' + 'Backups_Mantle/')


def call_fileExplorer(col):
  teste = str(loctemp) + '/'+col
  os.system("xdg-open " + teste)

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
        self.tableWidget.setHorizontalHeaderLabels(['Backups '])  # header for table
        self.tableWidget.horizontalHeader().setStretchLastSection(True)  # header size
        self.tableWidget.resizeRowsToContents()

        # insert data from array
        for entry in loctemp.iterdir():
            ArBackups.insert(1, entry.name.split())

        ArBackupshoted = sorted(ArBackups)

        numrows = len(ArBackups)  # 6 rows in your example
        numcols = len(ArBackups[0])

        self.tableWidget.setColumnCount(numcols)
        self.tableWidget.setRowCount(numrows)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # imprimir no terminal data select in table
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)

        # insert data from array in table
        for row in range(numrows):
            for column in range(numcols):
                self.tableWidget.setItem(row, column, QTableWidgetItem((ArBackupshoted[row][column])))

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.initUI()

    def cell_was_clicked(self):
        col = self.tableWidget.currentItem().text()
        print("col=", col)
        call_fileExplorer(col)
        return (col)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    showGB = ShowGB()
    showGB.show()
    sys.exit(app.exec_())
