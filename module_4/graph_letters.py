import networkx as nx
import matplotlib.pyplot as plt


# Граф із назвами вершин — буквами
G = nx.Graph()  # створити неорієнтований граф
G.add_node('a')  # додати вузол
G.add_node('b')  # додати вузол
G.add_node('c')  # додати вузол
G.add_node('d')  # додати вузол
G.add_edge('a', 'b')
G.add_edge('a', 'c')
G.add_edge('b', 'c')
G.add_edge('c', 'd')

print(G.number_of_nodes(), G.number_of_edges())  # кількість вузлів і ребер
print('nodes', G.nodes)  # вузли
print('edges', G.edges)  # ребра
print('adj', G.adj)  # сусіди вершин
print('degree', G.degree)  # степені вершин (кількість ребер вершин)

nx.draw(G, with_labels=True)  # рисувати граф за допомогою matplotlib

plt.show()

# 4 4
# nodes ['a', 'b', 'c', 'd']
# edges [('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd')]
# adj {'a': {'b': {}, 'c': {}}, 'b': {'a': {}, 'c': {}}, 'c': {'a': {}, 'b': {}, 'd': {}}, 'd': {'c': {}}}
# degree [('a', 2), ('b', 2), ('c', 3), ('d', 1)]
