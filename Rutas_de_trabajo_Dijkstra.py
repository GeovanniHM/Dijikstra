import matplotlib.pyplot as plt
import networkx as nx
import random

p1 = random.randint(1,15)
p2 = random.randint(1,15)
p3 = random.randint(1,15)
p4 = random.randint(1,15)
p5 = random.randint(1,15)
p6 = random.randint(1,15)
p7 = random.randint(1,15)
p8 = random.randint(1,15)
p9 = random.randint(1,15)
p10 = random.randint(1,15)
p11 = random.randint(1,15)
p12 = random.randint(1,15)
p13 = random.randint(1,15)
p14 = random.randint(1,15)
p15 = random.randint(1,15)
p16 = random.randint(1,15)
p17 = random.randint(1,15)
p18 = random.randint(1,15)

c1 = random.randint(1,15)
c2 = random.randint(1,15)
c3 = random.randint(1,15)
c4 = random.randint(1,15)
c5 = random.randint(1,15)
c6 = random.randint(1,15)
c7 = random.randint(1,15)
c8 = random.randint(1,15)
c9 = random.randint(1,15)
c10 = random.randint(1,15)
c11 = random.randint(1,15)
c12 = random.randint(1,15)
c13 = random.randint(1,15)
c14 = random.randint(1,15)
c15 = random.randint(1,15)
c16 = random.randint(1,15)
c17 = random.randint(1,15)
c18 = random.randint(1,15)
c19 = random.randint(1,15)
c20 = random.randint(1,15)
c21 = random.randint(1,15)
c22 = random.randint(1,15)
c23 = random.randint(1,15)
c24 = random.randint(1,15)
c25 = random.randint(1,15)
c26 = random.randint(1,15)
c27 = random.randint(1,15)
c28 = random.randint(1,15)
c29 = random.randint(1,15)
c30 = random.randint(1,15)
c31 = random.randint(1,15)
c32 = random.randint(1,15)
c33 = random.randint(1,15)
c34 = random.randint(1,15)
c35 = random.randint(1,15)
c36 = random.randint(1,15)
c37 = random.randint(1,15)
c38 = random.randint(1,15)
c39 = random.randint(1,15)
c40 = random.randint(1,15)
c41 = random.randint(1,15)

nodos = {'DALTON_PATRIA', 'DALTON_VALLARTA', 'DALTON_LMATEOS', 'KIA_MATEOS', 'AUTOLAVADO_MEXICO', 'AUTOLAVADO_CARWASH', 'AUTOLAVADO_JUAN', 'Autolavado_Santos', 'Autolavado_CARHAPPY', 'Autolavado_LasLomas',
         'Limpieza_salas_CLEANER', 'Limpieza_salas_happy', 'Limpieza_salas_Santos', 'Autolavado_brother', 'Limpieza_de_Azulejos', 'Limpieza_de_pisos', 'Limpieza_de_Carros_VIP'}

