# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:21:11 2016

@author: Thomas
"""

import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns

G = nx.read_edgelist("C:\Users\Thomas\Downloads\\brunson_revolution\out.brunson_revolution_revolution", comments='%')

#G= list(nx.connected_component_subgraphs(G))[0]

num_nodes = G.number_of_nodes()
print num_nodes

pos = nx.spring_layout(G,iterations = 10)
plt.show()