
from PyQt5.QtWidgets import QApplication, QMainWindow,QTabWidget,QTextEdit, QDialog, QGridLayout, QVBoxLayout,QHBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView, QStackedWidget ,QToolTip,QFormLayout
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QIntValidator
import time

from PyQt5 import QtCore

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget,QTableWidgetItem, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView
from PyQt5.QtCore import Qt, QDate, QAbstractTableModel
from PyQt5.QtGui import QIcon,QImage,QPixmap,QIntValidator
import sys

import mysql.connector

#connection with my sql server
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql6464",database='data_base_project')
mycursor=mydb.cursor()


class Tabs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("booking  System ")

        # Set the size and position of the window


        self.resize(800, 700)

        self.setWindowTitle("Airline Reservation System ")
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))

        

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

      
        self.tabs.addTab(domestic_flight_booking(), "Domestic Flights")
        self.tabs.addTab(International_flight_booking(), "International Flights")
        

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
        from Passenger_dashboard import Passengers
        self.obj=Passengers()
        self.obj.show()
        Tabs.close(self)


class domestic_flight_booking(QMainWindow):
    my_list=[]
    L1=[]
    l3=[]
    def __init__(self):
        super().__init__()
        self.setWindowTitle("booking  System ")

        # Set the size and position of the window


        self.resize(800, 700)

        self.setWindowTitle("Airline Reservation System ")
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
        self.booking_window()
        self.show()
        self.setStyleSheet("""
            QMainWindow{
                background-color: #F0E9D9;
                width: 800px;
                height: 760px;
            }
            QTextEdit {
                font-family: Arial;
                font-size: 14px;
                background-color: #f2f2f2;
                border: 1px solid #ccc;
                padding: 5px;
            }
            QTextEdit:focus {
                border: 1px solid #2a7af5;
            }
            QToolTip {
                background-color: #F8F8F8;
                border: none;
                padding: 8px;
                font-size: 14px;
                color: #2px;
                font-weight: bold;
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
            QSpinBox{
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

    def booking_window(self):
        self.name_label=QLabel("Name:")
      
        self.name_edit=QLineEdit()

        self.name_edit.setFixedSize(200,40)
        self.email_label=QLabel("Email: ")
       
        self.email_edit=QLineEdit()
        self.email_edit.setFixedSize(200,40)    
        self.phone_label = QLabel('Phone Number : ')
       
        self.phone_edit = QLineEdit()
        self.phone_edit.setFixedSize(200,40)
        self.phone_edit.setValidator(QIntValidator())
        self.phone_edit.setMaxLength(13)
        self.cnic_label = QLabel("Passport number:")
      
        self.cnic = QLineEdit()
        self.cnic.setFixedSize(200,40)
        
        self.label2=QLabel(" ")
        
        self.cnic.setValidator(QIntValidator())
        self.cnic.setMaxLength(13)
        self.city_label = QLabel("Address:")
    
        self.city_edit = QTextEdit()
        self.city_edit.setFixedSize(200,60)
        self.country_label = QLabel("Country: ")
    
        self.country_edit = QLineEdit()
        self.country_edit.setFixedSize(200,40)
        self.From_label=QLabel("From:")
    
        self.From_edit=QComboBox()
        self.From_edit.setFixedSize(200,40)
        self.TO_label=QLabel("TO:")

        self.To_edit=QComboBox()
        self.To_edit.setFixedSize(200,40)


        self.DOB_label=QLabel("Birth date")

        self.dob_edit=QDateEdit()
        self.dob_edit.setFixedSize(200,40)


        self.dob_edit.setCalendarPopup(True)
        self._today_buton=QPushButton('&Today',clicked=self.setToday)
        self.dob_edit.calendarWidget().layout().addWidget(self._today_buton)

        self.Departure_date = QLabel("Departure Date:")
    
        self.date_edit = QDateEdit()
        self.date_edit.setFixedSize(200, 40)

        self.date_edit.setCalendarPopup(True)
        self._today_buton = QPushButton('&Today', clicked=self.setToday)
        self.date_edit.calendarWidget().layout().addWidget(self._today_buton)
        cities = ["Islamabad", "Lahore", "Karachi", "Peshawer", "Sialkot", "Multan", "Faislabad"]

        
        self.From_edit.addItems(cities)
        self.To_edit.addItems(cities)
        
       

        self.Passangers=QLabel("Passengers")
        self.Adults_label=QLabel("Adults:")
    
        self.Adults=QComboBox(self)
        self.Adults.setFixedSize(200, 40)
        self.children_label = QLabel("children:")
    
        self.children = QComboBox(self)
        self.children.setFixedSize(200, 40)
        self.Infants_label = QLabel("Infants:")
    
        self.infants = QComboBox(self)
        self.infants.setFixedSize(200, 40)



        for i in range(0,6):
            self.children.addItem(str(i))
            self.Adults.addItem(str(i))
            self.infants.addItem(str(i))

        self.Passangers = QLabel("0")


           
        #self.Passangers.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.button1=QPushButton("ADD")
        self.button1.setFixedSize(200, 40)
        self.button1.clicked.connect(self.set)
        
        self.Book_button=QPushButton("Book")
        self.Book_button.setFixedSize(200, 40)
       
        self.Book_button.clicked.connect(self.booked)
        self.Find_flight=QPushButton("Find Flights")
        self.Find_flight.setFixedSize(200, 40)

        self.class_label=QLabel("Class: ")
        self.class_edit=QComboBox(self)
        self.class_edit.setFixedSize(200, 40)
        self.class_edit.addItem("Economy")
        self.class_edit.addItem("Executive")
        self.class_edit.addItem("Buissness")

        self.seats=QLabel("Seats: ")

        self.class_edit.currentIndexChanged.connect(self.change)

        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)

        label.setAlignment(QtCore.Qt.AlignCenter)
        
        


        


        self.label=QLabel("Booking")

        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.Vlayout=QVBoxLayout()
        self.Vlayout.addWidget(label)
        self.Vlayout.addWidget(self.label)
       

        
        self.Hlayout0 = QHBoxLayout()
        self.formlayout1=QFormLayout()
        self.formlayout2=QFormLayout()

        self.container01=QWidget()
        self.container01.setLayout(self.formlayout1)
        self.container02=QWidget()
        self.container02.setLayout(self.formlayout2)


        self.Hlayout0.addWidget( self.container01)
        self.Hlayout0.addWidget( self.container02)


        self.formlayout1.addRow(self.name_label,self.name_edit)
        self.formlayout1.addRow(self.email_label,self.email_edit)
        self.formlayout1.addRow(self.DOB_label,self.dob_edit)
        self.formlayout1.addRow(self.From_label,self.From_edit)
        self.formlayout1.addRow(self.phone_label,self.phone_edit)
        self.formlayout1.addRow(self.Adults_label,self.Adults)
        self.formlayout1.addRow(self.Infants_label,self.infants)
        self.formlayout1.addRow(self.children_label,self.children)

        self.formlayout2.addRow(self.city_label,self.city_edit)
        self.formlayout2.addRow(self.country_label,self.country_edit)
        self.formlayout2.addRow(self.cnic_label,self.cnic)
        self.formlayout2.addRow(self.TO_label,self.To_edit)
        self.formlayout2.addRow(self.Departure_date,self.date_edit)
        self.formlayout2.addRow(self.class_label,self.class_edit)
        self.formlayout2.addRow(self.seats,self.Passangers)
        self.formlayout2.addRow(self.label2)



        


        
        self.container = QWidget(self)
        self.container.setLayout(self.Hlayout0)
        
        self.Hlayout=QHBoxLayout()
        
        self.Hlayout.addWidget(self.button1)
        self.Hlayout.addWidget(self.Book_button)
        self.Hlayout.addWidget(self.Find_flight)
        
        self.container3=QWidget(self)
        self.container3.setLayout(self.Hlayout)


        self.Vlayout.addWidget(self.container)
        
        self.container2 = QWidget(self)
        self.container2.setLayout(self.Vlayout)


        self.setCentralWidget(self.container2)

      

        mycursor.execute("SELECT * FROM domestic_flight_schedules")
        data = mycursor.fetchall()
        self.column_names = [i[0] for i in mycursor.description]

        self.table =QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        # Populate table with data
        self.table.setHorizontalHeaderLabels(self.column_names)
        """for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.table.setItem(i, j, item)"""

        
        self.Passangers.setAlignment(QtCore.Qt.AlignCenter) # to algin the label at centre

        self.Vlayout.addWidget(self.container3)
        self.Vlayout.addWidget(self.table)
        
        

        self.Find_flight.clicked.connect(self.find_clicked)
        self.L1=[]

        self.show()
    
    def change(self):
        if self.class_edit.currentText()=="Executive":
           self.label2.setText("Executive class additional 10% of Economy Class")


    
        elif self.class_edit.currentText()=="Buissness":
            self.label2.setText("Buissness class additional 20% of Economy Class")
        else:
            self.label2.setText("")




    def setToday(self):
        today = QDate().currentDate()
        self.dob_edit.calendarWidget().setSelectedDate(today)
        self.date_edit.calendarWidget().setSelectedDate(today)

        self.show()

    def set(self):
        self.Passangers.setText(f"{int(self.Adults.currentText())+int(self.children.currentText())+int(self.infants.currentText())}")
        self.Passangers.setStyleSheet("font-size: 20px; font-family: Arial;")
        

    def find_clicked(self):

        mycursor.execute(f"SELECT * FROM domestic_flight_schedules WHERE `From` = '{self.From_edit.currentText()}' AND `TO` = '{self.To_edit.currentText()}';")
        data=mycursor.fetchall()
        self.flag=0
          
            

        if data :

            self.new_table =QTableWidget()
            self.new_table.setRowCount(len(data))
            self.new_table.setColumnCount(len(data[0]))
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

            # Assuming the QTableWidget is called my_table_widget and the column index is 1
            for row in range(self.new_table.rowCount()):
                item = self.new_table.item(row, 1)
                if item is not None:
                    domestic_flight_booking.my_list.append(item.text())
            print(domestic_flight_booking.my_list)
       


        elif self.From_edit.currentText()==self.To_edit.currentText():
            error_msg = QMessageBox()
            error_msg.setText("Departure location and arrival location can't be same  ")
            error_msg.exec_()    
        else:
            error_msg = QMessageBox()
            error_msg.setText(f"Flight From : {self.From_edit.currentText()} TO: {self.To_edit.currentText()} is not available ")
            error_msg.exec_()
            self.flag=1
       


    def booked(self):
        if self.name_edit.text() == "":
            # Display an error message
            error_msg = QMessageBox()
            error_msg.setText("Please enter your full name.")
            error_msg.exec_()
        elif self.email_edit.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your Email.")
            error_msg.exec_()

        elif self.cnic.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please confirm your CNIC.")
            error_msg.exec_()

        elif self.country_edit.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your Country name.")
            error_msg.exec_()
        elif self.phone_edit.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your Phone number.")
            error_msg.exec_()

        elif self.city_edit.toPlainText()=="":
            error_msg = QMessageBox()
            error_msg.setText("Enter your Address   .")
            error_msg.exec_()
        elif self.Passangers.text()=="0":
            error_msg = QMessageBox()
            error_msg.setText("Enter the seats you want to book    .")
            error_msg.exec_()
        


            
        
        elif self.flag==1:
            error_msg = QMessageBox()
            error_msg.setText(f"Flight From : {self.From_edit.currentText()} TO: {self.To_edit.currentText()} is not available ")
            error_msg.exec_()

        else:
            domestic_flight_booking.L1.append(self.name_edit.text())
            domestic_flight_booking.L1.append(self.From_edit.currentText())
            domestic_flight_booking.L1.append(self.To_edit.currentText())
            domestic_flight_booking.L1.append(self.class_edit.currentText())
            domestic_flight_booking.L1.append(int(self.Passangers.text()))
            domestic_flight_booking.l3.append(int(self.Passangers.text()))

           
         

            self.obj=FlightIdDialog()



class FlightIdDialog(domestic_flight_booking):
    def __init__(self):
        super().__init__()
        # Create label and line edit widgets for flight ID
        self.flight_id_label = QLabel("Enter Flight ID:")
        self.flight_id_edit = QLineEdit()
        print(domestic_flight_booking.L1)
        # Create confirmation button
        self.confirm_button = QPushButton("Confirm")
        
        self.confirm_button.clicked.connect(self.confirm)
        self.setFixedSize(300,200)
        

        self.form_layout=QFormLayout()
        self.form_layout.addRow(self.flight_id_label,self.flight_id_edit)
        self.form_layout.addRow("      ",self.confirm_button)
        self.container2 = QWidget(self)
        self.container2.setLayout(self.form_layout)
        self.setCentralWidget(self.container2)
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
            }""")

        self.show()
    def confirm(self ):
        mycursor.execute(f"SELECT Flight_status FROM domestic_flight_schedules WHERE Flight_number='{self.flight_id_edit.text()}'")

        # Fetch all the rows returned by the query
        data = mycursor.fetchall()

        if self.flight_id_edit.text() in domestic_flight_booking.my_list:
        #Check the value of the 'Flight_status' column
            if  data[0][0] == "Active":
            
                if domestic_flight_booking.L1[3]=="Economy":

    
    
                    query = f"""INSERT INTO booking_information (User_name, Flight_no, Name, `From`, Departure_date, departure_time, `To`, Arrival_time, Arrival_date, Class, Seats, price)
                    SELECT new_table.user_name, '{self.flight_id_edit.text()}', '{domestic_flight_booking.L1[0]}', '{domestic_flight_booking.L1[1]}', domestic_flight_schedules.Depart_date, domestic_flight_schedules.depart_time, '{domestic_flight_booking.L1[2]}', domestic_flight_schedules.Arrival_time, domestic_flight_schedules.Arrival_date, '{domestic_flight_booking.L1[3]}', '{domestic_flight_booking.L1[4]}', {domestic_flight_booking.L1[4]} * (domestic_flight_schedules.Economy_price)
                    FROM new_table, domestic_flight_schedules   
                    WHERE Flight_number = '{self.flight_id_edit.text()}'"""   
        
                    print(1)
                    mycursor.execute(query)
                    seats_booked=domestic_flight_booking.l3.pop()
    
                    mycursor.execute(f"Update domestic_flight_schedules set Economy_seats=Economy_seats-{seats_booked}   WHERE Flight_number = '{self.flight_id_edit.text() }' ")
    
    
                    mydb.commit()
                    domestic_flight_booking.my_list.clear()
                    domestic_flight_booking.L1.clear()
                    error_msg = QMessageBox()
                    error_msg.setText("Flight Successfully Booked.")
                    error_msg.exec_()  
                    
                    self.close()
                elif domestic_flight_booking.L1[3]=="Buissness":
                    query = f"""INSERT INTO booking_information (User_name, Flight_no, Name, `From`, Departure_date, departure_time, `To`, Arrival_time, Arrival_date, Class, Seats, price)
                    SELECT new_table.user_name, '{self.flight_id_edit.text()}', '{domestic_flight_booking.L1[0]}', '{domestic_flight_booking.L1[1]}', domestic_flight_schedules.Depart_date, domestic_flight_schedules.depart_time, '{domestic_flight_booking.L1[2]}', domestic_flight_schedules.Arrival_time, domestic_flight_schedules.Arrival_date, '{domestic_flight_booking.L1[3]}', '{domestic_flight_booking.L1[4]}', {domestic_flight_booking.L1[4]} * (domestic_flight_schedules.Economy_price*(20/100)+domestic_flight_schedules.Economy_price)
                    FROM new_table, domestic_flight_schedules
                    WHERE Flight_number = '{self.flight_id_edit.text()}'""" 
                    print(2)
        
                    mycursor.execute(query)
                    seats_booked=domestic_flight_booking.l3.pop()
    
                    mycursor.execute(f"Update domestic_flight_schedules set Buissnes_seats=Buissnes_seats-{seats_booked}   WHERE Flight_number = '{self.flight_id_edit.text() }' ")
                    error_msg = QMessageBox()
                    error_msg.setText("Flight Successfully Booked.")
                    error_msg.exec_()
    
                    mydb.commit()
        
                    domestic_flight_booking.my_list.clear()
                    domestic_flight_booking.L1.clear()  
                    self.close()
                elif domestic_flight_booking.L1[3]=="Executive":
                    query = f"""INSERT INTO booking_information (User_name, Flight_no, Name, `From`, Departure_date, departure_time, `To`, Arrival_time, Arrival_date, Class, Seats, price)
                    SELECT new_table.user_name, '{self.flight_id_edit.text()}', '{domestic_flight_booking.L1[0]}', '{domestic_flight_booking.L1[1]}', domestic_flight_schedules.Depart_date, domestic_flight_schedules.depart_time, '{domestic_flight_booking.L1[2]}', domestic_flight_schedules.Arrival_time, domestic_flight_schedules.Arrival_date, '{domestic_flight_booking.L1[3]}', '{domestic_flight_booking.L1[4]}', {domestic_flight_booking.L1[4]} * (domestic_flight_schedules.Economy_price*(10/100)+domestic_flight_schedules.Economy_price)
                    FROM new_table, domestic_flight_schedules
                    WHERE Flight_number = '{self.flight_id_edit.text()}'""" 
                    print(3)
        
                    mycursor.execute(query)
                    seats_booked=domestic_flight_booking.l3.pop()
    
                    mycursor.execute(f"Update domestic_flight_schedules set Exeuctive_seats=Exeuctive_seats-{seats_booked}   WHERE Flight_number = '{self.flight_id_edit.text() }' ")
                    mydb.commit()
                    error_msg = QMessageBox()
                    error_msg.setText("Flight Successfully Booked.")
                    error_msg.exec_()
        
                    domestic_flight_booking.my_list.clear()
                    domestic_flight_booking.L1.clear()  
                    error_msg = QMessageBox()
                    error_msg.setText("Flight Successfully Booked.")
                    error_msg.exec_()
                    self.close()
             
                      
            else:
                error_msg = QMessageBox()
                error_msg.setText("Flight you want to book is delayed ")
                error_msg.exec_()
        else: 
                error_msg = QMessageBox()
                error_msg.setText("invalid flight number entered .")
                error_msg.exec_()




