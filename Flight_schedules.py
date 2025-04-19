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


class Tabs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("booking  System ")

        # Set the size and position of the window


        self.resize(1000, 500)

        self.setWindowTitle("Airline Reservation System ")
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))

        

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

      
        self.tabs.addTab(domestic_flight_schedules(), "Domestic Flights")
        self.tabs.addTab(International_flight_schedules(), "International Flights")
        

        self.back_button=QPushButton("back")
        self.back_button.clicked.connect(self.back)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.back_button)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("""
            QMainWindow{
                background-color: black;
                width: 800px;
                height: 760px;
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
                background-color: #FF9F1C;} """)

      

        self.show()
    def back(self):
        from admin_dash_board import Admin
        self.obj =Admin()
        self.obj.admin()
        self.obj.show()
        self.close()
       


class domestic_flight_schedules(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Flight schedules ")

        # Set the size and position of the window

       
        self.setFixedSize( 1000 , 500)

        
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
        # Create a QLabel and set a background image
        self.setStyleSheet("""
            QMainWindow{
                background-color: #F0E9D9;
                width: 800px;
                height: 760px;
            }
           
            QLabel {
                font-size: 18px;
                font-weight: bold;
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
           
            }
        """)
        
        self.page()
    def page(self):     
      
            self.label =QLabel("Domestic Flights")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
           

            mycursor.execute("SELECT * FROM domestic_flight_schedules  ")
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
    
            
                    
            image = QLabel(self)
            pixmap = QPixmap('lgo.jpeg')
            image.setPixmap(pixmap)
            image.setAlignment(QtCore.Qt.AlignCenter)

            self.Vlayout=QVBoxLayout()

            self.Vlayout.addWidget(image)
            self.Vlayout.addWidget(self.label)
            self.Vlayout.addWidget(self.table)
          

            self.centralWidget = QWidget(self)
            self.centralWidget.setLayout(self.Vlayout)
            self.setCentralWidget(self.centralWidget)

class International_flight_schedules(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Flight schedules ")

        # Set the size and position of the window

       
        self.setFixedSize( 1000 , 500)

        
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
        # Create a QLabel and set a background image
        self.setStyleSheet("""
            QMainWindow{
                background-color: #F0E9D9;
                width: 800px;
                height: 760px;
            }
           
            QLabel {
                font-size: 18px;
                font-weight: bold;
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
           
            }
        """)
        
        self.page()
    def page(self):     
      
            self.label =QLabel("International Flights Schedule")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
        
           

            mycursor.execute("SELECT * FROM international_flight_schedules  ")
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
    
            
                    
            image = QLabel(self)
            pixmap = QPixmap('lgo.jpeg')
            image.setPixmap(pixmap)
            image.setAlignment(QtCore.Qt.AlignCenter)

            self.Vlayout=QVBoxLayout()

            self.Vlayout.addWidget(image)
            self.Vlayout.addWidget(self.label)
            self.Vlayout.addWidget(self.table)
          

            self.centralWidget = QWidget(self)
            self.centralWidget.setLayout(self.Vlayout)
            self.setCentralWidget(self.centralWidget)
            

            

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Tabs()
    
    window.show()
    
    sys.exit(app.exec_())
