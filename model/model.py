import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.best_sol = None
        self.methods = DAO.get_all_methods()
        self.graph = None

    def build_graph(self, year, method, soglia):
        self.graph = nx.DiGraph()
        nodes = DAO.get_nodes(year, method)
        self.graph.add_nodes_from(nodes)
        for u in self.graph.nodes:
            for v in self.graph.nodes:
                if u != v and float(v.ricavo_tot) >= (1 + soglia) * float(u.ricavo_tot):
                    self.graph.add_edge(u, v)

    def get_graph_details(self):
        return len(self.graph.nodes), len(self.graph.edges)

    def get_piu_redditizi(self):
        sorted_edges = []
        for n in self.graph.nodes:
            if self.get_len_uscenti(n) == 0:
                sorted_edges.append((n, self.get_len_entranti(n)))
        sorted_edges.sort(key=lambda x: x[1], reverse=True)
        piu_redditizi = sorted_edges[:5]
        return piu_redditizi

    def get_len_entranti(self, node):
        return len(list(self.graph.predecessors(node)))

    def get_len_uscenti(self, node):
        return len(list(self.graph.successors(node)))

    def get_percorso(self):
        self.best_sol = []
        nodi_partenza = [n for n in self.graph.nodes if self.get_len_entranti(n) == 0]
        for n in nodi_partenza:
            for s in self.graph.successors(n):
                parziale = [(n, s)]
                self.ricorsione(parziale)
                parziale.pop()
        return self.best_sol

    def ricorsione(self, parziale):
        ultimo = parziale[-1][1]
        if len(parziale) > len(self.best_sol):  # soluzione ottima
            if self.get_len_uscenti(ultimo) == 0:  # soluzione ammissibile
                self.best_sol = copy.deepcopy(parziale)
                print(parziale)
        for s in self.graph.successors(ultimo):
            if (ultimo, s) not in parziale and (s, ultimo) not in parziale:
                parziale.append((ultimo, s))
                self.ricorsione(parziale)
                parziale.pop()
