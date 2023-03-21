#finds the nodes at distance 1 then finds the nodes at distance 2
def bfs(graph,root):
    queue=[]
    discovered=[False]*len(graph.data)
    distance=[None]*len(graph.data)
    parent=[None]*len(graph.data)


    discovered[root]=True
    queue.append(root)
    idx=0
    distance[root]=0

    while idx<len(queue):#deque operation
        current=queue[idx]
        idx+=1

        #check all current edges
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node]=1+distance[current]
                parent[node]=current
                discovered[node]=True
                queue.append(node)

    return queue,distance,parent


