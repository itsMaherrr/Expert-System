import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from mainwindow import Ui_MainWindow


applicaton = QApplication(sys.argv)
interface = Ui_MainWindow()
window = QtWidgets.QMainWindow()
interface.setupUi(window)
window.show()
sys.exit(applicaton.exec_())
