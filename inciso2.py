from logging import NullHandler
from time import time
from tkinter import E
from tkinter.filedialog import SaveFileDialog
import requests
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#Mostrar los cambios de los anuncios de un prefijo hacia un ASN en un 
#período de tiempo específico.  

#prefix refers to the ip subnets it owns
result = []
result_event = []
ASN = 3280
ASN_event = 3280
ip = '181.189.154.0/24'
start_time = '2022-08-13T23:59:40'
end_time = '2022-08-14T00:03:59'
coord_x = []
coord_y = []
cx_event = []
cy_event = []

time_stamp = 0
url = 'https://stat.ripe.net/data/bgplay/data.json?resource={}'.format(ip)+'&starttime='+start_time+'&endtime='+end_time


print(url)
resp = requests.get(url)

initial_state = len(resp.json()['data']['initial_state'])
routes = len(resp.json()['data']['initial_state'][0]['path'])

events = len(resp.json()['data']['events'])


temporal_event = []

for i in range (events):
    a = 0
    G_event = nx.DiGraph()
    # try:
    AS_event = resp.json()['data']['events'][i]['attrs']['path']
    #print(AS_event)

    for j in range (len(AS_event)-1):
        if(AS_event[j] == ASN_event):
            time_stamp = resp.json()['data']['events'][i]['timestamp']
            print(time_stamp)
            
            a = 1
        if(a == 1):
            for k in range (0,2):
                temporal_event.append(AS_event[j+k])
            G_event.add_edge(temporal_event[1], temporal_event[0])
            #print(temporal_event)
            temporal_event = []
    pos_event = nx.planar_layout(G_event)
    nx.draw_networkx_nodes(G_event,pos_event, node_size=50)
    nx.draw_networkx_edges(G_event, pos_event, edgelist=G_event.edges(), edge_color='black', width=0.5)
    nx.draw_networkx_labels(G_event,pos_event, font_size=8)
    plt.show()
    G_event.clear
                
    # except:
    #     print('NEL')





# for i in range (len(result_event)):
#     for j in range (len(result_event[i])):
#         #print(result_event[i][j])
#         if(result_event[i][j] == ASN_event):
#             print('Encontrado')
#             cx_event.append(i)
#             cy_event.append(j)


# for i in range (len(cx_event)):
#     a = 0
#     for j in range ((len(result_event[cx_event[i]])) -1):
#         if ((result_event[cx_event[i]][j]) == ASN_event):
#             #a partir de aquí tengo que comenzar a agregar los edges
#             a = 1
#         if (a == 1):
#             for k in range (0,2):
#                 temporal_event.append(result_event[cx_event[i]][k+j])
#             G_event.add_edge(temporal_event[1], temporal_event[0])
#             print(temporal_event)
#             temporal_event = []

            


    
# for i in range (initial_state):
#     routes = len(resp.json()['data']['initial_state'][i]['path'])
#     AS = resp.json()['data']['initial_state'][i]['path']
#     result.append(AS)




# for i in range (len(result)):
#     for j in range (len(result[i])):
#         #print(result[i][j])
#         if(result[i][j] == ASN):
#             print('Encontrado')
#             coord_x.append(i)
#             coord_y.append(j)

# print('x: ',coord_x)          
# print('y: ',coord_y) 
# print(result[coord_x[0]])


# G = nx.DiGraph()
# temporal = []

# for i in range (len(coord_x)):
#     a = 0
#     for j in range ((len(result[coord_x[i]])) -1):
#         if ((result[coord_x[i]][j]) == ASN):
#             #a partir de aquí tengo que comenzar a agregar los edges
#             a = 1
#         if (a == 1):
#             for k in range (0,2):
#                 temporal.append(result[coord_x[i]][k+j])
#             G.add_edge(temporal[1], temporal[0])
#             #print(temporal)
#             temporal = []




# pos = nx.planar_layout(G)
# nx.draw_networkx_nodes(G,pos, node_size=50)
# nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', width=0.5)
# nx.draw_networkx_labels(G,pos, font_size=8)
# plt.show()
