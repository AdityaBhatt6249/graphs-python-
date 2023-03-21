class Graph:
    def __init__(self,num_nodes,edges):

        self.num_nodes=num_nodes
        self.data=[[] for x in range (num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}.{}".format(n,neighbours) for n ,neighbours in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

graph1=Graph(num_nodes,edges)

