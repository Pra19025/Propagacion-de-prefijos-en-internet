from asyncio.windows_events import NULL
import requests
import networkx as nx
import matplotlib.pyplot as plt
import json
import numpy as np

ip = '181.189.154.29/24'
result = []
AS = []

def RIPE(ip):

    url = 'https://stat.ripe.net/data/ris-peerings/data.json?resource={}'.format(ip)

    resp = requests.get(url)
    
    probe = len(resp.json()['data']['peerings'])
    peerings = len(resp.json()['data']['peerings'][0]['peers'])
    routes = len(resp.json()['data']['peerings'][0]['peers'][0]['routes'][0]['as_path'])
    for i in range (probe):
        peerings = len(resp.json()['data']['peerings'][i]['peers'])
        for j in range (peerings):
            routes = len(resp.json()['data']['peerings'][i]['peers'][j]['routes'])    
            for k in range (routes):
                AS = resp.json()['data']['peerings'][i]['peers'][j]['routes'][k]['as_path']
                result.append(AS)
    G = nx.MultiGraph()
    temporal = []

    print(result[0])

    for i in range (len(result)):
        for j in range (len(result[i])-1):    
            for k in range (0,2):
                try:
                    temporal.append(result[i][k+j])
                except:
                    print("NEL")
            try:
                #print(temporal)
                G.add_edge(temporal[1],temporal[0])
            except:
                print("Nel")
            temporal = []

    for i in range (len(result)):
        G.add_nodes_from(result[i])


    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos, node_size=50)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', width=0.5)
    nx.draw_networkx_labels(G,pos, font_size=8)
    plt.show()
    return

RIPE(ip)






