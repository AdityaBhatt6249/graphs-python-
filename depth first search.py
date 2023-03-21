def dfs(graph,root):
    stack=[]
    result=[]
    discovered=[False]*len(graph.data)

    stack.append(root)

    while len(stack)>0:
        current=stack.pop()
        if not discovered current:
            discovered[current] = True
            result.append(current)

            for node in graph.data[current]:#for shortest distance don't use bfs
                if not discovered[node]:
                    stack.append(node)
    return result

