from asyncio.windows_events import NULL
from datetime import datetime
from tracemalloc import start
import requests
import networkx as nx
import matplotlib.pyplot as plt
import json
import numpy as np
from re import X
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from datetime import datetime
from networkx import *

global ip, start_time, end_time, ASN_event
ip = '181.189.154.29/24'
start_time = '1660474800'
end_time = '1660476600'
result = []
result_event = []
ASN_event = 3280




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 0, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 110, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(260, 260, 133, 0))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        #self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(60, 380, 651, 41))
        # font = QtGui.QFont()
        # font.setFamily("Consolas")
        # font.setPointSize(11)
        # font.setKerning(True)
        # # self.pushButton_3.setFont(font)
        # self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.pushButton_3.setObjectName("pushButton_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 120, 86, 61))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(120, 120, 133, 60))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 430, 651, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setGeometry(QtCore.QRect(260, 270, 151, 51))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.splitter_5)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.splitter_5)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        # self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QtCore.QRect(590, 220, 101, 61))
        # self.pushButton_4.setObjectName("pushButton_4")


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 510, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,     0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Código de las acciones de la interfaz
        #global ip 
        
        self.pushButton.clicked.connect(self.RIPE)
        self.pushButton_2.clicked.connect(self.Cambios_anuncios)

        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())

    # Funciones de la interfaz:

    # Para el primer inciso:

    def RIPE(self):
        result = []
        global ip
        ip = self.lineEdit.text()

        AS = []
        url = 'https://stat.ripe.net/data/ris-peerings/data.json?resource={}'.format(ip)
        print(url)
        resp = requests.get(url)
        #print(resp.text)

        probe = len(resp.json()['data']['peerings'])
        peerings = len(resp.json()['data']['peerings'][0]['peers'])
        routes = len(resp.json()['data']['peerings'][0]
                     ['peers'][0]['routes'][0]['as_path'])
        for i in range(probe):
            peerings = len(resp.json()['data']['peerings'][i]['peers'])
            for j in range(peerings):
                routes = len(resp.json()['data']['peerings']
                             [i]['peers'][j]['routes'])
                for k in range(routes):
                    AS = resp.json()[
                        'data']['peerings'][i]['peers'][j]['routes'][k]['as_path']
                    result.append(AS)
        G = nx.MultiGraph()
        temporal = []

        print(result[0])

        for i in range(len(result)):
            for j in range(len(result[i])-1):
                for k in range(0, 2):
                    try:
                        temporal.append(result[i][k+j])
                    except:
                        print("NEL")
                try:
                    # print(temporal)
                    G.add_edge(temporal[1], temporal[0])
                except:
                    print("Nel")
                temporal = []

        for i in range(len(result)):
            G.add_nodes_from(result[i])

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=50)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(),
                               edge_color='black', width=0.5)
        nx.draw_networkx_labels(G, pos, font_size=8)
        plt.show()

    def Cambios_anuncios(self):

        global start_time, end_time, ip, ASN_event
        ip = self.lineEdit.text()
        start_time =self.dateTimeEdit.text()
        end_time = self.dateTimeEdit_2.text()     
        ASN_event = int(self.lineEdit_2.text())  

        # ip = '168.234.49.0'
        # ASN_event = 8298
        # start_time = '2022-08-20T12:35:31'
        # end_time = '2022-08-20T15:22:01'

        time_stamp = 0
        url = 'https://stat.ripe.net/data/bgplay/data.json?resource={}'.format(
            ip)+'&starttime='+start_time+'&endtime='+end_time

        print(url)
        resp = requests.get(url)
    

        initial_state = len(resp.json()['data']['initial_state'])
        routes = len(resp.json()['data']['initial_state'][0]['path'])
        events = len(resp.json()['data']['events'])

        temporal_initial = []
        G_event = nx.DiGraph()
        temporal_event = []
        guardar = []

          

        for i in range (events):


            for y in range (initial_state):
                a = 0
                path = resp.json()['data']['initial_state'][y]['path']
                for j in range (len(path)):
                    if(path[j] == ASN_event):
                        #print(path)
                        for n in range (len(path)-1):
                            for k in range (0,2):
                                temporal_event.append(path[n+k])
                            G_event.add_edge(temporal_event[1],temporal_event[0], color = 'red')
                            temporal_event = []

        
            a = 0

            try:
                AS_event = resp.json()['data']['events'][i]['attrs']['path']
            except:
                print('Error')
        
            for j in range (len(AS_event)):   # Se recorren todos los eventos
                #print(AS_event[j])
                if(AS_event[j] == ASN_event):   # Si el evento es el indicado se entra
                    time_stamp = resp.json()['data']['events'][i]['timestamp']
                    self.label_7.setText(time_stamp)
                    print(time_stamp)
                    a = 1
                if(a == 1): # Si el AS era el indicado, se cumple la condición.
                    for k in range (0,2):
                        temporal_event.append(AS_event[j+k-1]) # Se hace un arreglo con el presente y el siguiente AS (en los eventos que incluyen el AS específicado)
                    G_event.add_edge(temporal_event[1], temporal_event[0], color = 'blue')
                    if(temporal_event[0] == ASN_event):
                        guardar = temporal_event
                    #print(temporal_event)
                    temporal_event = []
            if(a == 1):
                pos_event = nx.planar_layout(G_event)
                colors = nx.get_edge_attributes(G_event, 'color').values()

                nx.draw_networkx_nodes(G_event,pos_event, node_size=50)
                nx.draw_networkx_edges(G_event, pos_event, edgelist=G_event.edges(), edge_color=colors)
                nx.draw_networkx_labels(G_event,pos_event, font_size=9)
                plt.draw()
                plt.show()
                
                keyboardClick=False
                while keyboardClick != True:
                    keyboardClick=plt.waitforbuttonpress()
                
                #plt.waitforbuttonpress(-1)
                G_event = create_empty_copy(G_event)
                #print(guardar)
               #G_event.add_edge(guardar[1], guardar[0])
                #G_event.clear()
                plt.close()
                plt.show()
        # except:
            #     print('NEL')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "Propagación de prefijos en internet"))
        self.pushButton.setText(_translate(
            "MainWindow", "Generar diagrama de propagación de prefijo"))
        self.label_4.setText(_translate("MainWindow", "Período de tiempo"))
        self.label_5.setText(_translate("MainWindow", "Tiempo de inicio:"))
        self.label_6.setText(_translate(
            "MainWindow", "Tiempo de finalización:"))
    
        #self.pushButton_3.setText(_translate(
        #    "MainWindow", "Mostrar anuncios de un prefijo hacia un ASN actualmente"))
        self.label_2.setText(_translate("MainWindow", "Prefijo"))
        self.label_3.setText(_translate("MainWindow", "ASN"))
        self.pushButton_2.setText(_translate(
            "MainWindow", "Mostrar cambios de los anuncios de un prefijo hacia un ASN en tiempo definido"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-ddTHH:mm:ss"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy-MM-ddTHH:mm:ss"))
        
        self.label_7.setText(_translate("MainWindow", "Time stamp"))
        #self.pushButton_4.setText(_translate("MainWindow", "➡️"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
