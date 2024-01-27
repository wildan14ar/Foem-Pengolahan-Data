from PyQt5 import QtWidgets, uic
import sys
#Project UAS By Wildan Abdurrasyid and Salsabila laras
from formdatal import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *   
import MySQLdb as mdb

class loginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginApp, self).__init__()
        uic.loadUi('formlogin.ui',self)
        self.signals()

    #fungsi utama
    def signals(self):
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_SignIn.clicked.connect(self.guest)

    #fungsi Login
    def login(self):
        try:
                username = self.lineEdit_username.text()
                password = self.lineEdit_username_3.text()
                con = mdb.connect('localhost', 'root', '', 'formdata')
                cur = con.cursor()
                cur.execute("SELECT Username,Password from user where username like '"+username + "'and password like '"+password+"'")
                result = cur.fetchone()

                if result == None:
                        QMessageBox.information(self,'Information','Failed to Login Incorrect Email & Password')

                else:
                        QMessageBox.information(self,'Information','Login Success You Are Login')
                        self.close()
                        admin.show()

        except mdb.Error as e:
                QMessageBox.information(self,'Information',"tidak tehubung dg database")

    #fungsi Guest
    def guest(self):
        try:
                QMessageBox.information(self,'Information','tehubung dengan database')
                self.close()
                guest.show()
        except:
                QMessageBox.information(self,'Information',"tidak tehubung dg database")

class adminApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(adminApp, self).__init__()
        uic.loadUi('formdata.ui', self)
        self.signals()

    #sinyal bagan utama
    def signals(self):
        self.loadData()
        self.radioButton.toggled.connect(lambda: self.radiol(self.radioButton))
        self.radioButton_2.toggled.connect(lambda: self.radiol(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda: self.radiol(self.radioButton_3))
        self.go.clicked.connect(self.loadData)
        self.apply.clicked.connect(self.addperson)
        self.reset.clicked.connect(self.reseting)
        self.update.clicked.connect(self.updateData)
        self.delete_2.clicked.connect(self.deleteData)

        #menampilkan data
    def loadData(self):
        try:
                sqlcom = self.comsql.text()
                if sqlcom == "":
                        sqlcom = "SELECT * FROM user"
                db = mdb.connect('localhost', 'root', '', 'formdata')
                mycursor = db.cursor()
                self.comsql.setText(sqlcom)
                mycursor.execute(sqlcom)
                myresult = mycursor.fetchall()
                if myresult == ():
                        myresult = (('', '', '', '', '', '', '', '', ''),)
                numrows = len(myresult)
                numcols = len(myresult[0])

                # Set colums and rows in QTableWidget
                self.tableWidget.setColumnCount(numcols)
                self.tableWidget.setRowCount(numrows)

                # Loops to add values into QTableWidget
                for row in range(numrows):
                        for column in range(numcols):
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem((str(myresult[row][column]))))
                self.pilihan()
        except:
                QMessageBox.information(self,'Information','Gagal Memuat data')

    def pilihan(self):
#sinyal bagan utama
def signals(self):
    self.loadData()
    self.radioButton.toggled.connect(lambda: self.radiol(self.radioButton))
    self.radioButton_2.toggled.connect(lambda: self.radiol(self.radioButton_2))
    self.radioButton_3.toggled.connect(lambda: self.radiol(self.radioButton_3))
    self.go.clicked.connect(self.loadData)
    self.apply.clicked.connect(self.addperson)
    self.reset.clicked.connect(self.reseting)
    self.update.clicked.connect(self.updateData)
    self.delete_2.clicked.connect(self.deleteData)

#menampilkan data
def loadData(self):
    try:
        sqlcom = self.comsql.text()
        if sqlcom == "":
            sqlcom = "SELECT * FROM user"
        db = mdb.connect('localhost', 'root', '', 'formdata')
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM user")
        self.comsql.setText(sqlcom)
        mycursor.execute(sqlcom)
        myresult = mycursor.fetchall()
        nal = []
        for i in range(len(myresult)):
                nal.append(str(myresult[i][1]))
        self.comboBox_2.clear()
        self.comboBox_2.addItems(tuple(dict.fromkeys(nal)))

        #gender
    def radiol(self,r):
                global gen
                if r.isChecked() == True:
                        gen = r.text()

        #menambahkan data
    def addperson(self):
        try :
                db = mdb.connect('localhost', 'root', '', 'formdata')
                mycursor = db.cursor()
                sql = "INSERT INTO user (Name, Gender, Birth, Religion, Address, Username, Password, Note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                Name = self.name.text()
                Gender = gen
                Birth = self.dateEdit.date().toPyDate()
                Religion = self.comboBox.currentText()
                Address = self.address.text()
                Username = self.phone.text()
                Password = self.email.text()
                Note = self.note.text()
                mycursor.execute(sql, (Name, Gender, Birth, Religion, Address, Username, Password, Note))
                db.commit()
                self.loadData()
                self.reseting()
        except:
                QMessageBox.information(self,'Information','Gagal menambahkan data')

        #Delete Data
    def deleteData(self):
        try: 
                db = mdb.connect('localhost','root','','formdata')
                mycursor = db.cursor()
                z = self.comboBox_2.currentText()
                mycursor.execute("DELETE FROM user WHERE Name =%s", [z])
                db.commit()
        except:
                QMessageBox.information(self,'Information','Gagal menghapus data')
        if myresult == ():
            myresult = (('', '', '', '', '', '', '', '', ''),)
        numrows = len(myresult)
        numcols = len(myresult[0])

        # Set colums and rows in QTableWidget
        self.tableWidget.setColumnCount(numcols)
        self.tableWidget.setRowCount(numrows)

        # Loops to add values into QTableWidget
        for row in range(numrows):
            for column in range(numcols):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem((str(myresult[row][column]))))
        self.pilihan()
    except:
        self.massage('Gagal Memuat data')

