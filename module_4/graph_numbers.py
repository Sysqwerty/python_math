import networkx as nx
import matplotlib.pyplot as plt


# Граф із назвами вершин — цифрами

G = nx.Graph()  # створити неорієнтований граф
G.add_node(1)  # додати вузол
G.add_nodes_from([2, 3, 4])  # додати вузли
G.add_edge(1, 2)  # додати ребро
G.add_edges_from([(2, 3), (3, 4), (4, 2)])  # додати ребра

print(G.number_of_nodes(), G.number_of_edges())  # кількість вузлів і ребер
print('nodes', G.nodes)  # вузли
print('edges', G.edges)  # ребра
print('adj', G.adj)  # сусіди вершин
print('degree', G.degree)  # степені вершин (кількість ребер вершин)

nx.draw(G, with_labels=True)  # рисувати граф за допомогою matplotlib
plt.show()

# 4 4
# nodes [1, 2, 3, 4]
# edges [(1, 2), (2, 3), (2, 4), (3, 4)]
# adj {1: {2: {}}, 2: {1: {}, 3: {}, 4: {}}, 3: {2: {}, 4: {}}, 4: {3: {}, 2: {}}}
# degree [(1, 1), (2, 3), (3, 2), (4, 2)]
