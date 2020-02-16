import sys

from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QTableWidget, QGridLayout, QApplication
from setup import *

class ShowGB(QWidget):

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

    grid_layout = QGridLayout(self)
    central_widget.setLayout(grid_layout)


    self.tableWidget = QTableWidget()
    self.tableWidget.setColumnCount(1)
    self.tableWidget.setHorizontalHeaderLabels(['Backups '])    # header for table
    self.tableWidget.horizontalHeader().setStretchLastSection(True)     # header size
    self.tableWidget.resizeRowsToContents()

    for item in ArBackups:
      layout.setItem()


    layout.addWidget(self.tableWidget)
    self.setLayout(layout)

    self.initUI()

  def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)
      numrows = len(ArBackups)  # 6 rows in your example

      self.tableWidget.setRowCount(numrows)
      for row in range(numrows):
          # Check if value datatime, if True convert to string
            self.tableWidget.setItem(row, QTableWidgetItem(ArBackups[row]))


if __name__ == '__main__':

  app = QApplication(sys.argv)
  showGB = ShowGB()
  showGB.show()
  sys.exit(app.exec_())
