

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView, QStackedWidget ,QToolTip
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QIntValidator
import time
from PyQt5 import QtCore

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon,QImage,QPixmap,QIntValidator
import sys

import mysql.connector

#connection with my sql server
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql6464",database='data_base_project')
mycursor=mydb.cursor()



class Registration_Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("AirLine Reservation System ")
        self.resize( 300 , 700)
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))

        # Set the stylesheet to beautify the UI
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
                background-color: #FFFFFF;
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


        self.signup1()
    def signup1(self):
       
        self.name1Edit = QLineEdit()
        self.name1Edit.setPlaceholderText("Enter your first name...")
        
        self.name2Edit = QLineEdit()
        self.name2Edit.setPlaceholderText("Enter your last name...")
       
        self.emailEdit = QLineEdit()
        self.emailEdit.setPlaceholderText("Enter your Email...")  
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setPlaceholderText("Enter your password...")

        
        self.password2Edit = QLineEdit()
        self.password2Edit.setPlaceholderText("Confirm Password ...")
       
        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText("Enter your Phone number...")
        self.phone_edit.setValidator(QIntValidator())
        self.phone_edit.setMaxLength(12)

        self.gender_label = QLabel("Gender : ")

        self.male = QRadioButton("male")
        self.female = QRadioButton("female")
        self.other = QRadioButton("other")

        self.show_password_checkbox = QCheckBox("Show password")
        self.show_password_checkbox.stateChanged.connect(self.showPassword1)
        self.show_password_checkbox1 = QCheckBox("Show password")
        self.show_password_checkbox1.stateChanged.connect(self.showPassword2)

      
        self.user_name_edit = QLineEdit()
        self.user_name_edit.setPlaceholderText("Enter your User Name...")
        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)
       
       
        
        self.registerButton = QPushButton("Register")

        self.Back=QPushButton("Back")
        self.Back.clicked.connect(self.back_pressed)

        # Create the grid layout and add the form elements
        self.verticalLayout = QVBoxLayout()

        self.verticalLayout.addWidget(label)
        self.verticalLayout.addWidget(self.name1Edit)

        self.verticalLayout.addWidget(self.name2Edit)

        self.verticalLayout.addWidget(self.emailEdit)

        self.verticalLayout.addWidget(self.user_name_edit)
    
        self.verticalLayout.addWidget(self.passwordEdit)
        self.verticalLayout.addWidget(self.show_password_checkbox)
    
        self.verticalLayout.addWidget(self.password2Edit)
        self.verticalLayout.addWidget(self.show_password_checkbox1)
    
        self.verticalLayout.addWidget(self.phone_edit)
        self.verticalLayout.addWidget(self.gender_label)
        self.verticalLayout.addWidget(self.male)
        self.verticalLayout.addWidget(self.female)
        self.verticalLayout.addWidget(self.other)
        self.verticalLayout.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.Back)
        
        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.centralWidget)

        self.registerButton.clicked.connect(self.register_pressed)

        
        self.show()

    def showPassword1(self, state):
        if state == Qt.Checked:
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)

    def showPassword2(self, state):
        if state == Qt.Checked:
            self.password2Edit.setEchoMode(QLineEdit.Normal)
        else:
            self.password2Edit.setEchoMode(QLineEdit.Password)

    def back_pressed(self):
        from front_end import Mainwindow

        self.obj=Mainwindow()
        self.obj.front_page()
        self.obj.show()
        self.close()

    def register_pressed(self):
        if self.name1Edit.text() == "":
            # Display an error message
            error_msg = QMessageBox()
            error_msg.setText("Please enter your first name.")
            error_msg.exec_()
        if self.name2Edit.text() == "":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your last name.")
            error_msg.exec_()
        if self.passwordEdit.text() == "":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your password.")
            error_msg.exec_()
        if self.password2Edit.text() == "":
            error_msg = QMessageBox()
            error_msg.setText("Please confirm your password.")
            error_msg.exec_()
        if self.user_name_edit.text() == "":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your  user name.")
            error_msg.exec_()
        if self.phone_edit.text() == "":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your Phone number.")
            error_msg.exec_()
      
        if self.passwordEdit.text() != self.password2Edit.text():
            error_msg = QMessageBox()
            error_msg.setText("password does not match .")
            error_msg.exec_()
        if not self.male.isChecked() and not self.female.isChecked() and not self.other.isChecked():
            # Display an error message
            error_msg = QMessageBox()
            error_msg.setText("Please select a gender.")
            error_msg.exec_()

        else:
            if self.male.isChecked():
                x="Male"
            elif self.female.isChecked():
                x="Female"
            elif self.female.isChecked():
                x="other"

            #Sql queries 
            sql = "INSERT INTO registration_rec (first_name, last_name, Email, User_name, Phone_number, Gender) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.name1Edit.text(), self.name2Edit.text(), self.emailEdit.text(), self.user_name_edit.text(), self.phone_edit.text(), x)
            mycursor.execute(sql, values)

           
            sql2="INSERT INTO passengers_account (User_name,password) VALUES(%s,%s)" 
            values1=(self.user_name_edit.text(),self.passwordEdit.text())
            mycursor.execute(sql2,values1)


            mydb.commit()
            msg = QMessageBox()

            msg.setText("Registration Successfully completed")

            msg.exec_()
            





