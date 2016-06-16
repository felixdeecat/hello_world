# reference from https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html

import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_edgelist("C:\Users\TJ\GitHub\\brunson_revolution\out.brunson_revolution_revolution",comments="%")
H = nx.DiGraph(G)
H.edges()

num_nodes = G.number_of_nodes()
print num_nodes

#pos = nx.spring_layout(G, iterations = 10)

nx.draw(G)

#==============================================================================
# K_5 = nx.complete_graph(5)
# nx.draw(K_5)
#==============================================================================

plt.show()


#plt.savefig("file_path.png")
