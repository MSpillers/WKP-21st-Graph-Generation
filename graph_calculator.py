#class for the graph Nodes, where each Node has an edges attr. for the number of edges it can have
# And a slots attr. for the number of edges it has left available
class Node:
    def __init__(self,id,edges):
        self.id = id
        self.edges = edges
        self.slots = edges

    #returns the number of edges for the Node
    def getNodeEdges(self):
        return self.edges

    #returns the available number of edges for a node
    def getOpenSlots(self):
        return self.slots
    
    #decrements the available number of edges for a node
    def removeSlot(self):
        self.slots = self.slots - 1
    #increments the available number of edges for a node
    def addSlot(self):
        self.slots = self.slots + 1

# class for the graph, where each graph has a list and dictionary of its nodes and the edges between them 
class Graph:
    def __init__(self,n_list):
        self.n_list = n_list
        self.n_dict = {}
    #returns the number of edges for the desired node
    def getEdgeNum(self,n_id):
        node = self.n_list[n_id]
        return node.getNodeEdges()
    #Intializes the graph dictionary with the node list
    def initGraphDict(self):
        n_list = self.n_list
        n_dict = {}
        
        #add the keys to the dictionary
        for i in range(len(n_list)):
            n_dict[i] = []

        #get the index of the last node in the list (will have to subtract by one) 
        l_node = len(n_list)
        #print(l_node)

        # Get available slots for the entire node list
        availSlots = 0
        for i in range(l_node):
            availSlots = availSlots + n_list[i].slots
        
        #first creates an edge to available nodes starting from the first node in the set 
        for i in range(l_node):
            #print(f"Available slots for the set of Nodes:{availSlots}")
            if i < l_node - 1 and n_list[i+1].slots > 0 and n_list[i].slots > 0:
                # print(f"Current node: {n_list[i].id} , Appending to node {n_list[i+1].id}")
                n_dict[i].append(n_list[i+1].id)
                n_list[i].removeSlot()
                availSlots = availSlots - 1
                # print(f"Current node slots left: {n_list[i].slots}")

                n_dict[i+1].append(n_list[i].id)
                n_list[i+1].removeSlot()
                availSlots =  availSlots - 1
        #         print(f"Next node slots left: {n_list[i + 1].slots}")
        # print(f"Available Slots after first pass : {availSlots}")

        #iterate through the list backwards if there are available nodes left,iterating fowards through the list for the nodes 
        #for nodes with available slots
        #Have to check if the node already has an edge 
        if availSlots > 0:
            for i in range(l_node - 1,0,-1):
                while n_list[i].slots > 0:
                    for j in range(l_node):
                        if n_list[j].slots > 0:
                            if j in n_dict[i]:
                                pass
                            else: 
                                if n_list[j].slots > 0 and n_list[i].slots > 0: 
                                    # print(f"Current node: {n_list[i].id} , Appending to node {n_list[j].id}")       
                                    n_dict[i].append(n_list[j].id)
                                    n_list[i].removeSlot()
                                    availSlots = availSlots - 1
                                    # print(f"Current node slots left: {n_list[i].slots}")

                                    # print(f"Next: {n_list[j].id} , Appending to node {n_list[i].id}")   
                                    n_dict[j].append(n_list[i].id)
                                    n_list[j].removeSlot()
                                    availSlots =  availSlots - 1
                                    # print(f"Next node slots left: {n_list[j].slots}")

        #print(f"Available Slots after backwards pass: {availSlots}")

        if availSlots > 0:
            print("No such Graph!")
            self.n_dict = {}
        
        else:
            #Copies the calculated graph to the objects dictionary
            self.n_dict = n_dict

        
    def displayGraphDict(self):
        print(self.n_dict)
        return 0


def driver():   
    #Create the Nodes for Graph One             
    n1 = Node(0,2)
    n2 = Node(1,3)
    n3 = Node(2,2)
    n4 = Node(3,3)
    n5 = Node(4,1)
    n6 = Node(5,1)

    #add them to the node list
    n_list = [n1,n2,n3,n4,n5,n6]

    # for i in range(len(n_list)):
    #     print(f"Info for element: {n_list[i].id}  Edges: {n_list[i].getNodeEdges()} Open Slots: {n_list[i].getOpenSlots()}")

    #Create the graph using the nodes within the Node Lists
    g1 = Graph(n_list)

    #for i in range(len(g1.n_list)):
        #print(f"Node List Info for the Graph Object: {g1.n_list[i].id} Edges: {g1.n_list[i].getNodeEdges()} Open Slots: {g1.n_list[i].getOpenSlots()}")
    
    g1.initGraphDict()
    g1.displayGraphDict()


    return 0


#driver()

            



