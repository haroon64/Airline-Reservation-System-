import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon,QImage,QPixmap,QIntValidator

import sys
import mysql.connector
from PyQt5 import QtCore

#connection with my sql server
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql6464",database='data_base_project')
mycursor=mydb.cursor()


class Admin(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Admin  Dashboard ")

        # Set the size and position of the window

        
        self.setFixedSize( 300 , 500)

        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
        self.admin()
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
               font-family: Arial, sans-serif;
               font-size: 25px;
               font-weight:bold;
               color: #333;
               display: block;
               margin-bottom: 5px;
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
               padding: 6px;
           }
           QPushButton:hover {
               background-color: #FF9F1C;
               border-style: solid; 
               border-width: 2px; border-color: black;
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
    def admin(self):
        self.logout_button_1= QPushButton("Logout")
        self.logout_button_1.clicked.connect(self.logout)


      
        

      
        self.user_info = QPushButton("User Info ")


        
        self.user_info.clicked.connect(self.passngers_account_information)
        
        self.Flights_info = QPushButton("Flights")

   
        
        self.Flights_info.clicked.connect(self.flight_schedules)
        

        self.passangers_booking = QPushButton("Reservations")
        
     
        
        self.passangers_booking.clicked.connect(self.booking_informations)

        self.Add_flight=QPushButton("ADD Flights ")
        
        
        self.Add_flight.clicked.connect(self.add_new_flight)
        

        self.update_flights = QPushButton("Update")
     
        
        self.update_flights.clicked.connect(self.update_flight_status)

        mycursor.execute("SELECT * FROM new_table LIMIT 1;")
        data = mycursor.fetchone() # to reterive first row data
        self.x=data[0]

        self.label1=QLabel(self.x)
       
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout=QVBoxLayout()
        self.layout2=QVBoxLayout()
        self.container2=QWidget()
        self.container2.setLayout(self.layout2)

        self.layout2.addWidget(self.user_info )
        self.layout2.addWidget(self.Flights_info)
        self.layout2.addWidget(self.passangers_booking)
        self.layout2.addWidget(self.Add_flight)
        self.layout2.addWidget(self.update_flights)

        self.layout.addWidget(label)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.container2)
       
        self.layout.addWidget(self.logout_button_1)


        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)
    
    def logout(self):

        mycursor.execute("DELETE FROM data_base_project.new_table;")
        mydb.commit()

        from front_end import Mainwindow
        self.object=Mainwindow()
        self.object.front_page()
        self.object.show()
        self.close()


    def add_new_flight(self):
        from Add_flights import Tabs
        self.obj4=Tabs()
        self.show()




    def update_flight_status(self):

        from Update_status import Tabs

        self.obj3=Tabs()
        self.obj3.show()
        self.close()
    def passngers_account_information(self):
        from account_info import passanger_accounts
        self.obj3=passanger_accounts()
        self.obj3.page()
        self.obj3.show()
        self.close()


    def flight_schedules(self):
        from Flight_schedules import Tabs
        self.obj=Tabs()
        self.obj.show()
        self.close()
        
    def booking_informations(self):
        from booking_info import Bookings
        self.obj2=Bookings()
        self.obj2.page()
        self.obj2.show()
        self.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    admin1 = Admin()
    admin1.admin()
    # window.Sign()
    admin1.show()
    sys.exit(app.exec_())