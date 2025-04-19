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
#connection with my sql server
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

      
        self.tabs.addTab(update_domestic_flight(), "Domestic Flights")
        self.tabs.addTab(update_international_flight(), "International Flights")
        

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



class update_domestic_flight(QMainWindow):
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
            QComboBox {
               font-size: 16px;
               background-color: #FFFFFF;
               border: 1px solid #D8D8D8;
               border-radius: 5px;
               padding: 8px;
               color: #2B2D42;
           }
           
            }
        """)
        
        self.page()
    def page(self):     
      
            self.label =QLabel("Domestic Flights")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.status = QLabel('Status: ', self)
        
            self.status_edit = QComboBox(self)
        
            self.status_edit.addItems(["Active", "Delayed"])
            self.status_edit.setFixedSize(170, 40)
            self.status.move(10,700)
            self.status_edit.move(100,700)
            self.flight_num = QLabel('Flight Number : ', self)
        
            self.flight_num_edit = QComboBox(self)
            self.flight_num_edit.addItem("Flight No")

            self.update_button=QPushButton("Update")
            self.select_button=QPushButton("Select")
            self.select_button.clicked.connect(self.select)
            self.update_button.clicked.connect(self.update)


           

            mycursor.execute("SELECT Flight_number FROM domestic_flight_schedules   ")
            data1 = mycursor.fetchall()
            result_list = []
            
            for row in data1:
                result_list.append(row[0])
            self.flight_num_edit.addItems(result_list)
            
           
            self.column_names = [i[0] for i in mycursor.description]
            mycursor.execute("SELECT * FROM domestic_flight_schedules   ")
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

            self.hlayout=QHBoxLayout()
            self.hlayout.addWidget(self.flight_num)
            self.hlayout.addWidget(self.flight_num_edit)
            self.hlayout.addWidget(self.status)
            self.hlayout.addWidget(self.status_edit)
            self.hlayout.addWidget(self.select_button)
            self.hlayout.addWidget(self.update_button)

            self.container=QWidget(self)
            self.container.setLayout(self.hlayout)

            self.Vlayout=QVBoxLayout()

            self.Vlayout.addWidget(image)
            self.Vlayout.addWidget(self.label)
            self.Vlayout.addWidget(self.container)
            self.Vlayout.addWidget(self.table)
          

            self.centralWidget = QWidget(self)
            self.centralWidget.setLayout(self.Vlayout)
            self.setCentralWidget(self.centralWidget)
    
    

    def update(self):
        if self.flight_num_edit.currentText() != "Flight No":
             mycursor.execute(f"Update  domestic_flight_schedules SET Flight_status='{self.status_edit.currentText()}' where Flight_number='{self.flight_num_edit.currentText()}'")
             data = mycursor.fetchall()
             mydb.commit()
             self.select()
        else:
            error_message = QMessageBox()
            error_message.setText("Please select flight number ")
            error_message.exec_()


    def select(self):
        if self.flight_num_edit.currentText() != "Flight No":

            mycursor.execute(f"SELECT *  from domestic_flight_schedules where Flight_number='{self.flight_num_edit.currentText()}'")
            data = mycursor.fetchall()
            mydb.commit()
            print("yes")
            self.new_table =QTableWidget()  
            self.new_table.setRowCount(len(data))
            self.new_table.setColumnCount(len(data[0]))
            self.column_names = [i[0] for i in mycursor.description]
                # Populate table with data
            self.new_table.setHorizontalHeaderLabels(self.column_names)
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.new_table.setItem(i, j, item)
    
            self.Vlayout.removeWidget(self.table)
            self.table.deleteLater()
            self.table = self.new_table
            self.Vlayout.addWidget(self.table) 
        else:
            error_message = QMessageBox()
            error_message.setText("Please select flight number ")
            error_message.exec_()
        
       


class update_international_flight(QMainWindow):

  
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
            QComboBox {
               font-size: 16px;
               background-color: #FFFFFF;
               border: 1px solid #D8D8D8;
               border-radius: 5px;
               padding: 8px;
               color: #2B2D42;
           }
           
            }
        """)
        
        self.page()
    def page(self):     
      
            self.label =QLabel("International Flights")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.status = QLabel('Status: ', self)
        
            self.status_edit = QComboBox(self)
        
            self.status_edit.addItems(["Active", "Delayed"])
            self.status_edit.setFixedSize(170, 40)
      
            self.flight_num = QLabel('Flight Number : ', self)
        
            self.flight_num_edit = QComboBox(self)
            self.flight_num_edit.addItem("Flight No")

            self.update_button=QPushButton("Update")
            self.select_button=QPushButton("Select")
            self.select_button.clicked.connect(self.select)
            self.update_button.clicked.connect(self.update)


           

            mycursor.execute("SELECT Flight_number FROM international_flight_schedules    ")
            data1 = mycursor.fetchall()
            result_list = []
            
            for row in data1:
                result_list.append(row[0])
            self.flight_num_edit.addItems(result_list)
            
           
            self.column_names = [i[0] for i in mycursor.description]
            mycursor.execute("SELECT * FROM international_flight_schedules   ")
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

            self.hlayout=QHBoxLayout()
            self.hlayout.addWidget(self.flight_num)
            self.hlayout.addWidget(self.flight_num_edit)
            self.hlayout.addWidget(self.status)
            self.hlayout.addWidget(self.status_edit)
            self.hlayout.addWidget(self.select_button)
            self.hlayout.addWidget(self.update_button)

            self.container=QWidget(self)
            self.container.setLayout(self.hlayout)

            self.Vlayout=QVBoxLayout()

            self.Vlayout.addWidget(image)
            self.Vlayout.addWidget(self.label)
            self.Vlayout.addWidget(self.container)
            self.Vlayout.addWidget(self.table)
          

            self.centralWidget = QWidget(self)
            self.centralWidget.setLayout(self.Vlayout)
            self.setCentralWidget(self.centralWidget)
    
    

    def update(self):
        if self.flight_num_edit.currentText() != "Flight No":
             mycursor.execute(f"Update  international_flight_schedules  SET Flight_status='{self.status_edit.currentText()}' where Flight_number='{self.flight_num_edit.currentText()}'")
             data = mycursor.fetchall()
             mydb.commit()
             self.select()
        else:
            error_message = QMessageBox()
            error_message.setText("Please select flight number ")
            error_message.exec_()


    def select(self):
        if self.flight_num_edit.currentText() != "Flight No":

            mycursor.execute(f"SELECT *  from international_flight_schedules  where Flight_number='{self.flight_num_edit.currentText()}'")
            data = mycursor.fetchall()
            mydb.commit()
            print("yes")
            self.new_table =QTableWidget()  
            self.new_table.setRowCount(len(data))
            self.new_table.setColumnCount(len(data[0]))
            self.column_names = [i[0] for i in mycursor.description]
                # Populate table with data
            self.new_table.setHorizontalHeaderLabels(self.column_names)
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.new_table.setItem(i, j, item)
    
            self.Vlayout.removeWidget(self.table)
            self.table.deleteLater()
            self.table = self.new_table
            self.Vlayout.addWidget(self.table) 
        else:
            error_message = QMessageBox()
            error_message.setText("Please select flight number ")
            error_message.exec_()
        



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window1 = Tabs()
    
    window1.show()
    sys.exit(app.exec_())
    

