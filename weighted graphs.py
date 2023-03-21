class Graph:
    def __init__(self,num_nodes,edges,directed=None,weighted=None):
        self.num_nodes=num_nodes
        self.directed=directed
        self.weighted=weighted
        self.data=[[]for x in range (num_nodes)]
        self.weight=[[] for x in range (num_nodes)]
        for edge in edges:
            if self.weighted:
                node1,node2,weight=edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)

                #work with weights
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

                #work without weights
    def __repr__(self):
        result=''
        if self.weight:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}:{}\n".format(i, list(zip(nodes, weights)))
        else:
            for i,nodes in enumerate(self.data):
                result+="{}:{}\n".format(i,nodes)
        return result
