import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QInputDialog,QLineEdit,QFileDialog, QProgressDialog, QMessageBox
from threading import Thread
from PyQt5.QtCore import pyqtSignal
import PARCEL_query
import Building_query
import AUXILIARY_query
import GCP_query
import Sector_query
import Zone_query
import Append_Process_query
import Pay_Zebt
import QUARTER
import Communication_Net
from Pay_Torpaqlari import Jn_Rn_check_aciklama, Jn_Rn_Cn_null, Check_iha_ha, Pay_Zebt_relation_check, Zebt_Torpaq_check, Find_Tikili_Komekci, Covered_tikili_torpaq,New_Old_Pay,FindDeletePay,Append_check_torpaq_pay,Check_Pay_Zebt,DeleteEmpty_Errors

object1 = PARCEL_query.Parcel
object2 = Building_query.Building
object3 = AUXILIARY_query.AUXILIARY_BUILDING
object4 = GCP_query.Ground_Control
object5 = Sector_query.Sector
object6 = Zone_query.Zone
object7 = Append_Process_query.Append
object8 = Pay_Zebt.Parsel_Zebt
object9 = QUARTER.Quarter
object10 = Communication_Net.Netwrok

object11 = Jn_Rn_check_aciklama.Pay_jnrnaciklama
object12 = Jn_Rn_Cn_null.Pay_jnrncn
object13 = Check_iha_ha.Iha_Ha
object14 = Pay_Zebt_relation_check.Pay_zebt_relcheck
object15 = Zebt_Torpaq_check.Check_ZebtTorpaq
object16 = Find_Tikili_Komekci.check_Tikili_Komekci
object17 = Covered_tikili_torpaq.Covered_tikilitorpaq
object18 = New_Old_Pay.Check_New_Old_Pay
object19 = FindDeletePay.FindDelete_pay
object20 = Append_check_torpaq_pay.Append_check_Process
object21 = Check_Pay_Zebt.Pay_Zebt_check
object22 = DeleteEmpty_Errors.deleteEmpty_layer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAna_s_hif = QtWidgets.QMenu(self.menubar)
        self.menuAna_s_hif.setObjectName("menuAna_s_hif")
        self.menuTEKUIS = QtWidgets.QMenu(self.menubar)
        self.menuTEKUIS.setObjectName("menuTEKUIS")
        self.menuAZCAD = QtWidgets.QMenu(self.menubar)
        self.menuAZCAD.setObjectName("menuAZCAD")
        self.payCheck = QtWidgets.QMenu(self.menubar)
        self.payCheck.setObjectName("payYoxla")
        self.menuK_m_k = QtWidgets.QMenu(self.menubar)
        self.menuK_m_k.setObjectName("menuK_m_k")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStatistika = QtWidgets.QAction(MainWindow)
        self.actionStatistika.setObjectName("actionStatistika")
        
        self.actionUqodiyalara_g_r = QtWidgets.QAction(MainWindow)
        self.actionUqodiyalara_g_r.setObjectName("actionUqodiyalara_g_r")
        self.actionQanunsuz_tikilil_r = QtWidgets.QAction(MainWindow)
        self.actionQanunsuz_tikilil_r.setObjectName("actionQanunsuz_tikilil_r")
        
        self.actionTEKUIS_haz_rlamaq = QtWidgets.QAction(MainWindow)
        self.actionTEKUIS_haz_rlamaq.setObjectName("actionTEKUIS_haz_rlamaq")
        self.actionTEKUIS_yoxlanmas = QtWidgets.QAction(MainWindow)
        self.actionTEKUIS_yoxlanmas.setObjectName("actionTEKUIS_yoxlanmas")
        
        self.actionAZCAD_a_evrilm = QtWidgets.QAction(MainWindow)
        self.actionAZCAD_a_evrilm.setObjectName("actionAZCAD_a_evrilm")
        self.actionAZCAD_yoxlanmas = QtWidgets.QAction(MainWindow)
        self.actionAZCAD_yoxlanmas.setObjectName("actionAZCAD_yoxlanmas")
        
        
        self.actionpayYoxla = QtWidgets.QAction(MainWindow)
        self.actionpayYoxla.setObjectName("Pay_tor_yoxla")
        
        self.actionStatistika_il_ba_l = QtWidgets.QAction(MainWindow)
        self.actionStatistika_il_ba_l.setObjectName("actionStatistika_il_ba_l")
        
        self.actionTEKUIS_il_ba_l = QtWidgets.QAction(MainWindow)
        self.actionTEKUIS_il_ba_l.setObjectName("actionTEKUIS_il_ba_l")
        
        self.actionAZCAD_il_ba_l = QtWidgets.QAction(MainWindow)
        self.actionAZCAD_il_ba_l.setObjectName("actionAZCAD_il_ba_l")
        
        self.menuAna_s_hif.addAction(self.actionStatistika)
        self.menuAna_s_hif.addAction(self.actionUqodiyalara_g_r)
        self.menuAna_s_hif.addAction(self.actionQanunsuz_tikilil_r)
        self.menuTEKUIS.addAction(self.actionTEKUIS_haz_rlamaq)
        self.menuTEKUIS.addAction(self.actionTEKUIS_yoxlanmas)
        self.menuAZCAD.addAction(self.actionAZCAD_a_evrilm)
        self.menuAZCAD.addAction(self.actionAZCAD_yoxlanmas)
        self.payCheck.addAction(self.actionpayYoxla)
        self.menuK_m_k.addAction(self.actionStatistika_il_ba_l)
        self.menuK_m_k.addAction(self.actionTEKUIS_il_ba_l)
        self.menuK_m_k.addAction(self.actionAZCAD_il_ba_l)
        self.menubar.addAction(self.menuAna_s_hif.menuAction())
        self.menubar.addAction(self.menuTEKUIS.menuAction())
        self.menubar.addAction(self.menuAZCAD.menuAction())
        self.menubar.addAction(self.payCheck.menuAction())
        self.menubar.addAction(self.menuK_m_k.menuAction())
        
        
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 600)) 

        self.background_label.setScaledContents(True)  
        self.background_label.setAlignment(QtCore.Qt.AlignCenter)

        self.set_background_image(self.background_label, r"C:\Users\FeqanU\Desktop\new.jpg") 
        
      
        # self.background_label = QtWidgets.QLabel(self.centralwidget)

       
        # self.background_label.setGeometry(QtCore.QRect(0, 0, 2000, 1000))

        
        # self.background_label.setPixmap(QtGui.QPixmap(r"C:\Users\FeqanU\Desktop\3409297.JPG"))

       
        # self.background_label.setAlignment(QtCore.Qt.AlignCenter)

        
        # self.background_label.raise_()
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Avtomatlaşdırılmış informasiya sistemi"))
        self.menuAna_s_hif.setTitle(_translate("MainWindow", "Statistika"))
        self.menuTEKUIS.setTitle(_translate("MainWindow", "TEKUIS"))
        self.menuAZCAD.setTitle(_translate("MainWindow", "AZCAD"))
        self.payCheck.setTitle(_translate("MainWindow", "Pay torpaqları yoxlama"))
        self.menuK_m_k.setTitle(_translate("MainWindow", "Kömək"))
        self.actionStatistika.setText(_translate("MainWindow", "Kateqoriyalara görə"))
        self.actionStatistika.triggered.connect(self.staticskate)
        self.actionUqodiyalara_g_r.setText(_translate("MainWindow", "Uqodiyalara görə"))
        self.actionUqodiyalara_g_r.triggered.connect(self.staticsuqod)
        self.actionQanunsuz_tikilil_r.setText(_translate("MainWindow", "Qanunsuz tikililər"))
        self.actionTEKUIS_haz_rlamaq.setText(_translate("MainWindow", "TEKUIS hazırlamaq"))
        self.actionTEKUIS_haz_rlamaq.triggered.connect(self.tekuisprocess)
        self.actionTEKUIS_yoxlanmas.setText(_translate("MainWindow", "TEKUIS yoxlanması"))
        self.actionTEKUIS_yoxlanmas.triggered.connect(self.checktekuisprocess)
        
        self.actionAZCAD_a_evrilm.setText(_translate("MainWindow", "AZCAD-a çevrilmə"))
        self.actionAZCAD_a_evrilm.triggered.connect(self.azcadprocess)
        self.actionAZCAD_yoxlanmas.setText(_translate("MainWindow", "AZCAD yoxlanması"))
        self.actionAZCAD_yoxlanmas.triggered.connect(self.checktekuisprocess)
        
        self.actionpayYoxla.setText(_translate("MainWindow","Pay Torpaqlarını Yoxla"))
        self.actionpayYoxla.triggered.connect(self.checkpayprocess)
        
        self.actionStatistika_il_ba_l.setText(_translate("MainWindow", "Statistika ilə bağlı"))
        self.actionTEKUIS_il_ba_l.setText(_translate("MainWindow", "TEKUIS ilə bağlı"))
        self.actionAZCAD_il_ba_l.setText(_translate("MainWindow", "AZCAD ilə bağlı"))
        
        
        
    def set_background_image(self, label, path):
        image = QtGui.QPixmap(path)
        label.setPixmap(image.scaled(label.size(), QtCore.Qt.KeepAspectRatio))
        
        
    def resizeEvent(self, event):
        if hasattr(self, 'background_label') and hasattr(self, 'image'):
            self.background_label.setPixmap(self.image.scaled(self.background_label.size(), QtCore.Qt.KeepAspectRatio))




    def staticskate(self):
        Ui_StatisticKate()

    def staticsuqod(self):
        Ui_StaticUqod()

        
    def tekuisprocess(self):
        Ui_TEKUIS()

    def checktekuisprocess(self):
        Ui_CheckTEKUIS()

    def azcadprocess(self):
        Ui_Azcad()

    def checkazcadprocess(self):
        Ui_CheckAZCAD()
        
        
    def checkpayprocess(self):
        Ui_CheckPay()