aristas = [('DALTON_PATRIA', 'Limpieza_de_Carros_VIP', c1), ('Limpieza_de_Carros_VIP', 'AUTOLAVADO_CARWASH', c3),
           ('AUTOLAVADO_CARWASH', 'AUTOLAVADO_JUAN', c9), ('AUTOLAVADO_JUAN', 'Limpieza_de_pisos', c10),
           ('Limpieza_de_pisos', 'Limpieza_de_Azulejos', c12), ('Limpieza_de_Azulejos', 'Autolavado_brother', c11),
           ('Autolavado_brother', 'DALTON_VALLARTA', c8), ('DALTON_VALLARTA', 'Limpieza_salas_Santos', c2),
           ('Limpieza_salas_Santos', 'Limpieza_salas_happy', c4), ('Limpieza_salas_happy', 'DALTON_PATRIA', c6),
           ('DALTON_PATRIA', 'Limpieza_salas_CLEANER', c5), ('Limpieza_salas_CLEANER', 'Limpieza_de_Carros_VIP', c7),
           ('Limpieza_salas_CLEANER', 'AUTOLAVADO_MEXICO', c12), ('AUTOLAVADO_MEXICO', 'AUTOLAVADO_CARWASH', c13), ('AUTOLAVADO_MEXICO', 'AUTOLAVADO_CARWASH', c14),
           ('AUTOLAVADO_MEXICO', 'Autolavado_LasLomas', c15), ('Autolavado_LasLomas', 'AUTOLAVADO_CARWASH', c16), ('Autolavado_LasLomas', 'AUTOLAVADO_JUAN', c17),
           ('Autolavado_LasLomas', 'Limpieza_de_pisos', c18), ('AUTOLAVADO_MEXICO', 'Limpieza_de_Azulejos', c19),
           ('Autolavado_LasLomas', 'Limpieza_de_Azulejos', c20), ('Autolavado_LasLomas', 'DALTON_LMATEOS', c21), ('Limpieza_de_Azulejos', 'DALTON_LMATEOS', c22),
           ('AUTOLAVADO_MEXICO', 'Autolavado_Santos', c23), ('Limpieza_salas_CLEANER', 'Limpieza_salas_happy', c24), ('Limpieza_salas_happy', 'KIA_MATEOS', c25),
           ('Limpieza_salas_CLEANER', 'KIA_MATEOS', c26), ('Autolavado_CARHAPPY', 'KIA_MATEOS', c27), ('Limpieza_salas_CLEANER', 'Autolavado_CARHAPPY', c28), ('DALTON_LMATEOS', 'Autolavado_CARHAPPY', c29),
           ('DALTON_LMATEOS', 'Autolavado_brother', c30), ('Autolavado_CARHAPPY', 'Autolavado_brother', c31), ('Autolavado_Santos', 'Autolavado_CARHAPPY', c32),
           ('Autolavado_CARHAPPY', 'DALTON_VALLARTA', c33), ('KIA_MATEOS', 'DALTON_VALLARTA', c34), ('KIA_MATEOS', 'Limpieza_salas_Santos', c35), ('Autolavado_Santos', 'KIA_MATEOS', c36),
           ('Limpieza_salas_CLEANER', 'Autolavado_Santos', c37), ('Limpieza_salas_CLEANER', 'Autolavado_CARHAPPY', c38), ('Autolavado_Santos', 'DALTON_LMATEOS', c39), ('Limpieza_de_Carros_VIP', 'AUTOLAVADO_MEXICO', c40),
           ('AUTOLAVADO_CARWASH', 'Limpieza_salas_CLEANER', c41)]

G = nx.DiGraph()
G.add_nodes_from(nodos)
G.add_weighted_edges_from(aristas)

pos = {'DALTON_PATRIA': [p1, p2], 'DALTON_VALLARTA': [p2, p3], 'DALTON_LMATEOS': [p3, p4], 'KIA_MATEOS': [p4, p5], 'AUTOLAVADO_MEXICO': [p5, p6],
       'AUTOLAVADO_CARWASH': [p6, p7], 'AUTOLAVADO_JUAN': [p7, p8], 'Autolavado_Santos': [p8, p9], 'Autolavado_CARHAPPY': [p9, p10],
       'Autolavado_LasLomas': [p10, p11], 'Limpieza_salas_CLEANER': [p11, p12], 'Limpieza_salas_happy': [p12, p13], 'Limpieza_salas_Santos': [p13, p14],
       'Autolavado_brother': [p14, p15], 'Limpieza_de_Azulejos': [p15, p16], 'Limpieza_de_pisos': [p16, p17],
       'Limpieza_de_Carros_VIP': [p17, p18]}



weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
nx.draw(G, pos=pos, with_labels=True)
best = nx.dijkstra_path(G, 'Autolavado_LasLomas', 'Limpieza_salas_happy')
print("La mejor ruta es la siguiente : ")
print(best)
best_road = nx.DiGraph()
for i in range(len(best) - 1):
    best_road.add_edge(best[i], best[i + 1])
nx.draw(best_road, pos=pos, with_labels=True, node_size=700, width=5, node_color='#ff1733',
        edge_color='#f0c206')
plt.show()
