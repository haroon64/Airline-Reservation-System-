from PyQt5 import QtCore
import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QTabWidget,QTextEdit, QDialog, QGridLayout, QVBoxLayout,QHBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView, QStackedWidget ,QToolTip,QFormLayout
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QIntValidator
import time



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget,QTableWidgetItem, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon,QImage,QPixmap,QIntValidator

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql6464",database='data_base_project')
mycursor=mydb.cursor()

 
class Bookings(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("AirLine Reservation System ")

        # Set the size and position of the window

       
        self.setFixedSize( 1000 , 500)

        self.setWindowTitle("Airline Reservation System ")
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
        # Create a QLabel and set a background image
        self.setStyleSheet("""
            QMainWindow{
                background-color: #F0E9D9;
                width: 800px;
                height: 760px;
            }
            QToolTip {
                background-color: #F8F8F8;
                border: none;
                padding: 8px;
                font-size: 14px;
                color: #2B2D42;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2B2D42;
            }
            QLineEdit {
                font-size: 16px;
                background-color: #bFFFFFF;
                border: 1px solid #D8D8D8;
                border-radius: 5px;
                padding: 8px;
                color: #2B2D42;
            }
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                color: #FFFFFF;
                background-color: #2B2D42;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF9F1C;
            }
            QCheckBox {
                font-size: 16px;
                font-weight: bold;
                color: #2B2D42;
                background-color: #F8F8F8;
            }
            QRadioButton {
                font-size: 16px;
                font-weight: bold;
                color: #2B2D42;
                background-color: #F8F8F8;
            }
            QComboBox {
                font-size: 16px;
                background-color: #FFFFFF;
                border: 1px solid #D8D8D8;
                border-radius: 5px;
                padding: 8px;
                color: #2B2D42;
            }
        """)
        

    def page(self):

        
            self.label =QLabel("Booking Information ")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.back=QPushButton("Back")
            self.back.clicked.connect(self.back_push)


            mycursor.execute("SELECT * FROM booking_information ")
            data = mycursor.fetchall()
            mydb.commit()
           
            self.column_names = [i[0] for i in mycursor.description]
    
            self.table =QTableWidget()
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(data[0]))
            # Populate table with data
            self.table.setHorizontalHeaderLabels(self.column_names)
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.table.setItem(i, j, item)
    
            
            

            label = QLabel(self)
            pixmap = QPixmap('lgo.jpeg')
            label.setPixmap(pixmap)
            label.setAlignment(QtCore.Qt.AlignCenter)
            
            self.Vlayout=QVBoxLayout()

            self.Vlayout.addWidget(label)
            self.Vlayout.addWidget(self.label)
            self.Vlayout.addWidget(self.table)
            self.Vlayout.addWidget(self.back)

            self.centralWidget = QWidget(self)
            self.centralWidget.setLayout(self.Vlayout)
            self.setCentralWidget(self.centralWidget)
            
    def back_push(self):
            from admin_dash_board import Admin
            self.obj1=Admin()
            self.obj1.admin()
            self.obj1.show()
            self.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Bookings()
    window.page()
    # window.Sign()
    window.show()
    sys.exit(app.exec_())