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


class Mainwindow(QMainWindow):
    user_name=None
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("AirLine Reservation System ")

        # Set the size and position of the window

       
        self.setFixedSize( 300 , 500)

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




        # show all the widgets
    
    def front_page(self):
        # Create a QLabel and set a background image
        self.signup = QPushButton("Signup", self)
        self.x=0
      
        self.login = QPushButton("Login", self)
        

        # entry box 1
        self.entry = QLineEdit(self)
    
        self.entry.setPlaceholderText("Enter your User Name...")
        # entry box 2
        self.entry2 = QLineEdit(self)

    
        self.entry2.setPlaceholderText("Enter your password...")

        self.check_box_1 = QCheckBox("hide or show password")
        
       
        self.check_box_1.setStyleSheet('QCheckBox::indicator { width: 40px; height: 40px; }')
        self.check_box_1.stateChanged.connect(self.show_password)

        self.check_box_1.setToolTip('click to  hide or show password')  # Set a tooltip for the button

        # Connect the mouse hover event to a function that shows a message box
        


       
        self.spinbox = QComboBox(self)

        self.spinbox.addItem("passenger")
        self.spinbox.addItem("Admin")

        
        self.spinbox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.spinbox.setStyleSheet("font-size: 18px; font-family: Arial;color : Black")
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

       

     
        self.signup.clicked.connect(lambda: self.Signup())

        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.login.clicked.connect(lambda: self.LogIn())
        self.horizontallayout=QHBoxLayout()
        self.horizontallayout.addWidget(self.login)
        self.horizontallayout.addWidget(self.signup)




        self.container = QWidget()
        self.container.setLayout(self.horizontallayout)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(label)
        self.verticalLayout.addWidget(self.entry)
        self.verticalLayout.addWidget(self.entry2)
        self.verticalLayout.addWidget(self.check_box_1)
        self.verticalLayout.addWidget(self.spinbox)
        self.verticalLayout.addWidget(self.container)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.centralWidget)





    def show_password(self,state):

        if state == Qt.Checked:
            self.entry2.setEchoMode(QLineEdit.Normal)
        else:
            self.entry2.setEchoMode(QLineEdit.Password)
    def Signup(self ):
        
      
        self.register_window = Registration_Window()
        self.register_window.signup1()
        self.register_window.show()
        self.close()


    def LogIn(self):

        if self.spinbox.currentText()=="passenger":


            mycursor.execute("SELECT * FROM passengers_account WHERE User_name=%s AND Password=%s", (self.entry.text(), self.entry2.text()))
            result=mycursor.fetchone()



            if result :
                sql = "INSERT INTO new_table (user_name) VALUES (%s)"
                val = (self.entry   .text(),)
                mycursor.execute(sql, val)
                mydb.commit()
                self.dashboard=Passengers()
                self.dashboard.show()
                self.hide()
            else:
                error_message = QMessageBox()
                error_message.setText("Invalid User_name or Password")
                error_message.exec_()


        elif self.spinbox.currentText()=="Admin":

            mycursor.execute("SELECT * FROM admin_account WHERE User_name=%s AND Password=%s", (self.entry.text(), self.entry2.text()))
            result=mycursor.fetchone()



            if result :
                from admin_dash_board import Admin
                sql = "INSERT INTO new_table (user_name) VALUES (%s)"
                val = (self.entry.text(),)
                mycursor.execute(sql, val)
                mydb.commit()
                self.dashboard=Admin()
                self.dashboard.admin()
                self.dashboard.show()
                self.close()
            else:
                error_message = QMessageBox()
                error_message.setText("Invalid User_name or Password")
                error_message.exec_()


           
        
def delete_data():
    mycursor.execute("delete from new_table;")
    mydb.commit()
    print("press")
 





if __name__ == "__main__":


    app = QApplication(sys.argv)
    window = Mainwindow()

    
    window.front_page()
    window.show()
    app.aboutToQuit.connect(delete_data)
    sys.exit(app.exec_())
    