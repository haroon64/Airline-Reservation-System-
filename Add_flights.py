from PyQt5 import QtCore
import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDateTimeEdit, QMainWindow,QTabWidget,QTextEdit, QDialog, QGridLayout, QVBoxLayout,QHBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView, QStackedWidget ,QToolTip,QFormLayout
from PyQt5.QtCore import Qt, QDate, QDate,  QTime
from PyQt5.QtGui import QIcon, QImage, QPixmap, QIntValidator
import time



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QVBoxLayout, QDateEdit, QLineEdit, QLabel, \
    QComboBox, QTableWidget, QPushButton, QWidget,QTableWidgetItem, QLineEdit, QRadioButton, QMessageBox, QCheckBox, QCalendarWidget, \
    QTableView



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

      
        self.tabs.addTab(Add_domestic_flights(), "Domestic Flights")
        self.tabs.addTab(Add_international_flights(), "International Flights")
        

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
        self.obj=Admin()
        self.obj.admin()
        self.obj.show()
        Tabs.close(self)

class Add_domestic_flights(QMainWindow):


    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Flights Addition")
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
       
        self.resize(800, 700)
        self.ui()
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
               font-size: 20px;
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



    def ui(self):
        self.departure = QLabel("Departure Location",self)
        

        self.departure_edit = QComboBox(self)
        self.departure_edit.setFixedSize(200, 40)
        self.departure_edit.addItems(["islamabad", "Lahore", "Karrachi", "Peshawer","Sialkot","Faislabad","Multan"])

        self.arrival = QLabel("Arrival: ",self)
        

        self.arrival_edit = QComboBox(self)
        self.arrival_edit.addItems(["islamabad", "Lahore", "Karrachi", "Peshawer", "Sialkot", "Faislabad", "Multan"])


        self.arrival_edit.setFixedSize(200, 40)
        self.economy_seats= QLabel('Economy Seats: ')
        
        self.economy_edit = QLineEdit(self)
        self.economy_edit.setFixedSize(200, 40)
        self.Executive_seats= QLabel('Executive Seats: ')
        
        self.Executive_edit = QLineEdit(self)
        self.Executive_edit.setFixedSize(200, 40)
        self.Buissness_seats= QLabel('Buissness Seats: ')
        
        self.Buissness_edit = QLineEdit(self)
        self.Buissness_edit.setFixedSize(200, 40)
        
        #self.economy_edit.setValidator(QIntValidator())
        self.Executive_edit.setMaxLength(3)
        self.economy_edit.setMaxLength(3)
        self.Buissness_edit.setMaxLength(3)
        self.departure_time = QLabel("Departure Time",self)
        
        self.departure_time_edit = QDateTimeEdit(self)
        self.departure_time_edit.setFixedSize(200, 40)
        self.departure_time_edit.setDisplayFormat("HH:mm:ss")
        self.departure_time_edit.setTime(QTime.currentTime())

        self.arrival_time = QLabel("Arrival Time : ",self)
        
        self.arrival_edit_time = QDateTimeEdit(self)
        self.arrival_edit_time.setFixedSize(200, 40)
        self.arrival_edit_time.setDisplayFormat("HH:mm:ss")
        self.arrival_edit_time.setTime(QTime.currentTime())







        self.departure_date = QLabel("Departure Date", self)
        
        self.departure_date_edit = QDateEdit(self)
        self.departure_date_edit.setFixedSize(200, 40)
        self.arrival_date = QLabel("Arrival Date : ", self)
        
        self.arrival_edit_date = QDateEdit(self)
        self.arrival_edit_date.setFixedSize(200, 40)

        self.departure_date_edit.setCalendarPopup(True)
        self._today_buton = QPushButton('&Today', clicked=self.setToday)
        self.departure_date_edit.calendarWidget().layout().addWidget(self._today_buton)

        self.arrival_edit_date.setCalendarPopup(True)
        self._today_buton1 = QPushButton('&Today', clicked=self.setToday)
        self.arrival_edit_date.calendarWidget().layout().addWidget(self._today_buton1)

        self.status = QLabel('Status: ',self)
        
        self.status_edit = QComboBox(self)
        self.status_edit.addItems(["Active","Delayed"])
        self.status_edit.setFixedSize(200, 40)

        self.flight_no = QLabel('Flight Number : ', self)
        
        self.flight_no_edit = QLineEdit(self)

        
        self.flight_no_edit.setFixedSize(200, 40)

        self.add=QPushButton("ADD Flight")
      
        
        self.add.clicked.connect(self.Add)

       
        
       



        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)



        label.setAlignment(QtCore.Qt.AlignCenter)
        self.price=QLabel("Price of Economy:")
        self.price_edit=QLineEdit(self)
        self.price_edit.setFixedSize(200,40)
        




        self.label=QLabel("ADD Domestic FLights")

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


        self.formlayout1.addRow(self.departure,self.departure_edit)
       
        self.formlayout1.addRow(self.departure_time,self.departure_time_edit)
        
        self.formlayout1.addRow(self.departure_date,self.departure_date_edit)
       
        self.formlayout1.addRow(self.status,self.status_edit)
        
        self.formlayout1.addRow(self.economy_seats,self.economy_edit)
        self.formlayout1.addRow(self.Buissness_seats,self.Buissness_edit)


        self.formlayout2.addRow(self.arrival, self.arrival_edit)
        self.formlayout2.addRow(self.arrival_time, self.arrival_edit_time)
        self.formlayout2.addRow(self.arrival_date, self.arrival_edit_date)
        self.formlayout2.addRow(self.flight_no, self.flight_no_edit)
        self.formlayout2.addRow(self.Executive_seats, self.Executive_edit)
        self.formlayout2.addRow(self.price, self.price_edit)






        self.container = QWidget(self)
        self.container.setLayout(self.Hlayout0)
        
        


        self.Vlayout.addWidget(self.container)
        self.Vlayout.addWidget(self.add)
      
        
        self.container2 = QWidget(self)
        self.container2.setLayout(self.Vlayout)


        self.setCentralWidget(self.container2)












   

    def setToday(self):
        today = QDate().currentDate()
        self.departure_date_edit.calendarWidget().setSelectedDate(today)
        self.arrival_edit_date.calendarWidget().setSelectedDate(today)
        print(type(self.economy_edit))
        self.show()





    def BACK(self):
        admin1.show()
        Add_New_flights.hide(self)

    def Add(self):
        mycursor.execute("Select Flight_number from domestic_flight_schedules ")
        data=mycursor.fetchall()

        l=[item for sublist in data for item in sublist]
        print(l)
        if self.flight_no_edit.text()  in l:
            QMessageBox.warning(self, "Error", "Flight number already reserved : ")



        elif self.departure_edit.currentText() == self.arrival_edit.currentText():
           QMessageBox.warning(self, "Error", "Departure and arrival dates cannot be the same.")
       


        elif self.departure_time_edit.time() == self.arrival_edit_time.time():
            QMessageBox.warning(self, "Error", "Departure time and Arrival time Can't be same")

        elif self.economy_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Economy Class seats ")

        elif self.Executive_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Executive Class seats ")


        elif self.Buissness_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Buissness Class seats ")

        elif self.price_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Price seat ")
        



        else:
            selected_date = self.departure_date_edit.date()
            datetime_obj = selected_date.toPyDate()
            formatted_date1 = datetime_obj.strftime("%Y-%m-%d")

            selected_date = self.arrival_edit_date.date()
            datetime_obj = selected_date.toPyDate()
            formatted_date2 = datetime_obj.strftime("%Y-%m-%d")

            selected_time = self.departure_time_edit.time()
            time_string1 = selected_time.toString("HH:mm:ss")

            selected_time = self.arrival_edit_time.time()
            time_string2 = selected_time.toString("HH:mm:ss")
            


            mycursor.execute(f"INSERT INTO domestic_flight_schedules (Flight_number, `From`, Depart_date, depart_time, Arrival_date, Arrival_time, `To`, \
            Flight_status, Economy_seats, Exeuctive_seats, Buissnes_seats, Economy_price) \
            VALUES ('{self.flight_no_edit.text()}', '{self.departure_edit.currentText()}', '{formatted_date1}', \
            '{time_string1}', '{formatted_date2}', '{time_string1}', \
            '{self.arrival_edit.currentText()}', '{self.status_edit.currentText()}', {int(self.economy_edit.text())}, \
            {int(self.Executive_edit.text())}, {int(self.Buissness_edit.text())}, {int(self.price_edit.text())})")

            mydb.commit()
            error_msg = QMessageBox()
            error_msg.setText("Flight added successfully.")
            error_msg.exec_()


