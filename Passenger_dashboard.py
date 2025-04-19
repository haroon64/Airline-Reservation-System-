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
from Booking import Tabs
#connection with my sql server
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql6464",database='data_base_project')
mycursor=mydb.cursor()


class Passengers(QMainWindow):

    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Passengers Dashboard ")

        # Set the size and position of the window

       
        self.setFixedSize( 300 , 500)



        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
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
               font-size: 30px;
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


        self.Ui()
        self.show()

    def Ui(self):

        self.logout_button=QPushButton("Logout")
        
       
        

        self.logout_button.clicked.connect(self.logout)
        self.logout_button.setStyleSheet("QPushButton { border-style: solid; border-width: 2px; border-color: black; }")

        self.Booking_button=QPushButton("Booking")
        self.Booking_button.setStyleSheet("QPushButton { border-style: solid; border-width: 2px; border-color: black; }")
        
        
        self.Booking_button.clicked.connect(self.BooK)

        self.cancelation = QPushButton("Cancelation")
        self.cancelation.setStyleSheet("QPushButton { border-style: solid; border-width: 2px; border-color: black; }")
        
        self.cancelation.clicked.connect(self.cancell_booking)
        
       



        self.booked_flight = QPushButton("Reservation")

        self.booked_flight.setStyleSheet("QPushButton { border-style: solid; border-width: 2px; border-color: black; }")
        self.booked_flight.clicked.connect(self.reservations)
        
        #self.booked_flight.clicked.connect(self.cancelation)


        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)

        mycursor.execute("SELECT * FROM new_table LIMIT 1;")
        data = mycursor.fetchone() # to reterive first row data
        self.x=data[0]

        self.label1=QLabel(self.x)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)


        self.layout=QVBoxLayout()
        self.layout2=QVBoxLayout()
        self.container2=QWidget()
        self.container2.setLayout(self.layout2)

        self.layout2.addWidget(self.Booking_button )
        self.layout2.addWidget(self.booked_flight)
        self.layout2.addWidget(self.cancelation)

        self.layout.addWidget(label)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.container2)
       
        self.layout.addWidget(self.logout_button)


        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

      


        self.show()












    def logout(self):

        mycursor.execute("DELETE FROM data_base_project.new_table;")

        #it is used to commit the current transaction to the database. These changes are only visible to your program and not actually saved to the database until you commit the transaction.
        mydb.commit()
        from front_end import Mainwindow
        self.hide()
        
        self.front_window=Mainwindow()
        self.front_window.front_page()
        self.front_window.show()
        


    def BooK(self):
        self.book=Tabs()
        self.book.show()
        self.close()

    def cancell_booking(self):
        from cancellation import CancellationPage
        self.obj=CancellationPage()
        self.obj.cancel_page()
        self.obj.show()
        self.close()

    def reservations(self):
        from Reservation import Reservation_window
        mycursor.execute("SELECT User_name from booking_information where User_name=%s;",(self.x,))
        data = mycursor.fetchall()

        if data:
            self.obj=Reservation_window()
            self.obj.page()
            self.obj.show()
            self.close()
        else:
            error_msg = QMessageBox()
            error_msg.setText("You Haven't Booked Any Flight ")
            error_msg.exec_()    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window1 = Passengers()
    # window.Sign()
    window1.show()
    sys.exit(app.exec_())
    


