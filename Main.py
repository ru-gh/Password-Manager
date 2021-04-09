#main
from PyQt5 import QtGui, QtWidgets, QtCore
from GUI import Ui_MainWindow
import sys

#This Runs first...
class MyWork(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWork, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      #Calls GUI.py, loads the GUI
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyWork()
    app.exec_()

if __name__ == "__main__":
    main()
