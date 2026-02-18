import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>686</width>
    <height>525</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>60</y>
      <width>661</width>
      <height>411</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addbtn">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="changebtn">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>20</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Изменить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>12</y>
      <width>421</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>686</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""

template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>236</width>
    <height>336</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>ID</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>61</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>61</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Прожарка</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Вкус</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Цена</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Объем</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>71</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Зерно/молотый</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="idEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>20</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="nameEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>50</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="bakingEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>80</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="typeEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>110</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="descEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>140</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="priceEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>170</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="volumeEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>200</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addBtn">
    <property name="geometry">
     <rect>
      <x>14</x>
      <y>242</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>236</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        temp = io.StringIO(template)
        uic.loadUi(temp, self)
        self.addbtn.clicked.connect(self.add_stroke)
        self.changebtn.clicked.connect(self.change_stroke)
        self.load_data()
        
    def load_data(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        info = self.cur.execute("""SELECT ID, name, baking, type, desc, price, volume FROM coffee""").fetchall()
        self.con.commit()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Имя", "Прожарка", "Зерно/молотый", "Вкус", "Цена", "Объём"])
        for i, row in enumerate(info):
            self.tableWidget.setRowCount(len(info))
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


    def add_stroke(self):
        self.add = AddOrChange("add", self)
        self.add.show()

    def change_stroke(self):
        self.add = AddOrChange("change", self)
        self.add.show()
                
class AddOrChange(QMainWindow):
    def __init__(self, state, parent):
        super().__init__()
        temp = io.StringIO(template1)
        uic.loadUi(temp, self)
        self.state = state
        self.parent = parent
        if self.state == "change":
            self.addBtn.setText("Изменить")
            self.addBtn.clicked.connect(self.change_stroke)
        else:
            self.addBtn.setText("Добавить")
            self.addBtn.clicked.connect(self.add_stroke)
    def add_stroke(self):
        try:
            ID = self.idEdit.text()
            name = self.nameEdit.text()
            baking = self.bakingEdit.text()
            typ = self.typeEdit.text()
            desc = self.descEdit.text()
            price = self.priceEdit.text()
            volume = self.volumeEdit.text()
            self.parent.cur.execute("""INSERT INTO coffee VALUES (?, ?, ?, ?, ?, ?, ?)""", (ID, name, baking, typ, desc, price, volume,))
            self.parent.con.commit()
            self.parent.load_data()
            self.close()
            self.parent.show()
        except Exception as e:
            print(e)
            
    def change_stroke(self):
        try:
            ID = self.idEdit.text()
            name = self.nameEdit.text()
            baking = self.bakingEdit.text()
            typ = self.typeEdit.text()
            desc = self.descEdit.text()
            price = self.priceEdit.text()
            volume = self.volumeEdit.text()
            self.parent.cur.execute("""UPDATE coffee SET name = ? WHERE ID = ?""", (name, int(ID),))
            self.parent.con.commit()
            self.parent.load_data()
            self.close()
            self.parent.show()
        except Exception as e:
            print(e)


        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