class Add_international_flights(QMainWindow):


    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Flights Addition")
        self.setWindowIcon(QIcon("istockphoto-1137971264-612x612.jpg"))
        self.resize(800, 700)
        self.ui()
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
               font-size: 20px;
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



    def ui(self):
        self.departure = QLabel("Departure Location",self)
        

        self.departure_edit = QComboBox(self)
        self.departure_edit.setFixedSize(200, 40)
        self.departure_edit.addItems([
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
            
    


        self.arrival = QLabel("Arrival: ",self)
        

        self.arrival_edit = QComboBox(self)
        self.arrival_edit.addItems([
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


        self.arrival_edit.setFixedSize(200, 40)
        self.economy_seats= QLabel('Economy Seats: ')
        
        self.economy_edit = QLineEdit(self)
        self.economy_edit.setFixedSize(200, 40)
        self.Executive_seats= QLabel('Executive Seats: ')
        
        self.Executive_edit = QLineEdit(self)
        self.Executive_edit.setFixedSize(200, 40)
        self.Buissness_seats= QLabel('Buissness Seats: ')
        
        self.Buissness_edit = QLineEdit(self)
        self.Buissness_edit.setFixedSize(200, 40)
        
        #self.economy_edit.setValidator(QIntValidator())
        self.Executive_edit.setMaxLength(3)
        self.economy_edit.setMaxLength(3)
        self.Buissness_edit.setMaxLength(3)
        self.departure_time = QLabel("Departure Time",self)
        
        self.departure_time_edit = QDateTimeEdit(self)
        self.departure_time_edit.setFixedSize(200, 40)
        self.departure_time_edit.setDisplayFormat("HH:mm:ss")
        self.departure_time_edit.setTime(QTime.currentTime())

        self.arrival_time = QLabel("Arrival Time : ",self)
        
        self.arrival_edit_time = QDateTimeEdit(self)
        self.arrival_edit_time.setFixedSize(200, 40)
        self.arrival_edit_time.setDisplayFormat("HH:mm:ss")
        self.arrival_edit_time.setTime(QTime.currentTime())







        self.departure_date = QLabel("Departure Date", self)
        
        self.departure_date_edit = QDateEdit(self)
        self.departure_date_edit.setFixedSize(200, 40)
        self.arrival_date = QLabel("Arrival Date : ", self)
        
        self.arrival_edit_date = QDateEdit(self)
        self.arrival_edit_date.setFixedSize(200, 40)

        self.departure_date_edit.setCalendarPopup(True)
        self._today_buton = QPushButton('&Today', clicked=self.setToday)
        self.departure_date_edit.calendarWidget().layout().addWidget(self._today_buton)

        self.arrival_edit_date.setCalendarPopup(True)
        self._today_buton1 = QPushButton('&Today', clicked=self.setToday)
        self.arrival_edit_date.calendarWidget().layout().addWidget(self._today_buton1)

        self.status = QLabel('Status: ',self)
        
        self.status_edit = QComboBox(self)
        self.status_edit.addItems(["Active","Delayed"])
        self.status_edit.setFixedSize(200, 40)

        self.flight_no = QLabel('Flight Number : ', self)
        
        self.flight_no_edit = QLineEdit(self)

        
        self.flight_no_edit.setFixedSize(200, 40)

        self.add=QPushButton("ADD Flight")
      
        
        self.add.clicked.connect(self.Add)

        self.updateComboBox1Items(0)
        
       



        label = QLabel(self)
        pixmap = QPixmap('lgo.jpeg')
        label.setPixmap(pixmap)



        label.setAlignment(QtCore.Qt.AlignCenter)
        self.price=QLabel("Price of Economy:")
        self.price_edit=QLineEdit(self)
        self.price_edit.setFixedSize(200,40)
        




        self.label=QLabel("ADD International FLights")

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


        self.formlayout1.addRow(self.departure,self.departure_edit)
       
        self.formlayout1.addRow(self.departure_time,self.departure_time_edit)
        
        self.formlayout1.addRow(self.departure_date,self.departure_date_edit)
       
        self.formlayout1.addRow(self.status,self.status_edit)
        
        self.formlayout1.addRow(self.economy_seats,self.economy_edit)
        self.formlayout1.addRow(self.Buissness_seats,self.Buissness_edit)


        self.formlayout2.addRow(self.arrival, self.arrival_edit)
        self.formlayout2.addRow(self.arrival_time, self.arrival_edit_time)
        self.formlayout2.addRow(self.arrival_date, self.arrival_edit_date)
        self.formlayout2.addRow(self.flight_no, self.flight_no_edit)
        self.formlayout2.addRow(self.Executive_seats, self.Executive_edit)
        self.formlayout2.addRow(self.price, self.price_edit)




        self.container = QWidget(self)
        self.container.setLayout(self.Hlayout0)
        
        


        self.Vlayout.addWidget(self.container)
        self.Vlayout.addWidget(self.add)
        
        
        self.container2 = QWidget(self)
        self.container2.setLayout(self.Vlayout)


        self.setCentralWidget(self.container2)





        self.departure_edit.currentIndexChanged.connect(self.updateComboBox1Items)




    def updateComboBox1Items(self, index):

            self.arrival_edit.clear()
            l1=['New York', 'Beijing', 'Sydney', 'Tokyo', 'Paris', 'Rome', 'Dubai', 'London','Riyadh', 'Jeddah',]
            l2=['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Sialkot', 'Faisalabad', 'Multan']
            if self.departure_edit.currentText() in l2:
                self.arrival_edit.addItems(l1)
            elif self.departure_edit.currentText() in l1:
                self.arrival_edit.addItems(l2)

    def setToday(self):
        today = QDate().currentDate()
        self.departure_date_edit.calendarWidget().setSelectedDate(today)
        self.arrival_edit_date.calendarWidget().setSelectedDate(today)
        print(type(self.economy_edit))
        self.show()





 
    def Add(self):
        mycursor.execute("Select Flight_number from international_flight_schedules ")
        data=mycursor.fetchall()

        l=[item for sublist in data for item in sublist]
        print(l)
        if self.flight_no_edit.text()  in l:
            QMessageBox.warning(self, "Error", "Flight number already reserved : ")



        elif self.departure_edit.currentText() == self.arrival_edit.currentText():
           QMessageBox.warning(self, "Error", "Departure and arrival dates cannot be the same.")
       


        elif self.departure_time_edit.time() == self.arrival_edit_time.time():
            QMessageBox.warning(self, "Error", "Departure time and Arrival time Can't be same")

        elif self.economy_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Economy Class seats ")

        elif self.Executive_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Executive Class seats ")


        elif self.Buissness_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Buissness Class seats ")

        elif self.price_edit.text()=="":
            QMessageBox.warning(self, "Error", "please enter the number of Price seat ")
        

        else:
            selected_date = self.departure_date_edit.date()
            datetime_obj = selected_date.toPyDate()
            formatted_date1 = datetime_obj.strftime("%Y-%m-%d")

            selected_date = self.arrival_edit_date.date()
            datetime_obj = selected_date.toPyDate()
            formatted_date2 = datetime_obj.strftime("%Y-%m-%d")

            selected_time = self.departure_time_edit.time()
            time_string1 = selected_time.toString("HH:mm:ss")

            selected_time = self.arrival_edit_time.time()
            time_string2 = selected_time.toString("HH:mm:ss")
            


            mycursor.execute(f"INSERT INTO international_flight_schedules (Flight_number, `From`, Depart_date, depart_time, Arrival_date, Arrival_time, `To`, \
            Flight_status, Economy_seats, Exeuctive_seats, Buissnes_seats, Economy_price) \
            VALUES ('{self.flight_no_edit.text()}', '{self.departure_edit.currentText()}', '{formatted_date1}', \
            '{time_string1}', '{formatted_date2}', '{time_string1}', \
            '{self.arrival_edit.currentText()}', '{self.status_edit.currentText()}', {int(self.economy_edit.text())}, \
            {int(self.Executive_edit.text())}, {int(self.Buissness_edit.text())}, {int(self.price_edit.text())})")

            mydb.commit()
            error_msg = QMessageBox()
            error_msg.setText("Flight added successfully.")
            error_msg.exec_()
        
        


            


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window1 = Tabs()
    # window.Sign()
    window1.show()
    sys.exit(app.exec_())
    


