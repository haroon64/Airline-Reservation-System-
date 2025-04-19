from PyQt5 import QtCore
import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout,QHBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView, QStackedWidget ,QToolTip
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QIntValidator
import time


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon,QImage,QPixmap,QIntValidator
from Registration import Registration_Window
from Passenger_dashboard import Passengers

import mysql.connector
#connection with my sql server
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql6464",database='data_base_project')
mycursor=mydb.cursor()

class CancellationPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AirLine Reservation System ")
        self.setFixedSize( 300 , 500)

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
       
    def cancel_page(self):

        self.cancellation_label = QLabel("Cancellation")
        self.flight_number_label = QLabel("Flight Number")
        self.user_name_label = QLabel("User Name")

        self.cancellation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flight_number_edit = QLineEdit()
        self.user_name_edit = QLineEdit()
        self.back_button=QPushButton("Back")
        self.back_button.clicked.connect(self.back_it)

       

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_reservation)

        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(label)
        self.layout.addWidget(self.cancellation_label)
        self.layout.addWidget(self.user_name_label)
        self.layout.addWidget(self.user_name_edit)
        self.layout.addWidget(self.flight_number_label)
        self.layout.addWidget(self.flight_number_edit)
        self.layout.addWidget(self.back_button)
       
        self.layout.addWidget(self.cancel_button)
        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)



        
        
    def back_it(self):
        from Passenger_dashboard import Passengers
        self.obj=Passengers()
        self.obj.Ui()
        self.obj.show()

        
        
        self.close()


     
    def cancel_reservation(self):
        mycursor.execute(f"Select Flight_no from booking_information where User_name='{self.user_name_edit.text()}';")
        data=mycursor.fetchall()
  

  
        l1=[]
        for row in data:
           

            l1.append((row[0]))
        print(l1,1)
        
        x=self.flight_number_edit.text()
       

       
        if x in l1:



            mycursor.execute(f"DELETE FROM booking_information WHERE User_name='{self.user_name_edit.text()}' AND Flight_no='{self.flight_number_edit.text()}'")
            mydb.commit()

            error_msg = QMessageBox()
            error_msg.setText("booking cancellation successful")
            error_msg.exec_()
      
        else:
            error_msg = QMessageBox()
            error_msg.setText("Flight number or user_name field not enetered! ")
            error_msg.exec_()
          
        
    

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cancellation_page = CancellationPage()
    cancellation_page.cancel_page()
    cancellation_page.show()
    sys.exit(app.exec_())