# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from parameters import TypesDeChainages, Parcours, Regimes, Monotonie
from base_des_faits import BF
from base_des_regles import BR
from base_de_connaissances import BC
from moteur_d_inferences import MoteurInference


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 725)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ia.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -70, 1111, 791))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.chainage = QtWidgets.QGroupBox(self.frame)
        self.chainage.setGeometry(QtCore.QRect(110, 520, 241, 80))
        self.chainage.setCheckable(False)
        self.chainage.setObjectName("chainage")
        self.avant = QtWidgets.QRadioButton(self.chainage)
        self.avant.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.avant.setChecked(True)
        self.avant.setObjectName("avant")
        self.arriere = QtWidgets.QRadioButton(self.chainage)
        self.arriere.setGeometry(QtCore.QRect(130, 30, 95, 20))
        self.arriere.setObjectName("arriere")
        self.regime = QtWidgets.QGroupBox(self.frame)
        self.regime.setGeometry(QtCore.QRect(420, 520, 241, 80))
        self.regime.setObjectName("regime")
        self.irrevocable = QtWidgets.QRadioButton(self.regime)
        self.irrevocable.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.irrevocable.setChecked(True)
        self.irrevocable.setObjectName("irrevocable")
        self.tentative = QtWidgets.QRadioButton(self.regime)
        self.tentative.setGeometry(QtCore.QRect(130, 30, 101, 20))
        self.tentative.setObjectName("tentative")
        self.strategie = QtWidgets.QGroupBox(self.frame)
        self.strategie.setGeometry(QtCore.QRect(110, 610, 241, 80))
        self.strategie.setObjectName("strategie")
        self.profondeur = QtWidgets.QRadioButton(self.strategie)
        self.profondeur.setGeometry(QtCore.QRect(10, 30, 91, 20))
        self.profondeur.setChecked(True)
        self.profondeur.setObjectName("profondeur")
        self.largeur = QtWidgets.QRadioButton(self.strategie)
        self.largeur.setGeometry(QtCore.QRect(130, 30, 95, 20))
        self.largeur.setObjectName("largeur")
        self.monotonie = QtWidgets.QGroupBox(self.frame)
        self.monotonie.setGeometry(QtCore.QRect(420, 610, 241, 80))
        self.monotonie.setObjectName("monotonie")
        self.monotone = QtWidgets.QRadioButton(self.monotonie)
        self.monotone.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.monotone.setChecked(True)
        self.monotone.setObjectName("monotone")
        self.nonMonotone = QtWidgets.QRadioButton(self.monotonie)
        self.nonMonotone.setGeometry(QtCore.QRect(130, 30, 111, 20))
        self.nonMonotone.setObjectName("nonMonotone")
        self.demarrer = QtWidgets.QPushButton(self.frame)
        self.demarrer.setGeometry(QtCore.QRect(320, 720, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(17)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.demarrer.sizePolicy().hasHeightForWidth())
        self.demarrer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.demarrer.setFont(font)
        self.demarrer.setObjectName("demarrer")
        self.bc = QtWidgets.QTextEdit(self.frame)
        self.bc.setGeometry(QtCore.QRect(110, 90, 551, 361))
        self.bc.setObjectName("bc")
        self.but = QtWidgets.QLineEdit(self.frame)
        self.but.setGeometry(QtCore.QRect(110, 470, 431, 31))
        self.but.setObjectName("but")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 470, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.sansBut = QtWidgets.QCheckBox(self.frame)
        self.sansBut.setGeometry(QtCore.QRect(580, 470, 81, 31))
        self.sansBut.setChecked(True)
        self.sansBut.setObjectName("sansBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setChainageState()
        self.setStrategieAndRegimeState()
        self.sansBut.clicked.connect(lambda : self.setChainageState())
        self.avant.clicked.connect(lambda : self.setStrategieAndRegimeState())
        self.arriere.clicked.connect(lambda : self.setStrategieAndRegimeState())
        self.demarrer.clicked.connect(lambda : self.verifier())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Moteur d\'inference"))
        self.chainage.setTitle(_translate("MainWindow", "Type de Chainage"))
        self.avant.setText(_translate("MainWindow", "Avant"))
        self.arriere.setText(_translate("MainWindow", "Arrière"))
        self.regime.setTitle(_translate("MainWindow", "Régime de contrôle"))
        self.irrevocable.setText(_translate("MainWindow", "Irrévocable"))
        self.tentative.setText(_translate("MainWindow", "Par tentative"))
        self.strategie.setTitle(_translate("MainWindow", "Stratégie de recherche"))
        self.profondeur.setText(_translate("MainWindow", "Profondeur"))
        self.largeur.setText(_translate("MainWindow", "Largeur"))
        self.monotonie.setTitle(_translate("MainWindow", "Critère de monotonie"))
        self.monotone.setText(_translate("MainWindow", "Monotone"))
        self.nonMonotone.setText(_translate("MainWindow", "Non monotone"))
        self.demarrer.setText(_translate("MainWindow", "Demarrer"))
        self.label.setText(_translate("MainWindow", "But"))
        self.label_2.setText(_translate("MainWindow", "BC"))
        self.sansBut.setText(_translate("MainWindow", "Sans But"))

    def setChainageState(self):
        if (self.sansBut.isChecked()):
            self.avant.setChecked(True)
            self.chainage.setDisabled(True)
            self.but.setDisabled(True)
        else:
            self.chainage.setDisabled(False)
            self.but.setDisabled(False)

    def setStrategieAndRegimeState(self):
        if (self.arriere.isChecked()):
            self.profondeur.setChecked(True)
            self.strategie.setDisabled(True)
            self.regime.setDisabled(False)
        else :
            self.strategie.setDisabled(False)
            self.irrevocable.setChecked(True)
            self.regime.setDisabled(True)

    def construireBC(self):
        bc = self.bc.toPlainText()
        self.bc.setPlainText("")
        br = []
        bf = set()
        for connaissance in bc.split("\n"):
            if (connaissance.__contains__("=")):
                br.append(connaissance)
            else :
                bf.add(connaissance)
        baseDeFaits = BF(bf)
        baseDeRegles = BR(br)
        return BC(baseDeFaits, baseDeRegles)

    def verifier(self):
        if self.sansBut.isChecked() :
            but = -1
        else :
            but = self.but.text()
        if self.avant.isChecked():
            chainage = TypesDeChainages.AVANT
        else :
            chainage = TypesDeChainages.ARRIERE
        if self.profondeur.isChecked() :
            parcours = Parcours.PROFONDEUR
        else :
            parcours = Parcours.LARGEUR
        if self.irrevocable.isChecked() :
            regime = Regimes.irrevocable
        else :
            regime = Regimes.parTentative
        if self.monotone.isChecked() :
            monotonie = Monotonie.monotone
        else :
            monotonie = Monotonie.nonMonotone
        if(MoteurInference(self.construireBC(), but, chainage, parcours, regime, monotonie).verifier(but)):
            self.bc.setPlainText("Succes")
        else :
            self.bc.setPlainText("Echec")


import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