class Ui_TEKUIS(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(50, 60, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 120, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 121, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(40, 260, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 260, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(50, 200, 331, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "TEKUIS məlumat bazasının hazırlanması"))
        self.label.setText(_translate("Dialog", "Aralıq baza"))
        self.pushButton.setText(_translate("Dialog", "Daxil et"))
        self.label_2.setText(_translate("Dialog", "Nəticələr üçün baza"))
        self.pushButton_2.setText(_translate("Dialog", "Daxil et"))
        self.checkBox.setText(_translate("Dialog", "\"Readme\" fayl yarat"))
        self.pushButton_3.setText(_translate("Dialog", "Prosesə başla"))

class Ui_CheckTEKUIS(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(50, 60, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 120, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 121, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(40, 260, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 260, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(50, 200, 331, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "TEKUIS məlumat bazasının yoxlanması"))
        self.label.setText(_translate("Dialog", "Aralıq baza"))
        self.pushButton.setText(_translate("Dialog", "Daxil et"))
        self.label_2.setText(_translate("Dialog", "Nəticələr üçün baza"))
        self.pushButton_2.setText(_translate("Dialog", "Daxil et"))
        self.checkBox.setText(_translate("Dialog", "\"Readme\" fayl yarat"))
        self.pushButton_3.setText(_translate("Dialog", "Prosesə başla"))


class Ui_Azcad(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
        
    def start_process(self):
        base_data_path = self.lineEdit.text()
        azcad_data_base = self.lineEdit_2.text()
        uqodiya_data_base = self.lineEdit_3.text()
        output_data_path = self.lineEdit_4.text()
        checkbox_value = self.checkBox.isChecked()
        if os.path.exists(base_data_path) and os.path.exists(azcad_data_base) and os.path.exists(uqodiya_data_base) and os.path.exists(output_data_path):
            # progress penceresi
            self.progress_dialog = QProgressDialog(self)
            self.progress_dialog.setWindowTitle("proses penceresi")
            self.progress_dialog.setLabelText("Proses davam edir")
            self.progress_dialog.setCancelButtonText("Imtina")
            self.progress_dialog.setRange(0, 0)
        

            # prosesi run_processing-e oturme
            worker_thread = Thread(target=self.run_processing, args=(base_data_path, azcad_data_base, uqodiya_data_base, output_data_path,checkbox_value,self.textBrowser))
            worker_thread.start()
            
            
        elif len(base_data_path)==0:
            info = "Aralıq bazanı daxil edin!"
            self.notification_(info)
            
        elif len(azcad_data_base)==0:
            info = "Azcad bazasını daxil edin!"
            self.notification_(info)
            
        elif len(uqodiya_data_base)==0:
            info = "Uqodiya cədvəlini daxil edin!"
            self.notification_(info)
            
        elif len(output_data_path)==0:
            info = "Çıxış məlumatlarının göndərilməsi üçün baza seçin!"
            self.notification_(info)
            
        elif len(output_data_path)!=0 or len(base_data_path)!=0 or len(azcad_data_base)!=0 or len(uqodiya_data_base)!=0:
            case = {
                base_data_path:'Aralıq baza doğru daxil edilməyib',
                azcad_data_base:'Azcad bazası doğru daxil edilməyib',
                uqodiya_data_base:'Uqodiya bazası doğru daxil edilməyib',
                output_data_path:'Nəticlələrin göndəriləcəyi yer doğru daxil edilməyib'
            }
            for title,notifi in case.items():
                print(title)
                if not os.path.exists(title):
                    print(f"{title} yolu doğru daxil edilməyib")
                    self.notification_(notifi)
                
                
                

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(445, 521)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(50, 60, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 121, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(40, 330, 121, 17))
        self.checkBox.setObjectName("checkBox")
      
        
      
        
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 330, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 121, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 110, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 121, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 230, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 230, 211, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(20, 400, 411, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.raise_()
        
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 91, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Aralıq baza"))
        self.pushButton.setText(_translate("Dialog", "Aralıq baza"))
        self.pushButton.clicked.connect(self.addaraliq)
        self.label_2.setText(_translate("Dialog", "Azcad şablon baza"))
        self.pushButton_2.setText(_translate("Dialog", "Azcad şablon"))
        self.pushButton_2.clicked.connect(self.addazcad)
        self.checkBox.setText(_translate("Dialog", "\"Readme\" fayl yarat"))
        self.pushButton_3.setText(_translate("Dialog", "Prosesə başla"))
        self.pushButton_3.clicked.connect(self.start_process)
        self.label_3.setText(_translate("Dialog", "Alt uqodiya cədvəli"))
        self.pushButton_4.setText(_translate("Dialog", "Alt uqodiya"))
        self.pushButton_4.clicked.connect(self.adduqodiya)
        self.label_4.setText(_translate("Dialog", "Nəticələr üçün baza"))
        self.pushButton_5.setText(_translate("Dialog", "Nəticələr"))
        self.pushButton_5.clicked.connect(self.output)
        self.label_5.setText(_translate("Dialog", "Proses tarixcəsi"))
        
        

        
        
    def notification_(self,info):
        # notification dialog
        notification = QMessageBox()
        notification.setWindowTitle("Xəbərdarlıq")
        notification.setIcon(QMessageBox.Information)
        notification.setText(info)
        notification.setStandardButtons(QMessageBox.Ok)
        notification.exec_()
        
            
            
            

    def run_processing(self, base_data_path, azcad_data_base, uqodiya_data_base, output_data_path, checkbox_value,textBrowser):
        # Prosesler burdan heyata kecirilir
        head_tail = os.path.split(base_data_path)
        head = head_tail[0]
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        
            object1(base_data_path, uqodiya_data_base, output_data_path, checkbox_value,textBrowser,readme,head)
            
            object2(base_data_path, output_data_path,checkbox_value,textBrowser,readme,head)
            
            object3(base_data_path, output_data_path,checkbox_value,textBrowser,readme,head)
                
            object4(base_data_path, output_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head)
            
            object5(base_data_path, output_data_path,checkbox_value,textBrowser,readme,head)
            
            object6(base_data_path, output_data_path,checkbox_value,textBrowser,readme,head)
            
            object7(output_data_path, azcad_data_base,checkbox_value,textBrowser,readme,head)
            
            object9(base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head)
                
            object8(base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head)

            object10(base_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head)
            
            
            
        else:
            object1(base_data_path, uqodiya_data_base, output_data_path, checkbox_value,textBrowser,"text",head)
            
            object2(base_data_path, output_data_path,checkbox_value,textBrowser,"text",head)
            
            object3(base_data_path, output_data_path,checkbox_value,textBrowser,"text",head)
                
            object4(base_data_path, output_data_path,azcad_data_base,checkbox_value,textBrowser,"text",head)
            
            object5(base_data_path, output_data_path,checkbox_value,textBrowser,"text",head)
            
            object6(base_data_path, output_data_path,checkbox_value,textBrowser,"text",head)
            
            object7(output_data_path, azcad_data_base,checkbox_value,textBrowser,"text",head)
            
            object9(base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,"text",head)
                
            object8(base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,"text",head)
                
            object10(base_data_path,azcad_data_base,checkbox_value,textBrowser,"text",head)
        
            
        
        
        
        self.on_process_finished()
        
        
    def on_process_finished(self):
        self.progress_dialog.close()  # Pencereni bagla
        self.pushButton_3.setEnabled(True)
        
        
    def addaraliq(self):
        araliq_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        self.lineEdit.setText(araliq_path)
        
    def addazcad(self):
        azcad_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_2.setText(azcad_path)
        
    def adduqodiya(self):
        uqodiya_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_3.setText(uqodiya_path)
        
    def output(self):
        output = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_4.setText(output)
        
        
class Ui_CheckPay(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
        
        
    def start_pay_process(self):
        base_data_path = self.lineEdit.text()
        error_data_path = self.lineEdit_2.text()
        trash_data_path = self.lineEdit_3.text()
        newpay = self.lineEdit_4.text()
        oldpay = self.lineEdit_5.text()
        itmim = self.lineEdit_6.text()
        checkbox_value = self.checkBox.isChecked()
        
        if os.path.exists(base_data_path) and os.path.exists(error_data_path) and os.path.exists(trash_data_path) and os.path.exists(newpay) and os.path.exists(oldpay) and os.path.exists(itmim):
            # progress penceresi
            self.progress_dialog = QProgressDialog(self)
            self.progress_dialog.setWindowTitle("proses penceresi")
            self.progress_dialog.setLabelText("Proses davam edir")
            self.progress_dialog.setCancelButtonText("Imtina")
            self.progress_dialog.setRange(0, 0)
            
            # prosesi run_processing-e oturme
            worker_thread = Thread(target=self.startcheckpay, args=(base_data_path, error_data_path, trash_data_path, newpay,oldpay,itmim,checkbox_value))
            worker_thread.start()
            
            
        elif len(base_data_path)==0:
            info = "Aralıq bazanı daxil edin!"
            self.notification_(info)
            
        elif len(error_data_path)==0:
            info = "Xətaların göndəriləcəyi bazanı seçin!"
            self.notification_(info)
            
        elif len(trash_data_path)==0:
            info = "Proses zamanı yaranan aralıq laylar üçün bazanı seçin!"
            self.notification_(info)
            
        elif len(newpay)==0:
            info = "Yeni payların göndərilməsi üçün baza!"
            self.notification_(info)
            
        elif len(oldpay)==0:
            info = "Köhnə payların göndərilməsi üçün baza!"
            self.notification_(info)
            
        elif len(itmim)==0:
            info = "İtmim-ə göndəriləcək laylar üçün bazanı seçin!"
            self.notification_(info)
            
        elif len(base_data_path)!=0 or len(error_data_path)!=0 or len(trash_data_path)!=0 or len(newpay)!=0 or len(oldpay)!=0 and len(itmim)!=0:
            case = {
                base_data_path:'Aralıq baza doğru daxil edilməyib',
                error_data_path:'Xətaların göndəriləcəyi bazanı yolunu doğru seçin',
                trash_data_path:'Proses zamanı yaranacaq artıq laylar üçün baza yolu doğru seçin',
                newpay:'Yeni payların göndəriləcəyi bazanı doğru seçin',
                oldpay:'Köhnə payların göndəriləcəyi bazanı doğru seçin',
                itmim:'İTMİM-də silinəcək layların göndərilməsi üçün olan bazanı düzgün seçin'
            }
            for title,notifi in case.items():
                print(title)
                if not os.path.exists(title):
                    print(f"{title} yolu doğru daxil edilməyib")
                    self.notification_(notifi)
    
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(579, 660)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(70, 70, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(320, 70, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 120, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 120, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 421, 351))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 150, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 150, 101, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 221, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 200, 231, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 200, 101, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 231, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 250, 231, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 250, 101, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 231, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 300, 231, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 231, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 300, 101, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(40, 510, 471, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(70, 460, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 450, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 490, 81, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.checkBox.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec()

    def  retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Daxil Et"))
        self.pushButton.clicked.connect(self.addpayaraliq)
        self.pushButton_2.setText(_translate("Dialog", "Daxil Et"))
        self.pushButton_2.clicked.connect(self.addoutput)
        self.groupBox.setTitle(_translate("Dialog", "Daxil etmələr"))
        self.label.setText(_translate("Dialog", "Aralıq baza"))
        self.label_2.setText(_translate("Dialog", "Xətaların göndəriləcəyi baza"))
        self.pushButton_4.setText(_translate("Dialog", "Daxil Et"))
        self.pushButton_4.clicked.connect(self.addtrash)
        self.label_4.setText(_translate("Dialog", "Aralıq laylar üçün baza"))
        self.pushButton_5.setText(_translate("Dialog", "Daxil Et"))
        self.pushButton_5.clicked.connect(self.addnewpay)
        self.label_5.setText(_translate("Dialog", "Yeni paylar üçün baza"))
        self.pushButton_6.setText(_translate("Dialog", "Daxil Et"))
        self.pushButton_6.clicked.connect(self.addoldpay)
        self.label_6.setText(_translate("Dialog", "Köhnə paylar üçün baza"))
        self.label_7.setText(_translate("Dialog", "ITMIM-də silinəcəklər"))
        self.pushButton_7.setText(_translate("Dialog", "Daxil Et"))
        self.pushButton_7.clicked.connect(self.additmim)
        self.checkBox.setText(_translate("Dialog", "\"Readme\" fayl yarat"))
        self.pushButton_3.setText(_translate("Dialog", "Prosesə başla"))
        self.pushButton_3.clicked.connect(self.start_pay_process)
        self.label_3.setText(_translate("Dialog", "Proses tarixcəsi"))
        
        
    def notification_(self,info):
        # notification dialog
        notification = QMessageBox()
        notification.setWindowTitle("Xəbərdarlıq")
        notification.setIcon(QMessageBox.Information)
        notification.setText(info)
        notification.setStandardButtons(QMessageBox.Ok)
        notification.exec_()
        
        
    def addpayaraliq(self):
        araliq_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        self.lineEdit.setText(araliq_path)
        
    def addoutput(self):
        output = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_2.setText(output)  
    
    def addtrash(self):
        output = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_3.setText(output)
        
    def addnewpay(self):
        output = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_4.setText(output)
        
        
    def additmim(self):
        output = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_6.setText(output)
        
        
    def addoldpay(self):
        output = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecet File Geodatabse')
        
        self.lineEdit_5.setText(output)
        
        
    def startcheckpay(self,base_data_path, error_data_path, trash_data_path, newpay, oldpay,itmim,checkbox_value):
        
        head_tail = os.path.split(base_data_path)
        head = head_tail[0]
        
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        
        
        
        object11(base_data_path,error_data_path)
        object12(base_data_path,error_data_path)
        object13(base_data_path,error_data_path)
        object14(base_data_path,error_data_path)
        object15(base_data_path,error_data_path,trash_data_path)
        object16(base_data_path,error_data_path)
        object17(base_data_path,error_data_path)
        object18(base_data_path,error_data_path,trash_data_path,newpay,oldpay)
        object19(base_data_path,error_data_path,trash_data_path,newpay,oldpay,itmim)
        object20(base_data_path,error_data_path,trash_data_path,newpay,oldpay)
        object21(base_data_path,error_data_path,trash_data_path)
        object22(error_data_path)
        
        readme.close()
        
        self.on_process_finished()
        
        
    def on_process_finished(self):
        self.progress_dialog.close()  # Pencereni bagla
        self.pushButton_3.setEnabled(True)

class Ui_CheckAZCAD(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 40, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 120, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 131, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(40, 260, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 260, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(50, 200, 331, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "AZCAD məlumat bazasının yoxlanması"))
        self.label.setText(_translate("Dialog", "AZCAD məlumat bazası"))
        self.pushButton.setText(_translate("Dialog", "Daxil et"))
        self.label_2.setText(_translate("Dialog", "Xətaların göndəriləcəyi yer"))
        self.pushButton_2.setText(_translate("Dialog", "Daxil et"))
        self.checkBox.setText(_translate("Dialog", "\"Readme\" fayl yarat"))
        self.pushButton_3.setText(_translate("Dialog", "Prosesə başla"))



class Ui_StatisticKate(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(432, 365)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(40, 200, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 180, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 110, 141, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 111, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 131))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(40, 240, 191, 17))
        self.checkBox.setObjectName("checkBox")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 231, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 320, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 361, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()
        self.checkBox.raise_()
        self.progressBar.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Kateqoriyalar üzrə statistika"))
        self.comboBox.setItemText(0, _translate("Dialog", "Kənd təsərrüfatı təyinatlı torpaqlar"
                                                ""))
        self.comboBox.setItemText(1, _translate("Dialog", "Yaşayış məntəqələrinin torpaqları"
                                                ""))
        self.comboBox.setItemText(2, _translate("Dialog", "Sənaye, nəqliyyat, rabitə, müdafiə və digər təyinatlı torpaqlar"
                                                ""))
        self.comboBox.setItemText(3, _translate("Dialog", "Xüsusi qorunan ərazilərin torpaqları"
                                                ""))
        self.comboBox.setItemText(4, _translate("Dialog", "Meşə fondu torpaqları"
                                                ""))
        self.comboBox.setItemText(5, _translate("Dialog", "Su fondu torpaqları"
                                                ""))
        self.comboBox.setItemText(6, _translate("Dialog", "Ehtiyat fondu torpaqları"
                                                ""))
        self.label.setText(_translate("Dialog", "Kateqoriyalar"))
        self.label_2.setText(_translate("Dialog", "Məlumat bazası"))
        self.pushButton.setText(_translate("Dialog", "Daxil et"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "AZCAD"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "TEKUIS"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Aralıq"))
        self.label_3.setText(_translate("Dialog", "Məlumat bazasının tipi"))
        self.groupBox.setTitle(_translate("Dialog", "Məlumat bazası"))
        self.checkBox.setText(_translate("Dialog", "Bütün kateqoriyalar üzrə statistika"))
        self.pushButton_2.setText(_translate("Dialog", "Prosesə başla"))
        self.groupBox_2.setTitle(_translate("Dialog", "Statistik məlumatların seçimi"))

class Ui_StaticUqod(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(578, 350)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 50, 81, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(320, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(50, 230, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 130, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 111, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 411, 141))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(50, 270, 131, 17))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 210, 291, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 240, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(30, 310, 291, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 310, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.checkBox.raise_()
        self.pushButton_2.raise_()
        self.progressBar.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Uqodiyalar üzrə hesabat"))
        self.label.setText(_translate("Dialog", "Məlumat bazası"))
        self.pushButton.setText(_translate("Dialog", "Daxil et"))
        self.comboBox.setItemText(0, _translate("Dialog", "Bağlar"))
        self.comboBox.setItemText(1, _translate("Dialog", "Bataqlı örüş"))
        self.comboBox.setItemText(2, _translate("Dialog", "Bataqlıqlar"))
        self.comboBox.setItemText(3, _translate("Dialog", "Bənd"))
        self.comboBox.setItemText(4, _translate("Dialog", "Biçənək"))
        self.comboBox.setItemText(5, _translate("Dialog", "Bostanlar"))
        self.comboBox.setItemText(6, _translate("Dialog", "Çay plantasiyaları"))
        self.comboBox.setItemText(7, _translate("Dialog", "Çaylar və arxlar"))
        self.comboBox.setItemText(8, _translate("Dialog", "Çoxillik əkmələr"))
        self.comboBox.setItemText(9, _translate("Dialog", "Daşlı kolluq"))
        self.comboBox.setItemText(10, _translate("Dialog", "Daşlı örüş"))
        self.comboBox.setItemText(11, _translate("Dialog", "Daşlıq, çınqıllıq"))
        self.comboBox.setItemText(12, _translate("Dialog", "Dəniz və göllər"))
        self.comboBox.setItemText(13, _translate("Dialog", "Dinc"))
        self.comboBox.setItemText(14, _translate("Dialog", "Əkin"))
        self.comboBox.setItemText(15, _translate("Dialog", "Kanallar"))
        self.comboBox.setItemText(16, _translate("Dialog", "Karxana"))
        self.comboBox.setItemText(17, _translate("Dialog", "Kollektorlar"))
        self.comboBox.setItemText(18, _translate("Dialog", "Kollu biçənək"))
        self.comboBox.setItemText(19, _translate("Dialog", "Kollu örüş"))
        self.comboBox.setItemText(20, _translate("Dialog", "Kolluqlar"))
        self.comboBox.setItemText(21, _translate("Dialog", "Lilliklər"))
        self.comboBox.setItemText(22, _translate("Dialog", "Meşə ilə örtülü sahələr"))
        self.comboBox.setItemText(23, _translate("Dialog", "Meşə ilə örtüsüz sahələr"))
        self.comboBox.setItemText(24, _translate("Dialog", "Meşə zolağı"))
        self.comboBox.setItemText(25, _translate("Dialog", "Meyvə bağları"))
        self.comboBox.setItemText(26, _translate("Dialog", "Parklar, stadionlar"))
        self.comboBox.setItemText(27, _translate("Dialog", "Qamışlı örüş"))
        self.comboBox.setItemText(28, _translate("Dialog", "Qamışlıq"))
        self.comboBox.setItemText(29, _translate("Dialog", "Qəbiristanlıqlar"))
        self.comboBox.setItemText(30, _translate("Dialog", "Qış otlağının k/t-na yararlı hissəsi"))
        self.comboBox.setItemText(31, _translate("Dialog", "Qobu, yarğan, dərə və sair torpaq"))
        self.comboBox.setItemText(32, _translate("Dialog", "Qumluq"))
        self.comboBox.setItemText(33, _translate("Dialog", "Su anbarları, nohurlar"))
        self.comboBox.setItemText(34, _translate("Dialog", "Şoran örüş"))
        self.comboBox.setItemText(35, _translate("Dialog", "Şoranlıq"))
        self.comboBox.setItemText(36, _translate("Dialog", "Təhsil, səhiyyə, mədəniyyət, nəqliyyat, rabitə və digər sosial və ictimai tikinti altında olan torpaqlar "))
        self.comboBox.setItemText(37, _translate("Dialog", "Təmiz örüş"))
        self.comboBox.setItemText(38, _translate("Dialog", "Tikinti altında olan torpaqlar"))
        self.comboBox.setItemText(39, _translate("Dialog", "Tut bağları"))
        self.comboBox.setItemText(40, _translate("Dialog", "Üzümlüklər"))
        self.comboBox.setItemText(41, _translate("Dialog", "Yararsız"))
        self.comboBox.setItemText(42, _translate("Dialog", "Yay otlağının k/t-na yararlı hissəsi"))
        self.comboBox.setItemText(43, _translate("Dialog", "Yollar və küçələr"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "AZCAD"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "TEKUIS"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Aralıq"))
        self.label_2.setText(_translate("Dialog", "Məlumat bazasının tipi"))
        self.groupBox.setTitle(_translate("Dialog", "Məlumat bazası və tipi"))
        self.checkBox.setText(_translate("Dialog", "Bütün uqodiyalar üzrə"))
        self.groupBox_2.setTitle(_translate("Dialog", "Statistik məlumatların seçimi"))
        self.pushButton_2.setText(_translate("Dialog", "Detallı statistika"))
        self.pushButton_3.setText(_translate("Dialog", "Prosesə başla"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