class International_flight_booking(QMainWindow):


    my_list=[]
    L1=[]
    l3=[]
    def __init__(self):
        super().__init__()
        self.setWindowTitle("booking  System ")

        # Set the size and position of the window


        self.resize(800, 700)

        self.setWindowTitle("Airline Reservation System ")
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
        self.booking_window()
        self.show()
        self.setStyleSheet("""
            QMainWindow{
                background-color: #F0E9D9;
                width: 800px;
                height: 760px;
            }
            QTextEdit {
                font-family: Arial;
                font-size: 14px;
                background-color: #f2f2f2;
                border: 1px solid #ccc;
                padding: 5px;
            }
            QTextEdit:focus {
                border: 1px solid #2a7af5;
            }
            QToolTip {
                background-color: #F8F8F8;
                border: none;
                padding: 8px;
                font-size: 14px;
                color: #2px;
                font-weight: bold;
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
            QSpinBox{
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

    def booking_window(self):
        self.name_label=QLabel("Name:")
      
        self.name_edit=QLineEdit()

        self.name_edit.setFixedSize(200,40)
        self.email_label=QLabel("Email: ")
       
        self.email_edit=QLineEdit()
        self.email_edit.setFixedSize(200,40)    
        self.phone_label = QLabel('Phone Number : ')
       
        self.phone_edit = QLineEdit()
        self.phone_edit.setFixedSize(200,40)
        self.phone_edit.setValidator(QIntValidator())
        self.phone_edit.setMaxLength(13)
        self.cnic_label = QLabel("Passport number:")
      
        self.cnic = QLineEdit()
        self.cnic.setFixedSize(200,40)
        
        self.label2=QLabel(" ")
        
        self.cnic.setValidator(QIntValidator())
        self.cnic.setMaxLength(13)
        self.city_label = QLabel("Address:")
    
        self.city_edit = QTextEdit()
        self.city_edit.setFixedSize(200,60)
        self.country_label = QLabel("Country: ")
    
        self.country_edit = QLineEdit()
        self.country_edit.setFixedSize(200,40)
        self.From_label=QLabel("From:")
    
        self.From_edit=QComboBox()
        self.From_edit.setFixedSize(200,40)
        self.TO_label=QLabel("TO:")

        self.To_edit=QComboBox()
        self.To_edit.setFixedSize(200,40)


        self.DOB_label=QLabel("Birth date")

        self.dob_edit=QDateEdit()
        self.dob_edit.setFixedSize(200,40)


        self.dob_edit.setCalendarPopup(True)
        self._today_buton=QPushButton('&Today',clicked=self.setToday)
        self.dob_edit.calendarWidget().layout().addWidget(self._today_buton)

        self.Departure_date = QLabel("Departure Date:")
    
        self.date_edit = QDateEdit()
        self.date_edit.setFixedSize(200, 40)

        self.date_edit.setCalendarPopup(True)
        self._today_buton = QPushButton('&Today', clicked=self.setToday)
        self.date_edit.calendarWidget().layout().addWidget(self._today_buton)
       

        
        self.From_edit.addItems([
    'Karachi',
    'Lahore',
    'Islamabad',
    'Peshawar',
    'Riyadh',
    'Jeddah',
    'Sialkot',
    'Faisalabad',
    'Multan',
    'New York',
    'Beijing',
    'Sydney',
    'Tokyo',
    'Paris',
    'Rome',
    'Dubai',
    'London'])
        self.To_edit.addItems([
    'Karachi',
    'Lahore',
    'Islamabad',
    'Peshawar',
    'Riyadh',
    'Jeddah',
    'Sialkot',
    'Faisalabad',
    'Multan',
    'New York',
    'Beijing',
    'Sydney',
    'Tokyo',
    'Paris',
    'Rome',
    'Dubai',
    'London'])
        
       

        self.Passangers=QLabel("Passengers")
        self.Adults_label=QLabel("Adults:")
    
        self.Adults=QComboBox(self)
        self.Adults.setFixedSize(200, 40)
        self.children_label = QLabel("children:")
    
        self.children = QComboBox(self)
        self.children.setFixedSize(200, 40)
        self.Infants_label = QLabel("Infants:")
    
        self.infants = QComboBox(self)
        self.infants.setFixedSize(200, 40)



        for i in range(0,6):
            self.children.addItem(str(i))
            self.Adults.addItem(str(i))
            self.infants.addItem(str(i))

        self.Passangers = QLabel("0")


           
        #self.Passangers.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.button1=QPushButton("ADD")
        self.button1.setFixedSize(200, 40)
        self.button1.clicked.connect(self.set)
        
        self.Book_button=QPushButton("Book")
        self.Book_button.setFixedSize(200, 40)
       
        self.Book_button.clicked.connect(self.booked)
        self.Find_flight=QPushButton("Find Flights")
        self.Find_flight.setFixedSize(200, 40)

        self.class_label=QLabel("Class: ")
        self.class_edit=QComboBox(self)
        self.class_edit.setFixedSize(200, 40)
        self.class_edit.addItem("Economy")
        self.class_edit.addItem("Executive")
        self.class_edit.addItem("Buissness")

        self.seats=QLabel("Seats: ")

        self.class_edit.currentIndexChanged.connect(self.change)

        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)

        label.setAlignment(QtCore.Qt   .AlignCenter)
        self.From_edit.currentIndexChanged.connect(self.updateComboBox1Items)
        


        


        self.label=QLabel("Booking")

        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.Vlayout=QVBoxLayout()
        self.Vlayout.addWidget(label)
        self.Vlayout.addWidget(self.label)
       

        
        self.Hlayout0 = QHBoxLayout()
        self.formlayout1=QFormLayout()
        self.formlayout2=QFormLayout()

        self.container01=QWidget()
        self.container01.setLayout(self.formlayout1)
        self.container02=QWidget()
        self.container02.setLayout(self.formlayout2)


        self.Hlayout0.addWidget( self.container01)
        self.Hlayout0.addWidget( self.container02)


        self.formlayout1.addRow(self.name_label,self.name_edit)
        self.formlayout1.addRow(self.email_label,self.email_edit)
        self.formlayout1.addRow(self.DOB_label,self.dob_edit)
        self.formlayout1.addRow(self.From_label,self.From_edit)
        self.formlayout1.addRow(self.phone_label,self.phone_edit)
        self.formlayout1.addRow(self.Adults_label,self.Adults)
        self.formlayout1.addRow(self.Infants_label,self.infants)
        self.formlayout1.addRow(self.children_label,self.children)

        self.formlayout2.addRow(self.city_label,self.city_edit)
        self.formlayout2.addRow(self.country_label,self.country_edit)
        self.formlayout2.addRow(self.cnic_label,self.cnic)
        self.formlayout2.addRow(self.TO_label,self.To_edit)
        self.formlayout2.addRow(self.Departure_date,self.date_edit)
        self.formlayout2.addRow(self.class_label,self.class_edit)
        self.formlayout2.addRow(self.seats,self.Passangers)
        self.formlayout2.addRow(self.label2)



        


        
        self.container = QWidget(self)
        self.container.setLayout(self.Hlayout0)
        
        self.Hlayout=QHBoxLayout()
        
        self.Hlayout.addWidget(self.button1)
        self.Hlayout.addWidget(self.Book_button)
        self.Hlayout.addWidget(self.Find_flight)
        
        self.container3=QWidget(self)
        self.container3.setLayout(self.Hlayout)


        self.Vlayout.addWidget(self.container)
        
        self.container2 = QWidget(self)
        self.container2.setLayout(self.Vlayout)


        self.setCentralWidget(self.container2)

      

        mycursor.execute("SELECT * FROM domestic_flight_schedules")
        data = mycursor.fetchall()
        self.column_names = [i[0] for i in mycursor.description]

        self.table =QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        # Populate table with data
        self.table.setHorizontalHeaderLabels(self.column_names)
        """for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.table.setItem(i, j, item)"""

        
        self.Passangers.setAlignment(QtCore.Qt.AlignCenter) # to algin the label at centre

        self.Vlayout.addWidget(self.container3)
        self.Vlayout.addWidget(self.table)
        
        

        self.Find_flight.clicked.connect(self.find_clicked)
        self.L1=[]

        self.show()
    def updateComboBox1Items(self, index):

            self.To_edit.clear()
            l1=['New York', 'Beijing', 'Sydney', 'Tokyo', 'Paris', 'Rome', 'Dubai', 'London','Riyadh', 'Jeddah',]
            l2=['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Sialkot', 'Faisalabad', 'Multan']
            if self.From_edit.currentText() in l2:
                self.To_edit.addItems(l1)
            elif self.From_edit.currentText() in l1:
                self.To_edit.addItems(l2)

    
    def change(self):
        if self.class_edit.currentText()=="Executive":
           self.label2.setText("Executive class additional 10% of Economy Class")


    
        elif self.class_edit.currentText()=="Buissness":
            self.label2.setText("Buissness class additional 20% of Economy Class")
        else:
            self.label2.setText("")




    def setToday(self):
        today = QDate().currentDate()
        self.dob_edit.calendarWidget().setSelectedDate(today)
        self.date_edit.calendarWidget().setSelectedDate(today)

        self.show()

    def set(self):
        self.Passangers.setText(f"{int(self.Adults.currentText())+int(self.children.currentText())+int(self.infants.currentText())}")
        self.Passangers.setStyleSheet("font-size: 20px; font-family: Arial;")
        
        

    def find_clicked(self):

        mycursor.execute(f"SELECT * FROM international_flight_schedules WHERE `From` = '{self.From_edit.currentText()}' AND `TO` = '{self.To_edit.currentText()}';")
        data=mycursor.fetchall()
        self.flag=0
          
            

        if data :

            self.new_table =QTableWidget()
            self.new_table.setRowCount(len(data))
            self.new_table.setColumnCount(len(data[0]))
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

            # Assuming the QTableWidget is called my_table_widget and the column index is 1
            for row in range(self.new_table.rowCount()):
                item = self.new_table.item(row, 1)
                if item is not None:
                    International_flight_booking.my_list.append(item.text())
            print(International_flight_booking.my_list)
       


        elif self.From_edit.currentText()==self.To_edit.currentText():
            error_msg = QMessageBox()
            error_msg.setText("Departure location and arrival location can't be same  ")
            error_msg.exec_()    
        else:
            error_msg = QMessageBox()
            error_msg.setText(f"Flight From : {self.From_edit.currentText()} TO: {self.To_edit.currentText()} is not available ")
            error_msg.exec_()
            self.flag=1
       


    def booked(self):
        if self.name_edit.text() == "":
            # Display an error message
            error_msg = QMessageBox()
            error_msg.setText("Please enter your full name.")
            error_msg.exec_()
        elif self.email_edit.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your Email.")
            error_msg.exec_()

        elif self.cnic.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please confirm your CNIC.")
            error_msg.exec_()

        elif self.country_edit.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your Country name.")
            error_msg.exec_()
        elif self.phone_edit.text()=="":
            error_msg = QMessageBox()
            error_msg.setText("Please enter your Phone number.")
            error_msg.exec_()

        elif self.city_edit.toPlainText()=="":
            error_msg = QMessageBox()
            error_msg.setText("Enter your Address   .")
            error_msg.exec_()
        elif self.Passangers.text()=="0":
            error_msg = QMessageBox()
            error_msg.setText("Enter the seats you want to book    .")
            error_msg.exec_()
        


            
        
        elif self.flag==1:
            error_msg = QMessageBox()
            error_msg.setText(f"Flight From : {self.From_edit.currentText()} TO: {self.To_edit.currentText()} is not available ")
            error_msg.exec_()

        else:
            International_flight_booking.L1.append(self.name_edit.text())
            International_flight_booking.L1.append(self.From_edit.currentText())
            International_flight_booking.L1.append(self.To_edit.currentText())
            International_flight_booking.L1.append(self.class_edit.currentText())
            International_flight_booking.L1.append(int(self.Passangers.text()))
            International_flight_booking.l3.append(int(self.Passangers.text()))
           
         

            self.obj=FlightIdDialog2()



class FlightIdDialog2(International_flight_booking):
    def __init__(self):
        super().__init__()
        # Create label and line edit widgets for flight ID
        self.flight_id_label = QLabel("Enter Flight ID:")
        self.flight_id_edit = QLineEdit()
        print(International_flight_booking.L1)
        # Create confirmation button
        self.confirm_button = QPushButton("Confirm")
        
        self.confirm_button.clicked.connect(self.confirm)
        self.setFixedSize(300,200)
        

        self.form_layout=QFormLayout()
        self.form_layout.addRow(self.flight_id_label,self.flight_id_edit)
        self.form_layout.addRow("      ",self.confirm_button)
        self.container2 = QWidget(self)
        self.container2.setLayout(self.form_layout)
        self.setCentralWidget(self.container2)
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
            }""")

        self.show()
    def confirm(self ):
        mycursor.execute(f"SELECT Flight_status FROM international_flight_schedules WHERE Flight_number='{self.flight_id_edit.text()}'")

        # Fetch all the rows returned by the query
        data = mycursor.fetchall()

        if self.flight_id_edit.text() in International_flight_booking.my_list:
            if data[0][0] == "Active":

        
            
                if International_flight_booking.L1[3]=="Economy":
    
    
                    query = f"""INSERT INTO booking_information (User_name, Flight_no, Name, `From`, Departure_date, departure_time, `To`, Arrival_time, Arrival_date, Class, Seats, price)
                    SELECT new_table.user_name, '{self.flight_id_edit.text()}', '{International_flight_booking.L1[0]}', '{International_flight_booking.L1[1]}', international_flight_schedules.Depart_date, international_flight_schedules.depart_time, '{International_flight_booking.L1[2]}', international_flight_schedules.Arrival_time, international_flight_schedules.Arrival_date, '{International_flight_booking.L1[3]}', '{International_flight_booking.L1[4]}', {International_flight_booking.L1[4]} * (international_flight_schedules.Economy_price)
                    FROM new_table, international_flight_schedules   
                    WHERE Flight_number = '{self.flight_id_edit.text()}'"""   
        
                    print(1)
                    mycursor.execute(query)
                    seats_booked=International_flight_booking.l3.pop()
    
                    mycursor.execute(f"Update international_flight_schedules set Economy_seats=Economy_seats-{seats_booked}   WHERE Flight_number = '{self.flight_id_edit.text() }' ")
    
    
                    mydb.commit()
                    International_flight_booking.my_list.clear()
                    International_flight_booking.L1.clear()  
                    error_msg = QMessageBox()
                    error_msg.setText("Flight Successfully Booked.")
                    error_msg.exec_()
                    
                    self.close()
                elif International_flight_booking.L1[3]=="Buissness":
                    query = f"""INSERT INTO booking_information (User_name, Flight_no, Name, `From`, Departure_date, departure_time, `To`, Arrival_time, Arrival_date, Class, Seats, price)
                    SELECT new_table.user_name, '{self.flight_id_edit.text()}', '{International_flight_booking.L1[0]}', '{International_flight_booking.L1[1]}', international_flight_schedules.Depart_date, international_flight_schedules.depart_time, '{International_flight_booking.L1[2]}', international_flight_schedules.Arrival_time, international_flight_schedules.Arrival_date, '{International_flight_booking.L1[3]}', '{International_flight_booking.L1[4]}', {International_flight_booking.L1[4]} * (international_flight_schedules.Economy_price*(20/100)+international_flight_schedules.Economy_price)
                    FROM new_table, international_flight_schedules
                    WHERE Flight_number = '{self.flight_id_edit.text()}'""" 
                    print(2)
        
                    mycursor.execute(query)
                    seats_booked=International_flight_booking.l3.pop()
    
                    mycursor.execute(f"Update international_flight_schedules set Buissnes_seats=Buissnes_seats-{seats_booked}   WHERE Flight_number = '{self.flight_id_edit.text() }' ")
    
    
                    mydb.commit()
        
                    International_flight_booking.my_list.clear()
                    International_flight_booking.L1.clear()  
                    error_msg = QMessageBox()
                    error_msg.setText("Flight Successfully Booked.")
                    error_msg.exec_()
                    self.close()
                elif International_flight_booking.L1[3]=="Executive":
                    query = f"""INSERT INTO booking_information (User_name, Flight_no, Name, `From`, Departure_date, departure_time, `To`, Arrival_time, Arrival_date, Class, Seats, price)
                    SELECT new_table.user_name, '{self.flight_id_edit.text()}', '{International_flight_booking.L1[0]}', '{International_flight_booking.L1[1]}', international_flight_schedules.Depart_date, international_flight_schedules.depart_time, '{International_flight_booking.L1[2]}', international_flight_schedules.Arrival_time, international_flight_schedules.Arrival_date, '{International_flight_booking.L1[3]}', '{International_flight_booking.L1[4]}', {International_flight_booking.L1[4]} * (international_flight_schedules.Economy_price*(10/100)+international_flight_schedules.Economy_price)
                    FROM new_table, international_flight_schedules
                    WHERE Flight_number = '{self.flight_id_edit.text()}'""" 
                    print(3)
        
                    mycursor.execute(query)
                    seats_booked=International_flight_booking.l3.pop()
    
                    mycursor.execute(f"Update international_flight_schedules set Exeuctive_seats=Exeuctive_seats-{seats_booked}   WHERE Flight_number = '{self.flight_id_edit.text() }' ")
                    mydb.commit()
        
                    International_flight_booking.my_list.clear()
                    International_flight_booking.L1.clear()
    
                    error_msg = QMessageBox()
                    error_msg.setText("Flight Successfully Booked.")
                    error_msg.exec_()
                    self.close()
             
                      
            
            else:
                error_msg = QMessageBox()
                error_msg.setText("Flight you want to book is delayed ")
                error_msg.exec_()
        else: 
                error_msg = QMessageBox()
                error_msg.setText("invalid flight number entered .")
                error_msg.exec_() 
                 
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Tabs()
    
    window.show()
    
    sys.exit(app.exec_())