def pilihan(self):
    db = mdb.connect('localhost', 'root', '', 'formdata')
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    nal = []
    for i in range(len(myresult)):
        nal.append(str(myresult[i][1]))
    self.comboBox_2.clear()
    self.comboBox_2.addItems(tuple(dict.fromkeys(nal)))

#gender
def radiol(self,r):
        global gen
        if r.isChecked() == True:
            gen = r.text()

#menambahkan data
def addperson(self):
    try :
        db = mdb.connect('localhost', 'root', '', 'formdata')
        mycursor = db.cursor()
        sql = "INSERT INTO user (Name, Gender, Birth, Religion, Address, Username, Password, Note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        Name = self.name.text()
        Gender = gen
        Birth = self.dateEdit.date().toPyDate()
        Religion = self.comboBox.currentText()
        Address = self.address.text()
        Username = self.phone.text()
        Password = self.email.text()
        Note = self.note.text()
        mycursor.execute(sql, (Name, Gender, Birth, Religion, Address, Username, Password, Note))
        db.commit()
        self.loadData()
        self.reseting()
    except:
        self.massage('Gagal menambahkan data')

        #Update Data
    def updateData(self):     
#Delete Data
def deleteData(self):
    try: 
        db = mdb.connect('localhost','root','','formdata')
        mycursor = db.cursor()
        z = self.comboBox_2.currentText()
        mycursor.execute("SELECT * FROM user WHERE Name IN (%s)",[z])
        myresult = mycursor.fetchall()
        self.name.setText(myresult[0][1])
        self.address.setText(myresult[0][5])
        self.phone.setText(myresult[0][6])
        self.email.setText(myresult[0][7])
        self.note.setText(myresult[0][8])
        self.deleteData()

        #atur ulang form
    def reseting(self):
                self.name.setText("")
                self.address.setText("")
                self.note.setText("")
                self.phone.setText("")
                self.email.setText("")

class guestApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(guestApp, self).__init__()
        uic.loadUi('formguest.ui',self)
        self.signals()

    def signals(self):
                self.loadData()
                self.go.clicked.connect(self.loadData)

    #fungsi pengubungan data
    def loadData(self):
        try:
                sqlcom = self.comsql.text()
                if sqlcom == "":
                        sqlcom = "SELECT * FROM user"
                db = mdb.connect('localhost', 'root', '', 'formdata')
                mycursor = db.cursor()
                self.comsql.setText(sqlcom)
                mycursor.execute(sqlcom)
                myresult = mycursor.fetchall()
                if myresult == ():
                        myresult = (('', '', '', '', '', '', '', '', ''),)
                numrows = len(myresult)
                numcols = len(myresult[0])

                # Set colums and rows in QTableWidget
                self.tableWidget.setColumnCount(numcols)
                self.tableWidget.setRowCount(numrows)

                # Loops to add values into QTableWidget
                for row in range(numrows):
                        for column in range(numcols):
                                if column != 6 and column != 7:
                                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem((str(myresult[row][column]))))
                                else:
                                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(('Akses Tidak di izinkan')))
        except:
                QMessageBox.information(self,'Information','Gagal Memuat data')

        mycursor.execute("DELETE FROM user WHERE Name =%s", [z])
        db.commit()
    except:
        self.massage('Gagal menghapus data')
    self.loadData()

#Update Data
def updateData(self):     
    db = mdb.connect('localhost','root','','formdata')
    mycursor = db.cursor()
    z = self.comboBox_2.currentText()
    mycursor.execute("SELECT * FROM user WHERE Name IN (%s)",[z])
    myresult = mycursor.fetchall()
    self.name.setText(myresult[0][1])
    self.address.setText(myresult[0][5])
    self.phone.setText(myresult[0][6])
    self.email.setText(myresult[0][7])
    self.note.setText(myresult[0][8])
    self.deleteData()

#atur ulang form
def reseting(self):
        self.name.setText("")
        self.address.setText("")
        self.note.setText("")
        self.phone.setText("")
        self.email.setText("")

def massage(self, info):
    msg = QMessageBox()
    msg.setText(info)
    msg.setWindowTitle("Information")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


Ui_Form.signals = signals
Ui_Form.pilihan = pilihan
Ui_Form.loadData = loadData
Ui_Form.addperson = addperson
Ui_Form.deleteData = deleteData
Ui_Form.updateData = updateData
Ui_Form.radiol = radiol
Ui_Form.reseting = reseting
Ui_Form.massage = massage

if __name__ == "__main__":              
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_Form() 
    ui.setupUi(MainWindow) 
    ui.signals()
    MainWindow.show() 
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = loginApp()
    admin = adminApp()
    guest = guestApp()
    login.show()
    app.exec_()
