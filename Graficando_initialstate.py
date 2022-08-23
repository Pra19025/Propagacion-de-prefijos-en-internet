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


# Busco graficar todo lo que sale del AS indicado


global ip, start_time, end_time, ASN_event
ip = '168.234.49.0'
start_time = '2022-08-20T12:35:31'
end_time = '2022-08-20T15:22:01'
result = []
result_event = []
ASN_event = 8298

#print(ASN_event)

time_stamp = 0
url = 'https://stat.ripe.net/data/bgplay/data.json?resource={}'.format(
ip)+'&starttime='+start_time+'&endtime='+end_time

print(url)
resp = requests.get(url)


initial_state = len(resp.json()['data']['initial_state'])
print(initial_state)
routes = len(resp.json()['data']['initial_state'][0]['path'])
events = len(resp.json()['data']['events'])

G_event = nx.MultiGraph()
temporal_event = []
guardar = []

for y in range (initial_state):
    a = 0
    path = resp.json()['data']['initial_state'][y]['path']
    for j in range (len(path)):
        if(path[j] == ASN_event):
            print(path)
            for n in range (len(path)-1):
                for k in range (0,2):
                    temporal_event.append(path[n+k])
                G_event.add_edge(temporal_event[1],temporal_event[0])
                temporal_event = []
            
# Lo que busco es que para las posiciones de path que incluyen el ASN indicado, ponerlas en parejas para crear los edges



pos_event = nx.planar_layout(G_event)
nx.draw_networkx_nodes(G_event,pos_event, node_size=50)
nx.draw_networkx_edges(G_event, pos_event, edgelist=G_event.edges(), edge_color='black', width=0.5)
nx.draw_networkx_labels(G_event,pos_event, font_size=8)
plt.show()

