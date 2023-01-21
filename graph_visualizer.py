import graph_calculator as gc
import networkx as nx
import matplotlib.pyplot as plt

class graphVisualization:
    def __init__(self,n_list):
        #stores the list of edges from each node
        self.graph = gc.Graph(n_list)
        self.edges = []

    #adds an edge to the list of edges for the visual
    def addEdge(self):
        graph = self.graph
        graph.initGraphDict()
        for key in graph.n_dict:
            for i in graph.n_dict[key]:
                temp = [key,i]
                self.edges.append(temp)

    def visualize(self):
        graph = nx.Graph()
        graph.add_edges_from(self.edges)
        nx.draw_networkx(graph)
        plt.show()

def driver():
     #Create the Nodes for Graph One             
    n1 = gc.Node(0,3)
    n2 = gc.Node(1,2)
    n3 = gc.Node(2,3)
    n4 = gc.Node(3,3)
    n5 = gc.Node(4,2)
    n6 = gc.Node(5,3)
    n7 = gc.Node(6,3)
    n8 = gc.Node(7,2)
    n9 = gc.Node(8,3)
    n10 = gc.Node(9,3)
    n11 = gc.Node(10,2)
    n12 = gc.Node(11,3)

    #add them to the node list
    n_list = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]

    g1v = graphVisualization(n_list)
 
    g1v.addEdge()

    g1v.visualize()

driver()




