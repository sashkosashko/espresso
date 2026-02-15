import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


with open("main.ui", "r") as f:
    template = f.read()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        info = self.cur.execute("""SELECT ID, name, baking, type, desc, price, volume FROM coffee""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Имя", "Прожарка", "Зерно/молотый", "Вкус", "Цена", "Объём"])
        for i, row in enumerate(info):
            self.tableWidget.setRowCount(len(info))
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()