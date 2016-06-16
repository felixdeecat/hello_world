# reference from https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html

import matplotlib.pyplot as plt
import networkx as nx
import sys

print sys.argv[1]

#G = nx.read_edgelist("C:\Users\Thomas\Downloads\\brunson_revolution\out.brunson_revolution_revolution",comments="%")
G = nx.read_edgelist(sys.argv[1],comments="%")
H = nx.DiGraph(G)
print H.edges()


num_nodes = G.number_of_nodes()
print num_nodes

#pos = nx.spring_layout(G, iterations = 10)

nx.draw(H)
nx.draw(G)

#==============================================================================
# K_5 = nx.complete_graph(5)
# nx.draw(K_5)
#==============================================================================

plt.show()


#plt.savefig("file_path.png")
