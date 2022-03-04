
# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication

from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import QDoubleValidator, QPixmap

from UI.Ui_MainWindow import Ui_MainWindow
from django.http import HttpResponse
from xlwt import *
import numpy as np
import tkinter
import tkinter.messagebox
g = 9.8



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)

        width = self.UI.label_26.width()
        height = self.UI.label_26.height()
        label = QPixmap("label.png").scaled(width, height)
        self.UI.label_26.setPixmap(label)

        validator = QDoubleValidator()
        self.UI.lineEdit.setText('3700')
        self.UI.lineEdit_2.setText('1600')
        self.UI.lineEdit_3.setValidator(validator)
        self.UI.lineEdit_4.setValidator(validator)
        self.UI.lineEdit_5.setText('0.065')
        self.UI.lineEdit_6.setText('2.588')
        self.UI.lineEdit_7.setText('6.037')
        self.UI.lineEdit_8.setText('0.690')
        self.UI.lineEdit_9.setText('8.600')
        self.UI.lineEdit_10.setText('5.975')
        self.UI.lineEdit_11.setText('25000')
        self.UI.lineEdit_16.setText('-0.065')
        self.UI.lineEdit_17.setText('-0.440')
        self.UI.lineEdit_18.setText('-0.234')
        self.UI.lineEdit_19.setText('-0.093')
        self.UI.lineEdit_20.setText('0')
        self.UI.lineEdit_21.setText('0')

    # “ausrechnen" klicken
    @pyqtSlot()
    def on_btn_calculate_clicked(self) -> None:
        m1 = float(self.UI.lineEdit.text())
        m2 = float(self.UI.lineEdit_2.text())
        Fl = float(self.UI.lineEdit_11.text())

        fai1 = float(self.UI.lineEdit_3.text())

        fai2 = float(self.UI.lineEdit_4.text())

        z11_x = float(self.UI.lineEdit_5.text())
        z11_y = float(self.UI.lineEdit_16.text())

        z12_x = float(self.UI.lineEdit_6.text())
        z12_y = float(self.UI.lineEdit_17.text())

        z21_x = float(self.UI.lineEdit_7.text())
        z21_y = float(self.UI.lineEdit_18.text())

        z22_x = float(self.UI.lineEdit_8.text())
        z22_y = float(self.UI.lineEdit_19.text())

        g2_x = float(self.UI.lineEdit_9.text())
        g2_y = float(self.UI.lineEdit_20.text())

        g3_x = float(self.UI.lineEdit_10.text())
        g3_y = float(self.UI.lineEdit_21.text())
        fai1 = fai1 / 180 * np.pi

        fai2 = fai2 / 180 * np.pi
        #fai1 = math.radians(fai1)
        #fai2 = math.radians(fai2)


        # F2 berechnen
        F2_1_1 = z22_x * np.sin(fai2) - z22_y * np.cos(fai2) + z21_y
        F2_1_2 = g2_x - z21_x + z22_x * np.cos(fai2) + z22_y * np.sin(fai2)
        F2_2 = (m2 * g * 0.5 * g3_x + Fl * g3_x) * np.cos(fai1 - fai2)

        F2 = round(F2_2 / (np.sin(fai2 - np.arctan(F2_1_1 / F2_1_2)) * z22_x), 4)
        self.UI.lineEdit_13.setText(str(F2))

        # F1 berechnen
        F1_1 = (m1 * g * 0.5 * g2_x + (m2 * g + Fl) * g2_x) * np.cos(fai1)
        F1_2 = (m2 * g * 0.5 * g3_x + Fl * g3_x) * np.cos(fai1 - fai2)
        F1_3 = F2 * np.sin((np.arctan((z22_x * np.sin(fai2) - z22_y * np.cos(fai2) + z21_y) / (g2_x - z21_x + z22_x * np.cos(fai2) + z22_y * np.sin(fai2))))) * z21_x

        F1_4 = z12_x * np.sin(fai1) + z12_y * np.cos(fai1) - z11_y
        F1_5 = z12_x * np.cos(fai1) - z12_y * np.sin(fai1) - z11_x

        F1 = round((F1_1 + F1_2 ) / ((np.sin(20 / 180 * np.pi )) * z12_x), 4)

        #fai1 - np.arctan(F1_4 / F1_5)
        self.UI.lineEdit_12.setText(str(F1))
        # L1 berechnen
        L1_1 = (z12_x * np.sin(fai1) + z12_y * np.cos(fai1) - z11_y) ** 2
        L1_2 = (z12_x * np.cos(fai1) - z12_y * np.sin(fai1) - z11_x) ** 2
        L1 = round(np.sqrt(L1_1 + L1_2), 4)
        self.UI.lineEdit_14.setText(str(L1))

        # L2 berechnen
        L2_1 = (z22_x * np.sin(fai2) - z22_y * np.cos(fai2) + z21_y) ** 2
        L2_2 = (g2_x - z21_x + z22_x * np.cos(fai2) + z22_y * np.sin(fai2)) ** 2
        L2 = round(np.sqrt(L2_1 + L2_2), 4)
        self.UI.lineEdit_15.setText(str(L2))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
