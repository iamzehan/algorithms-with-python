graph = {} 
nodes=list(input("What are the name of the Nodes?\n"))
end=nodes.pop(nodes.index(input("Define you finsh Node:\n")))
for i in nodes:
    graph[i]={} 
    neighbors=list(input(f"Neighbors of {i}:\n"))
    for j in neighbors :
        graph[i][j]= int(input(f"Cost {i} -> {j}:\n"))
graph[end]=None
print(graph)
       
